# Handoff — se-docs-frontdoor

**Last session**: 2026-07-27 (kickoff ingested → problem restated → variant switched to research → Stage 1 + Stage 5 authored)
**Position**: research variant. **Mechanical** reviewers green (0 blocks); the four agent-run judgment gates were run 2026-07-27 and **three returned BLOCKED**. Stage 5 deliverable drafted, partially remediated, not yet sent.

> Read `research/problem-space/problem-statement.md` before doing anything else. It supersedes the founding framing and the `pilot_profile` block in `blueprint.yml`. Working from `blueprint.yml` alone will reproduce the old model.

> **On the machine with internal access** (commerce.com tooling — Confluence, Drive, Jira, Slack, Gong, Make.com, Claude Enterprise admin), read `HANDOFF-INTERNAL-ACCESS.md` alongside this file. Four open questions are blocked on access rather than on thinking, and that file lists them in the order that changes the plan most. It also covers the setup that breaks when switching machines, and the data-governance call to make before pulling internal material into this repo.

## State

- **The problem changed on 2026-07-27**, not just the evidence. The founding model treated the doc corpus as a noisy given whose quality would improve as a byproduct of retrieval use. The sponsor kickoff established it as the output of a delivery process with structural truncation points — documentation stops when IPM hours run out, smaller engagements often get no folder, the template is not uniformly followed, and some documents are actively wrong where the platform shipped past documented workarounds. Capture quality bounds retrieval quality.
- **One founding decision is falsified**, not narrowed: grill row 13 (demand-driven filing) works when content exists but is misplaced, and does nothing when content was never written. This is why the founding scope cannot simply be widened.
- **ADR-0001 (configure-first) still holds**, with two qualifications now recorded in its Amendments section — the sponsor independently reached for a Claude-native surface twice, which strengthens it; and Gong is a named source outside the standard connectors, which is trigger 3 territory.
- Stage 1 research remains valid as evidence: three tracks, two adversarial verifications, the 16-question grill ledger, sibling scan, reference grade. None of it is retracted. What changed is the causal model the research was organized around.
- **Four open boundary decisions** (BD-1 read/write boundary, BD-2 audience, BD-3 whether an existing internal assistant owns this surface, BD-4 funding) are documented with owners in the problem statement. Three need the sponsor.
- **`BD-3` IS RESOLVED, and it reshapes the initiative.** `Ask Commerce` exists: Anthropic's native ask-your-org surface, configured by an internal **AI Operations** team, live, shared with every employee by default, connected to Confluence/Jira/Slack, with per-user permission scoping, numbered citations carrying last-modified dates, explicit conflict-surfacing, and 12-month staleness flags. **Six of the memo's seven guiding principles are already implemented in it.** The sponsor was naming the real system, not an analogy. Full artifact: `research/prior-art/ask-commerce.md` (`AC-1`–`AC-4`). Consequences: Phase 1 largely collapses into two evidenced requests to AI Operations (connect Drive; establish an authoritative source for solution knowledge); Phase 0 becomes *more* load-bearing because it is what makes those requests actionable; **Phase 2 — capture — is where the initiative's differentiated value now sits.**
- **Phase 0 partially ran.** `research/current-state/confluence-corpus-census.md` (`C-1`–`C-4`): 3,173 pages across `IPM`/`SA`/`TAM`/`SE`/`SIPR`, 26% touched in 12 months, 59% untouched for two years. `IPM` at 1,599 pages substantially answers where delivery records project state. The `SE` space is the smallest and stalest — the knowledge lives in other orgs, which is `P8`'s round trip explained structurally. Confluence only; Drive, Gong and Slack uncounted, and **timestamps cannot see the `P4` wrong-not-stale defect.**
- **Internal AI governance is in the corpus** — `research/current-state/ai-governance-constraints.md`, `G1`–`G8`. **Two findings were corrected the same day and the corrections are the instructive part:** `G4` originally read the software register as restricting Claude to unidentifiable/public data and called it a Stage 2 blocker. Wrong — Claude is deployed to every employee with no approval gate, usage-based at a $1,000/person monthly cap. The register is stale in the authoritative direction. `G5`'s NotebookLM recommendation is void with it. What stands: the corpus is Submit-for-Approval data (`G1`); the route is **Use-Case #2, an AI Use Case Review** (`G2`), duration still unmeasured; PoC rules forbid prototyping over the real corpus (`G3`); per-source constraints (`G6`). The file also records the data-governance decision for internal material: derived constraints travel, source registers do not.

## Done this session (items 1–3 of the previous list)

- `pilot_profile` extracted; `walkthrough_citation` now lives in `research/personas-and-jtbd.md`.
- **Variant switched to `research` by hand, not by the stamper.** `blueprint-init` preserves an existing `blueprint.yml`/`actor-output.yml`/`reader-contract.json`/`package.json`, so re-running it changes nothing — and `copyTree()` writes `research/personas-and-jtbd.md` *unconditionally* with the blank template, so running it for real would have destroyed the Stage 1 artifact. **Do not run the stamper against this initiative.**
- Stage 1 (`research/personas-and-jtbd.md`) and Stage 5 (`docs/decision-memo.md`) authored. All reviewers green.

## Next

1. **The memo's attribution defects are closed. Two caveats before sending — read both, they are not the same thing.**

   **`fact-check-loop-reviewer` never executed as specified.** Its agent went idle twice without reporting, so the *attribution* check was run by hand against the source PDF. That check is closed and its findings are fixed. But the gate's spec fans out to `citation-checker`, `current-state-claim-verifier`, and variant sub-checkers, then decides convergence — none of that ran. Do not record this gate as passed. One sub-check was hand-substituted; the gate is still owed. Stating otherwise here would be the same self-attestation this section warns about two paragraphs down.

   **A `citation-checker` run was in flight at session end** and its scope overlaps the open reference-grading item: the corpus-wide re-grade ran without web-fetch, so **no external URL has been re-derived**, and two claims carry forward as "cited, not re-derived" (NotebookLM API assertion; GH#53442 connector transfer). If that run came back having actually fetched those pages, the item resolves; if it came back empty, the label stands. Reconcile before trusting either state. Neither claim appears in the memo, so this gates the research corpus, not the send.

   Once sent, promote `decision-memo` to `issued` and set up the weekly sync.
2. ~~**Chase BD-3 first among the open decisions.**~~ **DONE — `Ask Commerce` exists.** See `research/prior-art/ask-commerce.md`. The memo has been rewritten as v2 around this; it is still `draft` and unsent.
3. ~~**Design Phase 0 concretely**~~ **DONE, as a draft protocol**: `research/pilot/phase-0-census-design.md`, wired to the `pilot-protocol` output (rescoped — the Claude Tag pilot it originally described is superseded). Three workstreams, two weeks elapsed, roughly four hours of senior SE/SA time. **Two things in it need a human decision before it can run:** the Drive access request (critical path, day 1) and the ~4 hours of senior adjudication time, which has to be asked of Andrew rather than quietly absorbed by Mark and Zac — unbilled senior time being the exact constraint `P2` blames for the whole problem.
4. **Run the empirical probe of Ask Commerce.** A dozen real SE questions, recording what comes back. Blocked 2026-07-27 on the **$1,000/person monthly Claude spend cap**, which was hit during research — not on access or permission. Wait for the 1st, get it raised, or run from an account with headroom. This is the single most useful artifact for the first sync and the memo names it as owed.
5. **Two inputs still not researchable from here**: an actual IPM to confirm `delivery-ipm/JOB-1` (flagged `implied-not-represented`), and whether IPM hours-tracking lives outside Confluence. The artifact substrate is found — `IPM` space, 1,599 pages (`C-1`).
6. **Ask TAM what they do differently.** Cheapest high-value item outstanding. `TAM` is the one space whose documentation is not decaying — 57% touched in 12 months against 19–21% for `SA` and `IPM`, under the same billing pressure (`C-3`). One conversation, and it is the best Phase 2 lead found.
7. **Drop `apps/portal/` + `packages/`** when a memo-rendering surface replaces them. Deferred deliberately: they are scaffolding under `template/CLAUDE.md` §1 and safe to delete, but they currently carry `npm run dev`/`build` and `reader-contract.json` declares `apps/portal/dist` as a surface. Deleting before the replacement exists just leaves a broken build. `persona-fit-reviewer` WARNs `PORTAL_OVER_PROMOTED` until then, which is correct.

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
| `fact-check-loop-reviewer` | **did not execute** — attribution sub-check hand-run instead: 1 critical + 3 high | Attribution findings **closed**. The gate itself is **still owed** — its agent went idle twice without reporting, and the convergence loop plus the other sub-checkers never ran. |

**What the two criticals were**, because both are instructive:
1. The memo promised the sponsor "a measurement attached" and defined no measurement anywhere, while never naming that as open. Hidden incompleteness, not named. Fixed by adding a "What this memo doesn't do yet" section — which also surfaced that the sponsor's *second* stated success criterion (a written diagnosis of documentation practice) was absent from the memo entirely.
2. `assets/readme/hero.svg` still rendered `greenfield · tier 1 · stage 1 closed → stage 2` as the README's first element, contradicting `variant: research` and the three paragraphs directly beneath it. Stakeholder-facing: Mark and Zac land on that README.

**What fact-check found**, and why it had to be run by hand: the dispatched agent went idle twice without producing a report, so the check was re-run directly against the source PDF in `~/Downloads`. That detour *was* the finding. The Stage 0 provenance record carried all sixteen load-bearing quotes with content and timestamps but **no speaker labels**, while asserting downstream claims were "verifiable from this repo alone." Nothing inside the repo could check a single name attribution.

| Sev | Finding | Fix |
| --- | --- | --- |
| CRITICAL | Memo enumerated Zac's no-enforced-schema observation (00:21:21) as part of **Mark's** objection, in a memo addressed to both by name | L14 split into four attributed bullets — which also closes doc-quality's 90-word-sentence HIGH and kills an ambiguous second-person "your" |
| HIGH | "This is the one you said you'd want most" attributed to Mark — a ranking he never gave | Replaced with what he did say (00:25:41, "I'm glad that this will actually kind of help") |
| HIGH | Measurement baseline named the sponsor's DM volume, but that channel runs **outbound** — he described himself asking the SAs ("I just bug them that often", 00:35:32) | Corrected in memo, `P8`, and the `knowledge-holder/JOB-1` acceptance criterion. `deflection-baseline` is now recorded as an open gap, which matches what `manifest:check` already reports |
| HIGH | Org-line labels on two named recipients ("Zac, and the SA side" / "Mark, and services delivery") — unsupported, and "services delivery" appears nowhere in the transcript. The sponsor explicitly declines to split them | Labels dropped; replaced with the sponsor's own assignment — guides to where the documentation lives |
| MEDIUM | `knowledge-holder` persona modelled as one person on "I'm the only one remaining," which is scoped to the old all-SE channel, not the holder population | Corrected; sponsor names Mark as another holder at 00:07:09 |
| MEDIUM | Twenty-questions framing credited to the sponsor's enthusiasm; it originates with Mark as a *concern* | Both attributions corrected |
| MEDIUM | "one-off client conversations **never** enter a documented process" — Mark said "sometimes… they don't" | Fourth hardened paraphrase this session. Softened |

Root cause is filed as a methodology amendment: a multi-party input asset needs per-quote speaker attribution, and a provenance record must not assert self-sufficiency it lacks. All quotes now carry `*Speaker:*`; four quotes downstream artifacts had begun resting on were added.

**Still open from doc-quality (HIGH, not blocking):** no glossary for "authority tier". `<title>` of `docs/se-team-brief.html` carries no superseded marker. This blockquote still has no destructive-action line.

**Still open from reference-grading:** the corpus-wide re-grade. The grader ran without web-fetch or shell, so **no external URL was re-derived** — it says so explicitly and does not count that as confirmation. Two specific downgrades to carry forward: the NotebookLM "(verified)" claim cites a product-chooser page for an API assertion, so it is "cited, not re-derived"; and GH#53442 documents the Cowork/MCP connector while the pilot risk is the claude.ai Enterprise connector, a transfer the sources doc caveats but the grading tables did not.

## Gotchas for the next session

- **`docs/solution-plan.md` is written in SCQ-R, deliberately** (Situation / Complication / Question / **Recommendation**) — the sponsor's manager states Minto Pyramid and SCQA as his preferred formats for receiving ideas and updates, and notes that at BC the "A" is habitually replaced by "R" for Recommendation. That document also argues for narrative prose with topic sentences over bullets and slide packs, citing the Amazon six-pager practice. Keep the register: **paragraphs that lead with their conclusion, not bullet lists.** Consequence for the gates: `reader:check` raised `dense-copy` at the default 70-word threshold, which is calibrated for the card-based SE brief. `reader-contract.json` now sets `maxWordsPerText: 115` for the Solution plan surface — that is a genre calibration with a stated reason, **not** a silenced warning. Every flagged block was checked and each already leads with its conclusion, which is the reviewer's own stated fix condition.

- Reviewer runner is NOT stamped into initiatives: run `node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs` from this root.
- `blueprint.yml` declares `variant: research` and retains the superseded `pilot_profile` block behind a SUPERSEDED banner. `pilot-profile-lock-reviewer` now short-circuits to PASS as out-of-scope for this variant, so the block is inert rather than authoritative — but it is still on disk and still reads as intent to a human skimming the file.
- **Do not put a trailing comment on the `variant:` line.** `research-completeness-reviewer` captures it, reports the variant as unrecognized, and silently falls back to greenfield — which defeated variant detection in three reviewers at once.
- `manifest:*` and `derive` resolve `BLUEPRINT_HOME` against the methodology source; set it if the checkout is not at `~/Workspace/dev/tools/blueprint`.
- **`actor-output.yml` was edited 2026-07-27 without schema validation.** Two changes: `pilot-protocol` rescoped and pointed at the Phase 0 design, and a comment block added under the `deflection-baseline` precondition. Both preserve the existing key shape, and the file parses as valid YAML — but `manifest:check` could not run (see next bullet), so **the edits are syntax-validated, not schema-validated.** Re-run `manifest:check` once the toolchain is repaired, before trusting the manifest board.
- **`manifest:check` cannot run against the current local blueprint checkout** (verified 2026-07-27, fresh clone of this repo). `package.json` invokes `template/tools/lib/actor-output.mjs`; that file does not exist in `~/Workspace/dev/tools/blueprint`, and **no file anywhere in that checkout references `actor-output` at all**. The checkout is clean at `9285222`, dated 2026-07-02 — 25 days behind this initiative's work, so the actor-output migration (`blueprint.yml` calls `actor-output.yml` "the live contract") landed upstream after it. Likely fix is pulling blueprint; not done here, because updating the methodology source mid-initiative can move gate behaviour and that is an operator call. **Consequence: the gate table's `manifest:check` line reflects a run from a newer toolchain and cannot currently be reproduced on this machine.** The mechanical reviewer suite is unaffected — it runs clean.
- The sponsor brief at `docs/se-team-brief.html` carries a superseded banner locally, but **the published artifact copy is unchanged** and still presents the old framing. Republishing is an operator call.
- The kickoff source PDF exists only in `~/Downloads`. Load-bearing quotes are transcribed into `research/sources/knowledge-database-kickoff-2026-07-27.md` so claims stay verifiable, but the binary is not durable.
- `reader-contract.json` covers only `docs/se-team-brief.html` and `apps/portal/dist`. `npm run reader:check` passing says nothing about the research corpus or the README.
- Remote is `git@github.com:nino-chavez/se-docs-frontdoor.git` (private). Worktree rule applies to any multi-session work.
