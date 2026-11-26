---
title: Give builders your design skills
parent: Skills
nav_order: 1
---

# Give builders your design skills

A design skill is your product's look and rules, written once. Any role that builds screens loads it, together with a short check of what the screen is for.

## Why it matters to you

Thursday, 14:40. You open a page a bot built for you. Every fact on it is right, and it still looks like nobody decided anything: a grid of boxes, two blue buttons, no next step.

The bot never knew your design existed, and nobody asked it what the page was for. Give the role two skills and it knows both, on every card, whichever brain takes the seat.

## The two skills a builder needs

- **`jtbd-ux-designer`**: before any pixel moves, the builder writes five lines. The job ("When ..., I want to ..., so I can ..."), the one primary action, what you see in the first five seconds, the empty state, and the phone layout.
- **Your product's design skill**: your colours, type, spacing, and the few rules that make a screen look like yours, with a dark-mode value for every colour. For HeyStax itself this is `heystax-design`.

No design skill for a product yet? Give the role `product-design-system`. Its first screen card writes one from your best existing page, then builds with it.

## How to do it

1. **Open [dash.heystax.ai/skills](https://dash.heystax.ai/skills).**
2. **Find `jtbd-ux-designer`** and press **Give to a role**. Pick the builder.
3. **Give the same role your product's design skill**, or `product-design-system` if you don't have one yet.
4. **Check the next screen card.** It should open with the job note and end with `Skill used: jtbd-ux-designer@1.0.0`.

Or tell your Chief: "Give @site-builder our design skills." It gives the role both skills and says so on the card.

{% capture s %}
{% include anim/node.html x=110 y=40 label="jtbd-ux-designer" sub="the job first" kind="record" w=160 d=0.2 %}
{% include anim/node.html x=370 y=40 label="Your design skill" sub="look and rules" kind="record" w=160 d=0.5 %}
{% include anim/edge.html x1=110 y1=66 x2=240 y2=130 d=1.0 %}
{% include anim/edge.html x1=370 y1=66 x2=240 y2=130 d=1.2 %}
{% include anim/node.html x=240 y=154 label="@site-builder" sub="any brain" kind="agent" w=150 d=1.5 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 d=2.0 %}
{% include anim/node.html x=240 y=244 label="Page with one next step" sub="phone and dark checked" kind="action" w=220 h=40 d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="Two skills feed the builder role: the job note and the product's design. The result is a page with one clear next step, checked on a phone and in dark mode." caption="The builder loads the job check and your design on every screen card. Whichever brain works the role, the page comes out looking like yours, with one clear next step." svg=s %}

## What happens without asking

- **New builder roles get both skills.** The Chief gives them to any role that builds screens, and builder roles from a pack arrive with them.
- **Both skills are in the HeyStax library,** so any account can copy them.
- **The dashboard's own pull requests are checked.** A screen change without its job note and its phone and dark screenshots fails the check.

## What stays yours

- **You set the look.** The design skill is yours, versioned, and private to your account. Fix it once when a page comes out wrong, and every builder moves to the new version.
- **You can check.** Every screen card says which skills ran, so you can see whether the job note was written before the page was built.

Now you can hand any builder a screen and get back a page that knows what it is for.

**Read next:** [Teach your roles skills](./) · [Have your Chief make skills](../chief/make-skills)
