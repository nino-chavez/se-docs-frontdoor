# Knowledge access for Solution Engineering

**For** leadership · **From** Nino Chavez · **30 July 2026**
**Status** In progress. No funding requested, no software purchase proposed.

---

## The situation

A decade of platform knowledge sits with a small number of senior people. When they are busy, deals slow down. When they leave, it leaves with them.

The documents that should hold that knowledge are a byproduct of billable delivery, so they stop where the billing stopped. We measured it rather than assumed it. Across the five internal spaces holding solution knowledge there are **3,173 pages, and roughly a quarter have been touched in the last twelve months.** Well over half have not been touched in two years.

The cost shows up as the same question asked twice — an engineer asks a colleague because the answer was never written down anywhere they would find it.

## What we found

We set out to build a search tool. We stopped, because Commerce already has one.

**Ask Commerce, run by our AI Operations team, is live for every employee and already does almost everything this project had specified.** Building our own would produce a later, smaller version of something we already own. That recommendation is not final — we are validating it over the next fortnight — but it is where the evidence points, and it removes the largest line item anyone expected to see here.

Two gaps remain, and both are about the documents rather than the tool.

| Gap | What it actually is |
| --- | --- |
| Our largest body of solution knowledge sits in Google Drive, which the tool cannot read | A setup that was never finished, not a product limit. Someone has to switch it on |
| No source is designated authoritative for solution knowledge | A policy request to the same team |

Neither is a build. Both are requests to a team that already exists.

## The part nobody has solved

Knowing when a document became **wrong** rather than merely old.

A document describing a workaround for something the platform could not do three years ago looks identical to a good one. Same author, same format, recent enough date. It is confidently incorrect, and anyone who follows it takes bad guidance into a client conversation.

We surveyed the market for this. Tools that draft documents, assign owners and expire them on a schedule are widely available. **Nothing we found detects that a document became wrong because the product shipped the capability it was working around.** That is the only part of this worth building, and we are not asking to build it yet.

## What this costs and what happens next

Two weeks of measurement, roughly **four hours of senior engineering time**, and two requests to a team that already exists. Nothing else.

That measurement answers the one question that decides whether there is a project here at all: how much of our documentation is actively wrong. If the answer is *not much*, better search over a mostly-accurate library was enough, and this finishes with two requests and no build. That is a real possibility and we would rather find it in two weeks than two quarters.

## What we are not doing

- **Not buying anything.** A Google alternative exists and is genuinely strong. It would mean a second subscription alongside our existing Claude spend, and two systems that answer the same question differently.
- **Not redesigning how the company stores documents.** We will identify where knowledge lives today and what limits it, and bring that to the leaders who own those processes. The decision is theirs.
- **Not opening it broadly yet.** Phase 1 is Solution Engineers, Solution Architects and Technical Account Managers. Some answers will be wrong, and the people using it need the background to catch that before it reaches a client.

## What we need from you

Nothing today.

One thing to be aware of: this work will turn up findings about how our teams record knowledge, and some of those will point at processes this group does not own. We will bring them to the right leaders rather than act unilaterally. If documentation practice needs to change, that is a decision for the people who own it.

---

<sub>Full analysis, methods and evidence grading: `docs/solution-plan.md`. Page counts are measured against recorded, re-runnable queries. The Drive figure is a lower bound, not an audit.</sub>
