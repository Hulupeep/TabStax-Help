---
title: Hey CLI Guide
parent: Hey CLI
nav_order: 1
---

# Catch a thought from your terminal

`hey` is the HeyStax command line. One line adds a next action to the stax you are in, without leaving your terminal.

```bash
hey "check rate limits on /api/users"
```

## Why it matters to you

You are mid-debug and a thought surfaces. In three seconds it is either written down or gone. `hey` writes it down where your head already is, and you go back to the bug.

The action is in your stax, not in the terminal. It shows in the dashboard, the TabStax extension and any AI app connected to HeyStax.

## How to do it

1. **Install:** `npm i heystax-cli`. The command is `hey`.
2. **Log in:** `hey login`. No account yet? Start at [dash.heystax.ai](https://dash.heystax.ai).
3. **Pick a stax:** `hey use "Client Portal"`. Names match loosely, so `hey use "portal"` works.
4. **Add a next action:** `hey "fix the invoice PDF bug"`.
5. **Leave a trail of what you did:** `hey -x "fixed the OAuth callback"`.
6. **See and finish:** `hey ls`, then `hey done 1`.

## Command reference

| Command | What it does |
|---|---|
| `hey "text"` | Add a next action to the current stax |
| `hey -x "text"` | Add a breadcrumb: something you did |
| `hey -p "stax" "text"` | Add to another stax |
| `hey ls` | Actions in the current stax |
| `hey ls stax` | All your stax, by priority |
| `hey ls --done` | Breadcrumbs only |
| `hey done 3` | Finish action 3 (`hey done` finishes the first) |
| `hey rm 2` | Remove action 2 without finishing it |
| `hey edit 1 "new text"` | Change action 1 |
| `hey mv 3 1` | Move action 3 to the top |
| `hey use "stax"` | Switch the current stax |
| `hey which` | Show the current stax |
| `hey pri "stax" must` | Set priority: `must`, `should`, `good` or `meh` |
| `hey login` · `hey logout` · `hey whoami` · `hey status` | Sign in and check who you are |

## Seven open actions per stax

`hey` warns when a stax already has seven open actions. Finish one, remove one, or add anyway with `--force`. A short list keeps the next move obvious.

## Let your AI read it too

An AI assistant that can run commands can run `hey ls stax` and `hey ls`. It then sees your stax and your next actions, and it can add or finish them for you. Tell it once:

```
I track next actions in HeyStax. Run 'hey ls stax' to see my stax,
'hey ls' for actions, and 'hey done 1' to finish one.
```

## When it goes wrong

| You see | Do this |
|---|---|
| Not logged in | `hey login` |
| Project not found | `hey ls stax`, then `hey use` with the exact name |
| Limit reached | `hey done 1`, `hey rm 3`, or add with `--force` |
| Actions not syncing | `hey status` shows who you are logged in as |

Workers that pick up cards on their own use a separate command, `heystax`. See [Connect a worker to a role](agents/connect-a-worker).

Now you can catch a thought in one line and find it later in every place you work.

**Links:** [HeyStax dashboard](https://dash.heystax.ai) · [TabStax extension](https://chromewebstore.google.com/detail/heystax/gfdcobncoohhlhppmoidalociahfdcam) · [npm package](https://www.npmjs.com/package/heystax-cli)
