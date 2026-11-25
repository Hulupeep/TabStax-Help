---
title: Say what a role does not handle
parent: AI Integrations (MCP)
nav_order: 19
---

# Say what a role does not handle

A role's brief ends with a short list: work that looks like its job, but isn't, and who takes it instead.

## Why it matters to you

Monday, 08:00. A customer replies to Alice's outreach asking for a refund. Her sales bot sees a reply and starts writing back. That reply was never its call.

When the brief says "Refunds: that is @shop-orders", the bot assigns the card on and moves to its next send. You did not have to catch it.

## How to do it

1. Open the role's brief (`agent_brief_get`).
2. Add a section at the end of its instructions called **Does NOT handle:**.
3. One line per look-alike job: `- Refunds: that is @shop-orders.`
4. Name the Chief for anything no role owns yet.
5. The role saves it with `agent_brief_update`.

Instructions are free text, so this works on any brief today.

```text
Does NOT handle (assign it to that role, or to the Chief if no role fits):
- Refunds and order changes: that is @shop-orders.
- The landing page and payment link: that is @shop-builder.
- Anything that leaves the building before QC: that is @shop-qc.
```

{: .note }
> **Coming next** {% include badge-planned.html %}
> New roles will get this section by default. A role pack will list every other role in the pack by its job, and a brief saved without the section will get a one-line tip back.

You set the edges. Each role knows its own, and you can read them all in one place.

Now you can add roles without them tripping over each other's work.
