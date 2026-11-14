---
title: Put an outside brain on a stax
parent: AI Integrations (MCP)
nav_order: 13
---

# Put an outside brain on a stax

{% include badge-partial.html %}

An **outside brain** is a bot that thinks somewhere else: a Grok Bot chat, a Claude project, ChatGPT. If it does work on a stax, it gets a role there, its own column and its own key.

## Why it matters to you

You open your Grok chat at 06:00 and ask "who do you send work to?". It answers in your name, because it writes through your personal key. On the board its column said "No one home", though something was running it. Your Chief sends it asks it never sees.

One rule fixes that: **every brain that works a stax is a role on that stax.** Then you can see what it did, it knows who it is, and nobody routes work to a brain that is asleep.

## The rule

- **Register it.** One role per job, such as `@timebreez-bot` for "Timebreez lead". The role is the job. The bot is the brain doing it, and you can swap it later.
- **Give it its own key.** It writes cards, comments and reports with that key, never yours. Then every move on the board says `@timebreez-bot`, not you.
- **Tell it who it is.** HeyStax writes that for you. The bot calls `agent_whoami` and gets its brain prompt: its handle, your mission and Never rules, its job on each stax, and who takes work from it now. For a bot you can only reach by pasting, press **Copy brain prompt** on its role card. The prompt holds no key.
- **Know how it wakes.** A worker that listens picks a card up within a minute. A chat brain wakes only when you open the chat, or when its own routine runs.

## How to do it

1. On the stax, add the role, or let your Chief create it.
2. On the role card, open **How to connect a worker** and press **Get a key**.
3. In the bot's app, add a HeyStax connector: `https://dash.heystax.ai/api/mcp`, with the header `Authorization: Bearer <the key>`. Turn your personal HeyStax connector off for this bot.
4. Ask the bot: "call agent_whoami and tell me your handle". It should say its role, not your name.
5. Give it its job. If it can call tools, it reads its brain prompt from `agent_whoami` on its own. If not, press **Copy brain prompt** on its role card and paste that into the bot's instructions. Both give the same text, read from HeyStax, so the next change you make to its job reaches it too.
6. If the bot can run on a schedule, give it an hourly routine that checks its comments and its cards.
7. Check the role card. Once the bot acts with its key, the card shows **🧠 Brain · acted 2h ago**. Tap it to read how the role wakes.

## Will a card I add get picked up?

| The card goes to | Who picks it up | When |
|---|---|---|
| A role with a listening worker, such as `@timebreez-builder` | That worker | Within a minute |
| A role whose brain is a chat, such as `@timebreez-bot` | The bot | Next time you open the chat, or its routine runs |
| A person, such as `@gayathrri0192` | That person | They get a Telegram message |

It does not matter whether you add the card in the board or the bot adds it. What matters is who it is assigned to.

A brain-led role may never have a worker. It runs from the top: it hands work out and picks up work given to it. So its card says **Brain**, not **Not connected**, and waiting work reads "2 waiting for its next turn".

## Scenario 1: the Timebreez lead

**Cast:** Colm (owner). `@timebreez-bot`, a Grok Bot chat that leads Timebreez. `@timebreez-builder`, Claude Code listening on the Minisforum. Gaia, who tests.

1. Colm asks in the Grok chat: "Abigale's import still blocks. Sort it."
2. The bot, writing as `@timebreez-bot`, adds a card for `@timebreez-builder`: "Check why a 2026 booking blocks Abigale", with the why and when it is done.
3. Within a minute the builder picks it up, reads the staging data, and reports its verdict with a pull request.
4. The bot adds a second card for Gaia: "Re-run the stage 3 import on staging". Gaia gets it in Telegram.
5. The board shows each step signed by whoever did it. Colm did one thing: ask.

**After:** two cards, three actors, every move named. Nobody wrote as Colm except Colm.

## Scenario 2: the Chief and a sleeping brain

**Cast:** the Chief of Staff (`@chief-of-staff`, one across all your stax). `@timebreez-bot`, whose brain is a chat with no routine.

1. At 04:20 the Chief sees CI went red on Timebreez main.
2. It looks at the roles. The builder is listening. `@timebreez-bot` is not.
3. The Chief puts the fix on a card for the builder, not for the bot, and leaves the bot a one-line note on the card.
4. At 06:00 Colm opens the Grok chat. The bot reads its comments first, sees the note, and finds the fix already in a pull request.

**After:** the work did not wait for anyone to wake up, and the lead still knows what happened.

Now you can let any bot work your stax, see everything it did under its own name, and swap the brain without losing the job.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Give a worker what it needs](give-a-worker-access) · [Roles, workers and their keys](roles-workers-tokens)
