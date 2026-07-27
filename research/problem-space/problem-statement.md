# Problem Statement — SE/SA knowledge access

**Date**: 2026-07-27
**Status**: canonical. Supersedes the founding framing in `research/sources/definition-and-grill-2026-07-09.md` § "The idea" and the `pilot_profile` block in `blueprint.yml`.
**Derived from**:
- `research/sources/definition-and-grill-2026-07-09.md` — founding definition, three research tracks, 16-question grill ledger
- `research/sources/knowledge-database-kickoff-2026-07-27.md` — sponsor kickoff, four attendees, full transcript (timestamps cited inline below)

## What this document is

An explanation of why the problem has the shape it does. It is meant to be read straight through, once, without looking anything up.

It does **not** choose a solution, and it is not a plan of record. Where it names a sequence, that sequence is a consequence of the problem's structure rather than a commitment.

Short labels appear throughout — `P1`, `BD-2`, and so on. They exist so other documents and tools can cite a specific claim precisely; `actor-output.yml` and `research/personas-and-jtbd.md` both do. **You never need them to read this.** Every label sits next to the thing it names, and the last section collects them for anyone citing this file.

---

## The problem, stated once

A decade of platform knowledge at commerce.com lives in a small and shrinking number of people. The documents that were supposed to hold that knowledge are produced as a byproduct of billable delivery work, so they are incomplete where billing ended, inconsistent where templates were optional, and wrong where the platform shipped features that invalidated documented workarounds. The most valuable category of that knowledge — what the platform cannot do and how to work around it — is also the category that decays fastest.

Today the working system of record is a person. Someone with a question interrupts someone with history. That works, does not scale, and has been losing capacity for years as long-tenured staff left.

## Who has the problem

Full jobs-to-be-done belong in the Stage 1 gate artifact, `research/personas-and-jtbd.md`, which derives from this document. Roles are named here only to establish who the problem belongs to:

| Role | Relationship to the problem |
| --- | --- |
| Sales engineer | Needs prior solutions and platform limits to scope a client engagement |
| Solutions architect | Needs the same, plus what was actually implemented versus what was sold |
| Tribal-knowledge holder | Currently the retrieval system. Absorbs the interruption cost |
| Delivery/IPM | Produces much of the corpus, under billing constraints that truncate it |
| Sponsor | Owns the outcome; needs discovery quality to improve measurably |

The sponsor is himself one of the tribal-knowledge holders, which concentrates both the pain and the authority to fix it. Two scopes should not be collapsed here: he is the last remaining member of the old all-SE channel (00:35:32 — "I'm the only one remaining"), which is narrower than being the only person who holds platform history. He names at least one other holder in the room (00:07:09 — "they don't have the same historical knowledge that you have, Mark, that I've had and some of the rest of the team has"). The holder population is small and shrinking; it is not one person.

## Why the corpus is the way it is

Eight claims. Each is load-bearing. Six are grounded directly in an input asset; two (`P6`, `P7`) are derived from the others and say so where they appear.

**`P1` — The knowledge is in people, more reliably than in documents.**
Staff with nine and seven years of platform history left; the sponsor is no longer in the SE role that generated the knowledge. The current team is described as talented and lacking the historical context (00:07:09).

**`P2` — The corpus is a byproduct of billable work, so it stops when billing stops.**
Documentation ends when IPM hours are exhausted, leaving solutions half-documented and retrospectives absent (00:20:18). Whether a project gets a folder and diagrams depends on its size: big or complex ones reliably do, and "a lot of our projects" — the example given was ones with only 20 hours — do not (00:11:54). Stated as a tendency by the practitioner, not a threshold; do not harden it into a rule.

**`P3` — The corpus has no enforced schema.**
A standard template exists and is followed differently on every project, which defeats any universal schema over the aggregate (00:21:21).

**`P4` — Parts of the corpus are wrong, not merely stale.**
Documented workarounds exist *because* a capability was missing. When the capability ships, those documents describe a solution to a problem that no longer exists, and the new approach is undocumented because it is new. Guest tokenization is the worked example (00:18:13).

**`P5` — The highest-value knowledge is negative knowledge.**
The sponsor's stated purpose is discovery, not sales enablement: knowing which hard questions to ask, including the ones where the answer is "we can't" (00:16:58). The supporting evidence is a win attributed directly to naming a limitation and its workaround when competing vendors concealed theirs (00:24:47).

**`P6` — Negative knowledge decays fastest.**
A derivation, not a citation: it follows from the two claims above. A limitation is invalidated by roadmap delivery; a capability description is not. **The most valuable category is the least durable.** Any system that indexes the corpus without modeling recency will degrade precisely where it matters most.

**`P7` — Retrieval quality is bounded above by capture quality.**
Also a derivation, from the byproduct, schema, and wrongness claims together. No retrieval technique recovers a retrospective that was never written.

**`P8` — Demand is real and currently served by a person-to-person round trip.**
The incumbent mechanism is one person asking another. It runs in both directions through the same few long-tenured people, and the transcript is explicit about the direction it documents: the sponsor maintains a standing 1:1 channel with every SA — each new SA is added to it — and describes himself as the one asking, because the SAs hold the implementation experience ("I just bug them that often", 00:35:32). Questions also arrive *at* him, since he is one of the few who carry the platform history (00:07:09, 00:27:46).

The distinction matters for measurement: the sponsor's direct-message volume is a record of his outbound questions, not of inbound demand on him, so it cannot serve as a deflection baseline without saying which direction is being counted. Demand does not need to be created, only redirected — but the round trip, not one person's inbox, is the thing being displaced.

## What the founding framing had backwards

The 2026-07-09 framing was: *SEs rely on isolated, distributed documents; build a front door to query across all available docs.*

That model treated the corpus as a **noisy given**. Better retrieval plus authority-tier labels would extract value from whatever was there, and document hygiene would improve as a byproduct of use — conflict flags would "double as a doc-hygiene signal," and filing would be demand-driven, triggered when the bot missed a trapped file.

The kickoff establishes that the corpus is the **output of a production process with named structural failure points**. That inverts the dependency: hygiene is an input to retrieval quality, not a byproduct of it.

One founding decision is falsified rather than widened. Grill row 13 locked *demand-driven filing* — when the bot misses a trapped file, that file gets filed. That mechanism works when content exists and is misplaced. It does nothing when the content was never created because the hours ran out. Demand cannot surface an artifact that does not exist.

This is why the founding scope cannot simply be extended. The retrieval-first model is not too narrow; its central assumption does not hold.

## The five things this problem is made of

They are not parallel. The arrows carry the argument.

| Name | What it covers | Handle |
| --- | --- | --- |
| **Source trust** | Which repositories exist, what each contains, how current and how authoritative each is | `A` |
| **The question surface** | Where a person brings a question and receives a cited answer | `B` |
| **How work produces knowledge** | How delivery work generates documentation, and where that generation truncates | `C` |
| **Existing integration tooling** | The systems that already move data between sources | `D` |
| **The capture standard** | New or adopted tooling that becomes the way solution knowledge is recorded going forward | `E` |

```
  How work produces knowledge ──┐
                                ├──▶  Source trust  ──▶  The question surface
  The capture standard ─────────┘                               ▲
                                                                │
  Existing integration tooling ─────────────────────────────────┘
                                            enables, does not determine
```

- **The question surface is downstream of source trust**, and source trust is bounded by how work produces knowledge and by the capture standard. The question surface can be built first, but its ceiling is set elsewhere.
- **How work produces knowledge and the capture standard are the same problem in two tenses.** The first is why the existing corpus has holes; the second is how future knowledge avoids them.
- **Integration tooling enables; it does not determine.** Moving data between sources does not make a truncated retrospective complete.

## What any solution has to do

Six constraints that follow from the claims above. Each is named so it can be referred to without a lookup.

1. **Cite or say nothing.** This does not rest on adoption research — see the note below. It follows from the two claims about negative knowledge: an answer about what the platform *cannot* do gets acted on in front of a client, and parts of the corpus are wrong rather than merely old. A reader therefore has to be able to check the source themselves. The supporting evidence is first-party: the engagement won by disclosing a limitation with its workaround (00:24:47) turned on the disclosure being verifiable, not on it being confident.
2. **Recency is correctness.** Because parts of the corpus are wrong rather than merely old, document age carries information about whether the content is still true. Authority tier alone is insufficient — an authoritative document can be confidently wrong.
3. **Surface conflicts; do not adjudicate them.** Contradictory sources are guaranteed. A single confident answer will sometimes be the stale one. Locked at founding (grill row 7) and unchanged.
4. **Assume no schema.** Every project documents differently, which rules out designs that presuppose uniform structure across the corpus.
5. **Measure against the person.** The person-to-person round trip is the baseline. Displacing it is the outcome; usage is a proxy. Whichever instrument is chosen has to state which direction of the round trip it counts — see `P8`.
6. **Coverage follows verified quality, not ambition.** Quality is unevenly distributed across sources. Indexing everything indexes the wrong things too.

> **Note on the adoption statistics.** An earlier version of this document grounded the citation
> invariant in market research — "under 15% weekly-active by month six", "citations are the #1
> adoption driver". Reference grading on 2026-07-27 found those figures carry no citation anywhere
> in the corpus, in a source document that attests every load-bearing claim has one. They are not
> weak evidence; they are unsourced. Removed from the argument rather than re-labelled. The
> invariant stands without them. Same finding applies to the "federated beats indexed retrieval"
> consensus claim, whose sole citation is a vendor advocating for its own product category — the
> independent reason federated fits here is uniform read access plus freshness sensitivity, which
> needs no external authority.

## The four decisions still open

Decisions, not research questions. Each changes what gets built.

**Does the capture standard sit inside this initiative?** — `BD-1`
Recording knowledge going forward is a write system. The founding decision locked `READ-ONLY v1` as a hard line, and ADR-0001 states that revisiting it requires a deliberate ADR of its own. So the capture standard either forces that ADR now, or sits outside this initiative's boundary and is recommended to a successor. It also changes the security and privacy surface, which the sponsor identified as the entire two-month floor (00:31:14). **Unresolved. Owner: operator.**

**What is the audience boundary?** — `BD-2`
The founding scope was sales engineers, with other audiences explicitly deferred. The sponsor asked for SE and SA, then for anyone in the company (00:09:27, 00:16:58). **Unresolved. Owner: operator with sponsor.**

**Does an existing internal assistant already own this surface?** — `BD-3`
The sponsor referred twice to an existing internal capability — "something similar to ask commerce that we do for everything within commerce" (00:09:27), and later placing this "directly within CLA, like ask commerce" (00:33:23).

> **RESOLVED 2026-07-27. It exists, and the sponsor was naming the actual system rather than an analogy.** `Ask Commerce` is Anthropic's native ask-your-org surface, configured and maintained by an internal AI Operations team, live, shared with every employee by default, connected to Confluence, Jira and Slack, with per-user permission scoping, numbered citations carrying last-modified dates, explicit conflict-surfacing, and a 12-month staleness flag. Six of the decision memo's seven guiding principles are already implemented in it.
>
> Full detail, including the four gaps that define this initiative's remaining work, in `research/prior-art/ask-commerce.md`. The successor question is no longer *whether* it exists but whether this initiative lives inside it — and the answer looks like yes, via the AI Operations intake process, rather than build-alongside. **Owner: operator, with AI Operations.**

**What is the funding line?** — `BD-4`
No budget was established. The question was raised and answered on a different axis (00:31:14). Tooling costs are currently absorbed personally by the single named developer (00:37:28). **Unresolved. Owner: sponsor.**

## The path that follows

Derived from the dependency above, not from a preferred architecture. Each phase exists because something downstream cannot be decided without it.

> **Revised 2026-07-27, after `BD-3` resolved.** The dependency structure above is unchanged and still carries the argument — the question surface is still downstream of source trust, and source trust is still bounded by capture. What changed is who builds the question surface. **It already exists.** So Phase 1 contracts sharply, Phase 0 becomes more load-bearing rather than less, and Phase 2 is where this initiative's differentiated value now sits. Each phase below carries its revision inline.

**Phase 0 — Count the corpus.**

> **Revised: partially executed, and now more load-bearing rather than less.** The Confluence portion ran on 2026-07-27 — 3,173 pages across five spaces, 26% touched within 12 months, 59% untouched for two years (`confluence-corpus-census.md`). Drive, Gong, Slack and the direct messages remain uncounted, and the tech scopes the sponsor wants to start with are **not** in those numbers.
>
> Its role changed. The census is no longer only an input to a build decision — it is **the evidence that makes the two Phase 1 requests to AI Operations actionable**. "Connect Drive" and "make solution knowledge authoritative" are asks that need a sized, characterized corpus behind them. The census is what turns them from opinion into request.
>
> The hard part is unchanged and still unmethoded: **timestamps cannot find the wrong-not-stale defect.** `P4`'s guest-tokenization class is invisible to every count run so far, `P6` says it is the most valuable and least durable category, and sizing it needs content sampling with a definition of "wrong" a sampler can apply. That method does not exist yet and is the most valuable thing left to design.

Every downstream decision depends on magnitude and quality distribution, and both are unknown. The founding session recorded corpus size as "genuinely unknown" and deferred the census into the pilot. The kickoff makes the census the gating question instead: how much exists, how current, how contradictory, and how it distributes across sources. This is cheap relative to everything else being discussed, and it is the only work that no other decision can proceed without.

It also produces the first real answer to *coverage follows verified quality* — which subset is trustworthy enough to serve.

**Phase 1 — A question surface over the highest-trust subset.**
Scoped by the census rather than by ambition. Structured tech scopes are more uniform than a decade of direct messages; the sponsor independently proposed exactly this scoping — tech scopes and the SA folder first, Slack later (00:30:03) — along with the release guardrail that a phase shipping bad or old information is worse than shipping nothing.

> **Revised: this phase largely collapses.** The question surface exists and serves the whole company. Phase 1 stops being *build or configure a surface* and becomes *close the coverage and standing gaps on the surface that already runs* — two requests to AI Operations, both of which the census is what justifies:
>
> 1. **Connect Drive contents** (`AC-1`). Ask Commerce can see Drive files and cannot read them; the tech scopes and SA folders the sponsor named live there.
> 2. **Establish an authoritative source for solution knowledge** (`AC-2`). The routing table has entries for GRC, HR, equity, IT and tool approval, and none for what an SE needs. The `SE`, `TAM` and `IPM` spaces are explicitly demoted, so 3,173 already-searchable Confluence pages can never stand as a source of truth.
>
> The sponsor's release guardrail survives intact and now has teeth: the demotion rules already encode "don't ship bad or old information," and the 12-month staleness flag already fires against roughly three-quarters of this corpus (`confluence-corpus-census.md`).

Configure-first is confirmed rather than merely leading — see `ADR-0001`'s 2026-07-27 (later) amendment. It was not just the right call; another team reached it independently and shipped it at org scale first.

**Phase 2 — Fix how work produces knowledge, and set the capture standard.**
Phase 1's ceiling is set here, because retrieval quality is bounded by capture quality. This determines whether the product improves or plateaus. It is organizational change, not software, and it cannot be delivered by shipping a retrieval surface. `BD-1` decides whether it lives in this initiative.

> **Revised: this is now where the initiative's differentiated value sits**, and there is first-party evidence for it that did not exist when this document was written. Ask Commerce's instructions carry hand-written workarounds for individual corpus contradictions — one page using two names for the same Slack channel, two pages disagreeing on a GitHub organization name. Every contradiction becomes a bespoke line of configuration maintained by one team (`AC-4`).
>
> **The retrieval layer is already absorbing capture failure as manual maintenance debt, at O(contradictions).** That is `P7` observed in production rather than argued from first principles, and it is the strongest available argument to the sponsor — made from Commerce's own system rather than from theory. `BD-1` is consequently the decision that now carries the most weight.
>
> A lead worth more than a framework: `TAM` is the one space in the census whose documentation is not decaying — 57% touched within 12 months against 19–21% for `SA` and `IPM`, under the same billing pressure (`C-3`). A working internal practice beats an imported one, and finding out what they do costs one conversation.

**Phase 3 — Discovery support.**
The sponsor's actual enthusiasm — generating the hard questions to ask a given merchant, including the disqualifying ones. Sequenced last because it depends on negative knowledge being both present and current, which is the decay problem that Phases 0 through 2 exist to address. A partial version already exists in the tech scope document the sponsor demonstrated (00:26:50); it is prior art, not a greenfield surface.

**Why the question surface can precede its own dependency.** Phase 1 ships before Phase 2 deliberately. It is the cheapest instrument for measuring the real question distribution and the real failure modes, and it converts the census from a one-time snapshot into a standing signal. It must not be mistaken for the finished product — *coverage follows verified quality* is what keeps it honest.

## What this document does not decide

- Which tools get used. Tooling selection follows the census and `BD-3`.
- Whether a build is required. ADR-0001's configure-first conclusion stands, with two named qualifications above.
- The measurement definition. The founding deflection metric survives as the right *kind* of measure — see *measure against the person* — but the sponsor's stated success criterion, a diagnosis of current documentation practice with recommended changes, is a second deliverable with no current home in the manifest.

---

# Reference — citation handles

The lookup layer. Other documents and tools cite these; nothing above requires them.

**Claims** — `P1` knowledge is in people · `P2` corpus is a byproduct of billable work · `P3` no enforced schema · `P4` parts are wrong, not stale · `P5` negative knowledge is most valuable · `P6` negative knowledge decays fastest · `P7` retrieval is bounded by capture · `P8` demand exists, served by a person-to-person round trip

**Domains** — `A` source trust · `B` the question surface · `C` how work produces knowledge · `D` existing integration tooling · `E` the capture standard

**Open decisions** — `BD-1` does the capture standard sit inside this initiative (**now the heaviest**) · `BD-2` audience boundary · ~~`BD-3` does an existing internal assistant own this surface~~ **RESOLVED 2026-07-27 — yes, `Ask Commerce`** · `BD-4` funding line (**first real input**: Claude runs on a $1,000/person monthly usage cap, and it binds)

**Outward handles** — `G1`–`G8` in `research/current-state/ai-governance-constraints.md` · `AC-1`–`AC-4` in `research/prior-art/ask-commerce.md` · `C-1`–`C-4` in `research/current-state/confluence-corpus-census.md`

**Solution constraints** — cite or say nothing · recency is correctness · surface conflicts, do not adjudicate · assume no schema · measure against the person · coverage follows verified quality

Citing convention: prefer the name in prose and attach the handle, so a reader never has to come here. `P6` and `BD-1` are already cited this way from `research/personas-and-jtbd.md`, `research/prior-art/capture-domain-prior-art.md`, `actor-output.yml`, and `decisions/0001-configure-first-pilot-as-prototype.md`.
