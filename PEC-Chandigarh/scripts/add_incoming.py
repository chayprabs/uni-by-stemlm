#!/usr/bin/env python3
"""Add photos/scans dropped into incoming/ to the library.

Expected layout (see incoming/README.md):
  incoming/<DEPT>/<semester>/<Course Name>/<MID-SEM|END-SEM>_<year>[_Reappear]/<pages>.jpg|.jpeg|.png
Pages are ordered by file name. Each folder becomes one paper (PDF + transcript),
is appended to data/manifest.json, and INDEX.md is regenerated.
Processed folders are moved to incoming/_done/ so re-running is safe.

Usage (from PEC-Chandigarh/):  OMP_THREAD_LIMIT=1 python3 scripts/add_incoming.py
"""
import glob
import hashlib
import json
import os
import re
import shutil
import sys

import img2pdf
from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(__file__))
from build_library import EXAM_LABEL, clean_ocr, slug, write_index  # noqa: E402
from catalog import DEPARTMENTS  # noqa: E402
from prepare_images import ocr, osd_rotation  # noqa: E402

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    manifest_path = f"{LIB}/data/manifest.json"
    manifest = json.load(open(manifest_path))
    added = 0
    for paper_dir in sorted(glob.glob(f"{LIB}/incoming/*/*/*/*/")):
        rel = os.path.relpath(paper_dir, f"{LIB}/incoming")
        if rel.startswith("_done"):
            continue
        dept, sem, course, exam_dir = rel.strip("/").split("/")
        m = re.fullmatch(r"(MID-SEM|END-SEM)_(\d{4}|undated)(_Reappear)?", exam_dir)
        if dept not in DEPARTMENTS or not sem.isdigit() or not m:
            print(f"skip {rel}: expected <DEPT>/<sem>/<Course>/<MID-SEM|END-SEM>_<year>[_Reappear]")
            continue
        exam, year, reappear = m.group(1), m.group(2), bool(m.group(3))
        files = sorted(f for f in glob.glob(f"{paper_dir}*") if f.lower().endswith((".jpg", ".jpeg", ".png")))
        if not files:
            continue
        pid = "local-" + hashlib.sha1("".join(open(f, "rb").read(4096).hex() for f in files).encode()).hexdigest()[:10]
        folder = f"papers/{dept}/Semester-{sem}/{slug(course)}"
        base = f"{exam}_{year}{'_Reappear' if reappear else ''}_{pid[6:12]}"
        os.makedirs(f"{LIB}/{folder}", exist_ok=True)

        pages, texts = [], []
        tmp = f"{LIB}/incoming/_tmp"
        os.makedirs(tmp, exist_ok=True)
        for i, f in enumerate(files):
            im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
            im.thumbnail((2200, 2200))
            rot, conf = osd_rotation(im)
            if rot and conf >= 2:
                im = im.rotate(-rot, expand=True)
            out = f"{tmp}/{i:03d}.jpg"
            im.save(out, quality=80, optimize=True)
            pages.append(out)
            texts.append(clean_ocr(ocr(im)))
        with open(f"{LIB}/{folder}/{base}.pdf", "wb") as fh:
            fh.write(img2pdf.convert(pages))
        shutil.rmtree(tmp)

        md = [
            f"# {course} - {EXAM_LABEL[exam]} {year}{' Re-appear' if reappear else ''}",
            "",
            "- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh",
            f"- **Department:** {dept} - {DEPARTMENTS[dept]}",
            f"- **Semester:** {sem}",
            f"- **Course:** {course}",
            f"- **Exam:** {EXAM_LABEL[exam]}{' (Re-appear)' if reappear else ''}",
            f"- **Year:** {year}",
            f"- **Pages:** {len(pages)}",
            f"- **Paper PDF:** [{base}.pdf]({base}.pdf)",
            "- **Source:** added locally via incoming/",
            "",
            "> Text below is machine OCR - check against the PDF.",
            "",
            "## Solutions",
            "",
            "_Not added yet._",
            "",
        ]
        for i, t in enumerate(texts):
            md += [f"## OCR transcript - page {i + 1}", "", "```text", t or "(no text recognised)", "```", ""]
        with open(f"{LIB}/{folder}/{base}.md", "w") as fh:
            fh.write("\n".join(md))

        manifest.append({
            "id": pid, "source": {"local_folder": rel}, "status": "included",
            "department": dept, "semester": int(sem), "course": course, "course_code": "",
            "exam": exam, "year": year, "reappear": reappear, "pages": len(pages),
            "pdf": f"{folder}/{base}.pdf", "transcript": f"{folder}/{base}.md",
        })
        done = f"{LIB}/incoming/_done/{rel}"
        os.makedirs(os.path.dirname(done.rstrip("/")), exist_ok=True)
        shutil.move(paper_dir, done)
        print(f"added {folder}/{base}.pdf ({len(pages)} pages)")
        added += 1

    with open(manifest_path, "w") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)
    write_index(LIB, [m for m in manifest if m["status"] == "included"], manifest)
    print(f"{added} paper(s) added")


if __name__ == "__main__":
    main()
