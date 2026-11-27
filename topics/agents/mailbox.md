---
title: Let ChatGPT file cards through the Mailbox
parent: AI Integrations (MCP)
nav_order: 17
---

# Let ChatGPT file cards through the Mailbox

{% include badge-partial.html %}

**The Mailbox** is a way in for an AI that can't hold a HeyStax key. It posts a short request as a comment on a GitHub issue. HeyStax reads it, makes the card under that AI's own role, and answers in the same thread.

## Why it matters to you

You're in ChatGPT at 22:40 and it has a good idea. Before, you copied it, opened the board, pasted it and assigned it.

Now you say "send that to the builder". The card lands on your stax, marked **added by @chatgpt**, not you. The builder picks it up within seconds. You didn't paste your context. It travelled.

## What it can do today

- **Make a card**, with a title, a brief, an optional done-when and who it's for.
- **Check one card** by its id: done or not, its state, who has it. Nothing else comes back: no notes, no comments, no reports.

That's all. It can't list cards, finish them or change anything else.

## How it stays safe

- **The words prove nothing.** A request counts only if GitHub signed the delivery, it came from the allowed app, the allowed account, the allowed repo and the allowed stax.
- **It works as its own role.** `@chatgpt` has a role on the stax like any other worker. Revoke that role's key and the Mailbox stops.
- **Every answer is written down.** HeyStax replies with a receipt comment: what it did, as whom, and the card id. A refusal gets a receipt too, so you can check.
- **One request, one card.** Each request carries its own id. Send it twice and you get the same card back.

## How to do it

1. Ask us to open the Mailbox for your repo, the AI's GitHub app and your stax. Today this is set up for you, not self-serve.
2. On the stax, give the AI a role, such as `@chatgpt`, with work access.
3. In ChatGPT, turn on its GitHub connector.
4. Say: "File that as a HeyStax request on our mailbox issue, for @heystax-builder."
5. ChatGPT posts the request. Within seconds it can read the receipt and tell you the card id.
6. Later, ask: "What's the state of that card?"

Now you can hand an idea from ChatGPT straight to the right worker, and see that it landed.

<div class="hs-callout" markdown="1">
**Coming next** {% include badge-planned.html %}

Other senders will post to the Mailbox too: an email, a plain signed web post from a device, a Telegram message. A Mailbox worker will be able to ask for its cards, report and finish them. See [Robots, fridges and other teammates](../scenarios/robots-and-fridges).
</div>
