---
title: Give a worker what it needs
parent: AI Integrations (MCP)
nav_order: 11
---

# Give a worker what it needs

{% include badge-partial.html %}

A worker uses only what its folder has been given. You choose each kind of access once, per folder.

## Why it matters to you

Gaia replies to a bug in Telegram. The card lands on your builder at 16:00. If the builder cannot see the data, it guesses, or stops with "can't reproduce".

Your Claude may be signed in to everything. A worker running alone is not, on purpose. You set the edges, so a card at 03:00 cannot change production.

## What a worker can reach

| Access | How you give it | Today |
|---|---|---|
| Code | Connect the repo folder | Works |
| Branch and pull request | `gh auth login` on that computer, and a remote called origin | Works |
| Data (any Postgres: Supabase, Neon, RDS) | `heystax db set-read-url` in the folder | Works, read only |
| Logs and deploys (Vercel, Railway) | Paste the log lines into the card | Not given to workers yet |

## How to give it data

1. `cd` into the worker's folder.
2. Run `heystax db set-read-url` on its own line.
3. In a repo linked to Supabase it shows the database and asks only for the password. Otherwise paste the `postgres://` address. Neither is shown on screen.
4. Restart the listener: `systemctl --user restart 'heystax-listen-*'`.
5. Check it: `heystax db read "select now()"` prints one row.

Use a staging database, ideally with a read-only login. Never point a worker at real patient or customer records.

## Check what a worker can reach

Run `heystax access` in the folder. It lists code, branch and pull request, data, and logs, with the fix for each gap. `heystax status` and `heystax listen --install` show the same list.

The worker runs it before it starts. A card that needs something missing comes back blocked with that fix, not a guess.

Now you can hand a bug to a builder and get a verdict that comes from your data, not a guess.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Hand a bug to an agent](../team-stax/hand-a-bug-to-an-agent)
