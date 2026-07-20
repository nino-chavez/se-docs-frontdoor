# se-docs-frontdoor — recovery brief

Derived 2026-07-20T17:30:16.206Z at commit `23fe38a` — rerun `npm run derive` to refresh; never hand-edit.

## Where things stand — manifest verdict: PENDING

Open (PENDING is not green):
- [R2-lifecycle] outcome sales-engineer.get-cited-answer is served only by slack-frontdoor(planned) — PENDING, not green
- [R2-lifecycle] outcome senior-se.redirect-pings is served only by slack-frontdoor(planned), pilot-protocol(planned) — PENDING, not green
- [R6-preconds] precondition deflection-baseline unmet (research/pilot/baseline-pings.md missing) — slack-frontdoor may not advance to ready/issued until it exists

## Recent movement (git)

- chore: initial commit — se-docs-frontdoor Blueprint portal

## Outputs

- slack-frontdoor (configured-surface, planned) → sales-engineer.get-cited-answer, senior-se.redirect-pings
- sponsor-decision-brief (view, ready) → pilot-sponsor.decide-pilot
- pilot-protocol (view, planned) → pilot-sponsor.decide-pilot, senior-se.redirect-pings
- measurement-plan (view, planned) → pilot-sponsor.decide-pilot
- recovery-brief (recovery-brief, ready) → maintainer.recover-context

## The account (canonical truth)

- decisions: `decisions/` (1 entries)
- research: `research/sources/` (1 entries)
- demand: `research/sources/definition-and-grill-2026-07-09.md`
- state: `HANDOFF.md`

## Decisions

- `decisions/0001-configure-first-pilot-as-prototype.md` — ADR-0001 — Configure-first: the Stage 2 "prototype" is a Claude Tag pilot protocol, not code
