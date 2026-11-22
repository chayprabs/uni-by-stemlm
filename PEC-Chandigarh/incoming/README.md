# incoming/ - drop new paper images here

Put photos or scans of a paper in one folder per paper:

```
incoming/<DEPT>/<semester>/<Course Name>/<MID-SEM|END-SEM>_<year>[_Reappear]/
    01.jpg
    02.jpg
    ...
```

Example: `incoming/ECE/4/Signals and Systems/END-SEM_2025/01.jpg`

- `<DEPT>` is one of: AERO, B-DES, CHEMISTRY, CIVIL, CSE, CSE-AI, CSE-DS, ECE, EE, HSM, MATHS, MECH, META, PHYSICS, PROD
- Pages are taken in file-name order (`.jpg`, `.jpeg`, `.png`).
- Use `undated` in place of the year if it's unknown.

Then, from `PEC-Chandigarh/`, run:

```bash
OMP_THREAD_LIMIT=1 python3 scripts/add_incoming.py
```

Each folder is turned into a PDF and an OCR transcript under `papers/`, then added to
`data/manifest.json` and `INDEX.md`. Processed folders are moved to `incoming/_done/`.
