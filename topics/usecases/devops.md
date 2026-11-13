---
nav_exclude: true
---

# On call: a production incident at 02:10

[← Back to Use Cases](index.md)

{% include badge-partial.html %}

The pager goes at 02:10. Errors on checkout. You need the dashboards, the logs, the runbook and the people, and you need them before your coffee.

## The stax

Priya keeps one stax ready for this, called **P1: checkout errors**.

| | |
|---|---|
| **Mission** | Customers can pay, day and night. |
| **Goal** | Checkout errors back under 1% within an hour of the page. |
| **Next Action** | Who does what next, on the board, with a name on each card. |

## What happens

1. **Open the cockpit.** Priya opens the stax's tabs with the TabStax extension: dashboards, logs, the deploy page, the runbook at the right section. One click, not ten minutes of links.
2. **Bring the team in.** Tom is on the stax as an editor. He sees the same cards and the same goal.
3. **Hand off from the chat.** In the incident Telegram group, Tom replies to the error screenshot with `/t @ops-builder`. The screenshot and the message land on a card for that agent role.
4. **Ask, don't wait.** The agent needs one fact. It comments on the card to `@priya`. She gets a Telegram DM and replies in plain words. The answer lands on the same card.
5. **Watch the board.** The `@ops-builder` column reads **Working**. When its fix is ready, the card shows **Open PR**. The rollback waits for Priya's go-ahead, because it cannot be undone.
6. **Hear back.** The finished notice in the group strikes itself through: **✓ Done by @ops-builder**.

## After

The stax holds the timeline: who did what, when, and why. Monday's review reads it instead of rebuilding it from a scrolled-away chat.

**You can check.** Every card, comment and go-ahead names the person or agent who wrote it.

## What works today

| Step | State |
|---|---|
| Open a stax's tabs with the TabStax extension | live |
| Share a stax with editors | live |
| `/t @agent` from a Telegram reply, with the screenshot on the card | live |
| An agent asks a person by comment; the Telegram DM and reply | live |
| Board columns, Working and Open PR on cards | partial: in the product, not yet seen signed in |
| A listener agent that picks up the card and opens the PR | partial: runs from the repo, not on npm yet |
| Go-ahead before work that cannot be undone | live |

Now you can switch into incident mode in one move, with every hand on the same cards.

[← Back to Use Cases](index.md)
