# Handoff — picking this up on the machine with internal access

**Written**: 2026-07-27, from the personal machine, at commit `8bff273`.
**For**: the employee laptop, which can reach commerce.com internal tooling — Confluence, Drive, Jira, Slack, Gong, Make.com, the Claude Enterprise admin, and whatever "ask commerce" / CLA turns out to be.

Read `HANDOFF.md` first for where the initiative stands. This file covers only the two things that are specific to switching machines: **what will break on setup**, and **what to go get that could not be gotten from the personal machine**.

> **The short version.** Four open questions have been blocked on access, not on thinking. The biggest is BD-3 — whether a sanctioned internal assistant already exists. If it does, and it already carries security and hosting approvals, the sponsor's stated two-month floor was composed *entirely* of those approvals, and the configure-versus-build decision changes. Answer BD-3 before designing anything.

> **Update 2026-07-27 — most of this file's premise has changed. Read `research/prior-art/ask-commerce.md` first.**
>
> **Internal access turned out to be available from the personal machine**, via the `browse-tool` CLI at `~/Workspace/dev/tools/browse-tool` launched with `--profile` (it seeds a persistent Chrome profile from the real one, carrying the Okta/Atlassian session). Confluence, Jira and claude.ai were all reachable. This file's framing — that these questions are blocked until the employee laptop — no longer holds for anything reachable through a browser.
>
> **`BD-3` is resolved: `Ask Commerce` exists and is live.** That was item 1 below and the question this handoff said "changes the plan most." It did. Phase 1 largely collapses; Phase 2 (capture) is where the remaining value sits.
>
> **`G4` was corrected.** An earlier version of this note said the Claude surface was unverified and a Stage 2 prerequisite. Wrong — Claude is deployed to every employee with no approval gate. The software register is stale. `G5`'s NotebookLM recommendation went with it.
>
> Items below are amended in place where they moved. Item 1 is closed; **1b, 2 and 3 changed shape**; the data-governance decision this file asked for is recorded in `ai-governance-constraints.md` § 2.

---

## Before you start — five things that will bite

**1. The toolchain lives outside this repo.** `npm run manifest:check`, `npm run derive`, and the reviewer suite all resolve through `$BLUEPRINT_HOME`, which defaults to `~/Workspace/dev/tools/blueprint`. That is a separate repo and it is **not** vendored here. If it is absent on that machine, the gates do not run — clone it before trusting any green result.

Also: calling the suite directly with an unexpanded tilde fails. This errors with `MODULE_NOT_FOUND`:

```bash
BP="${BLUEPRINT_HOME:-~/Workspace/dev/tools/blueprint}"; node "$BP/template/tools/run-reviewers.mjs" --root .
```

Use `$HOME` explicitly:

```bash
node "$HOME/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs" --root .
```

The npm scripts handle the expansion themselves, so `npm run manifest:check` is fine as-is.

**2. Repo auth.** This is a private repo under the **personal** GitHub account (`nino-chavez/se-docs-frontdoor`). If that laptop is signed into a work GitHub identity or is behind SSO, cloning will fail or will silently use the wrong account. Check `gh auth status` before assuming a push will work.

**3. The source PDF is not in this repo.** The kickoff recording lives only in `~/Downloads` on the personal machine. Everything load-bearing has been transcribed into `research/sources/knowledge-database-kickoff-2026-07-27.md` **with speaker labels**, so the repo is self-sufficient for every claim currently cited. Anything *not* already quoted there needs the PDF — copy it over, or better, move it somewhere durable, which that file has been asking for since it was written.

**4. Both machines can now diverge.** The cross-session worktree guard is per-machine and does nothing across two laptops. Pull before starting and push before stopping. If the internal-access work is exploratory — and the census probably is — do it on a branch rather than `main`, so a half-finished census does not become the record.

**5. 1Password behaves differently per machine.** If `OP_SERVICE_ACCOUNT_TOKEN` is not exported in that shell, `op` runs as your user account rather than the read-only service account, which means writes will work and may prompt. Run `op item list --vault "Developer Secrets"` before authoring any new secret reference — do not invent item names.

---

## Read this before pulling internal data into the repo

The census is going to put you in front of real client material: tech scope contents, named accounts, Gong call transcripts, and a decade of the sponsor's direct messages. This repo is private, but it is private on a **personal** GitHub account.

That is a decision to make deliberately, not a default to drift into. The provenance record already flags the narrower version of it — whether the kickoff PDF itself belongs in here, given it contains a full named transcript.

**Recommendation, and it costs nothing:** have Phase 0 produce *counts, distributions, and structural findings* — how many documents, how old, how many carry the wrong-not-stale defect, how they distribute across sources. Those are what every downstream decision actually needs. Keep raw content on the employee machine or in the internal systems. If a specific document has to be quoted as evidence, quote the minimum and note where the original lives.

If you decide differently, decide it explicitly and write it down here.

**Decided 2026-07-27, and it went the way this section recommends.** Two internal Confluence registers were read on the personal machine; the derived constraints landed in `research/current-state/ai-governance-constraints.md` and the source tables did not. That file's second section states the rule in full — derived constraints, thresholds and structural findings travel; registers, per-integration risk-and-owner rosters, and internal staff names stay in Confluence, quoted minimally and attributed only where a decision cannot be stated without them. One of the two source pages is classified **SENSITIVE**, which sharpens the rule rather than changing it. Apply the same rule to census output.

---

## What to go get, in the order that changes the plan most

### 1. ~~BD-3 — does "ask commerce" / CLA already exist?~~ — CLOSED 2026-07-27

**Yes.** `Ask Commerce` is Anthropic's native ask-your-org surface at `claude.ai/ask-your-org`, configured and maintained by an internal **AI Operations team** (`ai-ops@bigcommerce.com`), active, reviewed June 2026, shared with every employee by default with no access request. Connected to Confluence, Jira and Slack. Respects per-user permissions. Runs Opus 4.7.

The four questions this section asked, answered: it is a configured Anthropic product surface rather than a build; AI Operations owns it; it can be pointed at new sources **through their intake form**, which is the mechanism this initiative should use; and yes, this initiative plausibly belongs inside it.

**Four gaps define the remaining work** — `AC-1` Drive is not readable and the tech scopes live there; `AC-2` solution knowledge has no authoritative source and the `SE`/`TAM`/`IPM` spaces are structurally demoted; `AC-3` Gong is not connected; `AC-4` capture is untouched and the system is visibly hand-patching corpus contradictions one at a time. Detail in `research/prior-art/ask-commerce.md`.

**Still worth doing on the employee machine:** the empirical probe. Run real SE questions at Ask Commerce and record what comes back — it is the strongest single artifact for the first sponsor sync, and it is blocked only by the **$1,000/person monthly Claude spend cap**, which was hit on 2026-07-27. Wait for the 1st, get the cap raised, or run from an account with headroom.

**Superseded framing, retained for the record:**

**Why first:** the sponsor put the delivery floor at two months and said it was composed *entirely* of security review and hosting overhead (00:31:14). If a sanctioned internal assistant already holds those approvals, that floor mostly evaporates, and it becomes either the delivery vehicle or the most relevant prior art in existence. No other open question moves the plan this much.

The sponsor named **Levi and Shane** as the people he scoped this with (00:09:27, and again when explaining why Mark and Zac were on the call). They are the route in.

What to establish:
- Does it exist, and what is it actually — a Claude deployment, a RAG app, something else?
- Who owns it, and what approvals does it already carry?
- Can it be pointed at new sources, or is its corpus fixed?
- If it exists, does this initiative belong inside it? That is the question the memo asks the sponsor to decide.

Record the answer in `research/prior-art/capture-domain-prior-art.md` § "Still unscanned", which names this as item 1.

### 1b. AI Operations — the conversation that now matters most

**Revised 2026-07-27.** This slot previously held four GRC questions about whether Claude was approved. Three of them are answered and the fourth moved. The conversation to have is with **AI Operations**, not GRC, and it is a request rather than a clearance check.

**Two asks, both of which the census is the evidence for:**

1. **Connect Google Drive contents** (`AC-1`). Ask Commerce can surface Drive files and cannot read them — stated in its own configuration. The tech scopes and SA project folders the sponsor proposed starting with (00:30:03) are in Drive. Without this, the corpus that matters most is invisible to the surface that already works.
2. **Establish an authoritative source for solution knowledge** (`AC-2`). The routing table has entries for GRC, PEOP, Equity/MNPI, Claude access and IT deployment — and none for SE/SA. Worse, the demotion rules name `SE`, `TAM` and `IPM` as non-authoritative, so 3,173 already-searchable pages can never be a source of truth. **Standing, not coverage, is the binding constraint on the Confluence portion.**

Ask 2 is likely the harder one: every existing authoritative entry is owned by a governance or platform function, and domain knowledge would be a new category. Worth scoping — a single small space like `SIPR` (66 pages, readable end to end) is a more grantable first request than "the SE corpus."

**Three questions to bring, in the order that costs least:**

- **How long does an AI Use Case Review take?** (`G2`) The route is settled — this is **Use-Case #2**, existing approved tool, new data type, so an AI Use Case Review with a Privacy Impact Assessment rather than a Vendor Intake. The clock is the number that confirms or corrects the sponsor's two-month floor, and nobody has it. Contact `ai-review@commerce.com`.
- **What raises a per-person spend cap, and who pays?** (`BD-4`) Claude is usage-based at **$1,000/person/month**, and the cap binds — it was hit on 2026-07-27. Routing SE question traffic into Claude makes this a capacity question with a real funding line, which `BD-4` previously lacked entirely.
- **How is Ask Commerce's authoritative-source list maintained?** Its instructions carry a dated source-dependency contract over ten hardcoded page IDs. That is the *authority tier* mechanism running in production. Understanding its maintenance cost is directly relevant to whether ask 2 is realistic.

**One thing to notice rather than ask.** Ask Commerce hand-patches individual corpus contradictions in its instructions — a channel name that appears two ways, two pages disagreeing on a GitHub org name. Each one is a bespoke line maintained by one team (`AC-4`). That is the memo's central argument, evidenced from their system rather than ours, and it is the strongest thing to bring to the sponsor.

### 2. Whatever delivery/IPM uses to record project state

Item 2 of that same unscanned list, and the reason `delivery-ipm` is flagged `implied-not-represented` in `research/personas-and-jtbd.md`. No IPM was in the kickoff. The clearest structural finding in the whole project — documentation stops when IPM hours run out — came from **Mark and Zac describing someone else's constraint**, and that persona's job cannot be designed from second-hand description.

Two things needed: the system itself, and an actual IPM to talk to.

### 3. Phase 0 — the corpus census

This is the work no other decision can proceed without, and it is the reason the access matters. Sources named in the kickoff:

| Source | What to check |
| --- | --- |
| Tech scopes folder | Volume, recency, how uniform. The sponsor proposed starting here |
| SA project folders | Volume, and what fraction of projects have one at all |
| Gong call recordings | Volume, and what Make.com already pulls (see 4 below) |
| IPM notes | Where they live, whether reachable — depends on 2 above |
| Slack channels | Which channels carry solution discussion |
| The sponsor's 1:1 DMs with SAs | A decade of them. Also the measurement problem in 6 below |
| Internal doc sites | CMS-backed; relevant to ADR-0001 trigger 3 |

**Governance constraint added 2026-07-27** (`G1`, `G3`). Counting and characterizing documents is not an AI use case — but *using an AI tool to do the counting over the real corpus* is, and the corpus is Submit-for-Approval data at minimum. That is a design choice to make deliberately: a census run with scripts and file metadata needs no approval; a census run by pointing a model at the folder does. Note also that the PoC rules explicitly forbid the shortcut — public or dummy data only, no connections to other systems — so "just pilot it on the real folder and see" is not available as a fast path.

Beyond volume, the census has to answer three things the problem statement says nothing can proceed without:

- **How much is wrong rather than merely old.** The guest-tokenization class — a documented workaround that exists because a capability was missing, where the capability has since shipped. This is `P4`, and `P6` says it is the fastest-decaying and most valuable category. Any count that treats "old" and "wrong" as one bucket misses the point.
- **How contradictory it is.** Two sources disagreeing is guaranteed; the design commitment is to surface conflicts, not adjudicate them. The census sizes that problem.
- **Which subset is trustworthy enough to serve.** Phase 1 is scoped by this answer, not by ambition.

`~/Workspace/dev/tools/claude-docs-toolkit/` has `/doc-audit` (coverage analysis and gap detection) and `/doc-strategic` (health assessment) — the closest existing instruments, per the prior-art scan. They assume a codebase substrate, so the method transfers and the substrate assumption does not. `~/Workspace/dev/tools/fleet-observability/` is the census-instrument shape and carries real ADRs; worth reading before designing rather than after.

### 4. Gong and Make.com — is ADR-0001 trigger 3 live?

Gong is a named in-scope source, already pulled via Make.com, and **not** a standard Claude Enterprise connector. That is trigger 3 in `decisions/0001-configure-first-pilot-as-prototype.md` — "Tag can't cover the sources that pilot traffic actually needs." The trigger is not fired, because whether pilot traffic routes to Gong is unknown until the census runs. It is no longer hypothetical.

Check what Make.com already moves and where it lands. If Gong content already arrives somewhere a standard connector can see, the trigger may never fire.

**Partly answered 2026-07-27** (`G6`): Gong is an approved integration and Make AI (Enterprise) is approved tooling, so this path is not a governance dead end — the trigger's real question is connector *reach*, which stays technical. One constraint travels with it, and it is a design constraint rather than a checkbox: **AI-generated Gong output must not be used for employee performance management.** A surface that summarizes who-knew-what across SA calls edges toward exactly that, and the line has to be held in the design, not in a policy footnote.

**One caveat carried forward:** trigger 3 lost its reference implementation. `~/Workspace/dev/archive/knowledge-index` — named in the research corpus as the contingent crawl-and-index seam — no longer exists on disk. If the trigger fires, that branch has no reference implementation to adapt and is more expensive than the ADR assumed.

### 5. Shared-Drive visibility — ADR-0001 trigger 1

Directly testable with the Claude Enterprise admin: can the connector see Shared Drives, or only My Drive? The corpus flags this as `anthropics/claude-code#53442`, with a caveat worth re-reading — that issue documents the Cowork/MCP connector, while the pilot risk is the claude.ai Enterprise connector. **Test it rather than inferring from the issue.** This is one of two claims still labeled "cited, not re-derived."

### 6. A deflection baseline that measures the right direction

This session's open gap, and it is a real one. `manifest:check` reports `deflection-baseline` unmet (`research/pilot/baseline-pings.md` missing) — that is accurate, not a bookkeeping lag.

The trap, because it already caught this repo once: the obvious instrument is the sponsor's 1:1 DM volume with the SAs, but on the call he described that channel as **him asking them** — "I just bug them that often" (00:35:32). It measures his outbound questions, not inbound demand on him. Both directions are real and both are worth displacing. They are not the same number, and the inbound direction currently has no instrument at all.

Whatever gets built has to state which direction it counts. See `P8` in the problem statement and the measurement note on `knowledge-holder/JOB-1`.

### 7. Two external claims still labeled "cited, not re-derived"

Not internal, so doable from either machine, but still open:

- The NotebookLM "(verified)" claim cites a product-chooser page for an API assertion.
- GH#53442 — the connector transfer described in 5 above.

A `citation-checker` agent was in flight when the last session ended. Check whether its result landed before redoing this.

---

## Gate state as of `8bff273`

Green, with two things explicitly owed. Do not read the green board as readiness — that mistake has already been made once here.

| Check | State |
| --- | --- |
| Mechanical suite (5 apply under `variant: research`) | 4 PASS, `terminology-linter` WARN (30 acronym heuristics), `PORTAL_OVER_PROMOTED` warn |
| `manifest:check` | PENDING — 0 errors, 4 pending, 0 warns |
| `reader:check` | PASS — 15 rendered files, 0 findings |
| `doc-quality-auditor` | Ran. Both criticals closed; minor items open |
| `research-sibling-scanner` | Ran. Closed |
| `research-reference-grader` | Ran. Canonical fix landed; corpus-wide re-grade open — see 7 above |
| `fact-check-loop-reviewer` | **Still owed.** Its agent went idle twice without reporting. The attribution sub-check was hand-run against the source PDF and its findings are fixed, but the convergence loop and other sub-checkers never executed |

**Two standing traps**, both of which have already cost time:

- **Do not run the stamper** (`blueprint-init`) against this initiative. `copyTree()` writes `research/personas-and-jtbd.md` unconditionally with the blank template, which would destroy the Stage 1 artifact.
- **Do not put a trailing comment on the `variant:` line** in `blueprint.yml`. Three reviewers capture the comment text, report the variant as unrecognized, and silently fall back to greenfield.

## The memo

`docs/decision-memo.md` is the Stage 5 deliverable, addressed to Andrew, Mark, and Zac, and is currently `draft`. Its attribution defects are fixed — including one that credited Zac's observation to Mark. It is sendable; sending is an operator call. On send, promote it to `issued` in `actor-output.yml` and set up the weekly sync the operator committed to.

The single most useful thing to bring to the first sync is a concrete Phase 0 proposal: what gets counted, how, and over how long. The memo promises exactly that and currently has no duration attached.
