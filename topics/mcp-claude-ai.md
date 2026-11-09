---
title: Connect to Claude.ai
parent: AI Integrations (MCP)
nav_order: 1
---

# Connect Claude.ai to your stax

Claude.ai reads and writes your stax over MCP. Ask in plain words. The answer lands in your graph, not in a scrolled-away chat.

## Why it matters to you

You plan a launch with Claude on Tuesday. On Thursday you open ChatGPT or the `hey` CLI and the same next actions are there. You did not paste your context. It was already yours, and it travelled.

## You need

- A HeyStax account on the **Pro** or **Trial** plan. MCP needs one of these.
- A Claude account at [claude.ai](https://claude.ai).

## Connect it

1. Sign in to [claude.ai](https://claude.ai) and open **Settings**.
2. Open **Connectors** (older versions call it **Integrations**).
3. Add a custom connector with this address: `https://dash.heystax.ai/api/mcp`
4. Sign in to HeyStax when asked.
5. Click **Approve** on the consent screen.
6. Back in Claude.ai, HeyStax shows as **Connected**.

Check it: start a new chat and type `List my stax`. Claude lists your stax by name.

## What to ask

| Say | Claude uses | What happens |
|---|---|---|
| "What are my stax?" | `stax_list` | Lists your stax |
| "Show next actions for WebApp" | `next_actions_list` | Lists the open actions on one stax |
| "Add 'Fix login bug' to WebApp" | `next_actions_add` | Adds a next action |
| "Mark the login bug as done" | `next_actions_complete` | Completes it |
| "Note that the code review is finished" | `next_actions_log` | Adds a progress note to the action |

Claude can also read and write goals, dates, people and records. See [what is live](../docs/shipped-ledger).

## If it goes wrong

| You see | Do this |
|---|---|
| "Needs authentication" | Reconnect, or disconnect and connect again |
| `PLAN_REQUIRED` | Move to Pro or Trial at [dash.heystax.ai](https://dash.heystax.ai) |
| `TOKEN_INVALID` | Disconnect and connect again |
| No tools show | Check your plan is active, then reconnect |
| Stax not found | Use a more exact stax name |

## Disconnect

Open **Settings**, then **Connectors**, find HeyStax and click **Disconnect**. Your stax stay. Only Claude's access ends.

Now you can plan in Claude and find the plan waiting everywhere else.
