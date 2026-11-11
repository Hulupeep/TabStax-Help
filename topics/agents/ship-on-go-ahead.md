---
title: Ship on a go-ahead
parent: AI Integrations (MCP)
nav_order: 11
---

# Ship on a go-ahead

{% include badge-partial.html %}

A builder role writes the change and opens a pull request. Your Chief of Staff gives the go-ahead. Then the release runs itself: the database change, then the deploy.

## Why it matters to you

Today the builder stops at the pull request. Then you open a terminal on your own computer, paste a release script and watch it run. You are the last step of every change.

With this, the change goes live while you are on the school run. You read the result on the card.

## How it works

1. **The builder ships the PR.** A card assigned to `@timebreez-builder` ends with a branch and a pull request, noted on the card.
2. **The card asks for a go-ahead.** Anything that touches production is flagged as needing one. Workers cannot approve their own work.
3. **The Chief gives the go-ahead.** It checks the change against your mission and Never rules. You can give it yourself instead.
4. **CI applies it.** {% include badge-planned.html %} On merge, the release job will apply the database changes in order, then deploy.
5. **The card closes with proof.** {% include badge-planned.html %} The release job will note what went live and when, on the same card.

Steps 1 to 3 work today: irreversible work waits for a go-ahead from you or a Chief you granted go_ahead. Steps 4 and 5 are coming next.

{% capture s %}
{% include anim/node.html x=90 y=40 label="Builder" sub="@timebreez-builder" kind="agent" w=160 %}
{% include anim/edge.html x1=170 y1=40 x2=250 y2=40 kind="write" d=0.6 %}
{% include anim/node.html x=340 y=40 label="Pull request" sub="noted on the card" kind="action" w=170 d=0.8 %}
{% include anim/edge.html x1=340 y1=66 x2=340 y2=110 kind="read" d=1.4 %}
{% include anim/node.html x=340 y=136 label="Chief of Staff" sub="go-ahead" kind="agent" w=170 d=1.6 %}
{% include anim/edge.html x1=255 y1=136 x2=175 y2=136 kind="dispatch" d=2.2 %}
{% include anim/node.html x=90 y=136 label="CI release" sub="database, then deploy" kind="surface" w=160 d=2.4 %}
{% include anim/planned.html x=59 y=166 d=2.4 %}
{% include anim/edge.html x1=90 y1=192 x2=90 y2=226 kind="write" d=3.0 %}
{% include anim/node.html x=90 y=252 label="Card done" sub="what went live, when" kind="note" w=160 d=3.2 %}
{% include anim/planned.html x=59 y=282 d=3.2 %}
{% include anim/trail.html x=200 y=232 when="14:02" who="@timebreez-builder" agent="true" what="PR opened" d=3.6 %}
{% include anim/trail.html x=200 y=256 when="14:09" who="@chief-of-staff" agent="true" what="go-ahead given" d=4.0 %}
{% include anim/trail.html x=200 y=280 when="14:15" who="release" agent="true" what="live in production" d=4.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 310" label="Ship on a go-ahead: the builder opens a pull request, the Chief of Staff gives the go-ahead, CI applies the database change and deploys, and the card closes with proof" caption="The builder ships a pull request and notes it on the card. The Chief of Staff gives the go-ahead. The CI release and the closing note are planned: today you still run the release yourself." svg=s %}

## A Tuesday with Bob

Bob runs a small payroll product. At 13:40 he tells his Chief, "staff need to see their leave balance on the payslip."

The Chief adds a card for `@timebreez-builder`. The builder writes the change, with a new database column, and opens a pull request by 14:02. The card asks for a go-ahead because it touches production.

The Chief reads the change, checks it against "never touch a closed pay period", and gives the go-ahead at 14:09. Today Bob runs the release himself. When this is complete, CI runs it and the card says what went live.

## What stays yours

- **Who can give the go-ahead.** Only you, or a Chief you granted go_ahead. Never the worker that did the work.
- **The Never rules.** The Chief checks every go-ahead against them.
- **Turning it off.** Take go_ahead back from the Chief and every release waits for you again.

## Coming next

{% include badge-planned.html %} Deploy on merge for the HeyStax repo first, then for your own products such as Timebreez. A release that fails will stop, put the error on the card and message you.

Now you can hand a change to a role and see it reach production, with every step signed on the card.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Roles, workers and their keys](roles-workers-tokens)
