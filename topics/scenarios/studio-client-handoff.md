---
title: Studio client handoff
parent: Scenarios
nav_order: 2
scenario_state: partly
---

# A client review, and nobody chases a chat

{% include badge-partial.html %}

**Cast:** Nadia runs a small web studio. Jo is her designer. `@atlas-builder` is a Claude Code worker. The stax is **Atlas website**.

## Before

The client review is Thursday, 10:00. The mobile menu still fails with a keyboard. The focus colour lives in Jo's head, the fix in a terminal, and the preview link in a scrolled-away chat.

## What happens

| | |
|---|---|
| **Mission** | Win the Atlas renewal |
| **Goal** | The client signs off the mobile menu on Thursday |
| **Next Action** | `@atlas-builder`: make the mobile menu keyboard-accessible and post the preview link |

1. Nadia adds the Next Action on Atlas, assigned to `@atlas-builder`, with a check: the preview page must load.
2. `@atlas-builder` claims it. The card now names who is on it.
3. It needs Jo's focus-ring colour. It comments on the card to `@jo`. The HeyStax Telegram bot sends Jo the question.
4. Jo replies in Telegram with the colour. Her reply lands on the card as a comment.
5. `@atlas-builder` makes the fix and reports done with the preview link. HeyStax loads the preview itself. The card closes only when that check passes.
6. Nadia opens Atlas, checks the preview and decides what to tell the client.

## The graph after

{% capture s %}
{% include anim/plane.html x=20 y=6 w=440 h=144 label="Atlas website stax" %}
{% include anim/node.html x=240 y=80 label="Keyboard menu fix" sub="check: preview loads" kind="action" w=180 d=0.4 %}
{% include anim/node.html x=80 y=80 label="Nadia" sub="owner" kind="person" w=100 d=0.2 %}
{% include anim/edge.html x1=130 y1=80 x2=150 y2=80 kind="write" d=0.6 %}
{% include anim/node.html x=400 y=60 label="@atlas-builder" kind="agent" w=110 h=34 d=1.0 %}
{% include anim/node.html x=400 y=108 label="Jo" sub="via Telegram" kind="person" w=110 d=1.6 %}
{% include anim/edge.html x1=345 y1=60 x2=330 y2=72 kind="dispatch" d=1.2 %}
{% include anim/edge.html x1=345 y1=108 x2=330 y2=92 kind="write" d=1.8 %}
{% include anim/trail.html x=24 y=170 when="Tue 09:10" who="Nadia" what="adds the card with a check" d=2.2 %}
{% include anim/trail.html x=24 y=194 when="Tue 09:40" who="@atlas-builder" agent="true" what="asks @jo for the colour" d=2.6 %}
{% include anim/trail.html x=24 y=218 when="Tue 11:05" who="Jo" what="replies in Telegram" d=3.0 %}
{% include anim/trail.html x=24 y=242 when="Tue 15:20" who="@atlas-builder" agent="true" what="done, preview check passed" d=3.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 260" label="The Atlas stax holds Nadia's card with its check, the builder's claim, Jo's answer from Telegram and the passed preview check, each line signed by who did it" caption="One card holds the whole handoff. Nadia's request, the builder's question, Jo's answer from Telegram and the passed preview check sit on Atlas, each signed by who did it." svg=s %}

## Why it holds

**You can check.** On Thursday Nadia answers "where are we?" from Atlas. She does not ask two chats or the builder. Every line says who did it, and done means HeyStax checked the preview.

## What works today

| Step | State | Note |
|---|---|---|
| A card with a check that closes only when it passes | works today | `verified-done` |
| A comment to `@jo` reaches her in Telegram, and her reply comes back | works today | `action-messages` |
| A worker claims the card under its own name | partly | `agent-claim-rules`: in production, the full owner and two-agent journey still needs a browser check |
| The builder makes the change and the preview | outside HeyStax | Claude Code's own tools; HeyStax keeps the link |
| Telling the client | Nadia | No automatic client email |

## Try it

1. Make an Atlas stax and add the card. See [Verified done](../agents/asks-and-checks).
2. Connect a builder to a role. See [Connect a worker to a role](../agents/connect-a-worker).
3. Ask a person on a card. See [Let your bots ask you questions](../team-stax/messages).
