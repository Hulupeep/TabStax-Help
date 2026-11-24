---
title: Hire a nightly reviewer
parent: AI Integrations (MCP)
nav_order: 18
---

# Hire a nightly reviewer

A **reviewer role** works while you sleep, looks at how your work is really going, and leaves you a few sharp cards by morning. It never builds anything itself.

## Why it matters to you

It is Monday, 08:00. Alice opens her stax on the bus. Her builder shipped three things last week. Nobody checked whether a new customer could get through signup without help.

A reviewer fills that gap. One run a night, one journey, at most three cards, each with the evidence that earned it. You decide what gets built. Your builders build it.

## What makes it a reviewer, not a builder

- **Its job lives on your stax.** The outcome, the journeys it may look at, and its Never rules sit in its brief. Swap the brain and the job stays.
- **It reads, then files.** It reads cards, comments and run history, then files cards. It does not push, merge or open a pull request.
- **You set the edges.** Its Never rules are yours. It cannot edit them.
- **It has a kill date.** Give it a short test window and a plain keep-or-kill rule.

## How to do it

1. **Register the role** as a Scheduled agent, with its platform and its job in one line.
2. **Give it work access** on one stax, with an end date for the test.
3. **Write its job** in the brief: the outcome, which journeys, what each card must carry.
4. **Add its Never rules:** no code, no pull requests, a card cap a night, evidence on every card.
5. **Give it one standing card** assigned to the role. Each night's run reports on it.
6. **Put it on a timer** with `heystax run` on your own machine, once a night, from a folder that is not a git repo. {% include badge-partial.html %}
7. **Judge it by results.** At the end of the window, count the cards you accepted that shipped.

{% capture s %}
{% include anim/node.html x=110 y=40 label="Real use" sub="cards, runs, notes" kind="record" w=150 d=0.2 %}
{% include anim/edge.html x1=110 y1=66 x2=240 y2=130 d=0.8 %}
{% include anim/node.html x=240 y=154 label="@acme-design" sub="02:30, one journey" kind="agent" w=160 d=1.1 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 kind="write" d=1.6 %}
{% include anim/node.html x=240 y=244 label="3 cards" sub="mockup + evidence" kind="action" w=170 h=40 d=1.9 %}
{% include anim/node.html x=380 y=40 label="Your Never rules" sub="no code, max 3" kind="record" w=150 d=0.5 %}
{% include anim/edge.html x1=380 y1=66 x2=250 y2=130 d=1.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="A nightly reviewer reads real use and files at most three cards" caption="At 02:30 the reviewer role reads how the stax was really used, inside the Never rules you set, scores one journey and files up to three cards. Each card has a before and after sketch and one line of evidence. Builders pick up the ones you want." svg=s %}

## What a good card from it looks like

- **The job it fails:** "A new founder cannot tell which role is working."
- **Before and after:** a small sketch of the screen today and the fix.
- **Evidence:** one line with its source, such as a card note or a run that stalled.
- **Done when:** one line anyone can check.

`heystax run` runs from the repo today; it is not on npm yet.

Now you can wake up to the few design fixes that matter, backed by what really happened, and keep your builders on the work you choose.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Give a role a skill](give-a-role-a-skill)
