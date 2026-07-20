---
title: Telegram
parent: Team Stax
nav_order: 2
---

# Use HeyStax in Telegram

Use the production bot **[@heystax_bot](https://t.me/heystax_bot)** to add and update Next Actions without leaving Telegram. Do not use `@heystax_test_bot`; that account is reserved for automated testing.

There are two separate connections:

1. A group administrator connects one Telegram group to one Stax.
2. Every collaborator links their own Telegram identity to their own HeyStax account.

Connecting the group does not authenticate its members. Linking one member does not authenticate anyone else.

## Before you start

For group commands to work, all of these must be true:

- `@heystax_bot` is a member of the Telegram group.
- The group is connected to the intended Stax.
- The person sending the command has linked their own Telegram account.
- That person is a current owner or editor of the connected Stax.

For example, the **Claim Cowboys** Telegram group should be connected once to the **claim** Stax. Each editor in Claim Cowboys then links their own Telegram account; they do not reconnect the group.

## Group administrator: connect a group once

An owner or editor can connect the group.

1. Sign in at [dash.heystax.ai](https://dash.heystax.ai) with your own HeyStax account.
2. Open the Stax that the Telegram group should use. For Claim Cowboys, open **claim**.
3. Open **Project Settings**, then find **Telegram**.
4. If your account is not linked, select **Link account**, then **Continue in Telegram**. Complete the `/start` message with `@heystax_bot` within 15 minutes.
5. Return to the same Stax's Project Settings and select **Add group**.
6. Continue to Telegram and select the target group when Telegram asks where to add the bot. For this example, select **Claim Cowboys**.
7. Wait for the message `Group connected to HeyStax - claim Stax.`
8. Return to Project Settings and confirm that the group is listed in the Telegram section.

Do not select a separate DM default to connect a group. The group is connected to the Stax that was open when **Add group** was selected.

## Collaborator: link your own Telegram account

Every collaborator completes these steps once. They must use their own HeyStax and Telegram accounts.

1. Confirm that you are already an owner or editor of the shared Stax.
2. Sign in to your own account at [dash.heystax.ai](https://dash.heystax.ai).
3. Open the shared Stax, such as **claim**.
4. Open **Project Settings**, then find **Telegram**.
5. Select **Link account**, then **Continue in Telegram**.
6. Send the prepared `/start` message to `@heystax_bot` within 15 minutes.
7. Wait for `Telegram is linked to this Stax.`
8. Return to the Telegram group you already belong to and try a group command.

Do not select **Add group** when the group is already connected. Do not use another collaborator's link: account links are short-lived, single-use, and tied to the HeyStax user who created them.

## Commands in a Telegram group

### Add a Next Action

Mention the bot followed by the action:

```text
@heystax_bot working on draft presentation
```

The bot replies:

```text
<Your first name> Next Action: working on draft presentation
```

The action appears in the connected Stax under the sender's column. In Claim Cowboys, it appears in **claim**, not in the sender's DM default Stax.

Messages that do not mention `@heystax_bot` are ignored. Editing a Telegram message after the bot has processed it does not edit the HeyStax action; use the reply command below.

### See your status privately

In the group, send either:

```text
@heystax_bot status
```

```text
@heystax_bot what's up
```

The group receives `I sent your status by DM.` The bot sends your five most recently updated open actions and your current goal to your private chat. It does not post your action details in the group.

You must have started a private chat with `@heystax_bot` for Telegram to deliver the DM.

## Commands in your private bot chat

This means a one-to-one Telegram conversation with the HeyStax bot, not a message in Claim Cowboys or another group.

1. In Telegram, search for `@heystax_bot` or open [t.me/heystax_bot](https://t.me/heystax_bot).
2. Check that the chat header shows **Heystax** and the username `@heystax_bot`.
3. Open that contact and send the command directly to the bot.

The private chat uses your **DM default Stax**. It does not use the Stax connected to Claim Cowboys or any other Telegram group. Use `/stax` in the private chat to see or change that default.

### Example: Bob adds a private action

Bob opens his one-to-one chat with **Heystax (@heystax_bot)** and sends:

```text
/stax
```

HeyStax shows Bob the writable Stax he can choose from. Bob selects **Personal Admin**. He then sends this plain message in the same private bot chat:

```text
renew passport
```

HeyStax replies `Added to your default Stax.` The action `renew passport` appears under Bob in **Personal Admin**.

If Bob instead writes `@heystax_bot renew passport` in the **Claim Cowboys** group, the action appears under Bob in the group-connected **claim** Stax. The group's connected Stax always wins inside that group; Bob's private DM default does not change it.

### Example: Bob checks his private status

In the one-to-one **Heystax (@heystax_bot)** chat, Bob sends:

```text
/status
```

HeyStax returns up to five of Bob's recently updated open actions and his current goal from his DM default Stax. This response is visible only to Bob.

| What you want to do | What to send | Result |
|---|---|---|
| Add an action | Any plain text, for example `prepare client update` | Adds it to your current DM default Stax |
| See personal status | `/status`, `status`, `what's up`, or `whats up` | Shows up to five recent open actions and your current goal |
| Change the DM default | `/stax` | Shows the writable Stax you can choose from |

`/start <link-token>` is generated by **Link account** in Project Settings. It links your identity; it is not a general-purpose command to type manually. A bare `/start` or `/help` does not replace the setup steps on this page.

## Update a group action by replying to HeyStax

These commands are replies to a specific action confirmation posted by **Heystax (@heystax_bot)** in the Telegram group. They are not standalone group commands.

### Example: Bob marks the correct action done

Bob sends this in Claim Cowboys:

```text
@heystax_bot draft the client update
```

HeyStax replies to the group:

```text
Bob Next Action: draft the client update
```

To complete that exact action, Bob uses Telegram's **Reply** function on the `Bob Next Action: draft the client update` message:

1. On a phone, press and hold the HeyStax message and select **Reply**. On desktop, right-click it and select **Reply**.
2. Check that Telegram shows the HeyStax message quoted above the message box.
3. Type `done` and send it.

The conversation should look like this:

```text
Replying to Heystax:
Bob Next Action: draft the client update

Bob: done
```

HeyStax replies `Action updated.` and the action moves from **Open** to **Done** in the `claim` Stax.

If Bob sends `done` as a new standalone message, HeyStax cannot know which action he means, so nothing changes. If he replies to the wrong HeyStax confirmation, that other confirmation identifies a different action. Always check the quoted action before sending the reply.

The same reply pattern applies to every action update:

| Reply exactly | Result |
|---|---|
| `done` | Marks the action done |
| `reopen` | Reopens a done action |
| `edit <new action text>` | Replaces the action text |
| `block <reason>` | Adds `Blocked: <reason>` as a comment on the action |
| `delete` | Asks for deletion confirmation |

After `delete`, select **Confirm delete** within 15 minutes. The person who requested deletion must confirm it.

For safety, these replies work only for the person who created the action or the Stax owner. For example, Alice cannot mark Bob's action done by replying to Bob's confirmation unless Alice owns the Stax. Other editors can add and update their own actions.

## Run a group standup

Standups operate only in a connected group. Each participant must be linked and remain an owner or editor of the Stax.

| Command | Result |
|---|---|
| `/join` | Adds you to the group's standup roster |
| `/leave` | Removes you from the standup roster |
| `/sup` | Starts one standup for the enrolled roster |
| `@heystax_bot sup` | Also starts the standup |

Reply directly to the active standup prompt using this exact two-line format:

```text
Next: prepare the client presentation
Blocked: waiting for final figures
```

Use `Blocked: none` when there is no blocker. A valid response creates the `Next:` text as your Next Action in the connected Stax. A blocker is attached to that action. If you submit another response to the same active standup, the bot asks whether to replace your existing response.

When the standup closes, the group receives a summary showing who responded and who is missing.

### Example 1: Bob starts a standup and everyone responds

Bob, Alice, and Nancy are editors of the **claim** Stax and members of **Claim Cowboys**. Each person links their own Telegram account first. They then join the standup roster by sending this in Claim Cowboys:

```text
/join
```

Each person receives `You are in the standup roster.` Bob starts the standup:

```text
/sup
```

HeyStax posts:

```text
Standup roster: Bob, Alice, Nancy
Reply exactly:
Next: <what you are doing>
Blocked: <blocker or none>
```

Bob replies directly to that prompt:

```text
Next: finish the claim summary
Blocked: none
```

Alice replies:

```text
Next: confirm the policy dates
Blocked: waiting for the insurer
```

Nancy replies:

```text
Next: prepare the client presentation
Blocked: none
```

HeyStax replies `Standup response recorded.` to each valid response. In the **claim** Stax:

- Bob gets the open action `finish the claim summary`.
- Alice gets the open action `confirm the policy dates`, with the comment `Blocked: waiting for the insurer`.
- Nancy gets the open action `prepare the client presentation`.

### Example 2: Alice corrects her response

Alice notices that her Next Action was wrong. She replies to the same active standup prompt with:

```text
Next: call the insurer for the policy dates
Blocked: waiting for the insurer
```

HeyStax asks `Replace your existing standup response?` Alice selects **Replace** within 15 minutes. Her original standup action is replaced by the corrected response; HeyStax does not create two active standup responses for Alice.

### Example 3: Nancy does not respond

Suppose Bob and Alice respond, but Nancy does not reply before the 24-hour standup closes. HeyStax posts a summary like:

```text
Standup closed. Responded: Bob, Alice. Missing: Nancy.
```

Bob's and Alice's responses still create their actions. Nancy is named as missing and no standup action is created for her. Nancy remains enrolled for the next standup unless she sends `/leave`.

## What appears in HeyStax

- A group action is stored only in the Stax connected to that group.
- A private action is stored in the DM default selected with `/stax`.
- The action belongs to and is assigned to the Telegram sender's linked HeyStax user.
- Open actions appear under that person's column in the Stax **Open** view.
- An action disappears from **Open** after `done`; find it in the **Done** view.

## Troubleshooting

### “This group or sender is not authorized for HeyStax actions”

Check all four requirements: the production bot is in the group, the group is connected to the correct Stax, the sender linked their own Telegram account, and the sender still has owner or editor access to that Stax.

### The group was already connected

Do not select **Add group** again. Each remaining collaborator should follow **Collaborator: link your own Telegram account** above.

### The link is invalid or expired

Return to the intended Stax's Project Settings and create a new **Link account** link. Open it with the same Telegram account within 15 minutes. Do not reuse a link that already succeeded.

### The wrong bot opens

The chat header must show **Heystax** and `@heystax_bot`. Remove `@heystax_test_bot` from working groups.

### A group message did not create an action

Make sure the message contains the exact mention `@heystax_bot`, followed by non-empty action text. Check the bot's reply. If the action was marked done, look in the Stax **Done** view. Telegram edits made after creation are not synchronized.

### A reply command did nothing

Reply to the bot's confirmation for the exact action. Use the command formats shown above. Only the action creator or Stax owner can mutate it through Telegram.

### Status did not arrive by DM

Open a private chat with `@heystax_bot` and select **Start**, then retry `@heystax_bot status` in the group. Telegram bots cannot initiate a private conversation before the user starts it.

### A collaborator left the Stax

Removing or deactivating their Stax access prevents future group commands even if they remain in the Telegram group. Their Telegram identity does not grant access by itself.
