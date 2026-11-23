---
title: What's new
nav_order: 1.8
---

# What's new in HeyStax

Every change you can feel, newest first, in one line: what changed, and so that what.

## Why it matters to you

Gaia has not read a release note in her life. On Monday, 08:55, she has ten seconds before her first call. This page is one line per change, and each line says what it does for her.

You never hunt through pull requests to learn what changed.

## The list

{% for c in site.data.whats_new %}
- **{{ c.date | date: "%-d %b" }}.** {{ c.change }}, so that {{ c.so_that }}.{% if c.try %} *Try:* {{ c.try }}{% endif %}{% if c.help %} [More]({{ site.baseurl }}/{{ c.help }}){% endif %}
{% endfor %}

## Add a line

A change goes on this list on the day it goes live, never before. Edit `_data/whats_new.yml` in the help repo: the date, the change, the so that, who it is for, and the pull requests that shipped it.

Now you can see what moved in HeyStax this fortnight in one minute.
