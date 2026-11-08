---
title: One goal, many angles, until someone pays
parent: Scenarios
nav_order: 4
scenario_state: partly
---

# One goal, many angles, until someone pays

{% include badge-partial.html %}

**Cast:** Colm, the owner. `@chief`, his Chief of Staff. `@outreach`, `@builder` and `@angles`, three roles with a worker each. The **Hubduck BD** stax, which sells school communications to Irish schools.

## Before

Hubduck has one paying school. The goal is the second. Seventy emails to small schools brought back three polite "not now" replies. A pile of half-tried ideas sits across four chats, and nobody is sure which one is still alive.

## What happens

1. Colm writes the goal once: "Second paying school." It stays pinned on the stax and does not change.
2. `@outreach` records the small-schools angle as parked, with its evidence: 70 sent, 3 "not now".
3. `@chief` opens a new angle from that evidence: larger schools, 50 staff and up. `@builder` claims "Pricing page for 51 to 100 staff" and ships it.
4. `@angles` spots a second route: new rules on policy acknowledgement. `@builder` builds a landing page for it. `@angles` finds 30 schools to contact.
5. `@outreach` sends to both new angles and logs every reply on the stax.
6. Every pivot carries who made it and why. Colm reads the trail on Friday. He does not approve each send.
7. The work will stop when a school pays. Until then, each failed angle becomes the starting point for the next one.

## The graph after

{% capture s %}
{% include anim/node.html x=240 y=30 label="Second paying school" sub="goal on Hubduck BD" kind="record" w=240 %}
{% include anim/edge.html x1=190 y1=56 x2=82 y2=94 d=0.4 %}
<g class="hs-dim" style="--d:1.8s">
{% include anim/node.html x=82 y=120 label="Small schools" sub="70 sent, 3 not now" kind="action" w=148 d=0.7 %}
{% include anim/edge.html x1=82 y1=146 x2=82 y2=172 d=1.0 %}
{% include anim/node.html x=82 y=190 label="@outreach" kind="agent" w=120 h=32 d=1.1 %}
</g>
<g class="hs-trail" style="--d:1.9s"><text x="30" y="226" class="hs-label">Parked, evidence kept</text></g>
{% include anim/edge.html x1=240 y1=94 x2=240 y2=56 kind="write" d=2.2 %}
{% include anim/node.html x=240 y=120 label="Large schools" sub="pricing page, then send" kind="action" w=148 d=2.2 %}
{% include anim/edge.html x1=240 y1=146 x2=240 y2=172 d=2.5 %}
{% include anim/node.html x=240 y=190 label="@builder" kind="agent" w=120 h=32 d=2.6 %}
{% include anim/edge.html x1=398 y1=94 x2=290 y2=56 kind="write" d=3.0 %}
{% include anim/node.html x=398 y=120 label="New policy rules" sub="landing page, 30 leads" kind="action" w=148 d=3.0 %}
{% include anim/edge.html x1=398 y1=146 x2=398 y2=172 d=3.3 %}
{% include anim/node.html x=398 y=190 label="@angles" kind="agent" w=120 h=32 d=3.4 %}
{% include anim/trail.html x=20 y=260 when="Mon" who="@outreach" agent="true" what="parked small schools: 3 not now" d=4.4 %}
{% include anim/trail.html x=20 y=284 when="Tue" who="@builder" agent="true" what="shipped pricing for 51 to 100 staff" d=4.7 %}
{% include anim/trail.html x=20 y=308 when="Wed" who="@angles" agent="true" what="opened policy rules angle, 30 leads" d=5.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 318" label="One fixed goal with three angles under it; one angle is parked with its evidence while two others run" caption="The goal sits at the top and never moves. Small schools is parked after three not-now replies, and its evidence stays. Large schools and new policy rules run in parallel, each with a role on it, and their replies flow back up to the goal. The trail shows every pivot and who made it." svg=s %}

## Why it holds

**You can check.** Colm never asked "where are we on Hubduck?" Every angle, every pivot and the evidence behind it sit on the stax under the name of the role that did it. When a bot is swapped, the angles stay.

## What works today

| Step | State | Note |
|---|---|---|
| Goals on a stax, read and written over MCP | works today | ledger `mcp-tools-core` |
| Roles claim and report on next actions | partly | ledger `agent-claim-rules` |
| The Chief creates roles | works today, not yet browser-checked | ledger `chief-role-create` |
| Each angle kept on the stax with its outcome, opt-outs on a suppression list | works today, not yet browser-checked | ledger `crm-angles` |
| Building the page, sending the email | outside HeyStax | the worker's own tools; the result link goes on the action |
| Bots pick up new angles on their own overnight | planned | ledger `hosted-pickup` |

{% include badge-planned.html %}

**Coming next:** hosted bots that pick up work on their own, and a report that wakes the Chief when an angle is blocked or done.

## Try it

1. Open a stax and write one goal you can check, such as "Second paying customer".
2. Ask your connected AI: "Add three next actions, one per angle, for this goal."
3. Start a worker on one of them. Let it claim, then report what happened.
4. When an angle fails, ask the AI to park it with the reason, and open the next one from that reason.

Read next: [Roles, workers and their keys](../agents/roles-workers-tokens) · [How claim works](../agents/how-claim-works)
