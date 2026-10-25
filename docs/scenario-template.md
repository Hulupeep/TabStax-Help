---
title: Scenario template
nav_exclude: true
search_exclude: true
---

# Scenario template

Copy this into `topics/scenarios/<slug>.md`. Keep the whole page readable in two minutes.
Check every step against `_data/ledger.yml` before you write it.

{% raw %}
```markdown
---
title: <Outcome in the reader's words, e.g. "Back after a week away">
parent: Scenarios
nav_order: <n>
scenario_state: works-today | partly | planned
---

# <Title>

<If any step is partial or planned, put the matching badge here:>
{% include badge-partial.html %}  or  {% include badge-planned.html %}

**Cast:** <people and agents, with @handles>. <The stax by name.>

## Before

Two or three sentences. The felt mess, in concrete detail. "Thirty tabs. A WhatsApp thread
from Tuesday. Nobody sure who said they'd call the yard."

## What happens

1. <Step, present tense if it works today, future tense if planned.>
2. ...
3. ...

## The graph after

<Animation include from _includes/anim/, or a real-UI clip if every step is shipped.>

<figcaption> carries the same meaning in one or two sentences of text.

## Why it holds

One cognition beat, in the reader's terms. Pick the one this scenario proves best:
it is yours, it travels, you set the edges, you can check.

## What works today

| Step | State | Note |
|---|---|---|
| <step> | works today / partly / planned | <ledger id or issue> |

## Try it

Numbered steps for the parts that work today only. Link to the how-to pages.
```
{% endraw %}

## Rules

- Real names, real objects, real times. "Bob", "the XC90", "Monday, 08:00".
- No step describes a planned capability in the present tense.
- One animation per scenario.
- End with "Try it", never with a pitch.
