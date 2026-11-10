---
title: Work the queue
parent: Run outreach with the CRM
nav_order: 3
---

# Work the queue

Each run, the bot starts from two queues: replies to handle, then follow-ups due. Nobody has to remember who said "try us in spring".

## Why it matters to you

A reply never sits unread because the bot was busy with new sends. The queues come from the record, so a new bot picks up exactly where the last one stopped.

## The queues

| Ask | Returns |
|---|---|
| `crm_query` view `unresolved_replies` | Every reply or "not now" newer than its last handling |
| `crm_query` view `due_follow_ups` | Every follow-up due, soonest first. Do-not-contact targets are left out |
| `crm_query` view `counts` | Prospects by campaign, angle and stage, and messages by kind |
| `crm_identity_lookup` | One organisation across all your stax: who holds it, last touch, cooldown, suppressions and holds |

## Stages

A reply is a message, not a stage. The bot moves the stage itself with `crm_stage_move`.

| From | Can move to |
|---|---|
| new | researched, contacted, lost |
| researched | contacted, lost |
| contacted | engaged, lost |
| engaged | demo booked, lost |
| demo booked | engaged, pilot, won, lost |
| pilot | won, lost |
| lost | researched |
| won | stays won |

- A product question is engaged, never demo booked.
- No reply is never lost by itself.
- Each move needs the revision the bot last read. If someone else moved it first, the bot re-reads and decides again.

## Angles

An angle starts as testing. It becomes a winner or dead with `crm_angle_status_set`. Dead is final, but its sends and replies still count. Results are never typed in. `counts` works them out from what happened.

Now you can open one stax and see which angle is working, what is waiting, and who needs an answer.
