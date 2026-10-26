---
title: Studio client handoff
parent: Scenarios
nav_order: 2
---

# A studio owner sees the handoff without chasing chats

{% include badge-partial.html %}

Nadia runs a small web studio. She owns the **Atlas website** Stax. Jo is the designer; Claude Code is the coding worker. A client review is coming, and the mobile menu needs a keyboard-accessible fix.

## The handoff

1. Nadia writes one Next Action on Atlas: “Make the mobile menu keyboard-accessible; attach the preview link.” Jo adds the design constraint to the shared work.
2. When Nadia starts Claude Code, it reads Atlas and claims the action as `@claude`. The action now has a named worker.
3. Claude Code reports **blocked**: “Need Jo's final focus-ring colour.” Nadia sees the exact dependency and asks Jo. HeyStax has not sent Jo a message automatically.
4. Jo settles the colour. Claude Code uses its coding tools to make the change and reports **done** with the preview link. Nadia checks the preview and decides what to tell the client.
5. On Friday, Nadia opens Atlas and sees the design decision, worker result and next client-facing step in one place.

{% include agent-action-flow.html start="Nadia adds the mobile-menu action" middle="@claude claims it" blocker="Jo's focus-ring colour is needed" end="Preview link is reported" caption="Nadia starts the worker; Atlas keeps its claim, Jo's open decision and the preview to check." %}

## What remains on Atlas

Nadia can see that Claude Code was waiting on Jo, what Jo decided and which preview needs her own review before contacting the client. [Her older daily-ops example](../usecases/sme-owner) is about switching app contexts; this scene follows a shared handoff.

## The boundary that matters

The pilot worker joins Staxes owned by Nadia's account. It cannot use this flow to join a Stax owned by a different customer. **It is not a confidential per-client grant inside Nadia's account:** a worker with her agent token can request to join another Stax she owns. Use a nonsensitive test Stax until tighter outside-user permission controls are ready.

| Step | State |
|---|---|
| Nadia and Jo keep a shared Stax and a Next Action | Existing HeyStax work record. |
| Claude Code joins under its own name, claims and reports | Deployed MCP/web pilot; **Partial** until the live journey in [release evidence](../../docs/evidence/agent-peers-2026-10-26) is checked. |
| Claude Code creates a preview | Its separate coding/deployment tools do that; HeyStax stores the link. |

{% include badge-planned.html %}

Per-Stax agent grants, automatic notice to Jo, and automatic client email are **planned**. Nadia remains the person who decides whether to contact the client.

## Try the verified part

Make an Atlas Stax and add the mobile-menu action. Ask your existing connected AI to read the action and add the design question. Save the named-agent claim as a pilot step until the live tool and browser checks pass.

**Your cognition stays yours:** Nadia can answer “where are we?” from Atlas rather than asking two chats.
