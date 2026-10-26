---
title: Consultant returns to agent work
parent: Scenarios
nav_order: 3
---

# A consultant returns to a worker's blocked action

{% include badge-partial.html %}

Alex is a fractional CTO preparing one client's release. He owns a **Pilot release** Stax with the repo, goal and two Next Actions. Claude Code has claimed “Check the migration rollback plan.” Alex has to work elsewhere for four days.

## The return

1. Before Alex leaves, Claude Code reports **blocked** on its action: “The rollback script needs the old index name.” Its claim and question stay on Pilot release.
2. Four days later, Alex opens the Stax. The action is still open. He can see who owns it and what is missing without reading an old chat.
3. Alex starts Claude Code again and says: “Check your open work on Pilot release. Use the blocked note to continue; ask me if the index name is still unclear.” The worker can use `agent_whoami` for its open claims, then read the Stax and action. It did not run while offline.
4. Alex supplies the index name. Claude Code checks the repo with its own coding tools and reports **done** with the rollback commit link. Alex reviews that proof before using it in a release.

{% include agent-action-flow.html start="Check the rollback plan" middle="@claude claims it" blocker="Old index name is missing" end="Rollback commit link is reported" caption="Four days later, Alex finds the open claim and exact blocker on the Stax, then explicitly starts the worker again." %}

## What remains on Pilot release

Alex can answer three questions immediately: the old index name blocked the rollback check, Claude Code holds the claim, and he should ask it to continue after he supplies that name. [The earlier consultant example](../usecases/consultant) explains switching client tabs; this scene explains returning to unfinished agent work.

## What persists

The Stax keeps the action, claim and short notes. It does **not** import Claude's private conversation memory. If Alex replaces Claude with a different worker, the claim does not automatically transfer.

| Step | State |
|---|---|
| Alex reopens the Stax and reads open actions | Existing HeyStax capability. |
| The worker checks its own claims and reports with its identity | Deployed MCP pilot; **Partial** until [live release evidence](../../docs/evidence/agent-peers-2026-10-26) includes the full journey. |
| The worker edits the repo and supplies a commit link | Its separate coding tools do that. HeyStax holds the result. |

{% include badge-planned.html %}

Background wake-up, stall alerts and automatic transfer to another AI identity are **planned**. This scene uses one owner-owned Stax; it does not promise confidential per-client agent grants.

## Try the verified part

Add a clear rollback action to a test Stax and ask your existing connected AI to summarise what remains. Return to that Stax later and check whether the question still makes sense. The worker's own claim is still a pilot step pending live verification.

**Your cognition stays yours:** Alex returns to a named question and a named worker, without hoping that a private AI chat remembers his week.
