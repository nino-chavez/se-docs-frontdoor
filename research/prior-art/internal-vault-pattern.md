# Internal prior art — an automated knowledge vault, and the three ways it fails

**Doc type**: Reference (Diátaxis) — Look things up. Owns `V-1`–`V-5`.
**Date**: 2026-07-31
**Status**: canonical for what this pattern teaches. Does **not** assess the vault's fitness for its own purpose — that is another team's call and not this initiative's business.
**Derived from**: direct inspection on 2026-07-31 of `bigcommerce/data-enrichment-context`, a repository present on this machine. Surfaced by an unrelated conversation, not by this initiative's discovery process — which is `V-5`.

> **Scope and courtesy.** This is another team's working artifact, examined for structural lessons only. Product facts inside it — commercial terms, dates, billing constructs — are **not reproduced here**, consistent with the governance rule in `ai-governance-constraints.md`. Nothing below is a judgement of the people maintaining it; the pattern is better designed than most things on the market, which is exactly why its failure modes are worth studying.

---

## What it is

An automated knowledge vault for a product domain. A headless `claude -p` routine, specified in a `refresh-prompt.md`, reaches into GitHub, Jira, Slack, Drive and Figma, writes atomic notes, and maintains a provenance registry listing every source and its ingestion state. It is delta-based, idempotent, appends a changelog, carries PII guardrails, and opens a pull request when branch protection blocks a direct push.

**It also has something most knowledge systems do not: a written conflict-resolution policy.** Newest and most authoritative wins; superseded values are marked historical rather than deleted; the canonical decisions are named explicitly.

That is, in miniature, a working version of what this initiative's Phase 2 would design. It deserves study before we design anything.

## `V-1` — A wrong **rule** is worse than a wrong record, and this is the first live example

The refresh prompt hard-codes its canonical decisions inline, in the instructions. Among them is the location of the prototype repositories, stated as an organisation that **does not exist**.

Verified 2026-07-31: `commerce-corp/fdx-enrichment-prototype` fails to resolve. The live repository is `bigcommerce/fdx-enrichment-prototype`, last pushed 2026-06-30. The false organisation appears twice in the prompt, and critically **once inside the canon statement itself** — the very line that tells the routine which facts to treat as authoritative.

**This is a defect class the solution plan does not have.** §2 distinguishes documents that are *stale* (timestamps find them) from documents that are *wrong* (timestamps cannot). This is a third thing: **a wrong rule that manufactures wrong records on every run.**

The consequence is that refreshing does not fix it. Refreshing *reproduces* it. Every future execution re-asserts a false location with full confidence, and each output looks freshly generated and correctly dated. A staleness detector built on timestamps would rate these notes as the healthiest in the corpus.

**Why this lands hard on our plan.** The capture system §4 contemplates would generate records from instructions and templates. It is structurally the same shape and therefore vulnerable to the same failure. **Invalidation has to cover the generator, not only the output** — a requirement nothing in the plan currently states.

## `V-2` — Surfacing a conflict where nobody reads it is not surfacing it

The provenance registry carries a section for sources that have been read but not yet reconciled into the notes. **Five items sit in it.** One of them records a contradiction on a headline commercial fact — a source document and the vault's own canon disagree on both a date and a billing basis. The system knows. It parked the knowledge and moved on.

Anyone ramping into the domain reads the confident notes. They do not read the registry's pending queue. **The contradiction is documented and invisible at the same time.**

**This is a correction to a principle this initiative treats as satisfied.** `docs/solution-plan.md` §1 scores *surface conflicts, do not adjudicate* as implemented, because Ask Commerce is instructed to show both sides rather than pick. That scoring is not wrong, but it is incomplete. This vault also implements the principle — it has an explicit arbitration policy, better specified than most — and the principle still fails, because **where** a conflict surfaces determines whether it functions.

The plan's §4 already carries *write where the reader can read*. This is its sibling and it belongs alongside it: **surface conflicts where the reader is looking, not into a queue.** A conflict routed to a place the asker will never open is, from the asker's position, indistinguishable from a corpus with no conflict in it.

## `V-3` — Automation inherits the bus factor it was supposed to remove

Twenty-two commits. One human author. No CI configuration of any kind — the routine is documented as something to schedule locally, and the machine has to be awake. The last activity was 2026-07-24; a week has passed with nothing.

Nothing surfaces that fact to a reader. The notes do not get a banner. They simply keep being confidently dated from the last time someone's laptop happened to be running.

**The plan has the inverse of this risk and not this one.** §1's second validation condition asks whether Ask Commerce is *ours to run*, treating dependence on another team as a cost. True, and this is the price of the alternative: a system that is ours to run can quietly become one person's laptop.

`P2` says documentation stops when the billable hours stop. This is the same structure one level up — **automation stops when one person's attention stops**, and the automation is less likely to announce it than a person would be. Any capture system this initiative proposes needs a named owner, scheduled execution off anyone's workstation, and a visible heartbeat. That is a requirement, not an operational detail.

## `V-4` — Freshness should be measured against a source's rate of change, not the calendar

Implied by the above rather than stated in the vault. A twelve-month threshold — which is what Ask Commerce applies to "fast-moving topics" — is a reasonable default and a blunt one. A source that changes weekly is stale in a month; a source that changes annually is fine at eleven.

Recorded as a refinement to *recency is correctness*, worth carrying into the pilot's design: surface a per-source last-verified view, and let an answer lead with its age when the claim is older than the source's own change rate.

## `V-5` — Two for two: internal prior art exists, and our discovery is not finding it

`BD-3` was resolved by discovering `Ask Commerce` — an internal system that already implemented six of this initiative's seven principles, which the founding research had recorded as an open question rather than checked.

This vault is the second instance, and it surfaced **by accident**, out of an unrelated conversation. Nothing in this initiative's discovery process would have found it.

**That is a finding about the process, not about either artifact.** Two independent, undiscovered, working internal implementations of things this project planned to design, both found late and both by chance. The reasonable inference is that there are more. Before Phase 2 designs anything, someone should ask across the organisation what already exists — which is cheap, and which this initiative has now twice failed to do in advance.

---

## What this does not establish

- **Nothing about the vault's fitness for its own purpose.** It was examined for pattern, not audited, and the team maintaining it has context this inspection does not.
- **Nothing about SE/SA knowledge.** Different domain, different team, different corpus. The transfer is structural.
- **No product facts travel.** The contradiction in `V-2` is described by shape and left unquoted deliberately.

## Corroboration worth noting, and two candidates we have not assessed

The unrelated analysis that surfaced this vault reached the same headline conclusion as `docs/solution-plan.md` §2 — retrieval is a solved commodity, reconciliation is not — from a different starting point and against a different vendor set. Independent convergence is stronger evidence than either analysis alone.

It named **Unblocked** and **Sourcegraph** as market entries in the ramping-onto-unfamiliar-systems category. **Neither appears in `research/competitive/buy-landscape.md`.** That analysis explicitly graded its own market claims as recollection rather than verified capability, so they enter here at the same grade: **`Reported` — unverified, and to be checked before any of it is repeated.**
