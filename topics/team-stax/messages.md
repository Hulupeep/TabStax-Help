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

Four teams, one pattern: ask on the card, answer from the phone, the work moves.

### A storm, 02:10

<iframe id="hs-scene-storm" src="{{ '/assets/anim/message-scenes.html' | relative_url }}?s=storm" title="Animation: a coordinator agent asks a crew lead about a fallen tree, he replies from the van, and the crew is sent" loading="lazy" style="width:100%;height:640px;border:0;display:block"></iframe>

`@storm-coordinator` asks Declan on the "Clear fallen tree, N71 at Bandon" card: "Can Cork crew 2 take this before 04:00?" He replies from the van: "Crew 2 yes, 03:15." The coordinator assigns the card and sends Aoife an FYI.

Hourly "still monitoring" notes go in as logs. Nobody wakes for those. At 07:00 the morning shift reads one card, not a night of group chat.

### The board pack, Thursday 17:00

<iframe id="hs-scene-board" src="{{ '/assets/anim/message-scenes.html' | relative_url }}?s=board" title="Animation: the Chief of Staff agent finds two revenue figures, asks the CFO, fixes the slide and tells the CEO and Head of Sales" loading="lazy" style="width:100%;height:640px;border:0;display:block"></iframe>

`@chief-of-staff` finds two Q3 revenue figures: 1.42m on the sales slide, 1.38m in the finance summary. It asks Tom, the CFO. He replies "1.38m". The Chief fixes the slide and tells Priya and Maeve on the same action. Maeve chased nobody.

### The import that needs one answer

<iframe id="hs-scene-build" src="{{ '/assets/anim/message-scenes.html' | relative_url }}?s=build" title="Animation: a coding agent asks Gaia which org a file is for, waits, then finishes the import and tells her it is fixed" loading="lazy" style="width:100%;height:640px;border:0;display:block"></iframe>

`@timebreez-builder` finds two orgs called "Dublin" and cannot tell which one an import file is for. It asks Gaia on the import action, then waits:

```text
next_actions_comment
  action_id: <the import action>
  to:        ["@gaia"]
  kind:      question
  content:   Which org is the stage-2 file for, Dublin North or Dublin City?
```

Gaia replies "Dublin City" in Telegram. The builder wakes, finishes the import, opens a pull request and sends her an `fyi`: "Fixed." It works the other way too: Gaia comments to `@timebreez-builder` from Claude, and it wakes with her message.

### A warehouse robot: bay 14 is blocked

<iframe id="hs-scene-robot" src="{{ '/assets/anim/message-scenes.html' | relative_url }}?s=robot" title="Animation: a robot worker of the picker role meets a blocked aisle, asks the floor lead, and reroutes by aisle 9 when she replies" loading="lazy" style="width:100%;height:640px;border:0;display:block"></iframe>

`robot-02`, a worker of the `@picker` role, meets a pallet in bay 14. Its controller asks Niamh on the card: "Wait, or go round by aisle 9?" She replies "Aisle 9" and it reroutes. HeyStax never drives motors. The controller reads the card and reports back.

Niamh writes to `@picker`, the job, not to the machine. Swap the robot next year and nothing changes for her.

<script>addEventListener('message',function(e){if(e.data&&e.data.hsSceneHeight&&e.data.scene){var f=document.getElementById('hs-scene-'+e.data.scene);if(f)f.style.height=(e.data.hsSceneHeight+4)+'px';}});</script>

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
