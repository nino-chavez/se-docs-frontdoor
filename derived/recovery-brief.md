# se-docs-frontdoor — recovery brief

Derived 2026-07-27T21:35:12.880Z at commit `a145fcb` — rerun `npm run derive` to refresh; never hand-edit.

## Where things stand — manifest verdict: PENDING

Open (PENDING is not green):
- [R2-lifecycle] outcome pilot-sponsor.decide-pilot is served only by sponsor-decision-brief(draft), pilot-protocol(planned), measurement-plan(planned), decision-memo(draft) — PENDING, not green
- [R2-lifecycle] outcome sales-engineer.get-cited-answer is served only by slack-frontdoor(planned) — PENDING, not green
- [R2-lifecycle] outcome senior-se.redirect-pings is served only by slack-frontdoor(planned), pilot-protocol(planned) — PENDING, not green
- [R6-preconds] precondition deflection-baseline unmet (research/pilot/baseline-pings.md missing) — slack-frontdoor may not advance to ready/issued until it exists

## Recent movement (git)

- docs: restructure the problem statement so it reads without lookups
- fix: correct a hardened paraphrase, and refresh stale handoff state
- feat: author the decision memo — Stage 5 deliverable, 0 reviewer blocks
- feat: switch to research variant; reviewer blocks 6 -> 1
- feat: Stage 1 personas/JTBD artifact + close two real reviewer findings

## Outputs

- slack-frontdoor (configured-surface, planned) → sales-engineer.get-cited-answer, senior-se.redirect-pings
- sponsor-decision-brief (view, draft) → pilot-sponsor.decide-pilot
- pilot-protocol (view, planned) → pilot-sponsor.decide-pilot, senior-se.redirect-pings
- measurement-plan (view, planned) → pilot-sponsor.decide-pilot
- decision-memo (view, draft) → pilot-sponsor.decide-pilot
- recovery-brief (recovery-brief, ready) → maintainer.recover-context

## The account (canonical truth)

- decisions: `decisions/` (1 entries)
- research: `research/sources/` (2 entries)
- demand: `research/sources/knowledge-database-kickoff-2026-07-27.md`
- state: `HANDOFF.md`

## Decisions

- `decisions/0001-configure-first-pilot-as-prototype.md` — ADR-0001 — Configure-first: the Stage 2 "prototype" is a Claude Tag pilot protocol, not code
