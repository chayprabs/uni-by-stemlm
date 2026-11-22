# PEC Chandigarh - Previous Year Question Papers

Previous year question papers (PYQs) from **Punjab Engineering College (Deemed to be University), Chandigarh**,
collected for STEM LM. This folder will also hold worked solutions for each paper.

- **Index:** [INDEX.md](INDEX.md) lists every paper by branch, then semester, then course.
- **Papers:** `papers/<DEPT>/Semester-<n>/<Course>/`
  - `<EXAM>_<year>[_Reappear]_<id>.pdf` is the question paper, one page per photo, rotated upright.
  - `<EXAM>_<year>[_Reappear]_<id>.md` has the metadata (course code, exam, year), an empty **Solutions** section to fill in, and an OCR transcript of every page.
- **Machine-readable data:** [data/manifest.json](data/manifest.json) lists every upload on the source site and what happened to it (included, duplicate, excluded or missing). [data/source_api_dump.json](data/source_api_dump.json) is the raw API response.
- **Adding your own images:** see [incoming/README.md](incoming/README.md).

## What's here

| Dept | Name | Papers |
|---|---|---|
| AERO | Aerospace Engineering | 3 |
| CHEMISTRY | Chemistry | 9 |
| CIVIL | Civil Engineering | 5 |
| CSE | Computer Science and Engineering | 15 |
| CSE-AI | CSE (Artificial Intelligence) | 2 |
| CSE-DS | CSE (Data Science) | 6 |
| ECE | Electronics and Communication Engineering | 34 |
| EE | Electrical Engineering | 5 |
| HSM | Humanities, Social Sciences and Management | 16 |
| MATHS | Mathematics | 18 |
| MECH | Mechanical Engineering | 47 |
| META | Metallurgical and Materials Engineering | 1 |
| PHYSICS | Physics | 3 |
| PROD | Production and Industrial Engineering | 5 |
| **Total** | | **169 papers, 263 pages** |

B-DES (Bachelor of Design) is a department on the site, but it had no uploads.

## Source and how it was collected

Source: <https://pecpapers.vercel.app/>, a crowd-sourced archive. It is a React front end. Its JS bundle shows that:

1. paper metadata comes from `https://pecpapers.onrender.com/papersOnFilterOrSearch?...&skip=N`, 10 records per page, 193 records in total;
2. each paper is one or more phone photos hosted on Cloudinary (`res.cloudinary.com`).

The site has no PDFs. Every paper is a set of JPG photos, so the pipeline builds the PDFs itself:

```bash
python3 scripts/fetch_pecpapers.py work                        # metadata + all photos (resumable)
OMP_THREAD_LIMIT=1 python3 scripts/prepare_images.py work      # EXIF/OSD auto-rotate, downscale, OCR
python3 scripts/build_library.py work .                        # PDFs, transcripts, manifest, INDEX.md
```

Requirements: Python 3, `pip install pillow img2pdf`, and `tesseract-ocr` (with `eng` and `osd` data).
Cleanup rules for subjects (course names, codes, duplicates, junk) live in [scripts/catalog.py](scripts/catalog.py).
Re-running the pipeline picks up anything uploaded to the site since.

## Data notes

All 193 uploads on the site were downloaded and checked; none were silently dropped:

- **169 included.** Every unique paper is in the library.
- **19 duplicates skipped.** The same photos were uploaded more than once. Each one maps to the copy that was kept (`duplicate_of` in the manifest). This covers:
  - five copies of the CIVIL Sem-7 *Green Building* mid-sem, one of which had no metadata;
  - ECE Sem-4 *"Signals and Systems"*, which is actually the ECE *Digital Logic Design* end-sem (EC1231).
- **4 test uploads excluded.** ECE Sem-7 "random subject", "randomest subject", etc. are a wallpaper image, not papers.
- **1 missing.** CSE Sem-3 "maths" mid-sem (`A7m4hDutopxEGAsThmhz`): the site still lists it, but its only image was deleted from Cloudinary (HTTP 404 under every URL variant tried). It cannot be recovered from this source.

Other cleanup:

- **Subject names** were free text on the site. Typos were fixed ("Algebric Coding theroy", "Manufacturing Processess", "Electronics Decices"…), and abbreviations were expanded after reading the papers:
  - CFD: Computational Fluid Dynamics
  - GTP: Gas Turbine Propulsion
  - HSA: High Speed Aerodynamics
  - MFAI: Mathematical Foundations of AI
  - Finance: Essentials of Finance
  - "Maths" (CSE-DS): Linear Algebra, Differential Equations and Vector Calculus
- **Course codes** were read off the papers. A blank code means it was not legible.
- **Year** comes from the uploader's comment when there is one, otherwise from the paper header ("read from paper" in the transcript). Papers with neither are `undated`.
- **Semesters and departments** are kept as the uploader tagged them. First-year common courses (Mechatronics, Computing, Environmental Sciences…) show up under whichever branch uploaded them.
- **Orientation:** pages were auto-rotated using EXIF data, tesseract orientation detection and an OCR-quality retry. A few were fixed by hand. Photos were downscaled to 2200 px (JPEG q80) to keep the repo small. Originals are on Cloudinary; the URLs are in the manifest.
- **OCR** is raw tesseract output from phone photos. It is fine for search and for seeing what a paper covers, but formulas, circuit diagrams and tables are often garbled, so use the PDF as the source of truth.
