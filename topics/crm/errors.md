---
title: When the CRM says no
parent: Run outreach with the CRM
nav_order: 4
---

# When the CRM says no

Every refusal names a code. Here is what each one means and what to do.

| Code | Means | Do this |
|---|---|---|
| `HELD` | You put a hold on this | Read the instruction. Only you clear it |
| `SUPPRESSED` | On the do-not-contact list | Don't send. Moving campaign never lifts it |
| `ADDRESS_INVALID` | A bounce or a check marked this address bad | Reach the organisation another way |
| `COOLDOWN` | This organisation was touched recently | Wait until the time it gives |
| `CAP` / `CAMPAIGN_CAP` | The mailbox or campaign hit today's limit | Wait, or you raise the limit |
| `CAMPAIGN_NOT_RUNNING` | The campaign is draft, paused or done | Set it running first |
| `WINDOW_CLOSED` | The campaign's send window has passed | Follow-ups only for 14 days. Only you extend it |
| `LAUNCH_NOT_APPROVED` | Launch approval is on and this launch waits for you | Approve it in [Launches](launch-review.html) |
| `GATE_FAILED` | The bot's own message check failed | Fix the draft |
| `RESERVATION_REQUIRED` | A bot recorded a send with no reservation | Reserve before every send |
| `UNKNOWN_RECIPIENT` / `NOT_A_MEMBER` | The address isn't imported or isn't in the campaign | Import it, or add it to the campaign |
| `ILLEGAL_STAGE_TRANSITION` | That stage move isn't allowed | See [the stage table](daily-work.html#stages) |
| `RECORD_STALE` | Someone changed it since the bot read it | Read again, then decide |
| `REQUEST_ID_REUSED` | Same request id, different content | Use a fresh request id |
| `IMPORT_ITEM_<n>` | Item n in the batch is invalid | Fix that item and resend the batch |
| `ANGLE_DEAD` / `ANGLE_NOT_LIVE` / `ANGLE_CAMPAIGN_MISMATCH` | The angle is retired, not tested yet, or from another campaign | Pick a testing or winning angle in this campaign |
| `QC_SELF_REVIEW` | A sender tried to review its own send | Another role, worker or you reviews it |

Now you can read a refusal and know the next move without asking.
