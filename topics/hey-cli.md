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

You are mid-debug and a thought surfaces. In three seconds it is either written down or gone. `hey` writes it down, and you go back to the bug.

{% capture s %}
{% include anim/node.html x=240 y=36 label='hey "check rate limits"' sub="your terminal" kind="surface" w=220 %}
{% include anim/edge.html x1=240 y1=62 x2=240 y2=118 kind="write" d=0.5 %}
{% include anim/plane.html x=20 y=96 w=440 h=76 label="Client Portal stax" d=0.2 %}
{% include anim/node.html x=240 y=146 label="check rate limits" sub="next action" kind="action" w=170 d=1.0 %}
{% include anim/edge.html x1=200 y1=172 x2=85 y2=210 kind="read" d=1.6 %}
{% include anim/edge.html x1=240 y1=172 x2=240 y2=210 kind="read" d=1.8 %}
{% include anim/edge.html x1=280 y1=172 x2=395 y2=210 kind="read" d=2.0 %}
{% include anim/node.html x=85 y=230 label="Dashboard" kind="surface" w=130 d=2.2 %}
{% include anim/node.html x=240 y=230 label="TabStax" kind="surface" w=130 d=2.4 %}
{% include anim/node.html x=395 y=230 label="Your AI app" kind="surface" w=130 d=2.6 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 260" label="One hey line writes a next action into your stax, and the dashboard, the TabStax extension and your AI app all read it from there" caption="You type one line. The next action lands in your stax, not in the terminal. The dashboard, the TabStax extension and any AI app connected to HeyStax all show it." svg=s %}

## How to do it

1. **Install:** `npm i heystax-cli`. The command is `hey`.
2. **Log in:** `hey login`. No account yet? Start at [dash.heystax.ai](https://dash.heystax.ai).
3. **Pick a stax:** `hey use "Client Portal"`. Names match loosely, so `hey use "portal"` works.
4. **Add a next action:** `hey "fix the invoice PDF bug"`.
5. **See and finish:** `hey ls`, then `hey done 1`.

## Command reference

| Command | What it does |
|---|---|
| `hey "text"` | Add a next action to the current stax |
| `hey "text @ana"` | Add it and assign it to @ana |
| `hey -u "text"` | Add it as urgent (`--now` works too) |
| `hey -x "text"` | Add a breadcrumb: something you did |
| `hey -p "stax" "text"` | Add to another stax |
| `hey -s "New stax"` | Make a stax and switch to it |
| `hey ls` | Actions in the current stax |
| `hey ls stax` | All your stax, by priority |
| `hey ls --done` | Breadcrumbs only |
| `hey done 3` | Finish action 3 (`hey done` finishes the first) |
| `hey rm 2` | Remove action 2 without finishing it |
| `hey edit 1 "new text"` | Change action 1 |
| `hey mv 3 1` | Move action 3 to the top |
| `hey use "stax"` · `hey which` | Switch the current stax, or show it |
| `hey pri "stax" must` | Set priority: `must`, `should`, `good` or `meh` |
| `hey login` · `hey logout` · `hey whoami` · `hey status` | Sign in and check who you are |

## Seven open actions per stax

On a stax only you work on, `hey` stops at seven open actions. Finish one, remove one, or add anyway with `--force`. A short list keeps the next move obvious. A shared stax has no cap.

## When it goes wrong

| You see | Do this |
|---|---|
| Not logged in, or session expired | `hey login` |
| Project not found | `hey ls stax`, then `hey use` with the exact name |
| Limit reached | `hey done 1`, `hey rm 3`, or add with `--force` |
| Actions land in the wrong account | `hey whoami` shows who you are logged in as |

Workers that pick up cards on their own use a separate command, `heystax`. See [Connect a worker to a role](agents/connect-a-worker).

Now you can catch a thought in one line and find it later in every place you work.

**Links:** [HeyStax dashboard](https://dash.heystax.ai) · [TabStax extension](https://chromewebstore.google.com/detail/heystax/gfdcobncoohhlhppmoidalociahfdcam) · [npm package](https://www.npmjs.com/package/heystax-cli)
