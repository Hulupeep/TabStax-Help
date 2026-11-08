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
{% include anim/edge.html x1=82 y1=140 x2=82 y2=172 d=1.4 %}
{% include anim/edge.html x1=240 y1=140 x2=240 y2=172 d=1.6 %}
{% include anim/edge.html x1=398 y1=140 x2=398 y2=172 d=1.8 %}
{% include anim/node.html x=82 y=198 label="Email 20 schools" sub="@outreach" kind="action" w=148 d=1.6 %}
{% include anim/node.html x=240 y=198 label="Make one book" sub="@book-maker" kind="action" w=148 d=1.8 %}
{% include anim/node.html x=398 y=198 label="Fix signup bug" sub="Claude Code" kind="action" w=148 d=2.0 %}
{% include anim/edge.html x1=50 y1=172 x2=50 y2=140 kind="write" d=2.8 %}
{% include anim/trail.html x=20 y=256 when="14:10" who="@outreach" agent="true" what="reported done: 20 sent" d=2.6 %}
{% include anim/trail.html x=20 y=280 when="14:12" who="You" what="asked: did the goal move?" d=3.2 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 290" label="One mission branches into three goals, each goal has a next action with an owner" caption="One mission at the top. Three goals under it, each a number you can check. Under each goal, the next move and who makes it. When @outreach reports done, the question goes back up the branch: did the goal move?" svg=s %}

When you come back to a stax, those three answers are waiting. You skip the ten minutes of working out where you were. That is the reconstruction tax, and the stax pays it for you.

A finished action is not the point. The point is whether the goal moved. If it did not, the next action changes. The mission stays.

---

## Think in projects, not tools

Traditional thinking:
> "I need to open Notion, then find the doc, then check Jira, then pull up the dashboard."

HeyStax thinking:
> "I'm in the API Migration project." Everything else follows from that.

A Stax is the entry point for a project, not for a tool. You move between projects, not between apps. The tools are inside the Stax. You don't have to assemble them every time.

---

## Context is shared

This applies to your teammates and your AI agents, not just you.

When someone is added to a Stax, they get the same entry point: the same tabs, the same next actions, the same priority, the same state. When an agent connects via MCP, it reads the same context. No "let me catch you up." No five links pasted into Slack. The model doesn't change depending on who or what is accessing the project. It's always: name the project, find the state, take the next action.

---

## The constraint is the feature

HeyStax shows you a small number of next actions per project, on purpose. Not because it can't hold more, but because the job is to answer "what do I do right now?" not "what is everything that could ever be done?"

A Stax with one clear next action is more useful than a Stax with thirty vague ones. The constraint is what makes re-entry fast. You open a Stax, you see the next action, you do it. No scrolling. No triaging. No decision fatigue about which of forty-seven items to start with.

---

## The psychology

**Your working memory can only hold 4–7 things at once** (Miller, 1956; Cowan, 2001). Every time you try to remember where you left off (which tools, which docs, what you were about to do), you're burning through that budget before any useful work happens.

**The Zeigarnik Effect** (Zeigarnik, 1927) shows that unfinished tasks create mental tension. Your brain loops on them, trying not to forget. But the moment you have a clear, external plan for what to do next, the loop stops. You don't need to finish the task. You just need to trust that you've captured it and know the next step.

A Stax does both: captures the full context so your working memory is freed, and stores the next action so the Zeigarnik loop releases. Your brain stops trying to be a bookmark manager and a task tracker. It gets to just do the work.

---

## The model in one sentence

Your brain should spend its energy doing the work, not reconstructing where you were.

---

**Related guides:**
- [What problem HeyStax solves](what_problem_tabstax_solves): the core problem
- [What is a Stax?](what_is_a_stax): the building block of everything
- [Creating your first Stax](creating_your_first_stax): step by step with the TabStax extension
- [Surfaces](surfaces/): how HeyStax works across browser, terminal, AI, and dashboard
