---
title: Business development
parent: Start from a template
nav_order: 1
---

# A business development team of bots

A business development stax finds the right organisations, learns what matters to each one, tests angles, and sends within your limits. The template for it is coming {% include badge-planned.html %}. You can build the same team by hand today.

## Why it matters to you

One bot doing everything forgets which school said "not now", repeats a dead angle, and emails the same principal twice. Four roles with clear jobs, one shared CRM and hard send limits keep it honest. Hubduck runs this way.

## The team

| Role | Its job | Main tools |
|---|---|---|
| `@<product>-research` | Finds target organisations and records what matters about each: size, who decides, timing, local hooks. Every fact with its source link | `crm_import` |
| `@<product>-angles` | Writes angles with a hook, a hypothesis and a stop condition. Retires the ones that fail | `crm_angle_upsert`, `crm_query` counts |
| `@<product>-outreach` | Drafts and sends, one reserved email at a time. Handles replies and follow-ups | `crm_send_reserve`, `crm_message_event_add`, `crm_stage_move` |
| `@<product>-qc` | Reviews sampled sends. Never its own | `crm_qc_review` |

Your Chief of Staff staffs the roles, reads the counts and comes to you only for a yes.

## Build it by hand today

1. **Make the stax** for one market, with its mission and one goal you can count, such as "25 paying schools by 30 January".
2. **Set up your Chief** on it. See [Set up your Chief of Staff](../chief/).
3. **Ask the Chief to create the four roles** with `role_create`, each with a brief from the table above.
4. **Give outreach the do-not-contact list** with your own token: `crm_suppression_grant` with `suppression_read` and `suppression_add`.
5. **Set your limits** with your own token, or keep the defaults: 30 sends per mailbox per day, 7 days between touches of one organisation.
6. **Create the campaign and first angles**, then import. See [Set up a campaign](../crm/setup.html).
7. **Connect a worker to each role**: a hosted bot such as Grok Bot, or `heystax connect` in a folder {% include badge-partial.html %}.

## What the template will add

> **Coming next.** One step instead of seven: the roles and briefs, the campaign, the send limits and the standing cards (weekly angle review, follow-ups due, replies to handle) in place. Tracked as tabstax#1168.

Now you can stand up a business development team today and swap in the template when it ships.
