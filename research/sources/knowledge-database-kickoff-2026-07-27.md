# Input asset — Knowledge Database Kickoff, 2026-07-27

**Stage 0 (Inputs Intake) provenance record.**

| Field | Value |
| --- | --- |
| Asset | "Knowledge Database Kickoff — 2026_07_27 10_57 PDT — Notes by Gemini" (PDF, 34pp) |
| Type | Meeting recording: machine-generated notes + summary + full transcript |
| Date | 2026-07-27, ~39 min (transcription ends 00:39:13) |
| Attendees | Sponsor (SE/SA leadership, 10+ yrs tenure), two SA-side practitioners, operator |
| Author | Google Gemini (automated); meeting organized by the sponsor |
| Where it lives | `~/Downloads/` at time of review — **not durable** |
| Verification | First-party. Operator attended. Transcript is machine-generated and carries Google's own accuracy disclaimer |

**Durability action required**: the asset currently exists only in a local Downloads folder. Load-bearing quotes are transcribed below so that claims in `research/problem-space/problem-statement.md` remain verifiable from this repo alone, but the source PDF should be moved somewhere durable. Whether the binary belongs in this repo is an operator call — it contains a full named transcript.

---

## Handling caveat — use the transcript, not the notes

The generated notes and the transcript do not tell the same story, and the divergence is material.

The notes' "Decisions / Aligned" section lists three items: project initiation, timeline-from-plan, and a weekly sync. None of them is the data-quality problem, and **no Next Step assigns an owner to it** — despite it being raised twice and being a premise-level objection to the whole project.

The notes also render `Make.com proposed for connecting disparate systems like Google Drive and AI tools` as a settled proposal. In the transcript it is the sponsor describing a tool the team already uses to pull call recordings, while the operator asks what it is (00:12:48–00:13:53). Nothing was selected.

Any downstream artifact derives from the transcript.

---

## Load-bearing quotes, by timestamp

Cited by `research/problem-space/problem-statement.md`. Lightly cleaned of filler; no substantive edits.

**00:07:09 — the knowledge-loss trigger (P1)**
> "what we found is especially on the SE side, most of the people who had been here for years left. So there was Stuart had been here for nine years, I've been here for over 10 years, George seven years. And I'm no longer an [SE]. So I still have the knowledge there, but it meant we've got an SE team which is brilliant and so much talent within the team. However, they don't have the same historical knowledge that you have, Mark, that I've had."

**00:08:23 — prior attempts, and why now**
> "How do we document those challenges, the limitations and our workarounds and how we implemented it so that other people have access to it. We tried many times. It's been a failure, but it's been a failure mainly because of the limits of the technology we've had available to us at that time."

**00:09:27 — the sponsor's opening instinct (BD-3)**
> "Could we have a claude like a sim something similar to ask commerce that we do for everything within commerce. Could we have something that points specifically to the documents where all of our tech scopes are sorted and any kind of repository for where the [SAs] log their documents."

**00:10:31 — the premise objection**
> "your whole premise is based on complete documentation on our end. Or complete documentation in all projects sometimes doesn't exist. That's the problem. A lot of our discussions sometimes with the clients are Q and A and they are one-offs. So they don't come into a more documented process."

**00:11:54 — small projects get no folder (P2)**
> "we try to, it really depends on the project. If it's big enough, we definitely will. If it's complex we definitely will along with the correlated diagrams. But for a lot of our projects, like for those that only have 20 hours, we don't."

**00:16:58 — discovery, not sales enablement (P5, BD-2)**
> "this is more about, less about trying to present the good something to a client and more about discovery, understanding what the platform needs… I want the [SE] to be able to initially go in and the SA for that matter, or anyone within the company to be able to go in and say they want to do this. What are the limitations?"

**00:18:13 — documents that are wrong, not stale (P4)**
> "The biggest problem I kind of foresee is some of the older documents don't relate anymore. Like guest tokenization. We have docs out there that just has workarounds because we never had guest tokenization, right? … old data that might conflict with new features now. That just was never available two years ago. And that's available now. But we've probably never documented a new approach yet because it's brand new."

**00:20:18 — documentation stops when billing stops (P2)**
> "it's all point in time and as well as with something from two years ago might be very out of date based on features today. There's also a problem I ran into where the second they run out of IPM hours, the documentation stops. So there's also things where there's halfway through working through a solution or an implementation and the documentation just stops. So we don't actually have a lot of the completed retrospective or anything like that on a lot of these solutions and buildouts."

**00:21:21 — no enforceable schema (P3)**
> "there's a lot of differences between how each project is documented. There's sort of a standardized template that is supposed to be followed, but every project gets documented a little different, which makes it difficult for like enforcing a universal schema on this data."

**00:21:21 — the sponsor's success definition (second deliverable)**
> "what I would see a success for this project would be… documenting where the current challenges are, issues with how to get this, implementing a process for actually the system working but also highlight and recommending process changes going forward."

**00:24:47 — why negative knowledge wins deals (P5)**
> "guest tokenization was the exact issue. So I raised it with them saying this is how you're going to have to solve it. And they went away, discussed it with all of the other platforms, every other platform hid it from them and then couldn't give them a solution. And he said, 'We're selecting big commerce because you highlighted the thing we couldn't do and told us how to solve it. Nobody else was able to do that.'"

**00:26:50 — partial prior art for Phase 3**
> "if you look in each of these, let's look at kitting and bundling for a second. You highlight them, it highlights the kind of questions you need to ask and all the components… these are all of the hard questions."

**00:30:03 — release guardrail and phase-1 scoping**
> "it would be fine to release this in iterations unless the iteration is going to be more damaging than useful. So if the first phase is just going to give bad information and old information, we don't want to release it. But we could release it in sections where this is going to focus on maybe we're just looking at the tech scopes and the [SA] folder for now. Then we're going to look at Slack."

**00:31:14 — constraints and the timeline floor (BD-4)**
> Operator: "are there any hard constraints that are already known in terms of budget tooling? I'm assuming things have to go through GRC."
> Sponsor: "that probably gives you the timeline. You're not getting this out sooner than 2 months because it takes that long just to go through the security checks and hosting."

*Budget was raised here and answered on the timeline/access axis. No funding line was established.*

**00:32:28 — resourcing**
> "You are the developer… what I'm saying is it won't be extended beyond that."

**00:33:23 — the surface question, restated (BD-3)**
> "Slack would be fine to do it, but maybe if it's directly within CLA, like ask commerce, if we had a 'ask the [SEs] and [SAs]'… there's also an opportunity to highlight what the [SEs] and [SAs] do as well."

**00:35:32 — the operator's channel is the retrieval system today (P8)**
> "Every time an [SA] changes, they just get added to that one-on-one chat. It generally, we used to have a channel where me and all of the other [SEs] chattered together. I'm the only one remaining."

**00:37:28 — tooling cost currently personal (BD-4)**
> Sponsor: "we have a blocker section every week and the blocker I have is claude credits."
> Operator: "I'm now personally using Claude and Codex Max subscriptions."

---

## Commitments recorded in the meeting

| Owner | Commitment |
| --- | --- |
| Operator | Straw man project plan — guiding principles, objectives, open questions, gaps, constraints. "Something halfbaked within the week" (00:34:18) |
| Operator | Stand up a weekly sync; sponsor optional after the first |
| SA practitioners | Informal list of where tech scopes, project docs, and relevant Slack conversations live |
| SA practitioners | GitHub usernames for repo access (00:36:29) |

No timeline was agreed. The two-month figure is the sponsor's estimate of security review plus hosting overhead, not a build estimate.

## Named data sources mentioned

Tech scopes folder · SA project folders · Gong call recordings · IPM notes · Slack channels · the sponsor's decade of 1:1 direct messages with SAs (not a channel) · an existing internal assistant referred to as "ask commerce" / CLA (unverified, see BD-3).

Note for the configure-first assessment: Gong is named as a source and is already pulled via Make.com. It is not a standard Claude Enterprise connector, which is trigger 3 in `decisions/0001-configure-first-pilot-as-prototype.md`.
