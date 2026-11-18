---
title: Connect to Claude Code
parent: AI Integrations (MCP)
nav_order: 2
---

# Connect HeyStax to Claude Code

Claude Code reads and writes your stax from the terminal, while you code.

## Why it matters to you

You are deep in a branch at 23:00 and remember a bug. Tell Claude Code. The next action lands on the stax, and it is there in the morning on the dashboard and in Telegram.

## You need

- A HeyStax account on the **Pro** or **Trial** plan. MCP needs one of these.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed.
- Your personal access token from **Settings, MCP** at [dash.heystax.ai](https://dash.heystax.ai).

## How to do it

1. Copy your token. Keep it out of chats and screenshots.
2. Add HeyStax for all your projects:

   ```bash
   claude mcp add --transport sse heystax \
     https://dash.heystax.ai/api/mcp/sse \
     --header "Authorization: Bearer YOUR_TOKEN"
   ```

   For one project only, add `--scope project`. That writes `.mcp.json` in the project root, so keep it out of git.
3. Run `claude`, then type `/mcp`. HeyStax shows as connected.
4. Type `List my stax`. Claude lists your stax by name.

## What to ask

- "What are the next actions on WebApp?"
- "Add 'fix the auth timeout bug' to WebApp"
- "Log that I deployed v2.3 on WebApp"

For quick capture without Claude, the [hey CLI](hey-cli) writes to the same stax. Want Claude Code to work under its own name instead of yours? See [Connect a worker to a role](agents/connect-a-worker).

## If it goes wrong

| You see | Do this |
|---|---|
| "needs authentication" or `TOKEN_INVALID` | `claude mcp remove heystax`, then add it again with a fresh token |
| `PLAN_REQUIRED` | Move to Pro or Trial at [dash.heystax.ai](https://dash.heystax.ai) |
| HeyStax is not in `/mcp` | Run the `claude mcp add` command again |

To disconnect: `claude mcp remove heystax`.

Now you can capture work mid-flow and find it waiting everywhere else.
