# Confluence corpus census — Phase 0, partial

**Date**: 2026-07-27
**Status**: first hard measurement of corpus magnitude. Partial — Confluence only.
**Method**: Confluence Cloud REST search API (`/wiki/rest/api/search`, CQL), executed against the live instance from an authenticated session. Counts are `type = page` and `type = attachment` per space, with recency cuts at `lastmodified >= 2025-07-27` and `>= 2024-07-27`. Reproducible: the query shape is four counts per space key.

> The founding session recorded corpus size as "genuinely unknown" and deferred the census into the pilot. The problem statement made it Phase 0 and gating. **This is the first of it to actually run.**

---

## What was counted

Five spaces, selected because they hold SE/SA/delivery solution knowledge. Space keys are the live ones; the full space list was enumerated rather than guessed.

| Space | Key | Pages | Modified <12mo | <24mo | Attachments |
| --- | --- | ---: | ---: | ---: | ---: |
| Technical Project Management | `IPM` | 1,599 | 335 | 584 | 2,138 |
| Solutions Architects | `SA` | 912 | 173 | 288 | 1,715 |
| Technical Account Management | `TAM` | 441 | 252 | 333 | 2,432 |
| Solutions Engineering | `SE` | 155 | 35 | 59 | 393 |
| Solution Architecture Knowledge Base | `SIPR` | 66 | 22 | 28 | 314 |
| **Total** | | **3,173** | **817** | **1,292** | **6,992** |

**26% touched in the last 12 months. 41% in the last 24. 59% untouched for two years or more.**

## Four findings, in order of how much they change the plan

### `C-1` — Delivery records project state in Confluence, and it is the largest corpus

`IPM` holds 1,599 pages of per-client project documentation — over half the total, with 2,138 attachments. Spot-checked titles are named client engagements.

This substantially answers the open item that `research/personas-and-jtbd.md` flags as blocking: `delivery-ipm/JOB-1` is marked `implied-not-represented` because no IPM was at the kickoff and the delivery system of record was unexamined. **A large part of it is Confluence, and it was reachable all along.**

It does not answer everything. Whether IPM *hours-tracking* and scheduling live elsewhere is still open, and the persona still needs a real IPM to talk to — second-hand description of someone else's constraint is what `P2` currently rests on. But the artifact substrate is located.

### `C-2` — The primary persona's own space is the smallest and the stalest

`SE` is 155 pages, the smallest of the five, with only 35 touched in the past year. The knowledge sits in `IPM`, `SA`, and `TAM` — other organizations.

**This is `P8`'s person-to-person round trip, explained structurally.** The sales engineer asks someone because the knowledge was never in the sales engineer's space to begin with. The round trip is not a habit or a tooling gap; it is the shape of where the documentation lives relative to who needs it. Any design that improves SE self-service has to cross an org boundary, not just a search boundary.

### `C-3` — TAM is the one corpus that is not decaying, and nobody has asked why

`TAM` has 252 of 441 pages touched within 12 months — **57%, against 21% for `IPM` and 19% for `SA`** — and carries 2,432 attachments against only 441 pages, the highest attachment-to-page ratio in the set.

Whatever practice Technical Account Management runs produces documentation that stays current under the same billing pressures that truncate everything else. `P2` says the corpus stops when billable hours stop; TAM appears to be a partial counterexample sitting inside the same company.

**That is the most promising lead for Phase 2 found so far**, and it costs one conversation. Phase 2 is organizational change, and a working internal practice beats an imported one.

### `C-4` — Most of this corpus is already inside Ask Commerce's connectors, and none of it is authoritative

All five spaces are Confluence, which Ask Commerce searches today. But its configuration explicitly demotes team- and project-space pages, naming `SE`, `TAM`, and `IPM` among others (`AC-2` in `research/prior-art/ask-commerce.md`).

So 3,173 pages are **searchable but never a source of truth**, and there is no authoritative-source entry for solution knowledge at all. Coverage is not the binding constraint on the Confluence portion of the corpus. Standing is.

## What this measurement cannot tell you

Stated plainly, because the temptation to treat these numbers as the census is real and they are not.

- **Confluence only.** Google Drive — where the tech scopes and SA project folders live, and which Ask Commerce cannot read — is uncounted. So are Gong, Slack, and the sponsor's direct messages. The tech scope corpus the sponsor proposed starting with is **not in these numbers at all**.
- **Last-modified is currency, not correctness.** The `P4` defect class — documented workarounds invalidated by shipped capability, of which guest tokenization is the worked example — is completely invisible here. A page edited last week can be wrong; a page untouched for three years can be right. `P6` says the wrong-not-stale category is both the most valuable and the fastest-decaying, and **no count of timestamps will ever find it.** Sizing it requires content inspection, which is the expensive part of Phase 0 and the part that still has no method.
- **Nothing about contradiction rate.** Two sources disagreeing is guaranteed; this says nothing about how often.
- **Nothing about question coverage.** The question the memo says nobody can answer — what fraction of real SE questions have an answer anywhere — is untouched by volume counts.

## What to run next

1. **The same counts against Drive.** Requires a Drive API path or export; the folder structure is the unknown, not the method.
2. **Content sampling for the wrong-not-stale rate.** The only measurement that addresses `P4`/`P6`. Needs a method design and a definition of "wrong" that a sampler can apply — the hardest open piece of Phase 0.
3. **Ask TAM what they do differently** (`C-3`). Cheapest high-value item on this list.
4. **Per-space authority candidates.** Which subset of `SIPR` (Solution Architecture Knowledge Base — 66 pages, small enough to read entirely) could stand as an authoritative source. That is the concrete form of the `AC-2` request.
