---
title: Roles, workers and their keys
parent: AI Integrations (MCP)
nav_order: 8
---

# Hire roles, then give them workers

{% include badge-partial.html %}

A **role** is a job on a Stax, such as `@waymarks-bizdev`. A **worker** is whatever does that job right now: Grok Bot, Claude Code on your laptop, Codex on a server. You keep the role. You can swap the worker.

## Why it matters to you

You fire a bot on a Friday. On Monday a different one picks up the same role. It has the same mission, the same open actions and the same history, and you didn't re-explain anything.

Each key opens only what its holder needs, so your own key never sits inside a bot.

## The three keys

| Key | Who holds it | What it can do |
|---|---|---|
| **Your personal access token** | You, and nobody else | Everything you can do. It registers roles and sets their access. |
| **A role token** | The role's owner, usually your Chief of Staff | Acts as that role on the Stax you authorized it for. Enrolls workers. |
| **A worker token** | One machine or one bot | Acts as the role, under the role's limits. It can't enroll other workers. |

Each token is shown once. It goes straight into the bot's secret setting, for example its MCP bearer-token header. Never put it in a chat, a Stax, a screenshot or a file.

## How it works today

1. **You:** with your own token, call `agent_register` to create the role, then `agent_authorize` it on your Stax (`read`, `work` or `full`).
2. **The role:** with its role token, calls `stax_join` and says what it is accountable for.
3. **Each worker:** the role calls `worker_register` once per machine. That machine gets its own worker token.
4. **The worker:** starts a run, claims a Next Action and reports on it. If the machine dies, its claim is released when the run stops sending heartbeats, so the action doesn't stay stuck.
5. **You:** see every claim and report under the role's `@handle`, along with which worker did it.

To remove a worker, end its access. The role and its other workers carry on.

## Let your Chief of Staff hire roles

Grant your Chief of Staff one permission per Stax, `manage_roles`. You do it once, with your own token: `agent_authorize` with `manage_roles: true`. After that, the Chief creates new roles with `role_create` and never needs your key.

- A new role never gets more access than the Chief has on that Stax.
- It works on that one Stax only, and its access ends when the Chief's does.
- A Chief can create up to 10 active roles per Stax.
- Every role it creates is recorded as created by the Chief. You can end any of them.
- The Chief can't pass `manage_roles` on. Only you can grant it.

The chain is: **your key → Chief of Staff → role → workers**. You set direction. The Chief staffs the work.

{% capture s %}
<g class="hs-dim" style="--d:1.2s">{% include anim/node.html x=240 y=28 label="You" sub="mission + goal" kind="person" w=150 %}</g>
{% include anim/edge.html x1=240 y1=54 x2=240 y2=74 kind="write" d=0.4 %}
{% include anim/node.html x=240 y=100 label="@chief" sub="Chief of Staff" kind="agent" w=170 d=0.7 %}
{% include anim/edge.html x1=200 y1=126 x2=82 y2=164 kind="dispatch" d=1.4 %}
{% include anim/edge.html x1=240 y1=126 x2=240 y2=164 kind="dispatch" d=1.6 %}
{% include anim/edge.html x1=280 y1=126 x2=398 y2=164 kind="dispatch" d=1.8 %}
{% include anim/node.html x=82 y=190 label="@outreach" sub="role" kind="agent" w=140 d=1.6 %}
{% include anim/node.html x=240 y=190 label="@builder" sub="role" kind="agent" w=140 d=1.8 %}
{% include anim/node.html x=398 y=190 label="@angles" sub="role" kind="agent" w=140 d=2.0 %}
{% include anim/edge.html x1=82 y1=216 x2=82 y2=246 d=2.3 %}
{% include anim/edge.html x1=240 y1=216 x2=240 y2=246 d=2.4 %}
{% include anim/edge.html x1=398 y1=216 x2=398 y2=246 d=2.5 %}
{% include anim/node.html x=82 y=262 label="Grok Bot" kind="surface" w=110 h=32 d=2.4 %}
<g class="hs-out" style="--d:3.2s">{% include anim/node.html x=240 y=262 label="Codex" kind="surface" w=110 h=32 d=2.5 %}</g>
{% include anim/node.html x=240 y=262 label="Claude Code" kind="surface" w=110 h=32 d=3.2 %}
{% include anim/node.html x=398 y=262 label="Hermes" kind="surface" w=110 h=32 d=2.6 %}
{% include anim/edge.html x1=290 y1=164 x2=290 y2=126 kind="write" d=3.8 %}
{% include anim/planned.html x=400 y=291 d=3.8 %}
{% include anim/trail.html x=20 y=306 when="10:40" who="@builder" agent="true" what="reported blocked: which price band?" d=3.8 %}
{% include anim/trail.html x=20 y=330 when="10:42" who="@chief" agent="true" what="answered and assigned it back" d=4.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 340" label="You hand the mission to the Chief of Staff, who creates three roles; workers fill them and a blocker goes to the Chief" caption="You give @chief the mission and goal once, then step back. @chief creates three roles. A worker fills each one, and when Codex is swapped for Claude Code the @builder role stays. @builder gets blocked on a price band. The question goes to @chief, not to you, and @chief answers. Waking the Chief on a blocker is planned; today the Chief checks for blocked work." svg=s %}

Blockers stop at the Chief, not at you. The Chief answers, or hands the question to the role that can.

{% include badge-planned.html %}

**Coming next:** a blocked or done report will wake the Chief on its own. Today the Chief checks for blocked and done work each time it runs.

[See what has been verified](../../docs/shipped-ledger).
