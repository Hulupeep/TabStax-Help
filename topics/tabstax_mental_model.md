---
title: The HeyStax mental model
parent: Getting Started
nav_order: 2
---

[← Back to Help Home](/)

# <img src="../icons/tabstax-32.png" alt="HeyStax" width="32" height="32" style="vertical-align: middle; margin-right: 10px;">The HeyStax mental model

Most tools ask you to manage tasks. HeyStax asks you to hold intent: why the work exists, what would count as done, and the next move. People and agents both work from that same intent.

---

## Why, goal, next action

Every stax answers three questions, in this order:

1. **Why does this work exist?** That is the mission. One sentence.
2. **What result would count?** Those are the goals. Each one has a number or a date you can check.
3. **What is the next concrete move, and who makes it?** Those are the next actions, each with a person or an agent on it.

{% capture s %}
{% include anim/node.html x=240 y=30 label="Mission" sub="Support my family by building things people pay for" kind="stax" w=360 %}
{% include anim/edge.html x1=200 y1=56 x2=82 y2=88 %}
{% include anim/edge.html x1=240 y1=56 x2=240 y2=88 d=0.2 %}
{% include anim/edge.html x1=280 y1=56 x2=398 y2=88 d=0.4 %}
{% include anim/node.html x=82 y=114 label="10 paying schools" sub="goal: Hubduck" kind="record" w=148 d=0.6 %}
{% include anim/node.html x=240 y=114 label="First book sale" sub="goal: Waymarks" kind="record" w=148 d=0.8 %}
{% include anim/node.html x=398 y=114 label="20 Pro users" sub="goal: HeyStax" kind="record" w=148 d=1.0 %}
{% include anim/edge.html x1=82 y1=172 x2=82 y2=140 kind="write" d=1.4 %}
{% include anim/edge.html x1=240 y1=140 x2=240 y2=172 d=1.6 %}
{% include anim/edge.html x1=398 y1=140 x2=398 y2=172 d=1.8 %}
{% include anim/node.html x=82 y=198 label="Email 20 schools" sub="@outreach" kind="action" w=148 d=1.6 %}
{% include anim/node.html x=240 y=198 label="Make one book" sub="@book-maker" kind="action" w=148 d=1.8 %}
{% include anim/node.html x=398 y=198 label="Fix signup bug" sub="Claude Code" kind="action" w=148 d=2.0 %}
{% include anim/trail.html x=20 y=256 when="14:10" who="@outreach" agent="true" what="reported done: 20 sent" d=2.6 %}
{% include anim/trail.html x=20 y=280 when="14:12" who="You" what="asked: did the goal move?" d=3.2 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 290" label="One mission branches into three goals, each goal has a next action with an owner" caption="One mission at the top. Three goals under it, each a number you can check. Under each goal, the next move and who makes it. When @outreach reports done, the question goes back up the branch: did the goal move?" svg=s %}

When you come back to a stax, those three answers are waiting. You skip the ten minutes of working out where you were. That is the reconstruction tax, and the stax pays it for you.

A finished action is not the point. The point is whether the goal moved. If it did not, the next action changes. The mission stays.

---

## Think in projects, not tools

Old habit: open Notion, find the doc, check Jira, pull up the dashboard.

New habit: "I'm in the API Migration stax." The tabs, the next actions and the people are already inside it. You move between projects, not between apps.

---

## Everyone starts from the same place

Add Alice to a stax and she sees the same tabs, next actions and state as you. Connect Claude over MCP and it reads the same context. No "let me catch you up". No five links pasted into Slack.

---

## One clear next action beats thirty vague ones

The job of a stax is to answer "what do I do right now?". Open it, see the next action, do it. No scrolling, no triage.

---

## Why it works

| Idea | What it means for you |
|---|---|
| Working memory holds about four to seven things (Miller, 1956; Cowan, 2001) | Remembering where you left off spends that budget before real work starts. |
| Unfinished tasks keep looping in your head (Zeigarnik, 1927) | Once the next step is written down outside you, the loop lets go. |

A stax holds the context and the next step, so your head does not have to.

---

**Related guides:**
- [What problem HeyStax solves](what_problem_tabstax_solves): the core problem
- [What is a stax?](what_is_a_stax): the building block
- [Creating your first stax](creating_your_first_stax): step by step
- [Surfaces](surfaces/): how HeyStax works across browser, terminal, AI, and dashboard
