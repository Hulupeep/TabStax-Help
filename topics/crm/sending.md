---
title: Send safely
parent: Run outreach with the CRM
nav_order: 2
---

# Send safely

Every email goes through three steps: reserve, send one email, record it. There is no approval step. Within your limits the bot sends on its own. Outside them it can't.

## Why it matters to you

You don't review 400 drafts. You set the limits once, and HeyStax refuses anything outside them, whichever bot is sending.

## The three steps

1. **Reserve** with `crm_send_reserve`: the address, the campaign and the mailbox it sends from. A reservation lasts 15 minutes by default.
2. **Send** exactly one email.
3. **Record** it with `crm_message_event_add`, kind `sent`, with the reservation id and the mailbox's message and thread ids. A bot's send without a reservation is refused.

Decided not to send? `crm_send_release` frees the reservation, so it stops counting.

## What the reservation checks, in order

| Check | Refusal | Default |
|---|---|---|
| Your holds | `HELD` | none |
| Do-not-contact list | `SUPPRESSED` | |
| Campaign is running | `CAMPAIGN_NOT_RUNNING` | |
| The bot's own message check, if it sends one | `GATE_FAILED` | |
| One touch per organisation, across every campaign and stax | `COOLDOWN` | 7 days |
| Sends per mailbox in 24 hours, across everything | `CAP` | 30 |
| Sends per campaign in 24 hours | `CAMPAIGN_CAP` | none |

A refusal means do not send. Cooldowns and caps come back with when to try again.

## What only you control

With your own token. A bot's key is refused.

- **Limits:** `crm_send_limits_set` per stax, campaign or mailbox. Set a cap to 0 to stop a mailbox.
- **Holds:** `crm_hold_set` on everything, a stax, a campaign or one organisation. Open reservations are cancelled at once. Write your reason and your exact instruction; the bot reads both. Only you clear it, with `crm_hold_clear`.

## Checking after the fact

- **QC sample:** 1 send in 10 is sampled by default. Another role, another worker or you review it with `crm_qc_review`. The sender can't review its own.
- **Mailbox scan:** the bot matches what really went out with `crm_send_reconcile`. A send with no reservation still counts toward caps, and only you can resolve it.
- **Scan report:** `crm_scan_report` after every scan. The goal board treats "no replies" as unknown unless a scan is under 48 hours old.

Now you can set the rules once and let the bot send without waiting on you.
