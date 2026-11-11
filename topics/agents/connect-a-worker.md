---
title: Connect a worker to a role
parent: AI Integrations (MCP)
nav_order: 9
---

# Connect a worker to a role

{% include badge-partial.html %}

A **role** is the job, such as `@healthlensplus-main`. A **worker** is one folder on one computer doing that job. You connect the folder, and Claude Code or Codex working in it picks up the role's cards.

## Why it matters to you

You assign a card on Monday at 08:00. You don't open a chat to say "go". The worker in that folder picks it up, signs it as the role, and the card moves on the board.

## The one rule: the folder is the worker

Run `heystax connect` **inside the folder where the work happens**, such as the repo the bot edits. Not your home folder. Not the HeyStax repo, unless that is the work.

- Subfolders inherit the role.
- Two folders on one computer can be two different roles. Codex in one repo, Claude Code in another.
- Connecting says who this folder works as. Work only arrives once something listens (step 4).

## How to do it

1. **Install the command once.** It is not on npm yet, so build it from the HeyStax repo: `cd cli && npm i && npm run build && npm link`. The command is `heystax`. After you pull an update, run `npm run build` again.
2. **Get a key.** Open the stax in HeyStax. On the role this folder should work as, open **How to connect a worker** and press **Get a key**. The key starts `tsw_live_` and is shown once. Only the stax owner sees the button. Getting a key never changes the role key or cuts off the role's other workers.
3. **Connect the folder.** `cd` into the work folder, run `heystax connect`, and paste the key. Paste only the key. `heystax status` shows who this folder works as.
4. **Start listening.** Pick one:
   - **Just work.** Open Claude Code or Codex in the folder. The standing order makes it tell HeyStax what it starts, notes and finishes.
   - **Always on.** `heystax listen --install --agent claude` (or `codex`). It waits for work, and each card gets a fresh session in its own git worktree, so your own files are never touched.
5. **Check it worked.** The role card on the board changes from **No worker connected** to **Listening**. Assign one small card to the role and watch it move to working.

## Keep the key safe

- The key you paste is never saved. The folder keeps its own worker token at `~/.config/hey/folders/`, readable only by you.
- Never put a key in a chat, a stax, a screenshot or a file.
- A personal token or a role key also works in `heystax connect`, but use **Get a key**. Re-issuing a role key cuts off every worker of that role.

## When it goes wrong

| You see | What to do |
|---|---|
| The key prompt eats the next line | Run `heystax connect` on its own line, then paste only the key. Or `heystax connect --key-file <(read -rs K && printf %s "$K")`. |
| The role says **No worker connected** | Nothing is listening for that role. Run step 4 in the right folder. |
| A card says **Stalled since** | It was claimed, but no worker is alive on it. Start the worker again, or reassign the card. |
| The work landed in the wrong role | You connected the wrong folder. Run `heystax connect` again in that folder. |

## Coming next

{% include badge-planned.html %} One install from npm, and one `hey` command instead of two.

Now you can hand a card to a role and let the folder do the work, with every move signed in your stax.

**Read next:** [Roles, workers and their keys](roles-workers-tokens) · [How claim works](how-claim-works)
