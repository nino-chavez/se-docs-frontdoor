# Confluence corpus census — Phase 0, partial

**Date**: 2026-07-27
**Status**: first hard measurement of corpus magnitude. Partial — Confluence only.
**Method**: Confluence Cloud REST search API, executed against the live instance from a browser-authenticated session on 2026-07-27.

**Reproduce it.** Four counts per space key. The count is the `totalSize` field of the response, with `limit=1` — the result rows are not read, only the total:

```
GET /wiki/rest/api/search?cql=<query>&limit=1     →  response.totalSize

pages          space = "<KEY>" and type = page
fresh <12mo    space = "<KEY>" and type = page and lastmodified >= "2025-07-27"
fresh <24mo    space = "<KEY>" and type = page and lastmodified >= "2024-07-27"
attachments    space = "<KEY>" and type = attachment
```

Space keys counted: `IPM`, `SA`, `TAM`, `SE`, `SIPR`. The candidate set was enumerated rather than guessed — `GET /wiki/rest/api/space?limit=500&type=global`, filtered on names matching `solution|architect|engineer|project management|account management`.

**What the dates mean.** `lastmodified` is Confluence's last-edit timestamp. The cuts are relative to the run date, so re-running later shifts the window; to reproduce the figures below exactly, keep the literal dates above rather than recomputing "12 months ago."

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

## `C-5` — Drive, first look: the opportunity corpus dwarfs everything counted above

**Added 2026-07-27**, from direct inspection of Google Drive in an authenticated session. **Read the method caveat before citing the number.**

**Structure, confirmed rather than inferred.** The tech scopes live in an `Opportunities` shared drive, organised by year, with **one folder per client opportunity**. Inside a folder, the tech scope is a **Google Sheet** instantiated from a shared `Discovery/Tech Scope Template`. A sibling `RFP` folder exists at the same level. Rows carry an owner and a modified date, so a proper census here could produce the same recency distribution as the Confluence table above.

**Scale, stated as a floor.** The `2026` folder alone contains **at least 692 opportunity folders**.

Set that against the Confluence numbers: the entire `SE` Confluence space is **155 pages**. One year of opportunity folders in Drive is **more than four times the whole SE space**, and roughly a fifth of every page across all five Confluence spaces combined. Earlier years were not counted and almost certainly multiply it.

**This is the corpus. Confluence is the footnote.** The sponsor proposed starting with tech scopes (00:30:03) and that instinct is now measured rather than assumed — it is where the volume is, it is the most uniform material in the estate because it is template-instantiated, and **Ask Commerce cannot read a single one of them** (`AC-1`).

> **Method caveat, and it is not a formality.** 692 is a **floor, not a count.** The figure came from scrolling the Drive web UI and accumulating rendered rows, because Drive's API is not reachable from a browser session and the internal endpoints are closed. The successful pass began mid-list and covered names from A through W, so entries sorting after W are missing — at least six were visible on screen and are not in the total. A second pass intended to start from the top returned far fewer rows and was discarded rather than reconciled.
>
> **Treat 692 as "roughly 700, certainly more than 690, not audited."** It is sound enough to establish the order of magnitude and the asymmetry against Confluence, which is what the argument needs. It is not sound enough to put in front of the sponsor as a precise inventory. A real count needs Drive API access — which is a request to make, not a scraping problem to solve harder.

## What this measurement cannot tell you

Stated plainly, because the temptation to treat these numbers as the census is real and they are not.

- **Drive is sized but not counted** (`C-5`). Structure and order of magnitude are established; an audited inventory is not, and needs API access rather than more scraping. Gong, Slack, and the sponsor's direct messages remain entirely uncounted.
- **Last-modified is currency, not correctness.** The `P4` defect class — documented workarounds invalidated by shipped capability, of which guest tokenization is the worked example — is completely invisible here. A page edited last week can be wrong; a page untouched for three years can be right. `P6` says the wrong-not-stale category is both the most valuable and the fastest-decaying, and **no count of timestamps will ever find it.** Sizing it requires content inspection, which is the expensive part of Phase 0 and the part that still has no method.
- **Nothing about contradiction rate.** Two sources disagreeing is guaranteed; this says nothing about how often.
- **Nothing about question coverage.** The question the memo says nobody can answer — what fraction of real SE questions have an answer anywhere — is untouched by volume counts.

## What to run next

1. **An audited Drive count.** Structure is now known (`C-5`); the blocker is access. Drive's API is not reachable from a browser session, so this needs a real API path — a Workspace admin export, a service account, or an Apps Script run by the owner. Scraping the UI produced an order of magnitude and should not be pushed further.
2. **Content sampling for the wrong-not-stale rate.** The only measurement that addresses `P4`/`P6`. Needs a method design and a definition of "wrong" that a sampler can apply — the hardest open piece of Phase 0.
3. **Ask TAM what they do differently** (`C-3`). Cheapest high-value item on this list.
4. **Per-space authority candidates.** Which subset of `SIPR` (Solution Architecture Knowledge Base — 66 pages, small enough to read entirely) could stand as an authoritative source. That is the concrete form of the `AC-2` request.
