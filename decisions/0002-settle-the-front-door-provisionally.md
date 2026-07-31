# ADR-0002 — Settle the front door on Ask Commerce provisionally, and convert the platform test into a gap inventory

- **serves**: `se/JOB-1`, `sponsor/JOB-1`. The front-door choice has been treated as open for three weeks while every downstream decision waited on it. It is not as open as it looks, and holding it open is now the expensive part.
- **Status**: proposed, 2026-07-31. Supersedes nothing; extends `ADR-0001` (configure-first), which this confirms rather than revisits.
- **Date**: 2026-07-31
- **Source**: `research/prior-art/ask-commerce.md`, `research/competitive/buy-landscape.md`, `research/requirements/front-door-requirements.md`, `research/sources/se-docs-frontdoor-sync-2026-07-30.md` `S-6a`, `research/prior-art/internal-vault-pattern.md`

## Context

Three questions were live: research more of the market, revisit a custom build, or settle on a platform and enumerate gaps. Taken in that order they imply the front-door choice is the open decision. It mostly is not, and the last week's evidence narrowed it further.

**The market question is answered.** Two independent scans — this initiative's (`buy-landscape.md`) and an unrelated analysis reaching the same conclusion against a different vendor set — converged: retrieval is commodity, reconciliation is not. Two named entries remain unexamined (Unblocked, Sourcegraph). That is a half-hour of checking, not a research phase.

**The candidate comparison has one new tiebreaker.** On the three sources Mark named (`S-6a`):

| Source | Ask Commerce | Gemini Enterprise |
| --- | --- | --- |
| Confluence `SA` | Connected | Documented connector |
| Shared Google Drive | Not connected — unfinished setup (`AC-1`) | Documented, with shared-drive scoping |
| Lucidchart | Official Claude connector exists (MCP) | **No Lucid connector in its published set** |

Gemini leads on Drive today; Claude is the only path to Lucid at all. Neither reads two of three right now. **The Drive gap is a request on either platform** — on Claude it is finishing a documented setup, on Gemini it is a Vendor Intake plus that same setup.

**What actually separates them is cost of entry, and only one direction is reversible.** Claude is deployed org-wide, approved, no gate, no incremental spend (`G4`). Gemini Enterprise routes to a `G2` Vendor Intake — the expensive path `ADR-0001` exists to avoid — and its cost premise is under re-check but its duplicate-surface objection is not: two ask-your-org systems answering the same question with nothing to adjudicate them is `P4` at the tool tier, manufactured by us.

## Decision

**Settle on Ask Commerce as the working front door, provisionally, with named reversal triggers. Convert the joint Alex Vela test from a bake-off into a gap inventory.**

Three consequences, and the second is the point of this ADR.

**1. Stop researching the market.** Close the Unblocked/Sourcegraph gap in one sitting, at `Reported` grade, and record it. Anything further is motion.

**2. The platform test scores one candidate against `REQ-1`–`REQ-12` and produces a gap list with an owner and a cost per gap.** "Which tool wins" is a question we can already answer well enough to proceed. "What does the tool we are going to use fail to do, and what does each failure cost to close" is not, and it is what every downstream decision actually needs. The output is a table, not a verdict.

**3. The build decision stays deferred, and its trigger is now sharper.** `internal-vault-pattern.md` `V-1` named a capability nothing on either shelf provides: **invalidating a record because the rule that generated it became wrong.** That is a much smaller thing than a front door — a checker that runs against a corpus, not a system anyone queries. If the census shows a wrong-rate that justifies it, that is what gets built, and it sits behind whatever front door we picked rather than replacing it.

## Reversal triggers, named

| Trigger | Consequence |
| --- | --- |
| AI Operations declines the Drive connection, **and** the census shows Drive holds the majority of decision-grade knowledge | Gemini Enterprise reopens as a Vendor Intake, on evidence |
| AI Operations confirms we cannot manage sources and configuration directly | Control becomes the deciding factor rather than cost; §1's second condition fails and the comparison restarts |
| MCP connectors cannot attach to a Claude enterprise-search project | Lucid is unreachable from Ask Commerce; if Lucid proves load-bearing, this becomes a build trigger rather than a platform one |
| The entitlement re-check shows Gemini Enterprise is already covered | The cost argument weakens. The duplicate-surface objection survives it and is sufficient on its own — reopen only with the census behind it |

## What this does not decide

- **Not whether we build.** That waits on the census wrong-rate, as it has since revision 1.
- **Not the capture design.** `V-1`, `V-2` and `V-3` set requirements for it (invalidation must cover the generator; conflicts must surface where the reader looks; a named owner, scheduled execution and a visible heartbeat) and none of them chooses a shape.
- **Not Lucid.** Two open questions — whether MCP attaches to an enterprise-search surface, and whether adding one triggers the `G2` AppSec review — decide whether it is reachable at all.

## Why not the alternatives

**Why not keep researching**: two independent scans converged, and the category is commoditised. Additional scanning would defer the decision it is meant to inform.

**Why not build now**: the wrong-rate is unmeasured, and `REQ-7` prefers configuration. The custom case has narrowed to one capability rather than widened to a product, which is an argument for patience, not urgency.

**Why not run a full bake-off**: it would cost a week to produce a verdict we can already reach on approval route alone, and it would produce no gap list — which is the artifact the next three decisions need.
