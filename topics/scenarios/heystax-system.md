---
title: The whole system in 90 seconds
parent: Scenarios
nav_order: 5
scenario_state: partly
---

# The whole system in 90 seconds

{% include badge-partial.html %}

**Cast:** Colm, the owner. A Chief of Staff and three roles on the **Hubduck** stax: Marketing, Business Development and Builder. Grok Bot, Hermes, Claude Code and Codex fill those roles as workers. Names and numbers in the film are illustrative.

## Before

The goal is clear: a second school pays by 20 November. The route is not. Ideas live in four chats, and every bot needs the story told again.

## Watch it

<div class="hs-film" style="position:relative;width:100%;aspect-ratio:16/9;border:1px solid var(--border-color, #ddd);border-radius:8px;overflow:hidden">
  <iframe src="{{ '/assets/animations/heystax-system.html' | relative_url }}" title="HeyStax system animation: one goal, four roles, workers coming and going until a school pays" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy"></iframe>
</div>

[Open full screen]({{ '/assets/animations/heystax-system.html' | relative_url }}){: target="_blank" rel="noopener" }. Use the Replay button to watch again.

## What happens

1. One goal card sits at the top: "School 2 paying". Nothing yet says how.
2. Four roles line up under it. Each role's mission draws a thread back to the goal.
3. Workers join the roles. Any runtime can fill one: Grok Bot, Hermes, Claude Code, Codex.
4. Marketing tries three angles. Two fade on their evidence. One holds.
5. The angle turns into next actions, routed by `@handle` to Builder and Business Development.
6. Builder sessions come and go. When Codex stops, its claim is released and Claude picks the card up.
7. Done cards stay one line. Done wakes the next role.
8. Business Development sends within its daily cap. A reply turns into a booked call: the only card in Colm's column.
9. Grok Bot is swapped for Hermes under Marketing. The angles and evidence do not move.
10. The goal flips to done, and the next goal slides in.

## Why it holds

**It travels.** The bot changed in scene 9 and nothing was lost. The angles, the evidence and the mission sat on the stax, not inside Grok Bot.

**You can check.** Colm did not approve each send. He reads who did what, and he gets the one moment only he can do.

## What works today

| Step | State | Note |
|---|---|---|
| Goals and next actions on a stax | works today | ledger `mcp-tools-core` |
| Roles claim and report on next actions | partly | ledger `agent-claim-rules` |
| The Chief creates roles | works today, not yet browser-checked | ledger `chief-role-create` |
| Workers join a role, one per machine | works today, not yet browser-checked | ledger `agent-worker-tokens` |
| A stopped session's claim is released for the next worker | works today, not yet browser-checked | ledger `agent-run-leases` |
| Done wakes the Chief | works today, not yet browser-checked | ledger `chief-wake` |
| Angles kept on the stax with their outcome | works today, not yet browser-checked | ledger `crm-angles` |
| Sending email, building pages | outside HeyStax | the worker's own tools; the result goes on the action |

Read next: [One goal, many angles, until someone pays](fishing-for-revenue) · [Roles, workers and their keys](../agents/roles-workers-tokens)
