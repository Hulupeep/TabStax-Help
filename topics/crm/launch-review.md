---
title: Review what each launch sent
parent: Run outreach with the CRM
nav_order: 7
---

# Review what each launch sent

A launch is one page or feature a role shipped at one audience. Launch review shows each one on a card: what it is, why it was built, who it is for, the links, and who it went to.

## Why it matters to you

It is 07:40 and your bots sent 34 emails to tour boat operators overnight. You did not approve them, and you should not have to. You want one screen that says what went out, to whom, and what came back.

## How to do it

1. Open **Launches** from the goal board or the CRM header. Each campaign card also has a **Launch review** link.
2. Pick a stax, such as Hubduck · Sell. The launches that need a look come first.
3. Read the card: the state and why, such as "34 of 37 sent. 1 replied".
4. Open a launch. You see what, why, who, why it is worth doing, and the ask.
5. Check the links to the landing page and the feature.
6. Read the ads and blog verdicts. Each one says yes, no, test only or later, and why.
7. Filter the send list by sent, not sent, replied, bounced or suppressed. A row that was not sent says why.

Sends go ahead by default. Nothing waits for you. If a launch looks wrong, press **Pause sends**. That sets your hold on the campaign. **Resume sends** clears it.

## Check the first few, then let go

You can choose to see a launch before its first email goes. Set it once per stax, at the top of Launches or on the stax's CRM Campaigns page.

1. Pick **Launch approval**: off, approve every new launch, or approve the first few.
2. For the first few, set how many, such as 3. Press **Save**.
3. A new launch shows **Needs your approval**. Its email draft, landing page and feature link sit on one screen.
4. Press **Approve** when the three match. Sends start.

Your approval covers that copy, that page and that link. If a role changes any of them, the launch waits for you again. Launches that already sent keep sending. Once you have approved the first few, new launches go on their own.

A slot the role has not filled says so, such as "Landing page: Not set by @hubduck-marketing". You see the gap before anyone gets the email.

## What the role writes

The role that ran the launch writes the brief with `crm_campaign_launch_set`: what, why, worth, ask, when to stop, the feature link, the email copy, and the ads and blog verdicts. A field it has not written yet is named on the card, so you can see the gap.

The counts come from the message history, never from the role. Signups and payments show as "?" until they are credited to a campaign. They never show as 0.

## For bots

`launch_review` reads the same cards over MCP, with a stax id and an optional campaign id for the send list. A send for a launch that waits for the owner is refused with `LAUNCH_NOT_APPROVED`. The bot posts one line with the launch review link and moves on.

Now you can see everything a role shipped, and who it reached, without being the one who approved it.
