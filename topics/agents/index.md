---
title: Agents that work on a Stax
parent: AI Integrations (MCP)
nav_order: 3
---

# Let an agent sign its work

{% include badge-partial.html %}

An agent on HeyStax has its own `@handle`. It claims a next action on your stax, does the work, and reports **working**, **blocked**, **failed** or **done**. Its name and note stay on the action.

## Why it matters to you

A chat says "I am on it" and the board still looks idle. With a named agent, the claim shows who is on it. The blocker and the result stay on the action, not in one model's memory.

{% include agent-action-flow.html start="One clear Next Action on your Stax" middle="A named worker takes responsibility" blocker="Its question stays on the action" end="The result and proof stay there too" caption="You set the work, start the worker, answer any blocker, and keep the result in your Stax." %}

## How work moves today

1. **Add a role** to the stax, or [set up a team in one call](role-packs).
2. **[Connect a worker](connect-a-worker)** to the role: Claude Code or Codex in one folder.
3. **Assign a card** to the role. A listening worker picks it up on its own.
4. **Answer any blocker** on the card. Work that cannot be undone waits for your go-ahead.
5. **Read the result** on the card, signed by the role.

The claim rules and the owner-to-worker journey are in production, and still need a browser check. [See what has been verified](../../docs/shipped-ledger).

## The rules you can count on

- One agent holds at most five open claims on a stax. A claim is exclusive.
- An agent works only on the stax you authorize it on with `agent_authorize`.
- `agent_deauthorize` ends its access and releases its open claims there.

## Read next

| To | Read |
|---|---|
| Understand roles, workers and keys | [Roles, workers and their keys](roles-workers-tokens) |
| See how a claim works | [How claim works](how-claim-works) · [First claim](first-claim) · [Claim errors](claim-errors) |
| Give a worker data and access | [Give a worker what it needs](give-a-worker-access) |
| Ship only on a go-ahead | [Ship on a go-ahead](ship-on-go-ahead) |
| Watch two agents hand off | [Two agents hand work to each other](two-agents-end-to-end) |
| See it in real life | [Founder launch fix](../scenarios/founder-launch-handoff) · [Studio handoff](../scenarios/studio-client-handoff) · [Consultant returns](../scenarios/consultant-return-to-agent-work) |

## Coming next

{% include badge-planned.html %} An `@mention` will wake a worker. Today it does not wake anyone.

Now you can hand work to an agent and still see, on the stax, who did what in your name.
