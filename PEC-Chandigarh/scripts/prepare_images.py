#!/usr/bin/env python3
"""Make raw phone photos upright + small, and OCR them.

  WORK/raw/*.jpg  ->  WORK/proc/*.jpg (EXIF-rotated, auto-oriented, <=2200px, q80)
                  ->  WORK/ocr/*.txt  (tesseract, English)

Orientation: EXIF first, then tesseract OSD; pages whose OCR still looks like
garbage are retried at 90/180/270 degrees and the best-reading one is kept.
A few pages that defeat both heuristics are listed in MANUAL_ROTATE.

Needs: tesseract-ocr (with osd + eng data), Pillow.
Run with OMP_THREAD_LIMIT=1 - multi-threaded tesseract thrashes badly in parallel.
Usage: OMP_THREAD_LIMIT=1 python3 prepare_images.py WORK
"""
import collections
import concurrent.futures as cf
import glob
import io
import os
import re
import subprocess
import sys

from PIL import Image, ImageOps

# extra counter-clockwise rotation (degrees) applied after the automatic passes
MANUAL_ROTATE = {
    "5gQwK7AugpOyhg5oBOTk_02": 90,
    "ocKtSreQ7SJBgzjBLQLn_02": 90,
    "WWvh44134dMtBB2OfSn4_01": 90,
}


def ocr(im, psm="3"):
    b = io.BytesIO()
    im.save(b, "JPEG", quality=85)
    return subprocess.run(["tesseract", "stdin", "-", "--psm", psm], input=b.getvalue(), capture_output=True).stdout.decode()


def osd_rotation(im):
    o = ocr(im, "0")
    m, c = re.search(r"Rotate: (\d+)", o), re.search(r"Orientation confidence: ([\d.]+)", o)
    return (int(m.group(1)) if m else 0), (float(c.group(1)) if c else 0.0)


def pass1(src, work):
    key = os.path.basename(src)[:-4]
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((2200, 2200))
    rot, conf = osd_rotation(im)
    if rot and conf >= 2:
        im = im.rotate(-rot, expand=True)
    im.save(f"{work}/proc/{key}.jpg", quality=80, optimize=True)
    return key, ocr(im)


def main(work):
    os.makedirs(f"{work}/proc", exist_ok=True)
    os.makedirs(f"{work}/ocr", exist_ok=True)
    with cf.ThreadPoolExecutor(os.cpu_count()) as ex:
        results = list(ex.map(lambda s: pass1(s, work), sorted(glob.glob(f"{work}/raw/*.jpg"))))

    # vocabulary of words that appear often across all pages = "real" exam words
    freq = collections.Counter(w for _, t in results for w in re.findall(r"[a-z]{3,}", t.lower()))
    vocab = {w for w, c in freq.items() if c >= 8}

    def score(t):
        return sum(1 for w in re.findall(r"[A-Za-z]{3,}", t) if w.lower() in vocab)

    def finish(r):
        key, text = r
        im = Image.open(f"{work}/proc/{key}.jpg")
        im.load()
        if score(text) < 40:
            best = (score(text), im, text)
            for deg in (90, 180, 270):
                cand = im.rotate(deg, expand=True)
                t = ocr(cand)
                if score(t) > best[0] * 1.5 + 5:
                    best = (score(t), cand, t)
            _, im, text = best
        if key in MANUAL_ROTATE:
            im = im.rotate(MANUAL_ROTATE[key], expand=True)
            text = ocr(im) or text
        im.save(f"{work}/proc/{key}.jpg", quality=80, optimize=True)
        with open(f"{work}/ocr/{key}.txt", "w") as f:
            f.write(text)

    with cf.ThreadPoolExecutor(os.cpu_count()) as ex:
        list(ex.map(finish, results))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "work")
