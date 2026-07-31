# Source — SE Docs Frontdoor sync, 2026-07-30

**Doc type**: Reference (Diátaxis) — Look things up. Owns what was decided and assigned on 2026-07-30, as `S-1`–`S-9`.
**Date**: 2026-07-30, 14:59 CDT, 30 minutes.
**Present**: Andrew Todd (sponsor), Mark Seung, Zac Abbruzzese, Alex Vela (AI Operations), Nino Chavez.
**Derived from**: the Gemini-generated notes and full transcript of the session. **Where the notes and the transcript disagree, the transcript wins** — see `S-1`.

---

## `S-1` — The meeting record contradicts itself, and the Decisions block is the wrong half

The Gemini notes carry two statements of the same decision that cannot both be true.

| Where | What it says |
| --- | --- |
| **Decisions → Aligned** | "The Phase 1 solution strategy is confirmed to function as a **document retrieval tool rather than an autonomous answer engine**." |
| **Details** | "The group reached a **consensus that the tool should function as an agent** that can interact with the knowledge base to produce answers, rather than just returning raw documents." |

**The Details block is correct and the Decisions block is wrong.** The transcript resolves it plainly. Nino asked the question directly at 00:20:08 — "are we looking for a document retrieval solution or an answer engine?" — and Andrew's reply at 00:21:17 was "How would you do that without an agent? Even the most basic, you'd need that." He closed at 00:23:10 with "just working how ask commerce works, I think is sufficient," and Ask Commerce is an answer engine with citations, not a file-listing tool.

The likely source of the error is Andrew's phrase at 00:23:10 — "it's returning data" — read out of context. In context that sentence is about **who the answer is written for**, not about what the system produces: "we treat this as if the person asking the question has context and understands the data."

**Recorded as its own finding because of what it is.** A governance artifact that is *wrong rather than merely old*, whose staleness is invisible from its contents, and which a reader would act on confidently. That is `P4`, produced by an AI summarizer, about a meeting whose subject was fixing exactly this defect. Anyone who reads only the Decisions block builds the wrong thing.

## `S-2` — It is an answer engine, and the reader is assumed to have context

The decision, stated correctly: **an agent over the corpus that produces answers with citations**, not a search that returns files.

The paired design assumption is Andrew's and it is what makes the decision safe: *for Phase 1, we treat the asker as someone who has the context to evaluate the answer.* His framing — build it for the key people it is meant to serve, and if it later works for everyone else, good, but that should not change how we start.

This confirms and sharpens the audience constraint added in plan revision 2. The audience test is not *who benefits*; it is *who can evaluate an answer that might be wrong*. Andrew said outright that some answers will not be right, and that this is precisely why access is limited.

## `S-3` — Phase 1 audience: SE, SA and TAM. TPM deferred, on Mark's caution

Mark: SAs and TAMs are where it makes most sense. TPMs are "a tricky one" — he put himself at 50/50 and named the reason: the results carry nuance, and he did not want them forwarded to clients unreviewed. Andrew's concern was the same one from the sales side: "I don't want the salesperson just giving out answers to the customers without speaking to us first."

**Two corrections this forces on the plan.** The audience is SE/SA **and TAM**, not SE/SA — TAM was not in the plan's scope. And the reason for the boundary is now on record: it is about *forwarding unreviewed answers to clients*, which is a sharper and more defensible line than "technical context."

**TAM's inclusion has a second consequence nobody raised.** The census found TAM is the only corpus in the estate that is not decaying — 57% touched in twelve months against 19–21% for SA and IPM under identical billing pressure. TAM is now both a user and the one group whose documentation practice already works. The plan's open question — *ask TAM what they do differently* — stops being a research errand and becomes a conversation with a stakeholder.

## `S-4` — Scope is confirmed as analysis, not redesign

Andrew: the team should not unilaterally dictate the company's long-term data-storage strategy. It is responsible for identifying where data lives today and what the limitations are, and presenting that to leadership — Shane named — so they can decide on any shift.

**This ratifies the §3 reframe already landed in plan revision 2.** It arrived independently, from the sponsor, in the same words. No further change needed; the plan was ahead of the meeting on this one point.

## `S-5` — Commerce moved to full Google Enterprise accounts, and this undercuts a rejection premise

Alex Vela, at 00:04:31: within the last week or two the company transitioned to a different class of Google Enterprise account. Previously it went through a third-party vendor with "a lot of the features but not everything"; now it is a "full Google Enterprise" arrangement that "can open up more stuff."

**This is the most consequential new fact in the meeting and it lands on `buy-landscape.md`.** The assessment of Gemini Enterprise rejected it primarily because it is a separate paid subscription, which routes it to a `G2` Vendor Intake rather than an AI Use Case Review. That reasoning was sound against the entitlement position as understood on 2026-07-29. **It may no longer describe what Commerce holds.**

Precisely what is now unsafe to assert: that adopting a Google front door necessarily requires a new purchase. What remains true and unaffected: Gemini Enterprise is a distinct Google Cloud product from Workspace, and the duplicate-surface argument (`P4` at the tool tier) stands regardless of licensing.

**Graded as `Reported`** — one participant's account of a recent change, given with hedges ("I think"). It is not yet evidence about entitlement. It is a reason to check, and checking is `S-7`.

## `S-6a` — Mark answered, and one of his three is invisible to every candidate

**Answered by email 2026-07-30, 22:23.** Mark named three "major ones":

| Source | Status against the front door |
| --- | --- |
| **Confluence — the `SA` space** | Connected to Ask Commerce today. 912 pages, 19% touched in twelve months (`C-1`) — the second-largest and second-stalest space in the census |
| **A shared Google Drive** | Not connected (`AC-1`). The identifier he supplied carries Google's shared-drive prefix, so this is a **shared drive**, not a personal folder — which is precisely the case `AC-1` is about |
| **Lucidchart** | **Not in this initiative's landscape at all until now.** No candidate front door reads it as configured |

**The headline is the overlap, and it is worse than the plan currently argues.** Ask Commerce connects to Confluence, Jira and Slack. Mark named Confluence, Drive and Lucid. **One of three.** The tool is connected to two sources he did not name and cannot read two he did.

`AC-1` framed the Drive gap as one missing source. On Mark's evidence it is closer to *the majority of what a senior SA reaches for is unreadable*. The census measured the Confluence corpus precisely and that corpus turns out to be a third of his working set.

**Note what is absent.** No Slack, no Jira, no Figma. Figma was **my speculation in the meeting**, not a report — the transcript has "Slack, Jira, Confluence, Google Drive, maybe Figma. I don't know what else" (00:04:31). Mark's answer supersedes the guess: **Lucid is the real third source and Figma should not be carried as one** until someone names it independently. Zac has not yet answered and may add to this.

### The Lucid finding, and the constraint it introduces

Lucid ships an **official Claude connector**, announced 2026, delivered as a **provider-hosted MCP server** (`mcp.lucid.app/mcp`) using OAuth with dynamic client registration. It searches documents, retrieves and summarises diagram content, and inherits Lucid's own permission model — which satisfies `REQ-3` without new access plumbing.

**But it is an MCP connector, and that has a governance cost this initiative has so far avoided.** `G2` records that an **AppSec review is triggered by new or updated MCP, integrations, open-source software, or custom code**. Every path chosen to date has deliberately added none of those. Connecting Lucid would be the first requirement to push this work out of the configure-only lane and into an AppSec review.

**Unverified and load-bearing**: whether an MCP connector can be attached to a Claude **enterprise-search project** at all, as opposed to an individual's chats and projects. Ask Commerce is the former. Its setup chooses connectors for Documents and Chat; nothing I could resolve says MCP servers can join that set. **If they cannot, Lucid is unreachable from Ask Commerce regardless of the connector existing** — and that is a sharper version of the same question `AC-1` asks about Drive. First thing to put to Alex Vela.

*Sources: Lucid's launch announcement and MCP server documentation, resolved 2026-07-31. The capability claims are `Read`; nothing has been observed running.*

### Governance note on the identifiers

Mark's email carries a live Confluence space URL, a shared-drive ID and a Lucid folder ID. **They are deliberately not transcribed here**, consistent with the rule in `ai-governance-constraints.md`: derived findings and structure travel into this repo, raw internal identifiers do not, because the repo is private but sits on a personal account. There is no precedent for internal URLs in this corpus and this is not the place to start one. The identifiers stay in email and go directly into the AI Operations request.

**One structural question they raise.** The census established that tech scopes live in an `Opportunities` shared drive organised by year (`C-5`). Whether Mark's shared drive is that one, a parent of it, or a different drive entirely is **not determinable from the link alone** and changes what the Drive request should name. Ask him; do not assume.

## `S-6` — Source list as scoped in the session, superseded in part by `S-6a`

Named in the session as daily-reach sources: Slack, Jira, Confluence, Google Drive, and **Figma**. Mark and Zac own producing the actual list.

Figma does not appear anywhere in `research/current-state/source-and-org-landscape.md`. Whether it holds solution knowledge or only design artifacts is unexamined.

Andrew also referenced something transcribed as "M.com" as another route for pulling data out of repositories. **Unresolved** — the transcription is unreliable and the referent is not recoverable from context. Ask before treating it as a source.

## `S-7` — Action items, as assigned

| # | Owner | Action | Bears on |
| --- | --- | --- | --- |
| 1 | Mark, Zac | List the information sources reached for daily, to scope the MVP corpus | `S-6`; census scope |
| 2 | **Nino, Alex Vela** | Test what Claude and Google Enterprise can actually do now. Verify connector access and permissions; identify who enables restricted features | Plan §1 conditions **one and two**; `S-5`; `AC-1` |
| 3 | Zac | Consult **Levi** on where project documentation is stored today; establish a standard location if none is designated | `S-4`; the folder-structure hypothesis |
| 4 | Mark | Confirm which groups get Phase 1 access | `S-3` — substantially answered in the session already |
| 5 | **Nino** | Convert the planning documents into business-oriented format for management | `S-8` |

**Item 2 is the unblock the plan has been waiting on.** Plan §1 names two validation conditions — that Ask Commerce closes the gaps in behaviour, and that it is ours to run. Both were blocked: the first on a per-person spend cap, the second on not having asked. Item 2 assigns both, and pairs Nino with a member of AI Operations, which is the team that owns the answer to the second. The empirical probe is no longer waiting on a sponsor to unblock a budget; it has a partner and a deadline.

## `S-8` — The plan is not readable by its management audience, and that is a finding about the plan

Andrew, at 00:24:07: management should be able to see what is planned, in a format they will understand. His description of reading the current document was that he felt he "needed to go back to school for an AI PhD" — offered warmly, and it is still the clearest available signal that the artifact fails a reader it needs.

**This is not a request for a summary.** The solution plan is written for a sponsor who will interrogate the evidence; it grades its own claims and shows its corrections. That is correct for its reader and wrong for a CPO scanning for whether this is worth funding. Two derived surfaces are the response, at different altitudes.

## `S-8b` — Requirements were produced in this session and I did not capture them

The first pass over this session recorded decisions and action items and treated everything else as discussion. That was wrong. The room also produced **requirements**, several of which never reached any artifact:

- The **caution-wrapper** ask (Mark, 00:12:24), which he raised twice and re-framed himself when it was misread as an access-control request.
- The **explicit rejection** of per-document classification and ACLs (Nino, 00:12:24), which is a scope boundary worth having on record.
- **Training and messaging as a legitimate way to satisfy a requirement** (Nino, 00:14:38), which is the release valve on the point above.
- Andrew's request that the plan carry **a written placeholder** for revisiting broader access (00:15:46) — a specific ask, not a vague "later."
- Andrew's **speed-over-generality trade** (00:16:59): serve SE/SA fast, and a rebuild to broaden later is acceptable.
- Andrew's request to **name both SE and SA** in every artifact and invitation (00:10:13).

**The consequence was concrete.** `S-7` item 2 commits Alex Vela and me to evaluating platforms, and without these written down that evaluation had no acceptance criteria. `research/requirements/front-door-requirements.md` now owns them as `REQ-1`–`REQ-12` and is the checklist for that test.

## `S-9` — Adjacent, and explicitly out of scope

Public-facing developer documentation. Andrew's point: the dev docs describe the API but not how to solve real problems, and the pricing question is his example — real-time to ERP versus server-side, with nothing that tells anyone how to implement it. Zac added the idea of a register of pre-vetted architectural patterns.

**Chris owns work already pointed this way** (Mark). Andrew flagged it as "not related to this project" and asked only that it be known. Recorded so a later phase can pick it up and so that the overlap with Chris is not discovered twice.

---

## What this changes in the plan

| Change | Where |
| --- | --- |
| Answer engine, not retrieval — decided, with the safety assumption that makes it work | New; §1 and §4 |
| Audience is SE, SA **and TAM**; TPM deferred; the line is *forwarding unreviewed answers to clients* | §4 audience constraint; §7 |
| Gemini Enterprise's licensing premise needs re-verification against the new Google Enterprise accounts | §1, §5 row, `buy-landscape.md` |
| Validation conditions are assigned to Nino + Alex, not blocked | §1, §7 |
| Figma enters the source list; "M.com" unresolved | `source-and-org-landscape.md` |
| Scope-as-analysis ratified | §3 — already correct, no edit |
| Requirements extracted as `REQ-1`–`REQ-12` | `research/requirements/front-door-requirements.md`; §4 placeholder for the deferred-access note |
