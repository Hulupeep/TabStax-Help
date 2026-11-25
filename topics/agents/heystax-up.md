---
title: Start every builder with one command
parent: AI Integrations (MCP)
nav_order: 9
---

# Start every builder with one command

{% include badge-partial.html %}

`heystax up` connects every builder role you own to this computer. You sign in once in the browser. You paste no key.

## Why it matters to you

Friday, 18:00. Three stax, three builders. That used to mean three keys, three folders and three `connect` runs. Now it is one command, and you close the laptop knowing which builders are listening.

## How to do it

1. **Install the command once.** It is not on npm yet, so build it from the HeyStax repo: `cd cli && npm i && npm run build && npm link`. Check with `heystax --version` (0.5.1 or later).
2. **Run `heystax up`.** Your browser opens HeyStax. If it does not, open the link it prints.
3. **Sign in and approve.** The page lists the builder roles this computer will run. Press **Approve**.
4. **Read the table.** One line per builder: stax, builder, folder, status. **listening** means it is waiting for cards.

{% capture s %}
{% include anim/node.html x=100 y=40 label="heystax up" sub="one command" kind="surface" w=150 %}
{% include anim/edge.html x1=175 y1=40 x2=250 y2=40 kind="dispatch" d=0.5 %}
{% include anim/node.html x=340 y=40 label="Your browser" sub="sign in, Approve" kind="person" w=170 d=0.8 %}
{% include anim/edge.html x1=300 y1=66 x2=85 y2=124 kind="write" d=1.4 %}
{% include anim/edge.html x1=340 y1=66 x2=240 y2=124 kind="write" d=1.6 %}
{% include anim/edge.html x1=380 y1=66 x2=395 y2=124 kind="write" d=1.8 %}
{% include anim/node.html x=85 y=150 label="@shop-builder" sub="folder, key, listener" kind="agent" w=150 d=2.2 %}
{% include anim/node.html x=240 y=150 label="@site-builder" sub="folder, key, listener" kind="agent" w=150 d=2.4 %}
{% include anim/node.html x=395 y=150 label="@app-builder" sub="folder, key, listener" kind="agent" w=150 d=2.6 %}
{% include anim/trail.html x=20 y=214 when="18:00" who="you" what="heystax up, Approve" d=3.0 %}
{% include anim/trail.html x=20 y=238 when="18:01" who="3 builders" agent="true" what="listening for cards" d=3.4 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 260" label="heystax up: one command opens your browser, you sign in and approve, and each builder role gets its folder, its own key and a listener" caption="You run heystax up and approve once in the browser. Each builder you own gets its folder, its own key and a listener. The table then shows all three as listening." svg=s %}

## What it does for each builder

- **The folder.** It uses `~/projects/code/<repo>`, the stax's GitHub repo. If the folder is missing, it clones it. A stax with no repo gets an empty folder, and the builder's card "Create the repo" fixes that.
- **The key.** It saves the builder's own key in that folder, readable only by you. The key is never printed.
- **The listener.** It installs one listener per folder, so cards run while you are away.
- **The plugin.** If Claude Code is on this computer, it adds the HeyStax plugin.
- **Linger.** If your computer needs one `sudo` line so listeners keep running after you log out, it prints that line. Run it once.

Running it again is safe: same folders, same workers, new keys.

## When a listener goes wrong

A listener fixes the common breaks itself:

- **Its launcher was revoked.** It registers a new one and carries on, with no restart. The log says "the launcher was revoked; registered a new one and carried on".
- **Its role was taken off the stax.** It joins the stax once and tries again.

When it cannot fix the break, the builder's chip on the stax page says **Down** or **Restarting**. Hover over it to see why and the one step that fixes it, such as "run heystax up". Three failed starts in ten minutes are reported once, not on every try.

You can check that it is your listener. The chip shows when it started listening, and every card it takes is signed as the builder role, not as you.

## Coming next

{% include badge-planned.html %}

`npx heystax up`, with nothing to build first, once the command is on npm.

{% include badge-planned.html %} **Scheduled roles will get a nightly run.** A role your Chief registers as Scheduled, on Claude Code or Codex, will come back from the same sign-in. It will get its own empty folder, never a clone, and a run once a night at 02:30 or the time you pick with `--at`, not a listener. It will read, report and file cards, and it will never write files, run git or open a pull request. The Chief makes the role. Your next `heystax up` runs it. ([#1390](https://github.com/Hulupeep/tabstax/issues/1390))

Now you can start every builder you own with one sign-in, and see which ones are listening.
