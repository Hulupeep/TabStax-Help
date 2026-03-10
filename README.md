---
title: Home
nav_order: 1
description: Help center for HeyStax — your workspace for momentum
permalink: /
---

# <img src="icons/tabstax-48.png" alt="HeyStax" width="48" height="48" style="vertical-align: middle; margin-right: 10px;">Welcome to HeyStax

**You're not disorganized. You lose momentum.**

When hyperfocus breaks, you don't just stop working — you lose the thread. And without the thread, you can't get back in. That's not a character flaw. That's a design problem.

HeyStax solves it. A **Stax** is a workspace that holds everything you need to pick up where you left off: the people you're working with, the AI agents helping you, the web tabs you had open, and the concrete next action that tells you exactly what to do. One click and you're back in flow.

---

## What is a Stax?

A Stax is bigger than a tab group. It's a **momentum container**.

| What's inside | Why it matters |
|---------------|---------------|
| **People** | Collaborators with @handles, colour-coded ownership, role-based access |
| **Agents** | AI assistants (Claude, ChatGPT) that read your stax, add actions, and do work |
| **Tabs & Links** | The web resources for this workspace — open them all in one click |
| **Next Actions** | The concrete step that lets you re-enter flow without thinking about what to do first |
| **Context** | Start Here pages, breadcrumbs, notes — where you left off and why |

A Stax isn't a list of bookmarks. It's a named room you can walk back into cold — with your team and your AI already there.

→ [What is a Stax?](topics/what_is_a_stax.md)

---

## HeyStax surfaces

Your Stax lives everywhere you work. Same data, every surface. Add an action on the web; it shows in the terminal. Complete it from your AI; the extension reflects it.

| Surface | What it is | Best for |
|---------|-----------|----------|
| **TabStax** (Chrome extension) | Tabs for your Stax workspace — capture and restore browser contexts | Context switching between projects in one click |
| **Dashboard** ([dash.heystax.ai](https://dash.heystax.ai)) | Attention blocks, actions mode, collaboration, timesheets | Planning, prioritizing, team visibility, phone access (PWA) |
| **Hey CLI** (`hey`) | Terminal-native next actions — `hey "do the thing"`, `hey done 1` | Capturing thoughts without leaving the terminal |
| **MCP** (AI integrations) | Your AI reads and writes your stax through natural conversation | Claude.ai, Claude Code, ChatGPT — AI-powered project management |
| **Timesheets** ([dash.heystax.ai/time](https://dash.heystax.ai/time)) | Flow-native weekly hours capture scoped to your stax | Time tracking that doesn't break your flow |
| **Share Pages** | Public URLs — anyone can view, import, or open your stax | Team handoffs, onboarding, shared workflows |

---

## The problem HeyStax solves

Every time you return to a project, you pay a **reconstruction tax**: reopen tabs, re-find docs, try to remember what you were doing. The more projects you juggle, the more energy goes to *remembering* instead of *doing*. Projects drift. Momentum dies.

Todo apps don't fix this. "Finish Q3 reporting" doesn't open the spreadsheet, the dashboard, and the email thread. It doesn't tell you where you stopped. It's a reminder without a runway.

**HeyStax preserves your state so you can pick up any project cold.** No reconstruction. No guilt spiral. Just the next action and the workspace to do it in.

→ [Read the full problem statement](topics/what_problem_tabstax_solves.md)

### See it in action

[![Watch HeyStax in action](https://img.youtube.com/vi/jcc-PsCdbM8/maxresdefault.jpg)](https://www.youtube.com/watch?v=jcc-PsCdbM8)

*Click to watch on YouTube*

---

## What you'll find here

### Getting started
* [What problem HeyStax solves](topics/what_problem_tabstax_solves.md) — the core problem and mindset shift
* [The HeyStax Mental Model](topics/tabstax_mental_model.md) — think in problems, not tabs
* [What is a Stax?](topics/what_is_a_stax.md) — the core concept
* [Creating your first Stax](topics/creating_your_first_stax.md) — step-by-step with a real example

### TabStax (Chrome extension)
* [First time opening TabStax](topics/first_time_opening_tabstax.md) — your first experience after installing
* [Understanding the popup](topics/using_the_main_popup.md) — navigate next actions and open Stax
* [Adding Favourites](topics/adding_favourites.md) — pin current priorities for fast access

### Hey CLI
* [Hey CLI Guide](topics/hey-cli.md) — manage next actions from your terminal

### AI Integrations (MCP)
* [Connect to Claude.ai](topics/mcp-claude-ai) — use Stax through conversation
* [Connect to Claude Code](topics/mcp-claude-code) — manage actions while coding with Claude

### Collaboration & Sharing
* What it means when someone shares a Stax with you, and how collaborative Stax work with @handles and roles

### Accounts & Sync
* Using HeyStax locally without an account, or signing in to sync across devices

---

## If you're new

Pick one project. Save the tabs you use for it as a Stax. Add a couple of next actions. That's your home base for that piece of work.

Tomorrow, open that Stax. Tabs load. Next action is right there. You're working in seconds, not minutes.

That moment — opening a cold project and immediately knowing what to do — is what HeyStax exists to produce. We call it a **Flowful Re-entry**.

**Want to understand the core idea?** → [What problem HeyStax solves](topics/what_problem_tabstax_solves.md)
**Just installed TabStax?** → [First time opening TabStax](topics/first_time_opening_tabstax.md)
**Ready to try it?** → [Creating your first Stax](topics/creating_your_first_stax.md)

---

## If someone shared a Stax with you

They've captured the way they work on something into a single shared space. Opening that Stax lets you stand in the same place: same structure, same tabs, same context, same next actions.

You can treat it like a curated workspace built around one purpose. As with any link, only fully trust Stax from sources you trust.

---

## Hey CLI — your terminal surface

```bash
npm install -g heystax-cli

hey login
hey use "My Project"
hey "Build the feature"
hey ls
hey done 1
```

**Why CLI?** Because leaving your terminal to capture a thought kills momentum. The CLI syncs bidirectionally — add an action in terminal, see it in the extension. Complete it in the dashboard, the CLI reflects it.

→ [Full Hey CLI Guide](topics/hey-cli.md)

---

## AI Integrations — your LLM surface

HeyStax connects to AI assistants through the **Model Context Protocol (MCP)**. Your AI can read your projects, add actions, mark things done — all through natural conversation.

```
You: What are my next actions for the WebApp project?

Claude: Here are the pending actions for WebApp:
  1. Fix the auth timeout bug
  2. Review PR #42
  3. Update deployment docs
```

Works with **Claude.ai**, **Claude Code**, and **ChatGPT**. Connect once, use everywhere.

→ [Connect to Claude.ai](topics/mcp-claude-ai)
→ [Connect to Claude Code](topics/mcp-claude-code)

---

## Staying in momentum

HeyStax is built around one core idea:

> Your brain should spend its energy doing the work, not reconstructing where you were.

This help center supports that. Every article aims to:

* Explain things in simple mental models
* Show you how to get back to a working state quickly
* Help you use Stax as the central room where your work happens — with your people, your agents, your tabs, and your next action all in one place

---

## Still need help?

If something is unclear or you hit a wall, come back here. Everything is aimed at one outcome:

Preserving your momentum, with as little friction as possible.
