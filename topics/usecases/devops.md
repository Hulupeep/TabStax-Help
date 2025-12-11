# DevOps Responding to a Production Incident

[← Back to Use Cases](index.md)

---

PagerDuty goes off.

For this type of incident, you usually need:

* Grafana / Datadog dashboards
* Logs
* Deployment pipeline
* Feature flag console
* Runbook doc
* Incident Slack/Teams channel

## Without TabStax

You burn 5–10 minutes just spinning everything up and pasting links around.

## With TabStax

You already prepared **"P1 – Web Latency / Errors"** Stax:

* All relevant dashboards with the right filters
* The runbook opened at the exact section
* CI/CD panel
* Comms channel

You hit **Open Stax → "P1 – Web Latency / Errors"** and you're in the cockpit.

You **share that Stax in the incident channel**:

* On-call devs and managers click the same link.
* Everyone instantly sees the same dashboards and runbook instructions — no "please share link?" spam.

**Outcome:** Context switching from "regular work" to "incident mode" is a single action, not an adrenaline-fuelled scavenger hunt.

---

[← Back to Use Cases](index.md)
