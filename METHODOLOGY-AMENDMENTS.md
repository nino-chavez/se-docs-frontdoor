# Methodology Amendments — se-docs-frontdoor

Append-only, reverse-chronological. Convention: `$BLUEPRINT_HOME/template/docs/methodology/methodology-amendments-convention.md`.

---

## 2026-07-27 — Research variant has no problem-statement slot upstream of the personas gate

**Trigger**: A sponsor kickoff replaced this initiative's founding problem framing. There was nowhere canonical to record the superseding problem statement — Stage 0 is Inputs Intake (a provenance catalog of assets), Stage 1 is the personas/JTBD gate, and `research/problem-space/` is listed as a Stage 2 output directory.
**Scope**: Candidate for methodology promotion
**Status**: Active

The research variant's pipeline assumes the problem is settled by the time personas are grounded. Blueprint's `template/research/personas-and-jtbd.template.md` enforces that every persona derive from a named input asset, which is the right gate — but it presupposes an agreed problem. When new input *changes the problem* rather than adding evidence to it, the sequence has no step for restating it, and the personas gate will faithfully ground personas in a superseded frame.

That is not hypothetical here. The founding framing treated the document corpus as a noisy given whose quality would improve as a byproduct of retrieval use. New input established the corpus as the output of a delivery process with structural truncation points, which inverts the dependency — capture quality now bounds retrieval quality. One founding decision (demand-driven filing) is falsified by that inversion rather than merely narrowed. Grounding personas without restating the problem first would have carried the old causal model into Stage 1 intact.

**What this initiative did**: wrote `research/problem-space/problem-statement.md` as a canonical artifact that explicitly supersedes the founding framing and the `pilot_profile` block, ahead of the Stage 1 personas gate. It states first principles with per-claim input citations, names the domain dependency order, derives solution invariants, and separates open boundary decisions (with owners) from resolved ones. The personas artifact will derive from it rather than from the founding definition.

**Suggested promotion shape**: a problem-statement step between Stage 0 and Stage 1 in the research variant, required only when the initiative supersedes a prior framing — a re-founding, not a new founding. Two candidate mechanisms: (a) a problem-statement template under Blueprint's `template/research/`, carrying a `supersedes:` field the personas reviewer can resolve; (b) a `persona-fit-reviewer` extension that fails when a persona's grounding asset predates a `supersedes:` declaration. Not proposing either as canonical on one instance — logging the gap so a second occurrence has something to match against.

**Adjacent, not the same gap**: Blueprint's `docs/variant-selection.md` already records two initiatives mis-stamped as greenfield (mrr-automation, ChapterZero). Those were wrong-variant-at-init. This one is right-variant, changed-problem-mid-flight. Related failure family, different trigger.

**References**:
- `research/problem-space/problem-statement.md`
- `research/sources/definition-and-grill-2026-07-09.md` (superseded framing)
- `research/sources/knowledge-database-kickoff-2026-07-27.md` (the new input)
- `decisions/0001-configure-first-pilot-as-prototype.md`
