---
title: Give a worker its own identity
nav_exclude: true
search_exclude: true
---

# Give a worker its own identity

{% include badge-partial.html %}

This is the **internal pilot** path for a worker such as Codex or Claude Code. All six worker commands appeared in an authenticated production MCP tool list on 26 October 2026. A complete owner, worker and browser journey has not yet been verified. [Public worker onboarding is not ready](https://github.com/Hulupeep/tabstax/issues/1005).

## The simple version

You make a Stax for a real project and add a small Next Action. You register a worker under its own name. When you start it, the worker reads the Stax, claims the action and reports back there. You can see the blocker or result without looking through its chat history.

> **Example request to your already connected worker:** “Open my Launch Stax. Tell me the open Next Actions. Claim ‘Fix the checkout retry’ if it is free. If you need a decision, report `blocked` with the question on that action. Put the PR link in your result.”

The worker's coding tools can create the PR. HeyStax records the claim and report; it does not merge or deploy the code.

## Pilot sequence

1. **Owner:** Create an owner-owned test Stax with a nonsensitive Next Action. Use a working HeyStax MCP connection. The plan requirement should be checked on your account before starting.
2. **Owner:** Use your own PAT with `agent_register` to create a worker name such as `codex`. The agent token is returned once. Put it only in that worker's secure MCP bearer-token setting. Do not paste it into a chat, URL, screenshot, issue or shell history. Do not give the worker your PAT.
3. **Worker:** Connect with its own agent token and call `agent_whoami`. Then use `stax_join` on the Stax you own, with a short line saying what it is responsible for.
4. **Worker:** Read the Stax and its open Next Actions. Call `next_actions_claim` on one free action, then refresh to confirm who holds it. Concurrent claims can race in this pilot; use one worker per action until [the atomic claim fix](https://github.com/Hulupeep/tabstax/issues/1011) lands.
5. **Worker:** Call `next_actions_report` with `working`, `blocked`, `failed` or `done` and a short note. A `done` report asks HeyStax to complete the action. The owner should check that the state and note appeared; action, comment and activity writes are not yet one transaction.
6. **Owner:** Check the action in HeyStax and decide the next move. If the worker leaves with `stax_leave`, refresh to confirm its open claims cleared.

{% include agent-action-flow.html start="Fix checkout retry on Launch" middle="@codex claims the open action" blocker="The decline-message question is recorded" end="PR link is reported on the action" caption="The worker checks for work when you start it; HeyStax keeps the claim, blocker and result on the same action." %}

## What to expect and what to check

| If you see... | Check this first |
|---|---|
| The worker is missing | Is it using its own agent token, and did it join this owner-owned Stax? |
| A token is rejected | Was the one-time token stored in the worker's secure bearer-token setting? Return to the owner if it was lost; this tool cannot display it again. Do not put a token in a URL. |
| “Stax not found” | This pilot agent can join a Stax owned by its owner account, not another customer's Stax. |
| “Already claimed” | Refresh the action to see the stored claimant. Ask the owner before moving work; do not start duplicate work. |
| `CLAIM_LIMIT` | Finish or release an open claim. The pilot checks a five-claim limit, but concurrent claims can pass that check together. |
| No reply while the worker is off | Start it or arrange a check. Automatic signed delivery is not live. |

{% include badge-planned.html %}

**Current access limit:** the pilot token is not a per-Stax grant. A worker with that token can request to join other Staxes the same owner owns. Use a nonsensitive test Stax and one worker per action until [Stax grants](https://github.com/Hulupeep/tabstax/issues/1013) and [atomic writes](https://github.com/Hulupeep/tabstax/issues/1011) are ready. Hosted wake-up and HookTunnel push are planned. You still approve external messages, merges, deployments and spending.

For a story that makes the flow concrete, see [Mara's launch handoff](../scenarios/founder-launch-handoff).
