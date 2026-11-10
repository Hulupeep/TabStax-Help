---
title: Set up a campaign
parent: Run outreach with the CRM
nav_order: 1
---

# Set up a campaign

One stax per market holds the campaign, for example **Hubduck Business Development** for Irish schools. The bot works in that stax with its own key.

## Why it matters to you

Every record the bot writes carries its name. If a send looks wrong, you can see which role and which worker made it.

## Before the bot starts

1. **Give the bot its own key** and grant it the stax with `access: full`. See [Set up your Chief of Staff](../chief/). Then the bot joins the stax.
2. **Let it use the do-not-contact list.** With your own token: `crm_suppression_grant` for its handle, with `suppression_read` and `suppression_add`.
3. **Load the do-not-contact list first.** Every known opt-out, bounce and "never again" goes in with `crm_suppression_add`, before the first import.
4. **Create the campaign** with `crm_campaign_upsert`: a key such as `hubduck-ie-2026`, a name, the goal and the audience. Only a running campaign takes new prospects.
5. **Add angles** with `crm_angle_upsert`: the hook, the hypothesis, the proof, the cost, the downside and a stop condition such as "fewer than 2 replies in 25 sends".
6. **Import prospects** with `crm_import`, up to 200 at a time. Each organisation is keyed by country, kind of number and number, such as `IE:roll_number:12345A`.

## Import rules worth knowing

- Send a fresh `request_id` with each batch. A retry with the same one returns the stored result, so a timeout never imports twice.
- Importing the same schools again updates them. It never makes duplicates.
- An email that already belongs to another organisation is never moved.
- One bad item fails the whole batch and names the item, such as `IMPORT_ITEM_3`.
- An import never changes an existing stage.

## Paste this into the outreach bot

```text
You run outreach on HeyStax stax <stax id>, campaign <campaign key>.
- Use only the HeyStax CRM tools. Never keep prospects or history in your own memory.
- Before the first import, add every known opt-out and bounce with crm_suppression_add.
- Import with crm_import, a fresh request_id per batch.
- Before every email: crm_send_reserve. Refused? Do not send. Read the reason.
- After every email: crm_message_event_add kind sent, with the reservation_id.
- Every run: crm_query unresolved_replies, then due_follow_ups. Move stages with crm_stage_move.
- After each mailbox scan: crm_send_reconcile, then crm_scan_report.
- Retire an angle when its stop condition is met. Write what you learned on the campaign.
```

Now you can hand a market to a bot and know the ground rules are in the system, not in its head.
