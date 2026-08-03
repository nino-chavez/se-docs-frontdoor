# SE/SA knowledge access — where this stands, and what we need

**For** team leads and managers across Services, Support and Documentation · **From** Nino Chavez · **3 August 2026**
**Status** In progress. Actions assigned; validation running over the next fortnight.

---

## Why you are reading this

This started as a way to give Solution Engineers faster access to prior solution knowledge. It has turned into something that touches how several teams record and store documents, which is why it is now in front of you rather than staying inside one function.

Nothing here asks you to change a process. Some of it asks what your process currently is.

## Where we landed, and how

**We are not building a search tool.** Commerce already has one — Ask Commerce, run by AI Operations, live for every employee. When we compared it against the seven principles this project had committed to, six were already implemented: citations with dates, staleness flags, conflicts surfaced rather than silently resolved, permission-aware search across Confluence, Jira and Slack.

That is a working assessment rather than a closed one. Two things have to be true before we treat it as settled, and both are being tested now:

1. **It works in practice, not just on paper.** Everything above is read from its configuration. We have not yet run real questions through it and recorded what comes back.
2. **It is ours to run.** If every source we add and every rule we adjust is a request to another team, that is a standing cost on how fast this can improve. We are asking AI Operations directly rather than assuming an answer.

## What we measured

Numbers, because opinions about documentation quality are cheap and these were not.

| Confluence space | Pages | Touched in last 12 months |
| --- | ---: | ---: |
| Technical Project Management | 1,599 | 21% |
| Solutions Architects | 912 | 19% |
| **Technical Account Management** | **441** | **57%** |
| Solutions Engineering | 155 | 23% |
| Solution Architecture Knowledge Base | 66 | 33% |
| **All five** | **3,173** | **26%** |

Two things stand out.

**The SE space is the smallest of the five.** That explains the shoulder-tap better than any theory — an engineer asks a person because the answer was never filed anywhere an engineer would look.

**TAM is the outlier, and it is the useful one.** At 57% touched in twelve months against 19–21% for SA and IPM, TAM is the only corpus in the estate that is not decaying, under the same billing pressure as everyone else. **We would rather learn what TAM already does than import a practice from outside.** That is a genuine ask, not a courtesy.

Separately, at least 692 client opportunity folders sit in Drive for 2026 alone. That is a floor from counting a file listing, not an audited number, and getting a real one needs proper access.

## What Mark's answer changed

Mark named three archives he works from: the Confluence `SA` space, a shared Google Drive, and Lucidchart.

**Ask Commerce reads one of them.** It is also connected to Jira and Slack, which he did not name. So the tool is wired to two sources our most senior SA did not list, and blind to two he did.

That reframes the problem. The Confluence figures above are precise, and they turn out to describe roughly a third of one senior person's actual working set. It is the strongest argument yet for getting Drive connected, and it is worth someone else checking against their own habits — **Zac, your list may differ, and if it does that matters.**

**Lucid is new to this work.** An official Claude connector exists and inherits Lucid's own permissions, which is the hard part solved. Two things are unresolved: whether that kind of connector can attach to a shared org-wide assistant rather than an individual's, and whether adding it triggers a security review that every path we have chosen so far was designed to avoid. Both are on the list for the platform test this week.

## What we have decided, and what is still open

**We have settled the front door provisionally: Ask Commerce.** Not because it beat the alternative on features — Google's product is genuinely strong and reads shared drives today, which ours does not. It wins on cost of entry. Ours is already approved and deployed to everyone; adopting a second means a new purchase, a new approval, and two assistants answering the same question differently with nothing to settle between them.

That is written down with four specific findings that would reverse it. A working assumption, not a lock.

**The session with AI Operations changed shape as a result.** It is no longer *which tool wins*. It is a gap inventory: score what we are going to use against the requirements list, and produce a table of what it cannot do, with an owner and a cost against each gap. That table is what the next three decisions need.

## The problem underneath

Search quality is capped by what gets written down. When capture fails, the retrieval layer absorbs the damage.

We have first-party evidence of this rather than a theory. Ask Commerce's own configuration carries hand-written patches for specific contradictions in our documentation — one page using two different names for the same Slack channel, two pages disagreeing on a GitHub organisation name with an instruction not to state it confidently. Every contradiction in our corpus becomes a line of configuration a person maintains by hand. It works. It does not scale.

The sharper version of the problem is documents that are **wrong rather than old**. A document describing a workaround for a gap the platform has since closed looks identical to a good one in every count we can run. Timestamps find stale. They cannot find wrong.

## What we are asking of each team

| Who | What | Why |
| --- | --- | --- |
| ~~Mark~~ — **answered 30 July** | Confluence `SA`, a shared Google Drive, Lucidchart | It changed the shape of the problem. See *What Mark's answer changed* above |
| **Zac** | Still open — the sources you reach for daily | Mark's three may not be yours |
| **Zac, with Levi** | Where project documentation is stored today, and whether a standard location exists | This may be the cheapest fix available. See *The cheapest thing on the table* below |
| **Mark** | Confirm Phase 1 access groups | Substantially settled: SE, SA, TAM. TPMs deferred for now |
| **Alex Vela, AI Operations** | A gap inventory, scored against the requirements list | Answers both validation questions above. First question: whether a diagramming connector can attach to a shared org-wide assistant at all |
| **TAM leads** | Twenty minutes on what you do differently | You are the only group whose documentation is not decaying |
| **Chris** | A comparison of scope | Your documentation work overlaps this. Better to find the overlap now than twice |
| **Anyone reading this** | Tell us what already exists | We have now found working internal systems for this twice, both by accident. Thirty seconds of your recall beats another week of ours |

## The cheapest thing on the table

Andrew raised a possibility worth taking seriously: part of this gap may not be missing documents but **missing places to put them**.

If a meaningful share of what an engineer cannot find already exists, sitting somewhere nobody thinks to look, then a folder structure and a naming convention close more of this gap than anything else being discussed — in days rather than a quarter. That is now something the two-week measurement explicitly tests.

## Scope, so nobody is surprised later

**We are not redesigning how Commerce stores documents.** Our job is to identify where things live, where that limits us, and bring findings to the leaders who own those processes. Any change is their call, not ours.

**Phase 1 is an answer engine, not a file search.** You ask a question, an agent reasons over the corpus and answers with citations. It does not hand back a list of documents.

**Access is limited on purpose.** Some answers will be wrong. The boundary exists so nobody forwards an unreviewed answer to a client. That is the actual risk, and it is why access is defined by who can evaluate an answer rather than who would benefit from one.

**Whatever we end up with has to keep running without one person.** We looked at an automated knowledge system inside Commerce this week. Twenty-two commits, one author, no scheduled run — it works when a laptop happens to be awake, and it had not run for a week when we looked. Nothing told a reader that.

Anything we propose needs a named owner, a schedule that does not depend on anyone's machine, and a visible sign of life. A system that is quietly not running is worse than no system, because people keep trusting it.

## Timeline

Two weeks. The measurement runs alongside the validation and the two configuration requests, not after them.

At the end of it we will know how much of our documentation is actively wrong. If the answer is *not much*, the honest conclusion is that better search over a mostly-accurate corpus was enough, and this ends there. That outcome is on the table and we have written down what would produce it.

---

<sub>Full analysis, methods and per-claim evidence grading: `docs/solution-plan.md`. Session record: `research/sources/se-docs-frontdoor-sync-2026-07-30.md`. Corpus figures are measured with recorded queries; the Drive count is a lower bound.</sub>
