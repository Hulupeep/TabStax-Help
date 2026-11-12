---
title: Give your Chief its own key
parent: Set up your Chief of Staff
nav_order: 1
---

# Give your Chief its own key

{% include badge-partial.html %}

Your Chief needs a key in its own name: a role key, `@chief-of-staff`. Your own token stays with you.

## Why it matters to you

A bot on your token writes as you. Every card it adds says you added it. It can't message you either, because a message from you to you is dropped. With its own key, every write says `@chief-of-staff`, and you can check what it did in your name.

## Three keys

| Key | Starts with | Who holds it |
|---|---|---|
| Your token | `tabstax_` | You. From **Settings, MCP** at [dash.heystax.ai](https://dash.heystax.ai) |
| A role key | `tsk_live_` | The Chief's bot, in its secret store |
| A worker key | `tsw_live_` | One machine doing a role's work. See [Roles, workers and their keys](../agents/roles-workers-tokens.html) |

## Make the key

There is no button for this yet. You ask an AI app that is connected with your own token to do it for you.

1. Connect one AI app with your token. See [Connect to Claude Code](../mcp-claude-code.html), or use ChatGPT.
2. Paste this into it:

```text
Set up my HeyStax Chief of Staff.
1. If @chief-of-staff exists, call agent_token_issue(handle: "chief-of-staff").
   Otherwise call agent_register(name: "chief-of-staff").
2. Show me the tsk_live_ key once. Do not repeat it or save it anywhere.
```

3. Copy the key straight into the Chief's bot secret store. Grok Bot has a Secrets box for this.
4. Keep the key out of chats, notes and screenshots.

## Lost the key, or it leaked?

Run the same prompt again. `agent_token_issue` gives the Chief a new key and stops the old one at once, along with every worker key under it. The Chief keeps its handle, its grants and its history.

Now you can tell the Chief's work from yours at a glance.
