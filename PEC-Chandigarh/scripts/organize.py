#!/usr/bin/env python3
"""Put every paper in its right place: branch -> semester -> course, with one name per course.

Run after any import (it is idempotent):  python3 scripts/organize.py
It moves files with `git mv`, rewrites the metadata lines of each paper's .md, updates
data/manifest.json, and regenerates INDEX.md, BY-COURSE.md, BY-SEMESTER.md and the
per-department READMEs.

Rules, in order:
 1. FIXES       per-paper corrections (semester / course / code) backed by the paper header.
 2. NAMES       one canonical name per course (spelling variants merged).
 3. CODES       fill in a missing course code where another paper of the same course shows it.
 4. COMMON      first-year (semester 1-2) courses taught to all branches go to COMMON,
                whichever branch happened to upload them ("uploaded under" is kept).
 5. HSM         humanities / management courses (HS*, HSM*, MHN*) from semester 3 on go to HSM.
"""
import collections
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from catalog import DEPARTMENTS  # noqa: E402

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BRANCHES = ["AERO", "CIVIL", "CSE", "CSE-AI", "CSE-DS", "ECE", "EE", "MECH", "META", "PROD", "B-DES"]
OTHER = ["COMMON", "HSM", "MATHS", "CHEMISTRY", "PHYSICS"]
EXAM_LABEL = {
    "MID-SEM": "Mid-Semester", "END-SEM": "End-Semester", "PRACTICAL": "Practical", "QUIZ": "Quiz / Class Test",
    "SESSIONAL": "Sessional Test", "ASSIGNMENT": "Assignment", "UNKNOWN": "Exam (type not stated)",
}

# manifest id (or prefix) -> fields to set, with the evidence
FIXES = {
    "NjxUOChuShG45qReomxt": dict(semester=3, why="header reads Year/Semester 'Second/1st' = semester 3"),
    "QVcoGPMW1FmGIFxRsK1X": dict(semester=3, why="header reads Year/Semester 'Second/3rd'"),
    "2026-11-22_github_pec-css:g056": dict(semester=3, course_code="CSN202",
                                           why="CSN202 (code from the Robotics-PEC archive), Dec exam = odd semester"),
    "2026-11-22_github_pec-css:g083": dict(semester=3, course_code="",
                                           why="same course as MECH sem-3 Elements of Thermodynamics; 2015 paper predates code ME1032"),
    "h52Vwmr1mZJriWxY1fKB": dict(course_code="", why="semester-4 paper; EC1352 is the semester-5 course's code"),
    "tDYcPkeLRQIZnMyKywG5": dict(course_code="PY2301", why="header shows 'Course Code: PY..'; same course as PY2301"),
    "2026-11-22_github_pec-css:g112": dict(semester=3, course="Information Technology in Engineering (EOIT)",
                                           course_code="ESC202", why="header reads 'Subject: ESC202 ... Mid Sem'"),
}

NAMES = {
    "Engineering Drawing using CAD Software": "Engineering Drawing with CAD Software",
    "Neural Network and Fuzzy System": "Neural Networks and Fuzzy Systems",
    "Electrical Vehicles": "Electric Vehicles",
    "Information Technology (Electronics)": "Information Technology in Engineering (EOIT)",
}
NAME_BY_CODE = {"CH2301": "Applied Chemistry I"}

FIRST_YEAR_CODE = re.compile(r"^(ES|GS|TA|PY|CH(1201|2301)|MA(102|1101|1201|2301|2302)|HS(1101|2351))\d*[A-Z]?$")
FIRST_YEAR_NAMES = {"Engineering Drawing", "Applied Chemistry", "Electromagnetic Theory and Quantum Physics"}
HSM_CODE = re.compile(r"^(HS|HSM|MHN)\d")


def target(e):
    t = dict(department=e["department"], semester=e["semester"], course=e["course"], course_code=e.get("course_code") or "")
    for k, v in FIXES.items():
        if e["id"] == k:
            t.update({x: y for x, y in v.items() if x != "why"})
            t["code_fixed"] = "course_code" in v  # a deliberate code (or deliberate blank) is never auto-filled
    t["course"] = NAME_BY_CODE.get(t["course_code"], NAMES.get(t["course"], t["course"]))
    sem = t["semester"]
    if sem in (1, 2) and (t["department"] in OTHER or FIRST_YEAR_CODE.match(t["course_code"])
                          or t["course"] in FIRST_YEAR_NAMES):
        t["department"] = "COMMON"
    elif isinstance(sem, int) and sem >= 3 and HSM_CODE.match(t["course_code"]):
        t["department"] = "HSM"
    return t


def fill_codes(entries):
    """Same branch, semester and course with a code on some papers and none on others: use the single known code."""
    codes = collections.defaultdict(set)
    key = lambda e: (e["department"], e["semester"], e["course"])  # noqa: E731 - codes change between schemes/semesters
    for e in entries:
        if e["course_code"]:
            codes[key(e)].add(e["course_code"])
    for e in entries:
        c = codes.get(key(e), set())
        if not e["course_code"] and not e.get("code_fixed") and len(c) == 1:
            e["course_code"] = next(iter(c))


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", s.replace("&", "and")).strip("-")


def rewrite_md(path, e, uploaded_under):
    s = open(path).read()
    lines = s.split("\n")
    code = e["course_code"]
    title_tail = lines[0].rsplit(" - ", 1)[1] if " - " in lines[0] else ""
    lines[0] = f"# {e['course']}{f' ({code})' if code else ''} - {title_tail}".rstrip(" -")
    out = []
    for ln in lines:
        if ln.startswith("- **Uploaded under:**"):
            continue
        if ln.startswith("- **Department:**"):
            ln = f"- **Department:** {e['department']} - {DEPARTMENTS[e['department']]}"
            out.append(ln)
            if uploaded_under and uploaded_under != e["department"]:
                out.append(f"- **Uploaded under:** {uploaded_under} (a first-year/common course, so it is filed under {e['department']})")
            continue
        if ln.startswith("- **Semester:**"):
            ln = f"- **Semester:** {e['semester']}"
        elif ln.startswith("- **Course:**"):
            ln = f"- **Course:** {e['course']}"
        elif ln.startswith("- **Course code:**"):
            ln = f"- **Course code:** {code or 'not legible on paper'}"
        out.append(ln)
    if not any(x.startswith("- **Course code:**") for x in out):
        i = next(i for i, x in enumerate(out) if x.startswith("- **Course:**"))
        out.insert(i + 1, f"- **Course code:** {code or 'not legible on paper'}")
    open(path, "w").write("\n".join(out))


def git_mv(src, dst):
    if src == dst:
        return
    os.makedirs(os.path.dirname(f"{LIB}/{dst}"), exist_ok=True)
    r = subprocess.run(["git", "mv", src, dst], cwd=LIB, capture_output=True, text=True)
    if r.returncode:  # not tracked yet
        os.replace(f"{LIB}/{src}", f"{LIB}/{dst}")


def organize():
    mpath = f"{LIB}/data/manifest.json"
    manifest = json.load(open(mpath))
    for d in os.listdir(f"{LIB}/papers"):  # department READMEs are regenerated below
        readme = f"papers/{d}/README.md"
        if os.path.exists(f"{LIB}/{readme}"):
            if subprocess.run(["git", "rm", "-q", "-f", readme], cwd=LIB, capture_output=True).returncode:
                os.remove(f"{LIB}/{readme}")
    inc = [e for e in manifest if e["status"] == "included"]
    for e in inc:
        e.setdefault("uploaded_under", e["department"])
        e.update(target(e))
    fill_codes(inc)
    moved = 0
    for e in inc:
        folder = f"papers/{e['department']}/Semester-{e['semester']}/{slug(e['course'])}"
        base = os.path.splitext(os.path.basename(e["transcript"]))[0]
        new_md = f"{folder}/{base}.md"
        if new_md != e["transcript"]:
            git_mv(e["transcript"], new_md)
            if e.get("pdf"):
                git_mv(e["pdf"], f"{folder}/{base}.pdf")
                e["pdf"] = f"{folder}/{base}.pdf"
            e["transcript"] = new_md
            moved += 1
        rewrite_md(f"{LIB}/{e['transcript']}", e, e["uploaded_under"])
    # remove empty folders
    for root, dirs, files in sorted(os.walk(f"{LIB}/papers"), key=lambda x: -len(x[0])):
        if not os.listdir(root):
            os.rmdir(root)
    json.dump(manifest, open(mpath, "w"), indent=1, ensure_ascii=False)
    generate_all(manifest)
    print(f"{len(inc)} papers, {moved} moved")


# ---------------------------------------------------------------- indexes
def sem_key(s):
    s = str(s)
    return (not s.isdigit(), s.zfill(3))


def exam_key(e):
    return (list(EXAM_LABEL).index(e["exam"]), e["year"], e.get("reappear", False), e["transcript"])


def row(e, rel_to="", with_where=False):
    rel = (lambda p: os.path.relpath(p, rel_to)) if rel_to else (lambda p: p)
    exam = EXAM_LABEL[e["exam"]] + (" (Re-appear)" if e.get("reappear") else "")
    paper = f"[PDF]({rel(e['pdf'])}) ({e['pages']}p)" if e.get("pdf") else "text only"
    where = f"{e['department']} | {e['semester']} | " if with_where else ""
    return f"| {where}{e['course_code'] or '-'} | {exam} | {e['year']} | {paper} | [text]({rel(e['transcript'])}) |"


def generate_all(manifest):
    inc = [e for e in manifest if e["status"] == "included"]
    st = collections.Counter(e["status"] for e in manifest)
    by = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    for e in inc:
        by[e["department"]][e["semester"]][e["course"]].append(e)
    order = [d for d in BRANCHES + OTHER if d in by]
    total = f"**{len(inc)} papers, {sum(e['pages'] for e in inc)} pages.**"
    nav = "Views: [by branch](INDEX.md) · [by course](BY-COURSE.md) · [by semester](BY-SEMESTER.md)"
    note = (f"Not included: {st['duplicate']} duplicates, {st['excluded']} excluded (test uploads, or other universities' "
            f"papers mislabelled PEC), {st['missing']} missing - all listed in [data/manifest.json](data/manifest.json).")

    def dept_line(d, link):
        n = sum(len(v) for s in by[d].values() for v in s.values())
        sems = ", ".join(str(s) for s in sorted(by[d], key=sem_key))
        return f"| [{d}]({link}) | {DEPARTMENTS[d]} | {n} | {sems} |"

    # INDEX.md : branch -> semester -> course
    out = ["# PEC Chandigarh - Previous Year Papers (by branch)", "", nav, "", total + " " + note, "",
           "Folder layout: `papers/<BRANCH>/Semester-<n>/<Course>/<EXAM>_<year>_<source>.pdf` (+ `.md` with metadata, "
           "solutions section and OCR text).", "",
           "## Engineering branches", "", "| Branch | Name | Papers | Semesters |", "|---|---|---|---|"]
    out += [dept_line(d, f"#{slug(d).lower()}") for d in order if d in BRANCHES]
    out += ["", "## Common and service departments", "",
            "First-year courses taken by every branch are in **COMMON**; humanities/management courses in **HSM**; "
            "maths, chemistry and physics electives under their departments.", "",
            "| Group | Name | Papers | Semesters |", "|---|---|---|---|"]
    out += [dept_line(d, f"#{slug(d).lower()}") for d in order if d not in BRANCHES]
    out.append("")
    for d in order:
        out += [f"## {d}", "", f"_{DEPARTMENTS[d]}_ - [folder README](papers/{d}/README.md)", ""]
        for s in sorted(by[d], key=sem_key):
            out += [f"### {d} - Semester {s}", "", "| Course | Code | Exam | Year | Paper | Transcript |", "|---|---|---|---|---|---|"]
            for c in sorted(by[d][s]):
                for e in sorted(by[d][s][c], key=exam_key):
                    out.append(f"| {c} " + row(e))
            out.append("")
    open(f"{LIB}/INDEX.md", "w").write("\n".join(out))

    # BY-COURSE.md : course (A-Z) -> every paper of it, wherever filed
    bc = collections.defaultdict(list)
    for e in inc:
        bc[e["course"]].append(e)
    out = ["# PEC Chandigarh - Previous Year Papers (by course)", "", nav, "", total, "",
           f"{len(bc)} courses, A-Z. A course taught in several branches or semesters shows all its papers together.", ""]
    letters = sorted({c[0].upper() for c in bc})
    out += [" · ".join(f"[{L}](#{L.lower()})" for L in letters), ""]
    for L in letters:
        out += [f"## {L}", ""]
        for c in sorted(x for x in bc if x[0].upper() == L):
            es = sorted(bc[c], key=lambda e: (sem_key(e["semester"]), e["department"]) + exam_key(e))
            codes = ", ".join(sorted({e["course_code"] for e in es if e["course_code"]})) or "-"
            out += [f"### {c}", "", f"Code(s): {codes}", "",
                    "| Branch | Sem | Code | Exam | Year | Paper | Transcript |", "|---|---|---|---|---|---|---|"]
            out += [row(e, with_where=True) for e in es]
            out.append("")
    open(f"{LIB}/BY-COURSE.md", "w").write("\n".join(out))

    # BY-SEMESTER.md : semester -> branch -> course
    bs = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    for e in inc:
        bs[e["semester"]][e["department"]][e["course"]].append(e)
    sems = sorted(bs, key=sem_key)
    out = ["# PEC Chandigarh - Previous Year Papers (by semester)", "", nav, "", total, "",
           " · ".join(f"[Semester {s}](#semester-{str(s).lower()})" for s in sems), ""]
    for s in sems:
        n = sum(len(v) for d in bs[s].values() for v in d.values())
        out += [f"## Semester {s}", "", f"{n} papers", ""]
        for d in [x for x in BRANCHES + OTHER if x in bs[s]]:
            out += [f"### Semester {s} - {d}", "", "| Course | Code | Exam | Year | Paper | Transcript |", "|---|---|---|---|---|---|"]
            for c in sorted(bs[s][d]):
                for e in sorted(bs[s][d][c], key=exam_key):
                    out.append(f"| {c} " + row(e))
            out.append("")
    open(f"{LIB}/BY-SEMESTER.md", "w").write("\n".join(out))

    # papers/<DEPT>/README.md
    for d in order:
        n = sum(len(v) for s in by[d].values() for v in s.values())
        out = [f"# {d} - {DEPARTMENTS[d]}", "", f"{n} papers. [Full index](../../INDEX.md) · [by course](../../BY-COURSE.md) "
               f"· [by semester](../../BY-SEMESTER.md)", ""]
        if d in BRANCHES:
            out += ["First-year courses common to all branches (Calculus, Chemistry, Mechatronics, Engineering Drawing...) "
                    "are in [COMMON](../COMMON/README.md).", ""]
        for s in sorted(by[d], key=sem_key):
            out += [f"## Semester {s}", "", "| Course | Code | Exam | Year | Paper | Transcript |", "|---|---|---|---|---|---|"]
            for c in sorted(by[d][s]):
                for e in sorted(by[d][s][c], key=exam_key):
                    out.append(f"| {c} " + row(e, rel_to=f"papers/{d}"))
            out.append("")
        open(f"{LIB}/papers/{d}/README.md", "w").write("\n".join(out))


if __name__ == "__main__":
    organize()
