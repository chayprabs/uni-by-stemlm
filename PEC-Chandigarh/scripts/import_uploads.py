#!/usr/bin/env python3
"""Import papers from bundled source files (multi-paper PDFs, zips of PDFs, .docx of photos).

A spec in data/imports/<batch>.json lists, for each paper, the source file
(relative to sources/<batch>/; "X.zip/inner.pdf" reaches inside a zip), the page
range, and its department / semester / course / code / exam / year.

* PDF sources: the page range is cut out with poppler (pdfseparate + pdfunite),
  so the original scan quality and any embedded text layer are kept.
* .docx sources: the embedded images (in document order) are the pages; they are
  auto-rotated, downscaled and wrapped into a PDF.
Transcript text = the PDF's own text layer or tesseract, whichever reads better.

Usage (from PEC-Chandigarh/):  OMP_THREAD_LIMIT=1 python3 scripts/import_uploads.py data/imports/<batch>.json
Re-running replaces this batch's papers (idempotent).
"""
import collections
import glob
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

import img2pdf
from PIL import Image, ImageOps

sys.path.insert(0, os.path.dirname(__file__))
from build_library import EXAM_LABEL, clean_ocr, slug, write_index  # noqa: E402
from catalog import DEPARTMENTS  # noqa: E402
from prepare_images import ocr, osd_rotation  # noqa: E402

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build_vocab():
    """Words that recur across the existing transcripts = words OCR should produce."""
    c = collections.Counter()
    for f in glob.glob(f"{LIB}/papers/**/*.md", recursive=True):
        c.update(re.findall(r"[a-z]{3,}", open(f).read().lower()))
    return {w for w, n in c.items() if n >= 8}


def score(text, vocab):
    return sum(1 for w in re.findall(r"[A-Za-z]{3,}", text) if w.lower() in vocab)


def docx_images(path):
    z = zipfile.ZipFile(path)
    rels = z.read("word/_rels/document.xml.rels").decode()
    target = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="(media/[^"]+)"', rels))
    order = re.findall(r'r:embed="(rId\d+)"', z.read("word/document.xml").decode())
    return [z.read("word/" + target[r]) for r in order]


def resolve(batch_dir, name, tmp):
    if ".zip/" in name:
        zname, inner = name.split(".zip/", 1)
        z = zipfile.ZipFile(f"{batch_dir}/{zname}.zip")
        member = next(m for m in z.namelist() if m.endswith("/" + inner) or m == inner)
        out = os.path.join(tmp, re.sub(r"[^A-Za-z0-9.]+", "_", name))
        with open(out, "wb") as f:
            f.write(z.read(member))
        return out
    return f"{batch_dir}/{name}"


def pdf_pages(src, a, b, dest, tmp, vocab):
    for f in glob.glob(f"{tmp}/pg-*.pdf"):
        os.remove(f)
    subprocess.run(["pdfseparate", "-f", str(a), "-l", str(b), src, f"{tmp}/pg-%03d.pdf"], check=True)
    parts = sorted(glob.glob(f"{tmp}/pg-*.pdf"))
    if len(parts) == 1:
        os.replace(parts[0], dest)
    else:
        subprocess.run(["pdfunite", *parts, dest], check=True)
    texts = []
    for p in range(a, b + 1):
        layer = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), src, "-"], capture_output=True, text=True).stdout
        png = subprocess.run(["pdftoppm", "-r", "200", "-gray", "-png", "-f", str(p), "-l", str(p), src], capture_output=True).stdout
        tess = ocr(Image.open(io.BytesIO(png))) if png else ""
        texts.append(clean_ocr(layer if score(layer, vocab) >= score(tess, vocab) else tess))
    return texts


def image_pages(blobs, dest):
    files, texts = [], []
    with tempfile.TemporaryDirectory() as t:
        for i, blob in enumerate(blobs):
            im = ImageOps.exif_transpose(Image.open(io.BytesIO(blob))).convert("RGB")
            im.thumbnail((2200, 2200))
            rot, conf = osd_rotation(im)
            if rot and conf >= 2:
                im = im.rotate(-rot, expand=True)
            out = f"{t}/{i:03d}.jpg"
            im.save(out, quality=80, optimize=True)
            files.append(out)
            texts.append(clean_ocr(ocr(im)))
        with open(dest, "wb") as f:
            f.write(img2pdf.convert(files))
    return texts


def main(spec_path):
    spec = json.load(open(spec_path))
    batch = os.path.splitext(os.path.basename(spec_path))[0]
    batch_dir = f"{LIB}/sources/{batch.split('_')[0]}"
    manifest_path = f"{LIB}/data/manifest.json"
    manifest = [m for m in json.load(open(manifest_path)) if m.get("source", {}).get("batch") != batch]
    vocab = build_vocab()
    docx_cache = {}

    with tempfile.TemporaryDirectory() as tmp:
        for p in spec["papers"]:
            dept = p.get("department", spec["department"])
            sem, course, code, exam, year = str(p["sem"]), p["course"], p["code"], p["exam"], p["year"]
            a, b = p["pages"]
            folder = f"papers/{dept}/Semester-{sem}/{slug(course)}"
            base = f"{exam}_{year}_upload-{batch.split('_')[0]}"
            os.makedirs(f"{LIB}/{folder}", exist_ok=True)
            dest = f"{LIB}/{folder}/{base}.pdf"

            if p["file"].endswith(".docx"):
                path = f"{batch_dir}/{p['file']}"
                docx_cache.setdefault(path, docx_images(path))
                texts = image_pages(docx_cache[path][a - 1:b], dest)
            else:
                texts = pdf_pages(resolve(batch_dir, p["file"], tmp), a, b, dest, tmp, vocab)

            label = EXAM_LABEL[exam]
            md = [
                f"# {course} ({code}) - {label} {year}",
                "",
                "- **Institute:** Punjab Engineering College (Deemed to be University), Chandigarh",
                f"- **Department:** {dept} - {DEPARTMENTS[dept]}",
                f"- **Semester:** {sem}",
                f"- **Course:** {course}",
                f"- **Course code:** {code}",
                f"- **Exam:** {label}" + (f" - {p['note']}" if p.get("note") else ""),
                f"- **Year:** {year}",
                f"- **Pages:** {len(texts)}",
                f"- **Paper PDF:** [{base}.pdf]({base}.pdf)",
                f"- **Source:** owner upload `sources/{batch.split('_')[0]}/{p['file']}`, page(s) {a}-{b}",
                "",
                "> Text below is OCR of scanned/photographed pages. Equations, diagrams and tables",
                "> are often garbled - always check against the PDF before solving.",
                "",
                "## Solutions",
                "",
                "_Not added yet._",
                "",
            ]
            for i, t in enumerate(texts):
                md += [f"## OCR transcript - page {i + 1}", "", "```text", t or "(no text recognised)", "```", ""]
            with open(f"{LIB}/{folder}/{base}.md", "w") as f:
                f.write("\n".join(md))

            manifest.append({
                "id": f"{batch}:{p['file']}:{a}-{b}",
                "source": {"batch": batch, "file": p["file"], "pages": [a, b]},
                "status": "included", "department": dept, "semester": int(sem), "course": course,
                "course_code": code, "exam": exam, "year": year, "reappear": False, "pages": len(texts),
                "pdf": f"{folder}/{base}.pdf", "transcript": f"{folder}/{base}.md",
            })
            print(f"{folder}/{base}.pdf  ({len(texts)}p)")

    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    write_index(LIB, [m for m in manifest if m["status"] == "included"], manifest)


if __name__ == "__main__":
    main(sys.argv[1])
