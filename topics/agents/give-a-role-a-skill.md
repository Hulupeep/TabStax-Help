---
title: Give a role a skill
parent: AI Integrations (MCP)
nav_order: 17
---

# Give a role a skill

A **skill** is what to do, step by step, and why. It lives in your HeyStax account, next to the role. Your stax holds the role's job. The skill holds the know-how.

## Why it matters to you

It is Tuesday. Bob's builder bot ships a fix, then trips on the same release step it tripped on last week. You explain it again. Then the bot is swapped for a cheaper one, and you explain it a third time.

Write it once as a skill and every brain on that role reads the same steps. Claude, Codex, Grok Bot or Hermes. Nothing to paste.

## How the two fit

- **Your stax says what.** The role's job, its goal, its Never rules, and the record of what got done.
- **The skill says how.** The method the brain loads on every card, or ignores when the brief says otherwise.
- **No cage.** A skill is plain text in your account. Any brain on the role gets it on its card. Swap the brain and the skill stays.

## How to do it

1. **Do the job once with your bot.** Correct it like a new hire until the result is right.
2. **Write down what worked.** Ask the bot: "Turn what we just did into a skill." Keep the method, drop the figures.
3. **Save it on [dash.heystax.ai/skills](https://dash.heystax.ai/skills).** Press **New skill**, paste it, pick the kind. [Which kind of skill?](four-kinds-of-skill)
4. **Press Give to a role.** Its next card carries the skill's text. Nothing to paste into a brief.
5. **Check it now and then.** Each skill shows when it was last used. If a role does better without it, shrink it.

{% capture s %}
{% include anim/node.html x=120 y=40 label="Role brief" sub="job + Never" kind="record" w=150 d=0.2 %}
{% include anim/node.html x=360 y=40 label="Skill" sub="how, in steps" kind="record" w=150 d=0.5 %}
{% include anim/edge.html x1=120 y1=66 x2=240 y2=130 kind="write" d=1.0 %}
{% include anim/edge.html x1=360 y1=66 x2=240 y2=130 d=1.2 %}
{% include anim/node.html x=240 y=154 label="@acme-builder" sub="any brain" kind="agent" w=150 d=1.5 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 d=2.0 %}
{% include anim/node.html x=240 y=244 label="Release 1338" sub="done, checks true" kind="action" w=170 h=40 d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="A role's brief and a skill both feed the role's worker, which finishes the card" caption="The role's brief on your stax says what the job is and what it must never do. The skill in your account says how. Whichever brain works @acme-builder reads both, then finishes the card, and the result lands on your stax under the role's name." svg=s %}

## Role packs carry skills

When you hire a role from a pack, its skills come with it. Library skills are copied into your account and given to the new role, so its first card already has them.

Now you can teach a role once, swap its brain, and keep the know-how. The job and the proof stay on your stax.

**Read next:** [Build roles, not agents](../roles/) · [Keep method in skills, facts on the stax](four-kinds-of-skill) · [Set up a team in one call](role-packs) · [Connect a worker to a role](connect-a-worker)
