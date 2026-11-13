---
title: Connect a bot by sign-in
parent: AI Integrations (MCP)
nav_order: 8
---

# Connect a bot by sign-in

Add HeyStax as a connector in your AI app, sign in, and pick the role the bot works as. You never see a key.

## Why it matters to you

Ann wants a BD bot on her product stax. She used to copy a key into a settings box and hope she pasted it right. Now she signs in, picks "a new role: bd", and the bot says hello as `@bd`. It works as that role, not as her, so everything it writes is marked as the bot's.

## Connect it

1. In your AI app, add a connector with the address `https://dash.heystax.ai/api/mcp`.
2. Your app opens HeyStax. Sign in.
3. Under **will work as**, pick one of your roles, or make a new one on one of your stax. No stax yet? Name your first one there.
4. Check the line that says where the sign-in goes back to. If HeyStax could not verify the app, it says so. Only continue if you started this from an app you trust.
5. Click **Connect**. You are back in your app.
6. Say "check HeyStax". The bot writes its job first, then takes its first card.

## What the bot can do

The bot gets the role's access and nothing more. It sees only the tools that role may use. It cannot act as you, change your plan, or make keys.

Connect the same app to the same role again and you get the same bot back, not a second one.

## Disconnect it

Open [dash.heystax.ai/mcp/connect](https://dash.heystax.ai/mcp/connect). Under **Bots connected by sign-in**, click **Disconnect**. The bot's next call is refused.

## If it goes wrong

| You see | Do this |
|---|---|
| "Connecting a bot needs HeyStax Pro or a trial" | Start a trial, then connect again |
| "That role name is taken" | Use the suggested name, already filled in |
| "This stax already has 10 roles" | Pick one of the roles listed, or another stax |
| "HeyStax could not verify this app" | Stop unless you started this from that app yourself |

Prefer a key? [Connect with your token](../mcp-claude-code) still works.

Now you can hire a bot for a role in about a minute, and take it back with one click.
