---
title: Hand a bug to an agent
parent: Team Stax
nav_order: 4
---

# Hand a bug to an agent from the chat

Gaia is testing the Timebreez import. The Reconcile step throws a red error. She screenshots it into the team group, like she always does.

Before, that screenshot waited for Colm to read it, retype it into a ticket and chase a developer. Now she replies to it with one line, and an agent works it and answers her in the same chat.

{% include badge-partial.html %}

## Why it matters to you

- **One agent, many reporters.** Twenty people can report bugs to one agent role. They need no AI account, no repo access and no setup beyond linking Telegram once.
- **Nothing is retyped.** The agent gets the reporter's words, the message they replied to and the screenshot itself.
- **The loop closes where the bug was found.** The group sees "picked up", then "finished" with a verdict: a bug and its fix, not a bug and why, or can't reproduce.
- **Nothing is explained twice.** The agent also reads what happened since: notes from earlier runs, related cards, summaries from Claude Code sessions and your later replies. See [What a worker reads before it starts](../agents/what-a-worker-gets).
- **You can check.** The card holds the report, every note the agent left, the branch and the PR. The owner gets a copy when someone hands work over in a private chat.

## How to do it

1. Find the bug message or screenshot in the group.
2. Reply to it (swipe left, or tap **Reply**).
3. Send `/t @timebreez-builder`, using the agent's handle from `/who`. Add words after the handle if you want: `/t @timebreez-builder happens after carry forward too`.
4. The bot answers with the card it made. When the agent claims it, the group sees `@timebreez-builder picked up: ...`.
5. When it is done, the group sees `finished` and a `Result:` line with the verdict.

Use the `/t` form. In most groups the bot only receives commands, so a plain `@timebreez-builder` never reaches it. A group owner can change that in Telegram, and then the plain handle works too.

{% capture s %}
{% include anim/node.html x=100 y=48 label="Gaia: screenshot" sub="Timebreez_work group" kind="surface" w=170 d=0.2 %}
{% include anim/edge.html x1=100 y1=74 x2=120 y2=150 kind="write" d=0.6 %}
{% include anim/plane.html x=20 y=118 w=440 h=92 label="timebreez stax" d=0.4 %}
{% include anim/node.html x=135 y=168 label="Card + screenshot" kind="action" w=170 h=34 d=1.0 %}
{% include anim/edge.html x1=220 y1=168 x2=330 y2=168 kind="dispatch" d=1.4 %}
{% include anim/node.html x=370 y=168 label="@timebreez-builder" kind="agent" w=150 h=34 d=1.8 %}
{% include anim/edge.html x1=370 y1=185 x2=330 y2=250 kind="write" d=2.2 %}
{% include anim/node.html x=250 y=264 label="finished · Result: Not a bug" kind="note" w=250 h=34 d=2.6 %}
{% include anim/edge.html x1=125 y1=264 x2=40 y2=74 cx=20 cy=264 kind="dispatch" d=3.0 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 300" label="A screenshot in a Telegram group becomes a card for an agent, and the verdict comes back to the group" caption="Gaia replies to her screenshot with /t @timebreez-builder. The card carries her words and the picture. The agent claims it, works it, and the group gets finished with a Result line." svg=s %}

## Scenarios

**The in-house tester.** Gaia rehearses a customer import and hits an error at Reconcile. She replies `/t @timebreez-builder` to her screenshot. Twenty minutes later the group reads `Result: Not a bug: the leave year is not set for this organisation. Set it in Leave settings, then reconcile.` She fixes the setting and moves on. Nobody else was pulled in.

**The agency client.** Nadia's studio shares a group with a client. The client posts a photo of a broken menu on their phone. Nadia replies `/t @atlas-builder`. The agent finds the cause, opens a PR and reports `Bug: menu overlaps at 375px, fixed in PR 41`. Nadia checks the preview before she tells the client.

**The field team.** Bob is on site with a tablet. The inspection form rejects a date. He snaps it and sends `/t @forms-builder date field rejects 31/10` as the photo caption. The agent answers `Cannot reproduce: 31/10/2026 saves on the current form. Which app version is the tablet on?` and the question comes to Bob in Telegram.

**The beta group.** A founder runs a group of 30 beta users. Each bug report is one reply away from the builder role. The founder reads verdicts, not raw reports, and only steps in when the answer is a real bug that needs a product call.

## What you need once

- The group is connected to the stax and each reporter has linked Telegram. See [Telegram](telegram).
- The agent role is on the stax with a worker listening. See [Connect a worker](../agents/connect-a-worker).

## What works today

| Step | State |
|---|---|
| `/t @agent` as a reply, card with the quoted message and screenshot | live in the product, not yet seen end to end |
| Agent reads the report and the screenshot on your machine | live in the CLI, not yet seen end to end |
| Picked up and finished with a verdict, in the chat | live in the product, not yet seen end to end |
| A plain `@agent` with no `/t` | only in groups where the bot can read all messages |

Now you can turn a screenshot into a verdict without retyping a word.
