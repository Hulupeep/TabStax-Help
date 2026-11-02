---
title: Your agent's first claim
parent: AI Integrations (MCP)
nav_order: 5
---

# Your agent's first claim

{% include badge-partial.html %}

A ten-minute run on a throwaway stax. You will see a claim, a refused reassign and a completion, all under the agent's own name.

The calls below match the production server as of 2 November 2026. This exact run has not been checked end to end in a browser yet. [See what has been verified](../../docs/shipped-ledger).

## What you need

- Your personal access token (PAT) from the dashboard.
- An MCP client that lets you pick which token it sends. The address is `https://dash.heystax.ai/api/mcp`.
- A way to make a UUID, for example `uuidgen` in a terminal.

You will switch between two tokens: **yours** and **the agent's**. Each step says which.

## Steps

**1. Register the agent.** *Your token.*

```json
agent_register { "name": "demo-worker" }
```

Copy the `token` it returns. It is shown once.

**2. Make a throwaway stax and one action.** *Your token.*

```json
stax_create { "name": "Claim test" }
next_actions_add { "stax_id": "<stax id>", "content": "Write a two-line hello note" }
```

**3. Let the agent work there.** *Your token.*

```json
agent_authorize { "stax_id": "<stax id>", "handle": "demo-worker", "access": "work" }
```

**4. Join and find the work.** *Agent token.*

```json
stax_join { "stax_id": "<stax id>", "accountable_for": "Hello notes" }
next_actions_list { "stax_id": "<stax id>" }
```

**5. Claim it.** *Agent token.*

```json
next_actions_claim { "action_id": "<action id>", "note": "Drafting now" }
```

Save `grant_generation` from the reply. Every report needs it.

**6. Watch a reassign get refused.** *Agent token.* Try to take the claimed action off its holder by unassigning it:

```json
next_actions_assign { "action_id": "<action id>", "why": "test" }
```

You get `ACTION_ALREADY_CLAIMED`. The claim holds. Handing it to any other handle is refused the same way. In the [two-agent run](two-agents-end-to-end) you see a second agent bounce off it.

**7. Report progress, then finish.** *Agent token.* Use a new UUID per report. Reuse the same one only when retrying that report.

```json
next_actions_report { "action_id": "<action id>", "state": "working",
  "note": "First line written", "request_id": "<uuid 1>", "expected_generation": <grant_generation> }

next_actions_report { "action_id": "<action id>", "state": "done",
  "note": "Hello. This note was written and closed by demo-worker.",
  "request_id": "<uuid 2>", "expected_generation": <grant_generation> }
```

**8. Check what happened.** *Your token.*

```json
next_actions_list { "stax_id": "<stax id>" }
```

The action is done, `completed_by_agent_id` is set, and the two notes sit on the action as comments.

**9. Clean up.** *Your token.*

```json
agent_deauthorize { "stax_id": "<stax id>", "handle": "demo-worker" }
```

Now you can give a real agent a real stax and know what a good run looks like.

**You can check.** Every step above was written in the agent's name, not yours.

## If something says no

Most first-run refusals are `Stax not found`: the agent has not joined, or step 3 used the `read` level. See [Claim errors and fixes](claim-errors).
