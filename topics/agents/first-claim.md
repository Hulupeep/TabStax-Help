---
title: Your agent's first claim
parent: AI Integrations (MCP)
nav_order: 5
---

# Your agent's first claim

{% include badge-partial.html %}

A ten-minute run on a throwaway stax. You see an agent claim a card, hold it, and close it under its own name.

The calls match the production tool list on 17 November 2026. Nobody has walked this exact run in a browser yet. [See what has been verified](../../docs/shipped-ledger).

{% capture s %}
{% include anim/node.html x=120 y=30 label="Your token" sub="owner" kind="person" w=130 %}
{% include anim/node.html x=360 y=30 label="Agent token" sub="@demo-worker" kind="agent" w=130 %}
{% include anim/node.html x=120 y=110 label="Register, authorize" kind="action" w=150 d=0.4 %}
{% include anim/edge.html x1=120 y1=56 x2=120 y2=90 kind="write" d=0.3 %}
{% include anim/edge.html x1=195 y1=110 x2=285 y2=110 kind="dispatch" d=0.8 %}
{% include anim/node.html x=360 y=110 label="Join, claim" kind="action" w=150 d=1.0 %}
{% include anim/edge.html x1=360 y1=56 x2=360 y2=90 kind="write" d=1.0 %}
{% include anim/node.html x=360 y=180 label="Report done" kind="action" w=150 d=1.4 %}
{% include anim/edge.html x1=360 y1=130 x2=360 y2=160 kind="write" d=1.3 %}
{% include anim/trail.html x=20 y=236 when="10:00" who="You" what="authorized @demo-worker to work" d=1.8 %}
{% include anim/trail.html x=20 y=260 when="10:01" who="@demo-worker" agent="true" what="claimed Write a two-line hello note" d=2.1 %}
{% include anim/trail.html x=20 y=284 when="10:04" who="@demo-worker" agent="true" what="reported done" d=2.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="You register and authorize an agent with your token; the agent joins, claims and closes the card with its own token" caption="With your token you register @demo-worker and let it work on one stax. With its own token the agent joins, claims the card and reports it done. The trail shows each step under the name that did it." svg=s %}

## What you need

- Your personal access token from the dashboard.
- An MCP client where you can switch the token it sends. The address is `https://dash.heystax.ai/api/mcp`.
- A way to make a UUID, such as `uuidgen`.

## Steps

**1. Register the agent.** *Your token.* Copy the `token` it returns. It is shown once.

```json
agent_register { "name": "demo-worker" }
```

**2. Make a throwaway stax and one card.** *Your token.*

```json
stax_create { "name": "Claim test" }
next_actions_add { "stax_id": "<stax id>", "title": "Write a two-line hello note" }
```

**3. Let the agent work there.** *Your token.*

```json
agent_authorize { "stax_id": "<stax id>", "handle": "demo-worker", "access": "work" }
```

**4. Join, find the card and claim it.** *Agent token.* Save `grant_generation` from the claim. Every report needs it.

```json
stax_join { "stax_id": "<stax id>", "accountable_for": "Hello notes" }
next_actions_list { "stax_id": "<stax id>" }
next_actions_claim { "action_id": "<action id>", "note": "Drafting now" }
```

**5. Watch a reassign get refused.** *Agent token.* Try to unassign the claimed card. You get `ACTION_ALREADY_CLAIMED`. The claim holds. The [two-agent run](two-agents-end-to-end) shows a second agent bounce off it.

```json
next_actions_assign { "action_id": "<action id>", "why": "test" }
```

**6. Report, then finish.** *Agent token.* A new UUID per report. Reuse one only to retry that same report.

```json
next_actions_report { "action_id": "<action id>", "state": "working",
  "note": "First line written", "request_id": "<uuid 1>", "expected_generation": <grant_generation> }

next_actions_report { "action_id": "<action id>", "state": "done",
  "note": "Hello. This note was written and closed by demo-worker.",
  "request_id": "<uuid 2>", "expected_generation": <grant_generation> }
```

**7. Check, then clean up.** *Your token.* The card is done, `completed_by_agent_id` is set, and both notes sit on it as comments.

```json
next_actions_list { "stax_id": "<stax id>" }
agent_deauthorize { "stax_id": "<stax id>", "handle": "demo-worker" }
```

**You can check.** Every step the agent took carries its name, not yours.

## If something says no

Most first-run refusals are `Stax not found`: the agent has not joined, or step 3 used `read`. See [Claim errors and fixes](claim-errors).

Now you can give a real agent a real stax and know what a good run looks like.
