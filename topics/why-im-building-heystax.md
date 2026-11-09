---
title: Why I am building HeyStax
description: Colm Byrne on useful products, commercial outcomes, and creating a living.
---

# Why I am building HeyStax

*A personal statement by Colm Byrne, founder of HeyStax.*

We've all been building with AI for a while now. Like many of you, I've built my own harness for building software. I also built HeyStax to coordinate work with people and AI agents.

It has three simple primitives: **Mission. Goal. Next Action.**

Why? Because we're doing hundreds of pull requests a month, sometimes thousands. Stories and tickets multiply too. They're too fine-grained to tell me whether I am getting where I want to go.

I spent many years coding, and about ten years in product management. With AI, I found myself building things again. I love it.

But then I asked myself: **What am I actually trying to do?**

It's not to be a better engineer. It's not to be a better product manager.

I want to build useful things, make money building useful things, support my family and earn the freedom to keep doing it.

I realised I had been optimising the part that was getting easier: building.

The hardest part was still finding individuals and businesses who needed something, establishing commercial relationships, earning trust, and getting paid.

Engineering a bridge is important. But building the bridge isn't the reason for the bridge.

Persistent AI agents have changed the possibilities. Agents can run in different environments, use different tools and work across different providers. Their mission shouldn't disappear when their provider changes.

Where models are now, I can trust them to build more and more. A site. A web app. A batch of emails to the right schools. What slows them down is waiting for me to approve the next step.

So I stop being the blocker. I give them the mission, I set the fences, and I read what they did in the morning.

{% capture s %}
<g class="hs-trail" style="--d:0s"><text x="20" y="22" class="hs-label">You approve each step</text></g>
{% include anim/node.html x=90 y=62 label="Draft ready" sub="18:10" kind="action" w=120 d=0.3 %}
{% include anim/edge.html x1=150 y1=62 x2=180 y2=62 kind="dispatch" d=0.7 %}
{% include anim/node.html x=240 y=62 label="Waiting on you" sub="all night" kind="note" w=120 d=0.9 %}
{% include anim/edge.html x1=300 y1=62 x2=330 y2=62 d=1.3 %}
{% include anim/node.html x=390 y=62 label="You, 08:00" sub="14 things waiting" kind="person" w=120 d=1.5 %}
{% include anim/trail.html x=20 y=118 when="Goal" who="Paying schools" what="no change" d=1.9 %}
<g class="hs-trail" style="--d:2.4s"><text x="20" y="162" class="hs-label">You set the mission</text></g>
{% include anim/node.html x=90 y=204 label="Site built" sub="21:00" kind="agent" w=120 d=2.7 %}
{% include anim/edge.html x1=150 y1=204 x2=180 y2=204 kind="write" d=3.1 %}
{% include anim/node.html x=240 y=204 label="40 emails sent" sub="23:30" kind="agent" w=120 d=3.3 %}
{% include anim/edge.html x1=300 y1=204 x2=330 y2=204 kind="write" d=3.7 %}
{% include anim/node.html x=390 y=204 label="2 replies" sub="06:40" kind="agent" w=120 d=3.9 %}
<g class="hs-trail" style="--d:4.3s"><text x="20" y="258" class="hs-label">Fences: 50 sends a day, opt-outs honoured, revoke any time</text></g>
{% include anim/trail.html x=20 y=284 when="08:00" who="You" what="read the night in six lines" d=4.7 %}
{% endcapture %}
{% include anim/figure.html viewbox="0 0 480 296" label="Two lanes over the same night: approving each step stalls the work, setting the mission lets it run inside fences" caption="Top lane: the worker finishes a draft at 18:10 and waits for you all night. At 08:00 fourteen things are waiting and the goal has not moved. Bottom lane: the same worker has the mission and fences. It builds a site, sends 40 emails and logs two replies before you wake. You read the trail at 08:00." svg=s %}

A worker can now wait for work and pick it up on its own as soon as it is assigned. You can pause it, or cap its runs per hour. Every step it takes is on the stax trail.

So I've started using HeyStax as an **operational plane for continuous commercial pursuit**.

Start with a product, find customers who need it, and pursue a sale. Or start with a customer problem, find a solution, deliver it and get paid. Or discover an underserved niche. Or exploit a short-lived opportunity.

Sunny day? Sell ice cream.

Whatever route we take, the question is: **Did we achieve the outcome?**

If not, what did we learn? What do we try next? Who is actually doing the work?

I don't want AI manufacturing thousands of tasks for nobody to execute. I want a system relentlessly reducing the distance between intention and result.

And personally, I want to spend less time managing the machinery and more time thinking, creating, making decisions, and being with my family.

**Not more work. More outcomes.**

That is my mission. Yours could be entirely different: building a house, getting a medicine through regulatory review, finishing a film, transforming a community. The operating principle is the same.

*This is a founder's statement of purpose. The full outcome-pursuit product is still under development; it is not being represented here as entirely shipped.*
