---
title: Connect to Claude.ai
parent: AI Integrations (MCP)
nav_order: 1
---

# Connect Heystax to Claude.ai

Connect your Stax and Next Actions to Claude.ai so you can manage your projects through conversation.

---

## Prerequisites

- A Heystax account with **Pro** or **Trial** plan
- A Claude account at [claude.ai](https://claude.ai) (free tier works)

---

## Step-by-step setup

### 1. Open Claude.ai settings

Sign in to [claude.ai](https://claude.ai), then click the **gear icon** (bottom-left) to open Settings.

### 2. Go to Integrations

Click **Integrations** in the settings sidebar. You may see it listed as "Connectors" depending on your Claude version.

### 3. Add Heystax

Click **Add Integration** (or **Add Connector**), then enter:

```
https://dash.heystax.ai/api/mcp
```

### 4. Authenticate

You'll be redirected to the Heystax login page. Sign in with your Heystax email and password.

### 5. Approve access

On the consent screen, click **Approve** to grant Claude access to your Stax and Next Actions.

### 6. Done

You'll be redirected back to Claude.ai. Heystax should show as **Connected** in your integrations list.

---

## Verify it works

Start a new conversation and try:

```
List my stax
```

Claude should return your Stax names, tags, and action counts.

---

## What you can ask

| Prompt | What happens |
|--------|-------------|
| "What are my stax?" | Lists all your Stax |
| "Show next actions for WebApp" | Lists pending actions for a specific Stax |
| "Add 'Fix login bug' to WebApp" | Creates a new next action |
| "Mark action 1 on WebApp as done" | Completes an action |
| "Log that I finished the code review on WebApp" | Adds a breadcrumb |

---

## Available tools

These are the MCP tools Claude can use:

| Tool | What it does |
|------|-------------|
| `stax_list` | List all your Stax with tags and action counts |
| `stax_get` | Get details of a specific Stax including tabs |
| `next_actions_list` | List pending next actions for a Stax |
| `next_actions_add` | Add a new next action |
| `next_actions_complete` | Mark a next action as done |
| `next_actions_delete` | Remove a next action |
| `breadcrumb_add` | Log a completed activity |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Needs authentication" | Click to re-authenticate, or disconnect and reconnect |
| "PLAN_REQUIRED" | You need a Heystax Pro or Trial plan — [upgrade here](https://dash.heystax.ai) |
| "TOKEN_INVALID" | Disconnect the integration and reconnect |
| No tools showing | Check your plan is active, then try disconnecting and reconnecting |
| Stax not found | The tool uses fuzzy matching — try a more specific name |

---

## Disconnect

To remove the connection:

1. Go to Claude.ai **Settings > Integrations**
2. Find Heystax
3. Click **Disconnect**

Your Heystax data is not deleted — only the connection to Claude is removed.
