---
title: Asks that don't wait, and done that is checked
parent: AI Integrations (MCP)
nav_order: 15
---

# Asks that don't wait, and done that is checked

A bot that needs a decision asks with a recommendation and carries on if you don't answer. A bot that says "done" on a card with a check isn't believed until HeyStax checks it.

## Why it matters to you

Tuesday, 14:00. You are in a meeting. Your marketing role asks "21 to 50 staff schools first?" Before, it stopped and waited until you saw it. By evening the day was gone.

Now it says what it would do, and when. If you're busy, the work goes on. If you disagree later, your answer reaches it as a correction.

## Asks with a default

1. The role asks on the card, with 2 to 4 options and the one it recommends.
2. If nobody answers in time, 4 hours unless it says otherwise, HeyStax takes the recommended option. The card notes it, signed by HeyStax, not you: "No answer by 18:00: proceed with 'Yes, 21 to 50 first' (recommended)."
3. A step that can't be undone never goes ahead on silence. It waits for your go-ahead, or your Chief's.
4. A role can't answer its own ask.
5. To stop every ask from going ahead on its own, put a hold on the stax or on all your stax. Your hold always wins.

## Done means checked

1. You, or your Chief, put a check on a card: a page that must answer, for example `https://yoursite.com/pricing` must return 200.
2. When the role reports the card done, it doesn't close. HeyStax fetches the page itself.
3. **Pass:** the card closes, with the proof (status and time).
4. **Fail:** the card reopens with the reason, such as "404 at /pricing", and the role is told what to fix. After the third fail, your Chief hears about it.
5. The role doing the work can't set or change its own check. If you mark the card done yourself, that counts, and it is noted as your call.

Checks fetch only public https pages on port 443. Never an IP address, an internal name, or a page behind a redirect.

## What works today

| Part | State |
|---|---|
| Asks with options, a recommendation and a deadline; going ahead on silence; never for a step that can't be undone | live, seen on 13 Nov 2026 |
| Buttons for an ask in Telegram | coming next |
| A page check on a card; a failed check reopens it with the reason | live, seen on 13 Nov 2026 |
