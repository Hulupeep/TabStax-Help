---
title: See what a worker reads before it starts
parent: AI Integrations (MCP)
nav_order: 14
---

# See what a worker reads before it starts

{% include badge-partial.html %}

When a worker takes a card, it gets the card's history before it writes a line: what was said, what was tried, and who said it.

## Why it matters to you

Gaia reports a bug in Telegram on Monday. By Wednesday it has two cards, three Claude Code sessions and a note from the Chief. At 02:00 a headless worker claims the next card. It used to start blind, so somebody explained it all again.

Now the worker reads that history first. You did not paste your context. It was already yours, and it travelled.

## What the worker reads

| Part | What it holds |
|---|---|
| **The card's notes** | Newest first. Forty runs that all say "still blocked" become one line with a count. The first diagnosis and the latest note are always kept. |
| **The reporter's words** | The Telegram report, with the message it answered and the screenshot link. |
| **Session summaries** | Five lines from each Claude Code session that worked the card or a related one. |
| **Related cards** | Cards on the same stax that share an issue number or two title words, plus the role's latest cards. |
| **Code history** | PRs named on the card or matching its title, recent commits and branches. Read with git and gh in the worker's own checkout. |

Each item says who wrote it and when, and links to where it came from. It is history, never orders. It stays under 8 KB, so the oldest and least related items are dropped first.

## How to use it

1. Connect the worker's folder. See [Connect a worker](connect-a-worker).
2. Install the [HeyStax plugin](claude-code-plugin) where you work in Claude Code, so your own sessions leave summaries.
3. Assign the card to the role. The listener's agent runs `heystax task show` first and reads all of it.
4. To check it yourself, run `heystax task show <card>` in the repo folder.
5. A worker over MCP calls `work_next` instead. One call takes the next card with its brief and history. `next_actions_context` reads the history of any card.

{% capture s %}
{% include anim/node.html x=90 y=48 label="Gaia: Telegram report" kind="surface" w=170 d=0.2 %}
{% include anim/node.html x=250 y=48 label="Alice: session summary" kind="surface" w=170 d=0.4 %}
{% include anim/node.html x=410 y=48 label="40 blocked runs" kind="note" w=130 d=0.6 %}
{% include anim/plane.html x=20 y=118 w=440 h=92 label="timebreez stax" d=0.8 %}
{% include anim/edge.html x1=90 y1=74 x2=200 y2=155 kind="write" d=1.0 %}
{% include anim/edge.html x1=250 y1=74 x2=240 y2=155 kind="write" d=1.2 %}
{% include anim/edge.html x1=410 y1=74 x2=280 y2=155 kind="write" d=1.4 %}
{% include anim/node.html x=240 y=168 label="Card history, one view" kind="action" w=200 h=34 d=1.8 %}
{% include anim/edge.html x1=240 y1=185 x2=240 y2=245 kind="dispatch" d=2.2 %}
{% include anim/node.html x=240 y=262 label="@timebreez-builder, 02:00" kind="agent" w=210 h=34 d=2.6 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A Telegram report, a session summary and forty repeated notes fold into one card history that the worker reads before it starts" caption="Gaia's report, Alice's session summary and forty identical blocked runs land on the stax. The worker that claims the card at 02:00 reads one short history, with the repeats folded into one line." svg=s %}

## Scenario

Gaia reports "unable to sign off on reconciliation" in Telegram, with a screenshot. Alice opens Claude Code at her desk, finds half the cause and closes the laptop. Her session leaves five lines on the card: what she was asked, what she changed, the result, what is next, and her branch.

At 02:00 `@timebreez-builder` claims the follow-up card. It reads Gaia's report, Alice's summary and her branch, opens her PR and finishes it. Gaia hears the verdict in Telegram. Nobody explained anything twice.

## What works today

| Step | State |
|---|---|
| Card history with folded repeats, Telegram report, related cards | live, read from a real card on 13 Nov 2026 |
| `work_next` | live in the MCP tool list, not yet used by a running worker |
| Session summaries from Claude Code | released 13 Nov 2026 with the [HeyStax plugin](claude-code-plugin), which is partial; not yet seen on a card |
| Code history in `heystax task show` | released in the CLI, not yet seen end to end |

Now you can hand a card to any worker, at any hour, and it starts where the last one stopped.
