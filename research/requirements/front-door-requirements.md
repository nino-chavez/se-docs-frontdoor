# Front-door requirements — the acceptance criteria for the platform test

**Doc type**: Reference (Diátaxis) — Look things up. Owns `REQ-1`–`REQ-12`: what the chosen front door has to do, what it must not have to do, and what is deferred.
**Date**: 2026-07-30
**Status**: canonical for requirements. Supersedes nothing; this is the first requirements artifact in the initiative.
**Derived from**: the 2026-07-30 sync transcript (`research/sources/se-docs-frontdoor-sync-2026-07-30.md`), Andrew's written feedback on plan revision 1, and the guiding principles in `docs/decision-memo.md`.

> **Why this exists, stated plainly because it is a gap I created.** The 30 July sync produced decisions and action items, and I recorded both. It also produced **requirements**, and I did not — they were folded into narrative or dropped. The consequence is concrete: `S-7` item 2 commits Alex Vela and me to "test what Claude and Google Enterprise can actually do," and until this document existed **that test had no acceptance criteria.** We would have gone in and evaluated against recollection. `REQ-4` in particular — the one Mark asked for twice and clarified once — was in none of my notes.

---

## How to read the grades

| Grade | Meaning |
| --- | --- |
| **Must** | The front door is disqualified without it |
| **Should** | Wanted; absence is a cost to weigh, not a disqualifier |
| **Deferred** | Named by the room, explicitly pushed to a later phase |
| **Not** | Explicitly ruled out. Recorded so it does not get re-litigated or quietly re-added |

---

## Functional

### `REQ-1` — Produce answers, not file lists · **Must**

An agent reasons over the corpus and returns an answer with citations. Not a search that hands back documents.

*Source*: 00:20:08–00:23:10. Nino asked directly; Andrew — "How would you do that without an agent? Even the most basic, you'd need that" — and closed on "just working how ask commerce works, I think is sufficient."

> **The meeting's own Gemini notes record this backwards** in their Decisions block. See `S-1`. This requirement is the corrected version.

### `REQ-2` — Cite sources with dates on every claim · **Must**

Carried from the guiding principles and confirmed by the choice of Ask Commerce as the reference implementation. An answer a reader cannot verify is worse than no answer, because §`REQ-3` assumes the reader checks.

### `REQ-3` — Respect each user's existing source permissions · **Must**

Surface nothing the asker could not already open directly. Ask Commerce does this today; Gemini Enterprise does it via identity sync on a 30-minute-to-7-day schedule (`buy-landscape.md`), which is a real difference between the two and belongs in the test.

### `REQ-4` — Attach a caution wrapper to answers · **Should**

The front door should be able to mark an answer as technical, carrying a caveat that the reader may lack the context to act on it safely.

*Source*: Mark, 00:12:24, and he corrected the framing himself when it was misread as an access-control ask — "it's not access I'm looking for. It's more warnings or notifications or something to make sure that hey, be careful with this." Andrew: "it might be the wrapping around the information."

**This is the requirement most likely to discriminate between candidate platforms**, because it is a presentation-layer capability rather than a retrieval one, and it is the one I failed to record. It is graded `Should` rather than `Must` because `REQ-9` offers a non-technical route to the same outcome.

### `REQ-5` — Connect to the sources people actually use · **Must**

Confirmed in-session: Slack, Jira, Confluence, Google Drive. **Figma** was named and is unassessed (`S-6`). Mark and Zac own the definitive list.

**Google Drive shared drives are the load-bearing case.** The tech scopes and SA project folders live there, and that is `AC-1`, the largest single gap.

### `REQ-6` — Scope access by group · **Must**

Phase 1 is **SE, SA and TAM**. TPM deferred on Mark's caution. The platform has to support restricting the audience to named groups.

*Source*: `S-3`. Note the boundary's actual rationale, which is sharper than "technical content": Andrew — "I don't want the salesperson just giving out answers to the customers without speaking to us first." **The risk is forwarding an unreviewed answer to a client**, not comprehension in the abstract.

---

## Constraints on how we get there

### `REQ-7` — Prefer configuration over anything bespoke · **Must**

*Source*: Nino, 00:13:40 — "I want to make sure that we're tempering this against what do we have available versus building something bespoke, because I don't think we are all signing up for building something bespoke here." Unchallenged in the room.

Consistent with `ADR-0001` and with the plan's §5. Any requirement that can only be met by building is a candidate for deferral rather than a reason to build.

### `REQ-8` — Optimise for serving SE/SA fast, and accept that broadening may mean a rebuild · **Must**

*Source*: Andrew, 00:16:59 — "if this can be done in 10% of the time and just support the SEs and SAs then that should be the goal." He went further and pre-authorised the trade: "if we need to go bespoke to support everybody else, let's do it."

**This is not in tension with Andrew's written requirement that the design survive source systems moving, and the distinction matters.** Sources relocating must not force a rebuild — that is `REQ-11`. The *audience* expanding is allowed to force one. Do not over-engineer Phase 1 for readers it is not for.

### `REQ-9` — Some requirements are allowed to be met by training, not by the product · **Should**

*Source*: Nino, 00:14:38 — "lots of things don't have to be solved with technology or by the product. It can be training and messaging."

This is the release valve on `REQ-4`. If no candidate platform can wrap a caution around an answer, the requirement is satisfiable by how the tool is introduced and to whom, and it should not by itself justify a build.

### `REQ-10` — Refer to this as serving SE **and** SA, in every artifact and invitation · **Must**

*Source*: Andrew, 00:10:13. He flagged it himself as "one very finicky thing" and asked for it anyway: "can we not stipulate it's both, because I want to make sure when people are seeing this, it's driven towards supporting both goals... so SAs can get documentation, not just how my team can get documentation."

Recorded as a requirement rather than a courtesy because it governs meeting titles, document headers and channel names, and because that class of thing is exactly what gets dropped and then noticed. The initiative name and the plan's own title currently say "SE/SA" — compliant. Watch invitations.

### `REQ-11` — Survive the sources moving · **Must**

From Andrew's written feedback, carried into plan §4. If the process owners relocate documents — which is the point of reporting findings to them — a solution needing a rebuild was the wrong solution. Configuration over code; named sources over hardcoded ones.

---

## Ruled out and deferred

### `REQ-12` — **Not**: per-document classification with an access-control layer

Explicitly rejected in-session. Nino, 00:12:24 — "if we need to do something beyond that where we have to have some sort of access control list, that blows this up tremendously, because now we need to mark the source of the data as to who has access to it and why... which I don't think we want to do any of that for this." Mark agreed and clarified that this was never his ask.

**Recorded because it is the natural next thought after `REQ-4`, and it is a scope explosion.** Anyone proposing it later should have to argue past this entry rather than discover the objection fresh.

### Deferred to a later phase, by name

| Item | Who | Note |
| --- | --- | --- |
| Access beyond SE/SA/TAM | Andrew, 00:15:46 | He asked specifically that the plan carry **a written note to revisit this**, with caution about which data a wider audience should see. Not a vague "later" — a requested placeholder |
| TPM access | Mark, 00:20:08 | 50/50, on the nuance in the results |
| Reader-adaptive answers | Nino, 00:16:59 | Identify reader type and data type, then adapt the answer to the reader. Andrew's call was to explore rather than decide now |
| Public-facing developer documentation | Andrew, 00:26:25 | Explicitly out of scope for this project. Chris owns adjacent work (`S-9`) |

---

## What to do with this

**It is the checklist for `S-7` item 2.** The joint test with Alex Vela evaluates candidates against `REQ-1`–`REQ-6` and `REQ-11`, and records a verdict per row rather than a general impression. `REQ-4` and the shared-drive half of `REQ-5` are the two most likely to separate the candidates.

**It is not complete.** Mark and Zac's source list will sharpen `REQ-5`. Nothing here has been tested against a running system — every claim about what Ask Commerce or Gemini Enterprise does is read from documentation, which is the same weakness plan §1 already names as its gating condition.
