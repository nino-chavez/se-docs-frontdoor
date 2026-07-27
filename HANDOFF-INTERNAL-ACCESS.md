# Handoff — picking this up on the machine with internal access

**Written**: 2026-07-27, from the personal machine, at commit `8bff273`.
**For**: the employee laptop, which can reach commerce.com internal tooling — Confluence, Drive, Jira, Slack, Gong, Make.com, the Claude Enterprise admin, and whatever "ask commerce" / CLA turns out to be.

Read `HANDOFF.md` first for where the initiative stands. This file covers only the two things that are specific to switching machines: **what will break on setup**, and **what to go get that could not be gotten from the personal machine**.

> **The short version.** Four open questions have been blocked on access, not on thinking. The biggest is BD-3 — whether a sanctioned internal assistant already exists. If it does, and it already carries security and hosting approvals, the sponsor's stated two-month floor was composed *entirely* of those approvals, and the configure-versus-build decision changes. Answer BD-3 before designing anything.

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

---

## What to go get, in the order that changes the plan most

### 1. BD-3 — does "ask commerce" / CLA already exist?

**Why first:** the sponsor put the delivery floor at two months and said it was composed *entirely* of security review and hosting overhead (00:31:14). If a sanctioned internal assistant already holds those approvals, that floor mostly evaporates, and it becomes either the delivery vehicle or the most relevant prior art in existence. No other open question moves the plan this much.

The sponsor named **Levi and Shane** as the people he scoped this with (00:09:27, and again when explaining why Mark and Zac were on the call). They are the route in.

What to establish:
- Does it exist, and what is it actually — a Claude deployment, a RAG app, something else?
- Who owns it, and what approvals does it already carry?
- Can it be pointed at new sources, or is its corpus fixed?
- If it exists, does this initiative belong inside it? That is the question the memo asks the sponsor to decide.

Record the answer in `research/prior-art/capture-domain-prior-art.md` § "Still unscanned", which names this as item 1.

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

Beyond volume, the census has to answer three things the problem statement says nothing can proceed without:

- **How much is wrong rather than merely old.** The guest-tokenization class — a documented workaround that exists because a capability was missing, where the capability has since shipped. This is `P4`, and `P6` says it is the fastest-decaying and most valuable category. Any count that treats "old" and "wrong" as one bucket misses the point.
- **How contradictory it is.** Two sources disagreeing is guaranteed; the design commitment is to surface conflicts, not adjudicate them. The census sizes that problem.
- **Which subset is trustworthy enough to serve.** Phase 1 is scoped by this answer, not by ambition.

`~/Workspace/dev/tools/claude-docs-toolkit/` has `/doc-audit` (coverage analysis and gap detection) and `/doc-strategic` (health assessment) — the closest existing instruments, per the prior-art scan. They assume a codebase substrate, so the method transfers and the substrate assumption does not. `~/Workspace/dev/tools/fleet-observability/` is the census-instrument shape and carries real ADRs; worth reading before designing rather than after.

### 4. Gong and Make.com — is ADR-0001 trigger 3 live?

Gong is a named in-scope source, already pulled via Make.com, and **not** a standard Claude Enterprise connector. That is trigger 3 in `decisions/0001-configure-first-pilot-as-prototype.md` — "Tag can't cover the sources that pilot traffic actually needs." The trigger is not fired, because whether pilot traffic routes to Gong is unknown until the census runs. It is no longer hypothetical.

Check what Make.com already moves and where it lands. If Gong content already arrives somewhere a standard connector can see, the trigger may never fire.

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
