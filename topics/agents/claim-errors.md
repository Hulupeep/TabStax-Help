---
title: Claim errors and fixes
parent: AI Integrations (MCP)
nav_order: 6
---

# Claim errors and fixes

{% include badge-partial.html %}

Every refusal an agent or owner can hit around claims, what it means and what to do. Taken from the production server code as of 2 November 2026; not yet confirmed in a browser run. [See what has been verified](../../docs/shipped-ledger).

## Why so many say "Stax not found"

When an agent asks for something it has no access to, the server answers as if the thing does not exist. `Stax not found` for stax and actions. `Record not found` for records.

That is deliberate. If "no access" and "does not exist" looked different, a token could probe your account and learn which stax and records are there. Identical answers tell it nothing. The cost is that you diagnose from your side, as owner, not from the agent's error.

## What the agent sees

| Message | What it means | What to do |
|---|---|---|
| `Stax not found` | One of: no access on this stax; access is `read` and the call needs `work`; access expired or was ended; the agent has not joined; the action id is wrong; a report sent an old `grant_generation`. | As owner, run `agent_authorize` with `work`. Have the agent run `stax_join`. Claim again to get the current `grant_generation`. |
| `Record not found` | The same, for records. | Grant `full`, and give the agent a token with record scopes. |
| `ACTION_ASSIGNED` | The action is assigned to someone else. An agent can claim only unassigned work or work assigned to its own handle. | Assign it to the agent first, in the web app or with `next_actions_assign`. |
| `ACTION_ALREADY_CLAIMED` | Another agent holds it. Also returned when any agent tries to reassign or unassign a claimed action. | Wait, or ask the holder to release it. |
| `CLAIM_LIMIT` | The agent already holds five open claims on this stax. | Finish one with a `done` report, or release one. |
| `GO_AHEAD_REQUIRED` | The action is flagged `needs_go_ahead` and nobody has approved it. | Ask the owner, or the Chief of Staff, to run `next_actions_go_ahead`. See [Work that cannot be undone](how-claim-works#work-that-cannot-be-undone). |
| `GO_AHEAD_NOT_GRANTED` | An agent tried to approve without the `go_ahead` grant, or on work it proposed, holds or is assigned. | The owner approves it, or grants `go_ahead` to a different role. |
| `ACTION_UNAVAILABLE` | The action is done, or the agent is reporting on an action it does not hold. | Check `next_actions_list`. Claim before you report. |
| `ACTION_NOT_CLAIMED_BY_AGENT` | A release on an action this agent does not hold. | Nothing to release. |
| `GRANT_GENERATION_REQUIRED` or `expected_generation must be a positive integer` | A report without the number from the claim reply. | Send `expected_generation` from the claim's `grant_generation`. |
| `request_id must be a UUID` or `INVALID_REPORT` | Missing or malformed report fields. State must be `working`, `blocked`, `failed` or `done`. Notes up to 2000 characters. | Fix the fields and send again. |
| `REQUEST_ID_REUSED` | The same `request_id` was sent with a different report. | One new UUID per report. Reuse it only to retry that exact report. |
| `ASSIGNEE_NOT_FOUND` or `ASSIGNEE_AMBIGUOUS` | The handle in `assign_to` is not on this stax, or matches more than one. | Use a handle from the stax's people list. |
| `Missing required scope: ...` | The agent's token lacks a scope, for example `actions:complete` for a `done` report. | Access level and token scopes are separate. Both must allow it. |
| `Agent tokens cannot call tool: next_actions_complete` | Agents finish work with a report, not this tool. | Send `next_actions_report` with state `done`. |
| `Agent tokens cannot call tool: stax_leave` | Agents cannot leave a stax on their own yet. | Ask the owner to run `agent_deauthorize`. |

## What the owner sees

| Message | What it means | What to do |
|---|---|---|
| `Only the stax owner can change an agent's access, for an active agent they registered` | One of: you do not own the stax; the agent is not yours or is inactive; **or the agent still holds open claims here** (`AGENT_CLAIMS_REQUIRE_RECOVERY`). | If you own both, it is the claims. Run `agent_deauthorize`, which releases them, then `agent_authorize` again. |
| `No active agent @name registered to you` | Wrong handle, or the agent belongs to another account. | Check the handle you registered. |
| `agent_authorize needs the stax owner's own token, not an agent token` | Called with an agent token. | Use your personal access token. |
| `expires_at must be in the future` | The end time you set has passed. | Pick a later time, or leave it out. |
| `assign_to, why and request_id need an agent token; assign people in the web app` | Owners assign in the web app today. | Assign from the stax page. |

## Re-authorize with open claims, in plain words

You changed an agent's access, or renewed it after it expired, and got refused. The agent still holds claims from its old access. Those claims have to end before new access starts, so that no claim ever runs on authority it was not made under.

1. Run `agent_deauthorize` for that agent on that stax. Its claims are released.
2. Run `agent_authorize` with the level you want.
3. The agent claims again.

If `agent_deauthorize` comes back with status `cleanup_pending` and a list of `residual_action_ids`, some claims could not be released automatically. Re-authorize stays refused until they are recovered. There is no self-serve fix for this yet; contact support with the stax and the action ids.

## An agent stopped mid-claim

If it claimed inside a run, the claim is released once the run stops sending heartbeats. A claim made outside a run stays put: complete the action yourself with `next_actions_complete`, or run `agent_deauthorize` to release it.

Now you can read a refusal and know which side to fix.

**You set the edges.** Most of these errors are the edges doing their job.
