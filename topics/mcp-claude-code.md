---
title: Connect to Claude Code
parent: AI Integrations (MCP)
nav_order: 2
---

# Connect TabStax to Claude Code (CLI)

Use your Stax and Next Actions directly from the terminal while coding with Claude Code.

---

## Prerequisites

- A TabStax account with **Pro** or **Trial** plan
- Claude Code installed ([install guide](https://docs.anthropic.com/en/docs/claude-code))

---

## Option 1: Claude.ai connector (recommended)

If you've already connected TabStax to Claude.ai (see [Connect to Claude.ai](mcp-claude-ai)), **it automatically works in Claude Code too**. The same connector is shared between both.

### Verify

Open Claude Code in your terminal:

```bash
claude
```

Type `/mcp` to see connected servers. TabStax should appear as connected.

If it shows "needs authentication", press Enter to re-authenticate in your browser.

---

## Option 2: Add manually (global)

Add TabStax to all your Claude Code projects:

```bash
claude mcp add tabstax \
  --transport sse \
  https://dash.tabstax.app/api/mcp/sse
```

You'll be prompted to authenticate in your browser.

### Verify

```bash
claude
```

Then type `/mcp` — TabStax should show as connected.

---

## Option 3: Add manually (per-project)

Add TabStax only to the current project:

```bash
claude mcp add tabstax \
  --transport sse \
  --scope project \
  https://dash.tabstax.app/api/mcp/sse
```

This creates a `.mcp.json` file in your project root. Useful if you want different tokens or settings per project.

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

TabStax MCP and the [Hey CLI](hey-cli) complement each other:

| Use case | Best tool |
|----------|-----------|
| Quick capture mid-flow | `hey "fix the bug"` |
| Review and manage actions in conversation | Claude Code MCP |
| Add actions while chatting with Claude | Claude Code MCP |
| Bulk operations from terminal | Hey CLI |

Both write to the same Stax — changes sync in real time.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "needs authentication" | Press Enter to re-auth in browser |
| "PLAN_REQUIRED" | Upgrade to TabStax Pro or Trial |
| TabStax not in `/mcp` list | Run `claude mcp add` command above |
| "TOKEN_INVALID" | Remove and re-add: `claude mcp remove tabstax` then add again |
| Connection timeout | Check your internet connection; the MCP server is at `dash.tabstax.app` |

---

## Remove

To disconnect TabStax from Claude Code:

```bash
claude mcp remove tabstax
```

Or if using the claude.ai connector, disconnect from Claude.ai Settings > Integrations.
