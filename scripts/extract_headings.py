#!/usr/bin/env python3
"""Extract all headings from markdown files in the usecases directory."""

import re
from pathlib import Path


def extract_headings(file_path: Path) -> list[tuple[int, str]]:
    """Extract headings from a markdown file.

    Returns list of (level, heading_text) tuples.
    """
    headings = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
            if match:
                level = len(match.group(1))
                text = match.group(2)
                headings.append((level, text))
    return headings


def main():
    usecases_dir = Path(__file__).parent.parent / 'topics' / 'usecases'
    output_file = Path(__file__).parent.parent / 'topics' / 'usecases' / 'headings.md'

    # Get all markdown files, excluding index.md and headings.md
    md_files = sorted([
        f for f in usecases_dir.glob('*.md')
        if f.name not in ('index.md', 'headings.md')
    ])

    output_lines = ['# Use Case Headings\n\n']

    for md_file in md_files:
        headings = extract_headings(md_file)
        if headings:
            output_lines.append(f'## {md_file.name}\n\n')
            for level, text in headings:
                indent = '  ' * (level - 1)
                output_lines.append(f'{indent}- {text}\n')
            output_lines.append('\n')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f'Extracted headings to {output_file}')


if __name__ == '__main__':
    main()
