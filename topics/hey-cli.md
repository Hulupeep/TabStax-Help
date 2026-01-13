# Say hello to the Tabstax CLI - Hey CLI - Your Next Actions in Your Workflow

## The Problem It Solves

You're deep in your code editor, terminal, or AI assistant. You know exactly what needs to happen next on your project. But to capture that thought, you have to:

1. Switch to your browser
2. Find the TabStax extension
3. Click to open it
4. Navigate to the right project
5. Add your next action

By the time you've done all that, you've lost your flow. The context switch killed your momentum.

**Hey CLI brings your Next Actions to where you already work** - your terminal, your IDE, your AI assistant.

```bash
# You're in your terminal, you just realized something
hey "Add validation to the signup form"

# Done. Back to coding. No context switch.
```

## The Core Insight: LLMs Need Your Context

Modern development increasingly involves AI assistants - Claude, ChatGPT, Cursor, Copilot. These tools are powerful, but they don't know what you're working on across your projects.

**Hey CLI bridges this gap.**

When you tell your AI assistant to run `hey ls`, it instantly sees:
- All your projects (Stax)
- What needs to be done (Next Actions)
- What you've accomplished (Breadcrumbs)
- Your priorities (Must/Should/Good/Meh)

Now your AI has context. It can help you plan, prioritize, and execute.

---

## Installation

```bash
npm install -g tabstax-cli
```

Then authenticate with your TabStax account:

```bash
hey login
```

**Don't have a TabStax account?** It's simple - just go to the [Chrome Web Store](https://chromewebstore.google.com/detail/tabstax/your-extension-id) and install the TabStax extension. Create an account there, and you'll see all your next actions against each project in both the extension and the CLI.

---

## Quick Start

```bash
# Set your default project
hey use "My Project"

# Add a next action (something to do)
hey "Build the login page"

# Add a breadcrumb (something you did)
hey -x "Fixed the auth bug"

# See your actions
hey ls

# Complete an action
hey done 1
```

---

## Command Reference

### Adding Actions

| Command | Description |
|---------|-------------|
| `hey "message"` | Add a next action (future intent) |
| `hey -x "message"` | Add a breadcrumb (past accomplishment) |
| `hey "msg" --force` | Add even when at the 7-action limit |
| `hey -p "project" "msg"` | Add to a specific project |

**Next Actions vs Breadcrumbs:**
- **Next Action**: "Build the API endpoint" → Something you *will* do
- **Breadcrumb**: "Fixed the login bug" → Something you *did*

### Listing & Viewing

| Command | Description |
|---------|-------------|
| `hey ls` | Show actions for current project |
| `hey ls stax` | List all your stax with priorities |
| `hey ls --all` | Expanded view with actions per stax |
| `hey ls --done` | Show only breadcrumbs (completed) |
| `hey ls "project"` | Show actions for specific project |

### Managing Actions

| Command | Description |
|---------|-------------|
| `hey done` | Complete action #1 (first in list) |
| `hey done 3` | Complete action #3 |
| `hey rm 2` | Remove action #2 (without completing) |
| `hey edit 1 "new text"` | Edit action #1's content |
| `hey mv 3 1` | Move action #3 to position #1 |

### Projects & Priority

| Command | Description |
|---------|-------------|
| `hey use "project"` | Set default project (fuzzy matched) |
| `hey pri "project" must` | Set priority to Must (★) |
| `hey pri "project" should` | Set priority to Should (◆) |
| `hey pri "project" good` | Set priority to Good (○) |
| `hey pri "project" meh` | Set priority to Meh (·) |
| `hey which` | Show current context |

### Authentication

| Command | Description |
|---------|-------------|
| `hey login` | Log in to TabStax |
| `hey logout` | Log out |
| `hey whoami` | Show current user |
| `hey status` | Show full CLI status |

---

## Priority System

TabStax uses attention-based priorities to help you focus:

| Icon | Level | Meaning |
|------|-------|---------|
| ★ | Must | Critical - do today |
| ◆ | Should | Important - do this week |
| ○ | Good | Nice to have |
| · | Meh | Low priority / someday |

Set priorities to see your most important projects at the top of `hey ls stax`.

---

## The 7-Action Limit

TabStax enforces a maximum of **7 active actions per project**. This isn't a bug - it's a feature.

**Why?** Research shows humans can only hold ~7 items in working memory. More than 7 actions means you're not being specific enough, or you're avoiding the hard work of prioritizing.

When you hit the limit:
```bash
hey "Another task"
# ⚠ Project has 7/7 active actions (limit reached)
# Options:
#   • Complete one:  hey done <n>
#   • Remove one:    hey rm <n>
#   • Force add:     hey "task" --force
```

**Best practice:** Complete or remove actions before adding new ones. If you absolutely must exceed the limit, use `--force`.

---

## Use Cases by Persona

### The Solo Developer

You're building a side project. You work on it in bursts - mornings before work, weekends, random evenings.

**The problem:** Every time you return, you've forgotten where you were.

**The solution:**
```bash
# End of session - capture where you stopped
hey -x "Got OAuth working with Google"
hey "Add OAuth for GitHub next"
hey "Then handle the callback errors"

# Next session - instant context
hey ls
# 1. Add OAuth for GitHub next
# 2. Then handle the callback errors
# ✓ Got OAuth working with Google (2d ago)
```

### The Tech Lead

You're managing multiple projects and people. Context-switching is your life.

**The problem:** You can't remember the status of each project.

**The solution:**
```bash
# Quick overview
hey ls stax
# ★ Must
#   API Migration    3/7 actions   last: 2h ago
#   Security Audit   5/7 actions   last: 1d ago
# ◆ Should
#   Performance      2/7 actions   last: 3d ago

# Dive into the urgent one
hey use "API Migration"
hey ls
```

### The AI-Assisted Developer

You use Claude, ChatGPT, or Cursor daily. You want your AI to understand your projects.

**The problem:** Your AI doesn't know what you're working on.

**The solution:**
```
You: "What should I work on today?"

AI: Let me check your TabStax projects.
    *runs: hey ls stax*

    You have 3 "Must" priority projects:
    - API Migration (3 actions pending)
    - Security Audit (5 actions pending)
    - Client Demo (2 actions pending)

    The API Migration hasn't been touched in 2 hours.
    Want me to show you those actions?

You: "Yes, and help me break down the first one"

AI: *runs: hey ls "API Migration"*

    Your next action is "Migrate user endpoints to v2"

    That's a big task. Let me help break it down:
    *runs: hey rm 1*
    *runs: hey "List all user endpoints in v1"*
    *runs: hey "Create v2 schema for /users"*
    *runs: hey "Write migration script for /users"*
    *runs: hey "Add tests for v2 /users"*

    I've replaced the vague task with 4 specific actions.
```

### The Agency/Freelancer

You juggle multiple clients. Each has their own project context.

**The problem:** Client calls catch you off-guard. "Where are we on the redesign?"

**The solution:**
```bash
# Before a client call
hey use "Acme Redesign"
hey ls

# Instant context:
# 1. Waiting on: Client approval for homepage mockup
# 2. Once approved: Build header component
# 3. Then: Implement mobile nav
# ✓ Sent mockup v2 to client (3d ago)
# ✓ Revised color scheme per feedback (5d ago)
```

---

## Syncing with TabStax Extension

**Everything syncs automatically.**

When you add an action via CLI:
```bash
hey "Review pull request #42"
```

It appears instantly in:
- The TabStax browser extension
- The TabStax dashboard
- Any other device where you're logged in

When you complete an action in the extension, the CLI sees it:
```bash
hey ls
# Shows the updated list
```

This means you can:
- Capture actions in terminal while coding
- Review them in the browser extension
- Check them off on your phone (via dashboard)
- Ask your AI to help manage them

**One source of truth, accessible everywhere.**

---

## Tips & Tricks

### Fuzzy Project Matching
You don't need exact names:
```bash
hey use "tab"      # Matches "TabStax Project"
hey use "api"      # Matches "API Migration"
hey -p "sec" "Fix the auth bug"  # Matches "Security Audit"
```

### Quick Capture Workflow
When an idea hits, capture it fast:
```bash
hey "the thing I just thought of"
# Adds to your current default project
```

### Breadcrumb Your Progress
End each work session with breadcrumbs:
```bash
hey -x "Got the tests passing"
hey -x "Pushed to staging"
hey "Deploy to prod tomorrow"
```

### Priority Triage
Start your day with:
```bash
hey ls stax
# See what's ★ Must priority
# Adjust priorities as needed
hey pri "Old Project" meh
hey pri "Urgent Client" must
```

### Integrate with AI Assistants
Tell your AI about Hey CLI:
```
"I use TabStax to track my next actions. You can run 'hey ls stax'
to see my projects, 'hey ls' to see actions, and 'hey done 1' to
complete them. Help me manage my work."
```

---

## Troubleshooting

### "Not logged in"
```bash
hey login
# Follow the prompts
```

### "Project not found"
```bash
hey ls stax
# See exact project names, then use one
hey use "Exact Project Name"
```

### "Limit reached"
```bash
hey done 1        # Complete something
# or
hey rm 3          # Remove something
# or
hey "msg" --force # Override (not recommended)
```

### Actions not syncing
Check your connection:
```bash
hey status
# Should show "Logged in as your@email.com"
```

---

## What's Next?

Hey CLI is the foundation for bringing TabStax into your development workflow. Coming soon:

- **MCP Integration**: Direct integration with Claude and other AI assistants
- **Git Hooks**: Auto-capture breadcrumbs on commits
- **IDE Extensions**: Hey CLI embedded in VS Code, Cursor, etc.

---

## Links

- [Install TabStax Extension](https://tabstax.app)
- [TabStax Dashboard](https://tabstax.app/dashboard)
- [npm Package](https://www.npmjs.com/package/tabstax-cli)
- [Report Issues](https://github.com/Hulupeep/tabstax/issues)
