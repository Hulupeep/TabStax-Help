---
title: See what the work earned and cost
parent: Set up your Chief of Staff
nav_order: 6
---

# See what the work earned and cost

Busy is not the same as paid. HeyStax records what the work earned (replies, signups, money) and what each run cost, against the role that did it.

## Why it matters to you

Monday, 08:00. Your receipt says 24 cards moved. That tells you your roles were busy. It does not tell you whether @kite-bd's emails brought a single reply, or what the week of runs cost you. This page is how you find out.

## What the work earned

1. **Connect a source.** With your own token, ask your AI app to run `outcome_connect` on the stax. Pick `stripe` (a restricted read key, then the webhook secret) or `webhook` (your product posts signups and trials, signed).
2. **Replies count already.** Every reply your CRM records becomes an outcome. Nothing to connect.
3. **Read it.** Ask for `outcomes_list`. You get each reply, signup and payment, newest first, and a summary per stax for 7 and 30 days.
4. **See who earned it.** Each one is credited to the role, and the card, whose CRM send to that organisation came last in the 60 days before. No send, no credit, but it still counts for the stax.
5. **Watch MRR on the goal board.** It comes from Stripe. Until Stripe is connected it says **not connected**, never 0.

{% capture s %}
{% include anim/node.html x=110 y=40 label="@kite-bd" sub="claims a card" kind="agent" w=140 d=0.2 %}
{% include anim/edge.html x1=180 y1=40 x2=280 y2=40 kind="write" d=0.6 %}
{% include anim/node.html x=360 y=40 label="CRM send" sub="Hill Street School" kind="record" w=160 d=0.8 %}
{% include anim/edge.html x1=360 y1=66 x2=100 y2=126 kind="read" d=1.2 %}
{% include anim/node.html x=100 y=150 label="Reply" sub="from the school" kind="record" w=130 d=1.4 %}
{% include anim/node.html x=240 y=150 label="Payment" sub="from Stripe" kind="record" w=130 d=1.6 %}
{% include anim/node.html x=380 y=150 label="Signup" sub="from your product" kind="record" w=130 d=1.8 %}
{% include anim/edge.html x1=100 y1=176 x2=140 y2=232 kind="write" d=2.2 %}
{% include anim/edge.html x1=240 y1=176 x2=160 y2=232 kind="write" d=2.3 %}
{% include anim/edge.html x1=380 y1=176 x2=180 y2=232 kind="write" d=2.4 %}
{% include anim/edge.html x1=240 y1=176 x2=360 y2=232 kind="write" d=2.5 %}
{% include anim/node.html x=140 y=258 label="Credited to @kite-bd" sub="and its card" kind="action" w=180 d=2.6 %}
{% include anim/node.html x=370 y=258 label="Goal board" sub="MRR from Stripe" kind="stax" w=150 d=2.8 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A role's CRM send leads to a reply, a payment or a signup; each is credited back to that role and its card, and payments set MRR on the goal board" caption="@kite-bd claims a card and sends to Hill Street School. A reply, a payment from Stripe or a signup from your product comes in. Each is credited to @kite-bd and the card it held, because its send came last. Payments also set MRR on the goal board." svg=s %}

## What it cost

| Where | What you see |
|---|---|
| A run ends | The worker can report its model, tokens and `cost_usd` on `run_end`. Cost is never guessed. |
| The stax | `stax_get` shows this month's spend, split by role. Runs that reported no cost are counted, not priced. |
| The coach board | Each client stax shows its spend. See [Run many client stax](../crm/coach-board.html). |

## Share a receipt {% include badge-partial.html %}

You can make a receipt link from your AI app today with `receipt_share`. It shows counts and role names by default, never a person's name, an email or an amount. It expires within 30 days, and `receipt_share_revoke` ends it at once.

The page that link opens is coming next. Until it is live, a link has nowhere to open.

Now you can tell busy from paid, per role, and know what the runs cost.
