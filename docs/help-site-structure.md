# HeyStax Help Site — Structure Reference

**URL:** https://hulupeep.github.io/TabStax-Help/
**Repo:** `Hulupeep/TabStax-Help`
**Engine:** Jekyll + Just the Docs v0.10.0 (GitHub Pages)
**Colour scheme:** tabstax (custom)

---

## Navigation Tree

```
Home (README.md)                                    nav_order: 1
│
├── Getting Started                                 nav_order: 2
│   ├── Get started with HeyStax                    nav_order: 1  ← action-first quick start
│   ├── What problem HeyStax solves                 nav_order: 2
│   ├── The HeyStax mental model                    nav_order: 2
│   └── What is a Stax?                             nav_order: 3
│
├── Surfaces                                        nav_order: 3
│   ├── TabStax (Chrome extension)                  nav_order: 1  [has_children]
│   │   ├── First time opening TabStax              nav_order: 1
│   │   ├── Using the TabStax popup                 nav_order: 2
│   │   ├── Adding Favourites                       nav_order: 3
│   │   └── Creating your first Stax               nav_order: 4  ← extension-specific walkthrough
│   ├── Dashboard                                   nav_order: 2
│   ├── Hey CLI                                     nav_order: 3  [has_children]
│   │   └── Hey CLI Guide                           nav_order: 1
│   ├── AI Integrations (MCP)                       nav_order: 4  [has_children]
│   │   ├── Connect to Claude.ai                    nav_order: 1
│   │   └── Connect to Claude Code                  nav_order: 2
│   └── Timesheets                                  nav_order: 5
│
├── Account & Sync                                  nav_order: 4
│
├── Use Cases                                       nav_order: 5  [no children in nav]
│   ├── 16 Hero pages (nav_exclude: true)
│   └── 9 collection files (nav_exclude: true)
│
└── [Retired] Working with Stax                     nav_exclude: true
```

---

## Page-by-Page Reference

### Home

| Field | Value |
|-------|-------|
| **File** | `README.md` |
| **URL** | `/` |
| **Purpose** | Landing page — orients visitors, links to all sections |

> Pick up where your mind left off. You know you were working on something. You just can't get back in. Not because the work disappeared. Because the *context* did. The thread you were holding — what you were doing, what came next, why it mattered — that's what's gone. And without the thread, even opening the project feels like starting over. That's not a focus problem. It's a design problem. And it compounds.

**Links to:** What problem HeyStax solves, What is a Stax, First time opening TabStax, Creating your first Stax, Mental Model, Hey CLI Guide, MCP Claude.ai, MCP Claude Code

---

### Getting Started

| Field | Value |
|-------|-------|
| **File** | `topics/getting-started.md` |
| **Purpose** | Section index — action-first onboarding |

> Go to dash.heystax.ai and sign up. Then follow Get started with HeyStax. It takes five minutes and gets you to your first project with next actions, completed work, and a collaborator. The other guides in this section explain the concepts underneath — worth reading once you've felt the thing working.

---

#### Get started with HeyStax

| Field | Value |
|-------|-------|
| **File** | `topics/creating_your_first_stax.md` |
| **Parent** | Getting Started |
| **Purpose** | Action-first quick start — 5 steps to first Flowful Re-entry + collaboration |

> Five minutes. One project. Step 1: sign up at dash.heystax.ai. Step 2: create a Stax named after a real project. Step 3: write three concrete next actions. Step 4: complete one. Step 5: close the tab, come back tomorrow — your next action is right there. Then level 2: create a shared Stax, add a collaborator, both add actions. No more WhatsApp messages that disappear.

**Links to:** TabStax extension, Hey CLI, Connect to Claude.ai, What is a Stax, Use Cases

---

#### What problem HeyStax solves

| Field | Value |
|-------|-------|
| **File** | `topics/what_problem_tabstax_solves.md` |
| **Parent** | Getting Started |
| **Purpose** | Core positioning — reconstruction tax, momentum framing, collaboration gap |

> The real problem isn't disorganisation. It's loss of momentum. You know what it feels like to be deep in something. Hours disappear. You think clearly, move fast, connect dots. Momentum is your power source. The problem is what happens when it breaks. You don't just stop doing the task — you lose access to the state you need to do it. The thread dissolves. And getting it back costs more than the work itself.

**Links to:** Mental Model, What is a Stax, Creating your first Stax, Surfaces

---

#### The HeyStax mental model

| Field | Value |
|-------|-------|
| **File** | `topics/tabstax_mental_model.md` |
| **Parent** | Getting Started |
| **Purpose** | Mindset shift — manage context not tasks, think in projects not tools |

> Most tools ask you to manage tasks. HeyStax asks you to manage context. A task manager says: here is the thing you need to do. A context manager says: here is the full state of being in the work — the tools you need, the thread you were following, the people involved, the next concrete move — preserved, named, and ready to reopen. Three questions every project re-entry requires: state, tools, next action. The constraint is the feature — one clear next action beats thirty vague ones.

---

#### What is a Stax?

| Field | Value |
|-------|-------|
| **File** | `topics/what_is_a_stax.md` |
| **Parent** | Getting Started |
| **Purpose** | Core concept — system-first definition with components table |

> A Stax is a named project workspace. Not a tab group. Not a to-do list. A live container for everything needed to step back into a piece of work and immediately know what's happening and what to do next. Components: Name, Next Actions, Priority, Tabs & Links, Collaborators, Agents, Breadcrumbs. A Stax lives everywhere — same data across extension, CLI, dashboard, MCP. The Flowful Re-entry is what HeyStax is built to produce.

---

### Surfaces

| Field | Value |
|-------|-------|
| **File** | `topics/surfaces/index.md` |
| **Purpose** | Section index — table of all HeyStax surfaces with access links |

> HeyStax meets you where you work. The same Stax, the same next actions, the same momentum — across every surface.

**Contains table linking:** TabStax extension, Dashboard, Hey CLI, AI Integrations (MCP), Timesheets

---

#### TabStax (Chrome extension)

| Field | Value |
|-------|-------|
| **File** | `topics/surfaces/tabstax-extension.md` |
| **Parent** | Surfaces |
| **Purpose** | Browser surface overview — save/restore tabs, tags, priority, share, auto-sync |

> TabStax is the Chrome extension that started it all. It turns your browser into a workspace launcher. You're deep in a project — six tabs open, a spreadsheet, two docs, a Jira board, a Slack thread. You need to leave. Tomorrow you won't remember which tabs, which doc, what you were about to do next. TabStax captures all of that in one click. Name it. Add a next action. Close everything. When you come back — tomorrow, next week, next month — open the Stax. Every tab loads. The next action is right there. You're working in seconds, not minutes. Momentum preserved.

**Links to:** Chrome Web Store install, First time opening, Using the popup, Adding Favourites, Creating your first Stax

---

##### First time opening TabStax

| Field | Value |
|-------|-------|
| **File** | `topics/first_time_opening_tabstax.md` |
| **Parent** | TabStax (Chrome extension) |
| **Purpose** | First-run UX walkthrough — pin icon, see tabs, name Stax, add tags, click New |

> You've just installed Heystax, pinned it to your browser toolbar, and clicked the icon. This is the very first screen you'll see. It's designed to capture your current browser window — all the tabs you have open right now — and save them as your first Stax. This gives you a safe, named workspace you can return to anytime.

**Has screenshots:** yes (3 — install click, naming, start page)

---

##### Using the TabStax popup

| Field | Value |
|-------|-------|
| **File** | `topics/using_the_main_popup.md` |
| **Parent** | TabStax (Chrome extension) |
| **Purpose** | Popup UI guide — My Next Actions (pink glow, cross-project), My Stax (open/search/create) |

> The TabStax popup is the browser extension interface — your quick-access panel for next actions and Stax while you're working in Chrome. When you're juggling multiple projects, your brain has to answer two questions: 'What should I do next?' and 'Which project should I open?' The main popup splits those questions into two clean sections so you can either follow the last thing you were working on, pick a different next action that matters more right now, or open a whole Stax.

**Has screenshots:** yes (2 — main popup, collapsed view)

---

##### Adding Favourites

| Field | Value |
|-------|-------|
| **File** | `topics/adding_favourites.md` |
| **Parent** | TabStax (Chrome extension) |
| **Purpose** | Pin up to 3 Stax as quick-access pills — focus filter for busy seasons |

> When you're deep in a project season — maybe billing week, or a launch sprint — you don't want to scroll through a long list every time you switch contexts. Favourites let you pin the Stax that matter *right now* to the top, so your brain doesn't have to search. It's a focus filter: keep the current priorities visible, and everything else stays one click away when you need it.

**Has screenshots:** yes (2 — star icon, favourite pills)

---

#### Dashboard

| Field | Value |
|-------|-------|
| **File** | `topics/surfaces/dashboard.md` |
| **Parent** | Surfaces |
| **URL** | dash.heystax.ai |
| **Purpose** | Priority planning surface — Attention Blocks + Actions Mode |

> The HeyStax Dashboard at dash.heystax.ai is where you see everything at once — and decide what to enter first. Fifteen projects in flight. Looking at all of them is paralysing. You don't know which one to enter, so you enter none. The Dashboard gives you two lenses for the same data: Attention Blocks (drag into Must/Should/Good/Meh priority lanes, pink glow on most important action) and Actions Mode (execution lens, single column, check off, next surfaces).

---

#### Hey CLI

| Field | Value |
|-------|-------|
| **File** | `topics/hey-cli-section.md` |
| **Parent** | Surfaces |
| **Purpose** | Section index — terminal surface intro |

> Never leave your editor. `hey ls` to see what's next. `hey done 1` to check it off. `hey "write the migration script"` to capture a thought before it fades. Momentum stays unbroken.

---

##### Hey CLI Guide

| Field | Value |
|-------|-------|
| **File** | `topics/hey-cli.md` |
| **Parent** | Hey CLI |
| **Install** | `npm i heystax-cli` |
| **Purpose** | Full CLI reference — capture thoughts, list actions, manage projects, priority system, 7-action limit, persona use cases, AI integration |

> The Problem It Solves — catch a thought before it fades... `hey "validate the signup form"` — That's it. The thought exists now. It's in your project. Go back to what you were doing. You're mid-flow — coding, debugging, talking to Claude — and a thought surfaces: "Need to check the rate limits on that endpoint." In the next three seconds, one of two things happens: 1. You capture it. 2. It's gone.

**Sections:** Quick Start, Command Reference (adding, listing, managing, projects, auth), Priority System, 7-Action Limit, Use Cases by Persona (solo dev, tech lead, AI-assisted dev, agency/freelancer), Troubleshooting

---

#### AI Integrations (MCP)

| Field | Value |
|-------|-------|
| **File** | `topics/mcp-section.md` |
| **Parent** | Surfaces |
| **Purpose** | Section index — MCP concept, what you can ask, supported assistants |

> Heystax connects to AI assistants through the Model Context Protocol (MCP). This lets Claude and other AI tools read your Stax, manage Next Actions, and log breadcrumbs — all through natural conversation. What you can do: 'What are my stax?', 'Add review PR #42 to WebApp', 'Mark the first action on WebApp as done', 'What's on my plate?'

**Links to:** Connect to Claude.ai, Connect to Claude Code

---

##### Connect to Claude.ai

| Field | Value |
|-------|-------|
| **File** | `topics/mcp-claude-ai.md` |
| **Parent** | AI Integrations (MCP) |
| **MCP URL** | `https://dash.heystax.ai/api/mcp` |
| **Purpose** | Step-by-step OAuth setup for Claude.ai integration |

> Connect your Stax and Next Actions to Claude.ai so you can manage your projects through conversation. Prerequisites: A Heystax account with Pro or Trial plan. A Claude account at claude.ai (free tier works). Step-by-step: Open Claude.ai settings → Integrations → Add Integration → enter `https://dash.heystax.ai/api/mcp` → authenticate → approve access.

---

##### Connect to Claude Code

| Field | Value |
|-------|-------|
| **File** | `topics/mcp-claude-code.md` |
| **Parent** | AI Integrations (MCP) |
| **Purpose** | Two connection options — via Claude.ai connector or manual CLI add |

> Use your Stax and Next Actions directly from the terminal while coding with Claude Code. Option 1: Claude.ai connector (recommended) — if already connected to Claude.ai, it automatically works in Claude Code. Verify with `/mcp`. Option 2: Manual — `claude mcp add heystax --transport sse https://dash.heystax.ai/api/mcp/sse`.

---

#### Timesheets

| Field | Value |
|-------|-------|
| **File** | `topics/surfaces/timesheets.md` |
| **Parent** | Surfaces |
| **URL** | dash.heystax.ai/time |
| **Purpose** | Flow-native time tracking built on Stax — weekly view, evidence-aware, draft→submit |

> HeyStax Timesheets at dash.heystax.ai/time let you log hours against Stax — the projects you're already tracking. Most time tracking tools ask you to context-switch into a separate system, remember what you worked on, and manually log it. That's friction on top of friction. HeyStax already knows your projects. It knows your next actions. It knows when you were last active. Timesheets build on top of that — you're logging time against work contexts that already exist.

---

### Account & Sync

| Field | Value |
|-------|-------|
| **File** | `topics/account-sync.md` |
| **Purpose** | Free vs Pro comparison, local-only mode, cross-device sync, signup flow |

> HeyStax works locally with no account. Sign in to unlock cloud sync, sharing, collaboration, and access across every surface. Free: unlimited local Stax, no account needed. Pro: cloud sync, sharing, collaboration, timesheets, Attention Blocks, MCP + CLI.

---

### Use Cases

| Field | Value |
|-------|-------|
| **File** | `topics/usecases/index.md` |
| **Purpose** | Master index — 70+ real-world scenarios, 16 hero pages, categorised by work and life |

> Real people. Real chaos. Real Stax. Below you'll find over 70 ways people actually use HeyStax — from high-pressure work scenarios to deeply personal life moments. Each story shows how a named workspace with tabs, next actions, and context can cut through chaos and help you stay present.

**All child pages are `nav_exclude: true`** — they're linked from the index, not shown in nav.

---

#### 16 Hero Use Cases (dedicated pages)

| File | Persona | Domain |
|------|---------|--------|
| `consultant.md` | Independent consultant, 3 clients, 5 min to switch | Work: Multi-client |
| `neurodivergent-builder.md` | ND founder, 5 parallel projects, setup cost kills re-entry | Work: Deep work |
| `scrum-master.md` | Scrum master, shared standup cockpit for Team Falcon | Work: Rituals |
| `sme-owner.md` | Design studio owner, 6 daily apps, morning ops rebuild | Work: SME |
| `devops.md` | DevOps engineer, P1 incident, 5-10 min spinup cost | Work: Ops |
| `product-manager.md` | PM, 3 parallel streams, 15-min gap between meetings | Work: Multi-stream |
| `public-defender.md` | Public defender, 3 cases, court in 10 min, 100°F LA | Work: Legal/crisis |
| `remote-founder.md` | Remote founder, investor pitch + interview + roadmap same afternoon | Work: Multi-context |
| `nd-parent.md` | Parent, school admin chaos, shared to-do with co-parent | Life: Family |
| `special-needs-mum.md` | Mum, special needs child, school incident, meeting tomorrow | Life: Family/crisis |
| `surgery-prep.md` | Patient, surgery in 4 weeks, pre-op + insurance + home logistics | Life: Health |
| `funeral-planning.md` | Adult child, father died, funeral logistics while grieving | Life: Crisis/loss |
| `retiree.md` | Retiree, pension + second act, vague "someday" → concrete experiments | Life: Dreams |
| `marathon-training.md` | 240lb first-time marathoner, 16-week build, scattered plans | Life: Dreams |
| `returning-actor.md` | Woman in 40s, buried acting dream, structured re-entry attempt | Life: Dreams |
| `caregiver.md` | Adult child, ageing mum, health portals + legal + siblings | Life: Care |

---

#### Collection Files (numbered scenarios)

| File | Scenarios | Focus |
|------|-----------|-------|
| `10niche.md` | #11–20 | PM, sales engineer, customer success, data analyst, startup founder, HR, legal, teacher, architect, event planner |
| `11-20.md` | #11–20 | Same content as 10niche (duplicate) |
| `21-30.md` | #21–30 | Agency founder, recruiter, journalist, compliance officer, ER nurse, wedding planner, academic, financial advisor, social worker, film editor |
| `31-40.md` | #31–40 | Public defender, immigration lawyer, firefighter, surgeon, diplomat, humanitarian, military spouse, chaplain, election official, disaster coordinator |
| `41-50.md` | #41–50 | Emergency vet, midwife, air traffic controller, NICU nurse, sports coach, refugee caseworker, forensic accountant, investigative journalist, crisis negotiator, search & rescue |
| `41-50a.md` | #41–50 | Alternate version of same scenarios |
| `51-60_nontraditional.md` | #1–10 | Special needs mum, surgery prep, funeral planning, caregiver, retiree, marathon training, returning actor, ND parent, divorce navigation, house move |
| `61-70 real life.md` | #1–10 | Retiree second act, marathon runner, returning actor, ND parent school crisis, special needs mum, surgery prep, funeral planning, caregiver, professor running for senate, whistleblower |
| `71_75 real life 2.md` | #1–5 | Professor/senator candidate, whistleblower, others |

---

#### Supporting Files

| File | Purpose |
|------|---------|
| `topten_use_cases.md` | Condensed top 10 with Before/After format |
| `category.md` | Category taxonomy design — 14 categories across work and life domains |
| `headings.md` | Extracted heading structure from all collection files |

---

### Retired Pages

| File | Status |
|------|--------|
| `topics/working-with-stax.md` | `nav_exclude: true` — redirects to Surfaces → TabStax |

---

## Terminology

| Term | Meaning |
|------|---------|
| **HeyStax** | The platform/system — all surfaces, all data |
| **Stax** | A named workspace — tabs + next actions + priority + collaborators + agents + breadcrumbs |
| **TabStax** | The Chrome extension surface specifically |
| **Flowful Re-entry** | Opening a cold Stax and immediately knowing what to do |
| **Reconstruction tax** | The time/energy cost of rebuilding context when returning to a project |
| **Surfaces** | The different interfaces into HeyStax (extension, dashboard, CLI, MCP, timesheets) |
| **Next Actions** | Concrete steps attached to a Stax — what to do when you return |
| **Breadcrumbs** | Timestamped trail of what happened — captured with `hey -x` |
| **Attention Blocks** | Dashboard priority lanes — Must / Should / Good / Meh |
| **Actions Mode** | Dashboard execution lens — one action per project, ordered by priority |

---

## Key URLs

| Surface | URL |
|---------|-----|
| Help site | https://hulupeep.github.io/TabStax-Help/ |
| Dashboard | https://dash.heystax.ai |
| Timesheets | https://dash.heystax.ai/time |
| MCP endpoint | https://dash.heystax.ai/api/mcp |
| MCP SSE endpoint | https://dash.heystax.ai/api/mcp/sse |
| Chrome Web Store | https://chromewebstore.google.com/detail/heystax/gfdcobncoohhlhppmoidalociahfdcam |
| CLI install | `npm i heystax-cli` |
| Main site | https://heystax.ai |
