# CLAUDE.md

Guidance for anyone, human or agent, writing pages for the HeyStax help site:
https://hulupeep.github.io/TabStax-Help/ (Jekyll, Just the Docs, GitHub Pages).

## What HeyStax is

HeyStax is the **operational plane** for your work. One typed graph holds your stax and
everything in them: next actions, people, agents, dates, goals, records, links. Every surface
reads and writes that same graph: the dashboard, the TabStax extension, the `hey` CLI,
AI clients over MCP, and Telegram. People and agents are both actors on it, addressed the
same way by `@handle`. Every write is attributed.

- **HeyStax** is the system. **TabStax** is the Chrome extension that saves and reopens a
  stax's tabs. Never mix them up.
- It is an agent operations platform where agents are peers, not bots.
- A **stax** (singular and plural) is a named piece of work in the graph.

## The thread on every page: own your own cognition

Your working state (what you are doing, what is next, why, and who is on it) belongs to you.
Not to one chat app's memory. Not to one person's head. Every page lands at least one of
these four beats, in the reader's own terms, never as a slogan:

1. **It is yours.** Your context sits in your account, not inside a model vendor.
2. **It travels.** The same context opens in Claude, ChatGPT, Claude Code, the CLI.
3. **You set the edges.** You decide what an agent can see and do.
4. **You can check.** You can see what every actor did in your name.

Agents extend your thinking. They never take custody of it.

Good: "You did not paste your context. It was already yours, and it travelled."
Bad: "HeyStax empowers you to own your cognition."

## Truth rule

Before you name any capability, look it up in `_data/ledger.yml` (rendered at
`docs/shipped-ledger.md`).

| Ledger state | What the page may say |
|---|---|
| `shipped`, `live`, `unverified` | Describe it as it works today, using the ledger's wording. |
| `partial` | Say which part works today. Add `{% include badge-partial.html %}`. |
| `planned` | Future tense only. Add `{% include badge-planned.html %}`. Put it in a "Coming next" box. |

`scripts/check_truth.py` enforces this on every pull request. If the product changed, update the
ledger first, with evidence, then the page.

- The MCP address is `https://dash.heystax.ai/api/mcp`. Never `dash.tabstax.app`.
- Say "the HeyStax Telegram bot" for what exists today. `@notify` is planned.

## Voice

Short sensory sentences. Warm, not effusive. The reader is smart, busy and tired. They live or
die by momentum, and they lose it on every switch.

- Concrete over abstract: "30 tabs", "a scrolled-away chat", "Monday, 08:00".
- One idea per sentence. Paragraphs of three lines or fewer.
- Name the felt moment before the mechanism.
- Use "you". Use real names in scenarios (Bob, Alice), never "the user".

### Never write

`scripts/check_voice.py` flags these.

- Em dashes. Use a full stop, a comma, or a colon.
- "project management", "productivity tool", "productivity app", "flow manager", "focus app",
  "task manager".
- "connect your life to AI".
- Wellness framing: "wellness", "self-care", "mindfulness", "peace of mind", "calm your mind".
- Hype: "revolutionary", "game-changer", "game-changing", "seamless", "supercharge", "unleash",
  "cutting-edge", "next-level", "effortless", "world-class", "best-in-class", "10x".
- Credentialism: awards, "trusted by", "built by experts".
- Internal names: table names, JSON, migration ids, edge functions, unless the ledger's wording
  uses them.

### Lines you may use

- "ChatGPT has a text box. HeyStax has the nervous system."
- "Your typed graph. Any LLM."
- "Always know what to do next."
- "Pick up where your mind left off." (extension pages)

## Page shape

1. **Title**: short, verb-first where it fits ("Connect Claude to your stax").
2. **What it is**: one or two sentences.
3. **Why it matters to you**: two or three sentences tied to a real moment.
4. **How to do it**: 3 to 7 numbered steps, few words each.
5. **The animation** from `_includes/anim/` (once the kit lands), with a caption that carries
   the same meaning in text.
6. **Payoff**: one line starting "Now you can".

A reader should get the whole page in under 30 seconds.

Front matter: `title`, `parent` (if nested), `nav_order`. Archived pages get `nav_exclude: true`.

## Animations

- Inline SVG plus CSS from the shared kit. No JS animation libraries. No video for diagrams.
- Real-UI clips (`.webm` with a poster frame) only on scenario pages, recorded from the live product.
- Every animation has a `<figcaption>`. `prefers-reduced-motion` shows the final frame.
- Readable at 375px wide and in dark mode.

## Scenarios

Scenario pages live in `topics/scenarios/` and follow `docs/scenario-template.md`: cast,
starting state, steps, what the graph looks like after, the cognition beat, and a table of each
step's ledger state. A scenario with any planned step is badged on the page and on its index card.

## Checks before you open a pull request

```bash
python3 scripts/check_truth.py --changed origin/main
python3 scripts/check_voice.py --changed origin/main
python3 -m unittest discover -s scripts -p "test_*.py"
python3 scripts/render_ledger.py --check
```

## Repo map

- `README.md`: home page.
- `topics/`: help pages.
- `_data/ledger.yml`: what is live. `docs/shipped-ledger.md` is generated from it.
- `_includes/`: badges, and later the animation kit.
- `screenshots/`: UI captures. Replace old TabStax popup shots when a page is rewritten.
- `scripts/`: checks and their tests.
- Work is tracked in epic #9.


## Outcome mission clarification (29 October 2026)

Lead with what HeyStax is: an operational plane for persistent intent. The three simplest reader-facing primitives are **Mission (why), Goal (observable result), Next Action (who does what next)**. Humans and interchangeable AI agents share durable responsibility, evidence, decisions and context. Continuity serves outcomes, not activity counts.

Do not treat PR volume, tasks, emails or demos as verified business results. The founder's personal commercial purpose is one application, not a restriction on users' missions. Clinical/regulatory, construction and community outcomes are examples, not claims of automated authorisation. Describe the full outcome-driven autonomous loop as the product vision unless the shipped ledger provides fresh verification.

Canonical mission: `topics/what-heystax-really-is.md`. Founder account: `topics/why-im-building-heystax.md`. Editorial drafts: `blog/`. Keep the existing voice, truth-gate, and navigation rules above.
