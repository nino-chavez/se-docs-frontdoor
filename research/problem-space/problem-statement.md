# Problem Statement — SE/SA knowledge access

**Date**: 2026-07-27
**Status**: canonical. Supersedes the founding framing in `research/sources/definition-and-grill-2026-07-09.md` § "The idea" and the `pilot_profile` block in `blueprint.yml`.
**Derived from**:
- `research/sources/definition-and-grill-2026-07-09.md` — founding definition, three research tracks, 16-question grill ledger
- `research/sources/knowledge-database-kickoff-2026-07-27.md` — sponsor kickoff, four attendees, full transcript (timestamps cited inline below)

This document states the problem. It does not choose a solution. Its job is to make the solution path follow from the problem rather than from anyone's instinct about tooling.

---

## The problem, stated once

A decade of platform knowledge at commerce.com lives in a small and shrinking number of people. The documents that were supposed to hold that knowledge are produced as a byproduct of billable delivery work, so they are incomplete where billing ended, inconsistent where templates were optional, and wrong where the platform shipped features that invalidated documented workarounds. The most valuable category of that knowledge — what the platform cannot do and how to work around it — is also the category that decays fastest.

Today the working system of record is a person. Someone with a question interrupts someone with history. That works, does not scale, and has been losing capacity for years as long-tenured staff left.

## Who has the problem

Full jobs-to-be-done belong in the Stage 1 gate artifact, which does not exist yet and derives from this document. Roles are named here only to establish who the problem belongs to:

| Role | Relationship to the problem |
| --- | --- |
| Sales engineer | Needs prior solutions and platform limits to scope a client engagement |
| Solutions architect | Needs the same, plus what was actually implemented versus what was sold |
| Tribal-knowledge holder | Currently the retrieval system. Absorbs the interruption cost |
| Delivery/IPM | Produces much of the corpus, under billing constraints that truncate it |
| Sponsor | Owns the outcome; needs discovery quality to improve measurably |

The tribal-knowledge holder and the sponsor are currently the same person, which concentrates both the pain and the authority to fix it (kickoff 00:35:32 — "I'm the only one remaining").

## First principles

Each claim below is load-bearing, and each is grounded in an input asset rather than inferred.

**P1 — The knowledge is in people, more reliably than in documents.**
Staff with nine and seven years of platform history left; the sponsor is no longer in the SE role that generated the knowledge. The current team is described as talented and lacking the historical context (00:07:09).

**P2 — The corpus is a byproduct of billable work, so it stops when billing stops.**
Documentation ends when IPM hours are exhausted, leaving solutions half-documented and retrospectives absent (00:20:18). Whether a project gets a folder and diagrams depends on its size: big or complex ones reliably do, and "a lot of our projects" — the example given was ones with only 20 hours — do not (00:11:54). Stated as a tendency by the practitioner, not a threshold; do not harden it into a rule.

**P3 — The corpus has no enforced schema.**
A standard template exists and is followed differently on every project, which defeats any universal schema over the aggregate (00:21:21).

**P4 — Parts of the corpus are wrong, not merely stale.**
Documented workarounds exist *because* a capability was missing. When the capability ships, those documents describe a solution to a problem that no longer exists, and the new approach is undocumented because it is new. Guest tokenization is the worked example (00:18:13).

**P5 — The highest-value knowledge is negative knowledge.**
The sponsor's stated purpose is discovery, not sales enablement: knowing which hard questions to ask, including the ones where the answer is "we can't" (00:16:58). The supporting evidence is a win attributed directly to naming a limitation and its workaround when competing vendors concealed theirs (00:24:47).

**P6 — Negative knowledge decays fastest.**
This follows from P4 and P5 together. A limitation is invalidated by roadmap delivery; a capability description is not. **The most valuable category is the least durable.** Any system that indexes the corpus without modeling recency will degrade precisely where it matters most.

**P7 — Retrieval quality is bounded above by capture quality.**
Follows from P2, P3, and P4. No retrieval technique recovers a retrospective that was never written.

**P8 — Demand is real and currently served by interrupting a person.**
The incumbent behavior is the shoulder-tap. Every SA change routes through a single 1:1 channel with the sponsor (00:35:32). Demand does not need to be created, only redirected.

## What the founding framing had backwards

The 2026-07-09 framing was: *SEs rely on isolated, distributed documents; build a front door to query across all available docs.*

That model treated the corpus as a **noisy given**. Better retrieval plus authority-tier labels would extract value from whatever was there, and document hygiene would improve as a byproduct of use — conflict flags would "double as a doc-hygiene signal," and filing would be demand-driven, triggered when the bot missed a trapped file.

The kickoff establishes that the corpus is the **output of a production process with named structural failure points**. That inverts the dependency: hygiene is an input to retrieval quality, not a byproduct of it.

One founding decision is falsified rather than widened. Grill row 13 locked *demand-driven filing* — when the bot misses a trapped file, that file gets filed. That mechanism works when content exists and is misplaced. It does nothing when the content was never created because the hours ran out (P2). Demand cannot surface an artifact that does not exist.

This is why the founding scope cannot simply be extended. The retrieval-first model is not too narrow; its central assumption does not hold.

## Five concern domains

The problem decomposes into five domains. They are not parallel — the arrows matter.

| # | Domain | What it covers |
| --- | --- | --- |
| **A** | Sources and their unequal trust | Which repositories exist, what each contains, how current and how authoritative each is |
| **B** | Question surface | Where a person brings a question and receives a cited answer |
| **C** | Process | How delivery work produces knowledge, and where that production truncates |
| **D** | Tooling | The systems that already move data between sources |
| **E** | Capture standard | New or adopted tooling that becomes the way solution knowledge is recorded going forward |

Dependency order, derived from the principles above:

```
C (process) ──────┐
                  ├──> A (source quality) ──> B (question surface)
E (capture) ──────┘
                             ▲
                             │
D (tooling) ─────────────────┘   enables, does not determine
```

- **B is downstream of A**, and A is bounded by C and E (P7). B can be built first, but its ceiling is set elsewhere.
- **C and E are the same problem at different tenses.** C is why the existing corpus has holes; E is how future knowledge avoids them.
- **D is an enabler, not a driver.** Integration tooling moves data between sources. It does not make a truncated retrospective complete.

## Invariants for any solution

Derived from the principles; these constrain every candidate design.

1. **Answers cite sources.** Trust in negative knowledge requires provenance a reader can check. Citations were already identified as the primary adoption driver for internal document assistants (grill, research track 2).
2. **Recency is a correctness signal, not metadata.** P6 means document age carries information about whether the content is still true. Authority tier alone is insufficient — an authoritative document can be confidently wrong.
3. **Conflicts surface; they are not adjudicated.** P4 guarantees contradictory sources. A single confident answer will sometimes be the stale one. This invariant was already locked at founding (grill row 7) and survives unchanged.
4. **No solution may require a schema the corpus does not have.** P3 rules out designs that presuppose uniform structure across projects.
5. **Success is measured against the human incumbent.** P8 makes the shoulder-tap the baseline. Displacing it is the outcome; usage is a proxy.
6. **Coverage is scoped by verified quality, not by ambition.** P2 and P3 mean quality is unevenly distributed across sources. Indexing everything indexes the wrong things too.

## Open boundary decisions

These are decisions, not research questions. Each changes what gets built.

**BD-1 — Does domain E sit inside this initiative?**
E is a write system: tooling that records knowledge going forward. The founding decision locked `READ-ONLY v1` as a hard line, and ADR-0001 states that revisiting it requires a deliberate ADR of its own. E therefore either forces that ADR now, or sits outside this initiative's boundary and is recommended to a successor. It also changes the security and privacy surface, which the sponsor identified as the entire two-month floor (00:31:14). **Unresolved. Owner: operator.**

**BD-2 — What is the audience boundary?**
The founding scope was sales engineers, with other audiences explicitly deferred until deflection moved. The sponsor asked for SE and SA, then for anyone in the company (00:09:27, 00:16:58). **Unresolved. Owner: operator with sponsor.**

**BD-3 — Does an existing internal assistant already own this surface?**
The sponsor referred twice to an existing internal capability — "something similar to ask commerce that we do for everything within commerce" (00:09:27), and later placing this "directly within CLA, like ask commerce" (00:33:23). If that platform exists, it is either the delivery vehicle or prior art that must be reviewed before any tooling decision, and it may already hold the approvals that constitute the stated timeline floor. **Unverified. Owner: sponsor to identify.**

**BD-4 — What is the funding line?**
No budget was established. The question was raised and answered on a different axis (00:31:14). Tooling costs are currently absorbed personally by the single named developer (00:37:28). **Unresolved. Owner: sponsor.**

## The natural path

The sequence below is derived from the dependency graph, not from a preferred architecture. Each phase exists because something downstream cannot be decided without it.

**Phase 0 — Corpus census.**
Every downstream decision depends on magnitude and quality distribution, and both are unknown. The founding session recorded corpus size as "genuinely unknown" and deferred the census into the pilot. The kickoff makes the census the gating question instead: how much exists, how current, how contradictory, and how it distributes across sources. This is cheap relative to everything else being discussed, and it is the only work that no other decision can proceed without.

It also produces the first real answer to invariant 6 — which subset is trustworthy enough to serve.

**Phase 1 — Question surface over the highest-trust subset.**
Domain B, scoped by the census rather than by ambition. Structured tech scopes are more uniform than a decade of direct messages; the sponsor independently proposed exactly this scoping, tech scopes and the SA folder first, Slack later (00:30:03), along with the release guardrail that a phase shipping bad or old information is worse than shipping nothing.

Configure-first remains the leading candidate here because the sponsor's own opening instinct was a Claude-native surface, and because the stated timeline floor is composed entirely of security review and hosting overhead that a configured path may avoid. That candidacy is now qualified: sources the existing connectors do not reach are a named trigger for a custom build in ADR-0001, and at least one such source is already in scope.

**Phase 2 — Capture-side correction.**
Domains C and E. Phase 1's ceiling is set here (P7), so this determines whether the product improves or plateaus. This is organizational change, not software, and it cannot be delivered by shipping a retrieval surface. BD-1 decides whether it lives in this initiative.

**Phase 3 — Discovery support.**
The sponsor's actual enthusiasm — generating the hard questions to ask a given merchant, including the disqualifying ones. Sequenced last because it depends on negative knowledge being both present and current, which is the P6 problem that Phases 0 through 2 exist to address. Note that a partial version already exists in the tech scope document the sponsor demonstrated (00:26:50); it is prior art, not a greenfield surface.

**Why B can precede its own dependency.** Phase 1 ships before Phase 2 deliberately. It is the cheapest instrument for measuring the real question distribution and the real failure modes, and it converts the census from a one-time snapshot into a standing signal. It must not be mistaken for the finished product, and invariant 6 is what keeps it honest.

---

## What this document does not decide

- Which tools get used. Tooling selection follows the census and BD-3.
- Whether a build is required. ADR-0001's configure-first conclusion stands, with two named qualifications above.
- The measurement definition. The founding deflection metric survives as the right *kind* of measure per invariant 5, but the sponsor's stated success criterion — a diagnosis of current documentation practice with recommended changes — is a second deliverable with no current home in the manifest.
