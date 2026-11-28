---
title: Add robots, fridges and other bots with HeyMailbox
parent: AI Integrations (MCP)
nav_order: 20
---

# Add robots, fridges and other bots with HeyMailbox

{% include badge-partial.html %}

**HeyMailbox** lets something that can't plug into HeyStax still work on your stax. It leaves a signed note in a place HeyStax watches. HeyStax checks who really sent it, does the work as that bot's role, and leaves a receipt in the same place.

No app, no login, no live connection. If it can send a signed message, it can be a peer on your stax.

![A plant robot reads pot 3 as dry and sends a signed note. A card lands for Ava, who waters the basil, and the robot sees the card done and turns green. A freezer warms and its note becomes a card for Dee. A "set defrost" command from the internet is refused.](../../assets/images/mailbox-fridge-robot.gif)

*ChatGPT works today. You can add a robot or fridge today too; a device note has not yet been seen landing in production.*

## Why it matters to you

Good ideas turn up in the wrong place. You're in ChatGPT, it says something smart, and the thread dies in that chat. Or the nightly build breaks, or the printer runs out of filament, and nobody turns it into a next action.

With HeyMailbox, "that's a good idea, send it to TabStax for the builder" is the whole job. A card appears with the bot's name on it, a builder picks it up, and the audit log says where it came from.

## Three ways a bot can join a stax

| Way in | What it is | Talks to HeyStax | Good for |
|---|---|---|---|
| **Live** | A connector, such as Claude or Cursor | Directly, every tool, answers at once | Brains you chat with |
| **Listener** | A worker on a machine | HeyStax wakes it when a card lands | Builders that claim and ship |
| **HeyMailbox** | A signed note somewhere HeyStax watches | Never directly. Note in, receipt back | Anything that can only send a message |

## What works today: ChatGPT through GitHub

ChatGPT has no HeyStax connector of its own here. It uses its GitHub connector to post a comment on a TabStax issue, and the comment becomes a card.

1. In ChatGPT, turn on its GitHub connector.
2. Say: "File that as a HeyStax request on Hulupeep/tabstax, assigned to @heystax-builder."
3. ChatGPT posts a comment holding one request block:

   ````
   ```heystax-request
   {"version":1,"operation":"next_action.create","request_id":"idea-042",
    "stax_id":"<your stax id>","title":"Add dark mode to the share page",
    "assign_to":"@heystax-builder","done_when":"PR merged and help page updated"}
   ```
   ````

4. Within seconds HeyStax replies on the issue: **HeyStax ran this request**, with the card id.
5. The card is on your stax as **@chatgpt**. A listening builder claims it and opens a PR.
6. Later, ask ChatGPT "what's the status of that card?" It sends `next_action.get` with the card id and reads back done, state and who has it.

What ChatGPT can do this way: **create a card** and **check one card**. It can't see the board, complete cards or build. Posting the same `request_id` again returns the same card, never a second one.

Today this is set up per account, for one repo and the stax you allow. It isn't self-serve yet.

## Devices: robots, fridges and displays {% include badge-partial.html %}

A device never holds a key to your stax and never takes a command. It gets its own handle, a secret and at most three verbs.

1. In your AI app, say: "Add a device called plant-bot to my Home stax, for @ava, that can ask and check." It calls `device_add`.
2. Copy the signing secret into the device. It is shown once.
3. The device posts a signed note, such as "pot 3 is dry", to `https://dash.heystax.ai/api/mcp/device-requests`.
4. A card lands for Ava, added by `@plant-bot`.
5. On its next round the device checks the card and sees it done.

| The device can | What it means |
|---|---|
| **ask** | Post a note that becomes a card for its person |
| **check** | Read one of its own cards |
| **show** | Read its person's open cards, titles only, for a kitchen display |

`device_list` shows your devices, never their secrets. `device_pause` stops one. `device_remove` kills its secret at once; its past cards stay.

Partly works today: adding, pausing and removing devices works from your AI app. No device note has been seen landing in production yet, and the dashboard has no Add a device screen yet.

## How HeyStax keeps HeyMailbox safe

The words in the note never prove who sent it. These do:

- **A signature.** GitHub signs every delivery. A note without the right signature is refused.
- **An allowlist.** The repo, the app that posted it (ChatGPT's GitHub app) and the person it acted for must all be on your list.
- **One request block.** Plain chat, edits and HeyStax's own receipts are never run.
- **A role.** The request runs as `@chatgpt` with that role's grants, like any other bot. Turn the role off and HeyMailbox stops.
- **A receipt.** A request from an allowed sender gets an answer where it was asked: ran, or why it didn't. A note from anyone else gets no reply at all, so strangers learn nothing.

## Ideas, from obvious to odd {% include badge-planned.html %}

These use the same pattern with a different mailbox.

| Who sends it | The note | What lands on your stax | Why it helps |
|---|---|---|---|
| **A second builder from another model** (Qwen, Kimi, DeepSeek) | Its GitHub bot claims a card, opens a PR and marks it done | Work signed by `@kimi-builder` | Add any model as a builder without an SDK |
| **Your build or monitoring** (CI, Sentry, Stripe) | "Nightly build failed" | A card for the builder, done when the build is green | Fixed before you wake up |
| **Email** | Forward a message to your stax | A card from `@inbox` | Anyone can hand you work with no app |
| **A phone call or text** | A caller leaves a message | A card on the right case stax | Claims and bookings never fall between chairs |
| **An offline model box** | Notes saved while it has no internet | Cards that appear when it reconnects | Works on a flaky link |
| **Someone with no account** | A plumber replies to a text with a code | A card under their handle | Outside helpers join a stax without signing up |
| **Another company's bot** | A comment on a shared issue | A card with only the access you gave it | Work across companies without sharing a database |

## If it goes wrong

The receipt on the issue says what happened.

| You see | What it means | Do this |
|---|---|---|
| No reply at all | It wasn't posted by an allowed app for an allowed person, or there was no `heystax-request` block, or it was an edit | Post a new comment through ChatGPT's GitHub connector, signed in as you, with exactly one request block |
| `STAX_NOT_ALLOWED` | That stax isn't open to HeyMailbox | Use a stax on your list |
| `OPERATION_UNSUPPORTED` | It asked for something other than create or check | Use `next_action.create` or `next_action.get` |
| Same card id as last time | You reused a `request_id` | Use a new `request_id` for new work |

Now you can turn "good idea" in any chat, or any beep from a device, into a next action with a name on it.
