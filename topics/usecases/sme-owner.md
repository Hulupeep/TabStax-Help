---
nav_exclude: true
---

# A studio owner running the business from six apps

[← Back to Use Cases](index.md)

{% include badge-partial.html %}

Maya runs **BrightPixel Studio**. Xero, the bank portal, Asana, email, Figma and WhatsApp Web are open by 08:30. She rebuilds the picture by hand each morning, and some mornings an overdue invoice slips through.

## What Maya sets up

| | |
|---|---|
| **Mission** | Keep BrightPixel paid and clients happy |
| **Goal** | No invoice more than 14 days overdue |
| **Next Actions** | Chase the Atlas Retail invoice. Reply to Nova's logo notes. 10 minutes on leads. |

1. She makes a **BrightPixel Daily Ops** stax. The TabStax extension saves the six tabs with it.
2. Each client gets its own stax: **Atlas Retail Website**, **Nova Branding**, with only that client's tabs.
3. Daily Ops goes in **Must**, the quieter client in **Good**. The dashboard opens on today.
4. She shares Nova Branding with her freelancer, @tom. He sees the same tabs and next actions.
5. An agent, @pixel-agent, claims "Chase the Atlas invoice" under its own name and drafts the reminder. The send is flagged `needs_go_ahead`, so nothing goes out until Maya says yes.

{% capture s %}
{% include anim/node.html x=110 y=38 label="TabStax" sub="6 tabs saved" kind="surface" w=150 d=0.2 %}
{% include anim/node.html x=370 y=38 label="Maya" sub="Must lane" kind="person" w=130 d=0.4 %}
{% include anim/plane.html x=20 y=88 w=440 h=120 label="BrightPixel Daily Ops" d=0.6 %}
{% include anim/edge.html x1=110 y1=64 x2=130 y2=124 kind="write" d=1.0 %}
{% include anim/node.html x=130 y=150 label="Chase Atlas invoice" sub="@pixel-agent" kind="action" w=180 d=1.4 %}
{% include anim/edge.html x1=370 y1=64 x2=350 y2=124 kind="read" d=1.2 %}
{% include anim/node.html x=350 y=150 label="Reply to Nova notes" sub="Maya" kind="action" w=170 d=1.6 %}
{% include anim/edge.html x1=130 y1=176 x2=130 y2=236 kind="dispatch" d=2.0 %}
{% include anim/node.html x=130 y=258 label="Reminder drafted" sub="needs go-ahead" kind="note" w=170 d=2.4 %}
{% include anim/edge.html x1=215 y1=258 x2=390 y2=64 cx=440 cy=258 kind="dispatch" d=2.8 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="Maya's six tabs and two next actions live in one Daily Ops stax; the agent's reminder waits for her go-ahead" caption="TabStax saves Maya's six tabs into the BrightPixel Daily Ops stax. @pixel-agent claims the invoice chase and drafts the reminder. The send waits for Maya's go-ahead before anything leaves." svg=s %}

## Why it holds

**You set the edges.** The agent drafts. Maya keeps the one decision that cannot be undone, and the stax shows who did what.

## What works today

| Step | State |
|---|---|
| Stax, tabs, next actions, attention lanes | Works today |
| Sharing a stax with @handles | Works today |
| Go-ahead before irreversible work | Works today over MCP |
| An agent claiming and reporting under its own name | Partly works today: in production, not yet checked in a browser |

## Try it

1. [Create your first stax](../creating_your_first_stax).
2. [Share it and assign by @handle](../team-stax/assigning-actions).
3. [See how claims and the go-ahead work](../agents/how-claim-works).

[← Back to Use Cases](index.md)
