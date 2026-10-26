---
title: Founder launch handoff
parent: Scenarios
nav_order: 1
---

# A founder hands off a launch fix and sees the proof

{% include badge-partial.html %}

Mara is a founder with a checkout release and a sales demo in the same afternoon. She owns a **Launch** Stax. One Next Action says: “Fix failed-payment retry and link the PR.” Codex is her coding worker.

## The handoff

1. Mara opens Launch. The action and its reason are there; she does not need to reconstruct the request from chat.
2. She **starts** her registered Codex worker and asks: “Read Launch. Claim the failed-payment retry action. If a product decision blocks you, report the question there.” Starting the worker is deliberate; the Stax does not wake it by itself.
3. In the agent peer pilot, Codex claims the action as `@codex`. Mara can see that the action has a named worker.
4. Codex needs to know which decline message to show. It reports **blocked** with that exact question. Mara makes the product decision and records it with the work.
5. Codex uses its coding tools to open a GitHub PR and reports the PR link on the action. Mara reviews and decides whether to merge. The action is marked done only when the work is done.
6. Before the demo, Mara opens Launch again. The question, decision and PR proof are together, even if the original Codex conversation is gone.

{% include agent-action-flow.html start="Mara writes one Launch action" middle="@codex claims it" blocker="Which decline message should appear?" end="PR link and done report appear" caption="Open → claimed by @codex → blocked on Mara's decision → done with a PR link. Mara starts the worker and decides whether to merge." %}

## What remains on Launch

The same Stax holds the original action, Codex's claim, Mara's decision and the PR link. The work can be read later without the private Codex conversation. [Mara's earlier tab-switching example](../usecases/remote-founder) shows how she moves between meetings; this scene follows one action through its handoff.

## What works now, and what is still being checked

| Step | State |
|---|---|
| A connected AI reads a Stax and its Next Actions | Live MCP capability; this story can be tried with an existing connection. |
| A separate agent identity joins, claims, reports and appears in its own column | Deployed pilot; **Partial** until a fresh authenticated tool list and signed-in browser run are recorded in [the release evidence](../../docs/evidence/agent-peers-2026-10-26). |
| Codex creates a PR | Codex and GitHub do this outside HeyStax. HeyStax holds the result link. |

{% include badge-planned.html %}

Automatic HookTunnel delivery, automatic merge approval and a public agent installer are **planned**. An `@mention` does not start Codex today.

## Try the verified part

Create a Launch Stax with one concrete action. Ask an already connected AI, “What is next on Launch?” and then “Add an action to check the checkout retry.” That uses the current user-connected MCP path. The named-worker claim flow above remains a pilot check until the live evidence is complete.

**Your cognition stays yours:** the work and the proof live on Launch, not in one Codex chat. [Learn how a named worker fits into HeyStax](../agents/); the setup guide is held for internal testers.
