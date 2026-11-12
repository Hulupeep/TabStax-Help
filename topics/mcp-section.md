---
title: AI Integrations (MCP)
parent: Surfaces
nav_order: 4
has_children: true
---

# AI Integrations (MCP)

HeyStax connects to AI assistants through the **Model Context Protocol (MCP)**. This lets Claude and other AI tools read your Stax, manage Next Actions, and log breadcrumbs, all through natural conversation.

**What you can do:**

- "What are my stax?": list all your projects
- "Add 'review PR #42' to WebApp": add a next action
- "Mark the first action on WebApp as done": complete an action
- "What's on my plate?": see all pending actions across stax
- "Call Ana is waiting on Ana until Thursday": set where an action stands (next, decision, waiting, blocked or parked), who it waits on, when to look again, and how anyone can tell it is done. The same state shows on the dashboard's List cards.

**Supported integrations:**

| Integration | Status | How |
|------------|--------|-----|
| [Claude Code (CLI)](mcp-claude-code) | Live | One command with your token |
| [Claude.ai (web)](mcp-claude-ai) | Not today | It wants to sign in to HeyStax for you. HeyStax needs your token instead |
| ChatGPT | Live | Existing MCP connection; client-specific steps are being refreshed |

{% include badge-partial.html %}

**Agent peer pilot:** a worker can have its own name, claim a Next Action and report a blocker or result on the Stax. The backend is deployed; the complete owner/worker/browser journey still needs a live check. [See what it means in plain language](agents/). To set one up, see [Connect a worker to a role](agents/connect-a-worker).

{% include badge-partial.html %}

A worker can wait for work and pick it up as soon as it is assigned, and a launcher with a push URL is woken when work arrives. This is in production and still being checked end to end. Public worker installation is planned.

---

**Requirements:** HeyStax account with **Pro** or **Trial** plan.
