# Personas & Jobs-to-be-Done

**Stage 1 (research variant) — MANDATORY GATE.** No synthesis, decisions, or deliverables proceed until this is populated. `persona-fit-reviewer` blocks any downstream artifact that does not trace to a job below.

**Derived from**: `research/problem-space/problem-statement.md` (canonical problem), grounded in the two input assets catalogued in `research/sources/`. Every persona below names its asset. Roles the inputs imply but do not detail are flagged rather than asserted.

**Provenance anchor** (extracted from the superseded `blueprint.yml:pilot_profile.walkthrough_citation`, which the research-variant re-stamp drops — nothing else resolves it after that point):
- `research/sources/definition-and-grill-2026-07-09.md` — founding definition, three research tracks, two adversarial verifications, 16-question grill ledger
- `research/sources/knowledge-database-kickoff-2026-07-27.md` — sponsor kickoff, load-bearing quotes transcribed with timestamps

Job-id convention: `<slug>/JOB-<n>`.

**This file is the canonical persona model.** It supersedes `research/personas/se-researcher.md` and `research/personas/senior-se.md`, which remain on disk as founding context and carry supersession banners.

Those two files still hold `jtbd:` frontmatter pinning `surface: se-frontdoor-slack-channel`, and `prototype-forge-provenance-reviewer` parses that frontmatter — not this file, and not their banners. So it reports `JTBD_LACKS_SURFACE` against a surface that was assumed rather than decided (BD-3). That block is **expected and correct-to-ignore**: the reviewer is greenfield-only and stops applying at the research-variant re-stamp. The frontmatter is deliberately left intact until then rather than edited, because editing it to satisfy a reviewer that is about to be removed would be changing evidence to quiet a gate.

---

## Personas

### Sales engineer (`se`)

- **Slug:** `se`
- **Source:** grill 2026-07-09 § "The idea" (founding persona); kickoff 00:16:58 (sponsor names SE as a primary user)
- **Who:** Scopes client solutions against platform capability. Mid-ramp to experienced — knows the product, not where every fact lives.
- **Jobs:**
  - **JOB-1:** When scoping a client solution, I need to know what the platform *cannot* do and how prior engagements worked around it, so I can raise the disqualifying questions during discovery rather than after commitment.
    - **Acceptance:** For a sample of real scoping questions, receives either a cited answer or an explicit "no record exists" — never a confident answer without provenance. A wrong answer that looks sourced is worse than no answer, because it is acted on.
    - **Today:** Searches Confluence, searches Drive, scrolls Slack, gives up, pings a senior.
    - **Decision dependency:** BD-2 (audience), BD-3 (surface).
    - **Why this job and not "find documents faster":** the sponsor's evidence is that naming a limitation *wins* engagements — a client selected the platform specifically because the limitation was disclosed with a workaround while competitors concealed theirs (00:24:47). The valuable output is negative knowledge, which per P6 is also the fastest-decaying category. That is why acceptance turns on provenance and staleness, not on retrieval speed.

### Solutions architect (`sa`)

- **Slug:** `sa`
- **Source:** kickoff 00:09:27 (sponsor names the SA document repository as in-scope); 00:22:42 (handover expectations)
- **Who:** Implements what was sold. Owns project folders and the record of what was actually built.
- **Jobs:**
  - **JOB-1:** When picking up an implementation, I need to know what was recommended during the sales cycle and why, so I can tell whether the scoped solution still matches what the platform can currently do.
    - **Acceptance:** Can retrieve the tech scope and its recommendation for a named project, and can see whether that recommendation predates a platform change that invalidates it.
    - **Today:** Reads the project folder when one exists. Projects around 20 hours or less often have none (00:11:54).
    - **Decision dependency:** BD-2 (audience).

### Knowledge holder (`knowledge-holder`)

- **Slug:** `knowledge-holder`
- **Source:** kickoff 00:07:09 (departures: nine-year and seven-year tenures, plus the sponsor's own role change); 00:35:32 ("I'm the only one remaining")
- **Who:** The remaining long-tenured person holding a decade of platform history. **Effectively one person, and the same person as `sponsor`.** The founding research modelled this as "2–3 senior SEs"; the kickoff corrects that.
- **Jobs:**
  - **JOB-1:** When someone asks me a question I have answered before, I need to redirect them to a source that answers it as well as I would, so I stop being the retrieval system.
    - **Acceptance:** Question volume into their direct channel drops against a captured baseline, **and** no redirected question comes back with a wrong cited answer they must correct. Both halves are required — deflection achieved by degrading answers is a regression.
    - **Today:** Answers in a 1:1 direct-message channel. Every SA change is added to that channel; it is the de facto system of record.
    - **Decision dependency:** none. This job is stable across all four boundary decisions.
    - **Measurement note:** because this persona is a single named individual, their channel volume is the most tractable baseline instrument available — which is what makes the otherwise-unmet `deflection-baseline` precondition capturable.

### Delivery / IPM (`delivery-ipm`)

- **Slug:** `delivery-ipm`
- **Source:** kickoff 00:20:18 and 00:11:54 — the role and its constraint are described **by two other practitioners**. No IPM was present.
- **⚠ Verification:** `implied-not-represented`. The inputs name this role and describe its output constraint, but do not detail the role from the inside. This persona's job below is inferred from two second-hand descriptions and **must be confirmed with an actual IPM before anything is built for it.** Per the template's derived-from-inputs rule, this is flagged rather than asserted.
- **Who:** Produces much of the document corpus as a deliverable of billable project work.
- **Jobs:**
  - **JOB-1:** When project hours are exhausted mid-implementation, I need a way to record what was actually built that does not require unbilled hours, so the next person does not inherit a truncated record.
    - **Acceptance:** A completed-state record exists for implementations whose hours ran out — measurable as a ratio against whatever the corpus census establishes as the current baseline.
    - **Today:** Documentation stops when the hours stop. Completed retrospectives are frequently absent (00:20:18).
    - **Decision dependency:** **BD-1, structurally.** This job cannot be served by a read-only system — recording is a write. So BD-1 is not a scope preference: either this persona's job is out of scope for this initiative, or `READ-ONLY v1` gets the dedicated ADR that ADR-0001 requires. There is no third option that keeps both.

### Sponsor (`sponsor`)

- **Slug:** `sponsor`
- **Source:** kickoff throughout (convened the meeting, set success criteria, owns the timeline floor); grill 2026-07-09 ownership row ("SE team ask — leadership would sponsor")
- **Who:** SE/SA leadership. Owns the outcome and the authorization. Also `knowledge-holder`, which concentrates the pain and the authority to fix it in one actor.
- **Jobs:**
  - **JOB-1:** When deciding whether to authorize and fund this, I need to know what it will cost, what it will change, and how we will know it worked, so I can approve a defined scope rather than an aspiration.
    - **Acceptance:** A decision memo they can act on — phased scope, named risks, a measurement definition, and an explicit statement of what is *not* included. Committed 2026-07-27 as "something halfbaked within the week" (00:34:18).
    - **Today:** No current artifact. `docs/se-team-brief.html` was the prior attempt and its framing is superseded; it is demoted to `draft`.
    - **Decision dependency:** BD-4 (funding was raised and never answered), BD-3 (an existing internal platform may absorb most of the stated timeline).
  - **JOB-2:** When I hand a scoped project to delivery, I need the scope to already name the platform's limitations and the agreed workarounds, so implementation does not discover them.
    - **Acceptance:** Sampled tech scopes for merchants where a known limitation applies contain that limitation and a recommendation. Directly stated as the success criterion at 00:21:21 and 00:22:42.
    - **Today:** Inconsistent. The sponsor attributes this to SEs not knowing the question exists rather than to concealment (00:27:46).
    - **Decision dependency:** none for measurement; this is observable today by sampling.

### Maintainer (`maintainer`)

- **Slug:** `maintainer`
- **Source:** **intrinsic — declared in `actor-output.yml`, not input-derived.** Listed for honest provenance: it does not have the same footing as the five personas above, and is retained because the `recovery-brief` output serves it and would otherwise be orphaned.
- **Who:** The operator, and any agent session resuming the initiative.
- **Jobs:**
  - **JOB-1:** When resuming after a gap, I need to reach the current next step without re-deriving the problem and without picking up the superseded framing, so sessions compound instead of restarting.
    - **Acceptance:** A cold session reads `research/problem-space/problem-statement.md` before `blueprint.yml`, reaches the stated next step, and does not act on the `HANDOFF.md` do-not-do list.
    - **Today:** Satisfied by `HANDOFF.md` plus the supersession pointers added 2026-07-27.
    - **Decision dependency:** none.

---

## Named gaps

Per the derived-from-inputs rule — roles the inputs imply but do not detail:

1. **"Anyone within the company"** (kickoff 00:09:27, 00:16:58). The sponsor twice widened the audience beyond SE and SA. The inputs never say who that is, what they would ask, or what a good answer looks like for them. **Not modelled as a persona.** BD-2 must resolve before this becomes one; inventing it now would be exactly the vanity the `persona-fit-reviewer` exists to block.
2. **Delivery / IPM is second-hand**, as flagged in that persona block. Confirm with an actual IPM before building for `delivery-ipm/JOB-1`.
3. **No persona owns corpus curation.** The problem statement establishes that capture quality bounds retrieval quality, but no input names a role responsible for deciding what is authoritative or for retiring stale content. This may be a genuine organizational gap rather than a missing interview.

## Coverage check

- [x] Every persona traces to a named input asset in `research/sources/`, or declares non-input provenance explicitly (`maintainer`).
- [x] Every job has observable acceptance criteria — no "better experience" phrasing.
- [x] Every job notes its decision dependency, or `none`.
- [x] Gaps named explicitly, including one role that is implied-not-represented and one that may not exist.

## The test this artifact exists to pass

Before any decision, memo section, or surface ships, it must answer: **which persona's named job does this serve?** If the answer is "none," it is vanity — cut it or justify it as infrastructure with a one-line reason.

Two consequences already fall out of this artifact:

- `delivery-ipm/JOB-1` cannot be served read-only, which converts BD-1 from a preference into a fork.
- The superseded `research/funnel/pilot-funnel.md` served `se/JOB-1` only under the assumption that a missing answer means a misfiled document. With `delivery-ipm/JOB-1` on the board, that funnel's missing branch is visible as a persona-level gap rather than a modelling oversight.
