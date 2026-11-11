---
title: The HeyStax plugin for Claude Code
parent: AI Integrations (MCP)
nav_order: 10
---

# Work your stax from Claude Code

{% include badge-partial.html %}

The HeyStax plugin connects a Claude Code session to the role its folder works as. When a session opens, it tells Claude who it is working as and which cards are waiting. Two commands take those cards and report back to the stax.

## Why it matters to you

You open Claude Code at 08:00. You don't scroll back through yesterday's chat or paste the card in. Claude already knows it is `@timebreez-builder`, that two cards are waiting, and what it was halfway through.

When you close the laptop mid-card, the card goes back to the role with its last note on it. Nothing is left stuck as "working".

## Do you need it?

| You want | Use |
|---|---|
| Cards picked up while you are away | **Not the plugin.** Run `heystax listen --install --agent claude` in the folder. [Connect a worker](connect-a-worker). |
| Claude to take cards in a session you are watching | The plugin: `/heystax-work` or `/heystax-loop`. |
| Work you start yourself to show up on the stax | The plugin's standing order, or just `heystax connect` (it writes the same order for Codex). |

The plugin and the listener work side by side. The listener is for when you are away. The plugin is for when you are at the keyboard.

## Install it

1. Connect the folder first: [Connect a worker](connect-a-worker), steps 1 to 3.
2. In Claude Code, add the HeyStax repo as a plugin source: `/plugin marketplace add ~/path/to/tabstax` (your local copy of the HeyStax repo).
3. Install it: `/plugin install heystax@heystax`.
4. Open a new session in the connected folder. The first thing Claude sees is the role and what is waiting.

Check it any time with `/heystax-connect`. It says who this session works as, and what to do if the folder is not connected. It never asks you to paste a key into the chat.

## What it does

| When | What happens |
|---|---|
| **Session opens** | Claude is told which role and stax this folder works as, the standing order, any card already open in this folder, and how many cards are assigned to the role. If the owner paused the role, it is told not to pick up new cards. |
| **`/heystax-work`** | Takes the oldest card assigned to the role, claims it, does it, and reports: notes with the branch and PR as it goes, blocked if it needs a person, done with a one-line result. |
| **`/heystax-loop`** | The same, card after card. Waits up to 50 seconds for each new card. Stops after 10 cards (or the number you give), or after about 8 minutes with no work. |
| **You start your own work** | The standing order makes Claude put it on the stax first (`heystax task start`), then note and finish it there. |
| **Session closes** | An open card is handed back to the role with its last note, so another worker can pick it up. |

Claude only ever runs the `heystax` command, and `heystax` reads its own key. No key enters the chat.

{% capture s %}
{% include anim/node.html x=90 y=36 label="You" sub="open Claude Code" kind="person" w=150 %}
{% include anim/edge.html x1=165 y1=36 x2=230 y2=36 kind="dispatch" d=0.5 %}
{% include anim/node.html x=320 y=36 label="Session start" sub="role + 2 cards waiting" kind="surface" w=180 d=0.7 %}
{% include anim/edge.html x1=320 y1=62 x2=320 y2=96 kind="read" d=1.2 %}
{% include anim/node.html x=320 y=122 label="/heystax-work" sub="claims the oldest card" kind="agent" w=180 d=1.5 %}
{% include anim/edge.html x1=230 y1=122 x2=165 y2=122 kind="write" d=2.0 %}
{% include anim/node.html x=90 y=122 label="Card" sub="working, signed by the role" kind="action" w=150 d=2.2 %}
{% include anim/edge.html x1=90 y1=148 x2=90 y2=186 kind="write" d=2.8 %}
{% include anim/node.html x=90 y=212 label="Note + PR" sub="then done" kind="note" w=150 d=3.0 %}
{% include anim/edge.html x1=320 y1=148 x2=320 y2=186 kind="plain" d=3.4 %}
{% include anim/node.html x=320 y=212 label="Session ends" sub="open card goes back" kind="surface" w=180 d=3.6 %}
{% include anim/trail.html x=20 y=262 when="08:00" who="@timebreez-builder" agent="true" what="2 cards waiting" d=4.0 %}
{% include anim/trail.html x=20 y=286 when="08:41" who="@timebreez-builder" agent="true" what="done: export fixed, PR linked" d=4.6 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A Claude Code session with the HeyStax plugin: session start shows the role and waiting cards, /heystax-work claims one, notes and done land on the card, and an open card goes back when the session ends" caption="You open Claude Code in a connected folder. The plugin tells Claude its role and that two cards are waiting. /heystax-work claims the oldest. The card shows working, signed by the role, then a note with the PR and done. If you close the session mid-card, the card goes back to the role with its last note." svg=s %}

## Three mornings

**Bob takes the queue.** Bob opens Claude Code in his repo. It says two cards are assigned to `@timebreez-builder`. He types `/heystax-work`. Claude claims the first, fixes it, notes the PR and marks it done. Bob reads the result on the card from his phone.

**Alice starts something herself.** Alice asks Claude to tidy the import script. No card exists. Under the standing order, Claude runs `heystax task start "Tidy the import script"` first, so the work shows on the stax as hers and the role's. When she comes back next week, the note says where it got to.

**Sam goes to lunch.** Sam types `/heystax-loop 3` and leaves the session open. Claude works three cards in a row and posts a one-line update after each. One needs a price decision, so Claude marks it blocked with the question and moves to the next. The question waits on the card, not in a scrolled-away chat.

## When it goes wrong

| You see | What to do |
|---|---|
| "this folder is not connected" | Run `heystax connect` in a terminal in that folder, not in the chat. |
| "the heystax CLI is not installed" | Install it once: [Connect a worker](connect-a-worker), step 1. |
| "The owner has paused this role" | The role is paused on the board. Unpause it there, or leave it. |
| Cards wait but nothing happens while you are away | The plugin only works in an open session. Use `heystax listen --install`. |

## Coming next

{% include badge-planned.html %} Install from a public plugin directory, without a copy of the HeyStax repo.

Now you can open Claude Code and start on the right card, and every move lands on your stax under the role's name.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Roles, workers and their keys](roles-workers-tokens)
