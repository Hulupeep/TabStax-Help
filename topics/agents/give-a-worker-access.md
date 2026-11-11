---
title: Give a worker what it needs
parent: AI Integrations (MCP)
nav_order: 11
---

# Give a worker what it needs

A worker can only use what its folder has been given. You choose each kind of access once, per folder, and nothing else.

## Why it matters to you

Gaia replies to a bug in Telegram. The card lands on your builder at 16:00. If the builder cannot see the data, it guesses, or it stops with "can't reproduce". You lose the afternoon.

Your Claude may be signed in to everything. A worker running on its own with nobody watching is not. That is on purpose: you set the edges, so a card at 03:00 cannot change production.

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

Use a staging database. Better still, a login that can only read. Never point a worker at a database that holds real patient or customer records.

## Coming next

{% include badge-planned.html %} `heystax access` will list what a worker in a folder can reach, with the fix for each gap. The worker will run it before it starts, and when a card needs something missing it will come back blocked with that fix instead of a guess.

Now you can hand a bug to a builder and get a verdict that comes from your data, not a guess.

**Read next:** [Connect a worker to a role](connect-a-worker) · [Hand a bug to an agent](../team-stax/hand-a-bug-to-an-agent)
