---
title: Roles
nav_order: 2.6
has_children: true
---

# Build roles, not agents

A **role** is a seat on your org chart. It has a job, limits and a record. Any agent can take the seat: Claude today, Grok tomorrow, a person on Friday. The role tells it how to be.

## Why it matters to you

First we built lots of agents, each with its own bag of tricks. Then one general agent learned to load the right skill when it needs it. That fixed the crowd. It did not say what the agent is for, what it must never touch, or who checks.

Bob swaps his tax bot for a cheaper one in March. The new one starts on Monday with the same job, the same red lines and every draft the last one left. Nobody re-explains anything.

<figure>
  <img src="{{ '/assets/images/build-roles.png' | relative_url }}" alt="Three panels. The old way: three agents, each carrying its own skills. One agent, many skills: one general agent loads the skill it needs. Build roles: a CFO seat on the Taxes 24 stax, with its job, its limits and its record. Claude, Grok or a person can take the seat. House, craft, expertise and context skills plug into it." style="max-width:100%;height:auto;border-radius:12px">
  <figcaption>A skill is what it knows. A role is what it answers for. The CFO seat on Taxes 24 has a job (least legal tax, on time), limits (never sends, never touches Xero or filings, Tom signs off) and a record (every draft lands on a card). Any brain can sit in it. The skills plug in.</figcaption>
</figure>

## Skill or role?

| | A skill | A role |
|---|---|---|
| Answers | How do I do this? | What am I for, and who checks? |
| Lives in | A `SKILL.md` file, plain text | Your stax: the role's brief, its access and its cards |
| Travels | To any company, any runtime | Stays with your work. The brain in it changes |
| Can say no | No. A model can skip a rule in a file | Yes. Its access is checked outside the model |

## The three parts of a seat

1. **Job.** The outcome the role is accountable for, in its brief. "Least legal tax, on time."
2. **Limits.** The Never rules and what it does not handle. These sit outside the model: the role's key lists only the tools for its job, and work that cannot be undone waits for a go-ahead from you or your Chief.
3. **Record.** Every claim, draft and result lands on a card, signed by the role and the worker that did it.

Skills plug into the seat. There are four kinds: **house**, **craft**, **expertise** and **context**. [Keep method in skills, facts on the stax](../agents/four-kinds-of-skill).

## How to do it

1. **[Hire the role](../agents/role-packs).** One call sets up a team of roles, each with a job and Never rules.
2. **[Say what it does not handle](../agents/does-not-handle),** so look-alike work goes to the right seat.
3. **[Give it a skill](../agents/give-a-role-a-skill).** One line in its brief points at the method.
4. **[Put a brain in the seat](../agents/connect-a-worker).** Claude Code, Codex, Grok Bot or a person.
5. **[Watch the record](../agents/see-who-is-working).** Who did what, in your name.

Walk it end to end with one role: [Build the CFO role and its skill](cfo-example).

Now you can swap the agent and keep the role.
