---
title: Agent peer MCP release evidence
nav_exclude: true
search_exclude: true
---

# Agent peer MCP release evidence, 26 October 2026

This file supports the partial state in `_data/ledger.yml`. It contains no credentials or customer data.

## Confirmed

- `Hulupeep/tabstax` PR #995 merged the six agent peer tools: `agent_register`, `agent_whoami`, `stax_join`, `stax_leave`, `next_actions_claim`, `next_actions_report`.
- `Hulupeep/tabstax-webapps` PR #198 merged the Stax agent columns. Its production Vercel deployment was READY on 25 October.
- `supabase functions list --project-ref ayfhqcwzdqakxgkbzdpn --output json` on 26 October reported `mcp` ACTIVE, version 28, `verify_jwt=false`, updated at 09:41:38 UTC. The deployment command exited 0 from root commit `63b5a46e`.
- Local Deno tests for agent peers, Streamable HTTP notification handling and retired OAuth passed 23/23 before deployment. After deployment, both the direct Edge URL and `https://dash.heystax.ai/api/mcp` returned the expected HTTP 401 to an unauthenticated initialize request. An authenticated connected `stax_get` still returned the TabStax Stax.
- Production migrations needed by this deploy were applied and catalog-verified on 25 October; the linked dry run on merged main reported no queued migrations.

## Still required before calling the journey shipped

- Capture the six new names from a fresh **authenticated production** `tools/list`. The current connector's fixed tool catalog has not refreshed, and this shell has no `HEYSTAX_PAT`.
- With synthetic work on an owner-owned test Stax, register an agent, join, claim, report blocked and done, and check the resulting action and agent column in a signed-in browser. Record the date, account roles, tool responses and observed UI. Do not record tokens.
- Verify the negative owner boundary with a second account. Keep public agent onboarding blocked by tabstax#1005.

The deployed function is evidence of an available backend, not proof of the complete user journey. Until these checks pass, the help pages use the Partial badge and describe the manual/poll pickup path. Signed HookTunnel delivery and autonomous hosted workers remain Planned.

## Help page layout check

On 26 October, the shared scenario flow Sass compiled. A local Markdown/Liquid preview of the founder page was inspected in Chromium at 375px: document scroll width was 375px, its four open → claimed → blocked → result steps and caption remained readable, reduced motion set the animation to `none`, and dark mode kept the steps legible. This preview is not a Jekyll or production Pages build and does not satisfy the signed-in product journey above.
