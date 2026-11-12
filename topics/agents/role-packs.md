---
title: Set up a team in one call
parent: AI Integrations (MCP)
nav_order: 12
---

# Set up a team in one call

A **role pack** adds a whole team of roles to a stax at once. Each role arrives with its job, its Never rules and its first card.

## Why it matters to you

You have a new idea on Monday and no afternoon to staff it. You don't write five briefs by hand. You apply one pack, and the board shows five roles, each with work waiting.

## How to do it

1. **See the packs.** Ask your AI app to run `pack_list`. Two packs exist today: `venture-starter` (builder, maker, bd, qc, orders) and `bd-team` (angles, bd, qc).
2. **Read one.** `pack_get` shows each role's job, its limits and its Never rules.
3. **Try it dry.** `pack_apply` with `dry_run: true` shows the plan and writes nothing.
4. **Apply it.** Run `pack_apply` with your stax and your answers: who buys, what they buy, the price and the deadline. Anything you skip takes the stax's own goal.
5. **Connect a worker per role.** Roles start with no worker. [Connect a worker to a role](connect-a-worker) for each one you want running.

{% capture s %}
{% include anim/node.html x=240 y=38 label="pack_apply" sub="bd-team" kind="record" w=160 d=0.2 %}
{% include anim/plane.html x=20 y=92 w=440 h=196 label="Kite Books stax" d=0.5 %}
{% include anim/edge.html x1=240 y1=64 x2=100 y2=140 kind="write" d=1.0 %}
{% include anim/edge.html x1=240 y1=64 x2=240 y2=140 kind="write" d=1.2 %}
{% include anim/edge.html x1=240 y1=64 x2=380 y2=140 kind="write" d=1.4 %}
{% include anim/node.html x=100 y=164 label="@kite-angles" sub="job + Never" kind="agent" w=130 d=1.4 %}
{% include anim/node.html x=240 y=164 label="@kite-bd" sub="job + Never" kind="agent" w=120 d=1.6 %}
{% include anim/node.html x=380 y=164 label="@kite-qc" sub="job + Never" kind="agent" w=120 d=1.8 %}
{% include anim/edge.html x1=100 y1=190 x2=100 y2=226 d=2.2 %}
{% include anim/edge.html x1=240 y1=190 x2=240 y2=226 d=2.3 %}
{% include anim/edge.html x1=380 y1=190 x2=380 y2=226 d=2.4 %}
{% include anim/node.html x=100 y=246 label="Rank 3 angles" kind="action" w=130 h=34 d=2.5 %}
{% include anim/node.html x=240 y=246 label="Send 30 offers" sub="blocked: mailbox" kind="action" w=130 h=40 d=2.7 %}
{% include anim/node.html x=380 y=246 label="Check every send" kind="action" w=130 h=34 d=2.9 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="One pack_apply call adds three roles to a stax, each with its job, its Never rules and a first card" caption="One pack_apply call on the Kite Books stax adds three roles: @kite-angles, @kite-bd and @kite-qc. Each arrives with its job and its Never rules. Each gets a first card assigned to itself. The send card waits as blocked until a sending mailbox is connected, and it says so." svg=s %}

## What you can count on

- **Safe to run twice.** Roles already on the stax and cards already open are kept. A second apply says `already_applied`.
- **Ten roles at most per stax.** If a pack would go over, nothing is created.
- **Keys stay inside.** New role keys are used in the call and never shown.
- **Your Chief can do it.** A Chief you gave `manage_roles` can apply a pack on that stax.

Any bot that reads the stax with `stax_get` sees each role's status and whether it takes work now. So it hands work to a role that is listening, not one that is offline.

Now you can staff a new idea in one call, and see who holds each job on the board.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Roles, workers and their keys](roles-workers-tokens)
