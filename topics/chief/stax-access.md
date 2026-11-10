---
title: Let it work on your stax
parent: Set up your Chief of Staff
nav_order: 2
---

# Let your Chief work on your stax

{% include badge-partial.html %}

A new key can't see anything. You grant it each stax it should run, once per stax.

## Why it matters to you

You set the edges. The Chief works on the stax you name and nowhere else. You can take any stax back in one call.

## Grant it

Paste this into the same AI app you used to make the key:

```text
List my stax. For each stax I name, call agent_authorize for chief-of-staff
with access full, manage_roles true, go_ahead true.
Then tell me which stax it can now work on.
```

## What each grant gives

| Grant | The Chief can |
|---|---|
| `access: full` | Read and write the stax: next actions, goals, people, records |
| `manage_roles: true` | Create up to 10 roles on that stax with `role_create`. Never with more access than it has |
| `go_ahead: true` | Clear irreversible work that someone else proposed. Never its own, never work assigned to it |

Want a quieter Chief? Use `access: work` and leave `go_ahead` off. Irreversible work then waits for you.

## New stax

A grant covers one stax. When you make a new stax, grant it again.

## Take it back

Ask your app to call `agent_deauthorize` for chief-of-staff on that stax. Its open claims there are released. Roles it created on that stax stop with it.

Now you can hand a stax to your Chief and know exactly where its reach ends.
