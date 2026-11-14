---
title: Run outreach with the CRM
nav_order: 4
has_children: true
---

# Run outreach with the CRM

The CRM keeps every organisation you contact, every campaign and angle, and every email sent or received. It lives in your HeyStax account, so any bot you connect works from the same record.

## Why it matters to you

A bot that sends emails from its own memory will email the same school twice, forget an opt-out, and lose the reply that said "try us in spring". Here the record outlives the bot. Swap Grok Bot for another bot and the history, the do-not-contact list and the limits stay.

## Watch it work

<iframe id="hs-crm-anim" src="{{ '/assets/anim/crm.html' | relative_url }}" title="Animation: a bot imports prospects, reserves before each send, is refused when a school opted out or the cap is reached, handles a reply, and you hold all sends" loading="lazy" style="width:100%;height:720px;border:0;display:block"></iframe>
<script>addEventListener('message',function(e){if(e.data&&e.data.hsCrmHeight){var f=document.getElementById('hs-crm-anim');if(f)f.style.height=(e.data.hsCrmHeight+4)+'px';}});</script>

*Six short scenes. A bot loads the do-not-contact list, then imports 200 schools with no duplicates. Before each email it reserves a send, and the check runs your holds, the do-not-contact list, a 7-day cooldown per school and 30 sends per mailbox per day. A refusal means do not send. A reply is recorded and queued, and the bot moves the stage itself. You can hold every send with your own token. Angles are judged on counted results, and a losing angle is retired.*

## The parts

| Part | What it holds |
|---|---|
| **Organisation** | One school or company, keyed by its official number, such as a school roll number. Its emails, handles and contacts hang off it |
| **Campaign** | A goal and an audience, such as "Irish primary schools, 2026". Draft, running, paused or done |
| **Angle** | One line of attack inside a campaign: the hook, why it should work, the proof, and when to stop |
| **Membership** | One organisation in one campaign: its stage, angle and next follow-up |
| **Message history** | Every send, reply, bounce and opt-out. It can't be edited, and it never moves a stage by itself |
| **Do-not-contact list** | Account-wide. One opt-out covers every campaign and every stax |
| **Send limits** | Your holds, a cooldown per organisation, a cap per mailbox per day |

## In this section

1. [Set up a campaign](setup.html): the stax, the bot's key, the do-not-contact list, the import.
2. [Send safely](sending.html): reserve, send, record, and what you control.
3. [Work the queue](daily-work.html): follow-ups, replies, stages and counts.
4. [When the CRM says no](errors.html): every refusal and the fix.
5. [Reach people on every channel](channels.html): X, LinkedIn, GitHub, Discord, phone and more.
6. [Run many client stax](coach-board.html): one ranked list of the clients that need a push.

Now you can let a bot run outreach for weeks and still know who was contacted, why, and what they said.
