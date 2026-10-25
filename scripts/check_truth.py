#!/usr/bin/env python3
"""Truth gate for help pages.

Checks pages against _data/ledger.yml:
  - naming a `planned` capability without the Planned badge is an error
  - naming a `partial` capability without the Partial or Planned badge is an error
  - any `avoid` pattern (old URLs, retired names) is an error
  - naming a `live` or `unverified` capability is a warning until it is browser-verified

Usage:
  python3 scripts/check_truth.py                  # every page
  python3 scripts/check_truth.py FILE...          # these pages
  python3 scripts/check_truth.py --changed BASE   # pages changed since git ref BASE
  add --strict to turn warnings into errors
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "_data" / "ledger.yml"
PLANNED_BADGE = "badge-planned.html"
PARTIAL_BADGE = "badge-partial.html"
WARN_STATES = {"live", "unverified"}


def load_ledger(path=LEDGER):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    caps = data["capabilities"]
    for cap in caps:
        cap["_terms"] = [re.compile(t, re.IGNORECASE) for t in cap.get("terms", [])]
        cap["_avoid"] = [re.compile(t, re.IGNORECASE) for t in cap.get("avoid", [])]
    return caps


def page_files(root=ROOT):
    files = [root / "README.md"]
    files += sorted((root / "topics").rglob("*.md"))
    return [f for f in files if f.exists()]


def changed_files(base, root=ROOT):
    out = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{base}...HEAD"],
        cwd=root, capture_output=True, text=True, check=True,
    ).stdout.split()
    pages = []
    for name in out:
        p = root / name
        if p.suffix == ".md" and (name == "README.md" or name.startswith("topics/")):
            pages.append(p)
    return pages


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check_page(path, caps):
    text = Path(path).read_text(encoding="utf-8")
    has_planned = PLANNED_BADGE in text
    has_partial = PARTIAL_BADGE in text
    errors, warnings = [], []

    for cap in caps:
        for rx in cap["_avoid"]:
            m = rx.search(text)
            if m:
                errors.append(
                    f"{path}:{line_of(text, m.start())}: '{m.group(0)}' must not appear "
                    f"({cap['id']}). Use: {cap.get('wording', '')}"
                )

        hit = next((m for rx in cap["_terms"] if (m := rx.search(text))), None)
        if not hit:
            continue
        where = f"{path}:{line_of(text, hit.start())}"
        state = cap["state"]
        if state == "planned" and not has_planned:
            errors.append(
                f"{where}: names planned capability '{cap['name']}' ('{hit.group(0)}') "
                f"without {{% include {PLANNED_BADGE} %}}"
            )
        elif state == "partial" and not (has_partial or has_planned):
            errors.append(
                f"{where}: names partial capability '{cap['name']}' ('{hit.group(0)}') "
                f"without {{% include {PARTIAL_BADGE} %}}"
            )
        elif state in WARN_STATES:
            warnings.append(
                f"{where}: names '{cap['name']}' which is {state}, not browser-verified yet"
            )
    return errors, warnings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--changed", metavar="BASE")
    ap.add_argument("--ledger", default=str(LEDGER))
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args(argv)

    caps = load_ledger(args.ledger)
    if args.files:
        files = [Path(f) for f in args.files]
    elif args.changed:
        files = changed_files(args.changed)
    else:
        files = page_files()

    errors, warnings = [], []
    for f in files:
        e, w = check_page(f, caps)
        errors += e
        warnings += w

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"checked {len(files)} page(s): {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
