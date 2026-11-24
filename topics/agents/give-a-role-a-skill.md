---
title: Give a role a skill
parent: AI Integrations (MCP)
nav_order: 17
---

# Give a role a skill

A **skill** is a folder with one `SKILL.md` file in it: what to do, step by step, and why. Your stax holds the role's job. The skill holds the know-how.

## Why it matters to you

It is Tuesday. Bob's builder bot ships a fix, then trips on the same release step it tripped on last week. You explain it again. Then the bot is swapped for a cheaper one, and you explain it a third time.

Write it once as a skill and every brain on that role reads the same steps. Claude, Codex, Grok Bot or Hermes. Nothing to paste.

## How the two fit

- **Your stax says what.** The role's job, its goal, its Never rules, and the record of what got done.
- **The skill says how.** Optional know-how the brain may use, or ignore when it knows better.
- **No cage.** A skill is plain files. Any runtime reads it, with or without HeyStax. Swap the brain and the skill still works.

## How to do it

1. **Do the job once with your bot.** Correct it like a new hire until the result is right.
2. **Ask it to write the skill.** "Turn what we just did into a skill." Claude has a skill-creator for this.
3. **Put the folder where the worker runs.** In a repo, that is `.claude/skills/<name>/`. Claude Code loads it by itself.
4. **Point the role at it.** Add one line to the role's brief: "Skills you may load:" and the link. Any brain on the role sees it on its next card.
5. **Check it now and then.** Run the same card with and without the skill. If "without" wins, shrink the skill.

{% capture s %}
{% include anim/node.html x=120 y=40 label="Role brief" sub="job + Never" kind="record" w=150 d=0.2 %}
{% include anim/node.html x=360 y=40 label="SKILL.md" sub="how, in steps" kind="record" w=150 d=0.5 %}
{% include anim/edge.html x1=120 y1=66 x2=240 y2=130 kind="write" d=1.0 %}
{% include anim/edge.html x1=360 y1=66 x2=240 y2=130 d=1.2 %}
{% include anim/node.html x=240 y=154 label="@acme-builder" sub="any brain" kind="agent" w=150 d=1.5 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 d=2.0 %}
{% include anim/node.html x=240 y=244 label="Release 1338" sub="done, checks true" kind="action" w=170 h=40 d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="A role's brief and a skill both feed the role's worker, which finishes the card" caption="The role's brief on your stax says what the job is and what it must never do. The SKILL.md file says how. Whichever brain works @acme-builder reads both, then finishes the card, and the result lands on your stax under the role's name." svg=s %}

## Coming next

{% include badge-planned.html %} **Role packs will carry skills.** When you hire a role from a pack, it will also hand the worker links to the skills that role uses. It will stay a link to plain files, never a copy locked inside HeyStax.

Now you can teach a role once, swap its brain, and keep the know-how. The job and the proof stay on your stax.

**Read next:** [Set up a team in one call](role-packs) · [Connect a worker to a role](connect-a-worker)
