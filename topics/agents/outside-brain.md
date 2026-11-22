---
title: Put an outside brain on a stax
parent: AI Integrations (MCP)
nav_order: 13
---

# Put an outside brain on a stax

{% include badge-partial.html %}

An **outside brain** is a bot that thinks somewhere else: a Grok Bot chat, a Claude project, ChatGPT. If it works on a stax, it gets a role there, its own column and its own key.

## Why it matters to you

You open your Grok chat at 06:00 and it answers in your name, because it writes through your personal key. Its column says "No one home". Your Chief sends it asks it never sees.

One rule fixes that: **every brain that works a stax is a role on that stax.** Then you can see what it did, it knows who it is, and nobody routes work to a brain that is asleep.

## The rule

- **The role is the job.** Such as `@timebreez-bot` for "Timebreez lead". The bot is the brain doing it, and you can swap it later.
- **Its own key.** Every move on the board says `@timebreez-bot`, not you.
- **It knows who it is.** `agent_whoami` returns its brain prompt: its handle, your mission and Never rules, its job on each stax, and who takes work from it now. The prompt holds no key.
- **You know how it wakes.** A listening worker picks a card up within a minute. A chat brain wakes when you open the chat, or when its own routine runs.

## How to do it

1. On the stax, add the role, or let your Chief create it.
2. On the role card, open **How to connect a worker** and press **Get a key**.
3. In the bot's app, add a HeyStax connector: `https://dash.heystax.ai/api/mcp`, with the header `Authorization: Bearer <the key>`. Turn your personal HeyStax connector off for this bot.
4. Ask the bot: "call agent_whoami and tell me your handle". It should say its role, not your name.
5. Give it its job. A bot that calls tools reads its brain prompt on its own. For one that cannot, press **Copy brain prompt** on its role card and paste it into the bot's instructions.
6. Give it an hourly routine that checks its comments and cards, if it can run on a schedule. If it has a webhook, [give it a wake address](wake-a-brain) too.
7. Check the role card. Once the bot acts with its key, it shows **🧠 Brain · acted 2h ago**.

## Will a card I add get picked up?

| The card goes to | Who picks it up | When |
|---|---|---|
| A role with a listening worker, such as `@timebreez-builder` | That worker | Within a minute |
| A role whose brain is a chat, such as `@timebreez-bot` | The bot | Next time you open the chat, or its routine runs |
| A person, such as `@gaia` | That person | They get a Telegram message |

Who added the card does not matter. Who it is assigned to does.

A brain-led role may never have a worker. So its card says **Brain**, not **Not connected**, and waiting work reads "2 waiting for its next turn".

## Scenario 1: the Timebreez lead

Colm owns the stax. `@timebreez-bot` is a Grok Bot chat that leads Timebreez. `@timebreez-builder` is Claude Code, listening on the Minisforum. Gaia tests.

{% capture s %}
{% include anim/node.html x=90 y=40 label="Colm" sub="asks in Grok" kind="person" w=130 d=0.2 %}
{% include anim/edge.html x1=155 y1=40 x2=245 y2=40 kind="write" d=0.6 %}
{% include anim/node.html x=340 y=40 label="@timebreez-bot" sub="its own key" kind="agent" w=180 d=0.9 %}
{% include anim/plane.html x=20 y=96 w=440 h=92 label="Timebreez stax" d=1.2 %}
{% include anim/edge.html x1=320 y1=66 x2=130 y2=130 kind="write" d=1.5 %}
{% include anim/edge.html x1=360 y1=66 x2=350 y2=130 kind="write" d=1.7 %}
{% include anim/node.html x=130 y=150 label="Check the 2026 booking" kind="action" w=190 d=2.0 %}
{% include anim/node.html x=350 y=150 label="Re-run stage 3 import" kind="action" w=180 d=2.2 %}
{% include anim/edge.html x1=130 y1=170 x2=130 y2=206 kind="dispatch" d=2.6 %}
{% include anim/edge.html x1=350 y1=170 x2=350 y2=206 kind="dispatch" d=2.8 %}
{% include anim/node.html x=130 y=232 label="@timebreez-builder" sub="within a minute" kind="agent" w=190 d=3.1 %}
{% include anim/node.html x=350 y=232 label="Gaia" sub="in Telegram" kind="person" w=140 d=3.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 270" label="Colm asks the Timebreez bot once; the bot, with its own key, adds one card for the builder and one for Gaia, and each picks theirs up" caption="Colm asks once in the Grok chat. The bot, writing with its own key, adds a card for the builder and a card for Gaia. The builder picks its card up within a minute and reports with a pull request. Gaia gets hers in Telegram. Every move on the board is signed by whoever made it." svg=s %}

1. Colm asks: "Abigale's import still blocks. Sort it."
2. The bot adds a card for the builder: "Check why a 2026 booking blocks Abigale", with the why and when it is done.
3. Within a minute the builder picks it up and reports its verdict with a pull request.
4. The bot adds a second card for Gaia: "Re-run the stage 3 import on staging".

**You can check.** Two cards, three actors, every move named. Nobody wrote as Colm except Colm.

## Scenario 2: the Chief and a sleeping brain

1. At 04:20 the Chief sees CI went red on Timebreez main.
2. The builder is listening. `@timebreez-bot` is not.
3. The Chief puts the fix on a card for the builder, and leaves the bot a one-line note.
4. At 06:00 Colm opens the Grok chat. The bot reads its comments, sees the note, and finds the fix already in a pull request.

The work did not wait for anyone to wake up, and the lead still knows what happened.

Now you can let any bot work your stax, see everything it did under its own name, and swap the brain without losing the job.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Give a worker what it needs](give-a-worker-access) · [Roles, workers and their keys](roles-workers-tokens)
