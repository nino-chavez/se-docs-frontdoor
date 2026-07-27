# ADR-0001 — Configure-first: the Stage 2 "prototype" is a Claude Tag pilot protocol, not code

- **serves**: `se/JOB-1`, `sponsor/JOB-1` — the delivery-path choice determines whether the SE ever gets a cited answer, and it is the load-bearing input to the sponsor's authorize-and-fund decision. Jobs defined in `research/personas-and-jtbd.md`.
- **Status**: accepted, and **largely overtaken by events**. Configure-first is confirmed correct; `Ask Commerce` already implements it org-wide (`research/prior-art/ask-commerce.md`). The Claude Tag pilot this ADR specifies as Stage 2 is superseded — Stage 2 becomes an evidenced AI Operations intake request. The contingent build branch is effectively dead. See the 2026-07-27 (later) amendment, which supersedes the one beneath it.
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

**Trigger 3 lost its reference implementation.** Sibling-scan re-derivation on 2026-07-27 found that `~/Workspace/dev/archive/knowledge-index` — named in the research corpus as the contingent crawl-and-index seam for this ADR's trigger 3 — no longer exists anywhere on the filesystem. Workspace drift, not a research defect. The consequence is real: if trigger 3 fires, the fallback architecture has no reference implementation to adapt, so that branch is more expensive than this ADR assumed when it was written. Weigh it when the corpus census establishes whether CMS-backed internal doc sites are actually in pilot traffic.

**Unaffected.** Buy stays retired; nothing in the kickoff restores either ACL-sync or seat-economics justification. `READ-ONLY v1` stands as written — and its escape clause is now load-bearing, because the kickoff introduced a capture-standard concern (recording knowledge going forward) that is a write system by definition. That is BD-1 in the problem statement, and this ADR's requirement that reopening read-only needs its own ADR is what makes BD-1 a real decision rather than a drift.

**Also invalidated by the restatement, though not part of this decision:** the "demand-driven filing" commitment in the standing-design-commitments list above. It presumes content exists and is misplaced. It does nothing where documentation was never written because billable hours ended, which the kickoff established as a structural rather than incidental failure.

### 2026-07-27 (later) — SUPERSEDES the amendment below: configure-first is correct and already executed by another team

The amendment immediately following was written from two stale governance registers and reached the wrong practical conclusion. Direct inspection of internal Confluence and the live Claude deployment the same day corrected it. Both are kept; the superseded one is instructive about method, not about this decision.

**What is true.** Claude is deployed to **every Commerce employee** with no approval gate, usage-based at a $1,000/person monthly cap, spanning claude.ai, Desktop Chat, Cowork and Claude Code. There is a dedicated AI Operations team. And **`Ask Commerce` — Anthropic's native ask-your-org surface — already runs org-wide** with Confluence, Jira and Slack connected, per-user permission scoping, numbered citations with last-modified dates, explicit conflict-surfacing, and a 12-month staleness flag. Full detail in `research/prior-art/ask-commerce.md`.

**This decision is vindicated and mostly obsolete at once.** Configure-first was right — so right that another team reached the same conclusion independently and shipped it at org scale before this initiative finished its research. Six of the decision memo's seven guiding principles are already implemented in production. The Claude Tag pilot this ADR proposes as Stage 2 would be a smaller, later, worse-scoped version of a live system.

**What changes:**

- **The contingent build branch is effectively dead.** Trigger 2 (tier-label inadequacy) and trigger 4 (telemetry ceiling) were arguments for putting a bot in the middle of a surface that now exists and is owned by another team; this initiative would not be the one to rebuild it. Trigger 1 survives in transformed form — see below. Trigger 3's reference implementation was already lost (amendment below), which now matters less rather than more.
- **Trigger 1 was right and is now concrete.** Shared-Drive visibility was named at founding as the riskiest assumption. It is confirmed: Ask Commerce's own configuration states Drive is pointed to but **not a connected source** — it can surface Drive files and cannot read their contents. The tech scopes and SA project folders live in Drive. The trigger's resolution is not a custom build; it is an AI Operations intake request (`AC-1`).
- **A gap the ADR never anticipated.** Ask Commerce structurally **demotes** team- and project-space pages, naming `SE`, `TAM` and `IPM` among others, and has no authoritative-source entry for solution knowledge at all. So 3,173 Confluence pages are searchable and can never be a source of truth (`AC-2`, `C-4`). Standing, not coverage, is the binding constraint on the Confluence portion of the corpus.
- **Stage 2 is not a pilot protocol.** It is an evidenced intake request to AI Operations: connect Drive, and establish an authoritative source for solution knowledge. The census is what makes the second half actionable, which is why Phase 0 is gating rather than preliminary.

**The strongest thing found, and it argues for the memo rather than against it.** Ask Commerce's instructions carry hand-written workarounds for specific corpus contradictions — a channel name that appears two ways on one page, two IT pages disagreeing on a GitHub org name. Each contradiction becomes a bespoke line of configuration maintained by one team. That is `P4` in production and the mitigation is O(contradictions) in human effort. **Retrieval is absorbing capture failure as manual debt.** `READ-ONLY v1` still stands as written, but `BD-1` — whether the capture standard sits inside this initiative — is now the decision that carries the initiative's remaining value.

### 2026-07-27 — SUPERSEDED: internal AI governance registers: the vendor surface is unverified, the pattern holds

> Superseded by the amendment above, written the same day. Retained because the failure mode is worth keeping: two internal registers were read carefully and treated as current, and the pessimistic reading was acted on without an independent source-pull. The hedging was correct and the conclusion was still wrong.

Two internal Confluence pages were read into the corpus on 2026-07-27. Findings and their grades are in `research/current-state/ai-governance-constraints.md`; only what bears on this decision is recorded here.

**The decision is not reversed, and the qualification is narrower than it first looks.** Configure-first was never a bet on Anthropic. What this ADR concretely proposes — a **Claude Tag pilot** — is now unverified on two independent grounds, either of which is enough to stall a pilot that assumed it could start immediately.

**One: the approved-input class.** The software register lists **Claude (Desktop)** under *Restricted*, input limited to unidentifiable and public data, and lists no Claude surface under *Approved* (`G4`). The SE corpus is Submit-for-Approval data at minimum (`G1`). This **conflicts** with the founding session's record that commerce runs Claude in Slack on Enterprise seats with a live MCP connector performing writes, and that all SEs are seated. The conflict is recorded, not adjudicated — per this ADR's own third standing commitment. Note the reading that is invisible from either source alone and is the dangerous one: **deployment is not authorization.** Seats can be live while the approved input class stays narrow.

**Two: beta.** The founding session describes Claude Tag as *Beta, Team/Enterprise only*. The register states BETA software is not approved by default. Even granting the most favourable reading of the first point, the specific surface this ADR names needs its own approval before a pilot runs on it.

**What this changes in practice.** Nothing about configure-first. Something about *which configured surface*. `G5` records that **NotebookLM Pro is already approved with an input class spanning Non-public, Customer, Sensitive and Partner data** — a superset of what the corpus holds — with output restricted to internal, which matches this initiative's audience under every reading of `BD-2`. Its connector reach and citation behaviour are unassessed and may disqualify it; that assessment has not been done and this ADR does not pre-empt it. But a configured path whose approval burden is plausibly near zero now exists as a named alternative to one whose approval status is open on two counts.

**Do not resolve this from the documents.** Both registers are internal, one is eighteen months past its recorded annual review and banner-marked "Currently In Review", and the page links a separate *Approved GenAI Tool List* that may be the authoritative roster. The resolution is one conversation with GRC (`#compliance-grc`), and it should be treated as a prerequisite to Stage 2 rather than a task inside it.

**Newly relevant to trigger 3.** Gong is an approved integration and Make AI (Enterprise) is approved tooling (`G6`), so the Gong path is not a governance dead end. The trigger's actual question — connector *reach* — is unchanged and stays technical.
