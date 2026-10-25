#!/usr/bin/env python3
"""Render _data/ledger.yml to docs/shipped-ledger.md.

  python3 scripts/render_ledger.py          # write the page
  python3 scripts/render_ledger.py --check  # fail if the page is out of date
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "_data" / "ledger.yml"
OUT = ROOT / "docs" / "shipped-ledger.md"

ORDER = ["shipped", "live", "unverified", "partial", "planned"]
MEANING = {
    "shipped": "Seen working in production by a person in a browser. Describe it as live.",
    "live": "Observed in production from outside. Describe it, but it still needs a browser check.",
    "unverified": "Code or data says it exists. Nobody has seen it in production yet.",
    "partial": "Part of it is live, or it is merged and waiting for production. Needs the Partial badge.",
    "planned": "Not in production. Needs the Planned badge and future tense.",
}


def cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def render():
    data = yaml.safe_load(LEDGER.read_text(encoding="utf-8"))
    caps = data["capabilities"]
    lines = [
        "---",
        "title: Shipped ledger",
        "nav_exclude: true",
        "search_exclude: true",
        "---",
        "",
        "<!-- Generated from _data/ledger.yml by scripts/render_ledger.py. Do not edit by hand. -->",
        "",
        "# Shipped ledger",
        "",
        f"Last checked: {data.get('checked', '')}. Source: `_data/ledger.yml`.",
        "",
        "Help pages may only describe what this ledger says is live. "
        "`scripts/check_truth.py` enforces it on every pull request.",
        "",
        "| State | Meaning | Count |",
        "|---|---|---|",
    ]
    for state in ORDER:
        n = sum(1 for c in caps if c["state"] == state)
        lines.append(f"| `{state}` | {MEANING[state]} | {n} |")
    lines.append("")

    for state in ORDER:
        rows = [c for c in caps if c["state"] == state]
        if not rows:
            continue
        lines += [f"## {state.capitalize()}", "", "| Capability | Docs wording | Evidence |", "|---|---|---|"]
        for c in rows:
            lines.append(f"| {cell(c['name'])} | {cell(c.get('wording'))} | {cell(c.get('evidence'))} |")
        lines.append("")

    verify = [c for c in caps if c["state"] in ("live", "unverified")]
    lines += [
        "## Browser checks for Colm",
        "",
        "Tick each one after seeing it work in the product, then move its row to `shipped` "
        "(or down to `partial` / `planned`) in `_data/ledger.yml`.",
        "",
    ]
    for c in verify:
        lines.append(f"- [ ] {c['name']}")
    lines.append("")
    return "\n".join(lines)


def main():
    page = render()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != page:
            print("docs/shipped-ledger.md is out of date. Run: python3 scripts/render_ledger.py")
            return 1
        print("docs/shipped-ledger.md is up to date")
        return 0
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
