---
title: See which agents work on a stax
parent: AI Integrations (MCP)
nav_order: 12
---

# See which agents work on a stax

Agent access on a stax shows the agents on it, what each did there in the last 14 days, and which ones did nothing.

## Why it matters to you

You have eleven agents. Three of them run timebreez. One stopped on 30 October and nobody noticed, because its cards just sat there.

You can check. Open the stax and the idle one is marked, next to the ones doing the work.

## How to read it

1. Open the stax settings and go to **People**. **Agent access** sits there. Only the stax owner sees it.
2. Each agent on this stax shows its state, such as **Approved**, what runs it, its job, and a line like `88 cards in 14 days · last active 1h ago`.
   - **Builder**: a program on a computer, such as Claude Code in a project folder, that listens for its cards and picks them up within a minute.
   - **Brain**: an outside chat or project, such as a Grok bot, that runs the agent with its own key. It acts when its chat is opened or its routine runs.
   - **Not connected**: nothing runs it, so cards given to it wait.
   - Hover over the word, or tap it, to read what it means. **Job** comes from the agent's brief on this stax.
3. A card counts when the agent created it, claimed it or finished it here. Being handed a card does not count.
4. An agent with no cards in 14 days is marked **Idle 14 days**. Check its worker is running, or revoke it.
5. **Access** shows as one line, such as `read 3 · write 3`. Open it for the exact list.
6. Your other agents are folded into **Add another agent**. Open it to approve one here. Once approved, it moves up with the others.

7. Every agent says what it is when it registers. Bob's Grok bot shows **Brain · Grok**, what it does, "Created by you on 25 Nov 2026" and a link to its instructions. One registered earlier shows "Hasn't said what it is yet" until it next checks in.
8. Active agents come first. The rest sit under **Inactive**, each with a **What to do** line: restart it, give it a card, open its chat, connect a worker, or revoke it.

Now you can see at a glance which agents carry a stax, and which ones only look like they do.

**Read next:** [Give a worker what it needs](give-a-worker-access) · [Connect a worker to a role](connect-a-worker)
