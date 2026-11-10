---
title: Connect to Claude Code
parent: AI Integrations (MCP)
nav_order: 2
---

# Connect HeyStax to Claude Code (CLI)

Use your Stax and Next Actions directly from the terminal while coding with Claude Code.

{% include badge-partial.html %}

For the separate **agent peer pilot**, where Claude Code works under its own name and reports on claimed actions, see [Agents that work on a Stax](agents/). The usual connection described below acts through your existing account. The pilot setup guide is held for internal testers.

---

## Prerequisites

- A HeyStax account with **Pro** or **Trial** plan
- Claude Code installed ([install guide](https://docs.anthropic.com/en/docs/claude-code))

---

## Add HeyStax

Sign in at [dash.heystax.ai](https://dash.heystax.ai) and copy your personal access token from **Settings, MCP**. Claude Code sends it with every request.

For all your projects:

```bash
claude mcp add --transport sse heystax \
  https://dash.heystax.ai/api/mcp/sse \
  --header "Authorization: Bearer YOUR_TOKEN"
```

For this project only, add `--scope project`. That writes a `.mcp.json` file in the project root, so keep it out of git.

### Verify

Run `claude`, then type `/mcp`. HeyStax shows as connected.

---

## Usage examples

Once connected, just talk naturally:

```
> List my stax

> What are the next actions for my WebApp project?

> Add "fix the auth timeout bug" to WebApp

> Mark action 1 on WebApp as done

> Log that I deployed v2.3 to production on WebApp
```

---

## Combining with Hey CLI

HeyStax MCP and the [Hey CLI](hey-cli) complement each other:

| Use case | Best tool |
|----------|-----------|
| Quick capture mid-flow | `hey "fix the bug"` |
| Review and manage actions in conversation | Claude Code MCP |
| Add actions while chatting with Claude | Claude Code MCP |
| Bulk operations from terminal | Hey CLI |

Both write to the same Stax. Changes sync in real time.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "needs authentication" | Remove HeyStax and add it again with your token |
| "PLAN_REQUIRED" | Upgrade to HeyStax Pro or Trial |
| HeyStax not in `/mcp` list | Run `claude mcp add` command above |
| "TOKEN_INVALID" | Remove and re-add: `claude mcp remove heystax` then add again |
| Connection timeout | Check your internet connection; the MCP server is at `dash.heystax.ai` |

---

## Remove

To disconnect HeyStax from Claude Code:

```bash
claude mcp remove heystax
```
