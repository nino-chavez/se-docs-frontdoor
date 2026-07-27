# Handoff — se-docs-frontdoor

**Last session**: 2026-07-27 (kickoff ingested → problem restated → variant switched to research → Stage 1 + Stage 5 authored)
**Position**: research variant. **Mechanical** reviewers green (0 blocks); the four agent-run judgment gates were run 2026-07-27 and **three returned BLOCKED**. Stage 5 deliverable drafted, partially remediated, not yet sent.

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

1. **Do not send the memo until the judgment-gate remediation is closed** — see the reviewer-state section below for what is done and what is open. A green mechanical board was what made this look ready on the first pass; it wasn't. Once closed, promote `decision-memo` to `issued` and set up the weekly sync.
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

**Mechanical suite** (`run-reviewers.mjs`): 0 blocks. 5 reviewers apply under `variant: research`, down from 17 — that reduction is correct, not lost coverage. One standing warn, `PORTAL_OVER_PROMOTED`, clears with the portal deletion above.

**Agent-run judgment gates, run 2026-07-27.** Three of four returned BLOCKED. The mechanical board was green throughout, which is exactly why it is not evidence of readiness.

| Gate | Verdict | Status of remediation |
| --- | --- | --- |
| `doc-quality-auditor` | BLOCKED, 2 critical | Both criticals **closed**. Several HIGH/MEDIUM open — see below. |
| `research-sibling-scanner` | BLOCKED | **Closed.** Broken `knowledge-index` citation corrected at 5 sites; missed capture sibling (`claude-docs-toolkit`) added; gate's required H2 added. |
| `research-reference-grader` | BLOCKED | **Partly closed.** Canonical fix landed. Corpus-wide re-grade still open. |
| `fact-check-loop-reviewer` | still running at session end | **Open.** Highest-value outstanding gate — the memo attributes claims to named people. |

**What the two criticals were**, because both are instructive:
1. The memo promised the sponsor "a measurement attached" and defined no measurement anywhere, while never naming that as open. Hidden incompleteness, not named. Fixed by adding a "What this memo doesn't do yet" section — which also surfaced that the sponsor's *second* stated success criterion (a written diagnosis of documentation practice) was absent from the memo entirely.
2. `assets/readme/hero.svg` still rendered `greenfield · tier 1 · stage 1 closed → stage 2` as the README's first element, contradicting `variant: research` and the three paragraphs directly beneath it. Stakeholder-facing: Mark and Zac land on that README.

**Still open from doc-quality (HIGH, not blocking):** README does not mention `docs/decision-memo.md` anywhere, and its repo map still describes `docs/` as "the sponsor brief". Memo L14 is a ~90-word single sentence carrying the whole reframe. No glossary for "authority tier".

**Still open from reference-grading:** the corpus-wide re-grade. The grader ran without web-fetch or shell, so **no external URL was re-derived** — it says so explicitly and does not count that as confirmation. Two specific downgrades to carry forward: the NotebookLM "(verified)" claim cites a product-chooser page for an API assertion, so it is "cited, not re-derived"; and GH#53442 documents the Cowork/MCP connector while the pilot risk is the claude.ai Enterprise connector, a transfer the sources doc caveats but the grading tables did not.

## Gotchas for the next session

- Reviewer runner is NOT stamped into initiatives: run `node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs` from this root.
- `blueprint.yml` declares `variant: research` and retains the superseded `pilot_profile` block behind a SUPERSEDED banner. `pilot-profile-lock-reviewer` now short-circuits to PASS as out-of-scope for this variant, so the block is inert rather than authoritative — but it is still on disk and still reads as intent to a human skimming the file.
- **Do not put a trailing comment on the `variant:` line.** `research-completeness-reviewer` captures it, reports the variant as unrecognized, and silently falls back to greenfield — which defeated variant detection in three reviewers at once.
- `manifest:*` and `derive` resolve `BLUEPRINT_HOME` against the methodology source; set it if the checkout is not at `~/Workspace/dev/tools/blueprint`.
- The sponsor brief at `docs/se-team-brief.html` carries a superseded banner locally, but **the published artifact copy is unchanged** and still presents the old framing. Republishing is an operator call.
- The kickoff source PDF exists only in `~/Downloads`. Load-bearing quotes are transcribed into `research/sources/knowledge-database-kickoff-2026-07-27.md` so claims stay verifiable, but the binary is not durable.
- `reader-contract.json` covers only `docs/se-team-brief.html` and `apps/portal/dist`. `npm run reader:check` passing says nothing about the research corpus or the README.
- Remote is `git@github.com:nino-chavez/se-docs-frontdoor.git` (private). Worktree rule applies to any multi-session work.
