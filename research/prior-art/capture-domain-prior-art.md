# Prior art — the capture domain (domain E)

**Scanned 2026-07-27.** Scope: tooling and patterns that record knowledge *at the point of work*, rather than retrieving it afterward.

**Why this file exists.** The founding prior-art scan (2026-07-09, in [`../current-state/workspace-prior-art.md`](../current-state/workspace-prior-art.md)) covered **retrieval** implementations, because the founding problem was framed as retrieval friction. The 2026-07-27 restatement established that capture quality bounds retrieval quality ([`../problem-space/problem-statement.md`](../problem-space/problem-statement.md) P7), which makes capture a first-class domain — and it was unscanned. This closes that gap.

The transferable finding, stated up front: **every working capture mechanism found here replaces discipline with derivation.** None of them asks a person to remember to write something down. That is the structural answer to P2 (documentation stops when billable hours end), and it is the opposite of how the corpus is produced today.

---

## Prior Art (Workspace)

### 1. Blueprint archaeology substrate — the closest analogue

**Path:** `~/Workspace/dev/tools/blueprint/template/tools/archaeology/`
**Pattern doc:** `~/Workspace/dev/tools/blueprint/docs/patterns/archaeology-substrate-pattern.md`
**Status:** scaffolded template with a named proving ground (Phase 6 passed 2026-05-22)

An append-only event log across project history streams, with explicit refs that join them. Its stated purpose is to answer *"what did we know on date T, why did we pick X, who decided Z"* — without a new tool per question.

That is close to a restatement of the sponsor's ask (kickoff 00:08:23, 00:09:27): what were the known limitations, what did we recommend, what was actually implemented.

**Why it matters for P4 and P6 specifically.** The corpus's sharpest defect is documents that are *wrong*, not merely old — guest-tokenization workarounds that describe a solution to a problem the platform since fixed. An append-only, timestamped event log is structurally immune to that failure: it never claims a past event is current. It records that X was true on date T. A document store overwrites or, worse, silently keeps both. Given P6 (negative knowledge decays fastest), this distinction is load-bearing rather than academic.

**Mechanism, not discipline.** Capture runs through per-stream ingesters (`ingesters/git.py`, `adr.py`, `github.py`, `audits.py`, `iterations.py`, `inputs.py`, and others) — the log is derived from artifacts that already exist for other reasons.

**Divergence — where it does not transfer.** Its ingesters read *structured developer streams* (git commits, ADR files, GitHub issues). This initiative's sources are unstructured and human-authored: Gong call recordings, project folders with no enforced template (P3), and a decade of direct messages. There is no `ingesters/gong.py` equivalent, and P3 means there is no schema to write one against. The pattern transfers; the ingester layer does not.

### 2. claude-recall-cli — mining an ephemeral record for durable knowledge

**Path:** `~/Workspace/dev/tools/claude-recall-cli/`

Saves and searches reusable session entries, backed by SQLite + FTS5, surfaced as slash commands. Its `recall-scan` mode batch-scans session transcripts for recall-worthy patterns.

**The transferable idea:** the durable artifact is *extracted from a record produced for a different purpose*. Nobody writes the entries; a scan finds them in transcripts that existed anyway.

**Direct applicability.** This is the pattern for the kickoff's named-but-unexamined sources. Gong recordings and IPM notes both already exist as byproducts of work nobody did for documentation's sake — the same shape as a session transcript. The sponsor already reaches for this instinct (00:10:31: "a lot of the gong calls will be documented").

**Divergence.** Recall operates on a single operator's own transcripts, with that operator as the judge of what is worth keeping. This initiative's corpus is multi-author across teams with uniform read access but no agreed authority ranking. "Is this worth keeping" becomes a question with no owner — which is exactly the third named gap in [`../personas-and-jtbd.md`](../personas-and-jtbd.md): no persona owns corpus curation.

### 3. Blueprint's own working capture loop — the pattern this initiative is running

Worth naming because this repository is a live instance of it, and the mechanism is visible in it right now:

| Mechanism | What it captures | Why it survives attention ending |
| --- | --- | --- |
| `HANDOFF.md` | Position, next steps, do-not-do list | Written for a reader who has no context, including the same person later |
| `METHODOLOGY-AMENDMENTS.md` | Process learnings, append-only | Append-only means no editing pass is required to add to it |
| `npm run derive` → `derived/` | State snapshot from the manifest | Generated, never hand-edited — cannot go stale through neglect |
| SessionEnd hook | Triggers capture without being asked | The person does not have to remember |

**The finding.** Blueprint's answer to "documentation stops when attention stops" is a **hook plus a derive step**, not a template plus a reminder. Even so, this very session found `derived/` pinned two commits stale — which is the honest lesson: mechanical capture degrades more slowly than discipline-based capture, but it still needs a trigger that actually fires.

**Divergence.** Blueprint's loop assumes one operator with commit access and a repo, and it captures *reasoning about work*. The SE/SA corpus is multi-author, spans systems nobody in this initiative controls, and captures *facts about a platform*. The hook-plus-derive shape is the transferable part; the git-native substrate is not, because the sources are Drive, Confluence, Slack, and Gong.



### 4. claude-docs-toolkit — documentation audit, not just generation

**Path:** `~/Workspace/dev/tools/claude-docs-toolkit/`
**Found:** 2026-07-27, by re-derivation of this scan. **Missed by both prior passes**, including this file's first version.

Ten documentation commands, of which two are the relevant ones: `/doc-audit` (coverage analysis and gap detection over an existing codebase) and `/doc-strategic` (health assessment). It also carries `docs/research/autonomous-knowledge-synthesis.md`, a treatise on documentation drift. All verified present on disk.

**Why this matters more than the others.** It maps onto the two pieces of scope with no prior-art coverage anywhere in the corpus:

1. **The corpus census** — which `../problem-space/problem-statement.md` calls the only work no other decision can proceed without. `/doc-audit` is coverage-analysis-and-gap-detection, which is what a census *is*.
2. **The sponsor's second success criterion** — a written diagnosis of where documentation practice currently breaks, with recommended changes. `/doc-strategic` is a health assessment. `docs/decision-memo.md` now names this criterion as having no phase or owner; this is the closest existing instrument.

**Divergence.** It audits a *codebase* — files in one repo, on disk, with a git history. This corpus spans Drive, Confluence, Slack, and Gong, across systems nobody in this initiative controls, with no schema to audit against. The gap-detection *method* transfers; the substrate assumption does not.

**Secondary:** `~/Workspace/dev/tools/fleet-observability/` (which absorbed `repo-health-check`) is the census-instrument shape and carries real ADRs. Worth reading before designing Phase 0 rather than after.

**Why both passes missed it.** The capture primitive was written here as a category description — "tooling and patterns that record knowledge at the point of work" — rather than as a searchable primitive, unlike the retrieval side. A tool literally named for autonomous documentation generation did not surface against a description that abstract. The lesson is about how the primitive is stated, not about scan effort.

### 5. Adjacent, weaker relevance

- `~/Workspace/dev/tools/specchain/` — spec-driven implementation chain. Relevant only if domain E ends up standardizing a document *template*, which P3 suggests is the mechanism that already failed here: a template exists and is followed differently on every project. Named so a future scan does not treat "add a template" as unexplored.
- `~/Workspace/dev/tools/local-dictation/` — voice capture. Speculative, but the P2 failure is that writing costs unbilled time; lowering the cost of recording is one of the few levers that does not require more hours.


## Prior Art (internal, from the AI governance registers)

Added 2026-07-27 from the two internal Confluence registers read into `research/current-state/ai-governance-constraints.md` (`G7`). Both are **internal products already through security review**, which is a category this scan previously had nothing in — everything above is workspace tooling with no approval history.

### 6. Actively — a reasoning layer over internal systems, already approved

Described in the register as a go-to-market intelligence layer that "unifies and reasons over" Salesforce and Snowflake data. Approved, with a stated operating boundary: stay inside the approved sources, and **a new data connection requires a fresh risk assessment**.

Relevance is the boundary, not the product. It is the working template for how *this* initiative's source list will be governed as it grows — each additional source is a new assessment, not a free extension of an existing approval. That has direct consequences for Phase 1 scoping: a narrow high-trust subset is cheaper to approve *and* cheaper to widen later, which is the same conclusion *coverage follows verified quality* reaches from a different direction.

### 7. Discoverist AI — an approved AI answer surface over commerce knowledge

Register entry: *Merchant AI Support product*. Input spans Public, Non-public, Unidentifiable and Customer data; output usage is **Internal and Public**; it carries an approved security exception.

This is the closest existing analogue to the question surface (domain `B`) anywhere in the scan, internal or external — an AI answer surface over commerce knowledge that has already cleared security, including the exception process. Two questions worth more than anything the workspace scan produced: what corpus does it answer over, and what did its approval actually require? **Not scanned. Reachable only from the employee machine.**

## Still unscanned — the three that matter most

None is reachable from this workspace, and all three are more important than anything above:

1. **The internal assistant the sponsor called "ask commerce" / CLA** (kickoff 00:09:27, 00:33:23). BD-3. If it exists it is either the delivery vehicle or the most relevant prior art in existence, and it may already carry the approvals that constitute the stated two-month floor. Note that neither governance register contains an entry matching the sponsor's description — that is not evidence of absence (the registers cover tools and integrations, not internal builds), but it does mean BD-3 stays exactly where it was.
2. **Whatever delivery/IPM already uses to record project state.** Named in the kickoff as a source ("IPM notes", "documented within their side of things", 00:12:48) but never examined as a system. `delivery-ipm/JOB-1` cannot be designed without it, and that persona is already flagged `implied-not-represented`.
3. **Discoverist AI's corpus and approval path** — item 7 above. Cheaper to answer than either of the others, and it is the only known instance of this exact shape surviving commerce's security review.

All three are operator- or sponsor-resolvable, not researchable from here.
