---
title: Connect it to your bot
parent: Set up your Chief of Staff
nav_order: 3
---

# Connect your Chief to its bot

Your Chief is a role. A bot does the work: Grok Bot, ChatGPT, Claude Code or Codex. The bot talks to HeyStax at `https://dash.heystax.ai/api/mcp` and sends a key with every call.

## Why it matters to you

Swap the bot and the Chief stays. Its handle, grants and history belong to the role, not to the bot. You can move it from Grok Bot to Claude Code next month and lose nothing.

## Two connectors, one for reading and one for writing

A role key only sees the stax you granted it. A Chief that looks across all your stax needs to read more than that. So most Chiefs use two connectors:

| Connector | Key | Used for |
|---|---|---|
| HeyStax (owner) | Your token | Reading across all your stax |
| HeyStax (Chief) | The `@chief-of-staff` key | Every write and every message |

Keep one connector on your token for reading, and give every write a second connector that uses the Chief's key. The brief tells the bot which is which.

## Grok Bot

1. In the Chief's chat, ask it to add an MCP server named **HeyStax (Chief)** at `https://dash.heystax.ai/api/mcp`.
2. Its header is `Authorization: Bearer` followed by the secret that holds the Chief's key.
3. Ask it to list its tools. You should see `next_actions_comment` and `role_create`.
4. Ask `agent_whoami` on the Chief connector. It should answer `chief-of-staff`.

## ChatGPT

Add a connector with the same address and the Chief's key as the token. One connector is enough if the Chief runs only the stax you granted.

## Claude Code or Codex {% include badge-partial.html %}

In the folder the Chief works from, run `heystax connect` and paste the Chief's key. Choose the stax. The folder becomes a worker of `@chief-of-staff`. See [Roles, workers and their keys](../agents/roles-workers-tokens.html).

## If it goes wrong

| You see | Do this |
|---|---|
| Cards say you made them | The bot wrote with your token. Point writes at the Chief connector |
| `TOKEN_INVALID` on the Chief connector | The key was replaced. Paste the new one into the secret |
| `Stax not found` | The Chief has no grant on that stax. See [Let it work on your stax](stax-access.html) |
| No new tools | Remove and re-add the connector so it reads the tool list again |

Now you can change bots without changing who your Chief is.
