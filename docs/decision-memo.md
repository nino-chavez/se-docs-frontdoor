# Knowledge repository — straw man plan

**To:** Andrew (sponsor), Mark, Zac
**From:** Nino
**Date:** 2026-07-27
**Status:** Draft for the first weekly sync. This is the "halfbaked within the week" I committed to on the kickoff — built to be argued with, not approved.

---

## The short version

Mark was right, and it changes the plan.

The premise going into the kickoff was that the documents exist and are hard to find. Mark's objection was that they often don't exist. Between the two of you, four distinct holes:

- **One-off client conversations.** A lot of client discussion is Q&A that never enters a documented process at all (Mark).
- **Smaller engagements often get no project folder.** Big or complex projects reliably do, with diagrams; the example was the ones with only twenty hours (Mark).
- **Documentation stops when IPM hours run out.** Solutions half-worked-through, and no completed retrospective on a lot of real buildouts (Zac).
- **The template is followed differently every time.** A standard template exists, but per-project variance defeats any universal schema over the whole corpus (Zac).

That isn't a caveat on the plan. It's a different problem.

A search tool over documents assumes the documents are the supply. What we actually have is a supply problem: the corpus — every document we'd search across — is a byproduct of billable work, so it thins out exactly where the billing stopped. No amount of retrieval quality recovers a retrospective nobody wrote.

So I'd frame this as two efforts that were previously one:

1. **Get answers out of what exists** — and be honest about how much that is.
2. **Change what gets written down** — so this is worth doing again in a year.

The second one bounds the first. That's the whole argument in this memo.

## The most valuable knowledge is also the least durable

Andrew, your strongest example was the deal we won because we told the client what the platform couldn't do, and how to solve it, while every other vendor hid it. That reframes what the valuable content actually is: not what the platform does, but what it doesn't, and the workaround.

Here's the problem with that. It's also the fastest-decaying content we have. Mark's guest-tokenization example is exactly this — we have documents describing workarounds that exist *because* a capability was missing. The capability shipped. The documents are now wrong, not just old, and the current approach is undocumented because it's new.

The most valuable category is the least durable. Any version of this that indexes documents without tracking *when* something was true will be most confidently wrong about the thing we most want it for.

That single constraint drives most of what follows.

## Guiding principles

1. **Cite everything, or say nothing.** An answer with a link a person can open is useful. A confident answer with no source is worse than no answer, because someone will act on it in front of a client.
2. **Recency is correctness here, not metadata.** Given the above, "when was this true" has to be first-class.
3. **Surface conflicts; don't resolve them.** When two sources disagree, show both and flag it. We will have contradictions — silently picking one is how we ship a wrong answer with a real citation attached.
4. **Don't require a structure we don't have.** Every project documents differently. Any design that needs a uniform schema across the corpus is designing for a corpus we don't have.
5. **Measure against the current system, which is a person.** Today a hard question gets answered by a person-to-person round trip through one of the few people who carry the history. That's the baseline, and the round trip is the thing to displace.
6. **Scope coverage by verified quality, not ambition.** Indexing everything means indexing the stale and the wrong alongside the good.
7. **Present answers as a starting point, not a verdict.** Mark's ask on the call, and I'd make it a design rule: whoever asks has to understand the answer may not be the full or final response, and that some investigation is still theirs to do. This is separate from citing — a correctly cited answer can still be read as more settled than it is. It shapes how the answer is worded, not just what it links to.

Andrew — your own guardrail on the call already implies most of this: don't ship a phase that returns bad or old information, because it's more damaging than useful. I've taken that as a hard constraint rather than a preference.

## The plan

### Phase 0 — Count what we actually have

Before anything gets built. How much is there, how current is it, how much of it contradicts itself, and how does that break down by source.

This is the cheapest work in the plan and every later decision depends on it. Right now nobody can answer "what fraction of real SE questions have an answer anywhere in our corpus" — and until we can, any build estimate is a guess. It also tells us which subset is good enough to serve, which is what Phase 1 needs.

I'd rather spend two weeks finding out the corpus supports half of what we want than spend two months building for a corpus we assumed.

### Phase 1 — A place to ask, over the good subset only

Scoped by what Phase 0 found, not by what we wish we had. Andrew, you already proposed this scoping on the call: tech scopes and the SA folder first, Slack later.

On the how — you reached for a Claude-native surface twice, once as "something like ask commerce" and again as putting it directly in CLA. That instinct is right, and it's also the cheapest path. You put the floor at two months and attributed all of it to security review and hosting. A configured surface on seats and connectors we already have may avoid most of that.

Two things could break that, and I'd rather name them now:

- **Gong.** It's a named source, we already pull it through Make, and it isn't something the standard connectors reach. If pilot questions genuinely route to call recordings, that's a custom piece of work.
- **"Ask commerce."** I don't know what it is. See the open questions — this is the one that could change the plan most.

### Phase 2 — Fix the capture side

This is where Phase 1's ceiling gets set, and it isn't a software project.

The specific failure to solve is Zac's: documentation stops when the hours stop. Any fix that asks people to write more, on unbilled time, loses to the billing pressure that caused the problem. So the useful question isn't "what should the template be" — a template already exists and isn't followed. It's "what can we derive from work that's already happening."

Worth saying plainly: this is the half of the project that determines whether we're doing this again in eighteen months. It is also the half that might not be in scope — recording knowledge is a write, everything else here is read-only, and that's decision 1 below. I'd rather flag the tension than present this as settled.

### Phase 3 — Help ask the hard questions

Mark put the shape of this well on the call: the tool spits out the twenty questions you have to ask a client, and some of them are the ones we can't do. Andrew's answer was that those are exactly the ones to ask — that's the whole point of scoping — and the tech scope he demonstrated is already doing a version of it.

It's last because it depends on the negative knowledge being both present and current, which is the decay problem above. It's also not greenfield: the tech scope document you shared already does a version of this. I'd treat that as the starting point rather than building alongside it.

## What changes for each of you

Concretely, if this lands. Written as what someone can *do* afterward that they can't now — if any row reads as vague to the person named in it, that row is the problem.

| Who | What you can do that you can't today | Which phase |
| --- | --- | --- |
| **Sales engineers** | Ask what the platform can't do for a given requirement, and get an answer with a link you can open — or a straight "we have no record of this," which is also actionable. Today the honest options are guess or interrupt someone. | Phase 1 |
| **Zac** | Pick up an implementation and see what was recommended in the sales cycle and why — including whether that recommendation predates a platform change that invalidates it. Also: stop being the person who reconstructs it from memory. | Phase 1 |
| **Mark** | Receive a scope that already names the platform's limitations and the agreed workarounds, instead of finding them during implementation. You said you were glad this would help surface the solutions around the tough questions — this is where that lands. | Phase 3 |
| **Andrew, as one of the few people who carry the history** | Redirect a repeat question and trust the answer, without checking it. Both halves matter: fewer interruptions is not a win if you end up correcting what the bot told someone. | Phase 1 |
| **Delivery / IPM** | Have what you built recorded without spending unbilled hours to write it up. This is the one that needs decision 1. | Phase 2 |
| **Andrew, as sponsor** | Approve a defined scope with a stated measurement, instead of an aspiration — see the open items below for what the measurement still needs. | This memo |

The row I'd watch is delivery/IPM. It's the only one that can't be delivered by a read-only system, and it's the one I have the least direct evidence for — nobody in that role was on the call.

## What I need decided

Four things. Three of them are yours, and I can keep working without them — but not indefinitely. Number 3 I'd like an answer to before the first sync, because it could change the plan enough that designing Phase 0 around the wrong assumption wastes the week. The other three can wait until we've met once.

| # | Decision | Why it matters | Owner |
| --- | --- | --- | --- |
| 1 | **Does this write, or only read?** | Phase 2 means recording knowledge going forward. That's a write system. Everything scoped so far is read-only, which is a much smaller security and privacy surface — the one you said accounts for the whole two-month floor. If Phase 2 is in, that floor changes. | Andrew + me |
| 2 | **Who is this for?** | The kickoff went from SE, to SE and SA, to anyone in the company. Those are different products with different answers to "what's authoritative." I'd start narrow and widen on evidence. | Andrew |
| 3 | **What is "ask commerce" / CLA?** | If a sanctioned internal assistant already exists, it's either where this belongs or the most relevant prior work there is — and it may already hold the approvals that make up your two-month estimate. Answering this changes more than any other open question. | Andrew or Levi/Shane |
| 4 | **What's the budget?** | I asked on the call and we ended up on timeline and access instead. Related: Claude credits are already a standing blocker on your Monday checkpoint, and I'm currently running on personal subscriptions. That's fine for a straw man and not fine for a two-month build. | Andrew |

## What this memo doesn't do yet

Named so you can see the holes rather than find them.

**The measurement isn't defined.** I've said Phase 1 should be measured and that the thing to displace is the person-to-person round trip, but I have not specified what gets counted, how, or over what period. I also don't yet have a clean instrument. The obvious candidate was your 1:1 direct-message history with the SAs, but on the call you described that channel as you asking them — "I just bug them that often" — which measures your outbound questions, not inbound demand on you. Both directions are real and both are worth displacing; they just aren't the same number. Naming the instrument is Phase 0 work. The scope in front of you has a measurement *slot*, not a measurement.

**Your second definition of success is missing.** On the call you named two things: the system working, and a written diagnosis of where our documentation practice currently breaks with recommended changes. This memo plans the first and says nothing about the second. It isn't dropped — it's the natural output of Phase 0 and Phase 2, and it may matter more to you than the tool does. It needs a phase and an owner, and it has neither yet.

**Phase 0 has no duration.** I'll bring a concrete proposal — what gets counted, how, how long — to the first sync. Until then "two weeks" in the section above is a comparison, not an estimate.

## Gaps I can't close from here

- **No IPM in the room.** The clearest structural finding — documentation stopping at hours-exhaustion — came from Mark and Zac describing someone else's constraint. Before designing anything for it, I need to hear it from an IPM directly.
- **Nobody owns "what's authoritative."** We can label sources by authority tier, but no one currently decides what's canonical or retires what's stale. That may be a real gap rather than a missing conversation.
- **The corpus is unmeasured.** Phase 0.

## Constraints I'm treating as fixed

- Security and privacy review on anything that touches a data repository. Two months minimum on your estimate, and that's the floor, not the build.
- No new headcount. I'm the developer; Mark and Zac are guides and reviewers.
- No release that returns bad or stale information, per your own guardrail.
- Uniform read access across the SE team — which simplifies a lot, and is why I'm not designing per-user permissions.

## What I'd like from you three

**Mark and Zac** — Andrew put you both on this call as the guides for where the documentation actually lives, across both the SE and SA sides. So: the bullet list from the call, whenever. Where tech scopes live, where you write things up, where you dump the stuff that doesn't have a home. Informal is fine; a Slack message beats a document. Plus GitHub usernames and I'll add you to the working repo.

**Andrew** — decisions 2, 3, and 4 above. Number 3 first if you're picking one; it could reshape the plan.

I'll set up the weekly sync and bring Phase 0 as a concrete proposal — what we'd count, how, and how long. Everything in this memo is meant to be pushed on, particularly the sequencing. If you think Phase 1 should come before Phase 0, that's worth an argument, and I'd rather have it now than in six weeks.

---

<sub>**Traceability** — the "What changes for each of you" table above is this memo's statement of what each persona can do once this lands, written in the reader's language rather than the research vocabulary. Recommendations map to the jobs in `research/personas-and-jtbd.md` as follows: Phase 0 and Phase 1 serve `se/JOB-1` and `sa/JOB-1`. Phase 1's measurement serves `knowledge-holder/JOB-1`. Phase 2 serves `delivery-ipm/JOB-1`, which is the job that forces decision 1 — recording is a write. Phase 3 serves `sponsor/JOB-2`. The memo itself serves `sponsor/JOB-1`. Problem statement and evidence: `research/problem-space/problem-statement.md`.</sub>
