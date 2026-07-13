---
name: senior-se
jtbd:
  - surface: se-frontdoor-slack-channel
    time_budget: 30 seconds per redirect
    job: Deflect "quick question" pings by redirecting askers to the front door without the answer quality dropping
    acceptance: Weekly ping volume drops against the pre-pilot baseline within 4 weeks, and no redirected question comes back with a wrong cited answer they must correct
---

# Persona — Senior SE (the deflection target and the adoption engine)

One of the 2–3 people who hold the tribal knowledge. Today they are the search engine: "quick question" pings arrive all day, each costing context-switch time. They feel the pain the metric measures — which is why the grill (2026-07-09) recorded that they'd **champion** the pilot, not merely tolerate it.

## Role in the pilot

- **Baseline**: their current weekly ping volume is captured before go-live; the deflection metric is meaningless without it.
- **Redirect behavior**: answering a ping with "ask the bot first, then come back to me" is the single highest-leverage adoption behavior in the pilot.
- **Quality backstop**: when the bot surfaces conflicting docs (surface-both-and-flag rule), this persona is the natural adjudicator — and each conflict flag hands them a doc-hygiene fix.

## What kills it for this persona

Redirecting a colleague to a bot that answers wrong costs the senior credibility twice — once for the redirect, once for the correction. The acceptance criterion therefore pairs volume drop with zero uncorrected wrong answers on redirected questions.
