# Handoff — se-docs-frontdoor

**Last session**: 2026-07-27 (kickoff ingested → problem restated → variant switched to research → Stage 1 + Stage 5 authored)
**Position**: research variant, all reviewer gates green (0 blocks). Stage 5 deliverable drafted and not yet sent.

> Read `research/problem-space/problem-statement.md` before doing anything else. It supersedes the founding framing and the `pilot_profile` block in `blueprint.yml`. Working from `blueprint.yml` alone will reproduce the old model.

## State

- **The problem changed on 2026-07-27**, not just the evidence. The founding model treated the doc corpus as a noisy given whose quality would improve as a byproduct of retrieval use. The sponsor kickoff established it as the output of a delivery process with structural truncation points — documentation stops when IPM hours run out, smaller engagements often get no folder, the template is not uniformly followed, and some documents are actively wrong where the platform shipped past documented workarounds. Capture quality bounds retrieval quality.
- **One founding decision is falsified**, not narrowed: grill row 13 (demand-driven filing) works when content exists but is misplaced, and does nothing when content was never written. This is why the founding scope cannot simply be widened.
- **ADR-0001 (configure-first) still holds**, with two qualifications now recorded in its Amendments section — the sponsor independently reached for a Claude-native surface twice, which strengthens it; and Gong is a named source outside the standard connectors, which is trigger 3 territory.
- Stage 1 research remains valid as evidence: three tracks, two adversarial verifications, the 16-question grill ledger, sibling scan, reference grade. None of it is retracted. What changed is the causal model the research was organized around.
- **Four open boundary decisions** (BD-1 read/write boundary, BD-2 audience, BD-3 whether an existing internal assistant owns this surface, BD-4 funding) are documented with owners in the problem statement. Three need the sponsor.

## Done this session (items 1–3 of the previous list)

- `pilot_profile` extracted; `walkthrough_citation` now lives in `research/personas-and-jtbd.md`.
- **Variant switched to `research` by hand, not by the stamper.** `blueprint-init` preserves an existing `blueprint.yml`/`actor-output.yml`/`reader-contract.json`/`package.json`, so re-running it changes nothing — and `copyTree()` writes `research/personas-and-jtbd.md` *unconditionally* with the blank template, so running it for real would have destroyed the Stage 1 artifact. **Do not run the stamper against this initiative.**
- Stage 1 (`research/personas-and-jtbd.md`) and Stage 5 (`docs/decision-memo.md`) authored. All reviewers green.

## Next

1. **Send the memo.** It is authored, gates green, and `status: draft` in the manifest because it has not been sent. Promote to `issued` on send. Set up the weekly sync alongside it.
2. **Chase BD-3 first among the open decisions.** If the internal "ask commerce" / CLA assistant exists, it may already hold the approvals that constitute the sponsor's entire stated two-month floor. It is the question that most changes the plan.
3. **Design Phase 0 (corpus census) concretely** — what gets counted, how, over how long. The memo promises this at the first sync. Every later decision depends on it and nobody can currently answer what fraction of real questions have an answer anywhere.
4. **Two inputs to chase that are not researchable from here**: an actual IPM to confirm `delivery-ipm/JOB-1` (flagged `implied-not-represented`), and whatever delivery already uses to record project state.
5. **Drop `apps/portal/` + `packages/`** when a memo-rendering surface replaces them. Deferred deliberately: they are scaffolding under `template/CLAUDE.md` §1 and safe to delete, but they currently carry `npm run dev`/`build` and `reader-contract.json` declares `apps/portal/dist` as a surface. Deleting before the replacement exists just leaves a broken build. `persona-fit-reviewer` WARNs `PORTAL_OVER_PROMOTED` until then, which is correct.

## Do not do these

Carried from the previous handoff and now wrong. Listed explicitly because they would each clear a greenfield gate for a pipeline being abandoned.

- ~~Formalize grill commitments into `prototype/DESIGN.md` to clear `design-principles-reviewer`~~ — greenfield Stage 2 artifact. The research variant has no DESIGN.md step, and this would re-encode the superseded model including demand-driven filing.
- ~~Author the Claude Tag channel instruction set~~ — premature. Depends on the census (which subset is trustworthy enough to serve) and on BD-2/BD-3.
- ~~Pilot protocol for surface `se-frontdoor-slack-channel` to clear forge-provenance~~ — that reviewer is greenfield-only.
- ~~Measurement plan as senior-SE deflection alone~~ — still the right *kind* of measure, but the sponsor stated a second success criterion with no home in the manifest: a diagnosis of current documentation practice with recommended process changes.

## Reviewer state

Full suite run 2026-07-27, after the variant switch: **0 blocks.** The six greenfield/portal blocks that existed before the switch are gone — those reviewers correctly skip for `variant: research`.

Passing: `persona-fit-reviewer`, `doc-currency-reviewer`, `research-completeness-reviewer`, `stateful-claim-lint-reviewer`. The suite drops from 17 reviewers to 5 under this variant; that reduction is expected, not a coverage loss.

Two warnings, both correct and both deliberate:

- `persona-fit-reviewer` — `PORTAL_OVER_PROMOTED` while `apps/portal/` exists. This is the only thing between the current state and a fully clean board, and it clears with item 5 above.
- `terminology-linter` (30) — acronym heuristics, almost all in portal components. The reviewer labels them likely false positives itself.

Agent-run judgment gates have **not** been run and are not covered by the above: `doc-quality-auditor`, `fact-check-loop-reviewer`, `research-reference-grader`, `research-sibling-scanner`. A green mechanical board is not full coverage. `fact-check-loop-reviewer` is the highest-value one outstanding — the memo makes claims attributed to named people.

## Gotchas for the next session

- Reviewer runner is NOT stamped into initiatives: run `node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs` from this root.
- `blueprint.yml` declares `variant: research` and retains the superseded `pilot_profile` block behind a SUPERSEDED banner. `pilot-profile-lock-reviewer` now short-circuits to PASS as out-of-scope for this variant, so the block is inert rather than authoritative — but it is still on disk and still reads as intent to a human skimming the file.
- **Do not put a trailing comment on the `variant:` line.** `research-completeness-reviewer` captures it, reports the variant as unrecognized, and silently falls back to greenfield — which defeated variant detection in three reviewers at once.
- `manifest:*` and `derive` resolve `BLUEPRINT_HOME` against the methodology source; set it if the checkout is not at `~/Workspace/dev/tools/blueprint`.
- The sponsor brief at `docs/se-team-brief.html` carries a superseded banner locally, but **the published artifact copy is unchanged** and still presents the old framing. Republishing is an operator call.
- The kickoff source PDF exists only in `~/Downloads`. Load-bearing quotes are transcribed into `research/sources/knowledge-database-kickoff-2026-07-27.md` so claims stay verifiable, but the binary is not durable.
- `reader-contract.json` covers only `docs/se-team-brief.html` and `apps/portal/dist`. `npm run reader:check` passing says nothing about the research corpus or the README.
- Remote is `git@github.com:nino-chavez/se-docs-frontdoor.git` (private). Worktree rule applies to any multi-session work.
