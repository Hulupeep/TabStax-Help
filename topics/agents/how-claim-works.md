---
title: How claim works
parent: AI Integrations (MCP)
nav_order: 4
---

# How claim works

{% include badge-partial.html %}

A claim is an agent saying "this one is mine". While it holds the claim, no other agent can take the action or hand it to someone else.

The claim rules went into production on 2 November 2026. Nobody has walked the owner and two-agent journey in a browser yet, so this page is badged. [See what has been verified](../../docs/shipped-ledger).

{% capture s %}
{% include anim/node.html x=70 y=40 label="Open" sub="unassigned" kind="action" w=110 %}
{% include anim/edge.html x1=125 y1=40 x2=175 y2=40 kind="dispatch" d=0.4 %}
{% include anim/node.html x=230 y=40 label="Claimed" sub="@worker" kind="agent" w=110 d=0.6 %}
{% include anim/edge.html x1=285 y1=40 x2=345 y2=40 kind="write" d=1.0 %}
{% include anim/node.html x=405 y=40 label="Reported" sub="working" kind="agent" w=110 d=1.2 %}
{% include anim/edge.html x1=405 y1=60 x2=405 y2=110 kind="write" d=1.6 %}
{% include anim/node.html x=405 y=130 label="Done" sub="by @worker" kind="action" w=110 d=1.8 %}
{% include anim/trail.html x=20 y=118 when="09:02" who="@worker" agent="true" what="claimed" d=2.2 %}
{% include anim/trail.html x=20 y=142 when="09:20" who="@worker" agent="true" what="reported working" d=2.5 %}
{% include anim/trail.html x=20 y=166 when="09:41" who="@worker" agent="true" what="reported done" d=2.8 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 180" label="A next action moves from open, to claimed, to reported, to done" caption="One action, four states. It starts open. @worker claims it. @worker reports progress. @worker reports done and the action closes. Each step is written with @worker's name and the time." svg=s %}

## Why it matters to you

Two bots on one stax will both grab the same easy task if nothing stops them. A claim stops them. You open the stax and see one name on each piece of work, not two half-done attempts.

## The rules

| Rule | What it means |
|---|---|
| You set the edges | An agent works a stax only after you run `agent_authorize` on it with your own token. |
| It joins first | The agent calls `stax_join` with its own token before it can claim. |
| Open work only | It can claim an action that is unassigned, or assigned to its own handle. Not one assigned to anyone else. |
| Five at a time | At most five open claims per agent on one stax. Finishing or releasing one frees a slot. |
| Locked once claimed | No other agent can claim it, and no agent can reassign it to someone else. |
| Only the claimer reports | `next_actions_report` works only for the agent that holds the claim. |
| Done closes it | A report with state `done` completes the action under the agent's name. |
| Release hands it back | `next_actions_claim` with `release: true` gives it up. Any assignment stays. |

## Access levels

You pick one when you call `agent_authorize`. Calling it again changes the level.

| Level | The agent can |
|---|---|
| `read` | Read the stax, join it and read its actions. It cannot claim. |
| `work` (default) | All of `read`, plus add, assign, claim, report and complete actions. |
| `full` | All of `work`, plus records and the audit log, if its token also has those scopes. |

## How a claim ends

1. **The agent reports done.** The action closes. `completed by` shows the agent.
2. **The agent releases it.** The action goes back to open.
3. **You mark it done yourself.** As owner you can complete any action with `next_actions_complete`.
4. **You deauthorize the agent.** `agent_deauthorize` ends its access and releases every claim it holds on that stax. The actions stay assigned to its handle until you change them in the web app.

## The one that catches people

You cannot re-authorize an agent while it still holds open claims on that stax. That includes changing its access level, and renewing access that expired.

The server refuses with `AGENT_CLAIMS_REQUIRE_RECOVERY`. Today the message you see says only the stax owner can change an agent's access, which is confusing when you are the owner. The real reason is the open claims.

**Fix:** have the agent finish or release its claims. Or run `agent_deauthorize`, which releases them, then `agent_authorize` again.

Why it works this way: a claim was made under one grant. Changing the grant while the claim is live would let old work carry new authority. Clearing the claims first keeps every claim tied to the access it was made under.

## If an agent goes quiet

Its claims stay with it. Nothing times them out today. You end them with `agent_deauthorize`, or complete the actions yourself. An agent cannot leave a stax on its own yet; you remove it.

{% include badge-planned.html %}

**Coming next:** claim leases. A claim will expire when the agent's run stops checking in, and the action will go back to the agent's queue for its next run. The design is written; it is not built.

## Where to look

- `next_actions_list` shows who holds each action, its last reported state and note.
- Each report note is also kept as a comment on the action.
- `agent_whoami`, called by the agent, shows its open claims per stax.
- Every claim, report, release and access change is written to the stax audit log with the agent's name. A way to read those events back over MCP or in the dashboard is planned.

Now you can let two agents loose on one stax and see who is on what.

**You set the edges.** The agent claims inside them, and the record of what it did stays on your stax.

## Next

- [Your agent's first claim](first-claim)
- [Claim errors and fixes](claim-errors)
- [Two agents hand work to each other](two-agents-end-to-end)
