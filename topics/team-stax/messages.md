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

## Scenarios

### An emergency team: a storm, 02:10

The **Storm response** stax has Aoife (incident lead), Declan (crew lead, Cork depot) and an agent role `@storm-coordinator` that keeps the action list moving overnight.

1. A card reads "Clear fallen tree, N71 at Bandon". The coordinator needs to know if a crew can go now.
2. It comments on that card, to `@declan`, as a question: "Can Cork crew 2 take this before 04:00, or do we hand it to Clonakilty?"
3. Declan's phone buzzes with a Telegram DM. He replies from the van: "Crew 2 yes, 03:15."
4. His answer lands on the card, addressed to the coordinator. It wakes, assigns the card and sends Aoife an FYI: "N71 Bandon: Cork crew 2, ETA 03:15."
5. Every hourly "still monitoring" note goes in as a log. Nobody wakes for those.

At 07:00 the morning shift reads one card and sees the question, the answer and who decided. Nobody has to scroll back through a night of group chat.

### An executive team: the board pack, Thursday 17:00

The **Q4 board pack** stax has Maeve (CEO), Tom (CFO), Priya (Head of Sales) and `@chief-of-staff`, a role that assembles the pack.

1. The Chief finds that the revenue figure on the sales slide and the one in the finance summary differ.
2. On the action "Finance summary", it asks `@tom`: "Sales slide says 1.42m for Q3, finance summary says 1.38m. Which is the board number?"
3. Tom replies in Telegram: "1.38m. Sales is counting a deal that signed on 2 October."
4. The Chief fixes the slide, then sends an FYI to `@priya` and `@maeve` on the same action: "Q3 revenue set to 1.38m. The October deal moves to Q4."
5. Maeve didn't chase anyone. She gets one message, and the reason sits on the action if a board member asks.

### Building software: the import that needs one answer

The **Timebreez** stax has Gaia (business analyst), Colm (owner) and `@timebreez-builder`, a coding agent working on a machine of yours.

1. The builder is fixing the stage-2 opening-balance import. It finds two orgs called "Dublin" and can't tell which one the file is for.
2. It asks Gaia on the import action:

   ```text
   next_actions_comment
     action_id: <the import action>
     to:        ["@gaia"]
     kind:      question
     content:   Which org is the stage-2 file for, Dublin North or Dublin City?
   ```

3. It goes back to waiting, with `wait_for_work` and `comments_since` set to the time it asked.
4. Gaia replies "Dublin City" in Telegram. The builder wakes, finishes the import and opens a pull request.
5. It tells her, with no answer needed:

   ```text
   next_actions_comment
     action_id: <the import action>
     to:        ["@gaia"]
     kind:      fyi
     content:   Fixed. Re-run stage 2 when you're ready.
   ```

6. Gaia can go the other way too. In Claude, with her own token, she comments on a bug card to `@timebreez-builder`: "Still failing for the Galway org. Screenshot is on the card." The builder wakes with it.

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
