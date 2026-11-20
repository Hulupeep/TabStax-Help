---
title: Asks that don't wait, and done that is checked
parent: AI Integrations (MCP)
nav_order: 15
---

# Asks that don't wait, and done that is checked

A bot that needs a decision asks with a recommendation and carries on if you don't answer. A bot that says "done" on a card with a check isn't believed until HeyStax checks it.

## Why it matters to you

Tuesday, 14:00. You are in a meeting. Your marketing role asks "21 to 50 staff schools first?" It used to stop until you saw it, and the day was gone.

Now it says what it would do, and when. The work goes on. If you disagree later, your answer reaches it as a correction.

## Asks with a default

1. The role asks on the card, with 2 to 4 options and the one it recommends.
2. No answer in time (4 hours unless it says otherwise)? HeyStax takes the recommended option and notes it on the card, signed by HeyStax, not you.
3. A step that can't be undone never goes ahead on silence. It waits for your go-ahead, or your Chief's.
4. A role can't answer its own ask.
5. A hold on the stax, or on all your stax, stops every ask from going ahead. Your hold always wins.

## Done means checked

You, or your Chief, put a check on a card: a page must return 200, or pull request #123 must be merged.

{% capture s %}
{% include anim/node.html x=240 y=30 label="@builder: done" kind="agent" w=150 %}
{% include anim/edge.html x1=240 y1=52 x2=240 y2=84 kind="write" d=0.4 %}
{% include anim/node.html x=240 y=110 label="HeyStax checks" sub="the page or the PR" kind="surface" w=170 d=0.6 %}
{% include anim/edge.html x1=190 y1=136 x2=120 y2=170 kind="write" d=1.0 %}
{% include anim/node.html x=110 y=196 label="Pass: card closes" sub="with the proof" kind="action" w=170 d=1.2 %}
{% include anim/edge.html x1=290 y1=136 x2=360 y2=170 kind="dispatch" d=1.0 %}
{% include anim/node.html x=370 y=196 label="Fail: card reopens" sub="with the reason" kind="action" w=170 d=1.4 %}
{% include anim/trail.html x=20 y=250 when="16:02" who="@builder" agent="true" what="reported done" d=1.8 %}
{% include anim/trail.html x=20 y=274 when="16:02" who="HeyStax" what="404 at /pricing: reopened" d=2.1 %}
{% include anim/trail.html x=20 y=298 when="16:40" who="HeyStax" what="200 at /pricing: closed" d=2.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 310" label="A role reports a card done; HeyStax runs the check; a pass closes the card, a fail reopens it" caption="@builder says the card is done. HeyStax runs the check itself. A pass closes the card with the proof. A fail reopens it with the reason, and the role is told what to fix. After the third fail, your Chief hears about it." svg=s %}

The role doing the work can't set or change its own check. If you mark the card done yourself, that counts, and it is noted as your call.

Page checks fetch only public https pages on port 443. Never an IP address, an internal name, or a page behind a redirect.

A pull request check reads the GitHub repo linked to the stax. For a private repo, give HeyStax your own GitHub token for that stax with `github_check_token_set`. Only you can set it. Without it, a private repo shows as unreachable, not as the role's mistake.

## What works today

| Part | State |
|---|---|
| Asks with options, a recommendation and a deadline; going ahead on silence; never for a step that can't be undone | live, seen on 13 Nov 2026 |
| Buttons for an ask in Telegram | coming next |
| A page check on a card; a failed check reopens it with the reason | live, seen on 13 Nov 2026 |
| A merged pull request as a card's check, on a public repo | live, offered in production on 16 Nov 2026 |
| Your own GitHub token, so a pull request check can read a private repo | live, offered in production on 19 Nov 2026 |

## Coming next

{% include badge-planned.html %} **Earned autonomy.** A role will start small and earn its reach. A new role's asks will go to your Chief and never go ahead on silence. After 10 checked cards in 14 days it will move up a level. Failed checks will move it back down at once. It will be off until you turn it on for a stax.

Now you can let work go on while you are busy, and close a card only when the proof is in.
