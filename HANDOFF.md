# Handoff — se-docs-frontdoor

**Last session**: 2026-07-09 (founding session: definition → research → grill → scaffold → Stage 1 closed)
**Position**: Stage 1 → Stage 2 boundary, gates green.

## State

- Decision: configure-first (ADR-0001) — Claude Tag pilot in one SE channel; thin-build contingent behind four named triggers; buy retired. Read-only v1 is a hard line.
- Stage 1 closed against gates: research-completeness / pilot-profile-lock / persona-fit PASS; sibling-scan + reference-grade artifacts written (both PASS); cost-gate + terminology at WARN only.
- Remaining reviewer BLOCKs are stage-pending (DESIGN.md, serve.sh/@smoke, REPLACE_FOR_PROJECT portal files, forge-provenance surface check) or Pattern-B misfires on this Pattern-A initiative. None are Stage 1 defects.
- SE-team share brief: `docs/se-team-brief.html`, published at https://claude.ai/code/artifact/211c9b72-cf2e-42b9-a3e5-72d69629609d
- Full research corpus + 16-question grill ledger: `research/sources/definition-and-grill-2026-07-09.md`

## Next (Stage 2 — Design Principles, then pilot protocol)

1. Formalize grill commitments into `prototype/DESIGN.md`: authority-tier labels, surface-both-conflicts, citations-always, current-stable version pin, read-only. Clears `design-principles-reviewer`.
2. Author the Claude Tag channel instruction set (renders DESIGN.md into Tag per-channel instructions).
3. Pilot protocol artifact for surface `se-frontdoor-slack-channel` (clears forge-provenance `JTBD_LACKS_SURFACE`): three tests — Shared-Drive visibility (claude-code#53442), label/conflict-flag adequacy, citation quality — plus corpus census.
4. Measurement plan: capture senior-SE ping baseline BEFORE go-live; recruit the 2-3 seniors ("ask the bot first" redirect).
5. Human dependencies at commerce: Claude Enterprise admin (Drive/Slack connector toggles + pilot channel), senior SEs.

## Gotchas for the next session

- Reviewer runner is NOT stamped into initiatives: run `node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs` from this root.
- Persona JTBDs must stay in list shape (`jtbd:` then `- surface: ...`) — forge-provenance parses only that shape.
- Portal-chrome-canonical reports TEMPLATE_MISSING against the methodology repo itself — possible upstream blueprint issue; consider a methodology amendment when next in `tools/blueprint`.
- Git repo initialized; remote is `git@github.com:nino-chavez/se-docs-frontdoor.git` (private). Worktree rule applies to any multi-session work.
