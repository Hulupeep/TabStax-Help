---
title: Build the CFO role and its skill
parent: Roles
nav_order: 1
---

# Build the CFO role and its skill

One role, end to end. Bob runs a small company. Tax season is close, and he wants a CFO seat on his `Taxes 24` stax that any brain can fill.

## Why it matters to you

Bob's last tax bot kept everything in one long chat. When the chat scrolled away, so did the red lines. This time the job and the limits sit on the stax, the method sits in a skill, and the figures sit on cards.

## The seat

| Part | What Bob writes | Where it lives |
|---|---|---|
| Job | Least legal tax, on time | The role's brief |
| Limits | Never sends. Never touches Xero or filings. Tom, the accountant, signs off | Never rules and Does NOT handle, in the brief and the owner's boundaries |
| Record | Every draft lands on a card | The cards on `Taxes 24` |

## How Bob builds it

Bob gives directions. His Chief of Staff does the rest.

1. **Hire the role.** He [sets up a role](../agents/role-packs) called `@taxes24-cfo` on the stax, with its job and its Never rules.
2. **Ask the Chief for the skill.** One card to the [Chief](../chief/): "Give the CFO a method for cutting tax legally." The Chief checks the library first, then writes the method in Bob's account as steps with a "Why:" each.
3. **HeyStax checks it.** A skill that holds an email address, a tax number, a key or a five-figure euro amount is refused on save.
4. **Facts stay on the stax.** Figures, Tom's name and the open items are cards and dates on `Taxes 24`, never in the skill.
5. **The seat gets its skills.** The Chief gives the skill to `@taxes24-cfo`. Its next card carries the house skill, then `cfo-tax-cutter`. Bob sees both on [dash.heystax.ai/skills](https://dash.heystax.ai/skills).
6. **Put a brain in the seat.** A worker is [connected](../agents/connect-a-worker) to `@taxes24-cfo`. Claude Code today. Something cheaper next month.
7. **Read the record.** The worker leaves a draft for Tom on the card and ends its note with `Skill used: cfo-tax-cutter@1.0.0`.

The full rules for each kind of skill are on [Keep method in skills, facts on the stax](../agents/four-kinds-of-skill).

## Where the limits hold

The skill tells the brain how. It cannot stop the brain. The seat can:

- The role's key lists only the tools for its job. A CFO seat has no send tool to reach for.
- Work that cannot be undone waits for a go-ahead from Bob, or from a Chief he granted `go_ahead`.
- Every write is signed by `@taxes24-cfo` and the worker that made it. Bob can check.

## Shortcuts that work today

- **The CFO pack.** The `micro-company-cfo` [role pack](../agents/role-packs) hires a CFO role in one call. Ask the Chief for its skill straight after.
- **The house skill comes free.** Every worker gets its skills with each card: the house skill first, then the ones given to its role.
- **The record writes itself.** A worker passes `skills_used` when it reports, and the Skill used line lands on the card.
- **The library.** [dash.heystax.ai/skills](https://dash.heystax.ai/skills) lists every skill with a brief line to copy.

Now you can ask for a seat and its skill in one line, swap whoever sits in it, and see which method each draft used.

**Read next:** [Build roles, not agents](./) · [Give a role a skill](../agents/give-a-role-a-skill) · [Say what a role does not handle](../agents/does-not-handle)
