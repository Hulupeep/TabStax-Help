---
title: What problem HeyStax solves
parent: Getting Started
nav_order: 2
---

[← Back to Help Home](/)

# What problem HeyStax solves

## The real problem isn't disorganisation. It's loss of momentum.

You know what it feels like to be deep in something. Hours disappear. You think clearly, move fast, connect dots. Momentum is your power source.

The problem is what happens when it breaks. You don't just stop doing the task — you lose access to the state you need to do it. The thread dissolves. And getting it back costs more than the work itself.

That's why someone can work intensely for 10 hours and still not send one email. It's not carelessness. It's that when momentum breaks, everything downstream goes dark.

The usual advice — "get organized," try a new app, build a new system — lasts about six minutes. Because organisation isn't the root problem. **State preservation is.**

Every time you return to a project, you pay a **reconstruction tax**:

1. **Rebuild context** — which tabs, docs, dashboards, and tools do I need open?
2. **Recover position** — where did I leave off?
3. **Decide what's next** — what's the first thing I should actually do?

That tax compounds. The more projects you juggle, the more energy goes to *remembering* instead of *doing*. Projects drift. Momentum dies. Things slip — not because you forgot about them, but because getting back into them costs more than you have right now.

## The collaboration version is worse

When other people are involved, the reconstruction tax gets shared in the worst way: nobody can see each other's context.

Your teammate can't see what you have open, what you were working toward, or what the obvious next step is from where you left off. You can't see theirs. So projects accumulate invisible friction — status updates that don't update, handoffs that lose context, standups that exist primarily to reconstruct what everyone already knew.

Status updates are a workaround for this. So are standups. So is the mild dread of asking "where are we on this?" again.

## A different way of seeing projects

Most tools treat a project as a **list of tasks**. Add tasks. Check them off. Add more.

But that's not what a project feels like when you're inside it. A project is a **live mental state** — a configuration of tools, a thread of thinking, a concrete next move held in working memory. The task list is the skeleton. Context is what makes it possible to act.

When you lose context, you lose the ability to act without first rebuilding. And for agents as much as humans — an AI that can read your project state, see what's open and what's pending, is a fundamentally different collaborator than one starting from a blank prompt.

HeyStax treats context as the primary thing worth preserving. Not the task. The state of being *in* the work.

## What HeyStax does

HeyStax captures a **Stax** — a named project workspace containing everything needed to re-enter that project instantly:

- **Tabs and links** — the web resources for this project, opened in one click by the TabStax extension
- **Next actions** — the concrete step that gets you back to work without thinking
- **Priority** — where this sits in your attention right now (Must / Should / Good / Meh)
- **Collaborators** — team members with roles and @handles, sharing the same context
- **Agents** — AI assistants connected via MCP, reading and writing the same Stax
- **Breadcrumbs** — a timestamped trail of what happened, so returning feels like a pause not a restart

The moment of opening a cold Stax and immediately knowing what to do — that's a **Flowful Re-entry**. Momentum preserved. That's what HeyStax is built to produce.

## Where HeyStax lives

HeyStax is a system, not a single app. The same Stax data is accessible across every surface you work in:

| Surface | What it does |
|---|---|
| **TabStax** (Chrome extension) | Restores your browser workspace — opens all project tabs in one click |
| **Dashboard** ([dash.heystax.ai](https://dash.heystax.ai)) | Full attention view, actions mode, collaboration, timesheets |
| **Timesheets** ([dash.heystax.ai/time](https://dash.heystax.ai/time)) | Flow-native weekly hours, scoped to your Stax |
| **Hey CLI** (`npm i heystax-cli`) | Terminal-native next actions — capture thoughts without leaving your tools |
| **MCP** (AI integrations) | Your AI reads and writes your Stax through natural conversation |
| **Share Pages** | Public URLs anyone can open or import |

Add an action in the terminal. Complete it through Claude. Open the tabs from the extension. It's all the same project. Same context. Everywhere.

---

**Next steps:**
- [The HeyStax Mental Model](tabstax_mental_model) — think in projects, not tools
- [What is a Stax?](what_is_a_stax) — the core concept explained
- [Creating your first Stax](creating_your_first_stax) — step-by-step with a real example
- [Surfaces](surfaces/) — see how HeyStax works across browser, terminal, AI, and dashboard
