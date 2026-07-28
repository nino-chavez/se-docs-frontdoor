# Knowledge repository — revised plan

**To:** Andrew (sponsor), Mark, Zac
**From:** Nino
**Date:** 2026-07-27
**Status:** Draft v2 for the first weekly sync. Supersedes the version I circulated earlier the same day — the plan changed enough that patching it would have hidden the change.

---

## The short version

I went looking for whether "ask commerce" existed. It does. And it already does most of what I proposed building.

That is the whole memo. The rest is what's left.

**Ask Commerce** is a Claude surface the AI Operations team configured and maintains. It's live, it's shared with everyone by default, it's already in your Claude sidebar, and it searches Confluence, Jira, and Slack with your own permissions applied. It cites every claim with a link and a last-modified date. It flags sources older than twelve months. When two pages disagree, it shows both and names the conflict instead of picking one.

I had written six guiding principles for a thing to build. Ask Commerce implements all six.

Andrew — when you said "something similar to ask commerce" and later "directly within CLA, like ask commerce," I read that as an analogy for the kind of thing you wanted. It wasn't. You were naming the actual system. You were right and I filed it as an open question.

## What I got wrong, briefly

The earlier memo planned a build over a corpus we hadn't measured. Two corrections:

The **retrieval problem is largely solved**, by another team, using a configured product rather than custom software. My "configure rather than build" recommendation was correct and also late — AI Ops got there first and shipped it company-wide.

The **approval story is not what I thought.** I'd assumed a licensing and access problem. Every employee already has Claude — no request, no seat, usage-based billing. The two-month floor you put on this, Andrew, was real for a *build*. For what I'm now proposing, the path is an AI Use Case Review because Claude is already approved and we'd be pointing it at new data. That's a much smaller ask.

## What it can't see, and why that's the whole problem

Ask Commerce reads Confluence, Jira, and Slack. **It cannot read Google Drive.** It can see that a Drive file exists and cannot open it.

The tech scopes are in Drive. The SA project folders are in Drive. The `Opportunities` shared drive holds roughly **seven hundred client opportunity folders for 2026 alone** — one per opportunity, each with a tech scope built from the same template. That number is a floor from counting the folder listing directly; it isn't audited, and earlier years aren't in it.

For comparison, here's what's in Confluence, which Ask Commerce *can* read:

Across the five spaces that hold SE, SA and delivery knowledge: **3,173 pages, of which 26% have been touched in the last twelve months.** The `SE` space itself is the smallest at 155 pages. `TAM` is the healthiest by a distance at 57% fresh; `SA` and `IPM` sit at 19–21%.

*(Full per-space table, the queries behind it, and the caveats live in the census — `research/current-state/confluence-corpus-census.md`. I'm not restating it here so there's only one copy to keep true.)*

Three things fall out of those numbers.



**One year of Drive opportunity folders is four times the entire SE Confluence space.** The corpus that matters most is the corpus the tool can't open. Andrew, you proposed starting with tech scopes and the SA folder — that instinct now has a number behind it.

**The SE space is the smallest and the stalest.** The knowledge lives in IPM, SA, and TAM. That is why a sales engineer asks a person: the answer was never filed anywhere an SE would look. The round trip isn't a habit anyone needs to break. It's the shape of where the documents are.

**Three quarters of it hasn't been touched in a year.** Against Ask Commerce's own twelve-month rule, most of this corpus would arrive flagged as possibly stale.

There's a fourth thing that isn't about coverage at all. Ask Commerce deliberately treats team spaces — SE, TAM, IPM among them — as *not authoritative*. It has a list of topics with a designated source of truth: tool approval, HR, insider trading, deployment. There is no entry for how we solve things for clients. So even the pages it can read, it will never treat as settled. **That's a standing problem, not a coverage problem, and it's the more interesting of the two.**

## The argument that survives, now with evidence

I claimed last time that what gets written down bounds what any search tool can return. I argued it from first principles. I can now show it from our own system.

Ask Commerce's configuration contains hand-written patches for specific contradictions in our documentation. One page uses two different names for the same Slack channel, so the correct one is hardcoded. Two IT pages disagree about a GitHub organization name, so it's instructed not to state that name confidently and to send you to a human instead.

Every contradiction in our corpus becomes a line of configuration that a person writes and maintains. That works. It does not scale. One team is absorbing our documentation defects by hand, one defect at a time.

Mark, your guest-tokenization example is this same class — a documented workaround that exists because a capability was missing, still on the page after the capability shipped. No amount of retrieval quality fixes that. Somebody either updates the page or hardcodes an exception.

## The plan

### Phase 0 — Count what we have. Partially done.

I ran the Confluence half; it's the table above. Drive is sized but not audited, and that needs real API access rather than me scrolling a file list.

The hard part is untouched, and I want to name it rather than let it look finished. **Timestamps find stale. They don't find wrong.** Everything above measures when a document was last edited. Mark's guest-tokenization case is a document that is confidently, actively wrong, and it looks identical to a correct one in every count I can run. Sizing that means reading a sample and deciding what counts as wrong. I don't have that method yet, and it's the most valuable thing left to design.

### Phase 1 — Two requests, not a build

Ask AI Operations for:

1. **Drive contents connected**, starting with tech scopes and the SA folders.
2. **An authoritative source designated for solution knowledge**, so what we do have counts for something.

The second is the harder ask. Every current entry on that list is owned by a governance or platform team. Domain knowledge would be a new category. I'd start small and specific — the Solution Architecture Knowledge Base is 66 pages, small enough to actually vet — rather than asking them to bless the whole estate.

Your release guardrail, Andrew — don't ship a phase that returns bad or old information — is already built into how Ask Commerce behaves. That's an argument for working inside it rather than beside it.

### Phase 2 — Fix the capture side. This is now the real work.

Zac's failure is the one to solve: documentation stops when the hours stop. Any fix that asks for more writing on unbilled time loses to the same pressure that caused the problem. A template already exists and isn't followed uniformly, so the question isn't what the template should say. It's what we can derive from work that's already happening.

One lead worth more than any framework I could bring: **TAM's documentation isn't decaying.** 57% of their pages were touched in the last year, against 19–21% for SA and IPM, under the same billing pressure. Something in how that team works produces documentation that stays current. I'd rather find out what it is than import a practice from outside.

This is still the half that might be out of scope, because recording knowledge is a write and everything else here reads. That's decision 1.

### Phase 3 — Help ask the hard questions

Unchanged, and still last. Mark framed it as a concern on the call — the tool spits out twenty questions you have to ask, including ones we can't do. Andrew, your answer was that those are exactly the questions worth asking. It depends on the negative knowledge being present and current, which is the decay problem Phases 0 through 2 exist to address. The tech scope you demonstrated already does a version of this; I'd build from it rather than beside it.

## What changes for each of you

| Who | What you'd be able to do | Phase |
| --- | --- | --- |
| **Sales engineers** | Ask what the platform can't do for a requirement and get an answer with a link — or a clean "no record of this," which is also actionable. Today: guess, or interrupt someone. | 1 |
| **Zac** | Pick up an implementation and see what was sold and why, including whether it predates a platform change that invalidates it. Stop reconstructing it from memory. | 1 |
| **Mark** | Get a scope that already names the platform limits and agreed workarounds, rather than finding them mid-implementation. | 3 |
| **Andrew, as one of the few who carry the history** | Redirect a repeat question without checking the answer afterward. Both halves matter — fewer interruptions isn't a win if you're correcting the bot. | 1 |
| **Delivery / IPM** | Have what you built recorded without unbilled write-up hours. Needs decision 1. | 2 |
| **Andrew, as sponsor** | Approve a scope that's mostly requests and one real piece of work, instead of a build. | This memo |

The row I'd still watch is delivery/IPM — the only one a read-only system can't deliver, and the one I have the least direct evidence for, because nobody in that role was on the call.

## What I need decided

Question 3 from the last memo is closed. What replaces it is smaller.

| # | Decision | Why it matters | Owner |
| --- | --- | --- | --- |
| 1 | **Does this write, or only read?** | Phase 2 means changing what gets recorded. That's a write system and a bigger privacy surface. It's also where the remaining value is, now that retrieval is largely handled. This is the decision that determines whether this project is worth doing. | Andrew + me |
| 2 | **Who is this for?** | The kickoff went SE, then SE and SA, then anyone. Ask Commerce already serves everyone, so this now means: whose questions do we optimize the authoritative sources for. I'd start with SE and SA. | Andrew |
| 3 | **Do we ask AI Ops, or do we ask through you?** | Both Phase 1 requests go to a team I have no standing with. A sponsor request lands differently than an individual one, particularly the authoritative-source ask. | Andrew |
| 4 | **What's the budget?** | Different question than last time. Claude is usage-based with a $1,000 monthly cap per person — I hit mine while researching this memo. If SE questions route here at volume, that cap is the cost model, and somebody should look at it before we encourage the traffic. | Andrew |

## What this memo still doesn't do

**The measurement isn't defined.** Same gap as last time and I haven't closed it. What to displace is the person-to-person round trip. The obvious instrument was your DM history with the SAs, but you described that channel as you asking them — "I just bug them that often" — which counts your outbound questions, not inbound demand on you. Both are real, both worth displacing, and they aren't the same number. Naming the instrument is Phase 0 work.

**Your second success criterion still has no home.** You named two things on the call: the system working, and a written diagnosis of where our documentation practice breaks, with recommended changes. This memo now has considerably more material for the second — the census, the TAM contrast, the hand-patching evidence — but I still haven't scoped it as a deliverable with a date.

**I haven't actually used Ask Commerce against real SE questions.** Everything above is from reading how it's configured, not from testing what it returns. I intended to run a dozen real questions through it and hit my usage cap first. That test is the single most useful thing to bring to the sync, and I'd like to run it before we meet.

**Phase 0 still has no duration**, and now it partly depends on how quickly the Drive access question moves.

## What I'd like from you three

**Mark and Zac** — still the bullet list, and now a sharper version of it. Where the tech scopes and project folders actually live, which of them you'd trust a colleague to act on without checking, and where the stuff with no home ends up. Informal is fine; a Slack message beats a document. Plus GitHub usernames and I'll add you to the working repo.

**Andrew** — decisions 1 and 3. Decision 1 is the one that decides whether this is a project or a support ticket.

I'll set up the weekly sync. I'll bring a Phase 0 proposal with a duration, and the results of actually testing Ask Commerce if my cap resets or gets raised in time.

Push on the sequencing. My confidence in Phase 2 being the real work is higher than my confidence that Phase 1's two requests will be granted — and if AI Ops says no to connecting Drive, this plan needs rethinking rather than patching.

---

<sub>**Traceability** — the "What changes for each of you" table is this memo's statement of what each persona can do once this lands, written in the reader's language rather than research vocabulary. Recommendations map to `research/personas-and-jtbd.md` as follows: Phase 0 and Phase 1 serve `se/JOB-1` and `sa/JOB-1`. The measurement serves `knowledge-holder/JOB-1`. Phase 2 serves `delivery-ipm/JOB-1`, the job that forces decision 1. Phase 3 serves `sponsor/JOB-2`. The memo serves `sponsor/JOB-1`. Evidence: `research/problem-space/problem-statement.md` (canonical framing), `research/prior-art/ask-commerce.md` (`AC-1`–`AC-4`, what exists and what it can't see), `research/current-state/confluence-corpus-census.md` (`C-1`–`C-5`, the numbers), `research/current-state/ai-governance-constraints.md` (`G1`–`G8`, approval route).</sub>
