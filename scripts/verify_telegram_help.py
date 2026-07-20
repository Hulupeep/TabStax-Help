#!/usr/bin/env python3
"""Verify that the canonical Telegram guide covers the shipped public surface."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "topics" / "team-stax" / "telegram.md"


def main() -> None:
    text = GUIDE.read_text(encoding="utf-8")
    required = [
        "@heystax_bot",
        "@heystax_test_bot",
        "Group administrator: connect a group once",
        "Collaborator: link your own Telegram account",
        "Claim Cowboys",
        "Link account",
        "Add group",
        "/stax",
        "/status",
        "@heystax_bot what's up",
        "done",
        "reopen",
        "edit <new action text>",
        "block <reason>",
        "delete",
        "/join",
        "/leave",
        "/sup",
        "Next: prepare the client presentation",
        "Blocked: waiting for final figures",
        "This group or sender is not authorized",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit("Telegram help is missing: " + ", ".join(missing))

    linked_from = [ROOT / "README.md", ROOT / "topics" / "team-stax" / "index.md"]
    for source in linked_from:
        if "telegram" not in source.read_text(encoding="utf-8").lower():
            raise SystemExit(f"Telegram guide is not linked from {source.relative_to(ROOT)}")

    print("Telegram help contract passed")


if __name__ == "__main__":
    main()
