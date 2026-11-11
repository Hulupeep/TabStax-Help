---
title: Home
nav_order: 1
description: Help for HeyStax. Persisted intent. Set the mission and the goal once. People and agents keep working it until it is done.
permalink: /
---

# HeyStax

**Persisted intent.**

A plan in a Claude chat. Thirty tabs. A group thread from Tuesday. None of them holds the whole.

HeyStax is the **operational plane** for your work. One graph holds why the work exists, the result you want, and the next move. Every tool and every teammate, person or agent, works from that same graph.

{% capture s %}
{% include anim/node.html x=80 y=28 label="Claude chat" kind="note" %}
{% include anim/node.html x=240 y=28 label="30 tabs" kind="note" d=0.1 %}
{% include anim/node.html x=400 y=28 label="Group thread" kind="note" d=0.2 %}
{% include anim/plane.html y=88 h=104 d=0.3 %}
{% include anim/edge.html x1=80 y1=48 x2=390 y2=124 cx=300 cy=40 kind="write" d=0.5 %}
{% include anim/edge.html x1=240 y1=48 x2=390 y2=124 cx=330 cy=60 kind="write" d=0.6 %}
{% include anim/edge.html x1=400 y1=48 x2=390 y2=124 kind="write" d=0.7 %}
{% include anim/node.html x=390 y=150 label="Launch" sub="mission" kind="stax" w=150 d=0.9 %}
{% include anim/node.html x=245 y=150 label="5 paying users" sub="goal" kind="record" w=120 d=1.1 %}
{% include anim/node.html x=95 y=150 label="Call Ana's school" sub="next action" kind="action" w=150 d=1.3 %}
{% include anim/node.html x=80 y=250 label="Dashboard" kind="surface" w=110 d=1.5 %}
{% include anim/node.html x=240 y=250 label="ChatGPT" kind="surface" w=110 d=1.55 %}
{% include anim/node.html x=400 y=250 label="Telegram" kind="surface" w=110 d=1.6 %}
{% include anim/edge.html x1=95 y1=176 x2=80 y2=230 kind="read" d=1.8 %}
{% include anim/edge.html x1=95 y1=176 x2=240 y2=230 kind="read" d=1.8 %}
{% include anim/edge.html x1=95 y1=176 x2=400 y2=230 kind="read" d=1.8 %}
{% include anim/trail.html x=20 y=304 when="09:14" who="You via Claude" what="added Call Ana's school" d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 315" label="Scattered pieces of a project come together in one stax, and every tool reads the same next action" caption="Pieces of one project sit in a chat, thirty tabs and a group thread. HeyStax brings them into one stax: the mission, the goal and the next action. The dashboard, ChatGPT and Telegram all read that same action. The trail shows who added it, and from where." svg=s %}

[What HeyStax really is](topics/what-heystax-really-is) · [Why I'm building it](topics/why-im-building-heystax) · [What is live today](docs/shipped-ledger)

## Mission, Goal, Next Action

Every stax answers three questions.

| | Asks | Example |
|---|---|---|
| **Mission** | Why does this work exist? | Launch the tutoring app |
| **Goal** | What result counts? | 5 paying users by March |
| **Next Action** | Who does what next? | Bob calls Ana's school |

Keep next actions few. Three clear moves beat thirty vague ones.

→ [What is a stax?](topics/what_is_a_stax)

## Own your own cognition

| | |
|---|---|
| **It is yours** | Your context sits in your HeyStax account, not inside one AI vendor's chat memory. |
| **It travels** | The same stax opens in Claude, ChatGPT, Claude Code and the `hey` CLI. |
| **You set the edges** | You decide who joins a stax and what each agent may do there. |
| **You can check** | Every write names who made it, person or agent. |

Agents extend your thinking. They never take custody of it.

## Where HeyStax lives

Add an action in the terminal and it shows in the dashboard. Complete it through Claude and the extension knows.

| Surface | What it does |
|---|---|
| **Dashboard** ([dash.heystax.ai](https://dash.heystax.ai)) | Attention lanes, actions, people. Installs on your phone. |
| **TabStax** ([Chrome extension](https://chromewebstore.google.com/detail/heystax/gfdcobncoohhlhppmoidalociahfdcam)) | Saves a stax's tabs and reopens them in one click. |
| **Hey CLI** (`npm i heystax-cli`) | Next actions from your terminal: `hey "do the thing"`, `hey done 1`. |
| **AI clients** (MCP) | Claude Code, ChatGPT and other apps that send your token read and write your stax. |
| **Timesheets** ([time.heystax.ai](https://time.heystax.ai/time)) | Weekly hours, logged against each stax. |
| **Telegram** | The HeyStax Telegram bot links a group to a stax. |
| **Share Pages** | Public links anyone can open or import. |

## Start here

- **New?** [Get started](topics/getting-started), then [create your first stax](topics/creating_your_first_stax).
- **Just installed the extension?** [First time opening TabStax](topics/first_time_opening_tabstax).
- **Live in a terminal?** [Hey CLI guide](topics/hey-cli).
- **Use an AI assistant?** [Connect Claude Code](topics/mcp-claude-code). It takes one command.
- **Run a team in Telegram?** [Set up the Telegram bot](topics/team-stax/telegram).
- **Someone shared a stax with you?** Opening it puts you where they were: same tabs, same next actions. Open shared stax only from people you trust.

## Agents work beside you

{% include badge-partial.html %}

Start a worker such as Codex or Claude Code under its own name. It claims a next action, reports a blocker or a result, and every step carries its name. The claim rules are in production. The full journey is still being checked in a browser.

→ [How agents work on a stax](topics/agents/) · [Scenarios](topics/scenarios/)

## See it in action

[![Watch HeyStax in action](https://img.youtube.com/vi/jcc-PsCdbM8/maxresdefault.jpg)](https://www.youtube.com/watch?v=jcc-PsCdbM8)

## Plans

| Plan | What you get |
|---|---|
| **Free** | Local-only extension, receive shared stax |
| **Trial** | Cloud sync, sharing, MCP access, every device |
| **Pro** | Everything in Trial, plus collaboration, timesheets and team features |

MCP needs Trial or Pro.

Now you can open any stax cold and know the next move in seconds.
