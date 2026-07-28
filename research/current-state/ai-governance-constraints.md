# AI governance constraints — what commerce.com already permits

**Doc type**: Reference (Diátaxis) — Look things up. Owns the approval routes, data classification, and tool status as `G1`–`G8`.
**Date**: 2026-07-27
**Status**: canonical for tooling and data-handling constraints. Supplements `research/problem-space/problem-statement.md`; does not supersede it.
**Derived from** two internal Confluence pages, supplied by the operator on 2026-07-27:
- *Approved/Not Approved AI Use Case* — the data-classification taxonomy, the per-integration approval register, and per-tool safe-usage guidance.
- *Approved/Not Approved Software/Hardware* — the software register, including GenAI tools split across Not Approved / Restricted / Approved. Banner reads **"Currently In Review"**. Document Classification: **SENSITIVE**. Version 1.2, last annual review 2025-01-07.

## What this document is, and the governance call it embodies

The two source pages are internal and one is classified SENSITIVE. This repo is private but sits on a **personal** GitHub account. `HANDOFF-INTERNAL-ACCESS.md` names that as a decision to make deliberately rather than drift into, and asks for the decision to be written down. **This is the decision:**

> Derived constraints, thresholds, and structural findings are recorded here. The source registers are **not transcribed** — no full approved-software table, no integration-by-integration risk-and-owner roster, no named internal staff beyond what a constraint cannot be stated without. Where a specific row is load-bearing for a decision in this initiative, that row is quoted minimally and attributed to its page. The originals stay in Confluence.

This mirrors the recommendation already standing for the Phase 0 census: **counts, distributions, and structural findings travel; raw content does not.**

**Recency caveat, and it is not decorative.** The software register is banner-marked "Currently In Review" and its last recorded annual review is 2025-01-07 — roughly eighteen months stale at time of reading. It carries a date typo (`Aug 30, 2202`), several dead internal links the page itself annotates as "Can't find link", and a deactivated account as the approver of record on nearly every version row.

> ## Correction, 2026-07-27 — the caveat above was load-bearing and this document under-weighted it
>
> The first version of this file was written from the two registers alone. Direct inspection of internal Confluence and the live Claude deployment later the same day **reversed `G4` and voided `G5`'s recommendation.** Both are corrected in place below and the superseded reasoning is retained, because the failure mode is more instructive than the finding.
>
> **What went wrong:** a stale artifact was read carefully and treated as current. The hedging held — three readings were offered and "the register is stale" was one of them — but the *practical conclusion drawn* (treat the Claude surface as a Stage 2 blocker) acted on the pessimistic reading without an independent source-pull. Reading one document more closely cannot correct for not having read a second.
>
> **The corpus-wide lesson, which is this initiative's own thesis turned on itself:** the register is a governance artifact that is *wrong rather than merely old* — `P4`, in the document that governs the initiative. Its staleness is not visible from its contents. Only an external source exposed it. That is exactly what the memo argues about the SE corpus, and it is why *recency is correctness* has to be a design invariant rather than a nicety.

Read alongside: this document is itself a specimen of `P4` — a governance artifact that is wrong-or-uncertain rather than merely old, whose reader cannot tell which. That is the defect class this whole initiative exists to address, found in the document that governs it.

---

## `G1` — There is a data-classification taxonomy, and the SE corpus is not in the free tier

The AI use-case page defines input data types with three approval routes: **Approved** outright, **Submit for Approval**, and **Not Permitted**.

| Route | Classes |
| --- | --- |
| Approved | Unidentifiable Data; Public Data |
| Submit for Approval | Customer Data (no PII); Partner Data (no PII); Non-public Data; Sensitive Data |
| Submit for Approval **+ Privacy Assessment** | Customer/Prospective-Customer PII; Partner PII; Website-Visitor PII; Employee/Contractor PII |
| **Not Permitted** — no approval path stated | **Shopper PII** |

Two definitions carry directly onto this initiative's corpus. *Non-public Data* is defined to include "generic internal correspondence, product information". *Sensitive Data* is defined to include "IT infrastructure mappings".

**Derived, not attested — the census must confirm it.** Reading those definitions against the sources named in the kickoff:

- Tech scopes and SA project folders describe customer store configuration and architecture → at minimum **Customer Data**, and **Sensitive Data** wherever a solution diagram constitutes an infrastructure mapping.
- Any of those that name a customer's employees — which scoping documents routinely do — pull in **Customer PII**, which adds a privacy assessment.
- Internal Slack, Gong call content, and a decade of SA direct messages are **Non-public Data** at minimum.

**So the corpus this initiative wants to index sits in Submit-for-Approval territory across the board, and touches the privacy-assessment tier.** Not one document in the named source list is plausibly Approved-by-default. This is not a blocker; it is the shape of the work.

## `G2` — The sponsor's "two-month floor" has a concrete front door

The sponsor placed the delivery floor at two months and attributed it entirely to security review and hosting overhead (00:31:14). That review is not an unknown. It is a named process with named intake paths:

- **AI Use Case Approval Form** — free AI software and AI use-case review.
- **GRC & Security Use Case Intake Form** — AI review, data-use review, privacy review, FOSS.
- **Vendor Intake Form** — paid subscription or purchase.
- **Policy Exception** — a standard, an intake form, and tracking, for anything the register forbids.
- Slack `#compliance-grc`; PoCs additionally take a Jira ticket in the GRC project.

**This retires an unknown and replaces it with an estimate nobody in this initiative has yet made:** how long the AI Use Case review actually takes for a Submit-for-Approval corpus. That is answerable on the internal machine, and it is the single cheapest correction available to the memo's timeline discussion.

**Route resolved 2026-07-27.** The canonical GRC page — *AI Responsible Use Process, Workflow, and Resources* (v7, 2026-05-27), which supersedes the older Legal-space page and is the source Ask Commerce itself treats as authoritative — opens with "Almost all AI usage requires review and approval" and splits the process three ways. This initiative is unambiguously **Use-Case #2: an existing approved tool processing a new type of data.**

That means: **an AI Use Case Review, including Privacy Impact Assessment questions where PII is involved.** Not a Vendor Intake Form, because Claude is already a procured and approved tool — the expensive path is the one this initiative does *not* take. Contact is `ai-review@commerce.com`.

Duration remains unmeasured. Two known cost drivers, from the SOP's process steps: an **AppSec review is triggered by new or updated MCP, integrations, open-source software, or custom code**, and escalations requiring an ethical or regulatory decision go to an **AI Review Committee that meets quarterly** — a tail risk that could exceed the sponsor's entire stated two-month floor on its own. A configured path that adds no custom code and no new MCP avoids the first entirely.

## `G3` — Proof-of-concept rules forbid the obvious Phase 0 / Phase 1 shortcut

During a PoC the register permits only: public or dummy data as input, **no connections to other tools or systems**, and no use of output in the codebase — the stated reason being that a free trial does not carry the contractual protections.

**Consequence for this plan.** A "quick pilot pointed at the real tech-scope folder" is not a PoC under this policy. It is a production data flow over Submit-for-Approval data, and it needs the approval before it runs, not after it proves value. Phase 1's shape — a question surface over the highest-trust subset — must be scoped against an *approved* tool with an *approved* input class, or it must carry its own approval. Phase 0 is unaffected: counting and characterizing documents is not an AI use case unless an AI tool does the counting, which is a design choice this constraint should now influence.

Related: **BETA software is not approved by default**, and free or trial tiers are not for official business use absent Security/Legal/Privacy sign-off. Any pilot design resting on a preview feature is out before it starts.

## `G4` — CORRECTED: Claude is deployed org-wide with no approval gate. The register is stale.

> **This finding was reversed on 2026-07-27.** The original reading is preserved beneath the correction because the reasoning pattern matters more than the conclusion.

**What is actually true**, from the internal AI Operations `Claude Knowledge Hub` (reviewed July 2026) and direct inspection of the live deployment:

- **Every Commerce employee has Claude.** No application, no approval, no license request. Stated in those terms on the hub page.
- Access is **usage-based, not seat-based** — a **$1,000 monthly spend cap per person**, resetting on the 1st. Contrast ChatGPT, which is seat-limited to 1,000 purchased licenses with 30-day inactivity revocation.
- Surfaces in use: **claude.ai** (web/mobile), and Desktop Claude covering Chat, Cowork, and **Claude Code**. Entry is the Claude tile in Okta.
- Connectors (MCP) for Atlassian, Gmail, and Google Calendar are user-enablable.
- A dedicated **AI Operations team** owns Projects, Skills, Plugins and an intake form. `Ask Commerce` runs org-wide on this deployment — see `research/prior-art/ask-commerce.md`.
- The GRC **AI Registry** (2026-04-01) records *Anthropic — Claude (Desktop, CLI) — Medium risk — **Confidential** data classification — human-in-the-loop — SEC-AI-001*. Broader than the software register, newer, and it explicitly includes CLI.

**The cap is real and it binds.** An attempt to run empirical questions against Ask Commerce on 2026-07-27 was refused for having reached the monthly spend limit. That is a live input to `BD-4`, which previously had none: routing SE question traffic into Claude makes per-person caps a capacity question.

**Consequence for `ADR-0001`:** the configure-first path is not blocked, was never blocked, and the beta concern below is moot for the surface that matters — `Ask Commerce` is generally available and in production use, not a beta pilot. The ADR's third amendment is rewritten accordingly.

---

**Superseded reading, retained deliberately.** What follows was the original `G4`, written from the software register alone. It is wrong in effect. It is kept because the corpus should show its own corrections rather than quietly absorb them, and because the register text it describes is still on the page today — anyone reading that register without the AI Operations context will reach the same wrong conclusion.

The load-bearing finding, and it lands on `decisions/0001-configure-first-pilot-as-prototype.md`.

Under **Restricted Software → GenAI**, the register lists **Claude (Desktop)**, any version, any OS, with legal approval details stated as:

> Input: Unidentifiable data; public data — Output: Internal Only

Under **Approved Software → GenAI**, Claude does not appear in any form. Claude Code does not appear anywhere in the document, in a table where Cursor CLI, Codex CLI, Gemini CLI, OpenCode, Supersert CLI and Salesforce CLI each appear *with* linked secure-use guidelines.

**State this precisely, because the overclaim is tempting.** The finding is: *in this document, Claude is Restricted to unidentifiable and public data as input, and no Claude surface appears as Approved.* The finding is **not** that Claude is prohibited — the page links a separate *Approved GenAI Tool List* that may carry entries the tables do not, and the page is eighteen months past review with a "Currently In Review" banner.

**This conflicts with a first-party claim already in the corpus, and the conflict is not resolved here.** The founding session records that "commerce runs **Claude in Slack on Enterprise seats** with the **Atlassian/Jira MCP connector live** and performing writes", and that "**all SEs have Claude Enterprise seats**" (`research/sources/definition-and-grill-2026-07-09.md`). ADR-0001 rests on both. Set against a register that lists Claude only as Restricted, that is two first-party sources disagreeing:

| Reading | What would make it true |
| --- | --- |
| The register is stale | Seats and connectors were approved after 2025-01-07 and the page never caught up. Its own "Currently In Review" banner and dead links make this plausible. |
| The register is current, and the approval lives elsewhere | The separate *Approved GenAI Tool List* carries the Enterprise entry; the in-page table only ever covered the desktop client. |
| Both are accurate about different things | Enterprise seats are deployed and in use, while the *approved input class* for them remains unidentifiable/public — deployment is not authorization, and a live MCP connector says nothing about what data may pass through it. |

The third reading is the one that should worry us, because it is invisible from either document alone and it is the one under which the pilot proceeds confidently and wrongly. **Surface the conflict; do not adjudicate it** — this initiative's own third design constraint, applied to itself. GRC resolves this, not us.

**A second collision, sharper than the first.** ADR-0001's Stage 2 deliverable is a **Claude Tag** pilot protocol. The founding session describes Claude Tag as **Beta, Team/Enterprise only**. The software register states plainly: *BETA software (software not available for General Audience) is not approved by default.* So even on the most generous reading of the Claude approval question, the specific surface the ADR proposes is beta, and beta needs its own approval before a pilot runs on it.

**What this does to ADR-0001.** Configure-first survives; it was never a bet on one vendor. What does not survive unexamined is *configure-first on a Claude Tag pilot*, which is what the ADR concretely proposes and what the sponsor twice reached for. Three outcomes, all distinguishable in one conversation with GRC: an approval exists that these pages do not reflect; the surface needs a policy exception (time — and the timeline floor is exactly what configure-first was chosen to avoid); or the configured path should be an already-approved tool with an adequate input class, which is what `G5` describes.

Recorded as a third qualification on ADR-0001's Amendments section, not as a reversal.

## `G5` — CORRECTED: NotebookLM Pro's approval breadth is real; the recommendation built on it is void

> **The factual claim below stands. The conclusion drawn from it does not.**

The register entry is accurate: NotebookLM Pro is approved for every input class except Shopper PII, output internal-only. That remains the broadest stated input authorization on the approved list.

**But the argument it was carrying has collapsed.** The recommendation was "cheapest configured path by approval burden" — and that rested on `G4`'s premise that the Claude path carried an unresolved approval question. It does not. Claude is deployed org-wide with no approval gate, and `Ask Commerce` already runs on it with Confluence, Jira and Slack connected, citations, conflict-surfacing and staleness flags in production (`research/prior-art/ask-commerce.md`).

Approval burden does not discriminate between the two options, so it cannot decide between them. **NotebookLM Pro is not disqualified — it is simply no longer privileged**, and would now have to win on fitness (connector reach, citation behaviour, refresh semantics, corpus scoping) against an incumbent that already serves the whole company. On current evidence it does not, and no assessment is planned.

Recorded so a future reader does not revive the recommendation without the premise.

---

**Original finding, retained for the factual record:**

Also under **Approved Software → GenAI**:

> **NotebookLM (Pro)** — Input: Unidentifiable, Public, Non-public, Customer, Sensitive, Partner Data. Output: Internal Only.

That is every class in `G1` except Shopper PII, which has no approval path anywhere. No other general-purpose GenAI entry on the approved list states input breadth that wide; the only comparable entries are two SAP enterprise-architecture assistants.

**This is the most consequential positive finding in either document.** It says a tool already exists, already approved, whose authorized input class is a superset of what the SE corpus contains, and whose output restriction — internal only — matches this initiative's audience under every reading of `BD-2`.

Three things it does not say, and they matter:
- Nothing about **connector reach**. Whether NotebookLM Pro can see Shared Drives, tech-scope folders, or Gong exports is a technical question this document does not touch. It is the same question `ADR-0001` trigger 1 asks of a different vendor.
- Nothing about **fitness**. Notebook-scoped corpora, citation behaviour, and refresh semantics decide whether it serves the question surface. Unassessed here.
- Nothing that **retires configure-first**. It strengthens it — it names a configured path whose approval burden looks materially smaller than the alternatives.

Note the correction this forces on the research corpus: `research/research-reference-grade.md` carries a NotebookLM claim as *"cited, not re-derived"* against a product-chooser page. That grade stands for the **external product claim**. The internal approval status recorded here is a separate, first-party fact and does not resolve it.

## `G6` — Per-source constraints for the census sources

Every source named in the kickoff, against the register. Approval status is the integration's, from the AI use-case page; the constraint is that page's safe-usage guidance.

| Source | Status | Constraint that bears on this initiative |
| --- | --- | --- |
| **Confluence** | Approved | Do not put pages containing sensitive customer data, credentials, or **proprietary technical architecture** into external AI tools. Solution architecture docs are squarely that. |
| **Gong** | Approved | AI-generated Gong output **must not be used for employee performance management**. A surface that summarizes who-knew-what across SA calls edges toward exactly that; design has to hold the line explicitly. |
| **Google Workspace / Drive** | Approved | Do not process regulated data (PII, PCI, sensitive financials) outside an explicitly approved workflow. |
| **Slack** | Approved | Do not put sensitive customer data, credentials, or **confidential deal information** into AI-assisted Slack workflows. |
| **Jira** | Approved | Avoid tickets carrying security-vulnerability detail or credentials. |
| **Make (Make AI, Enterprise)** | Approved | The Gong→Make pipeline the kickoff described runs on approved rails. |
| **GitHub** | **Not Approved** | Register requests a business case. Relevant only if a build path needs it. |

**`ADR-0001` trigger 3 is partly answered.** Gong is an approved integration and Make AI is an approved tool, so the Gong path is not a governance dead end. The trigger's actual question — whether a standard connector can *reach* Gong content — stays open and stays technical.

**A constraint the deferred Slack front door has to answer.** `se-frontdoor-slack-channel` is deferred in the manifest. When it is revisited, note that an SE asking about a live client engagement is, routinely, confidential deal information. That is a design constraint on the surface, not a reason to abandon it.

## `G7` — Prior art: the company already buys and approves reasoning layers over internal data

Two approved entries are direct prior art for the shape this initiative proposes, and neither appears in `research/prior-art/capture-domain-prior-art.md`:

- **Actively** — a GTM intelligence layer that "unifies and reasons over" Salesforce and Snowflake data. Approved, with a stated boundary: stay within the approved sources, and a new data connection requires a fresh risk assessment. That boundary condition is the template for how this initiative's source list will be governed as it grows.
- **Discoverist AI** — an internally-approved *merchant AI support product*, input spanning Public/Non-public/Unidentifiable/Customer, output **Internal and Public**, carrying an approved security exception. An AI answer surface over commerce knowledge that has already cleared security. Whatever it is, someone here has already walked the path this initiative is about to walk.

Neither is "ask commerce" / CLA. **`BD-3` is untouched by these documents** — no entry in either register matches the sponsor's description. But both prove the approval shape exists and has been navigated, which lowers the prior on `BD-3`'s answer being "no such thing exists."

## `G8` — What remains open, after the 2026-07-27 corrections

**Resolved since first writing:**

- ~~The authoritative GenAI roster.~~ Settled. The SOP names *Approved/Not Approved Software/Hardware* (page `19368090`) as the record of approval, and Ask Commerce's own configuration treats it as authoritative — "if a tool is not listed on this page, it is NOT approved." The current canonical *process* page is *AI Responsible Use Process, Workflow, and Resources* (`2887843868`). The register being the system of record is precisely why its staleness on Claude matters beyond this initiative: **it is stale in the authoritative direction**, and Ask Commerce is instructed to treat absence from it as a negative answer.
- ~~MCP servers, undetermined.~~ Partly settled, and better than "undetermined": MCP is not a blank in the process — it is a **named trigger for AppSec review** in the SOP's process steps. A design that adds no new MCP avoids that review entirely.
- ~~`BD-3`, unmoved.~~ **Resolved.** See `research/prior-art/ask-commerce.md`.

**Still open:**

- **Review duration.** `G2` names the route precisely and still has no clock on it.
- **Connector reach.** Governance is not what stops Ask Commerce reading Drive — connection is (`AC-1`). Whether AI Operations will connect it, at what cost, is unasked.
- **Whether a domain-knowledge authoritative source is grantable** (`AC-2`). Every existing entry is owned by a governance or platform function. Solution knowledge would be a new category.
- **The empirical probe of Ask Commerce.** Blocked on the per-person spend cap, not on access or permission.

---

# Reference — citation handles

`G1` corpus sits in Submit-for-Approval territory · `G2` the route is Use-Case #2, an AI Use Case Review; duration still unknown · `G3` PoC rules forbid real-corpus prototyping · `G4` **corrected** — Claude is deployed org-wide with no approval gate; the software register is stale · `G5` **corrected** — NotebookLM Pro's approval breadth is real but no longer privileges it · `G6` per-source constraints · `G7` internal prior art for reasoning-over-internal-data · `G8` what remains open

Two handles cite outward: `AC-1`–`AC-4` are in `research/prior-art/ask-commerce.md`; `C-1`–`C-4` are in `research/current-state/confluence-corpus-census.md`.

Convention matches `research/problem-space/problem-statement.md`: prefer the claim in prose and attach the handle.
