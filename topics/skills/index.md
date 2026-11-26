---
title: Skills
nav_order: 2.7
has_children: false
---

# Teach your roles skills

A **skill** is how a role does its work, written once in plain words. It lives in your HeyStax account. Every brain that takes the role's seat loads it at the start of each card.

## Why it matters to you

Tuesday, 16:40. You correct @sales-bot's follow-up for the third time, the same way. Next week a cheaper model takes the seat and you explain it again.

Write the correction once as a skill. Whoever works the role reads it on every card: Claude, Codex, Grok Bot, a person. You never paste it, and nobody needs your repo.

## How to do it

1. **Open [dash.heystax.ai/skills](https://dash.heystax.ai/skills).** Sign in. Your roles start on house rules only.
2. **Start from the library, or write your own.** The library has proven skills, like `sales-call` and `cold-call-phone`. Press **New skill** to write one in your own words.
3. **Press Give to a role.** Pick the role. Its next card loads the skill.
4. **Fix it when the role gets it wrong.** Open the skill, press **Edit the method**, say what changed and save. You get a new version, and the roles move to it.
5. **Check it runs.** Each skill shows which roles have it and when it was last used.

Or ask your Chief: "Give @sales-bot a skill for follow-ups." It writes the skill and gives it to the role. When it creates a new role, it gives the role its skills in the same step.

{% capture s %}
{% include anim/node.html x=110 y=40 label="Your skill" sub="method, versioned" kind="record" w=150 d=0.2 %}
{% include anim/node.html x=370 y=40 label="Your stax" sub="facts, cards, dates" kind="record" w=150 d=0.5 %}
{% include anim/edge.html x1=110 y1=66 x2=240 y2=130 d=1.0 %}
{% include anim/edge.html x1=370 y1=66 x2=240 y2=130 kind="write" d=1.2 %}
{% include anim/node.html x=240 y=154 label="@sales-bot" sub="any brain" kind="agent" w=150 d=1.5 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 d=2.0 %}
{% include anim/node.html x=240 y=244 label="Follow-up drafted" sub="Skill used: follow-up@1.1.0" kind="action" w=210 h=40 d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="A skill and the stax's facts both feed the role's worker, which leaves a result that says which skill it used" caption="The skill in your account holds the method. Your stax holds the figures, people and dates. Whichever brain works @sales-bot gets both on its card and says which version of the skill it used." svg=s %}

## What stays yours

- **Private by default.** Your skills are only in your account. Another HeyStax account never sees them.
- **The library is read-only.** Giving a library skill to a role copies it into your skills, so you can change your copy.
- **Saved versions never change.** A fix is a new version. You can see who saved each one, you or a role.
- **Facts stay on the stax.** A skill that holds an email address, a phone number, a key or a big euro figure is refused on save, with the line that broke the rule. Put those on the stax as cards and dates.

Now you can teach a role once, swap its brain, and see which method ran on every card.

**Read next:** [Keep method in skills, facts on the stax](../agents/four-kinds-of-skill) · [Have your Chief make skills](../chief/make-skills) · [Build roles, not agents](../roles/)
