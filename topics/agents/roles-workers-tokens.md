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

## Coming next: your Chief of Staff hires roles

{% include badge-planned.html %}

You will grant your Chief of Staff one permission per Stax, `manage_roles`. You do it once, with your own token. After that, the Chief creates new roles with `role_create` and never needs your key.

- A new role never gets more access than the Chief has on that Stax.
- It works on that one Stax only, and its access ends when the Chief's does.
- A Chief can create up to 10 active roles per Stax.
- Every role it creates is recorded as created by the Chief. You can end any of them.
- The Chief can't pass `manage_roles` on. Only you can grant it.

The chain then becomes: **your key → Chief of Staff → role → workers**. You set direction. The Chief staffs the work.

[See what has been verified](../../docs/shipped-ledger).
