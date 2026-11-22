#!/usr/bin/env python3
"""Turn downloaded paper photos into the organised PEC Chandigarh library.

Input  (WORK dir, produced by fetch_pecpapers.py + prepare_images.py):
  WORK/source_api_dump.json      raw API records
  WORK/proc/<id>_<page>.jpg      upright, downscaled page images
  WORK/ocr/<id>_<page>.txt       tesseract OCR of each page
Output (LIB dir, normally PEC-Chandigarh/):
  papers/<DEPT>/Semester-<n>/<Course>/<EXAM>_<year>[_Reappear]_<id>.pdf   the paper
  papers/<DEPT>/Semester-<n>/<Course>/<EXAM>_<year>[_Reappear]_<id>.md    OCR transcript
  data/manifest.json                                                      every upload + its fate
  INDEX.md                                                                branch -> semester -> course index

Usage: python3 build_library.py WORK LIB
"""
import collections
import json
import os
import re
import sys

import img2pdf

sys.path.insert(0, os.path.dirname(__file__))
from catalog import BROKEN, COURSES, DEPARTMENTS, DUPLICATE_OF, JUNK, YEAR_OVERRIDES  # noqa: E402

EXAM_LABEL = {"MID-SEM": "Mid-Semester", "END-SEM": "End-Semester", "PRACTICAL": "Practical"}


def slug(s):
    s = s.replace("&", "and")
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s


def year_of(p):
    m = re.search(r"\b(20\d\d)\b", p.get("comments") or "")
    if m:
        return m.group(1), "uploader comment"
    y = YEAR_OVERRIDES.get(p["id"][:6])
    if y:
        return y, "read from paper"
    return "undated", ""


def clean_ocr(t):
    t = t.replace("\f", "")
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def main(work, lib):
    papers = json.load(open(f"{work}/source_api_dump.json"))
    manifest, entries = [], []
    used_names = set()

    for p in sorted(papers, key=lambda p: (p["department"], p["semester"], p["subjectName"].strip().lower(), p["examType"], p["id"])):
        pid = p["id"]
        rec = {
            "id": pid,
            "source": {k: p[k] for k in ("department", "semester", "subjectName", "examType", "comments", "cloudUrl")},
        }
        if pid in JUNK:
            rec.update(status="excluded", reason=JUNK[pid])
        elif pid in BROKEN:
            rec.update(status="missing", reason=BROKEN[pid])
        elif pid in DUPLICATE_OF:
            rec.update(status="duplicate", duplicate_of=DUPLICATE_OF[pid])
        manifest.append(rec)
        if "status" in rec:
            continue

        dept, sem = p["department"], p["semester"]
        course, code = COURSES[(dept, sem, p["subjectName"].strip().lower())]
        exam = p["examType"]
        year, year_src = year_of(p)
        reappear = "re-appear" in (p.get("comments") or "").lower()
        folder = f"papers/{dept}/Semester-{sem}/{slug(course)}"
        base = f"{exam}_{year}{'_Reappear' if reappear else ''}_{pid[:6]}"
        assert (folder, base) not in used_names, (folder, base)
        used_names.add((folder, base))
        os.makedirs(f"{lib}/{folder}", exist_ok=True)

        pages = [f"{work}/proc/{pid}_{i + 1:02d}.jpg" for i in range(len(p["cloudUrl"]))]
        pages = [x for x in pages if os.path.exists(x)]
        with open(f"{lib}/{folder}/{base}.pdf", "wb") as f:
            f.write(img2pdf.convert(pages))

        title = f"{course}{f' ({code})' if code else ''} - {EXAM_LABEL[exam]} {year}{' Re-appear' if reappear else ''}"
        md = [
            f"# {title}",
            "",
            f"- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh",
            f"- **Department:** {dept} - {DEPARTMENTS[dept]}",
            f"- **Semester:** {sem}",
            f"- **Course:** {course}",
            f"- **Course code:** {code or 'not legible on paper'}",
            f"- **Exam:** {EXAM_LABEL[exam]}{' (Re-appear)' if reappear else ''}",
            f"- **Year:** {year}{f' ({year_src})' if year_src else ''}",
            f"- **Pages:** {len(pages)}",
            f"- **Paper PDF:** [{base}.pdf]({base}.pdf)",
            f"- **Source:** pecpapers.vercel.app, upload id `{pid}`",
            "",
            "> Text below is machine OCR of phone photos of the paper. Equations, diagrams and",
            "> tables are often garbled - always check against the PDF before solving.",
            "",
            "## Solutions",
            "",
            "_Not added yet._",
            "",
        ]
        for i, _ in enumerate(pages):
            txt_path = f"{work}/ocr/{pid}_{i + 1:02d}.txt"
            txt = clean_ocr(open(txt_path).read()) if os.path.exists(txt_path) else ""
            md += [f"## OCR transcript - page {i + 1}", "", "```text", txt or "(no text recognised)", "```", ""]
        with open(f"{lib}/{folder}/{base}.md", "w") as f:
            f.write("\n".join(md))

        rec.update(
            status="included",
            department=dept,
            semester=int(sem),
            course=course,
            course_code=code,
            exam=exam,
            year=year,
            reappear=reappear,
            pages=len(pages),
            pdf=f"{folder}/{base}.pdf",
            transcript=f"{folder}/{base}.md",
        )
        entries.append(rec)

    os.makedirs(f"{lib}/data", exist_ok=True)
    with open(f"{lib}/data/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    write_index(lib, entries, manifest)


def write_index(lib, entries, manifest):
    by = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    for e in entries:
        by[e["department"]][e["semester"]][(e["course"], e["course_code"])].append(e)
    st = collections.Counter(m["status"] for m in manifest)

    out = [
        "# PEC Chandigarh - Previous Year Papers Index",
        "",
        "Organised **branch -> semester -> course**. Each paper has a PDF and a `.md` file with",
        "metadata, a (to be filled) solutions section and the OCR transcript.",
        "",
        f"**{st['included']} papers** across {len(by)} departments "
        f"({sum(e['pages'] for e in entries)} pages). "
        f"Skipped: {st['duplicate']} duplicate uploads, {st['excluded']} test uploads, {st['missing']} deleted upload "
        "(details in [README.md](README.md#data-notes)).",
        "",
        "## Departments",
        "",
    ]
    for d in sorted(by):
        n = sum(len(v) for s in by[d].values() for v in s.values())
        out.append(f"- [{d} - {DEPARTMENTS[d]}](#{slug(d).lower()}) ({n} papers)")
    out.append("")
    for d in sorted(by):
        out += [f"## {d}", "", f"_{DEPARTMENTS[d]}_", ""]
        for s in sorted(by[d]):
            out += [f"### {d} - Semester {s}", "", "| Course | Code | Exam | Year | Paper | Transcript |", "|---|---|---|---|---|---|"]
            for (course, code), es in sorted(by[d][s].items()):
                for e in sorted(es, key=lambda e: (e["exam"] != "MID-SEM", e["year"], e["reappear"])):
                    exam = EXAM_LABEL[e["exam"]] + (" (Re-appear)" if e["reappear"] else "")
                    out.append(
                        f"| {course} | {code or '-'} | {exam} | {e['year']} | "
                        f"[PDF]({e['pdf']}) ({e['pages']}p) | [text]({e['transcript']}) |"
                    )
            out.append("")
    with open(f"{lib}/INDEX.md", "w") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
