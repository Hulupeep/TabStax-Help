---
title: See which agents work on a stax
parent: AI Integrations (MCP)
nav_order: 12
---

# See which agents work on a stax

Agent access on a stax shows the agents on it, what each did there in the last 14 days, and which ones did nothing.

## Why it matters to you

You have eleven agents. Three of them run Timebreez. One stopped on 30 October and nobody noticed, because its cards just sat there.

You can check. Open the stax and the idle one is marked, next to the ones doing the work.

## How to read it

1. Open the stax settings and go to **People**. Only the stax owner sees **Agent access**.
2. Each agent shows its state, what runs it, its job and a line like `88 cards in 14 days · last active 1h ago`.
3. A card counts when the agent created, claimed or finished it here. Being handed a card does not count.
4. An agent with no cards in 14 days is marked **Idle 14 days**. Active agents come first. The rest sit under **Inactive**, each with a **What to do** line: restart it, give it a card, open its chat, connect a worker, or revoke it.
5. **Access** shows as one line, such as `read 3 · write 3`. Open it for the exact list.
6. Your other agents fold into **Add another agent**. Approve one there and it moves up with the others.

{% capture s %}
{% include anim/plane.html x=20 y=20 w=440 h=150 label="Agent access · Timebreez" d=0.1 %}
{% include anim/node.html x=95 y=100 label="@tb-builder" sub="Builder · 88 cards" kind="agent" w=130 d=0.4 %}
{% include anim/node.html x=240 y=100 label="@tb-grok" sub="Brain · 12 cards" kind="agent" w=130 d=0.6 %}
{% include anim/node.html x=385 y=100 label="@tb-qc" sub="Idle 14 days" kind="agent" w=130 d=0.8 %}
{% include anim/edge.html x1=385 y1=126 x2=385 y2=200 kind="read" d=1.2 %}
{% include anim/node.html x=385 y=222 label="What to do" sub="connect a worker" kind="action" w=140 d=1.5 %}
{% include anim/node.html x=140 y=222 label="You" sub="stax owner" kind="person" w=120 d=1.0 %}
{% include anim/edge.html x1=140 y1=196 x2=240 y2=126 kind="read" d=1.2 %}
{% include anim/trail.html x=20 y=284 when="09:02" who="You" what="opened Agent access, found @tb-qc idle" d=1.9 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 296" label="Agent access lists each agent on the stax with what runs it and its cards in 14 days; an idle agent gets a What to do line" caption="Agent access on the Timebreez stax lists each agent with what runs it and its cards in the last 14 days. @tb-builder and @tb-grok are working. @tb-qc has done nothing for 14 days, so it sits under Inactive with one fix: connect a worker." svg=s %}

## What runs each agent

| Word | Means | Cards given to it |
|---|---|---|
| **Builder** | A program on a computer, such as Claude Code in a project folder | Picked up within a minute |
| **Brain** | An outside chat or routine, such as a Grok bot with its own key | Picked up when its chat opens or its routine runs |
| **Not connected** | Nothing runs it | Wait |

Hover over the word, or tap it, to read this on the page. **Job** comes from the agent's brief on this stax.

Every agent says what it is when it registers. Bob's Grok bot shows **Brain · Grok**, what it does, "Created by you on 25 Nov 2026" and a link to its instructions. One registered earlier shows "Hasn't said what it is yet" until it next checks in.

Now you can see at a glance which agents carry a stax, and which ones only look like they do.

**Read next:** [Give a worker what it needs](give-a-worker-access) · [Connect a worker to a role](connect-a-worker)
