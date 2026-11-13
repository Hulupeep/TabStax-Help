---
title: Connect a worker to a role
parent: AI Integrations (MCP)
nav_order: 9
---

# Connect a worker to a role

{% include badge-partial.html %}

A **role** is the job, such as `@healthlensplus-main`. A **worker** is one folder on one computer doing that job. You connect the folder, and Claude Code or Codex working in it picks up the role's cards.

## Why it matters to you

Monday, 08:00. You assign a card and close the laptop lid. You don't open a chat to say "go". The worker picks it up, signs it as the role, and the card moves on the board.

## The one rule: the folder is the worker

Run `heystax connect` **inside the folder where the work happens**, such as the repo the bot edits. Not your home folder. Not the HeyStax repo, unless that is the work.

- Subfolders inherit the role.
- Two folders on one computer can be two roles: Codex in one repo, Claude Code in another.
- Connecting names the role. Work arrives only once something listens (step 4).

## How to do it

1. **Install the command once.** It is not on npm yet, so build it from the HeyStax repo: `cd cli && npm i && npm run build && npm link`. After each update, build again and check with `heystax --version`.
2. **Get a key.** On the role's card, open **How to connect a worker** and press **Get a key** (stax owner only). It starts `tsw_live_` and shows once. The role's other workers keep running.
3. **Connect the folder.** `cd` into the work folder, run `heystax connect`, and paste only the key. `heystax status` shows who this folder works as.
4. **Start listening.** Pick one:
   - **Just work.** Open Claude Code or Codex in the folder. It tells HeyStax what it starts, notes and finishes. In Claude Code, the [HeyStax plugin](claude-code-plugin) shows waiting cards; take one with `/heystax-work`.
   - **Always on.** `heystax listen --install --agent claude` (or `codex`). Each card gets a fresh session in its own git worktree, so your own files are never touched.
   - **Set how far it may go** with `--autonomy`: `edit` (files only), `build` (default: build, test, open a PR; never the database, never merge) or `full` (no prompts; go-ahead cards still wait). Careful on a client repo, `full` on your own venture.
5. **Check it worked.** The role card on the board changes from **Not connected** to **Listening**. Assign one small card to the role and watch it move to working.

## What one listener run does

{% capture s %}
{% include anim/node.html x=70 y=50 label="Card" sub="for @builder" kind="action" w=120 %}
{% include anim/edge.html x1=130 y1=50 x2=180 y2=50 kind="dispatch" d=0.4 %}
{% include anim/node.html x=250 y=50 label="Listener" sub="fresh worktree" kind="agent" w=130 d=0.6 %}
{% include anim/edge.html x1=315 y1=50 x2=355 y2=50 kind="write" d=1.0 %}
{% include anim/node.html x=410 y=50 label="Agent" sub="edits, commits" kind="agent" w=110 d=1.2 %}
{% include anim/edge.html x1=410 y1=76 x2=330 y2=140 cx=410 cy=140 kind="write" d=1.6 %}
{% include anim/node.html x=250 y=150 label="Listener" sub="pushes branch, opens PR" kind="agent" w=170 d=1.8 %}
{% include anim/edge.html x1=165 y1=150 x2=130 y2=150 kind="write" d=2.2 %}
{% include anim/node.html x=70 y=150 label="Card" sub="PR + note" kind="action" w=110 d=2.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 190" label="A card goes to the listener, the agent edits and commits in a fresh worktree, the listener pushes the branch and opens the PR, and the card gets the PR and a note" caption="The listener takes the card and opens a fresh worktree. The agent edits and commits, then exits. The listener pushes the card's own branch and opens the PR with this computer's git login. It never pushes main, never force-pushes and never merges. The card gets the PR and a note." svg=s %}

Nobody has to approve a push by hand at 02:00. If Claude Code refused a step, the card gets a note naming the step and the file where that rule lives.

## Keep the key safe

- The key you paste is never saved. The folder keeps its own worker token at `~/.config/hey/folders/`, readable only by you.
- Never put a key in a chat, a stax, a screenshot or a file.
- Your personal token also works in `heystax connect`, but **Get a key** is safer. Re-issuing a role key cuts off every worker of that role.

## When it goes wrong

| You see | What to do |
|---|---|
| The key prompt eats the next line | Run `heystax connect` on its own line, then paste only the key. Or `heystax connect --key-file <(read -rs K && printf %s "$K")`. |
| The role says **Not connected** | Nothing is listening for that role. Run step 4 in the right folder. Tap the label to read why. |
| A card says **Stalled since** | It was claimed, but no worker is alive on it. Start the worker again, or reassign the card. |
| A card has a note naming a refused step | Claude Code blocked it. Allow the step in the file the note names, or do it yourself. |
| A card says **Escalated** | It failed three times. The card's Listener note says why, and, with Telegram linked, you get one message with the reason. Fix the cause, then press **Clear** on the card. |
| The work landed in the wrong role | You connected the wrong folder. Run `heystax connect` again in that folder. |
| The worker says it cannot see the data | Give the folder a database to read. See [Give a worker what it needs](give-a-worker-access). |

## Coming next

{% include badge-planned.html %} One install from npm, and one `hey` command instead of two.

Now you can hand a card to a role and let the folder do the work, with every move signed in your stax.

**Read next:** [Roles, workers and their keys](roles-workers-tokens) · [How claim works](how-claim-works)
