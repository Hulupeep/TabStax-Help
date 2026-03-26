# LLM Instruction: Restructure Getting Started — system-first, surface-accurate

## The problem to fix

Getting Started currently has four conceptual pages. Three of them are framed around the TabStax Chrome extension — websites, tabs, browser windows. Only "What problem HeyStax solves" is genuinely system-level.

HeyStax is a multi-surface system (extension, dashboard, CLI, MCP, timesheets). Getting Started should teach the system. Surface-specific how-to content (first install, popup walkthrough, creating a stax via the extension) belongs under `Surfaces → TabStax (Chrome extension)`.

---

## Target state for Getting Started

After this instruction, Getting Started should contain exactly three pages:

```
Getting Started
├── What problem HeyStax solves    (largely done — light edits only)
├── What is a Stax?                (full rewrite — system-first)
└── The HeyStax mental model       (rewrite — remove browser framing)
```

`Creating your first Stax` moves to `Surfaces → TabStax (Chrome extension)` as `nav_order: 4`.

---

## Page-by-page instructions

---

### PAGE 1 — `topics/what_problem_tabstax_solves.md`
**Action: Light edit only**

This page is largely correct. Make only these targeted changes:

1. Remove any remaining references to "tabs" in the opening paragraphs. The reconstruction tax is about *project context*, not browser tabs specifically.

2. Ensure the surfaces table lists all five surfaces: TabStax (Chrome extension), Dashboard, Hey CLI, AI Integrations (MCP), Timesheets.

3. Fix the link at the bottom — it currently points to `tabstax_mental_model.html`. Verify it still works after the mental model page is rewritten.

4. Do not rewrite the core problem framing — it's correct.

---

### PAGE 2 — `topics/what_is_a_stax.md`
**Action: Full rewrite**

**Current problem:** The page defines a Stax as "all the websites you use together for a task." That's the TabStax extension model — websites and tabs. A Stax is bigger than that now. It has collaborators, agents, breadcrumbs, priority, and next actions. It lives in the CLI, in the dashboard, in Claude's context. It has nothing inherently to do with a browser.

**Rewrite the page with this structure:**

```
---
title: What is a Stax?
parent: Getting Started
nav_order: 3
---
```

**Content to cover:**

**Opening (2–3 sentences):**
A Stax is a named project workspace. Not a tab group. Not a todo list. A live container for everything needed to step back into a piece of work and immediately know what's happening and what to do next.

**The components table — replace the old one with this:**

| Component | What it is |
|---|---|
| **Name** | The project identity — what this work is called |
| **Next Actions** | The concrete step that gets you back to work without thinking |
| **Priority** | Must / Should / Good / Meh — where this sits in your attention right now |
| **Tabs & Links** | The web resources for this project (opened in one click by the TabStax extension) |
| **Collaborators** | Team members with @handles, roles, and colour-coded ownership |
| **Agents** | AI assistants connected via MCP — they read and write the same Stax |
| **Breadcrumbs** | A timestamped trail of what happened — so returning feels like a pause, not a restart |

**A Stax is not a bookmark folder** (short section):
Bookmark folders save URLs. A Stax saves intent. The difference is the next action — the concrete step that answers "what do I do when I come back?" without having to think about it. That's what makes reopening a Stax different from reopening a browser history page.

**A Stax lives everywhere** (short section):
The same Stax is accessible across every HeyStax surface. Add a next action from your terminal. Complete it through Claude. Open the tabs from the extension. Check the priority in the dashboard. It's all the same workspace. No copy-paste. No sync lag. No version confusion.

**The Flowful Re-entry** (closing paragraph):
The moment of opening a cold Stax and immediately knowing what to do — that's a Flowful Re-entry. It's what HeyStax is built to produce. A Stax is the container that makes it possible.

**Links to:** What problem HeyStax solves, The HeyStax mental model, Creating your first Stax (under Surfaces → TabStax)

---

### PAGE 3 — `topics/tabstax_mental_model.md`
**Action: Rewrite — remove browser/website framing, make system-first**

**Current problem:** The mental model is framed as "instead of asking which websites am I using, ask which problem am I in." That's specifically a reframe for browser-tab users. It's useful — but it's scoped to one surface. The system mental model is bigger.

**Rewrite the page with this structure:**

```
---
title: The HeyStax mental model
parent: Getting Started
nav_order: 2
---
```

**Content to cover:**

**Opening — the shift:**
Most tools ask you to manage tasks. HeyStax asks you to manage context. The difference sounds subtle. It isn't.

A task manager says: here is the thing you need to do. A context manager says: here is the full state of being in the work — the tools you need, the thread you were following, the people involved, the next concrete move — preserved, named, and ready to reopen.

**The three questions every project re-entry requires:**
When you return to any piece of work, your brain has to answer three questions before anything useful happens:
1. What is the state of this project right now?
2. What were the specific tools and resources I was working with?
3. What is the next concrete action I should take?

HeyStax answers all three without asking you to reconstruct them. That's the model.

**Think in projects, not tools:**
Traditional thinking: "I need to open Notion, then find the doc, then check Jira, then pull up the dashboard."
HeyStax thinking: "I'm in the API Migration project." Everything else follows from that.

A Stax is the entry point for a project, not for a tool. You move between projects, not between apps.

**Context is shared:**
This applies to your teammates and your AI agents, not just you. When someone is added to a Stax, they get the same entry point. When an agent connects via MCP, it reads the same context. The model doesn't change depending on who or what is accessing the project — it's always: name the project, find the state, take the next action.

**The constraint is the feature:**
HeyStax shows you a small number of next actions per project — deliberately. Not because it can't hold more, but because the job is to answer "what do I do right now?" not "what is everything that could ever be done?" A Stax with one clear next action is more useful than a Stax with thirty vague ones.

**Closing:**
The mental model in one sentence: your brain should spend its energy doing the work, not reconstructing where you were.

**Links to:** What is a Stax?, What problem HeyStax solves, Surfaces

---

### PAGE 4 — `topics/creating_your_first_stax.md`
**Action: Move to Surfaces → TabStax. Update front matter only. One content edit.**

**Front matter change:**
```yaml
---
title: Creating your first Stax
parent: TabStax (Chrome extension)
nav_order: 4
---
```

**One content edit:**
At the top of the page, before the existing content, insert:

```markdown
This guide walks you through creating a Stax using the TabStax Chrome extension. If you're using the CLI or dashboard, the concept is the same — name a project, add links and next actions — but the steps differ. See [Hey CLI Guide](../hey-cli.html) or [Dashboard](dashboard.html) for those surfaces.
```

No other content changes. The Christmas shopping example is fine — it's concrete and relatable. It just needs to be correctly scoped as an extension walkthrough.

---

## Getting Started section landing page (`topics/getting-started.md`)

**Action: Update the intro paragraph**

Replace the current intro with:

```markdown
New to HeyStax? Start here.

These three guides explain what HeyStax is and how to think about it — before you pick up any surface. Once the model clicks, everything else is straightforward.

For step-by-step setup guides, go to [Surfaces](../surfaces/) and find the surface you're using.
```

This sets the right expectation: Getting Started is conceptual. Surfaces is how-to.

---

## What to check after making all changes

Run through this checklist:

1. `grep -r "parent: Getting Started" topics/ --include="*.md"` — should return exactly 3 files: `what_problem_tabstax_solves.md`, `what_is_a_stax.md`, `tabstax_mental_model.md`

2. `grep -r "parent: TabStax (Chrome extension)" topics/ --include="*.md"` — should return 4 files: `first_time_opening_tabstax.md`, `using_the_main_popup.md`, `adding_favourites.md`, `creating_your_first_stax.md`

3. Check all internal links on the rewritten pages still resolve. Particularly:
   - Any link to `creating_your_first_stax.html` from Getting Started pages — update path to `../surfaces/tabstax-extension/creating_your_first_stax.html` if the file has moved directory, or leave as-is if it stays in `topics/`

4. Check the Getting Started section landing page renders three children — not four.

---

## Terminology — enforce throughout all edits

| Wrong | Correct |
|---|---|
| "websites you use together" | "the resources and tools for a project" |
| "tabs" as a primary concept | "next actions" as the primary concept; tabs as one component |
| "the HeyStax extension" | "the TabStax extension" or "TabStax" |
| "Heystax" (lowercase s) | "HeyStax" |
| "todo" or "to-do" | "next action" |
| "tab group" | "Stax" |
| "bookmark" | (avoid — frames the wrong mental model) |

---

## What NOT to change

- Do not rename any files
- Do not edit the Use Cases section
- Do not touch the Surfaces section pages — they are correct
- Do not change the content of `first_time_opening_tabstax.md`, `using_the_main_popup.md`, or `adding_favourites.md` beyond what was specified in `surfaces-migration-live-state.md`
- Do not add new nav sections — the structure is correct, only content and parents change
