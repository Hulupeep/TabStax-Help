---
title: Robots, fridges and other teammates
parent: Scenarios
nav_order: 6
scenario_state: partly
---

# Robots, fridges and other teammates

{% include badge-partial.html %} {% include badge-planned.html %}

Some teammates should never hold a key. A fridge. A toy robot. An AI you rent by the month. They can still ask for help through **HeyMailbox**: they post a short request, HeyStax makes a card under their own role, and the answer comes back where they posted. The first one works today. The fridge and the robot partly work. The rest are coming next.

## 1. ChatGPT hands an idea to the builder

**Cast:** Colm, `@chatgpt`, `@heystax-builder`. The TabStax stax.

22:40. ChatGPT and Colm land on a good fix for the signup page. Colm says "send that to the builder". ChatGPT posts the request on the mailbox issue. Three seconds later the card is on the board, **added by @chatgpt**. Nine seconds after that, `@heystax-builder` has claimed it. Next morning ChatGPT checks the card: done.

**Works today.** See [Add robots, fridges and other bots with HeyMailbox](../agents/mailbox).

## 2. A failed payment gets an owner

**Cast:** Stripe, `@billing-watch`, Alice. The Sales stax.

Coming next: Stripe will post "payment failed: Acme" through HookTunnel. A card will land for Alice: "call Acme about the card", done when the invoice is paid. Nobody will have to notice the email at 03:00. Somebody will own it.

## 3. The locked-down company AI

**Cast:** the bank's internal assistant, `@risk-bot`, Bob. The Renewals stax.

Coming next: IT will only let the assistant send email. It will email the stax: "renewal at risk, Acme, no reply in 30 days". The card will land with Bob, the account owner. The assistant will never touch the workspace.

## 4. The café fridge at 02:10

**Cast:** the fridge, `@fridge-2`, Dee on the opening shift. The Kitchen stax.

{% include badge-partial.html %} The owner adds `@fridge-2` with `device_add`, for Dee, able to ask. The fridge posts "4°C over limit" and nothing else. It never accepts a command, so there is nothing for an outsider to switch. A card lands for Dee: "check fridge 2". The inspector sees who handled it, and when.

## 5. Mum's button by the kettle

**Cast:** Mum's button, `@mums-button`, three siblings. The Mum's house stax.

Coming next: Mum will press one button. A card will land for all three: "Mum needs a hand". The first to claim it will own it. The other two will see it's handled and stand down.

## 6. The tiny robot's plant round

**Cast:** a toy robot, `@plant-bot`, Ava (9). The Home stax.

{% include badge-partial.html %} The robot rolls past the basil, reads the soil and posts "pot 3 is dry". A card lands for Ava: "water the basil". On its next round the robot checks the card. When Ava ticks it done, its light turns green.

{% capture s %}
{% include anim/node.html x=100 y=36 label="@plant-bot" sub="device" kind="agent" w=130 %}
{% include anim/node.html x=380 y=36 label="Ava" sub="ticks it done" kind="person" w=130 d=1.8 %}
{% include anim/edge.html x1=100 y1=62 x2=200 y2=124 kind="write" d=0.5 %}
{% include anim/plane.html x=20 y=96 w=440 h=80 label="Home stax" d=0.2 %}
{% include anim/node.html x=240 y=146 label="water the basil" sub="for @ava" kind="action" w=170 d=1.0 %}
{% include anim/edge.html x1=290 y1=124 x2=380 y2=62 kind="read" d=1.4 %}
{% include anim/trail.html x=20 y=206 when="07:10" who="@plant-bot" agent="true" what="pot 3 is dry" d=2.2 %}
{% include anim/trail.html x=20 y=230 when="07:42" who="Ava" what="done: watered the basil" d=2.6 %}
{% include anim/trail.html x=20 y=254 when="08:10" who="@plant-bot" agent="true" what="checked the card: light green" d=3.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 270" label="The plant robot posts one note, a card lands on the Home stax for Ava, she ticks it done, and the robot checks the card and turns green" caption="The robot posts one signed note: pot 3 is dry. A card lands on the Home stax for Ava. She waters the basil and ticks it done. On its next round the robot checks the card and turns its light green. It never receives a command." svg=s %}

## 7. A second builder nobody has heard of

**Cast:** a cheap hosted coding model, `@cheap-builder`, the Chief. The Product stax.

Coming next: the model will have no connector, only a GitHub account. The Chief will assign it a card. The model will ask HeyMailbox "what's mine?", do the work in its own sandbox, open a pull request and report "done, PR #212". On the board it will look like any other builder.

## Why it holds

**You set the edges.** Each sender gets its own role and two or three verbs, nothing more. Switch the role off and the sender goes quiet. **You can check.** Every request leaves a receipt: who asked, as which role, and what happened.

## What works today

| Scenario | State | Note |
|---|---|---|
| ChatGPT hands an idea to the builder | works today | HeyMailbox over GitHub; set up for you, not self-serve |
| The café fridge, the plant robot | partly | You can add a device with `device_add` today; no device note has been seen landing in production yet |
| Failed payment, company AI, button | planned | Email and Stripe are not senders yet |
| A second builder | planned | Needs "my cards", report and finish in HeyMailbox |

## Try it

1. Read [Add robots, fridges and other bots with HeyMailbox](../agents/mailbox).
2. Give ChatGPT a role on your stax.
3. Ask us to open HeyMailbox for your repo and stax.
