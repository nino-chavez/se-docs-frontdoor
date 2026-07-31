# Solution Plan — SE/SA Knowledge Capture

**Author**: Nino Chavez · **Date**: 2026-07-30 · **Format**: SCQ-R · **Revision**: 6
**Status**: In progress. The validation that gates everything else is now assigned rather than blocked — §1, and the action table in §7.
**For**: Andrew (sponsor), Mark, Zac. Annex B is addressed to AI Operations and is ready to send.

> **What changed in revision 2.** This responds to Andrew's notes. Three of them changed the plan rather than its wording:
>
> - **The Ask Commerce decision is now a hypothesis with named validation conditions**, not a settled conclusion. He was right that revision 1 asserted it, and Annex A already admitted the evidence did not support asserting it.
> - **Operational self-sufficiency is now a first-class requirement.** The sharpest of the three, and it cuts against my own recommended path.
> - **Phase 2 is scoped to evaluate and recommend**, not build.
>
> The audience test in §4 is his. §7's ask changed as a result.
>
> **Revision 3** folds in the 30 July sync. Four things moved: the tool is confirmed as an **answer engine, not document retrieval**; the audience is **SE, SA and TAM**, with TPM deferred; **both validation conditions are now assigned** to me and Alex Vela of AI Operations rather than blocked; and Commerce's move to full Google Enterprise accounts means the **licensing premise behind rejecting Gemini Enterprise has to be re-checked**. `research/sources/se-docs-frontdoor-sync-2026-07-30.md` owns the session.
>
> **Revision 4** adds the requirements that session produced and my first pass missed — the caution-wrapper ask, the explicit rejection of an access-control layer, the deferred-access placeholder Andrew requested, and the speed-over-generality trade. `research/requirements/front-door-requirements.md` owns them as `REQ-1`–`REQ-12` and is the checklist for the joint platform test.
>
> **Revision 5** lands Mark's answer on the source question, and it is worse than the plan assumed. His three main sources are Confluence `SA`, a shared Google Drive and **Lucidchart** — and Ask Commerce reads one of the three. `S-6a` owns it.
>
> **Revision 6** adds a defect class this plan did not have, found in a working internal system: a wrong *rule* that manufactures wrong records on every run, where refreshing reproduces the defect rather than fixing it. `research/prior-art/internal-vault-pattern.md` owns it.
>
> One warning about that session's record. The Gemini-generated notes state in their Decisions block that Phase 1 is "a document retrieval tool rather than an autonomous answer engine." **That is wrong** — the transcript and the notes' own Details section both say the opposite. Anyone working from that block will build the wrong thing. `S-1` documents it.

---

## Recommendation

**Do not build a search tool. Validate that Ask Commerce can close the gaps and that it is ours to run, send two requests to AI Operations, and run a two-week census.** I am not asking to build anything, and I am no longer asking for a yes-or-no on the write decision this week — Andrew's read that it is not a binary is better than the question I put to him.

## Situation, complication, question

We committed to building a front door to SE knowledge. The reasoning held: a decade of platform history sits in a shrinking number of people, and the documents that should hold it are a byproduct of billable delivery, so they thin out exactly where the billing stopped. Mark and Zac established the shape of that at kickoff — one-off client conversations that sometimes never enter a documented process, smaller engagements that get no folder, documentation that stops when IPM hours run out, and a template followed differently on every project.

The complication is that the front door already exists. `Ask Commerce`, built and maintained by our AI Operations team, is live, shared with every employee by default, and already implements six of the seven guiding principles this project committed to. It cites every claim with a last-modified date, flags anything over twelve months old, and surfaces conflicts rather than picking between them. Andrew, when you said "something similar to ask commerce," you were not reaching for an analogy — you were naming the system, and I filed it as an open question rather than checking.

That leaves the real question: **if the search tool is built, what is left worth building?**

My recommendation is above. The rest of this document is why I believe it, what would change my mind, and what I need from each of you. One caveat belongs here rather than buried: *the front door already exists* is a hypothesis I have evidenced from configuration and not yet tested by use, and §1 names what would have to be true before we act on it as settled.

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

That count is my assessment and the weakest-graded claim in this document, so it matters that it does not rest on one vendor.

**We are a Google Workspace shop, so I assessed the Google option rather than assume it away.** Gemini Enterprise covers the same source set with the same permission-aware, cited retrieval, and it does one thing Ask Commerce currently does not: its Drive connector treats shared drives as first-class configuration, scoped by named drive ID. That is our single biggest gap, documented as ordinary setup in a competing product.

**I am still not recommending it, for one reason that outweighs the rest.** It is a paid subscription, which routes it to a Vendor Intake rather than the AI Use Case Review this plan depends on — converting the cheap approval path into the expensive one, which is the trade this whole approach exists to avoid. Being a Workspace shop did not change that; Gemini Enterprise is a separate Google Cloud product, sold and licensed independently of Workspace.

**That premise is now under re-check.** Alex Vela reported on 30 July that Commerce moved to full Google Enterprise accounts within the last fortnight, having previously gone through a third-party vendor with partial features. If that changed what we are entitled to, the cost argument weakens and this reopens on evidence rather than on preference — which is exactly what the joint test in §7 is for. Add duplicate spend beside Claude Enterprise, and two ask-your-org surfaces that would disagree with nothing to adjudicate them, and it loses on our constraints rather than on its merits.

It stays on the shelf with a named revival condition in §5, and it is why §6's Drive-refusal branch now has an answer. `research/competitive/buy-landscape.md` owns the full assessment, including where the evidence is thin — I could not resolve Google's own pricing page, so no cost figure in this plan is one I would defend.

The wider point stands: two mature vendors ship the same principle set. These are table stakes in a mature category, not a specification we wrote first.

### What has to be true before we treat this as decided

Andrew's objection to revision 1 was that it stated the Ask Commerce decision as already made. He is right, and the previous draft was internally inconsistent about it: Annex A grades the six-of-seven count as **Assessed**, and admits that no claim about Ask Commerce has been verified by *using* it — every one is read from configuration, with the behavioural test blocked on a spend cap. A document cannot confess that and then open with a settled conclusion. Two conditions gate it, both his.

**One — it closes the gaps, in behaviour and not on paper.** Everything in the table above is read from its instructions. What a system is told to do and what it does are different claims, and only one of them is evidenced here. The test is real SE questions run against it, with the answers recorded. That has been listed as pending since 27 July, blocked on the per-person spend cap rather than on access. **It has now been promoted from a nice-to-have artifact to the gate on the recommendation**, which changes who needs to unblock it and how urgently.

**Two — it is ours to run.** This is the sharper condition and the plan did not have it. Relying on another team for every configuration change is a standing tax: it slows iteration and caps how fast the thing can improve. The concrete form is visible in its instructions, which carry a maintained list of roughly ten hardcoded Confluence page IDs with a note that the list needs updating whenever a page moves. Every source we add, every demotion rule we want changed, every contradiction that needs a patch is an edit to a prompt owned by AI Operations.

**This condition cuts against the path I am recommending, so I will state the cost rather than argue around it.** My plan routes everything through AI Operations — two requests now and an unbounded number later. It buys the cheap approval route and pays for it in operational latency, and revision 1 priced only the first half.

If the answer to "can we manage sources, configuration and updates directly" is no, then the alternatives get more attractive rather than less: **Gemini Enterprise and a thin build both share the property that we would control them.** That is a real argument in their favour and it is new. It does not yet outweigh a Vendor Intake and duplicate spend, but the margin is narrower than §5 implied, and the honest position is that this is a question for AI Operations before it is a conclusion of mine.

**Both conditions are now assigned rather than blocked, which is the most useful thing to come out of the 30 July sync.** Alex Vela of AI Operations and I own a joint test of what Claude and Google Enterprise can actually do today, including connector reach, permissions, and who enables restricted features. That pairs the behavioural question with someone from the team that owns the answer to the control question, and it means the first condition no longer waits on a budget decision and the second no longer waits on someone thinking to ask.

## 2. The corpus is the problem, and the unsolved part is invalidation

Two gaps separate what exists from what an SE actually needs, and both are about the corpus rather than the tool. Ask Commerce does not read Google Drive — it sees that a file exists and cannot open it — and the tech scopes and SA project folders live in Drive. That one is a setup that was never finished rather than something the platform cannot do, which is why it belongs in a request and not in a build. It also has no authoritative source designated for solution knowledge, and it explicitly demotes the `SE`, `TAM` and `IPM` spaces, so even the pages it can read it will never treat as settled.

**Mark answered the source question on 30 July, and it is worse than the paragraph above implies.** His three main sources are the Confluence `SA` space, a shared Google Drive, and Lucidchart. Ask Commerce reads the first and neither of the other two. It is also connected to Jira and Slack, which he did not name. **One of three.** The corpus the census measured so precisely turns out to be about a third of what a senior SA actually reaches for.

Lucid is new to this work and brings a constraint with it. An official Claude connector exists, but it is delivered as an MCP server, and `G2` records that new MCP triggers an AppSec review — the one cost every path chosen so far was designed to avoid. Whether it can attach to an enterprise-search surface at all is unresolved and is the first question for the joint test.

The measurements support taking this seriously. Across the five spaces holding SE, SA and delivery knowledge there are **3,173 pages, of which 26% have been touched in the last twelve months** and 59% have not been touched in two years. The `SE` space is the smallest of the five at 155 pages, which explains the round trip better than any theory: an SE asks a person because the answer was never filed anywhere an SE would look.

Drive is larger by an order of magnitude. The 2026 opportunity folder alone holds **at least 692 opportunity folders** — a floor rather than an audit, and counting folders where the Confluence figures count pages, so the comparison holds directionally and not as a multiple. The census owns these numbers and the queries behind them.

The strongest evidence is not a number. Ask Commerce's own configuration carries hand-written patches for individual contradictions in our documentation — one page that uses two different names for the same Slack channel, two pages that disagree on a GitHub organisation name, with an instruction not to state that name confidently. Every contradiction in our corpus becomes a line of configuration that a person writes and maintains. It works, and it does not scale. **One team is already absorbing our documentation defects by hand, one defect at a time**, which is the argument for fixing capture made from our own systems rather than from theory.

Capture itself is not the unsolved part, and a scan of that market is what narrows it. Drafting a record from an existing artifact, routing it to a named owner and expiring it on a clock all ship commercially today. What does not ship: invalidating a document *because a shipped capability made it wrong*, or holding negative knowledge as a record rather than as prose. **The gap is invalidation** — narrower than the claim this section used to make, and a much smaller thing to build.

One addition, from a working internal system rather than from theory. This plan has distinguished documents that are *stale* from documents that are *wrong*. There is a third case and it is the worst of them: **a wrong rule that generates wrong records on every run.** An internal vault hard-codes its canonical facts into the instructions its refresh routine follows, and one of those facts — the location of a repository — names an organisation that does not exist. I verified that on 31 July.

Refreshing does not correct it; refreshing re-asserts it, and every output arrives correctly dated and confidently wrong. A staleness detector built on timestamps would rate those notes the healthiest in the corpus.

**That matters here because the capture system in §4 is the same shape** — records generated from instructions and templates. **Invalidation has to cover the generator, not only the output.** `research/competitive/buy-landscape.md` owns that scan and grades it, including where it is thin.

## 3. Three things block the path, and none of them are mine to decide

Two of the three are requests to a team I have no authority over, which is the part of this that needs you rather than me. AI Operations would need to connect Drive contents to Ask Commerce, and to designate an authoritative source for solution knowledge.

The first is completing a setup their own platform documents — Drive is a supported source for the surface Ask Commerce runs on, and was never connected here. The second is harder, because every current entry on that list is owned by a governance or platform function and domain knowledge would be a new category — which is why I would open with a small, vettable space rather than asking them to bless the estate. Annex B is the request, written and ready to send.

Those two requests are not independent, and it took me too long to see it. Records produced by capture would land in Confluence, which Ask Commerce reads — but they would land in a *team* space, which its rules structurally demote. Without the authoritative-source designation, capture manufactures records the search tool is instructed not to believe. **The Drive request unblocks the corpus we already have; the authority request unblocks the corpus we would create.**

The third is the write decision, and Andrew's reframe of it is better than the question I asked. Revision 1 put it as a binary — does this write, or stay read-only — on the reasoning that a write system is a larger security and privacy surface. **His answer is that this initiative should not be building recording processes at all initially; it should be evaluating the current ones and handing the findings to the managers who own them.**

That is a scope reduction on the part of the plan I had called the differentiated value, and I think it is correct, for a reason I had not articulated: we do not own the processes we would be changing. Shane and his peers do. A plan that proposes new capture practice without them is proposing something it cannot land.

So the third blocker is no longer a decision I need from Andrew. It is a sequencing constraint: **evaluate, report to the process owners, and let them decide what changes** — with two exceptions he named and I would keep. If the gap turns out to be closable trivially, a folder structure in Drive being his example, that belongs in Phase 1 rather than waiting for a phase boundary. And if the storage or documentation processes are likely to change shortly after we deliver, we need to know whether that forces a rebuild — which is a design requirement, and §4 now carries it.

Governance is not the obstacle I expected it to be. Claude is already deployed to every employee with no approval gate, and the route for pointing an approved tool at new data is an AI Use Case Review rather than a vendor intake. What that review costs in time is the one number I still owe you.

---

## 4. What I recommend we do

**Finish the census. Two weeks, roughly four hours of senior time.** The Confluence half is done and is where the figures above come from. Drive needs real API access rather than the file-listing scrape that produced the floor. The quality half matters more than the volume half, because timestamps find *stale* and cannot find *wrong* — Mark's guest-tokenization case is a document that is confidently, actively incorrect and looks identical to a good one in every count I can run. Finding those means joining shipped platform capabilities against documents that predate them, plus a small adjudicated sample to establish a rate.

That join is also the one capability the market scan found nobody shipping, so the census as already designed measures the exact thing that would justify building anything. The narrowing in §2 costs no redesign.

It should also test the cheapest hypothesis anyone has put forward, which is Andrew's: that part of the gap is not missing documents but missing *places to put them*. If a meaningful share of what an SE cannot find turns out to exist already, sitting somewhere nobody thinks to look, then a folder structure and a naming convention close more of this gap than anything else in this plan — and they close it in Phase 1, for days of work rather than a quarter.

**Send the two requests now, in parallel.** Neither depends on the census finishing. The Drive one should be cheap to grant, since it asks for a documented setup rather than a new capability; the authority request is the one that needs a sponsor behind it.

One consequence of that request cuts against me, so I would rather name it than have it found. Connecting Drive makes at least 692 unaudited opportunity folders reachable through a tool people trust, with citations attached. Better retrieval over a defective corpus surfaces the defects faster — if the wrong-not-stale rate in Drive is high, the request I am pressing for spreads them rather than fixes them.

Two things stop that being an argument against sending it. Ask Commerce demotes team-space content by default, so nothing arriving from Drive is treated as settled. And the census is the thing that measures the rate. But it does mean the two should run together rather than in sequence: if the request lands first and the rate turns out to be bad, we will have made the corpus more reachable without making it more correct.

**Produce one record by hand — as evidence for the process owners, not as a prototype.** Take one closed engagement, produce its record manually from the transcripts and tech scope that already exist, and ask the SA who ran it whether they would have wanted it. That costs a day and can end the project, which makes it the cheapest decision-grade evidence available. Under the reframe in §3 it does a second job: it is the artifact to put in front of Shane and his peers when we report, because *documentation practice should change* lands differently next to a record showing what the change would produce.

**Write where the reader can read.** This is a constraint on the capture design rather than a task: the target is set by the retrieval surface's reach, not by what is convenient to build. Records that land anywhere Ask Commerce cannot see would recreate exactly the problem we are trying to solve, for a corpus of our own making.

**Surface conflicts where the reader is looking, not into a queue.** The sibling of the constraint above, and it corrects something §1 scores as satisfied. The same internal vault implements *surface conflicts, do not adjudicate* better than most — it has an explicit written arbitration policy — and the principle still fails, because unreconciled items are parked in a registry the reader never opens. Five sit there now, one of them a contradiction on a headline commercial fact.

The conflict is documented and invisible at the same time. **A conflict routed somewhere the asker will not look is, from where they stand, the same as no conflict at all.**

**Build an answer engine, not a document retrieval tool.** Decided on 30 July, and it is worth stating flatly because the meeting's own notes record it backwards. An agent reasons over the corpus and produces an answer with citations; it does not hand back a list of files. Andrew's test for it was the practical one — you could not do this without an agent, and Ask Commerce already works this way.

**Define the audience by who can evaluate an answer, not who would benefit from it.** Andrew's test, sharpened by what the room actually worried about. The concern was not comprehension in the abstract; it was someone forwarding an unreviewed answer to a client. Phase 1 access is therefore **SE, SA and TAM**, with TPM deferred on Mark's caution that the results carry nuance. Some answers will be wrong — that is assumed, not hoped against, and it is the whole reason the boundary exists. The pilot has to watch not just whether answers are right, but whether they are safely usable by whoever asked.

**Revisit wider access in a later phase — Andrew asked for this note specifically, so here it is.** Opening this beyond SE, SA and TAM is wanted, not refused. What has to be worked out first is which material a wider audience should see, which is a different question from whether they would find it useful. Mark's version of the safeguard is the one to design against: not access control, but a caution attached to an answer that says *be careful, this may be more technical than it looks*. Whether any candidate platform can do that is now a line item in the joint test.

**Serve SE and SA fast; a rebuild to widen later is an acceptable price.** Andrew's trade, and it is worth recording because it cuts against the instinct to generalise: if this can be done in a fraction of the time by serving the two groups it is for, that is the goal, and he pre-authorised going bespoke later if broadening demands it. Note the distinction from the constraint above — **sources moving must not force a rebuild; the audience widening is allowed to.**

**Design for the sources moving.** If the process owners change where documents live — which is the whole point of reporting to them — then a solution that needs rebuilding when they do was the wrong solution. In practice: configuration over code, named sources over hardcoded ones, and no assumption about folder layout. This is Andrew's requirement and it is also the strongest technical argument for the configured path over a build.

**Sequence discovery support last.** Generating the hard questions for a merchant depends on negative knowledge being present and current, which is the decay problem the earlier phases exist to address. The tech scope you demonstrated already does a version of it and is the right starting point.

## 5. What I recommend we not do

Each of these was in scope at some point, and each is excluded on evidence rather than preference.

| Not doing | Why | What would reopen it |
| --- | --- | --- |
| Building a question surface | It exists, org-wide, maintained by another team | AI Ops deprecating it |
| Building connectors ourselves | A request to AI Ops, not an engineering task. Our own would trigger an AppSec review and duplicate their roadmap | A refusal — which is a stop-and-replan signal, not a build trigger |
| Buying a second question surface | Gemini Enterprise is the strongest candidate and it documents Shared Drive support we lack. But it is a paid subscription, so it is a Vendor Intake rather than the AI Use Case Review this plan depends on — the expensive route we are deliberately not taking — and two ask-your-org surfaces would diverge with nothing to adjudicate them | AI Ops declining Drive **and** the census showing Drive holds the majority of decision-grade knowledge. Both, not either. Added in revision 2: **or** AI Operations confirming we cannot manage sources and configuration directly, which would make control the deciding factor instead of cost. Added in revision 3: **the cost premise itself is under re-check** — Commerce moved to full Google Enterprise accounts in late July, and if that changes what we already hold, this row's main argument weakens |
| Building capture workflow from scratch | Draft-from-artifact, route to an owner, expire on a clock all ship commercially. But §4's write-where-the-reader-can-read constraint rules those products out as destinations, because Ask Commerce cannot see them. Take the pattern, not the tool | A capture product that writes natively into Confluence or Drive |
| Remediating the existing corpus | Unbounded, and it does not address why the corpus got that way | A specific high-traffic subset shown to be actively harmful |
| Designing a new template | One exists and is followed differently every project. The constraint is unbilled hours, not template quality | Evidence that the template, not the time, is what fails |
| Adjudicating contradictions automatically | Locked at founding: surface conflicts, do not resolve them | Nothing foreseen. An invariant |
| Classifying documents and building an access-control layer over them | Ruled out in the 30 July sync. It means marking every source with who may see it and why, then maintaining that — a scope explosion for a Phase 1 whose audience is three groups who can already open everything in it | A materially different audience, not a safeguard requirement. `REQ-4`'s caution wrapper is the cheap way to get most of this |
| Indexing everything | Coverage follows verified quality | A census showing uniformly high quality, which nobody expects |
| Writing code before one record exists by hand | The manual test can end the project in a day | That test passing |

## 6. What would change my recommendation

Two assumptions carry it, and both are weaker than the rest of this document.

**That the wrong-not-stale problem is big enough to justify the work.** This rests on a single example — guest tokenization, from Mark. Everything in §4 depends on it and nothing has measured it. If the census sample comes back showing a low rate, the honest conclusion is that better search over a mostly-accurate corpus was enough, and this project ends with the two requests.

That is a cleaner test than it was a week ago: invalidation is the only capability the market scan found nobody shipping, so **if invalidation is not needed there is nothing left to build** — not a smaller build, none. That is the outcome I consider most likely to prove me wrong.

**That an SA would actually want a derived record.** Untested, and the one-record test in §4 is designed to find out cheaply before anything is built.

**That whatever we build keeps running.** The internal vault in `internal-vault-pattern.md` has twenty-two commits, one author and no scheduled execution — it runs when a laptop is awake, it last ran a week ago, and nothing tells a reader that. `P2` says documentation stops when the billable hours stop; this is the same structure one level up, where **automation stops when one person's attention stops** and announces it less readily than a person would.

It is also the price of §1's second condition: a system that is ours to run can quietly become one person's laptop. Any capture we propose needs a named owner, execution off anyone's workstation, and a visible heartbeat.

**That the questions SEs ask stay document-shaped.** Ask Commerce answers *find me the document* well, which is the right shape for a corpus of prose. Capture would change the corpus into uniform records, and uniform records invite aggregate questions — how many engagements hit this limitation, which workarounds recur across clients — where a federated search returns three documents and the asker wanted a distribution.

Negative knowledge has the same problem in a sharper form. Knowing what the platform cannot do, and whether that limitation still holds, looks more like a maintained register than a search index — and `P6` says that is the category which decays fastest and matters most. If Phase 0's demand work shows those questions are common, *don't rebuild retrieval* narrows to *don't rebuild search*, and a small query surface over the structured records earns its place. That is a far smaller build than the one we started with, and it is not decidable until we know what people actually ask.

**That Ask Commerce can be ours to run.** §1 states the condition and what it costs if false; it appears here because it is the likeliest of these to come back negative, and because it is the one I did not think to ask before Andrew did. If AI Operations cannot give us direct control of sources and configuration, §5's comparison changes — not because the alternatives got cheaper, but because operational latency turns out to be a price paid every week rather than once.

Two more that would change the shape rather than the direction: if AI Operations declines the Drive connection — less likely now it reads as a documented setup, and it no longer leaves us without a move, because Gemini Enterprise documents shared-drive scoping as ordinary configuration and would become worth a Vendor Intake if the census showed Drive holds the knowledge that matters; and if reviewer time is not committed, the verification step degrades into rubber-stamping, which would make a generated record worse than no record at all.

I would rather these be written down and wrong than unwritten and right.

---

## 7. What I need from each of you

**Andrew.** Not the write decision any more — your reframe replaced it, and it was the better question. Four things instead:

- **The spend cap lifted for a day**, so the behavioural test in §1 can run. It is now the gate on the whole recommendation, and it is blocked on budget rather than access.
- **The two requests in Annex B** — they land differently from you than from me, particularly the authoritative-source one and the self-management question your notes prompted.
- **Roughly four hours of senior SE/SA time** for the census sample, granted explicitly rather than absorbed quietly by Mark and Zac, since unbilled senior time is the exact constraint that caused this problem.
- **An introduction to Shane and to an IPM** — the process owners we would report findings to under your Phase 2 reframe, and the source of the clearest structural finding in this work.

**Mark and Zac.** Where the tech scopes and project folders actually live, and which of them you would trust a colleague to act on without checking. One closed engagement you would be willing to see a derived record for. And a pointer into TAM — theirs is the only corpus in the census that is not decaying, at 57% touched in twelve months against 19–21% for SA and IPM under identical billing pressure, and I would rather learn what they do than import a practice from outside.

**Not blocked on anyone.** I will finish the census design, draft the Drive access request, and produce the one hand-made record as soon as I have an engagement.

### Committed actions from the 30 July sync

These are assigned, not proposed. `research/sources/se-docs-frontdoor-sync-2026-07-30.md` is the record.

| Owner | Action | Why it matters here |
| --- | --- | --- |
| **Nino, Alex Vela** | Test what Claude and Google Enterprise can actually do today — connector reach, permissions, who enables restricted features | Answers **both** §1 validation conditions, and re-checks the Gemini Enterprise cost premise. The critical path |
| **Mark, Zac** | List the sources reached for daily | Scopes the MVP corpus. Figma is new and not in our landscape doc |
| **Zac** | Confirm with Levi where project documentation lives; establish a standard location if none is designated | Tests the cheapest hypothesis in §4 — that part of the gap is missing *places to put things* |
| **Mark** | Confirm Phase 1 access groups | Substantially answered in the session: SE, SA, TAM. TPM deferred |
| **Nino** | Business-format the planning documents for management | `docs/memo-leadership.md` and `docs/memo-team.md` |

**One open item nobody owns.** Andrew referenced something transcribed as "M.com" as another route for pulling data out of repositories. The transcription is unreliable and I cannot recover the referent. I will ask rather than guess.

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
| Gemini Enterprise documents Shared Drive scoping | Read | `research/competitive/buy-landscape.md` — vendor Drive data-store doc, resolved 2026-07-29. `SharedDriveIds` under `admin_filter` / `admin_exclusion_filter` |
| Adopting it would be a Vendor Intake, not a Use Case Review | Read | as above, against `G2`'s intake list. Its per-seat pricing is third-party-sourced only and graded **warn** there — no figure should be quoted from this plan |
| The four structural holes; the two-month floor | Reported | `research/sources/knowledge-database-kickoff-2026-07-27.md`, attributed per speaker |
| Guest tokenization as the wrong-not-stale example | Reported | Mark, 00:18:13. **One example. §6 rests on it** |

Three weaknesses, stated here rather than left to be found. The wrong-not-stale assumption rests on that single example. No claim about Ask Commerce has been verified by *using* it — all of it is read from configuration, and the behavioural test is blocked on the spend cap. **That weakness is what Andrew's first objection identified, and §1 now treats it as the gate rather than as a footnote here.** The Drive figure is a floor that counts folders where the Confluence figures count pages.

## Annex B — The request to AI Operations

Ready to send. Andrew, this reads better from you than from me.

> **Subject: Two requests for Ask Commerce — Drive contents, and an authoritative source for solution knowledge**
>
> Hi — I lead the SE/SA function and we have been looking at how our team finds prior solution knowledge. We started out planning to build a question surface, then found that Ask Commerce already does almost everything we had specified. Rather than build alongside it, we would like to ask for two changes.
>
> **First, Drive contents.** Our tech scopes and SA project folders live in Google Drive, and Ask Commerce can see those files but not read them. That is the single largest and most uniform body of solution knowledge we have — one folder per client opportunity, with the tech scope built from a shared template, and at least 692 opportunity folders for 2026 alone. Without it, the corpus that matters most to our team is invisible to the tool everyone uses.
>
> To put a number on it: we asked our most senior SA which archives he works from. He named three. Ask Commerce reads one of them. It is connected to two sources he did not name, and cannot read the two he did.
>
> We think this is a smaller ask than it sounds. Anthropic's documentation for the enterprise-search surface lists Drive among the sources it searches, and the Workspace connector reads file contents rather than just filenames — so this looks like completing a setup rather than obtaining a capability. The one thing we could not confirm from the docs is whether Shared Drives behave the same as personal Drive, and nearly all of ours are Shared. If you already know the answer, that alone would help.
>
> And if Shared Drives are the sticking point, one thing from the wider category might be useful. Google's Gemini Enterprise exposes shared-drive scoping as an explicit include-or-exclude filter over named drive IDs, so an administrator can point it at a single shared drive without opening the estate. We are not suggesting we go and buy that — we mention it because that shape, scope to one named drive rather than all-or-nothing, is probably what makes this easy to say yes to. It is the shape we would ask for.
>
> **Second, an authoritative source for solution knowledge.** We understand the routing table designates sources of truth for tool approval, HR, equity and deployment, and that team and project spaces are demoted by default. That rule is doing its job — but it means the 3,173 pages across our SE, SA, TAM and IPM spaces can be searched and never treated as settled. We would like to propose a small, vettable space as a first authoritative entry rather than asking you to bless the whole estate. The Solution Architecture Knowledge Base is 66 pages, small enough that we can review all of it and stand behind what it says.
>
> **One question, and it is genuinely a question rather than a preamble to another ask.** Your instructions carry a maintained list of authoritative page IDs with a note that it needs updating whenever a page moves. What does that maintenance actually cost you? If designating a new source is expensive to keep true, we would rather know before proposing one — and it bears directly on a documentation-practice problem we are trying to fix on our side.
>
> **A second question, and this one shapes whether we build on Ask Commerce at all.** How much of the configuration can a requesting team manage directly? If adding a source, adjusting a demotion rule or patching a contradiction is always an edit to instructions your team owns, we would like to understand the turnaround, and whether there is a supported way for us to hold some of it ourselves. We are not asking to edit your prompt. We are trying to work out whether to route our team's needs through you — which we would rather do — or to stand something up separately, which we would rather not.
>
> Happy to bring the corpus measurements behind any of this. Thank you for building the thing — it changed our plan considerably, and for the better.

---

<sub>**Sourcing.** Every claim has one owning document, listed in Annex A; this plan cites and links rather than restating, because duplicated claims rot at different rates. Problem framing and the `P1`–`P8` claims: `research/problem-space/problem-statement.md`, which argues them. Census method: `research/pilot/phase-0-census-design.md`. Sponsor memo: `docs/decision-memo.md`. The write decision is the deliberate reopening of read-only that `decisions/0001-configure-first-pilot-as-prototype.md` requires.</sub>
