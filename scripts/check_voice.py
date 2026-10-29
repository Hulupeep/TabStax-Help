#!/usr/bin/env python3
"""Voice check for help pages.

Flags em dashes, banned positioning, wellness framing and hype words (see CLAUDE.md).

Usage:
  python3 scripts/check_voice.py                  # every page, findings are warnings
  python3 scripts/check_voice.py FILE...          # these pages, findings are errors
  python3 scripts/check_voice.py --changed BASE   # pages changed since BASE, findings are errors
"""

import argparse
import re
import sys
from pathlib import Path

from check_truth import changed_files, line_of, page_files

RULES = [
    ("em dash", r"—"),
    ("positioning", r"\bproject management\b"),
    ("positioning", r"\bproductivity (tool|app)s?\b"),
    ("positioning", r"\bflow manager\b"),
    ("positioning", r"\bfocus app\b"),
    ("positioning", r"\btask manager\b"),
    ("positioning", r"\bconnect your life to AI\b"),
    ("wellness", r"\bwellness\b"),
    ("wellness", r"\bself-care\b"),
    ("wellness", r"\bmindfulness\b"),
    ("wellness", r"\bpeace of mind\b"),
    ("wellness", r"\bcalm your mind\b"),
    ("hype", r"\brevolutionary\b"),
    ("hype", r"\bgame[- ]chang(er|ing)\b"),
    ("hype", r"\bseamless(ly)?\b"),
    ("hype", r"\bsupercharge[sd]?\b"),
    ("hype", r"\bunleash(es|ed)?\b"),
    ("hype", r"\bcutting[- ]edge\b"),
    ("hype", r"\bnext[- ]level\b"),
    ("hype", r"\beffortless(ly)?\b"),
    ("hype", r"\bworld[- ]class\b"),
    ("hype", r"\bbest[- ]in[- ]class\b"),
    ("hype", r"\b10x\b"),
]
COMPILED = [(kind, re.compile(rx, re.IGNORECASE)) for kind, rx in RULES]


def check_page(path):
    text = Path(path).read_text(encoding="utf-8")
    findings = []
    for kind, rx in COMPILED:
        for m in rx.finditer(text):
            findings.append(f"{path}:{line_of(text, m.start())}: {kind}: '{m.group(0)}'")
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--changed", metavar="BASE")
    args = ap.parse_args(argv)

    if args.files:
        files, strict = [Path(f) for f in args.files], True
    elif args.changed:
        files, strict = changed_files(args.changed), True
    else:
        files, strict = page_files(), False

    findings = []
    for f in files:
        findings += check_page(f)

    label = "error" if strict else "warning"
    for f in findings:
        print(f"{label}: {f}")
    print(f"checked {len(files)} page(s): {len(findings)} {label}(s)")
    return 1 if strict and findings else 0


if __name__ == "__main__":
    sys.exit(main())
