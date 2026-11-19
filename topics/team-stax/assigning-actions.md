---
title: Assigning Actions to Team Members
parent: Team Stax
nav_order: 1
---

[← Back to Help Home](/)

# <img src="../../icons/tabstax-32.png" alt="HeyStax" width="32" height="32" style="vertical-align: middle; margin-right: 10px;">Assign an action with @handle

Type `@handle` in a next action on a shared stax and it goes to that person.

## Why it helps

You and Rob look at the same list. Without names on it, nobody knows who is doing what. With `@rob`, the action leaves your column and lands in his. No meeting, no Slack message.

## How to do it

1. Open a shared stax (one with collaborators).
2. Type the action with a mention: `Review the DNS config @rob`.
3. A blue **Assigning to @rob** badge appears under the input.
4. Press **Enter**.

The action moves to Rob's column and reads "Review the DNS config". He sees it in his **Mine** filter. You stay its creator; he is its assignee.

## Where it works

The same badge and result on every surface that adds a next action:

| Surface | Where you type |
|---|---|
| TabStax extension | Next action input in the popup |
| Dashboard swim lanes | Action input in any column |
| [Board](stax-board) | The add box at the foot of any column |
| Dashboard compact card | Action input on the card |

## Rules

| Rule | Detail |
|---|---|
| Collaborators only | Anyone else gets *"@handle is not a collaborator on this stax"*. |
| First mention wins | With several `@` mentions, only the first assigns. |
| Shared stax only | On a solo stax, `@handle` is plain text. |

Now you can hand work to a teammate without leaving the stax you are in.

---

**Related guides:**
- [Team Stax](./): overview of shared stax
- [Dashboard](../surfaces/dashboard): swim lanes and team views
- [Account & Sync](../account-sync): what collaboration needs
