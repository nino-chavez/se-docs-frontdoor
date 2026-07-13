---
name: se-researcher
jtbd:
  - surface: se-frontdoor-slack-channel
    time_budget: 5 minutes, async (not mid-call)
    job: Get a correct, source-cited answer to a client-solution question without pinging a senior SE
    acceptance: Receives an answer with at least one deep-linked citation the SE can open and verify, within 5 minutes of asking, for 8 of 10 real pilot questions
---

# Persona — SE researcher

The core user: a commerce.com sales engineer assembling a client solution. Mid-ramp to experienced; knows the product but not where every fact lives. Today their research loop is: search Confluence, search Drive, scroll Slack, give up, ping a senior.

## Context from the grill (2026-07-09)

- Asks **async research questions** — minutes are acceptable; mid-call speed is explicitly a v2 concern.
- Wants **lookup first** ("what's our SLA for X", "does the platform support Y"), synthesis later. The winning v1 output is a paragraph plus a deep link, not a generated deliverable.
- Uniform access: everything the front door can see, this persona can already open — so a citation link always resolves for them.
- Trust behavior: one confidently-wrong answer forwarded toward a client resets their usage to zero; the authority-tier label (official doc / team doc / Slack thread) and the conflict flag exist for this persona's verification step.

## What kills adoption for this persona

Stale answers presented confidently, citations that don't resolve, and answers slower than just pinging the senior anyway. The acceptance criterion above is written against all three.
