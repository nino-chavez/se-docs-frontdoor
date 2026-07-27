# ADR-0001 — Configure-first: the Stage 2 "prototype" is a Claude Tag pilot protocol, not code

- **Status**: accepted — core decision stands; two qualifications added 2026-07-27 (see Amendments)
- **Date**: 2026-07-09
- **Source**: research/sources/definition-and-grill-2026-07-09.md (founding session + grill ledger)
- **Context changed**: research/problem-space/problem-statement.md supersedes the problem framing this ADR was decided against. Read that before applying this ADR.

## Context

Canonical Blueprint Stage 2 produces a built prototype (static portal, embedded prototype, or hybrid per `blueprint-prototype`). This initiative's primary path involves zero code: Anthropic ships the product (Claude Tag), commerce already runs Claude in Slack on Enterprise seats with the Atlassian MCP connector live, every SE is seated, and the grill established uniform ACLs — which killed the one requirement (caller-identity OAuth) that a custom build uniquely serves.

## Decision

**Why not canonical**: a built prototype would test the *fallback* while leaving the *primary path's* riskiest assumptions untested — Shared-Drive connector visibility (anthropics/claude-code#53442), prompt-level authority-tier labeling adequacy, and citation quality on the real corpus are only testable by configuring Claude Tag against commerce's live sources. **Disqualifier**: code cannot answer any of them. **Chosen alternative**: Stage 2 deliverables are a pilot protocol — channel instruction set, measurement plan (senior-SE deflection baseline + weekly-active backup), corpus census procedure, and go/no-go triggers — run in commerce's Slack/Claude admin.

## The build branch stays contingent, with named triggers

The thin-build (Slack Bolt `agent_view` app → Messages API tool use → federated retrieval tools returning `search_result` blocks → Citations API) activates only if the pilot fails on one of:

1. **Shared-Drive blindness** — Enterprise connector can't see Shared Drives (fix is three Drive-API params in a custom tool).
2. **Tier-label inadequacy** — prompt-level authority tiers / conflict-surfacing prove too lossy; deterministic formatting needs a bot in the middle.
3. **Scoping gaps** — Tag can't restrict Slack search to named SE channels or can't cover the CMS-backed internal doc sites that pilot traffic actually needs.
4. **Telemetry ceiling** — deflection measurement demands per-question logging Tag doesn't expose (only a trigger if manual survey + senior self-report prove insufficient).

Buy options are retired entirely: uniform ACLs + existing Claude Enterprise spend remove both of the buy lane's justifications (ACL-sync connectors, seat economics). Revive Onyx only if an indexed-RAG-with-ACL-sync requirement somehow returns.

## Standing design commitments (bind both branches)

- **Read-only v1, hard line.** No writes of any kind; revisiting is a deliberate v2 decision with its own ADR.
- **Wide corpus with authority-tier labels**; conflicts are surfaced and flagged, never silently adjudicated.
- **Citations on every answer**, deep-linked where the source allows.
- **Async-first**; no call-time fast lane in v1.
- **Demand-driven filing**: bot misses on trapped content (local files, NotebookLM uploads) route that content into Drive/Confluence; no pre-migration sweep.
- **Public-docs version rule**: answer from current-stable, label version-specific content.

## Consequences

- `execution.depth: lean` — Stage 1 is substantively banked in the founding session; remaining research work is backfill and the corpus census.
- Stage 3 documents (internal proposal to SE leadership) are the deliverable regardless of which branch wins; the initiative portal is the pitch surface.
- The pilot needs two humans before go-live: a Claude Enterprise admin (connector toggles + pilot channel) and 2–3 senior SEs (deflection baseline + "ask the bot first" redirect).

## Amendments

### 2026-07-27 — sponsor kickoff: configure-first stands, two qualifications

The decision is not reversed. Both directions of movement are recorded because the ADR reads as more settled than it now is.

**Strengthened.** The sponsor independently reached for a Claude-native surface twice without prompting — "could we have a claude, like something similar to ask commerce that we do for everything within commerce" (kickoff 00:09:27), and later "maybe if it's directly within CLA, like ask commerce" (00:33:23). Configure-first is the sponsor's own opening instinct, not an operator preference argued against the room. The sponsor also put the delivery floor at two months composed *entirely* of security review and hosting overhead (00:31:14) — overhead a configured path may largely avoid, which raises the cost of choosing a build.

**Weakened.** Gong call recordings are a named in-scope source and are already pulled via Make.com. Gong is not a standard Claude Enterprise connector. That is **trigger 3** of this ADR's own build conditions — "Tag can't cover the sources that pilot traffic actually needs." The trigger is not fired, because whether pilot traffic routes to Gong is unknown until the corpus census runs, but it is no longer hypothetical.

**Unaffected.** Buy stays retired; nothing in the kickoff restores either ACL-sync or seat-economics justification. `READ-ONLY v1` stands as written — and its escape clause is now load-bearing, because the kickoff introduced a capture-standard concern (recording knowledge going forward) that is a write system by definition. That is BD-1 in the problem statement, and this ADR's requirement that reopening read-only needs its own ADR is what makes BD-1 a real decision rather than a drift.

**Also invalidated by the restatement, though not part of this decision:** the "demand-driven filing" commitment in the standing-design-commitments list above. It presumes content exists and is misplaced. It does nothing where documentation was never written because billable hours ended, which the kickoff established as a structural rather than incidental failure.
