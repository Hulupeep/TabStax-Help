---
title: What problem HeyStax solves
parent: Getting Started
nav_order: 2
---

[← Back to Help Home](/)

# What problem HeyStax solves

You lose momentum, not order. HeyStax keeps the state of the work so you can step back in.

## The reconstruction tax

You worked ten hours and never sent the one email. You were not careless. A switch broke the thread, and getting it back cost more than the work.

Every return to a project charges the same tax:

1. **Rebuild context.** Which tabs, docs and tools do I need open?
2. **Recover position.** Where did I leave off?
3. **Decide what is next.** What is the first thing to do?

The more projects you juggle, the more you spend remembering instead of doing.

## With other people, it is worse

Your teammate can't see what you have open or what you meant to do next. You can't see theirs.

So the team pays the tax together: status updates, standups, and "where are we on this?" asked again.

## What HeyStax keeps

{% capture s %}
{% include anim/node.html x=90 y=30 label="Which tabs?" kind="note" w=140 %}
{% include anim/node.html x=90 y=90 label="Where was I?" kind="note" w=140 d=0.2 %}
{% include anim/node.html x=90 y=150 label="What is next?" kind="note" w=140 d=0.4 %}
{% include anim/node.html x=90 y=230 label="Without a stax" sub="20 minutes back in" kind="person" w=150 d=0.6 %}
{% include anim/node.html x=360 y=60 label="Launch" sub="your stax" kind="stax" w=150 d=1.0 %}
{% include anim/edge.html x1=360 y1=86 x2=300 y2=150 kind="read" d=1.3 %}
{% include anim/edge.html x1=360 y1=86 x2=420 y2=150 kind="read" d=1.3 %}
{% include anim/node.html x=300 y=170 label="Tabs open" kind="surface" w=100 d=1.6 %}
{% include anim/node.html x=420 y=170 label="Next action" kind="action" w=100 d=1.7 %}
{% include anim/node.html x=360 y=230 label="With a stax" sub="one click back in" kind="person" w=150 d=2.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 270" label="Without a stax you answer three questions before you start. With a stax, one click opens the tabs and shows the next action." caption="Without a stax, every return starts with three questions: which tabs, where was I, what is next. With a stax, one click opens the tabs and shows the next action, so you start where you stopped." svg=s %}

A **stax** is one named piece of work. It holds:

| Part | What it gives you |
|---|---|
| Tabs | The pages for this work, reopened in one click by the TabStax extension |
| Next actions | The concrete step that gets you moving |
| Attention lane | Must, Should, Good or Meh, so you know where it sits |
| People and agents | Who is on it, each with an @handle |
| Trail | Who did what, and from where |

## One stax, every surface

The same stax opens in the dashboard, the TabStax extension, the hey CLI, Telegram, and AI apps over MCP. Add an action in the terminal. Close it from Claude. Reopen the tabs from Chrome. It is one piece of work.

Your context sits in your account, not inside one chat app.

Now you can step away from a project and come back without paying the tax.

**Next:** [What is a stax?](what_is_a_stax) · [Create your first stax](creating_your_first_stax) · [Surfaces](surfaces/)
