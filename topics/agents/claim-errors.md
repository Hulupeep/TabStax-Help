---
title: Claim errors and fixes
parent: AI Integrations (MCP)
nav_order: 6
---

# Claim errors and fixes

{% include badge-partial.html %}

An agent's claim was refused, or your own access change was. This page says which side to fix. The messages come from the production server code as of 2 November 2026, not yet confirmed in a browser run. [See what has been verified](../../docs/shipped-ledger).

## Why so many say "Stax not found"

An agent asking for something it cannot reach gets the same answer as for something that does not exist: `Stax not found` for stax and actions, `Record not found` for records.

That way a token cannot probe your account to learn what is there. The cost: you diagnose from your side, as owner, not from the agent's error.

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
| `ACTION_NOT_YOURS` | The role tried to close another role's card. | Comment on the card to its holder, the Chief or you. |
| `REOPEN_NOT_ALLOWED` | A role other than the Chief tried to reopen a done card. | File a new card, or ask the Chief with a comment. |
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

You changed or renewed an agent's access and got refused. The agent still holds claims made under its old access. Those end first, so no claim ever runs on authority it was not made under.

1. Run `agent_deauthorize` for that agent on that stax. Its claims are released.
2. Run `agent_authorize` with the level you want.
3. The agent claims again.

{% capture s %}
{% include anim/node.html x=90 y=60 label="Old access" sub="2 open claims" kind="agent" w=140 d=0 %}
{% include anim/edge.html x1=160 y1=60 x2=300 y2=60 kind="write" d=0.4 %}
{% include anim/node.html x=380 y=60 label="agent_deauthorize" sub="claims released" kind="person" w=160 d=0.8 %}
{% include anim/edge.html x1=380 y1=86 x2=380 y2=134 kind="write" d=1.2 %}
{% include anim/node.html x=380 y=160 label="agent_authorize" sub="the level you want" kind="person" w=160 d=1.6 %}
{% include anim/edge.html x1=300 y1=160 x2=170 y2=160 kind="dispatch" d=2.0 %}
{% include anim/node.html x=90 y=160 label="New access" sub="claims again" kind="agent" w=140 d=2.4 %}
{% include anim/trail.html x=40 y=240 who="You" what="deauthorized, then authorized work" when="10:02" d=2.8 %}
{% include anim/trail.html x=40 y=264 who="@builder" what="claimed the card again" when="10:03" agent="true" d=3.2 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 290" label="Old claims are released by deauthorize, new access is granted, then the agent claims again" caption="Deauthorize first: the old claims end. Authorize at the level you want. The agent claims again under its new access, and the trail shows both moves." svg=s %}

If `agent_deauthorize` returns `cleanup_pending` with `residual_action_ids`, some claims could not be released. Re-authorize stays refused until they are recovered. There is no self-serve fix yet: contact support with the stax and the action ids.

## An agent stopped mid-claim

If it claimed inside a run, the claim is released once the run stops sending heartbeats. A claim made outside a run stays put: complete the action yourself with `next_actions_complete`, or run `agent_deauthorize` to release it.

{% include badge-planned.html %} Coming next: you, or your Chief, will be able to free a claim held by an agent that is no longer working, without that agent. Its access ended, or it has no live run, so the card is no longer stuck behind it.

**You set the edges.** Most of these errors are the edges doing their job.

Now you can read a refusal and know which side to fix.
