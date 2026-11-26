---
title: Have your Chief make skills
parent: Set up your Chief of Staff
nav_order: 5
---

# Have your Chief make skills

{% include badge-planned.html %}

You say which role needs to get better at what. Your Chief picks the kind of skill, a builder writes it, and the role starts using it. You never run a script.

## Why it matters to you

Monday, 09:10. You correct the CFO's draft for the third time this month, the same way. That correction is a skill waiting to be written.

You should not be the one writing it. You give the direction. The Chief spots the pattern, gathers the proof and gets it built. Swap the brain in the seat next month and the method stays.

## The kind decides the route

| Kind | Triggered by | Written by | Lands in |
|---|---|---|---|
| **House** | A new standing rule of yours | A builder, from the Chief's card | The house skill every role loads |
| **Craft** | A builder tripping on the same step twice | That repo's builder | The repo the work is in |
| **Expertise** | "Give the CFO a tax method", or repeated corrections | A builder, from the Chief's card | The skill library, then a line in the role's brief |
| **Context** | Figures, people, deadlines | Nobody | Cards, notes and dates on your stax. Never a skill |

More on each kind: [Keep method in skills, facts on the stax](../agents/four-kinds-of-skill).

## How it will work

1. **You ask, or the Chief spots it.** One line on a card, or the same correction twice on a role's cards.
2. **The Chief picks the kind.** Facts go straight onto the stax as cards.
3. **The Chief gathers proof.** A card or PR link for every rule. No rule a model guessed.
4. **A builder writes it.** It runs `new-skill.sh`, writes the method with a "Why:" on each step, runs `build-catalog.ts` and opens a pull request.
5. **The Chief merges it** when the checks pass.
6. **The role adds one line** to its brief, from a card the Chief files. House changes skip this: every role already loads the house skill.
7. **The Chief checks it helps.** Five cards with the skill, five without. If it does not help, it gets smaller or goes.

The skill tools in step 4 are on main today. What is still coming is the Chief taking these steps on its own.

<figure>
<div style="overflow-x:auto">
<svg viewBox="0 0 720 150" role="img" aria-label="You ask, the Chief picks the kind and files a card, a builder writes the skill, the Chief merges it, the role adds a brief line and records which skill it used" style="width:100%;min-width:560px;height:auto;font-family:system-ui,sans-serif">
  <g font-size="13" text-anchor="middle">
    <rect x="10" y="40" width="100" height="56" rx="10" fill="#FFF3D9" stroke="#B97800" stroke-width="2"/>
    <text x="60" y="66" fill="#121C2B" font-weight="600">You</text><text x="60" y="84" fill="#5D6878">ask in one line</text>
    <rect x="150" y="40" width="120" height="56" rx="10" fill="#E3E9FF" stroke="#2B50E6" stroke-width="2"/>
    <text x="210" y="66" fill="#121C2B" font-weight="600">Chief</text><text x="210" y="84" fill="#5D6878">kind + proof</text>
    <rect x="310" y="40" width="120" height="56" rx="10" fill="#E3E9FF" stroke="#2B50E6" stroke-width="2"/>
    <text x="370" y="66" fill="#121C2B" font-weight="600">Builder</text><text x="370" y="84" fill="#5D6878">writes, opens PR</text>
    <rect x="470" y="40" width="100" height="56" rx="10" fill="#E3E9FF" stroke="#2B50E6" stroke-width="2"/>
    <text x="520" y="66" fill="#121C2B" font-weight="600">Chief</text><text x="520" y="84" fill="#5D6878">merges</text>
    <rect x="610" y="40" width="100" height="56" rx="10" fill="#FFFFFF" stroke="#121C2B" stroke-width="2"/>
    <text x="660" y="66" fill="#121C2B" font-weight="600">The role</text><text x="660" y="84" fill="#5D6878">loads it</text>
    <g stroke="#121C2B" stroke-width="2" fill="none"><path d="M110 68 H146"/><path d="M270 68 H306"/><path d="M430 68 H466"/><path d="M570 68 H606"/></g>
    <text x="360" y="128" fill="#5D6878">Context never enters a skill: it stays on your stax as cards and dates.</text>
  </g>
</svg>
</div>
<figcaption>You ask once. The Chief picks the kind and gathers proof, a builder writes the skill and opens a pull request, the Chief merges it, and the role adds one brief line and records which skill it used.</figcaption>
</figure>

Now you can teach a role by saying what it should get better at, and leave the making to your Chief.

**Read next:** [Build roles, not agents](../roles/) · [Give a role a skill](../agents/give-a-role-a-skill) · [Your Chief's standing brief](standing-brief)
