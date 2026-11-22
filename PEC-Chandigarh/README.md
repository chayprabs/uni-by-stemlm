# PEC Chandigarh - Previous Year Question Papers

Previous year question papers (PYQs) from **Punjab Engineering College (Deemed to be University), Chandigarh**,
collected for STEM LM. This folder will also hold worked solutions for each paper.

- **Index:** [INDEX.md](INDEX.md) lists every paper by branch, then semester, then course.
- **Papers:** `papers/<DEPT>/Semester-<n>/<Course>/`
  - `<EXAM>_<year>[_Reappear]_<id>.pdf` is the question paper, one page per photo, rotated upright.
  - `<EXAM>_<year>[_Reappear]_<id>.md` has the metadata (course code, exam, year), an empty **Solutions** section to fill in, and an OCR transcript of every page.
- **Machine-readable data:** [data/manifest.json](data/manifest.json) lists every upload on the source site and what happened to it (included, duplicate, excluded or missing). [data/source_api_dump.json](data/source_api_dump.json) is the raw API response.
- **Adding your own images:** see [incoming/README.md](incoming/README.md).
- **Original files you uploaded:** `sources/<date>/`, untouched. How they were split into papers is in `data/imports/<date>_*.json`.

## What's here

| Dept | Name | Papers |
|---|---|---|
| AERO | Aerospace Engineering | 8 |
| CHEMISTRY | Chemistry | 9 |
| CIVIL | Civil Engineering | 30 |
| COMMON | First-year common courses (all branches) | 8 |
| CSE | Computer Science and Engineering | 49 |
| CSE-AI | CSE (Artificial Intelligence) | 2 |
| CSE-DS | CSE (Data Science) | 8 |
| ECE | Electronics and Communication Engineering | 56 |
| EE | Electrical Engineering | 69 |
| HSM | Humanities, Social Sciences and Management | 23 |
| MATHS | Mathematics | 18 |
| MECH | Mechanical Engineering | 54 |
| META | Metallurgical and Materials Engineering | 17 |
| PHYSICS | Physics | 3 |
| PROD | Production and Industrial Engineering | 21 |
| **Total** | | **375 papers, 591 pages** |

B-DES (Bachelor of Design) is a department on the site, but it had no uploads.

## Sources

| Source | Papers | Years | Notes |
|---|---|---|---|
| [pecpapers.vercel.app](https://pecpapers.vercel.app/) | 169 | 2016-2026 | crowd-sourced site; see "Source and how it was collected" below |
| Owner uploads (`sources/2026-11-22/`) | 42 | 2023-2025 | EE semesters 1, 2, 3 and 5 |
| [PEC-CSS/PEC-Previous-Year-Papers](https://github.com/PEC-CSS/PEC-Previous-Year-Papers) (GitHub, PEC CSS student society) | 154 | 2013-2022 | mostly the old *PEC University of Technology* scheme (codes like CSN-409, EEN-413) |
| [Robotics-PEC/pyq](https://github.com/Robotics-PEC/pyq) (PEC Robotics Society's "PECademic" PYQ page) | 2 | 2022, 2025 | 25 PDFs checked; 23 duplicate papers already here (several are compilations of PEC-CSS folders) |
| [howtoexam.com](https://www.howtoexam.com) | 8 | 2007, 2010 | first-year MA102, TA101, TA103, PY101; 31 other entries labelled "PEC" there are other universities' papers and were excluded |

File names end with where the paper came from: `_<id>` (pecpapers), `_upload-<date>` (owner upload), `_pecss-gNNN` (PEC-CSS GitHub), `_robopec-rNN` (Robotics Society GitHub) or `_howtoexam-hNNNN`.

**Browsing:** start at [INDEX.md](INDEX.md), or open any department folder in `papers/`. Each one has its own README listing its papers.

### Completeness audit (2026-11-22)

- **Owner uploads:** all 7 files are stored byte-for-byte in `sources/2026-11-22/`. All 63 pages in them (16 PDFs inside the zips and bundles, plus 14 photos in the .docx) are assigned to a paper.
- **pecpapers.vercel.app:** re-queried after the first import and still 193 records with no changes. Every record is in the manifest.
- **PEC-CSS GitHub:** all 252 files on main, the full history, all branches, all 30 pull requests and 18 forks were checked. Nothing exists beyond the 252 files.
- **Robotics-PEC/pyq:** all branches, history and pull requests were checked. Its photos are Git LFS pointers to the PEC-CSS images.
- **howtoexam.com:** all 39 PEC-labelled entries were opened, including multi-page entries and attachments.

### Sources checked that had nothing usable

- **Scribd:** two PEC bundles ("Mech sem 3 Question Papers", "PYQs 1st Year - All Subjects 2023-24") are behind Scribd's bot check and login. Download them by hand and drop them into `incoming/` or `sources/`.
- **universitypaper.in / universitypaperindia.com, universitynewsindia.com:** SEO pages; every "download" link points to pec.ac.in's homepage.
- **sample-papers.com:** the PEC page only shows University of Delhi papers as filler.
- **goeduhub.com:** the PEC page no longer exists.
- **pec.ac.in:** the official site does not publish question papers.
- **PEC-CSS's original source** is a private Facebook group, which needs a login.

### howtoexam.com

All 39 entries listed under Punjab Engineering College were opened. Seven have the original scan attached; those were imported as PDFs. One PEC paper (TA103 Engineering Design end-sem) exists only as typed text, which the site has partly machine-reworded, so it is included as a transcript with no PDF. The remaining 31 are excluded, with the reason for each recorded in [data/imports/2026-11-22_howtoexam.json](data/imports/2026-11-22_howtoexam.json):

- the 2005 "B.Tech" set is in Punjab Technical University format;
- the 2006-2008 papers are Anna University (Regulation 2004/2007 codes such as CS1301 and MA1101) or B.Sc papers.

These 2007/2010 papers are filed under `COMMON` (first-year courses for all branches).

### GitHub: PEC-CSS/PEC-Previous-Year-Papers

All 252 unique files in the repo were checked, plus the full git history and 18 forks, which hold nothing extra. The repo's folders are named by subject but the photos inside are in random order (they were scraped from a Facebook group album), and one folder can mix mid-sems, end-sems and years. So **every page header was read by hand** to split the folders into **154 papers** and to record the department, semester, course code, exam and year. The full page-to-paper mapping, with links to every original file, is in [data/imports/2026-11-22_github_pec-css.json](data/imports/2026-11-22_github_pec-css.json).

- **9 files skipped as duplicates.** Five of them are 2024 first-year papers already in the library from your upload (UHV, Applied Chemistry, Engineering Drawing, Mechatronics, Linear Algebra). The other four are second photos of the same page.
- **Continuation pages** (pages with no header) were attached to the paper they most likely belong to, based on question numbering and marks. In a few multi-paper folders (Operations Research, Big Data, Network Security) that attachment is a best guess.
- **Exam types beyond mid/end-sem:** `QUIZ` (quizzes, class tests, lab quizzes), `SESSIONAL`, `ASSIGNMENT` (one M.Tech coursework sheet) and `UNKNOWN` (the header was not photographed).
- **`Semester-unknown`** holds papers whose semester isn't printed. **`Semester-MTech-2`** holds the M.Tech papers (Production and Industrial Engg.).
- **Years** come from the printed date or the session code (e.g. `18191` means the 2018-19 odd semester, i.e. Nov/Dec 2018). Papers without either are `undated`.

## Owner uploads

### 2026-11-22: EE batch (42 papers)

Source files are in [sources/2026-11-22/](sources/2026-11-22/), and the page-to-paper mapping is in [data/imports/2026-11-22_user_uploads.json](data/imports/2026-11-22_user_uploads.json). All papers are filed under **EE**. Semesters 1 and 2 are courses common to all B.Tech branches.

| Semester | Year | Papers |
|---|---|---|
| 1 (`End_Sem.zip`, `Mid_Sem.zip`) | 2023 | Calculus, Communication Skills (end only), Intro to Environmental Sciences, Intro to Electronics and Electrical Engg, Intro to Computer Programming, EM Theory and Quantum Physics: 11 papers |
| 2 (`2ndSem_END_terms.pdf`, `2ndSem_Mid_terms.pdf`) | 2024 | Engineering Drawing using CAD (mid, end and the April 2024 CAD **practical**), Universal Human Values (end), Intro to Mechatronics, Applied Chemistry, Linear Algebra, DE and Vector Calculus: 10 papers |
| 3 (`3rdSem_MST.pdf`, `3rdSem_EST.pdf`) | 2024 | Power System Engg, Object Oriented Programming, Electrical Machines I, Networks and Systems, Essentials of Finance, Measurement and Instrumentation (mid and end for each): 12 papers |
| 5 (`SEM_5_PYQ_2025-26.docx`) | 2025 | Power System Protection and Switchgear, Electric Drives, Electric Vehicles, Microprocessor and Microcontroller (mid and end for each), Analytical Tools for Data Science (minor, mid only): 9 papers |

The bundled PDFs were cut into one PDF per paper at their original scan quality, with the scanner's text layer kept. Each transcript uses whichever reads better: the scanner's text layer or a fresh tesseract OCR. To import another bundle, copy the files to `sources/<date>/`, write `data/imports/<date>_*.json` and run `OMP_THREAD_LIMIT=1 python3 scripts/import_uploads.py data/imports/<date>_*.json`.

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
