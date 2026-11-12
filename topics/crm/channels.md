---
title: Reach people on every channel
parent: Run outreach with the CRM
nav_order: 5
---

# Reach people on every channel

{% include badge-partial.html %}

An address in the CRM can be an email or a channel handle: X, LinkedIn, GitHub, Bluesky, Discord, Telegram, WhatsApp, a phone number, a contact page. Paste the profile link and HeyStax keeps the handle.

## Why it matters to you

Jane at Acme never answers email. She answers DMs on X within the hour. If the CRM only knows her inbox, your bot keeps knocking on the one door she ignores.

Now the record holds every door, and the same rules guard each one. An opt-out on LinkedIn is an opt-out. A DM on X counts toward the cooldown, so Jane is not hit on three channels in one afternoon.

## How to do it

1. **Import the handles** with the contact. Paste profile links or write `channel:handle`:
   `https://x.com/JaneAcme`, `linkedin.com/in/jane-acme`, `github:janeacme`, `discord:jane.acme`.
2. **Reserve before a DM**, exactly as for email. The sending account is your handle, such as `x:heystaxai`.
3. **Send one message**, then **record it** with the reservation id.
4. **Record an opt-out** on the handle it came from. That handle goes on the do-not-contact list.
5. **Pick the channel from the queue.** Each follow-up carries a reach list: every address of the organisation and its channel, the contact's own first.

## What it accepts

| You write | HeyStax keeps |
|---|---|
| `https://x.com/JaneAcme`, `twitter.com/janeacme`, `x:@JaneAcme` | `x:janeacme` |
| `https://www.linkedin.com/in/jane-acme/` | `linkedin:in/jane-acme` |
| `https://github.com/JaneAcme` | `github:janeacme` |
| `bsky.app/profile/jane.bsky.social`, `bluesky:@jane` | `bluesky:jane.bsky.social` |
| `t.me/jane_acme` | `telegram:jane_acme` |
| `discord:Jane.Acme` | `discord:jane.acme` |
| `phone:+353 87 123 4567`, `wa.me/353871234567` | `phone:+353871234567`, `whatsapp:+353871234567` |
| `https://acmehooks.io/contact` | `web:acmehooks.io/contact` |
| `jane@acmehooks.io` | `jane@acmehooks.io` |

Also: Mastodon, Threads, Instagram, Facebook, TikTok, YouTube, Reddit, Hacker News, Indie Hackers, Product Hunt and Signal.

The same handle written two ways is one address, so a second import adds nothing. A handle that breaks the channel's rules is refused with the rule, such as "1 to 15 letters, digits or _" for X.

## The rules that follow every channel

| Rule | On a channel handle |
|---|---|
| Do-not-contact list | An opt-out on a handle suppresses that handle, account-wide |
| Cooldown | One touch per organisation per 7 days, whichever channel it was on |
| Daily cap | 30 messages per sending account per 24 hours, counted per handle |
| Your holds | Stop every channel at once |

Coming next: the production database change. Until it is applied, the CRM accepts email only.

Now you can let a bot reach Jane where she answers, and still know every message it sent in your name.
