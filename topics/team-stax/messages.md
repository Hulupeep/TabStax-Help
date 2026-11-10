---
title: Bots ask you questions
parent: Team Stax
nav_order: 3
---

# Let your bots ask you questions

A bot gets stuck at 16:00. It needs one fact from Gaia. Before, that question sat in a log nobody read, and the card waited until morning.

Now the bot comments on the action, addressed to `@gaia`. Gaia gets a DM from the HeyStax Telegram bot. She replies in plain words, and the answer lands back on the same action, addressed to the bot.

## Why it matters to you

The question lives on the work it is about, not in one chat app. Anyone on the stax can read it later. Every message says who wrote it and who it was for, so you can check what each bot said in your name.

## How it works

1. A bot (or you, from Claude) calls `next_actions_comment` on an action and puts handles in `to`, such as `["@gaia"]`.
2. It marks the message as a `question` or an `fyi`, such as "That's fixed, PR is merged".
3. Each addressed person who has linked Telegram gets a DM: who is asking, the message, and the task it is about.
4. They reply to that DM with plain text. The reply becomes a comment on the same action, addressed back to whoever asked. The bot confirms who it went to.
5. The bot reads answers with `comments_for_me`, or calls `wait_for_work` with `comments_since` to wake the moment an answer lands.

## Watch it work

<iframe id="hs-msg-anim" src="{{ '/assets/anim/bot-messages.html' | relative_url }}" title="Animation: a bot asks Gaia a question on an action, she replies in Telegram, and the bot wakes with the answer" loading="lazy" style="width:100%;height:700px;border:0;display:block"></iframe>
<script>addEventListener('message',function(e){if(e.data&&e.data.hsMsgHeight){var f=document.getElementById('hs-msg-anim');if(f)f.style.height=(e.data.hsMsgHeight+4)+'px';}});</script>

*Six short scenes. A bot asks Gaia a question by commenting on the action, addressed to her. The HeyStax Telegram bot DMs her. She replies in plain words, the reply lands on the same action for the bot, and a bot waiting for work wakes with it. A bot can also just tell you "that's fixed". Progress notes ping nobody. Only people and agents on the stax can be reached. And you can ask a bot a question the same way.*

## The rules

| Rule | What happens |
|---|---|
| Nobody in `to` | A silent note on the action. Nobody is pinged. |
| `next_actions_log` | A progress note. It notifies nobody. |
| Someone not on the stax | Refused. The bot is told the handle is not on the stax. |
| More than 10 handles | Refused. |
| Your own handle | Dropped. You never ping yourself. |
| Money in the message | Masked in the DM. The full text stays on the action. |

## Before you start

- The person must be on the stax: its owner, an editor or a viewer.
- To get DMs, they link Telegram once. See [Telegram](telegram.html).
- A bot needs a key with work access on that stax. See [Roles, workers and their keys](../agents/roles-workers-tokens.html).

## For whoever writes the bot's brief

Add one line: "When you need a person, comment on the action with their handle in `to`. Do not just log it."

Now you can let a bot ask the right person the right question, and get the answer back on the work itself.
