---
title: Home
nav_order: 1
description: Help center for HeyStax — your workspace for momentum
permalink: /
---

# HeyStax

**Pick up where your mind left off.**

You know you were working on something. You just can't get back in.

Not because the work disappeared. Because the *context* did. The thread you were holding — what you were doing, what came next, why it mattered — that's what's gone. And without the thread, even opening the project feels like starting over.

That's not a focus problem. It's a design problem. And it compounds.

The more projects you hold, the more threads you're managing. And when other people are involved, it gets quieter and worse: they can't see your context. You can't see theirs. What's actually happening on a project is locked inside someone's head, or buried in a Slack thread from three weeks ago, or simply gone. Status updates are a workaround for this. So are standups. So is the mild dread of asking "where are we on this?" again.

HeyStax is a **flow manager**. It makes project context visible and shared — not just links, but intent — so anyone on a project can step back into it cold and immediately know what's happening and what to do next.

---

## A different way of seeing projects

Most tools treat a project as a list of tasks. Check things off, add more, repeat.

But that's not what a project actually is when you're inside it. A project is a **live mental state** — a specific set of tools open, a thread of thinking in progress, a concrete next move held in working memory. The task list is the skeleton. The context is what makes it possible to act.

When you lose context — through interruption, through switching, through handing off to someone else — you lose the ability to act without first doing reconstruction work. And reconstruction is friction. Friction becomes avoidance. Avoidance is where projects quietly die.

HeyStax treats context as the primary thing worth saving. Not the task. The state of being *in* the work.

That matters for humans. It turns out it matters just as much for agents. An AI that can read your project context — what's open, what's pending, what happened last — is a different kind of collaborator than one starting from a blank prompt.


→ [What problem HeyStax solves](topics/what_problem_tabstax_solves)

---

## What is a Stax?

A **Stax** is a named workspace. Not a bookmark folder. Not a todo list. A live container for a project that holds everything you need to step back into it:

| What's in a Stax | Why it matters |
|---|---|
| **Tabs & Links** | The web pages for this project — open them all in one click |
| **Next Actions** | The concrete step that gets you back to work without thinking |
| **Priority** | Must / Should / Good / Meh — where this sits in your attention right now |
| **Collaborators** | Team members with @handles, roles, and colour-coded ownership |
| **Agents** | AI assistants connected via MCP — they read your Stax, add actions, and do work inside the same context |
| **Breadcrumbs** | A trail of what happened — so returning after a week feels like a pause, not a restart |

The moment of opening a cold Stax and immediately knowing what to do next — we call that a **Flowful Re-entry**. That's what HeyStax is built to produce.

→ [What is a Stax?](topics/what_is_a_stax)

---

## Where HeyStax lives

Same data. Every surface. Add an action in the terminal; it appears in the extension. Complete it through Claude; the dashboard reflects it.

| Surface | What it is | Best for |
|---|---|---|
| **TabStax** (Chrome extension) | Captures and restores your browser context as a named Stax | One-click context switching between projects |
| **Dashboard** ([dash.heystax.ai](https://dash.heystax.ai)) | Full attention view, actions mode, collaboration, timesheets — installable as a PWA | Planning, prioritising, team visibility, phone access |
| **Timesheets** ([dash.heystax.ai/time](https://dash.heystax.ai/time)) | Flow-native weekly hours, scoped to your Stax | Time tracking that doesn't break your momentum |
| **Hey CLI** (`npm i heystax-cli`) | Terminal-native next actions: `hey "do the thing"`, `hey done 1` | Capturing thoughts without leaving your tools |
| **MCP** (AI integrations) | Claude.ai, Claude Code, ChatGPT — your AI reads and writes your Stax | Natural language project management, AI-powered planning |
| **Share Pages** | Public URLs anyone can open or import | Team handoffs, onboarding, shared workflows |

---

## The reconstruction tax

Every time you return to a project, you rebuild it from scratch.

Which tabs. Which docs. Which tools. Where you left off. What to do next.

That's the **reconstruction tax** — and it compounds. The more projects you're holding, the more energy goes to *remembering* instead of *doing*. Projects drift. Momentum quietly dies.

Todo apps don't fix this. "Finish Q3 reporting" doesn't open the spreadsheet, the Slack thread, and the dashboard. It doesn't tell you where you stopped. It's a reminder without a runway.

HeyStax preserves your state so you can pick up any project cold. No reconstruction. No guilt spiral. Just the next action and the workspace it lives in.

→ [Read the full problem statement](topics/what_problem_tabstax_solves)

### See it in action

[![Watch HeyStax in action](https://img.youtube.com/vi/jcc-PsCdbM8/maxresdefault.jpg)](https://www.youtube.com/watch?v=jcc-PsCdbM8)

*Click to watch on YouTube*

---

## Where to start

### Just installed the Chrome extension?
→ [First time opening HeyStax](topics/first_time_opening_tabstax)
→ [Creating your first Stax](topics/creating_your_first_stax)

### Want to understand the system?
→ [The HeyStax mental model](topics/tabstax_mental_model)
→ [What problem HeyStax solves](topics/what_problem_tabstax_solves)

### Using the CLI or MCP?
→ [Hey CLI guide](topics/hey-cli)
→ [Connect to Claude.ai](topics/mcp-claude-ai)
→ [Connect to Claude Code](topics/mcp-claude-code)

### Someone shared a Stax with you?
They've captured a whole working context and handed it to you. Opening that Stax puts you in the same place they were — same structure, same tabs, same next actions. Trust it the way you'd trust a link: only from sources you trust.

---

## Hey CLI — your terminal surface

```bash
npm i heystax-cli

hey login
hey use "My Project"
hey "Build the feature"
hey ls
hey done 1
```

Leaving your terminal to capture a thought costs you context. The CLI keeps you in flow — add an action here, complete it in the dashboard, see it in the extension. All the same Stax.

→ [Full Hey CLI guide](topics/hey-cli)

---

## AI integrations — your LLM surface

HeyStax connects to AI assistants through the **Model Context Protocol (MCP)**. Your AI reads your projects, adds actions, marks things done — through natural conversation.

```
You: What are my next actions for the WebApp project?

Claude: Here are the pending actions for WebApp:
  1. Fix the auth timeout bug
  2. Review PR #42
  3. Update deployment docs
```

Works with **Claude.ai**, **Claude Code**, and **ChatGPT**. Connect once.

→ [Connect to Claude.ai](topics/mcp-claude-ai)
→ [Connect to Claude Code](topics/mcp-claude-code)

---

## Plans

| Plan | What you get |
|---|---|
| **Free** | Local-only extension, receive shared Stax |
| **Trial** | Full cloud sync, sharing, MCP access, cross-device |
| **Pro** | Everything in Trial, plus collaboration, timesheets, team features |

MCP access requires Trial or Pro.

---

## The one thing

Your brain should spend its energy doing the work. Not reconstructing where you were.

Pick one project. Save the tabs as a Stax. Add a next action. Tomorrow, open that Stax. Tabs load. Next action is right there. You're working in seconds.

That moment — that's a Flowful Re-entry. That's what HeyStax is here for.
