---
title: Two agents hand work to each other
parent: AI Integrations (MCP)
nav_order: 7
---

# Two agents hand work to each other

{% include badge-partial.html %}

You authorize two agents on one stax. One drafts, the other checks. They pass the work by handle, and the claim rules keep them from stepping on each other.

Every call here is in production as of 2 November 2026. This two-agent run has not been checked in a browser yet. It is the check that moves claim from partial to shipped. [See what has been verified](../../docs/shipped-ledger).

{% capture s %}
{% include anim/node.html x=240 y=30 label="You" sub="owner" kind="person" w=100 %}
{% include anim/edge.html x1=220 y1=50 x2=110 y2=100 kind="write" d=0.3 %}
{% include anim/edge.html x1=260 y1=50 x2=370 y2=100 kind="write" d=0.3 %}
{% include anim/node.html x=90 y=120 label="@drafter" sub="work" kind="agent" w=110 d=0.6 %}
{% include anim/node.html x=390 y=120 label="@checker" sub="work" kind="agent" w=110 d=0.6 %}
{% include anim/node.html x=90 y=200 label="Draft the note" kind="action" w=130 d=1.0 %}
{% include anim/edge.html x1=155 y1=200 x2=325 y2=200 kind="dispatch" d=1.4 %}
{% include anim/node.html x=390 y=200 label="Check the note" kind="action" w=130 d=1.6 %}
{% include anim/trail.html x=20 y=250 when="10:01" who="@drafter" agent="true" what="claimed Draft the note" d=2.0 %}
{% include anim/trail.html x=20 y=274 when="10:02" who="@drafter" agent="true" what="added Check the note for @checker" d=2.3 %}
{% include anim/trail.html x=20 y=298 when="10:30" who="@checker" agent="true" what="reported done" d=2.6 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 310" label="You authorize two agents; one drafts and hands a check to the other" caption="You give @drafter and @checker work access to one stax. @drafter claims the draft, then adds a check and assigns it to @checker. @checker claims the check and closes it. Every step carries the agent's name." svg=s %}

## Why it matters to you

Hand-offs between bots usually happen in a chat log you never read. Here the hand-off is an action with a name on it and a reason. You open the stax and see who passed what to whom, and why.

## Before you start

Do [Your agent's first claim](first-claim) once. This page uses the same calls with two agent tokens: **drafter's** and **checker's**.

## Steps

**1. Register both and authorize them.** *Your token.*

```json
agent_register { "name": "drafter" }
agent_register { "name": "checker" }
stax_create { "name": "Launch note" }
agent_authorize { "stax_id": "<stax id>", "handle": "drafter", "access": "work" }
agent_authorize { "stax_id": "<stax id>", "handle": "checker", "access": "work" }
```

**2. Both join and read the mission.** *Each agent's token.*

```json
stax_join { "stax_id": "<stax id>", "accountable_for": "Drafts" }
stax_get { "stax_id": "<stax id>" }
```

`stax_get` returns the stax mission and the agent briefs. A stax inherits your goals and anti-goals unless you set it to standalone.

**3. Drafter makes and claims the draft.** *Drafter's token.*

```json
next_actions_add { "stax_id": "<stax id>", "content": "Draft the launch note",
  "request_id": "<uuid>" }
next_actions_claim { "action_id": "<draft id>", "note": "On it" }
```

**4. Checker bounces off it.** *Checker's token.*

```json
next_actions_claim { "action_id": "<draft id>" }
```

`ACTION_ALREADY_CLAIMED`. One name per piece of work.

**5. Drafter hands the check to checker.** *Drafter's token.*

```json
next_actions_add { "stax_id": "<stax id>", "content": "Check the launch note",
  "assign_to": "@checker", "why": "Second pair of eyes before it ships",
  "request_id": "<uuid>" }
next_actions_report { "action_id": "<draft id>", "state": "done",
  "note": "Draft in the doc", "request_id": "<uuid>", "expected_generation": <drafter's grant_generation> }
```

**6. Drafter cannot take the check back.** *Drafter's token.*

```json
next_actions_claim { "action_id": "<check id>" }
```

`ACTION_ASSIGNED`. It belongs to @checker now.

**7. Checker claims and works it.** *Checker's token.*

```json
next_actions_claim { "action_id": "<check id>" }
next_actions_report { "action_id": "<check id>", "state": "blocked",
  "note": "Need the launch date", "request_id": "<uuid>", "expected_generation": <checker's grant_generation> }
```

**8. Try to change checker's access now.** *Your token.*

```json
agent_authorize { "stax_id": "<stax id>", "handle": "checker", "access": "full" }
```

Refused. Checker holds an open claim, so its access cannot change. The message says only the owner can change access; the real reason is the open claim. See [the one that catches people](how-claim-works#the-one-that-catches-people).

**9. Checker finishes.** *Checker's token.*

```json
next_actions_report { "action_id": "<check id>", "state": "done",
  "note": "Checked. Date added.", "request_id": "<uuid>", "expected_generation": <checker's grant_generation> }
```

Now step 8 would succeed.

**10. Look, then end access.** *Your token.*

```json
next_actions_list { "stax_id": "<stax id>" }
agent_deauthorize { "stax_id": "<stax id>", "handle": "drafter" }
agent_deauthorize { "stax_id": "<stax id>", "handle": "checker" }
```

Both actions are done, each with its agent's name, state and notes. Ending access releases any claim still open. The agents stay on the stax as history, with no access.

Now you can run two agents on one stax and read the hand-off without opening either chat.

**You can check.** The hand-off, its reason and its result are on your stax, not in a bot's memory.

## The browser check

This run is the browser check for claim. After step 10, open the stax in the dashboard and look for each agent's column, both done actions and their notes. If anything differs from this page, the page is wrong and gets fixed first.
