# Ask Commerce empirical probe — the instrument

**Doc type**: How-to (Diátaxis) — Follow it to run the probe. Owns the question set, the scoring sheet, and the recording rule.
**Date**: 2026-08-30
**Status**: instrument ready, **not run**. See "Where this gets run" — the run is assigned to the joint AI Operations session, and its recording rule needs an explicit decision first.
**Derived from**: `research/prior-art/ask-commerce.md` (`AC-1`–`AC-4`), `research/requirements/front-door-requirements.md` (`REQ-1`–`REQ-12`), `research/personas-and-jtbd.md` (jobs), `research/problem-space/problem-statement.md` (`P4`, `P6`).

---

## Why this file exists

`HANDOFF.md` item 4 has said "a dozen real SE questions" since 27 July, and item 0b says to **score rather than by impression** against `REQ-1`–`REQ-12`. Neither the dozen questions nor the scoring sheet existed. The probe was therefore not blocked on the spend cap, on access, or on an AI Operations partner — it was blocked on having no instrument. This is the instrument.

Two requirements are named as the ones most likely to separate candidate platforms: `REQ-4`, the caution wrapper, and the shared-drive half of `REQ-5`. Questions 4, 5 and 9 exist to hit them directly.

## The recording rule — read this before running anything

**Record the verdict per question. Do not record the answer text.**

`HANDOFF-INTERNAL-ACCESS.md` sets the standing rule: derived constraints, thresholds and structural findings travel; raw content does not. A probe of Ask Commerce returns exactly what cannot travel — cited answers carrying client names, tech-scope contents and internal staff names. The verdict is what the sponsor sync needs and it is the only form that can live in this repo.

For each question record: **cited / uncited / no-record**, whether the staleness flag fired, whether a conflict was surfaced, and which space or source the citations came from. Nothing else. Where a specific document must be named as evidence, name its location, not its contents.

**A "no record exists" answer is a result, not a failure.** Questions 4, 5 and 11 are designed to return one. If they return a confident answer instead, `AC-1` or `AC-3` is wrong and that is the more interesting finding.

## Substitution before running

Questions below carry `<placeholders>`. Fill them on the machine, from the real corpus, at run time. **Do not fill them in this file** — a merchant name committed here is the raw-content rule broken by the instrument itself.

---

## The question set

### A — Negative knowledge (`se/JOB-1`, tests `P5`/`P6`)

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 1 | What are the platform's known limitations around `<a capability area the SE team scopes weekly>`, and how have prior engagements worked around them? | `REQ-1`, `REQ-2` | An answer, not a file list, every claim carrying a link and a date |
| 2 | Is the documented workaround for guest checkout tokenization still required, or has the platform shipped the capability? | `P4`, `REQ-2` | Surfaces the workaround **and** flags it as possibly superseded, or surfaces both and names the conflict. A confident stale answer is the failure this whole initiative is about |
| 3 | What can the platform not do for `<a requirement class that recurs in discovery>`? | `REQ-1` | Either a cited limitation or an explicit "no record" — never a confident answer without provenance |

### B — Drive-only questions (`AC-1`, `sa/JOB-1`, the `REQ-5` discriminator)

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 4 | Show me the tech scope for `<a named 2026 opportunity>`. | `AC-1`, `REQ-5` | **"No record."** The tech scopes are in Drive and Drive is not readable. A confident answer means `AC-1` is wrong |
| 5 | What was recommended during the sales cycle for `<a named delivered project>`, and does that recommendation predate a platform change that invalidates it? | `sa/JOB-1`, `AC-1` | "No record" on the first half. The second half is the `V-1` capability nothing on the shelf provides — expect it unanswered |

### C — Authority and staleness (`AC-2`, `REQ-2`)

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 6 | `<A question whose answer is in the SE Confluence space>` | `REQ-2` | Answer arrives with the 12-month staleness flag fired. 74% of that corpus is older than twelve months, so a run where the flag never fires means it is not doing what its configuration claims |
| 7 | `<A question a routing-table entry would own, if solution knowledge had one>` | `AC-2` | Says no authoritative source is designated, rather than answering confidently from a structurally demoted space |

### D — Conflict surfacing (`AC-4`, "surface conflicts, do not adjudicate")

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 8 | `<A question the census identified as having two contradictory source pages>` | `AC-4` | Shows both and names the conflict. Picking one silently is the failure mode |

### E — The caution wrapper (`REQ-4` — named discriminator)

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 9 | `<A deeply technical implementation question a non-SE could ask and misread>` | `REQ-4` | Any caveat that the reader may lack the context to act on this safely. Mark asked for this twice and corrected the framing once: **it is a warning, not access control** (`REQ-12` stays ruled out) |

### F — Permissions, coverage, and answer shape

| # | Question | Probes | Pass looks like |
|---|---|---|---|
| 10 | `<A question whose answer lives in a space the asker cannot open directly>` | `REQ-3` | Surfaces nothing the asker could not already open. Run this as the asker, not as an admin |
| 11 | What did the customer raise on the `<named>` discovery call? | `AC-3` | **"No record."** Gong is not connected |
| 12 | `<A broad scoping question with no single home>` | `REQ-1` | An answer with citations. A list of documents is a fail — `REQ-1` is a Must and the meeting's own notes recorded it backwards (`S-1`) |

---

## Scoring sheet

One row per question. Fill on the machine; bring the table, not the answers.

| # | Verdict (cited / uncited / no-record) | Staleness flag fired | Conflict surfaced | Citation source | `REQ` result |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |

**Two questions for Alex Vela in the same session**, from `HANDOFF.md` item 0b, because they do not survive being asked later: can an MCP connector attach to a Claude **enterprise-search project** at all, or only to individual chats and projects; and does adding one trigger the `G2` AppSec review. The second is the first thing that would push this work out of the configure-only lane.

## Where this gets run, and the decision it needs first

`HANDOFF.md` item 0b folds this probe into the joint session with AI Operations. That session answers three things at once — whether Ask Commerce behaves as its configuration claims, whether sources and configuration are ours to manage, and the Gemini entitlement re-check (`S-5`). Running the probe solo spends cap on a worse artifact and forfeits the only live opportunity to ask the two MCP questions.

**The decision that is not yet written down:** whether this may be run from an agent session at all. An agent run puts every returned answer — client names, tech-scope contents, named staff — into a session transcript on the personal machine, which the recall pipeline ingests. That is the same class of decision `HANDOFF-INTERNAL-ACCESS.md` asks to be made deliberately rather than drifted into, and it went the conservative way for the Confluence registers. Absent an explicit decision otherwise, **run it by hand and record verdicts only.**
