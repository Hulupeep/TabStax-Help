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

1. **Hire the role.** He [sets up a role](../agents/role-packs) called `@taxes24-cfo` on the stax, with its job and its Never rules.
2. **Build the expertise skill.** {% include badge-planned.html %} Once tabstax#1415 merges, he will start from the template in the tabstax repo:

   ```bash
   scripts/skills/new-skill.sh flout-cfo-tax-cutter expertise "an Irish micro-company CFO"
   ```

   He writes the method as steps, each with a "Why:", and ends with a `## Record` step.
3. **Keep the facts out.** Figures, Tom's name and the open items become cards and dates on `Taxes 24`. {% include badge-planned.html %} The catalog check will refuse a skill that holds an email address, a tax number, a key or a five-figure euro amount.
4. **Point the seat at its skills.** Two lines in the brief, under its Skills section:

   ```text
   - Load heystax-house@1.0.0 (house): https://github.com/Hulupeep/tabstax/tree/main/skills/heystax-house
   - Load flout-cfo-tax-cutter@1.0.0 (expertise): https://github.com/Hulupeep/tabstax/tree/main/skills/flout-cfo-tax-cutter
   ```

5. **Put a brain in the seat.** He [connects a worker](../agents/connect-a-worker) to `@taxes24-cfo`. Claude Code today. Something cheaper next month.
6. **Read the record.** The worker leaves a draft for Tom on the card and ends its note with `Skill used: flout-cfo-tax-cutter@1.0.0`.

The full rules for each kind of skill are on [Keep method in skills, facts on the stax](../agents/four-kinds-of-skill).

## Where the limits hold

The skill tells the brain how. It cannot stop the brain. The seat can:

- The role's key lists only the tools for its job. A CFO seat has no send tool to reach for.
- Work that cannot be undone waits for a go-ahead from Bob, or from a Chief he granted `go_ahead`.
- Every write is signed by `@taxes24-cfo` and the worker that made it. Bob can check.

## Coming next

{% include badge-planned.html %} **A CFO pack.** Hiring a micro-company CFO from a pack will set up the seat with its expertise skill already linked.

{% include badge-planned.html %} **Every seat gets the house skill on its own,** and a worker will record the skills it used for you. Today you write those lines in the brief and the note yourself.

Now you can build the seat once, swap whoever sits in it, and see which method each draft used.

**Read next:** [Build roles, not agents](./) · [Give a role a skill](../agents/give-a-role-a-skill) · [Say what a role does not handle](../agents/does-not-handle)
