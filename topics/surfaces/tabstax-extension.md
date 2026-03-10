---
title: TabStax — the browser surface
parent: Surfaces
nav_order: 1
---

# TabStax — the browser surface

TabStax is the Chrome extension that gives HeyStax a home in your browser.

When you're working on a project, your browser holds part of that context: the tabs you have open are the tools and resources for that work. TabStax captures that — by name, with all its tabs — so you can close it, walk away, and restore it exactly later.

That's the browser-specific problem TabStax solves: **your tabs are your workspace, and workspaces shouldn't need to be rebuilt from scratch every session.**

## What TabStax does

- **Save** — capture the current set of open tabs as a named Stax
- **Restore** — open all tabs for a Stax in one click, exactly as they were
- **Surface next actions** — see what to do next on any project without switching to the dashboard
- **Switch contexts** — move between projects without losing either one

TabStax is the entry point most people use when they first encounter HeyStax. Install it, save a tab group as a Stax, and you've already started.

## How it connects to the rest of HeyStax

TabStax is one surface in the system, not the whole product.

When you save a Stax in the extension, that Stax exists on every other surface too. The next actions you add in the popup appear in the dashboard and the CLI. The tabs you save are visible on the share page. If you've connected an AI via MCP, it can read and update that same Stax through conversation.

The extension is where a lot of re-entry happens — you click the icon, see your projects, open the right one — but the Stax itself lives in HeyStax, not in your browser.

## The browser context problem specifically

Browsers are stateless by design. When you close a window, the state is gone. Tab restore features help, but they restore everything — not *this project's* tabs, now, on demand.

TabStax makes your browser context durable and named. Instead of a pile of windows and tabs that mean something only while they're open, you have named project workspaces you can close and reopen without losing the thread.

This is what the original "reconstruction tax" looks like in a browser: reopen 7 tabs, sign back into two of them, find the doc you had open, remember what you were looking at. TabStax collapses that to one click.

## Installing TabStax

TabStax is available on the Chrome Web Store. It works in Chrome, Edge, and Brave.

→ [Get TabStax from the Chrome Web Store](https://chromewebstore.google.com/detail/heystax/gfdcobncoohhlhppmoidalociahfdcam)
→ [First time opening TabStax](../first_time_opening_tabstax) — what you'll see after installing
→ [Using the main popup](../using_the_main_popup) — navigating next actions and your Stax list
