---
title: Home
nav_order: 1
description: Help for HeyStax, the operational plane where people and agents work from one graph
permalink: /
---

# HeyStax

**Make things happen. Not merely get things done.**

Your work is scattered. A plan in a Claude chat. Thirty tabs. A group thread from Tuesday. None of them holds the whole. HeyStax is the **operational plane** for your work. One graph holds why each piece of work exists, the goal, and the next action. Every tool you use and every teammate, person or agent, works from that same graph.

{% capture s %}
{% include anim/node.html x=80 y=28 label="Claude chat" kind="note" %}
{% include anim/node.html x=240 y=28 label="30 tabs" kind="note" d=0.1 %}
{% include anim/node.html x=400 y=28 label="Group thread" kind="note" d=0.2 %}
{% include anim/plane.html y=88 h=104 d=0.3 %}
{% include anim/edge.html x1=80 y1=48 x2=390 y2=124 cx=300 cy=40 kind="write" d=0.5 %}
{% include anim/edge.html x1=240 y1=48 x2=390 y2=124 cx=330 cy=60 kind="write" d=0.6 %}
{% include anim/edge.html x1=400 y1=48 x2=390 y2=124 kind="write" d=0.7 %}
{% include anim/node.html x=390 y=150 label="Launch" sub="why: first customers" kind="stax" w=150 d=0.9 %}
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
{% include anim/figure.html max=520 viewbox="0 0 480 315" label="Scattered pieces of a project come together in one stax, and every tool reads the same next action" caption="Pieces of one project sit in a chat, thirty tabs and a group thread. HeyStax brings them into one stax: why it exists, the goal, and the next action. The dashboard, ChatGPT and Telegram all read that same action. The trail shows who added it, and from where." svg=s %}

---

## Own your own cognition

What you are doing, what comes next, why, and who is on it. That is your working state. It belongs to you.

| | |
|---|---|
| **It is yours** | Your context sits in your HeyStax account. It does not live inside one AI vendor's private chat memory. |
| **It travels** | The same stax opens in Claude, ChatGPT, Claude Code and the `hey` CLI. Switch models on Thursday. Lose nothing. |
| **You set the edges** | You decide who joins a stax, and you grant access to sensitive record fields one at a time. |
| **You can check** | Completed actions leave breadcrumbs. Every write names who made it. |

Agents extend your thinking. They never take custody of it.

---

## Why, goal, next action

Every stax answers three questions.

1. **Why does this work exist?** The stax holds its purpose in plain words.
2. **What result counts?** Goals say what must become true, with a date if it matters.
3. **What happens now?** A next action names one concrete move, and who makes it.

Keep next actions few. Three clear moves beat thirty vague ones. When a goal stalls, the next action is the question to ask, not a longer list.

→ [What is a Stax?](topics/what_is_a_stax)

---

## Where HeyStax lives

Same data. Every surface. Add an action in the terminal; it appears in the extension. Complete it through Claude; the dashboard reflects it.

| Surface | What it is | Best for |
|---|---|---|
| **TabStax** (Chrome extension) | Captures and restores your browser context as a named Stax | One-click context switching between projects |
| **Dashboard** ([dash.heystax.ai](https://dash.heystax.ai)) | Attention lanes, actions, collaboration and timesheets. Installable on your phone | Planning, prioritising, seeing the team's work |
| **Timesheets** ([dash.heystax.ai/time](https://dash.heystax.ai/time)) | Weekly hours, logged against each Stax | Time tracking that stays with the work |
| **Hey CLI** (`npm i -g heystax-cli`) | Next actions from your terminal: `hey "do the thing"`, `hey done 1` | Capturing a thought without leaving your tools |
| **MCP** (AI integrations) | Claude.ai, Claude Code, ChatGPT. Your AI reads and writes your Stax | Planning in conversation, with the result saved to your graph |
| **Share Pages** | Public URLs anyone can open or import | Team handoffs, onboarding, shared workflows |

---

## The reconstruction tax

Every time you return to a project, you rebuild it from scratch.

Which tabs. Which docs. Which tools. Where you left off. What to do next.

That's the **reconstruction tax**, and it compounds. The more projects you're holding, the more energy goes to *remembering* instead of *doing*. Projects drift. Momentum quietly dies.

Todo apps don't fix this. "Finish Q3 reporting" doesn't open the spreadsheet, the Slack thread, and the dashboard. It doesn't tell you where you stopped. It's a reminder without a runway.

HeyStax preserves your state so you can pick up any project cold. No reconstruction. No guilt spiral. Just the next action and the workspace it lives in.

→ [Read the full problem statement](topics/what_problem_tabstax_solves)

### See it in action

[![Watch HeyStax in action](https://img.youtube.com/vi/jcc-PsCdbM8/maxresdefault.jpg)](https://www.youtube.com/watch?v=jcc-PsCdbM8)

*Click to watch on YouTube*

---

## Where to start

### Just installed the Chrome extension?
→ [First time opening HeyStax](topics/first_time_opening_tabstax)
→ [Creating your first Stax](topics/creating_your_first_stax)

### Want to understand the system?
→ [The HeyStax mental model](topics/tabstax_mental_model)
→ [What problem HeyStax solves](topics/what_problem_tabstax_solves)

### Using the CLI or MCP?
→ [Hey CLI guide](topics/hey-cli)
→ [Connect to Claude.ai](topics/mcp-claude-ai)
→ [Connect to Claude Code](topics/mcp-claude-code)
→ [See how a named AI worker handles a Next Action](topics/agents/)
→ [Read founder, studio and consultant scenarios](topics/scenarios/)

### Someone shared a Stax with you?
They've captured a whole working context and handed it to you. Opening that Stax puts you in the same place they were: same structure, same tabs, same next actions. Trust it the way you'd trust a link: only from sources you trust.

### Using HeyStax with a Telegram group?
→ [Set up Telegram and see all supported commands](topics/team-stax/telegram)

---

## Hey CLI: your terminal

```bash
npm i heystax-cli

hey login
hey use "My Project"
hey "Build the feature"
hey ls
hey done 1
```

Leaving your terminal to capture a thought costs you context. The CLI keeps you in flow. Add an action here, complete it in the dashboard, see it in the extension. All the same Stax.

→ [Full Hey CLI guide](topics/hey-cli)

---

## AI integrations: your context in any model

HeyStax connects to AI assistants through the **Model Context Protocol (MCP)**. Your AI reads your projects, adds actions and marks things done, in plain conversation.

```
You: What are my next actions for the WebApp project?

Claude: Here are the pending actions for WebApp:
  1. Fix the auth timeout bug
  2. Review PR #42
  3. Update deployment docs
```

Works with **Claude.ai**, **Claude Code**, and **ChatGPT**. Connect once.

→ [Connect to Claude.ai](topics/mcp-claude-ai)
→ [Connect to Claude Code](topics/mcp-claude-code)

{% include badge-partial.html %}

**New agent peer pilot:** start a worker such as Codex or Claude Code under its own name. It can claim a Next Action and leave a blocked or done note on your Stax. [See the feature](topics/agents/) and [three everyday scenarios](topics/scenarios/). The full live journey is still being checked.

---

## Plans

| Plan | What you get |
|---|---|
| **Free** | Local-only extension, receive shared Stax |
| **Trial** | Full cloud sync, sharing, MCP access, cross-device |
| **Pro** | Everything in Trial, plus collaboration, timesheets, team features |

MCP access requires Trial or Pro.

---

## The one thing

Your brain should spend its energy doing the work. Not reconstructing where you were.

Pick one project. Save the tabs as a Stax. Add a next action. Tomorrow, open that Stax. Tabs load. Next action is right there. You're working in seconds.

That moment is a Flowful Re-entry. It is what HeyStax is here for.
