---
title: Telegram
parent: Team Stax
nav_order: 2
---

# Run your stax from Telegram

The HeyStax Telegram bot (`@heystax_bot`) turns a line in a chat into a Next Action in your stax. Add work, hand it to someone, tick it off, and see who is on the stax, without leaving Telegram.

## Why it matters to you

Bob is in a van between jobs. He types `/t ! call the insurer` in the team group. It lands in the **claim** stax as an urgent action under his name. Alice sees it on the dashboard before he reaches the next site.

Nobody pasted anything. The work was already in the stax, and it travelled to the chat.

{% capture s %}
{% include anim/node.html x=95 y=48 label="Claim Cowboys" sub="Telegram group" kind="surface" w=150 d=0.2 %}
{% include anim/node.html x=385 y=48 label="Dashboard" sub="Alice assigns" kind="surface" w=140 d=0.4 %}
{% include anim/plane.html x=20 y=118 w=440 h=92 label="claim stax" d=0.6 %}
{% include anim/edge.html x1=95 y1=74 x2=120 y2=155 kind="write" d=1.0 %}
{% include anim/node.html x=125 y=172 label="Bob: call the insurer" kind="action" w=180 h=34 d=1.4 %}
{% include anim/edge.html x1=385 y1=74 x2=355 y2=155 kind="write" d=1.8 %}
{% include anim/node.html x=355 y=172 label="Bob: check invoice" kind="action" w=170 h=34 d=2.2 %}
{% include anim/edge.html x1=355 y1=189 x2=330 y2=245 kind="dispatch" d=2.6 %}
{% include anim/node.html x=250 y=262 label="@bob, Alice assigned you" kind="note" w=220 h=34 d=3.0 %}
{% include anim/edge.html x1=140 y1=262 x2=40 y2=74 cx=20 cy=262 kind="dispatch" d=3.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A Telegram group writes actions into the claim stax, and assignments made on the dashboard come back to the group as notices" caption="Bob adds an action from the Claim Cowboys group and it lands in the claim stax under his name. Alice assigns Bob a second action on the dashboard. The bot posts the assignment back to the group, and Bob replies /done to it when it is finished." svg=s %}

## Set it up once

You need the bot in the group, the group connected to one stax, and every person linked to their own HeyStax account.

**Connect the group** (an owner or editor, once):

1. Open the stax at [dash.heystax.ai](https://dash.heystax.ai), then **Project Settings**, then **Telegram**.
2. Select **Add group** and pick the group in Telegram.
3. Wait for `Group connected to HeyStax - claim Stax.`

**Link yourself** (every person, once):

1. Open the same stax's **Project Settings**, then **Telegram**.
2. Select **Link account**, then **Continue in Telegram**.
3. Send the prepared `/start` message to `@heystax_bot` within 15 minutes.
4. Wait for `Telegram is linked to this Stax.`

Each link is single-use and tied to the person who made it. Never use someone else's.

## Everything works on one stax

In a group, that is the stax the group is connected to. In your private chat with the bot, it is your current stax. Send `/stax` to see it or switch.

## Add work

| Send | What happens |
|---|---|
| `send the draft` (private chat) | Adds it to your current stax |
| `/t send the draft` (group) | Adds it to the group's stax under your name. `@heystax_bot send the draft` also works. |
| `/t ! call the bank` | Adds it as urgent. A leading `!` or `urgent` does this. |
| `/t @alice check the invoice` | Assigns it to Alice. Use any handle on the stax, person or agent. |
| Reply `/t @timebreez-builder` to a bug or screenshot | Hands the bug to an agent with your words and the picture. You hear back with its verdict. See [Hand a bug to an agent](hand-a-bug-to-an-agent). |

## Change a task

Reply to the bot's message about that task. On a phone, swipe left on it or tap **Reply**. Then send:

| Reply | Result |
|---|---|
| `/done` | Marks it done |
| `/reopen` | Undoes done |
| `/edit new wording` | Changes the text |
| `/block waiting on Sam` | Says why it is stuck, as a comment |
| `/delete` | Removes it after you confirm, within 15 minutes |

Plain words without the slash work too. A `done` sent on its own, not as a reply, changes nothing. The bot cannot tell which task you mean.

Who can change what:

| Person | Can do |
|---|---|
| The person who made it, or the stax owner | Everything |
| The person it is assigned to | done, reopen, block |
| Any other editor of the stax | done, reopen, block, edit |

## See your work and your team

| Send | What you get |
|---|---|
| `/status` | Your open tasks in this stax, the ones you made and the ones assigned to you, newest first. Your goal and up to three tasks done this week. In a group, it comes to you by DM. |
| Reply `/done 1,3` to a status list | Ticks off tasks 1 and 3 and sends the list back with them crossed out |
| `/who` | Everyone on the stax, people and agents, with the handle to use, their title and what they are accountable for |
| `/morning off` | Stops the 8am list. `/morning on` starts it again. |
| `/help` | The full command list |

## You hear back

- When someone assigns you a task anywhere, on the dashboard, in Telegram or from an AI app, the bot posts it to the stax's group. With no group, it comes by DM. Reply `/done` to that notice when you finish.
- When someone else finishes a task you assigned, you get a notice. When an agent finished it, the notice ends with its result.
- When an agent picks up a task you made in Telegram, the group sees `picked up`.
- When an agent asks you a question on a task, it comes by DM. See [Bots ask you questions](messages).
- An old notice tidies itself. Once the task is done, moved or removed, the bot strikes it through and adds one line: **✓ Done by @builder**, **→ Now with Colm** or **✕ Card removed**.
- A message that names a PR or an issue gets an **Open PR** button, so you never hunt for the link.
- An agent's result leads with one bold line of state, then what you need to do. When nothing needs you, it is one quiet line.
- Money amounts are never posted to a group. An archived stax sends nothing.

## Run a standup

In a connected group, `/join` puts you on the roster and `/leave` takes you off. `/sup` starts a standup. Each person replies to the prompt in two lines:

```text
Next: confirm the policy dates
Blocked: waiting for the insurer
```

Use `Blocked: none` when nothing is in the way. The `Next:` line becomes your action, and the blocker is attached to it. After 24 hours the group gets a summary of who answered and who is missing.

## When it does not work

| You see | Do this |
|---|---|
| "This group or sender is not authorized for HeyStax actions" | Check that the bot is in the group, the group is connected to the right stax, you linked your own account, and you are still an owner or editor. |
| A link is invalid or expired | Make a new **Link account** link and use it within 15 minutes. |
| The wrong bot answers | The chat header must say **Heystax** and `@heystax_bot`. Remove `@heystax_test_bot` from working groups. |
| A reply did nothing | Reply to the bot's message for that exact task. Messages from before 10 November 2026 in private chats cannot be replied to. |
| Your status did not arrive | Open a private chat with `@heystax_bot`, press **Start**, then try again. A bot cannot start a private chat on its own. |
| A Telegram edit did not change the task | Edits are not synced. Reply `/edit new wording` instead. |

Removing someone from the stax stops their commands, even if they stay in the group.

Now you can add, hand off and finish work from a phone, and the stax stays the one record.
