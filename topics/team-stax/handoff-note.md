---
title: Say why when you hand a card on
parent: Team Stax
nav_order: 6
---

# Say why when you hand a card on

{% include badge-partial.html %}

When you move a card to someone, add a note. The note goes to them with the card.

## Why it matters to you

Colm parked a Hubduck idea three weeks ago. This morning he wants it built. He moves the card to `@chief-of-staff`, but the move carries no reason. The agent sees a card, not the intent.

A note fixes that. "Actually I want to build this. Find the tickets and see where we are." The why travels with the work, and you can read later what you asked and when.

## How to do it

1. Open the stax board.
2. On a card, pick a person or role in **Move to**.
3. A note box opens: **Note for @chief-of-staff (optional)**.
4. Say why. Press **Move and send note**.
5. Leave it empty and press **Move**: the card moves, nothing is sent.
6. To speak without moving, press **Comment** on any card. Pick who it is for under **For**.

{% capture s %}
{% include anim/plane.html x=20 y=30 w=440 h=240 label="Hubduck stax" d=0 %}
{% include anim/node.html x=110 y=110 label="Colm" sub="owner" kind="person" w=110 d=0.3 %}
{% include anim/node.html x=370 y=110 label="@chief-of-staff" sub="agent role" kind="agent" w=130 d=0.6 %}
{% include anim/edge.html x1=165 y1=110 x2=305 y2=110 cx=235 cy=70 kind="dispatch" d=1.0 %}
{% include anim/node.html x=240 y=200 label="Note: find the tickets, then build" kind="note" w=250 h=30 d=1.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="Colm moves a card to the chief-of-staff role, and a note saying why goes with it." caption="The card moves to @chief-of-staff, and the note goes with it. The agent reads it on its next check." svg=s %}

## Where the note lands

- **An agent** gets it on its next check, and a listening worker wakes up.
- **A person** gets a message from the HeyStax Telegram bot. A reply there comes back as a comment on the card.
- **Everyone on the stax** sees it on the card: "@hollywoodsign to @chief-of-staff".

## Scenarios

**Bring a parked idea back.** Colm moves the parked Hubduck card to `@chief-of-staff` with "I want to build this. Find the tickets." The chief finds three tickets and hands the build to `@hubduck-builder` with its own note.

**Ask a person a question.** Colm moves "Check the rota numbers" to Gaia with "Can you confirm before Friday?" Gaia gets it on Telegram and replies from there.

**Leave a word without moving.** A merge card sits with `@hubduck-builder`. Colm presses **Comment**, keeps **For** on the builder and writes "Hold the migration until School 2 books." The card stays where it is.

## What works today

| Part | State |
|---|---|
| A note box in **Move to**, sent to the new holder | live in the product, not yet seen signed in |
| **Comment** on any card with a **For** picker | live in the product, not yet seen signed in |
| Comments addressed to an `@handle`, delivered by the HeyStax Telegram bot or picked up by agents | live: agents and MCP clients can already do this, see [Bots and people message each other](messages.html) |

Now you can hand on the work and the reason together.
