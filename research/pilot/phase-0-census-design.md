# Phase 0 — census design

**Date**: 2026-07-27
**Status**: draft protocol, for the first sponsor sync. The decision memo promises "what gets counted, how, and over how long" and has no duration attached; this is that.
**Supersedes in practice**: the `pilot-protocol` output's original scope (a Claude Tag pilot in one SE channel). That pilot is superseded — see `decisions/0001` 2026-07-27 (later). What survives is the census, which was always the gating half.

---

## What Phase 0 is for

Three questions, and nothing downstream can be decided without them:

1. **How much is there, and where?** Magnitude and distribution across sources.
2. **How much of it is wrong rather than merely old?** The `P4`/`P6` question. The most valuable category, the least durable, and invisible to every measurement run so far.
3. **What is the round trip we're displacing, in numbers?** The `deflection-baseline` precondition, which has to be captured *before* anything ships or it becomes permanently unmeasurable.

The third is here for a sequencing reason that is easy to miss. `actor-output.yml` makes `deflection-baseline` block `slack-frontdoor` from ever reaching `issued`, on the grounds that a post-launch baseline is not a baseline. **Phase 0 is the only pre-launch window that exists.** If it is not captured here, it is not captured.

## What Phase 0 is not for

Naming this because census work expands to fill available time.

- Not a quality *improvement* pass. Finding wrong documents is in scope; fixing them is Phase 2.
- Not a tooling evaluation. The surface question is answered (`research/prior-art/ask-commerce.md`).
- Not exhaustive. Workstream B samples deliberately; see its precision statement.

---

## Workstream A — Inventory

**Confluence: done.** 3,173 pages across five spaces, recency distribution recorded in `confluence-corpus-census.md`. No further work needed.

**Drive: blocked on access, and this is the critical path.** The structure is known — `Opportunities` shared drive, one folder per client opportunity, tech scope as a Sheet from a shared template — and the 2026 folder holds at least 692 opportunity folders. That figure is a floor from scrolling a file listing, not an audited count (`C-5`).

An audited count needs one of: a Workspace admin export, a service account with Drive scope, or an Apps Script run by someone with access. **Pick one and request it in week 1.** Do not spend more time scraping the web UI; that path has been taken as far as it goes and returned an order of magnitude, which is all it can give.

What the audited count must produce, per year and per source:

| Field | Why |
| --- | --- |
| Folder / file count | Magnitude |
| Created and last-modified dates | Recency distribution, comparable to the Confluence table |
| File type | Tech scope Sheets are template-derived and therefore the most uniform material in the estate; everything else is not |
| Owner | Identifies whether documentation clusters in a few people — the `P1` concentration question |
| Whether a tech scope exists at all | **The single most useful number in Phase 0.** `P2` says smaller engagements often get no folder. This measures it directly rather than inferring it |

That last row deserves emphasis. "What fraction of opportunities have a tech scope at all" is the closest available proxy for the memo's stated unknown — what fraction of real questions have an answer anywhere — and it is a simple ratio once the inventory exists.

**Gong, Slack, DMs: deferred.** Ask Commerce already indexes Slack. Gong is not connected and is not on the critical path until the trust question is settled.

## Workstream B — Quality, including the wrong-not-stale rate

The hard part, and the one with no existing method. Two instruments, because they answer different questions and neither substitutes for the other.

### B1 — Changelog join: find the wrong ones cheaply

**The insight this rests on:** `P4` documents are not randomly wrong. They are wrong for a *specific, knowable reason* — a workaround was documented because a capability was missing, and the capability later shipped. That makes them findable without reading the corpus.

Procedure:

1. Pull platform release notes for a defined window — start with 24 months, which covers the bulk of the recency distribution.
2. Extract shipped capabilities that closed a previously-missing gap. Guest tokenization is the worked example (Mark, 00:18:13) and the template for what to look for.
3. For each capability, search the corpus for documents that describe a workaround for its absence **and predate its ship date**.
4. Every hit is a candidate `P4` defect. Adjudicate a subset to establish the false-positive rate.

This is a *targeted detector*, not a sample. It will not find every wrong document — only the class that decays for this reason. That class is the one `P6` says is most valuable and least durable, so partial coverage aimed at the right target beats uniform coverage aimed at everything.

It is also mechanizable, cheap to re-run, and produces a **standing** signal rather than a snapshot. Re-running it each quarter turns "which documents just went wrong" into a routine report. That is a Phase 2 asset produced as a Phase 0 by-product.

### B2 — Sample and adjudicate: establish a rate

The changelog join finds instances. It cannot tell you what fraction of the corpus is untrustworthy, because it only looks where it expects to find something. For a rate, sample.

- **Frame**: the tech-scope corpus first, since it is where the volume is and the most uniform.
- **Size**: 50 documents, drawn randomly, stratified by age bucket.
- **Adjudication**: a senior SE or SA rates each against a three-way scheme — *still true* / *outdated but harmless* / *actively wrong if acted on*. The third category is the number that matters; the first two are the control.
- **Precision**: 50 documents gives roughly ±14 percentage points at 95% confidence. **State that on every use of the number.** It is enough to distinguish "a few percent" from "a third of the corpus," which is the decision the number has to support. It is not enough to track quarter-over-quarter movement, and should not be used that way.

**The cost of B2 is the thing to negotiate before agreeing to it.** At five minutes per document, 50 documents is roughly four hours of senior time. That time is unbilled, and unbilled time is precisely the constraint `P2` identifies as the cause of the whole problem. Asking the people who are already the bottleneck to spend half a day being the bottleneck is a real ask, and it should be made explicitly to Andrew rather than absorbed quietly by Mark and Zac.

If four hours is not available, halve the sample and widen the interval to roughly ±20 points. Do not silently reduce it and keep quoting the original precision.

### B3 — Contradiction rate

Cheapest of the three and worth doing because there is now a worked reference. Ask Commerce's configuration already hand-patches specific contradictions (`AC-4`). Start from that list — those are confirmed contradictions someone already found the hard way — and count how many more exist in the same shape. It sizes the problem the memo says we must surface rather than adjudicate.

## Workstream C — The demand baseline

`deflection-baseline` is unmet and blocking. The trap is documented and has already caught this repo once: the obvious instrument is Andrew's 1:1 DM volume with the SAs, but he described that channel as **him asking them** — "I just bug them that often" (00:35:32). That measures outbound questions from him, not inbound demand on him.

Both directions are real. They are different numbers. **The instrument must state which one it counts.**

Proposal, in preference order:

1. **Inbound to knowledge-holders, self-recorded.** For two weeks, Andrew and Mark tally questions that arrive at them which they answer from memory rather than by looking something up. A tally, not a log — anything heavier will not survive contact with a working week. This measures the thing being displaced.
2. **Outbound from the sponsor, from DM history.** Already exists, requires no new effort, and measures a real cost. Counts a different thing, and must be labelled as such.

Run both. They bound the round trip from either end, and having two honestly-labelled numbers beats one number whose direction is ambiguous. Lands as `research/pilot/baseline-pings.md`, which clears the precondition.

---

## Duration and sequence

Two weeks of elapsed time, gated on one external dependency.

| Week | Workstream | Depends on |
| --- | --- | --- |
| 1 | A — request Drive access; run the changelog join (B1) | Drive access request is the critical path and should go out day 1 |
| 1 | C — start the two-week tally | Andrew and Mark agreeing to it |
| 2 | A — audited inventory once access lands; B2 adjudication session; B3 count | Drive access; ~4 hours senior time |
| 2 | Write-up | — |

**The honest risk:** if Drive access takes longer than a week, Workstream A slips and the headline number slips with it. B1, B2 on Confluence, and C are all runnable without it, so the fortnight still produces something. Say so up front rather than reporting a slip later.

**Two weeks is elapsed time, not effort.** The effort is roughly four hours of senior SE/SA time, plus whatever the Drive export costs whoever runs it, plus my own time which is not the constraint.

## What Phase 0 produces

1. An audited inventory with recency distribution across Confluence and Drive.
2. **The fraction of opportunities with no tech scope at all** — the closest thing to answering what fraction of questions have an answer anywhere.
3. A wrong-not-stale rate with a stated confidence interval, plus a re-runnable detector for the highest-value defect class.
4. A contradiction count.
5. A demand baseline that says which direction it counts.
6. The scoped answer to *which subset is trustworthy enough to serve* — the input Phase 1's authoritative-source request needs.

Items 2, 3 and 6 are also the raw material for Andrew's second stated success criterion — a written diagnosis of where documentation practice breaks — which the memo notes still has no home. It has one now.

## What would invalidate this design

- **If Drive access is refused**, the inventory question changes from measurement to negotiation, and Phase 1's first request is probably dead too.
- **If the changelog join returns almost nothing**, either the `P4` class is smaller than the kickoff suggested or the detector is wrong. Adjudicate a handful of known-bad documents first — guest tokenization among them — to confirm the detector catches what it should before trusting a null result.
- **If senior time is unavailable**, B2 does not run and the rate stays unknown. Say the rate is unknown. Do not substitute a proxy and present it as the rate.
