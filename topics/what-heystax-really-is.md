---
title: What HeyStax really is
description: Why HeyStax exists, and how a stax holds people, roles, workers and outside agents on one mission.
---

# What HeyStax really is

**HeyStax is where people and agents work as one on a mission.**

## Why it exists

Intelligence is now abundant. An agent can build a site, write an app or draft a hundred emails before lunch. So what do we spend our time on?

A Victorian clerk spent the whole day copying ledgers by hand. Nobody would do that now. We are at the same turn. Much of the detail of building things, which we did ourselves until very recently, now belongs to agents.

Stepping back from the detail does not mean losing what matters. You keep the inspiration. You keep the journey. You keep the say on where it goes.

What changes is where you look. At the outcome, not the task. At the mission, not the pull request. The point is to make an impact on the world you live in.

HeyStax is built for that. It supports mission-led work, with people and agents working together as one. As one means toward the same mission and the same goals.

## How a stax is built

Every project is a **stax**: a set of people and agents working together toward one mission. A stax holds three things.

- **Mission:** why the stax exists.
- **Goal:** the result that would count, as a number or a date.
- **Next action:** the move someone makes now. Next actions live inside the stax.

And it holds the people and agents doing the work.

- **People** are on the stax by `@handle`.
- **Agents are roles**, such as `@builder` or `@outreach`. A role is the job, not the software.
- **Workers** fill a role: Claude Code, Codex, whatever you like. Swap a worker and the role carries on.
- **Outside agents**, such as Grok Bot, connect to the stax. They bring judgment into it and support the work.

{% capture s %}
{% include anim/plane.html x=10 y=16 w=350 h=296 label="Stax: Hubduck BD" %}
{% include anim/node.html x=110 y=78 label="Mission" sub="why it exists" kind="stax" w=180 d=0.3 %}
{% include anim/node.html x=280 y=78 label="Goal" sub="2nd paying school" kind="record" w=140 d=0.6 %}
{% include anim/node.html x=70 y=150 label="Colm" sub="person" kind="person" w=100 d=1.0 %}
{% include anim/node.html x=185 y=150 label="@builder" sub="role" kind="agent" w=110 d=1.2 %}
{% include anim/node.html x=300 y=150 label="@outreach" sub="role" kind="agent" w=100 d=1.4 %}
{% include anim/edge.html x1=185 y1=176 x2=185 y2=198 d=1.7 %}
{% include anim/edge.html x1=300 y1=176 x2=300 y2=198 d=1.8 %}
{% include anim/node.html x=185 y=214 label="Claude Code" kind="surface" w=104 h=30 d=1.8 %}
{% include anim/node.html x=300 y=214 label="Codex" kind="surface" w=90 h=30 d=1.9 %}
{% include anim/edge.html x1=185 y1=229 x2=110 y2=256 kind="dispatch" d=2.3 %}
{% include anim/edge.html x1=300 y1=229 x2=280 y2=256 kind="dispatch" d=2.5 %}
{% include anim/node.html x=95 y=274 label="Ship pricing page" kind="action" w=150 h=34 d=2.4 %}
{% include anim/node.html x=270 y=274 label="Send batch B" kind="action" w=150 h=34 d=2.6 %}
{% include anim/node.html x=420 y=150 label="Grok Bot" sub="outside agent" kind="agent" w=104 d=3.0 %}
{% include anim/edge.html x1=420 y1=124 x2=350 y2=78 cx=420 cy=78 kind="read" d=3.3 %}
{% include anim/edge.html x1=420 y1=176 x2=345 y2=274 cx=420 cy=274 kind="write" d=3.6 %}
<g class="hs-trail" style="--d:3.8s"><text x="378" y="230" class="hs-label">judgment</text></g>
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 320" label="Anatomy of a stax: mission and goal at the top, a person and two roles with workers, next actions inside, and an outside agent connecting in" caption="One stax, Hubduck BD. The mission and goal sit at the top. Colm is on it as a person. @builder and @outreach are roles, and Claude Code and Codex are the workers filling them right now. The next actions live inside the stax. Grok Bot sits outside, reads the goal and brings its judgment into the work." svg=s %}

Now you can swap any worker, add any person, or plug in another outside agent, and the mission, the goals and the next actions stay where they are.

## Activity is not progress

AI can produce astonishing quantities of code, pull requests, documents, messages and tasks. Activity is not the same as progress. The question that matters is: **Did we achieve what we set out to achieve?**

{% capture s %}
<g class="hs-trail" style="--d:0s"><text x="20" y="84" class="hs-label">Activity</text></g>
<g class="hs-dim" style="--d:2.6s">
{% include anim/node.html x=80 y=106 label="14 PRs" kind="note" h=28 d=0.1 %}
{% include anim/node.html x=80 y=140 label="500 emails" kind="note" h=28 d=0.3 %}
{% include anim/node.html x=80 y=174 label="38 tasks" kind="note" h=28 d=0.5 %}
{% include anim/node.html x=80 y=208 label="9 docs" kind="note" h=28 d=0.7 %}
{% include anim/node.html x=80 y=242 label="6 drafts" kind="note" h=28 d=0.9 %}
</g>
{% include anim/node.html x=330 y=40 label="Mission" sub="Why: build things people pay for" kind="stax" w=280 d=1.8 %}
{% include anim/edge.html x1=300 y1=66 x2=300 y2=100 kind="dispatch" d=2.4 %}
<g class="hs-trail" style="--d:2.8s"><text x="196" y="92" class="hs-label">Progress</text></g>
{% include anim/node.html x=270 y=120 label="Email 20 schools" kind="action" w=150 d=2.8 %}
{% include anim/node.html x=270 y=170 label="Pricing page" kind="action" w=150 d=3.0 %}
{% include anim/node.html x=270 y=220 label="Book 3 calls" kind="action" w=150 d=3.2 %}
{% include anim/edge.html x1=345 y1=120 x2=370 y2=160 kind="write" d=3.6 %}
{% include anim/edge.html x1=345 y1=170 x2=370 y2=170 kind="write" d=3.7 %}
{% include anim/edge.html x1=345 y1=220 x2=370 y2=180 kind="write" d=3.8 %}
<g class="hs-out" style="--d:4.4s">{% include anim/node.html x=420 y=170 label="Paying" sub="customers: 0" kind="record" w=100 d=1.1 %}</g>
{% include anim/node.html x=420 y=170 label="Paying" sub="customers: 1" kind="record" w=100 d=4.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 270" label="A pile of agent activity leaves the goal at zero; a mission picks three moves and the goal moves" caption="On the left, agents produce a pile: pull requests, emails, tasks, docs. The goal stays at zero. Then a mission arrives. It picks three moves that serve it, the pile fades, and the count of paying customers goes from zero to one." svg=s %}

HeyStax is the **operational plane for persistent intent**. Its purpose is to keep the mission, goals, working context, responsibilities, decisions and evidence together as people and AI agents change. It is not a replacement for your coding harness, CRM, communication tools or agent runtime.

Everything else supports mission, goal and next action: context, permissions, accountable ownership, evidence, relationships, and history.

A thousand completed actions can leave a goal untouched. One useful conversation might change everything.

## The complete loop we are building

1. Understand the mission and measurable outcome.
2. Work backwards from the result: what must become true?
3. Find the smallest useful next move and a qualified person or agent to do it.
4. Capture what actually happened with attributable evidence.
5. Ask whether the outcome moved, an assumption failed, or the evidence is still inconclusive.
6. Adjust the plan, assign the next move, and preserve enough context for someone else to resume cold.

The system must not manufacture an enormous unowned task queue or call a PR, a sent email or an agent's assertion a verified outcome.

## Business is one example, not the limit

Our founder's mission is commercial: build useful products, win customers, get paid, support a family and earn the freedom to keep creating. Often the hardest part is not building the software. It is finding people with a real need, creating trust and establishing a commercial relationship.

Your mission could be different:

- **Drug development:** move a medicine through research, evidence, clinical, manufacturing and regulatory requirements towards an FDA decision. Qualified experts and regulators retain their judgment and authority.
- **Small business:** acquire five paying customers, not merely send 500 emails.
- **Community project:** complete an accessible community facility, not merely hold meetings.
- **House build:** reach a construction milestone before planning permission expires, not merely accumulate quotes.

What they have in common is sustained, accountable pursuit of a meaningful result.

## People and agents work on the same intention

The mission must survive a handoff between colleagues and between AI providers. HeyStax should record what everyone is authorised to do, what they accepted, what happened, and who owns the next move.

**Own your own cognition.** The purpose, work state and decisions remain yours rather than living only inside one model vendor's private chat.

## What's available today and what's coming

The browser extension, dashboard, CLI and MCP integration already give access to Staxes and shared working context. Check the [shipped ledger](../docs/shipped-ledger.md) for the evidence and current status of particular capabilities.

**The fully autonomous, evidence-led outcome pursuit loop described here is the product vision, not a claim that the entire system is shipped.** Company-level causal plans, autonomous pursuit, verified commercial advancement and replaceable-worker journeys are being built and evaluated.

Read [the founder's statement](why-im-building-heystax) for the reason behind this direction.
