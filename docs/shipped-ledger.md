---
title: Shipped ledger
nav_exclude: true
search_exclude: true
---

<!-- Generated from _data/ledger.yml by scripts/render_ledger.py. Do not edit by hand. -->

# Shipped ledger

Last checked: 2026-10-25. Source: `_data/ledger.yml`.

Help pages may only describe what this ledger says is live. `scripts/check_truth.py` enforces it on every pull request.

| State | Meaning | Count |
|---|---|---|
| `shipped` | Seen working in production by a person in a browser. Describe it as live. | 0 |
| `live` | Observed in production from outside. Describe it, but it still needs a browser check. | 14 |
| `unverified` | Code or data says it exists. Nobody has seen it in production yet. | 9 |
| `partial` | Part of it is live, or it is merged and waiting for production. Needs the Partial badge. | 5 |
| `planned` | Not in production. Needs the Planned badge and future tense. | 11 |

## Live

| Capability | Docs wording | Evidence |
|---|---|---|
| Web dashboard | the HeyStax dashboard at dash.heystax.ai | https://dash.heystax.ai/ and /attention return 200 (2026-10-25) |
| TabStax Chrome extension (save and reopen tabs for a stax) | the TabStax extension for Chrome | Chrome Web Store listing 'TabStax - Pick up where your mind left off' returns 200 (2026-10-25) |
| hey CLI | the hey CLI (npm install -g tabstax-cli) | npm tabstax-cli latest 0.1.11, published 2026-03-09 |
| MCP server | https://dash.heystax.ai/api/mcp (SSE: https://dash.heystax.ai/api/mcp/sse) | https://dash.heystax.ai/api/mcp returns 200; /api/mcp/sse returns 401 without auth; dash.tabstax.app/api/mcp 301-redirects to dash.heystax.ai (2026-10-25) |
| Claude.ai and Claude Code connect over MCP | Claude.ai and Claude Code | same endpoint as mcp-endpoint; connector pages exist (topics/mcp-claude-ai.md, topics/mcp-claude-code.md) |
| ChatGPT connects over MCP | ChatGPT | TabStax stax goal: ChatGPT MCP connector (tabstax#546) production-verified 2026-04-28; same endpoint live 2026-10-25 |
| Hosted API reference | the API reference at dash.heystax.ai/settings/mcp/swagger.yaml | https://dash.heystax.ai/settings/mcp/swagger.yaml returns 200 (2026-10-25) |
| MCP tools: stax, next actions, goals, dates, people | read and write stax, next actions, goals, dates and people | Live tools/list seen through a connected HeyStax MCP client on 2026-10-25: stax_list/get/create/update/delete, stax_audit_log, next_actions_list/add/update/complete/delete, goals_*, dates_*, people_* |
| MCP tools: records, record grants, record audit log | typed records, with grants and an audit log | Live tools/list on 2026-10-25: record_add/get/list/update/delete, record_grant, record_audit_log, records_schema_get |
| Today set (pick today's actions) | your Today list | Live tools/list on 2026-10-25: today_get, today_set, today_clear |
| Shared stax with roles and @handles | share a stax and assign by @handle | stax_get on the TabStax stax returns people with roles owner and agent and @handles (2026-10-25) |
| Attention lanes (Must, Should, Good, Meh) | Must, Should, Good, Meh | stax_get returns attention.priority and lane_position (2026-10-25) |
| Weekly timesheets per stax | timesheets at time.heystax.ai | https://time.heystax.ai/time returns 200 (2026-10-25) |
| Agents listed as people on a stax with an @handle | agents appear on the people list | stax_get on the TabStax stax lists @glenda with role agent (2026-10-25) |

## Unverified

| Capability | Docs wording | Evidence |
|---|---|---|
| MCP needs a Pro or Trial plan | MCP needs a Pro or Trial plan | supabase/functions/mcp/caller-identity.ts returns PLAN_REQUIRED for plans other than pro and trial (tabstax c3c18c1) |
| Project Settings page (description, goals, people, dates, grants) | Project Settings | Stax settings redesign epic tabstax#901 marked done on the TabStax stax |
| Breadcrumbs (completed actions as a trail) | breadcrumbs | Described in tabstax-capabilities.md; not observed |
| Telegram group to stax, personal linking, actions from messages, standups | the HeyStax Telegram bot (@heystax_bot) | t.me/heystax_bot resolves to 'Heystax'; migrations 20260717-20260720 telegram_*; help page merged 2026-07-20 (TabStax-Help PR #8) |
| Pro plan purchase through Stripe | upgrade to Pro | supabase/functions/stripe-webhook exists; prices not checked |
| Records in the dashboard | records | Account Records tabstax#688 in progress in May roadmap; MCP record tools are live |
| A page in the dashboard showing the audit trail | the trail | stax_audit_log and record_audit_log are live over MCP; no dashboard view observed |
| @glenda, the HeyStax guide agent | @glenda | Migration 20260928140000_glenda_agent.sql (#926); @glenda present on a prod stax; behaviour not observed |
| Agent registration, HookTunnel provisioning, @mention dispatch, comment writeback | mention an agent on an action | Migrations 20260401160000_agent_hooktunnel_linkage, 20260402094500_agent_dispatch_audit; architecture-overview lists as implemented |

## Partial

| Capability | Docs wording | Evidence |
|---|---|---|
| MCP tools merged but not in the live list: agent_activity, memory_capture, memory_import_ack, time_report, evidence requests | not yet available | Defined in supabase/functions/mcp/index.ts (tabstax c3c18c1); absent from live tools/list for an owner token on 2026-10-25 |
| Timesheet approval by a lead | approval is coming | CHANGELOG: approval RPC added, production activation remains separate (tabstax root #976, web #142/#143) |
| Invoices from approved time, invoice nudges, invoice PDF | invoicing is partly built | CHANGELOG roots #978 and #982: production activation remains separate; render-invoice-pdf function exists; epic tabstax#354 |
| Owner-authorized agent assignment and private agent audit (tabstax#986) | coming | CHANGELOG: production activation remains separate; migration 20261015020650 pending in prod rollout |
| Memory capture and import (tabstax#932-934) | not yet available | Migrations 20261005120000-150000 partly hand-applied; rollout step 2c pending |

## Planned

| Capability | Docs wording | Evidence |
|---|---|---|
| @heystax/hey CLI package | do not tell readers to install @heystax/hey yet | cli/package.json names @heystax/hey 0.1.0; npm returns Not found (2026-10-25) |
| Agents with their own identity: agent_register, agent_whoami, stax_join, stax_leave, next_actions_claim, next_actions_report | agents that join under their own name (planned) | tabstax#994, PR #995 open; tools absent from main and from live tools/list (2026-10-25); prod rollout steps 2a-2e pending |
| One column per agent on the stax page | planned | tabstax-webapps PR #198 open |
| Hosted bots pick up work on their own; /heystax-connect; pause switch and runs-per-hour cap | planned | tabstax#1015, #1016, blocked on #995 |
| @notify Telegram agent | planned; say 'the HeyStax Telegram bot' for what exists | Roadmap FEAT #696 / #682 not started in May snapshot; the Telegram bot is a separate shipped surface |
| @scribe email agent, email replies routed to actions, Action Response Primitive | planned | tabstax#567, #572, #681; stax description says ready to roll, not shipped |
| @meetbot, @pulse, @librarian, @foreman, @scout, @ledger, @refine, @steadyhand | planned | Roadmap post-M4 capabilities #711, #712, #716, #725, #730, #733 |
| Goal Verdict | planned | tabstax#609 open goal |
| Practices runtime | planned | Roadmap #727 / #728 not started |
| Executive Function Layer, hey next, Capacity Share | planned | Roadmap #739, #740, #741 not started |
| Stax composition and cascade awareness | planned | Roadmap #737, #738 not started |

## Browser checks for Colm

Tick each one after seeing it work in the product, then move its row to `shipped` (or down to `partial` / `planned`) in `_data/ledger.yml`.

- [ ] Web dashboard
- [ ] TabStax Chrome extension (save and reopen tabs for a stax)
- [ ] hey CLI
- [ ] MCP server
- [ ] MCP needs a Pro or Trial plan
- [ ] Claude.ai and Claude Code connect over MCP
- [ ] ChatGPT connects over MCP
- [ ] Hosted API reference
- [ ] MCP tools: stax, next actions, goals, dates, people
- [ ] MCP tools: records, record grants, record audit log
- [ ] Today set (pick today's actions)
- [ ] Shared stax with roles and @handles
- [ ] Attention lanes (Must, Should, Good, Meh)
- [ ] Project Settings page (description, goals, people, dates, grants)
- [ ] Breadcrumbs (completed actions as a trail)
- [ ] Telegram group to stax, personal linking, actions from messages, standups
- [ ] Weekly timesheets per stax
- [ ] Pro plan purchase through Stripe
- [ ] Records in the dashboard
- [ ] A page in the dashboard showing the audit trail
- [ ] Agents listed as people on a stax with an @handle
- [ ] @glenda, the HeyStax guide agent
- [ ] Agent registration, HookTunnel provisioning, @mention dispatch, comment writeback
