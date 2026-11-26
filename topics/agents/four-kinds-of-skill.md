---
title: Keep method in skills, facts on the stax
parent: AI Integrations (MCP)
nav_order: 18
---

# Keep method in skills, facts on the stax

A **role** is the seat: its job, its limits and its record. A **skill** is the know-how the role's worker loads to do that job. There are four kinds. Three are know-how in files: House, Craft and Expertise. The fourth, Context, is facts, and facts never go in a file. They sit on your stax.

## Why it matters to you

Bob wrote one long file for his tax bot. The red lines, the year-end checklist, and his own figures, his accountant's name and ten open items, all in one place.

Then a figure changed. Then Bob wanted the same method for a second company. The file was wrong in one place and private in another.

Split it. The CFO know-how becomes an expertise skill that works for any company. The figures stay on Bob's stax, where they change without anyone touching the method.

## The four kinds

| Kind | Holds | Example | Lives in |
|---|---|---|---|
| **House** | How every role behaves | Write back so a person can act, never send as you, say what you do not handle | The HeyStax skill library, for every role |
| **Craft** | How to do a type of work | A release checklist, a test method | The repo the work happens in |
| **Expertise** | The judgement of a profession | A micro-company CFO, a cold caller, a blog in your voice | The skill library, versioned, linked from the role's brief |
| **Context** | Facts about this case | Figures, people, open items, deadlines | **Your stax**: cards, notes and dates |

A skill holds method, never facts. A rule a model guessed doesn't go in either. Each rule in a skill says why it exists.

## How to do it

1. **Split the file.** Method goes in a `SKILL.md`. Every figure, name and open item becomes a card or a date on the stax.
2. **Start from the template.** {% include badge-planned.html %} Once tabstax#1415 merges, the tabstax repo will have: `scripts/skills/new-skill.sh cold-call-phone expertise "phone calls to a named list"`.
3. **Write the method.** Steps, each with a "Why:". End with a `## Record` step.
4. **Check it.** {% include badge-planned.html %} `scripts/skills/build-catalog.ts` will refuse a skill that holds an email address, a tax number, a key or a five-figure euro amount.
5. **Point the role at it.** Add one line to the role's brief, under its Skills section:

```text
Skills (load each at the start of a run; this brief wins if they disagree):
- Load heystax-house@1.0.0 (house): https://github.com/Hulupeep/tabstax/tree/main/skills/heystax-house
- Load flout-cfo-tax-cutter@1.0.0 (expertise): https://github.com/Hulupeep/tabstax/tree/main/skills/flout-cfo-tax-cutter
```

6. **Ask for the record.** The worker ends its note with `Skill used: flout-cfo-tax-cutter@1.0.0`, so you can see which method ran.

Brief instructions and report notes are free text, so steps 5 and 6 work on any role today.

{% capture s %}
{% include anim/node.html x=110 y=40 label="Expertise skill" sub="method, versioned" kind="record" w=150 d=0.2 %}
{% include anim/node.html x=370 y=40 label="Your stax" sub="facts, cards, dates" kind="record" w=150 d=0.5 %}
{% include anim/edge.html x1=110 y1=66 x2=240 y2=130 d=1.0 %}
{% include anim/edge.html x1=370 y1=66 x2=240 y2=130 kind="write" d=1.2 %}
{% include anim/node.html x=240 y=154 label="@acme-cfo" sub="any brain" kind="agent" w=150 d=1.5 %}
{% include anim/edge.html x1=240 y1=180 x2=240 y2=220 d=2.0 %}
{% include anim/node.html x=240 y=244 label="Draft for the accountant" sub="Skill used: cfo@1.0.0" kind="action" w=200 h=40 d=2.3 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 280" label="An expertise skill and the stax's facts both feed the role's worker, which leaves a draft with a Skill used line" caption="The expertise skill holds the method and travels to any company. Your stax holds the figures, people and deadlines. The worker reads both, leaves a draft on the card, and says which version of the method it used." svg=s %}

## Skills in the library

| Skill | For |
|---|---|
| `heystax-house` | Every role: start from HeyStax, facts on the stax, write back, route, ask first |
| `flout-cfo-tax-cutter` | An Irish micro-company CFO. Drafts for the accountant, never files |
| `colm-voice-blog` | A blog post in the founder's voice, with every AI tell cut |
| `colm-voice-social` | Short, rough social posts and DMs that sound typed on a phone |
| `cold-call-phone` | Call sheets and logging for calls a person makes to a named list |
| `sales-call` | From discovery to a paid-pilot ask, with scored feedback |
| `rule-page-writer` | One landing page per rule a buyer must meet |

## Coming next

{% include badge-planned.html %} **Every role will get the house skill on its own.** Pack briefs will list it, and the work packet will carry a skills list: the house skill first, then the ones the brief names.

{% include badge-planned.html %} **Workers will record it for you.** `skills_used` on a report will write the Skill used lines onto the card.

{% include badge-planned.html %} **A skill library page.** dash.heystax.ai/skills will list every skill with a line to copy into a brief, and Agent access will show each role's skills next to its job.

{% include badge-planned.html %} **Role packs will carry skills.** A micro-company CFO pack will hire one CFO role with its expertise skill already linked.

Now you can keep a profession's method in one versioned file, keep your own figures on your stax, and see which method each card used.

**Read next:** [Build roles, not agents](../roles/) · [Give a role a skill](give-a-role-a-skill) · [Say what a role does not handle](does-not-handle)
