---
title: Shipped ledger
nav_exclude: true
search_exclude: true
---

<!-- Generated from _data/ledger.yml by scripts/render_ledger.py. Do not edit by hand. -->

# Shipped ledger

Last checked: 2026-11-09. Source: `_data/ledger.yml`.

Help pages may only describe what this ledger says is live. `scripts/check_truth.py` enforces it on every pull request.

| State | Meaning | Count |
|---|---|---|
| `shipped` | Seen working in production by a person in a browser. Describe it as live. | 0 |
| `live` | Observed in production from outside. Describe it, but it still needs a browser check. | 14 |
| `unverified` | Code or data says it exists. Nobody has seen it in production yet. | 15 |
| `partial` | Part of it is live, or it is merged and waiting for production. Needs the Partial badge. | 9 |
| `planned` | Not in production. Needs the Planned badge and future tense. | 10 |

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
| Claim leases that expire when an agent run dies | a claim made inside a run is leased; if the run stops sending heartbeats the claim is released | tabstax#1071 migrations applied to production and mcp v32 deployed from main 8c105788 on 2026-11-08; production tools/list returned run_start, run_heartbeat and run_end; lease sweep cron runs every 30 s. Not walked in a browser. |
| Worker tokens, one per machine, enrolled with the role's own token | a role enrolls each machine it runs on as a worker with worker_register | Production tools/list returned worker_register on 2026-11-08 (mcp v32, tabstax#1071). A PAT is refused and a worker token cannot enroll another worker. Not walked end to end. |
| The Chief of Staff creates roles on a stax (roles_manage) | you grant manage_roles once per Stax; the Chief creates roles with role_create | tabstax#1127 migration 20261108140000 applied and mcp deployed from main 1779c06 on 2026-11-08; production tools/list returned role_create and agent_authorize.manage_roles, and role_create without the grant returned ROLES_MANAGE_NOT_GRANTED. A full create has not been walked. |
| Agent events the Chief reads: run ended, queue empty, claim escalated after 3 failures, no one home, worker missed | when a run ends, a worker runs out of work or an action fails three times, HeyStax records an event the Chief reads | Production MCP tools/list on 2026-11-09 includes agent_events_list and agent_queue_empty; tabstax#1071-#1073 are deployed (coordinator, 2026-11-09). Gate D, the end-to-end check, is running; no browser walk yet. A blocked report is not an event; it stays on the action. |
| Go-ahead on irreversible work: owner or a Chief with the go_ahead grant, never on its own proposal | irreversible work waits for a go-ahead from you or a Chief you granted go_ahead | tabstax#1134 deployed 2026-11-09 (coordinator); the production MCP tool list seen on 2026-11-09 includes next_actions_go_ahead. No browser walk yet. |
| Outreach angles, campaigns, stages and a suppression list on a stax (crm_* tools) | each angle is kept on the stax with its outcome; opted-out contacts go on a suppression list | tabstax#1126 merged and deployed 2026-11-08 13:56; production MCP tools/list includes crm_angle_upsert, crm_campaign_upsert, crm_stage_move, crm_suppression_add and crm_query, and crm_query counts on Hubduck Business Development returned an empty result on 2026-11-08. No angle has been recorded and read back yet. |
| Workers wait for work and pick it up on their own (wait_for_work); launchers with a pause switch and runs-per-hour cap | a worker waits for work and picks it up as soon as it is assigned; you can pause its launcher or cap its runs per hour | Production MCP tools/list on 2026-11-09 includes wait_for_work (paused, capped, retry_after_seconds), launcher_register, launcher_list and launcher_update; tabstax#1071-#1073 are deployed (coordinator, 2026-11-09). Gate D, the end-to-end check, is running; no browser walk yet. |

## Partial

| Capability | Docs wording | Evidence |
|---|---|---|
| Additional MCP tools awaiting fresh authenticated production verification: agent_activity, memory_capture, memory_import_ack, time_report, evidence requests | in the deployed function; verify before using | Bundled in production mcp v28 on 2026-10-26; fresh authenticated tools/list and behaviour check still needed |
| Timesheet approval by a lead | approval is coming | CHANGELOG: approval RPC added, production activation remains separate (tabstax root #976, web #142/#143) |
| Invoices from approved time, invoice nudges, invoice PDF | invoicing is partly built | CHANGELOG roots #978 and #982: production activation remains separate; render-invoice-pdf function exists; epic tabstax#354 |
| Owner-authorized agent assignment and private agent audit (tabstax#986) | internal pilot boundary; public grants remain planned | Migration 20261015020650 applied and catalog/RLS checks passed on 2026-10-25; outside-user boundary #1005 remains open |
| Memory capture and import (tabstax#932-934) | schema live; user journey unverified | All four 20261005 migrations applied and catalog-verified on 2026-10-25; fresh MCP behaviour check remains |
| Push wake to a launcher's URL when work is assigned (works today); @mention dispatch (planned) | a launcher with a push URL is woken when work is assigned to its agent; an @mention does not wake anyone yet | Production MCP tools/list on 2026-11-09 includes launcher_register (push_url) and push_deliveries_list (#1008 push audit); tabstax#1071-#1073 are deployed (coordinator, 2026-11-09). Gate D, the end-to-end check, is running; no browser walk yet. An @mention still does not wake anyone. |
| Agents with their own identity: agent_register, agent_whoami, stax_join, stax_leave, next_actions_claim, next_actions_report | agent peer commands are discoverable; claim/report and browser journey still need verification | Root PR #995 merged; mcp ACTIVE v28. Authenticated production initialize → initialized → tools/list returned all six names on 2026-10-26 (evidence/agent-peer-tools-list-2026-10-26.json); agent calls and owner/worker browser journey remain unverified (help #36). Claim/report races are tracked in tabstax#1011 |
| One column per agent on the stax page | web code deployed; signed-in display still to verify | webapps PR #198 merged and its main production deployment READY on 2026-10-25; signed-in agent-column browser check remains (help #36) |
| Claim rules for agents: owner access levels (read, work, full), five open claims per stax, locked once claimed, deauthorize releases claims, re-authorize refused while claims are open | claim rules are in production; the owner and two-agent journey still needs a browser check | tabstax main 74fbf44: migrations 20261027104402 (grants), 20261027201500 (claim/report), 20261028021204 and 20261028021206 (authority end), 20261029154500 (rejoin guard), 20261029200000 (add/assign); mcp agent-authorize.ts and agent-peers.ts. Release applied to production 2026-11-02. No owner or two-agent browser journey verified yet (help #50) |

## Planned

| Capability | Docs wording | Evidence |
|---|---|---|
| @heystax/hey CLI package | do not tell readers to install @heystax/hey yet | cli/package.json names @heystax/hey 0.1.0; npm returns Not found (2026-10-25) |
| Reading claim, report and release events back over MCP or in the dashboard | claim events are recorded; a way to read them back is planned | Claim, report, release and grant events are written to the stax audit log, but MCP stax_audit_log returns record events only (shared-stax.ts) and no dashboard audit view is observed (2026-11-02) |
| The /heystax-connect plugin that installs a listener with one question | planned | tabstax#1015; not confirmed in production as of 2026-11-09 |
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
- [ ] Claim leases that expire when an agent run dies
- [ ] Worker tokens, one per machine, enrolled with the role's own token
- [ ] The Chief of Staff creates roles on a stax (roles_manage)
- [ ] Agent events the Chief reads: run ended, queue empty, claim escalated after 3 failures, no one home, worker missed
- [ ] Go-ahead on irreversible work: owner or a Chief with the go_ahead grant, never on its own proposal
- [ ] Outreach angles, campaigns, stages and a suppression list on a stax (crm_* tools)
- [ ] Workers wait for work and pick it up on their own (wait_for_work); launchers with a pause switch and runs-per-hour cap
