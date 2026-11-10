---
title: Connect Claude
parent: AI Integrations (MCP)
nav_order: 1
---

# Connect Claude to your stax

Claude reads and writes your stax over MCP. Ask in plain words. The answer lands in your graph, not in a scrolled-away chat.

## Why it matters to you

You plan a launch with Claude on Tuesday. On Thursday you open the `hey` CLI and the same next actions are there. You did not paste your context. It was already yours, and it travelled.

## One thing first: HeyStax has no sign-in

HeyStax MCP takes a token, not a sign-in. Your app sends it as a header: `Authorization: Bearer <your token>`.

Claude.ai on the web asks you to sign in when you add a custom connector. That sign-in no longer exists, so it can't connect that way. Use Claude Code, or another app that sends a token header.

## You need

- A HeyStax account on the **Pro** or **Trial** plan. MCP needs one of these.
- Your personal access token from **Settings, MCP** at [dash.heystax.ai](https://dash.heystax.ai).

## Connect it

1. Copy your token. Keep it out of chats and screenshots.
2. Follow [Connect to Claude Code](mcp-claude-code). It is one command.
3. Start Claude and type `List my stax`. Claude lists your stax by name.

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
| The app asks you to sign in | It can't connect that way. Use a token connector |
| `TOKEN_INVALID` | Copy the token again and re-add the connector |
| `PLAN_REQUIRED` | Move to Pro or Trial at [dash.heystax.ai](https://dash.heystax.ai) |
| No tools show | Check your plan is active, then re-add the connector |

Now you can plan with Claude and find the plan waiting everywhere else.
