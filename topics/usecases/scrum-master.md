---
nav_exclude: true
---

# Scrum master: a standup that runs without you

[← Back to Use Cases](index.md)

You run standup for Team Falcon at 09:30. One morning you are sick. Without you the team freestyles: nobody opens the sprint goal, the bug filter is lost, and new starters stay quiet.

## The stax

Dana keeps one stax for it, called **Falcon standup**, shared with the whole team.

| | |
|---|---|
| **Mission** | The team leaves standup knowing who unblocks whom. |
| **Goal** | Every blocker named at standup has an owner by 10:00. |
| **Next Action** | One card per blocker, with a name on it. |

## What happens

1. **Open the room.** Whoever runs standup opens the stax's tabs with the TabStax extension: the board view, the sprint goal, today's bug filter, CI status. Same view for everyone.
2. **Know who is here.** In the team's Telegram group, `/who` lists everyone on the stax, people and agents, with the handle to use.
3. **Turn a blocker into a card.** Leo says the staging deploy is stuck. Dana, from bed, types `/t @leo fix the staging deploy`. It lands on the stax, assigned to Leo, under her name.
4. **Hand the dull part to an agent.** A reply to the CI failure with `/t @falcon-builder` puts the log screenshot on a card for that agent role.
5. **Check after.** Each card says who wrote it and who holds it. Tomorrow's standup starts from the cards, not from memory.

## After

Standup is a stax, not a person. Anyone can run it, and every blocker has a name beside it.

**You can check.** Every card names who added it, who holds it and what changed.

## What works today

| Step | State |
|---|---|
| Share a stax; open its tabs with the TabStax extension | live |
| `/who` and `/t @handle` in a Telegram group | live |
| `/t @agent` from a reply, with the screenshot on the card | live |
| An agent role that picks the card up on its own | partial: its listener runs from the repo, not on npm yet |

Now you can be off sick and still have a standup that ends with owners.

[← Back to Use Cases](index.md)
