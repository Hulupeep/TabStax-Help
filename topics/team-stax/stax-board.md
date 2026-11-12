---
title: Read your stax board
parent: Team Stax
nav_order: 5
---

# Read your stax board

Open a stax and you land on its board. There is one column for each actor who can hold work: Unassigned, then the people, then the agent roles.

{% include badge-partial.html %}

## Why it matters to you

Monday, 08:00. Twelve open actions, two people, four agent roles. You need to know who holds what without opening a single card.

- **Every holder is a column.** People and agents sit side by side, addressed the same way by `@handle`.
- **Nothing is hidden.** Work that nobody holds sits in Unassigned, where you can't miss it.
- **Only workers.** Contacts the stax deals with, like a customer in its CRM, never get a column. They are not holding the work.
- **You can check.** Each card says who added it, who it is assigned to and who claimed it.

## How to read it

1. **Unassigned** comes first. Move each card in it to a person or a role.
2. **People** come next: the owner and everyone invited to the stax.
3. **Agent roles** come last. Each one shows its purpose, its status and whether a worker is connected.
4. With many columns, scroll the board sideways. The scrollbar sits just under the board, and each column scrolls on its own.
5. Type in the box at the foot of a column to add work straight to that person or role.
6. Use **Move to** on a card to hand it to someone else.
7. Drag a column by its top strip to move it, or use **‹ ›**. **Reset column order** puts it back.
8. Tap the **×** on a column to hide it. It moves to the **Hidden** row above the board. Tap its name there to bring it back.

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

**The onboarding stax.** Colm owns the timebreez stax. Gaia, a collaborator, runs customer onboarding. Sandra and Mella are the customer's staff, kept as CRM contacts. The board shows Unassigned, Colm, Gaia and the builder role. It does not show Sandra or Mella. A card that says "Ask Sandra for the rota" is Gaia's work, so Colm moves it to Gaia.

**The busy venture team.** Alice's stax has five agent roles. On a laptop the last role sits off to the right. She scrolls sideways under the board and reaches it. She doesn't have to scroll to the bottom of the longest column first.

**The quiet view.** Colm only wants to see his agent roles tonight. He drags his builder role to the front and hides Unassigned and the people columns, so the board shows the roles side by side. Tomorrow he taps **Show all**.

**The phone check.** Bob opens the stax on his phone on the train. The columns stack one under another, with the title and buttons on top. He moves one card to `@hubduck-bd` and puts the phone away.

## What works today

| Part | State |
|---|---|
| Unassigned, people and agent role columns, with add in place and Move to | live in the product |
| No columns for CRM contacts; work assigned to a contact shows in Unassigned | live in the product, not yet seen signed in |
| The board fits the window and each column scrolls on its own | live in the product, not yet seen signed in |
| Reorder columns by drag or ‹ ›, kept per stax in this browser | live in the product, not yet seen signed in |
| Hide a column with its ×, kept per stax in this browser | live in the product, not yet seen signed in |
| Agent role columns showing whether a worker is connected | web code deployed; signed-in display still to verify |

Now you can see who holds every piece of work on a stax in one look.
