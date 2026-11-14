---
title: Wake a brain when work lands
parent: AI Integrations (MCP)
nav_order: 16
---

# Wake a brain when work lands

{% include badge-partial.html %}

HeyStax can call a bot the moment something changes on its stax. You give the bot's role a **wake address**. HeyStax posts a short, signed note to it. The bot wakes, reads the board itself, and acts.

## Why it matters to you

Your Chief checks the board every two hours. A worker blocks at 10:05 with a question. Nobody sees it until 12:00, and the card sits.

With a wake address, the Chief hears about it at 10:05. The two-hour check stays, but only as a safety net.

## What HeyStax sends

- **When:** work is assigned to the role. A Chief also wakes when a worker's run ends, a claim is stuck, a check fails, a queue empties, or a role has no one home.
- **What:** ids only. Which event, which stax, which card. Never the card's text. The bot reads that through its own key, so a leaked wake gives nothing away.
- **How:** a POST, signed with a secret only that launcher holds. HeyStax retries after 1, 5 and 30 minutes if the address does not answer.
- **Limits:** pause the launcher and it stops. Cap its runs per hour and HeyStax holds the rest. A Chief is never woken by its own moves.
- **Proof:** ask your AI app for `push_deliveries_list`. Every wake, its answer and its retries are there.

## How to do it with Grok Bot

Grok Bot routines can start from a webhook. That routine URL wants its own sender key. HeyStax signs with its own secret instead, so a relay sits in the middle: HookTunnel takes the HeyStax wake and passes it on with the routine's key, and keeps a log of each one.

1. In Grok Bot, open the role's webhook routine and copy its **webhook URL** and **sender key**.
2. In HookTunnel, make a hook that forwards to that URL with that key. Keep the key in HookTunnel, never in a chat or a card.
3. Ask the bot to call `launcher_register` with kind `hosted`, a label, and the HookTunnel hook URL as `push_url`. It gets a signing secret back once. Store it in the hook.
4. Give the routine one rule: "on every wake, ignore the body, call `agent_events_list` and `comments_for_me`, read the cards, then act."
5. Keep a slow routine, every two hours, that does the same. That catches anything a wake missed.
6. For GitHub, add a repo webhook (pull request, checks, merged) that points at another hook to the same routine.

## Other brains

| Brain | Wake it with | Works today |
|---|---|---|
| Claude Code or Codex on your machine | `heystax listen`: it waits on HeyStax and starts within a minute | Yes, comments included |
| Hermes, or any bot with an HTTPS address | Its own URL as `push_url`; check `X-HeyStax-Signature` | Yes |
| A bot whose webhook needs its own key | HookTunnel in the middle, as above | Yes |
| A chat with no routine | Only when you open the chat | No wake |

To check a signature: compute HMAC SHA-256 of `timestamp.body` with the launcher's secret, where the timestamp is the `X-HeyStax-Timestamp` header. Compare it with the hex after `sha256=`.

The brain is swappable. Move the role from Grok Bot to Hermes and you change one address. The role, its key, its cards and its history stay put.

## Coming next

{% include badge-planned.html %}

A comment wakes the role it is addressed to by push. Today a listening worker already wakes on comments, but a webhook brain only hears about a comment on its next check.

Now you can let a bot act on a blocked card in minutes, not hours, and still see every wake it got.

**Read next:** [Put an outside brain on a stax](outside-brain) · [Connect a worker to a role](connect-a-worker)
