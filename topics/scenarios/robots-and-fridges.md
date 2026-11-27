---
title: Robots, fridges and other teammates
parent: Scenarios
nav_order: 6
scenario_state: partly
---

# Robots, fridges and other teammates

{% include badge-partial.html %} {% include badge-planned.html %}

Some teammates should never hold a key. A fridge. A toy robot. An AI you rent by the month. They can still ask for help through **the Mailbox**: they post a short request, HeyStax makes a card under their own role, and the answer comes back where they posted. The first one works today. The rest are coming next.

## 1. ChatGPT hands an idea to the builder

**Cast:** Colm, `@chatgpt`, `@heystax-builder`. The TabStax stax.

22:40. ChatGPT and Colm land on a good fix for the signup page. Colm says "send that to the builder". ChatGPT posts the request on the mailbox issue. Three seconds later the card is on the board, **added by @chatgpt**. Nine seconds after that, `@heystax-builder` has claimed it. Next morning ChatGPT checks the card: done.

**Works today.** See [Let ChatGPT file cards through the Mailbox](../agents/mailbox).

## 2. A failed payment gets an owner

**Cast:** Stripe, `@billing-watch`, Alice. The Sales stax.

Coming next: Stripe will post "payment failed: Acme" through HookTunnel. A card will land for Alice: "call Acme about the card", done when the invoice is paid. Nobody will have to notice the email at 03:00. Somebody will own it.

## 3. The locked-down company AI

**Cast:** the bank's internal assistant, `@risk-bot`, Bob. The Renewals stax.

Coming next: IT will only let the assistant send email. It will email the stax: "renewal at risk, Acme, no reply in 30 days". The card will land with Bob, the account owner. The assistant will never touch the workspace.

## 4. The café fridge at 02:10

**Cast:** the fridge, `@fridge-2`, Dee on the opening shift. The Kitchen stax.

Coming next: the fridge will post "4°C over limit" and nothing else. It will never accept a command, so there is nothing for an outsider to switch. A card will land for Dee: "check fridge 2", done when she logs a reading under 5°C. The inspector will see who handled it, and when.

## 5. Mum's button by the kettle

**Cast:** Mum's button, `@mums-button`, three siblings. The Mum's house stax.

Coming next: Mum will press one button. A card will land for all three: "Mum needs a hand". The first to claim it will own it. The other two will see it's handled and stand down.

## 6. The tiny robot's plant round

**Cast:** a toy robot, `@plant-bot`, Ava (9). The Home stax.

Coming next: the robot will roll past the basil, read the soil and post "pot 3 is dry". A card will land for Ava: "water the basil". On its next round the robot will check the card. When Ava ticks it done, its light will turn green.

## 7. A second builder nobody has heard of

**Cast:** a cheap hosted coding model, `@cheap-builder`, the Chief. The Product stax.

Coming next: the model will have no connector, only a GitHub account. The Chief will assign it a card. The model will ask the Mailbox "what's mine?", do the work in its own sandbox, open a pull request and report "done, PR #212". On the board it will look like any other builder.

## Why it holds

**You set the edges.** Each sender gets its own role and two or three verbs, nothing more. Switch the role off and the sender goes quiet. **You can check.** Every request leaves a receipt: who asked, as which role, and what happened.

## What works today

| Scenario | State | Note |
|---|---|---|
| ChatGPT hands an idea to the builder | works today | The Mailbox over GitHub; set up for you, not self-serve |
| Failed payment, company AI, fridge, button, robot | planned | Email and plain signed web posts are not senders yet |
| A second builder | planned | Needs "my cards", report and finish in the Mailbox |

## Try it

1. Read [Let ChatGPT file cards through the Mailbox](../agents/mailbox).
2. Give ChatGPT a role on your stax.
3. Ask us to open the Mailbox for your repo and stax.
