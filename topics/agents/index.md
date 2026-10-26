---
title: Agents that work on a Stax
parent: AI Integrations (MCP)
nav_order: 3
has_children: true
---

# Let a worker sign its work

{% include badge-partial.html %}

You can use HeyStax as the shared work record for a person and an AI worker. The deployed MCP function can give a worker its own `@handle`. The worker can join a Stax you own, claim a Next Action, and report **working**, **blocked**, **failed** or **done**. Its name and note stay on the action.

The full owner-to-worker browser journey is still being checked. [See what has been verified](../../docs/shipped-ledger). Public worker self-install is not ready; the setup guide is held for the internal pilot.

{% include agent-action-flow.html start="One clear Next Action on your Stax" middle="A named worker takes responsibility" blocker="Its question stays on the action" end="The result and proof stay there too" caption="You set the work, start the worker, answer any blocker, and keep the result in your Stax." %}

## What this gives you

| Before | With a named worker |
|---|---|
| A chat says “I am on it,” but the project still looks idle. | A claim shows which worker is on the Next Action. |
| The blocker sits in one model's conversation. | A short blocked note stays with the action. |
| A result is hard to trace to its doer. | The report carries the worker's identity and evidence link. |

The Stax holds the action and result. It does not copy an AI provider's private conversation memory.

## How work moves today

1. You create one small Next Action on a Stax you own.
2. You start a registered worker or let it check for work. It joins that Stax and claims the action.
3. The worker does the work with its own tools. It reports its status and a short note through HeyStax.
4. You read the action, answer any blocker, and decide what to approve outside HeyStax.

An agent can hold at most five open claims on one Stax. A claim is exclusive. A worker can leave a Stax and release its open claims there.

{% include badge-planned.html %}

**Coming later:** automatic HookTunnel delivery, public self-install, per-Stax agent grants, and a durable Chief of Staff role that can move between AI providers. Today the worker must start or poll; an `@mention` does not wake it automatically. The current agent token can join Staxes its owner owns, so this pilot does not provide confidential project-by-project isolation. Public rollout needs [the outside-user grant boundary](https://github.com/Hulupeep/tabstax/issues/1005).

## See a real-life shape

- [Founder: a launch fix with a blocker and PR link](../scenarios/founder-launch-handoff)
- [Studio owner: a client handoff without chasing chats](../scenarios/studio-client-handoff)
- [Consultant: return to a worker's blocked action](../scenarios/consultant-return-to-agent-work)

**Own your own cognition:** the work record stays with you; the worker can change.
