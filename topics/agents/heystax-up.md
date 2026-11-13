---
title: Start every builder with one command
parent: AI Integrations (MCP)
nav_order: 9
---

# Start every builder with one command

{% include badge-partial.html %}

`heystax up` connects every builder role you own to this computer. You sign in once in the browser. You paste no key.

## Why it matters to you

Friday, 18:00. You have three stax, each with a builder. Before, that was three keys, three folders, three `connect` runs and three services. Now it is one command, and you can close the laptop knowing which builders are listening.

## How to do it

1. **Install the command once.** It is not on npm yet, so build it from the HeyStax repo: `cd cli && npm i && npm run build && npm link`. Check with `heystax --version` (0.5.1 or later).
2. **Run `heystax up`.** Your browser opens HeyStax. If it does not, open the link it prints.
3. **Sign in and approve.** The page lists the builder roles this computer will run. Press **Approve**.
4. **Read the table.** One line per builder: stax, builder, folder, status. **listening** means it is waiting for cards.

## What it does for each builder

- **The folder.** It uses `~/projects/code/<repo>`, the stax's GitHub repo. If the folder is missing, it clones it. A stax with no repo gets an empty folder, and the builder's card "Create the repo" fixes that.
- **The key.** It saves the builder's own key in that folder, readable only by you. The key is never printed.
- **The listener.** It installs one listener per folder, so cards run while you are away.
- **The plugin.** If Claude Code is on this computer, it adds the HeyStax plugin.
- **Linger.** If your computer needs one `sudo` line so listeners keep running after you log out, it prints that line. Run it once.

Running `heystax up` again is safe. You get the same folders and the same workers, with new keys.

## When a listener goes wrong

A listener fixes the common breaks itself:

- **Its launcher was revoked.** It registers a new one and carries on, with no restart. The log says "the launcher was revoked; registered a new one and carried on".
- **Its role was taken off the stax.** It joins the stax once and tries again.

When it cannot fix the break itself, it tells you on the board. The builder's chip on the stax page says **Down** or **Restarting**. Hover over it to see why and the one step that fixes it, for example "run heystax up". A listener that fails to start three times in ten minutes reports it once, not on every try.

You can check that it is your listener. The chip shows when it started listening, and every card it takes is signed as the builder role, not as you.

## Coming next

{% include badge-planned.html %}

`npx heystax up`, with nothing to build first, once the command is on npm.
