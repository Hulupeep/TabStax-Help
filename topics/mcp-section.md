---
title: AI Integrations (MCP)
parent: Surfaces
nav_order: 4
has_children: true
---

# AI Integrations (MCP)

Your AI app reads and writes your stax over MCP, the Model Context Protocol. The address is `https://dash.heystax.ai/api/mcp`.

## Why it matters to you

You plan in Claude on Tuesday and ask ChatGPT on Thursday. Both open the same stax, the same next actions, the same history. Your context sits in your account, not in one chat.

## Connect your app

| App | How | State |
|---|---|---|
| [Claude Code](mcp-claude-code) | One command with your token | Live |
| [Claude.ai](mcp-claude-ai) | Add the connector, sign in, pick a role | Live on HeyStax's side; not yet tried from Claude.ai itself |
| ChatGPT | The MCP connector | Live |
| Grok Bot and other apps | [Connect a bot by sign-in](agents/connect-by-sign-in), or send your token | Live on HeyStax's side; check it in your app |

MCP needs a **Pro** or **Trial** plan.

## What to ask

| Say | What happens |
|---|---|
| "What are my stax?" | Lists your stax |
| "Add 'review PR #42' to WebApp" | Adds a next action |
| "Mark the first action on WebApp as done" | Completes it |
| "Call Ana is waiting on Ana until Thursday" | Sets where the action stands, who it waits on and when to look again |

## Give work to agents

An agent works as a role on your stax, with its own key and its own column. Start at [Agents on your stax](agents/).

Now you can open the same work in any AI app and pick up where you left off.
