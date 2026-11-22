#!/usr/bin/env python3
"""Download every paper listed on https://pecpapers.vercel.app/.

How the site works (found by reading its JS bundle):
  * the front end is a static React app on Vercel;
  * paper metadata comes from a backend at https://pecpapers.onrender.com
      GET /papersOnFilterOrSearch?subjectName=&semester=&department=&examType=&skip=N
    which returns 10 papers per page plus `has_more` / `total`;
  * each paper is one or more photos hosted on Cloudinary (res.cloudinary.com).

Network hosts needed: pecpapers.onrender.com, res.cloudinary.com.

Usage:
  python3 fetch_pecpapers.py OUT_DIR
Writes OUT_DIR/source_api_dump.json and OUT_DIR/raw/<paperId>_<page>.jpg.
Already-downloaded images are skipped, so it can be re-run to pick up new uploads.
"""
import concurrent.futures as cf
import json
import os
import sys
import time
import urllib.request

API = "https://pecpapers.onrender.com/papersOnFilterOrSearch?subjectName=&semester=&department=&examType=&skip={}"


def get(url, tries=5, timeout=120):
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(url, timeout=timeout).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise
            err = e
        except Exception as e:  # noqa: BLE001 - render.com cold starts are flaky
            err = e
        time.sleep(5 * (attempt + 1))
    raise err


def fetch_metadata():
    papers, skip = {}, 0
    while True:
        page = json.loads(get(API.format(skip)))
        for p in page["data"]:
            papers[p["id"]] = p
        print(f"skip={skip} got={len(page['data'])} total={page.get('total')}", file=sys.stderr)
        if not page.get("has_more") or not page["data"]:
            break
        skip += 10
    return sorted(papers.values(), key=lambda p: p["id"])


def main(out):
    os.makedirs(f"{out}/raw", exist_ok=True)
    papers = fetch_metadata()
    with open(f"{out}/source_api_dump.json", "w") as f:
        json.dump(papers, f, indent=1)

    jobs = [(p["id"], i, u) for p in papers for i, u in enumerate(p["cloudUrl"])]

    def dl(job):
        pid, i, url = job
        dest = f"{out}/raw/{pid}_{i + 1:02d}.jpg"
        if os.path.exists(dest) and os.path.getsize(dest):
            return None
        try:
            data = get(url)
        except Exception as e:  # noqa: BLE001
            return url, str(e)
        with open(dest, "wb") as f:
            f.write(data)
        return None

    with cf.ThreadPoolExecutor(8) as ex:
        failed = [r for r in ex.map(dl, jobs) if r]
    print(f"{len(papers)} papers, {len(jobs)} images, {len(failed)} failed", file=sys.stderr)
    for url, err in failed:
        print(f"  FAILED {url}: {err}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "work")
