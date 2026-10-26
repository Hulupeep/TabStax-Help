---
title: AI Integrations (MCP)
parent: Surfaces
nav_order: 4
has_children: true
---

# AI Integrations (MCP)

Heystax connects to AI assistants through the **Model Context Protocol (MCP)**. This lets Claude and other AI tools read your Stax, manage Next Actions, and log breadcrumbs — all through natural conversation.

**What you can do:**

- "What are my stax?" — list all your projects
- "Add 'review PR #42' to WebApp" — add a next action
- "Mark the first action on WebApp as done" — complete an action
- "What's on my plate?" — see all pending actions across stax

**Supported integrations:**

| Integration | Status | How |
|------------|--------|-----|
| [Claude.ai (web)](mcp-claude-ai) | Live | OAuth connector |
| [Claude Code (CLI)](mcp-claude-code) | Live | Same connector or manual setup |
| ChatGPT | Live | Existing MCP connection; client-specific steps are being refreshed |

{% include badge-partial.html %}

**Agent peer pilot:** a worker can have its own name, claim a Next Action and report a blocker or result on the Stax. The backend is deployed; the complete owner/worker/browser journey still needs a live check. [See what it means in plain language](agents/). The setup guide is held for internal testers.

{% include badge-planned.html %}

Automatic delivery to an offline worker and public worker installation are planned. Current pickup starts when you run the worker or it checks for work.

---

**Requirements:** Heystax account with **Pro** or **Trial** plan.
