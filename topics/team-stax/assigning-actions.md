---
title: Assigning Actions to Team Members
parent: Team Stax
nav_order: 1
---

[← Back to Help Home](/)

# <img src="../../icons/tabstax-32.png" alt="HeyStax" width="32" height="32" style="vertical-align: middle; margin-right: 10px;">Assigning Actions to Team Members

## Why this helps

When you're working in a shared Stax, typing `@handle` in your next action assigns it to that person. They see it in their column. You see it leave yours. No meetings, no messages — just clear delegation.

This is what turns a shared workspace into shared responsibility. Without it, you and your collaborators are looking at the same list but nobody knows who's doing what. With `@handle`, every action has a name on it.

---

## How to assign an action

1. Open a **shared Stax** (any Stax with collaborators).
2. Type your action with an `@` mention — for example: `Review the DNS config @rob`
3. As you type, a blue **"Assigning to @rob"** badge appears below the input to confirm the assignment.
4. Press **Enter**.

The action moves to @rob's column. The `@rob` part is stripped from the displayed text — so the action reads cleanly as "Review the DNS config" in their view.

---

## What happens after you assign

- The action appears in the **assignee's swim lane**, not yours.
- They see it immediately in their **"Mine" filter** on the dashboard.
- You remain the **creator** of the action. They become the **assignee**.
- The action text is stored without the `@handle` — clean display, no clutter.

---

## Where this works

Assignment with `@handle` works everywhere you can add a next action to a shared Stax:

| Surface | Input location |
|---|---|
| **TabStax extension** | Next action input in the popup |
| **Dashboard — Swim lane view** | Action input in any column |
| **Dashboard — Expanded list** | Action input in the expanded list |
| **Dashboard — Compact card** | Action input on the compact card |

Same behaviour, same blue badge, same result — regardless of which surface you're using.

---

## Rules to know

| Rule | Detail |
|---|---|
| **Must be a collaborator** | The `@handle` must belong to someone who's already a collaborator on the Stax. If they're not, you'll see: *"@handle is not a collaborator on this stax"* |
| **First mention wins** | If you type multiple `@` mentions, only the **first** one is used for assignment |
| **Handle is stripped** | The `@handle` text is removed from the stored action — the action displays without it |
| **Works on shared Stax only** | On a solo Stax with no collaborators, `@handle` is treated as plain text |

---

## Now you can...

Delegate work inside a shared Stax without leaving the context you're in. Type the action, tag the person, move on. They see it in their column. You see it leave yours. No back-and-forth, no "can you check on that thing I mentioned in Slack." The Stax is the single source of truth for who's doing what.

---

**Related guides:**
- [Team Stax](./) — overview of collaborative workspaces
- [Dashboard](../surfaces/dashboard) — where swim lanes and team views live
- [What is a Stax?](../what_is_a_stax) — the core concept behind everything
- [Account & Sync](../account-sync) — free vs Pro and what collaboration requires
