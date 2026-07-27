# Handoff — se-docs-frontdoor

**Last session**: 2026-07-27 (sponsor kickoff ingested; problem restated from first principles)
**Position**: problem restated, variant change pending. **Not** at the old Stage 1 → Stage 2 boundary — that boundary belonged to a superseded framing.

> Read `research/problem-space/problem-statement.md` before doing anything else. It supersedes the founding framing and the `pilot_profile` block in `blueprint.yml`. Working from `blueprint.yml` alone will reproduce the old model.

## State

- **The problem changed on 2026-07-27**, not just the evidence. The founding model treated the doc corpus as a noisy given whose quality would improve as a byproduct of retrieval use. The sponsor kickoff established it as the output of a delivery process with structural truncation points — documentation stops when IPM hours run out, sub-20-hour projects get no folder, the template is not uniformly followed, and some documents are actively wrong where the platform shipped past documented workarounds. Capture quality bounds retrieval quality.
- **One founding decision is falsified**, not narrowed: grill row 13 (demand-driven filing) works when content exists but is misplaced, and does nothing when content was never written. This is why the founding scope cannot simply be widened.
- **ADR-0001 (configure-first) still holds**, with two qualifications now recorded in its Amendments section — the sponsor independently reached for a Claude-native surface twice, which strengthens it; and Gong is a named source outside the standard connectors, which is trigger 3 territory.
- Stage 1 research remains valid as evidence: three tracks, two adversarial verifications, the 16-question grill ledger, sibling scan, reference grade. None of it is retracted. What changed is the causal model the research was organized around.
- **Four open boundary decisions** (BD-1 read/write boundary, BD-2 audience, BD-3 whether an existing internal assistant owns this surface, BD-4 funding) are documented with owners in the problem statement. Three need the sponsor.

## Next

1. **Extract `pilot_profile` into a personas/JTBD artifact** derived from the problem statement. Four fields live only in that block and the research-variant re-stamp drops it entirely (`stamp.mjs`: research has no `pilot_profile`) — `walkthrough_citation`, `monetization_side`, `competitors_in_scope`, `out_of_scope_pilots`. Extract before re-stamping or they are silently lost.
2. **Re-stamp as `--variant=research`.** Rationale in the problem statement and the 2026-07-27 amendment entry: the deliverable is a decision memo built from input assets, which is variant-tree question 0. `apps/portal/` and `packages/` are scaffolding under `template/CLAUDE.md` §1 and are safe to drop at that point — not before, since they currently carry `npm run dev`/`build`.
3. **Sponsor's straw man plan** — the committed deliverable, "something halfbaked within the week" as of 2026-07-27. This is the research variant's Stage 5 decision memo. Load the voice guide before drafting; it goes to a sponsor.
4. **Corpus census** is now phase zero, not a pilot line item. Every downstream decision depends on magnitude and quality distribution, and both are unknown.
5. **Chase BD-3.** If the internal "ask commerce" / CLA assistant exists, it may already hold the approvals that constitute the sponsor's entire stated two-month floor.

## Do not do these

Carried from the previous handoff and now wrong. Listed explicitly because they would each clear a greenfield gate for a pipeline being abandoned.

- ~~Formalize grill commitments into `prototype/DESIGN.md` to clear `design-principles-reviewer`~~ — greenfield Stage 2 artifact. The research variant has no DESIGN.md step, and this would re-encode the superseded model including demand-driven filing.
- ~~Author the Claude Tag channel instruction set~~ — premature. Depends on the census (which subset is trustworthy enough to serve) and on BD-2/BD-3.
- ~~Pilot protocol for surface `se-frontdoor-slack-channel` to clear forge-provenance~~ — that reviewer is greenfield-only.
- ~~Measurement plan as senior-SE deflection alone~~ — still the right *kind* of measure, but the sponsor stated a second success criterion with no home in the manifest: a diagnosis of current documentation practice with recommended process changes.

## Expected reviewer state (do not chase these)

Full suite run 2026-07-27. **Six blocks are greenfield gates firing on an initiative that is changing variant.** They stop applying at the re-stamp; fixing any of them means building the thing we decided not to build.

| Reviewer | Why it blocks | Action |
| --- | --- | --- |
| `design-principles-reviewer` | Wants `prototype/DESIGN.md` | None. On the do-not-do list above. |
| `prototype-forge-provenance-reviewer` | `JTBD_LACKS_SURFACE` — reads the *old* persona frontmatter, which pins a surface that is now BD-3 | None. Canonical model is `research/personas-and-jtbd.md`. |
| `prototype-smoke-runner` | No `serve.sh`, no `@smoke` specs | None. No prototype to boot. |
| `portal-chrome-canonical-reviewer` | Portal chrome drift, 10 findings | None. Portal is scaffolding, drops at re-stamp. |
| `portal-initiative-conformance-reviewer` | Portal IA contract | None. Same. |
| `portal-review-conformance-reviewer` | Review-Portal gate on an Initiative-Portal initiative | None. Known misfire. |

**Passing and meaningful**: `persona-fit-reviewer`, `doc-currency-reviewer`, `research-completeness-reviewer`, `prescription-jtbd-traceability-reviewer`, `stateful-claim-lint-reviewer`, `roadmap-registry-sync-reviewer`.

**Passing but do not trust**: `pilot-profile-lock-reviewer` reads the superseded `pilot_profile` block as canonical. A green result here is not agreement with the framing.

**Warnings worth knowing**: `cost-gate-reviewer` (3) — all three `cost.stages` skip justifications in `blueprint.yml` still cite the old plan (DESIGN.md, prototype-as-pilot-protocol). Left as-is because the research re-stamp rewrites that block; correcting them now is throwaway work. `terminology-linter` (30) — acronym heuristics, mostly in portal components; the reviewer flags them as likely false positives itself.

## Gotchas for the next session

- Reviewer runner is NOT stamped into initiatives: run `node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs` from this root.
- `blueprint.yml` still declares `variant: greenfield` and retains the superseded `pilot_profile` block behind a SUPERSEDED banner. `pilot-profile-lock-reviewer` reads that block as canonical and will pass it. Do not treat a passing gate as agreement with the framing.
- `manifest:*` and `derive` resolve `BLUEPRINT_HOME` against the methodology source; set it if the checkout is not at `~/Workspace/dev/tools/blueprint`.
- The sponsor brief at `docs/se-team-brief.html` carries a superseded banner locally, but **the published artifact copy is unchanged** and still presents the old framing. Republishing is an operator call.
- The kickoff source PDF exists only in `~/Downloads`. Load-bearing quotes are transcribed into `research/sources/knowledge-database-kickoff-2026-07-27.md` so claims stay verifiable, but the binary is not durable.
- `reader-contract.json` covers only `docs/se-team-brief.html` and `apps/portal/dist`. `npm run reader:check` passing says nothing about the research corpus or the README.
- Remote is `git@github.com:nino-chavez/se-docs-frontdoor.git` (private). Worktree rule applies to any multi-session work.
