---
title: Read your stax board
parent: Team Stax
nav_order: 5
---

# Read your stax board

Open a stax and you land on its board. There is one column for each actor who can hold work: Unassigned, then the people, then the agent roles.

{% include badge-partial.html %}

## Why it matters to you

Monday, 08:00. Twelve open actions, two people, four agent roles. You need to know who holds what without opening a card.

- **Every holder is a column.** People and agents sit side by side, each addressed by `@handle`.
- **Nothing hides.** Work nobody holds sits in Unassigned.
- **Only workers.** A customer in the stax's CRM never gets a column. They don't hold the work.
- **You can check.** Each card says who added it, who holds it and who claimed it. When an agent assigned it, the card says so: "assigned to @gayathrri0192 by @timebreez-bot".

## How to read it

1. **Unassigned** comes first. Move each card to a person or a role.
2. **People** come next. Your own column carries a **You** tag.
3. **Agent roles** come last. A role card says **Working · 2 blocked** while it is busy with others waiting, or **Stuck · 2 blocked** when nothing moves.
4. A card that names a PR or an issue shows an **Open PR** button into the stax's GitHub repo.
5. Type at the foot of a column to add work to that person or role. Use **Move to** to hand a card on. Soon you can [say why](handoff-note.html) as you do.
6. Drag a column by its top strip, or use **‹ ›**. Tap **×** to hide it; tap its name in **Hidden** to bring it back.

## Switch stax in one click

Under the stax header sit your **In mind** chips: stax you pinned, plus ones you worked on in the last 10 days, up to 7. Tap one to jump. Pin the stax you are on, or drop a chip. The list lives in this browser for now.

{% capture s %}
{% include anim/plane.html x=20 y=30 w=440 h=240 label="timebreez stax" d=0 %}
{% include anim/node.html x=85 y=110 label="Unassigned" sub="3 cards" kind="action" w=110 d=0.3 %}
{% include anim/node.html x=200 y=110 label="Colm" sub="owner" kind="person" w=100 d=0.6 %}
{% include anim/node.html x=310 y=110 label="Gaia" sub="collaborator" kind="person" w=100 d=0.9 %}
{% include anim/node.html x=410 y=110 label="@builder" sub="agent role" kind="agent" w=90 d=1.2 %}
{% include anim/edge.html x1=85 y1=136 x2=410 y2=136 cx=245 cy=200 kind="dispatch" d=1.6 %}
{% include anim/node.html x=245 y=230 label="Sandra (CRM contact): no column" kind="note" w=230 h=30 d=2.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A stax board: Unassigned, two people and an agent role as columns, with a card moving from Unassigned to the agent. A CRM contact has no column." caption="Unassigned, then people, then agent roles. A card moves from Unassigned to @builder. Sandra is a contact in the stax's CRM, so she has no column." svg=s %}

## Scenarios

**The onboarding stax.** Gaia runs onboarding on Colm's timebreez stax. Sandra and Mella, the customer's staff, are CRM contacts, so they get no column. "Ask Sandra for the rota" is Gaia's work, so Colm moves it to Gaia.

**The quiet view.** Colm wants only his agent roles tonight. He drags the builder role to the front and hides the rest. Tomorrow he taps **Show all**.

**The phone check.** Bob opens the stax on the train. The columns stack. He moves one card to `@hubduck-bd` and taps his next stax in **In mind**.

## What works today

| Part | State |
|---|---|
| Unassigned, people and agent role columns, with add in place and Move to | live in the product |
| No columns for CRM contacts; work assigned to a contact shows in Unassigned | live in the product, not yet seen signed in |
| The board fits the window and each column scrolls on its own | live in the product, not yet seen signed in |
| Reorder columns by drag or ‹ ›, kept per stax in this browser | live in the product, not yet seen signed in |
| Hide a column with its ×, kept per stax in this browser | live in the product, not yet seen signed in |
| "assigned … by @agent" on cards an agent assigned; a person's assign shows no "by" yet | live in the product, not yet seen signed in |
| **You** tag on your column; **Working** or **Stuck** with a blocked count on role cards | live in the product, not yet seen signed in |
| **Open PR** buttons on cards that name a PR, issue or link | live in the product, not yet seen signed in |
| **In mind** chips, kept in this browser | live in the product, not yet seen signed in |
| Agent role columns showing whether a worker is connected | web code deployed; signed-in display still to verify |

## Coming next

{% include badge-planned.html %}

A long mission and five goals push the board down the page, and its sideways scrollbar with it. A **scroll rail** with **‹ ›** arrows will sit right above the columns, so you can reach the right-hand roles the moment the page opens. Today, hold Shift and turn the mouse wheel over the board, or scroll down to its own scrollbar.

Now you can see who holds every piece of work on a stax in one look.
