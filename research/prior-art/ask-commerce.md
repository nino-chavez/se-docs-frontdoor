# Ask Commerce — BD-3's answer, and most of Phase 1

**Date**: 2026-07-27
**Status**: canonical for what already exists. Resolves `BD-3`.
**Derived from**: direct inspection on 2026-07-27 of the live system at `claude.ai/ask-your-org`, its Project instructions panel (visible to any employee with the Project open, per its own Confluence documentation), and the `Ask Commerce` and `Claude Knowledge Hub` pages in the internal AI Operations space.

> **Governance.** Same rule as `ai-governance-constraints.md`: derived findings and minimal quotes travel; the system prompt is **not** reproduced here. It is roughly 4,000 words of internal operational configuration and it stays in the tool.

---

## The answer to BD-3

`BD-3` asked whether an existing internal assistant already owns this surface. The problem statement recorded it as **the question that most changes the plan**, on the reasoning that if such a system existed and already held security and hosting approvals, the sponsor's stated two-month floor was composed entirely of those approvals.

**It exists. It is live. Every employee already has it.**

| Field | Value |
| --- | --- |
| What | `Ask Commerce` — Anthropic's native **ask-your-org** surface, at `claude.ai/ask-your-org` |
| Owner | AI Operations team (`ai-ops@bigcommerce.com`), with a documented intake form |
| Status | Active. Reviewed June 2026 |
| Audience | All Commerce employees. Shared org-wide, appears in the Claude sidebar by default, **no access request** |
| Connected sources | Confluence, Jira, Slack |
| Model | Opus 4.7, adaptive thinking, set at the Project level |
| Permissions | Respects each user's existing per-source access. Surfaces nothing the asker could not already see |

**The sponsor was not reaching for an analogy.** "Something similar to ask commerce that we do for everything within commerce" (00:09:27) and "maybe if it's directly within CLA, like ask commerce" (00:33:23) name the actual production system. The answer to his question is that the thing he described already runs.

One correction to the framing this initiative carried: **Commerce did not build it.** `ask-your-org` is an Anthropic product surface that AI Operations configured and instructed. That is configure-first, executed, by another team, at org scale — which is `ADR-0001`'s conclusion arrived at independently and already in production.

## What it already does that this initiative planned to build

The decision memo commits to seven guiding principles. Six are implemented:

| Memo principle | Ask Commerce today |
| --- | --- |
| Cite everything, or say nothing | Every factual claim carries a numbered inline citation; answers end with a References section giving source name, **date last modified**, and URL. Its instructions forbid inventing URLs, ticket numbers, owners, or dates |
| Recency is correctness | Sources over 12 months old on fast-moving topics are flagged in the answer, and the last-updated timestamp is checked on every source relied on |
| Surface conflicts, do not adjudicate | On unresolved conflict it is instructed to surface it rather than pick silently, and to name both sources with their dates |
| Assume no schema | Federated search across three systems; no structural assumption about any document |
| Coverage follows verified quality | A source hierarchy plus explicit demotion rules — see below |
| Answers are a starting point | Staleness and DRAFT flags are framed as risk signals; high-stakes answers are routed to source verification |

The seventh — *measure against the person* — is a measurement question, not a product capability, and remains this initiative's to answer.

**Two design patterns worth stealing outright**, because both address problems this initiative had open:

- **Reasoning about absence.** For approval questions, absence from the authoritative list *is* the answer — not "I couldn't find it." Encoding what a null result means is precisely the discipline that a corpus with structural holes (`P2`) requires, and the founding research never named it.
- **A source hierarchy with explicit demotions.** Confluence is authoritative for policy and process; Jira for project state; Slack is a context layer that may not be cited as sole source for a factual claim where a Confluence or Jira equivalent exists. Demoted outright: DRAFT pages, team- and project-space pages describing tool setup, personal-space pages (`/spaces/~`), and anything over 12 months on a fast-moving topic.

## The gaps — where this initiative's work actually is

### `AC-1` — Drive is not readable, and the SE corpus lives there

Ask Commerce's own configuration states it plainly: Google Drive is pointed to but **not a connected source**; it can surface Drive files in search results and cannot read their contents. The instructions carry at least one hardcoded Drive URL specifically annotated as unreadable, with the fallback being to hand the user the link.

The tech scopes and SA project folders — the corpus the sponsor proposed starting with (00:30:03) — live in Drive. **The one system that already solves retrieval is blind to the most important SE source.**

This is `ADR-0001` trigger 1 (Shared-Drive visibility) resurfacing in concrete form. It is no longer a connector-capability unknown to be tested; it is a request to file with AI Operations.

### `AC-2` — Solution knowledge has no authoritative source, and its spaces are structurally demoted

The sharper gap, and the one that was invisible until the instructions were read.

The authoritative-source routing table covers GRC (tool approval, AI process), PEOP (HR), Equity & MNPI, Claude/ChatGPT access, and IT (deployment). **There is no entry for SE or SA solution knowledge.**

Worse, the demotion rules name the relevant spaces directly — `SE`, `TAM`, `IPM`, `DS` and others are called out as not authoritative. So the 3,173 Confluence pages counted in `confluence-corpus-census.md` are searchable but can never be treated as a source of truth by the system that searches them.

**The ask to AI Operations is therefore two things, not one:** connect Drive, *and* establish an authoritative source for solution knowledge. The second needs the census to justify — which is what makes Phase 0 the gating work rather than preliminary work.

### `AC-3` — Gong is not connected

Named in-scope at kickoff, absent from the connector list. Governance is not the obstacle (`G6`); connection is.

### `AC-4` — Capture is untouched, and the system is visibly straining against it

No retrieval surface writes the retrospective nobody wrote (`P7`). But the strain is now observable rather than theoretical, and that is the most useful thing found this session.

Ask Commerce's instructions carry **hand-patched workarounds for specific corpus defects**:
- A GRC page contains two different Slack channel names for the same channel; the prompt hardcodes which is correct.
- Two IT pages disagree on the GitHub organization name, so the prompt instructs the assistant not to state it with confidence and to route the asker to a human instead.

Each contradiction in the corpus becomes a bespoke line of prompt configuration, maintained by hand, by one team. That is `P4` and the conflict problem in production, and the mitigation does not scale — it is O(contradictions) in human maintenance effort.

**This is the memo's central argument, evidenced from Commerce's own system rather than from theory.** Retrieval quality is bounded by capture quality; when capture fails, the retrieval layer absorbs the defect as manual configuration debt until it can't.

## Two operational facts with consequences

**The instructions carry a maintainer contract.** They open with a dated source-dependency list — roughly ten hardcoded Confluence page IDs, with a standing note that if any page is moved, renamed, or deprecated the instructions need updating, and that the list exists so page owners know their page is wired in. This is the founding grill's *authority tier* concept, running in production, with an explicit staleness contract and a named owner. Read it before designing anything in that direction.

**Usage is capped per person and the cap binds.** Claude at Commerce is usage-based rather than seat-based — every employee has access, with a $1,000 monthly spend cap that resets on the 1st. This was discovered by hitting it: an attempt to run empirical questions against Ask Commerce on 2026-07-27 returned a spend-limit refusal and generated no answer. If this initiative routes real SE question traffic into Claude, per-person caps become a capacity and funding question. **That is a live input to `BD-4`, which had none.**

## What this does to the plan

- **`BD-3` is resolved.** No longer an open decision. The successor question — does this initiative live *inside* Ask Commerce — is now answerable, and the answer looks like yes-via-intake rather than build-alongside.
- **Phase 1 mostly collapses.** It stops being "configure a question surface" and becomes "file AI Operations intake requests, evidenced by the census." The surface exists; its coverage is the problem.
- **Phase 0 gets more important, not less.** The census is what converts `AC-2` from an opinion into a request AI Operations can act on.
- **Phase 2 is where the differentiated value now sits.** Fixing what gets written down is the part no existing system touches, and `AC-4` is first-party evidence that the gap is already costing another team real maintenance effort.

## Still unverified

- **The empirical probe did not run.** Real SE questions against Ask Commerce, recording what comes back, remains the strongest artifact for the first sponsor sync. Blocked on the spend cap, not on access.
- **Whether AI Operations will connect Drive**, and at what cost. Unasked.
- **Whether an SE authoritative source is a thing they grant.** Every current entry is owned by a governance or platform function (GRC, PEOP, IT). A domain-knowledge entry may be a different category of request.
- **Atlassian Rovo** appears in the GRC AI Registry and is a second Confluence-native candidate. Unexamined.
