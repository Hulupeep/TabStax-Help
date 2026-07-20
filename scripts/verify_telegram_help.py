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
        "Turn Telegram updates into shared work in HeyStax",
        "Everyone with access to the Stax can then see who is working on what",
        "A live view of the team's work",
        "Standups without another meeting",
        "Private personal status",
        "which Stax",
        "who owns",
        "Group administrator: connect a group once",
        "Collaborator: link your own Telegram account",
        "Claim Cowboys",
        "Link account",
        "Add group",
        "/stax",
        "/status",
        "@heystax_bot what's up",
        "one-to-one Telegram conversation with the HeyStax bot",
        "Heystax (@heystax_bot)",
        "Example: Bob adds a private action",
        "Added to your default Stax.",
        "Example: Bob checks his private status",
        "Update a group action by replying to HeyStax",
        "Example: Bob marks the correct action done",
        "Replying to Heystax:",
        "If Bob sends `done` as a new standalone message",
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
        "Example 1: Bob starts a standup and everyone responds",
        "Standup roster: Bob, Alice, Nancy",
        "Example 2: Alice corrects her response",
        "Replace your existing standup response?",
        "Example 3: Nancy does not respond",
        "Missing: Nancy",
        "This group or sender is not authorized",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise SystemExit("Telegram help is missing: " + ", ".join(missing))

    linked_from = [
        ROOT / "README.md",
        ROOT / "topics" / "team-stax" / "index.md",
        ROOT / "topics" / "surfaces" / "index.md",
    ]
    for source in linked_from:
        if "telegram" not in source.read_text(encoding="utf-8").lower():
            raise SystemExit(f"Telegram guide is not linked from {source.relative_to(ROOT)}")

    surfaces = (ROOT / "topics" / "surfaces" / "index.md").read_text(encoding="utf-8")
    if "[**Telegram**](../team-stax/telegram)" not in surfaces:
        raise SystemExit("Surfaces page does not link to the canonical Telegram guide")

    print("Telegram help contract passed")


if __name__ == "__main__":
    main()
