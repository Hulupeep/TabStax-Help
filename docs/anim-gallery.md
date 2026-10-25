---
title: Animation kit gallery
nav_exclude: true
search_exclude: true
---

# Animation kit gallery

Every primitive in `_includes/anim/`, and one composed scene. Use this page to check motion,
dark mode, reduced motion and phone width before a page ships.

How to compose a figure:

{% raw %}
```liquid
{% capture s %}
{% include anim/node.html x=240 y=60 label="Launch" kind="stax" %}
{% include anim/edge.html x1=240 y1=80 x2=240 y2=160 kind="write" d=0.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 220" label="What the picture shows" caption="The same meaning, in words." svg=s %}
```
{% endraw %}

Rules: every figure has a caption that carries its meaning in text. Anything not live yet gets
`anim/planned.html` next to it. Delays (`d`) are in seconds; keep a whole figure under 4 seconds.

## Nodes

{% capture s %}
{% include anim/node.html x=80 y=40 label="Launch" kind="stax" %}
{% include anim/node.html x=240 y=40 label="Bob" sub="person" kind="person" d=0.15 %}
{% include anim/node.html x=400 y=40 label="@claude" sub="agent" kind="agent" d=0.3 %}
{% include anim/node.html x=80 y=120 label="Dashboard" kind="surface" d=0.45 %}
{% include anim/node.html x=240 y=120 label="XC90" sub="record" kind="record" d=0.6 %}
{% include anim/node.html x=400 y=120 label="Email 5 yards" kind="action" w=140 d=0.75 %}
{% include anim/node.html x=240 y=190 label="A loose note" kind="note" d=0.9 %}
{% include anim/planned.html x=360 y=148 d=1.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 220" label="Seven node kinds: stax, person, agent, surface, record, action, note" caption="Node kinds. A stax is amber, people are blue, agents are violet with a dashed edge, surfaces are grey, records are green, actions are orange. A Planned tag marks anything not live yet." svg=s %}

## Edges

{% capture s %}
{% include anim/node.html x=70 y=40 label="Claude" kind="surface" w=100 %}
{% include anim/node.html x=410 y=40 label="Launch" kind="stax" w=100 %}
{% include anim/edge.html x1=120 y1=40 x2=360 y2=40 kind="read" d=0.2 %}
{% include anim/node.html x=70 y=110 label="hey CLI" kind="surface" w=100 %}
{% include anim/node.html x=410 y=110 label="Launch" kind="stax" w=100 %}
{% include anim/edge.html x1=120 y1=110 x2=360 y2=110 kind="write" d=0.5 %}
{% include anim/node.html x=70 y=180 label="Launch" kind="stax" w=100 %}
{% include anim/node.html x=410 y=180 label="@claude" kind="agent" w=100 %}
{% include anim/edge.html x1=120 y1=180 x2=360 y2=180 cx=240 cy=150 kind="dispatch" d=0.8 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 215" label="Three kinds of edge: read, write, dispatch" caption="Edges. Blue reads from the graph. Amber writes to it. Violet, dashed, hands work to an agent." svg=s %}

## The plane

{% capture s %}
{% include anim/plane.html y=10 h=100 d=0 %}
{% include anim/node.html x=95 y=72 label="Launch" sub="stax" kind="stax" w=110 d=0.2 %}
{% include anim/node.html x=240 y=72 label="Email 5 yards" kind="action" w=130 d=0.35 %}
{% include anim/node.html x=385 y=72 label="Fri 31 Oct" sub="date" kind="record" w=110 d=0.5 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 120" label="The plane holding a stax, an action and a date" caption="The plane. Your stax graph holds typed things: a stax, its next action, its date." svg=s %}

## Trail

{% capture s %}
{% include anim/trail.html x=20 y=30 when="09:02" who="Bob" what="added Book car seats" %}
{% include anim/trail.html x=20 y=56 when="09:14" who="@claude" agent="true" what="completed Draft the brief" d=0.3 %}
{% include anim/trail.html x=20 y=82 when="09:15" who="@claude" agent="true" what="added Send brief to Alice" d=0.6 %}
{% include anim/trail.html x=20 y=108 when="09:40" who="Alice" what="completed Send brief to Alice" d=0.9 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 125" label="Four trail rows: who did what, when" caption="The trail. Every write names who made it, person or agent, and when." svg=s %}

## Composed: one action moves through the plane

{% capture s %}
{% include anim/node.html x=80 y=30 label="Claude" kind="surface" w=110 %}
{% include anim/node.html x=240 y=30 label="Dashboard" kind="surface" w=110 %}
{% include anim/node.html x=400 y=30 label="Telegram" kind="surface" w=110 %}
{% include anim/plane.html y=90 h=110 d=0.1 %}
{% include anim/node.html x=130 y=158 label="Launch" sub="stax" kind="stax" w=110 d=0.2 %}
{% include anim/edge.html x1=80 y1=50 x2=130 y2=132 kind="write" d=0.5 %}
{% include anim/edge.html x1=185 y1=158 x2=255 y2=158 kind="plain" d=0.9 %}
{% include anim/node.html x=320 y=158 label="Email 5 yards" kind="action" w=130 d=1.0 %}
{% include anim/edge.html x1=320 y1=138 x2=240 y2=50 kind="read" d=1.4 %}
{% include anim/edge.html x1=320 y1=138 x2=400 y2=50 kind="read" d=1.4 %}
{% include anim/node.html x=110 y=245 label="You" kind="person" w=90 d=1.8 %}
{% include anim/node.html x=240 y=245 label="Dom" kind="person" w=90 d=1.9 %}
{% include anim/node.html x=370 y=245 label="@chief" kind="agent" w=90 d=2.0 %}
{% include anim/planned.html x=400 y=217 d=2.1 %}
{% include anim/trail.html x=20 y=302 when="09:14" who="You via Claude" what="added Email 5 yards" d=2.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 315" label="An action written from Claude lands in the stax and shows up on every surface" caption="You ask Claude to add an action. It lands in the Launch stax on your graph. The dashboard and Telegram read the same action at once. You, Dom and an agent all see it, and the trail records who added it. An agent with its own name, like @chief, is planned." svg=s %}
