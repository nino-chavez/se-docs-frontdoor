# Solution Plan — SE/SA Knowledge Capture

**Author**: Nino Chavez · **Date**: 2026-07-28 · **Format**: SCQ-R
**Status**: Pre-decision. One decision and two requests are outstanding; both are named in §6.
**For**: Andrew (sponsor), Mark, Zac. Annex B is addressed to AI Operations and is ready to send.

---

## Recommendation

**Stop building a search tool. Send two requests to AI Operations, run a two-week census, and reserve the build decision for capture — the half no search tool can deliver.** I am not asking to build anything yet, and the only decision I need this week is whether recording knowledge is in scope at all.

## Situation, complication, question

We committed to building a front door to SE knowledge. The reasoning held: a decade of platform history sits in a shrinking number of people, and the documents that should hold it are a byproduct of billable delivery, so they thin out exactly where the billing stopped. Mark and Zac established the shape of that at kickoff — one-off client conversations that sometimes never enter a documented process, smaller engagements that get no folder, documentation that stops when IPM hours run out, and a template followed differently on every project.

The complication is that the front door already exists. `Ask Commerce`, built and maintained by our AI Operations team, is live, shared with every employee by default, and already implements six of the seven guiding principles this project committed to. It cites every claim with a last-modified date, flags anything over twelve months old, and surfaces conflicts rather than picking between them. Andrew, when you said "something similar to ask commerce," you were not reaching for an analogy — you were naming the system, and I filed it as an open question rather than checking.

That leaves the real question: **if the search tool is built, what is left worth building?**

My recommendation is above. The rest of this document is why I believe it, what would change my mind, and what I need from each of you.

---

## 1. The retrieval problem is solved, and not by us

The evidence for that claim is a principle-by-principle comparison, and it is worth seeing rather than taking on trust, because the headline number is my assessment rather than a measurement.

| Guiding principle | Implemented? | How |
| --- | --- | --- |
| Cite or say nothing | Yes | Numbered citations; source name, last-modified date and URL on every answer. Instructed never to invent a URL, owner or date |
| Recency is correctness | Yes | Flags sources over twelve months old on fast-moving topics |
| Surface conflicts, don't adjudicate | Yes | On unresolved conflict, shows both with dates rather than choosing |
| Assume no schema | Yes | Federated search across Confluence, Jira and Slack |
| Measure against the person | **No** | Not a product capability. Ours to answer |
| Coverage follows verified quality | Yes | Source hierarchy with explicit demotion rules |
| Answers are a starting point | Yes | Staleness and DRAFT flags presented as risk signals |

Six of seven, and the seventh was never something a search tool could satisfy — it is a measurement question. The honest reading is that every principle a question surface *could* implement, is implemented. Building our own would produce a smaller, later, worse-supported version of something the whole company already has, which is why the first thing I am recommending is that we stop.

## 2. The capture problem is not solved, and we can now size it

Two gaps separate what exists from what an SE actually needs, and both are about the corpus rather than the tool. Ask Commerce cannot read Google Drive — it sees that a file exists and cannot open it — and the tech scopes and SA project folders live in Drive. It also has no authoritative source designated for solution knowledge, and it explicitly demotes the `SE`, `TAM` and `IPM` spaces, so even the pages it can read it will never treat as settled.

The measurements support taking this seriously. Across the five spaces holding SE, SA and delivery knowledge there are **3,173 pages, of which 26% have been touched in the last twelve months** and 59% have not been touched in two years. The `SE` space is the smallest of the five at 155 pages, which explains the round trip better than any theory: an SE asks a person because the answer was never filed anywhere an SE would look.

Drive is larger by an order of magnitude. The 2026 opportunity folder alone holds **at least 692 opportunity folders** — a floor rather than an audit, and counting folders where the Confluence figures count pages, so the comparison holds directionally and not as a multiple. The census owns these numbers and the queries behind them.

The strongest evidence is not a number. Ask Commerce's own configuration carries hand-written patches for individual contradictions in our documentation — one page that uses two different names for the same Slack channel, two pages that disagree on a GitHub organisation name, with an instruction not to state that name confidently. Every contradiction in our corpus becomes a line of configuration that a person writes and maintains. It works, and it does not scale. **One team is already absorbing our documentation defects by hand, one defect at a time**, which is the argument for fixing capture made from our own systems rather than from theory.

## 3. Three things block the path, and none of them are mine to decide

Two of the three are requests to a team I have no authority over, which is the part of this that needs you rather than me. AI Operations would need to connect Drive contents to Ask Commerce, and to designate an authoritative source for solution knowledge. The first is a connector change. The second is harder, because every current entry on that list is owned by a governance or platform function and domain knowledge would be a new category — which is why I would open with a small, vettable space rather than asking them to bless the estate. Annex B is the request, written and ready to send.

Those two requests are not independent, and it took me too long to see it. Records produced by capture would land in Confluence, which Ask Commerce reads — but they would land in a *team* space, which its rules structurally demote. Without the authoritative-source designation, capture manufactures records the search tool is instructed not to believe. **The Drive request unblocks the corpus we already have; the authority request unblocks the corpus we would create.**

The third is yours alone. Recording knowledge going forward is a write system, and everything scoped so far has been read-only — the smaller security and privacy surface you identified as the whole two-month floor. That decision determines whether the remaining work is a project or a support ticket, and I would rather have it wrong-and-early than right-and-late.

Governance is not the obstacle I expected it to be. Claude is already deployed to every employee with no approval gate, and the route for pointing an approved tool at new data is an AI Use Case Review rather than a vendor intake. What that review costs in time is the one number I still owe you.

---

## 4. What I recommend we do

**Finish the census. Two weeks, roughly four hours of senior time.** The Confluence half is done and is where the figures above come from. Drive needs real API access rather than the file-listing scrape that produced the floor. The quality half matters more than the volume half, because timestamps find *stale* and cannot find *wrong* — Mark's guest-tokenization case is a document that is confidently, actively incorrect and looks identical to a good one in every count I can run. Finding those means joining shipped platform capabilities against documents that predate them, plus a small adjudicated sample to establish a rate.

**Send the two requests now, in parallel.** They do not depend on the census finishing, and the answer to the Drive request determines whether the rest of this plan survives.

**Build capture only after one record exists by hand.** Before any pipeline, I would take one closed engagement, produce its record manually from the transcripts and tech scope that already exist, and ask the SA who ran it whether they would have wanted it. That costs a day and can end the project, which makes it the cheapest decision-grade evidence available.

**Write where the reader can read.** This is a constraint on the capture design rather than a task: the target is set by the retrieval surface's reach, not by what is convenient to build. Records that land anywhere Ask Commerce cannot see would recreate exactly the problem we are trying to solve, for a corpus of our own making.

**Sequence discovery support last.** Generating the hard questions for a merchant depends on negative knowledge being present and current, which is the decay problem the earlier phases exist to address. The tech scope you demonstrated already does a version of it and is the right starting point.

## 5. What I recommend we not do

Each of these was in scope at some point, and each is excluded on evidence rather than preference.

| Not doing | Why | What would reopen it |
| --- | --- | --- |
| Building a question surface | It exists, org-wide, maintained by another team | AI Ops deprecating it |
| Building connectors ourselves | A request to AI Ops, not an engineering task. Our own would trigger an AppSec review and duplicate their roadmap | A refusal — which is a stop-and-replan signal, not a build trigger |
| Remediating the existing corpus | Unbounded, and it does not address why the corpus got that way | A specific high-traffic subset shown to be actively harmful |
| Designing a new template | One exists and is followed differently every project. The constraint is unbilled hours, not template quality | Evidence that the template, not the time, is what fails |
| Adjudicating contradictions automatically | Locked at founding: surface conflicts, do not resolve them | Nothing foreseen. An invariant |
| Indexing everything | Coverage follows verified quality | A census showing uniformly high quality, which nobody expects |
| Writing code before one record exists by hand | The manual test can end the project in a day | That test passing |

## 6. What would change my recommendation

Two assumptions carry it, and both are weaker than the rest of this document.

**That the wrong-not-stale problem is big enough to justify the work.** This rests on a single example — guest tokenization, from Mark. Everything in §4 depends on it and nothing has measured it. If the census sample comes back showing a low rate, the honest conclusion is that better search over a mostly-accurate corpus was enough, and this project ends with the two requests. That is the outcome I consider most likely to prove me wrong.

**That an SA would actually want a derived record.** Untested, and the one-record test in §4 is designed to find out cheaply before anything is built.

**That the questions SEs ask stay document-shaped.** Ask Commerce answers *find me the document* well, which is the right shape for a corpus of prose. Capture would change the corpus into uniform records, and uniform records invite aggregate questions — how many engagements hit this limitation, which workarounds recur across clients — where a federated search returns three documents and the asker wanted a distribution.

Negative knowledge has the same problem in a sharper form. Knowing what the platform cannot do, and whether that limitation still holds, looks more like a maintained register than a search index — and `P6` says that is the category which decays fastest and matters most. If Phase 0's demand work shows those questions are common, *don't rebuild retrieval* narrows to *don't rebuild search*, and a small query surface over the structured records earns its place. That is a far smaller build than the one we started with, and it is not decidable until we know what people actually ask.

Two more that would change the shape rather than the direction: if AI Operations refuses the Drive connection, the plan needs rethinking rather than patching; and if reviewer time is not committed, the verification step degrades into rubber-stamping, which would make a generated record worse than no record at all.

I would rather these be written down and wrong than unwritten and right.

---

## 7. What I need from each of you

**Andrew.** One decision: does this write, or stay read-only. Then the two AI Operations requests in Annex B — a sponsor request lands differently than mine, particularly the authoritative-source one. Then a commitment of roughly four hours of senior SE/SA time for the census sample, which I would rather you grant explicitly than have Mark and Zac absorb quietly, since unbilled senior time is the exact constraint that caused this problem. And an introduction to an IPM, because the clearest structural finding in this work came from two people describing someone else's constraint.

**Mark and Zac.** Where the tech scopes and project folders actually live, and which of them you would trust a colleague to act on without checking. One closed engagement you would be willing to see a derived record for. And a pointer into TAM — theirs is the only corpus in the census that is not decaying, at 57% touched in twelve months against 19–21% for SA and IPM under identical billing pressure, and I would rather learn what they do than import a practice from outside.

**Not blocked on anyone.** I will finish the census design, draft the Drive access request, and produce the one hand-made record as soon as I have an engagement.

---

## Annex A — Evidence

Every load-bearing claim, with how it was produced. Grades, because these are not equally strong: **Measured** (a query that was run, method recorded, re-runnable) · **Floor** (a lower bound from an incomplete method) · **Read** (stated in a source read directly) · **Observed** (happened during this work) · **Assessed** (a judgement, with the comparison shown) · **Reported** (someone said it, attributed and timestamped).

| Claim | Grade | Source of record |
| --- | --- | --- |
| 3,173 pages; per-space counts; 26% / 59% recency | Measured | `research/current-state/confluence-corpus-census.md` — literal queries in its method block |
| TAM 57% vs SA 19%, IPM 21% | Measured | as above |
| ≥ 692 opportunity folders in Drive, 2026 | Floor | as above, `C-5`. Scrolled a file listing, covers A–W, Drive's API unreachable from a browser session |
| Drive is not connected, so its contents are unreadable | Read | `research/prior-art/ask-commerce.md` `AC-1`. A configuration state, not a platform limit: Anthropic's enterprise-search documentation lists Drive among supported sources and requires a Documents connector at setup. Resolved 2026-07-28 |
| Connector list is Confluence, Jira, Slack | **Read — as of 2026-07-27, unverified live** | Its configuration and AI Ops documentation. Its own docs say the set may grow and tell you to ask it directly; the spend cap prevented that. I have described a document, not observed a running system |
| Demotes SE/TAM/IPM; no authoritative source for solution knowledge | Read | `ask-commerce.md` `AC-2` |
| Six of seven principles implemented | **Assessed** | §1 of this document — dispute a row and the count changes |
| Contradictions hand-patched into its configuration | Read | `ask-commerce.md` `AC-4` |
| Claude org-wide, $1,000/person/month | Read | `research/current-state/ai-governance-constraints.md` `G4` |
| The cap binds | Observed | An attempt to test Ask Commerce on 2026-07-27 was refused for reaching the limit |
| Route is an AI Use Case Review, not a vendor intake | Read | `ai-governance-constraints.md` `G2` |
| The four structural holes; the two-month floor | Reported | `research/sources/knowledge-database-kickoff-2026-07-27.md`, attributed per speaker |
| Guest tokenization as the wrong-not-stale example | Reported | Mark, 00:18:13. **One example. §6 rests on it** |

Three weaknesses, stated here rather than left to be found. The wrong-not-stale assumption rests on that single example. No claim about Ask Commerce has been verified by *using* it — all of it is read from configuration, and the behavioural test is blocked on the spend cap. The Drive figure is a floor that counts folders where the Confluence figures count pages.

## Annex B — The request to AI Operations

Ready to send. Andrew, this reads better from you than from me.

> **Subject: Two requests for Ask Commerce — Drive contents, and an authoritative source for solution knowledge**
>
> Hi — I lead the SE/SA function and we have been looking at how our team finds prior solution knowledge. We started out planning to build a question surface, then found that Ask Commerce already does almost everything we had specified. Rather than build alongside it, we would like to ask for two changes.
>
> **First, Drive contents.** Our tech scopes and SA project folders live in Google Drive, and Ask Commerce can see those files but not read them. That is the single largest and most uniform body of solution knowledge we have — one folder per client opportunity, with the tech scope built from a shared template, and at least 692 opportunity folders for 2026 alone. Without it, the corpus that matters most to our team is invisible to the tool everyone uses.
>
> We think this is a smaller ask than it sounds. Anthropic's documentation for the enterprise-search surface lists Drive among the sources it searches, and the Workspace connector reads file contents rather than just filenames — so this looks like completing a setup rather than obtaining a capability. The one thing we could not confirm from the docs is whether Shared Drives behave the same as personal Drive, and nearly all of ours are Shared. If you already know the answer, that alone would help.
>
> **Second, an authoritative source for solution knowledge.** We understand the routing table designates sources of truth for tool approval, HR, equity and deployment, and that team and project spaces are demoted by default. That rule is doing its job — but it means the 3,173 pages across our SE, SA, TAM and IPM spaces can be searched and never treated as settled. We would like to propose a small, vettable space as a first authoritative entry rather than asking you to bless the whole estate. The Solution Architecture Knowledge Base is 66 pages, small enough that we can review all of it and stand behind what it says.
>
> **One question, and it is genuinely a question rather than a preamble to another ask.** Your instructions carry a maintained list of authoritative page IDs with a note that it needs updating whenever a page moves. What does that maintenance actually cost you? If designating a new source is expensive to keep true, we would rather know before proposing one — and it bears directly on a documentation-practice problem we are trying to fix on our side.
>
> Happy to bring the corpus measurements behind any of this. Thank you for building the thing — it changed our plan considerably, and for the better.

---

<sub>**Sourcing.** Every claim has one owning document, listed in Annex A; this plan cites and links rather than restating, because duplicated claims rot at different rates. Problem framing and the `P1`–`P8` claims: `research/problem-space/problem-statement.md`, which argues them. Census method: `research/pilot/phase-0-census-design.md`. Sponsor memo: `docs/decision-memo.md`. The write decision is the deliberate reopening of read-only that `decisions/0001-configure-first-pilot-as-prototype.md` requires.</sub>
