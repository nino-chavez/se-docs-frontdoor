# Pilot funnel — how a question becomes a deflected ping

> **⚠ SUPERSEDED 2026-07-27 — this funnel has a missing branch, not just dated framing.**
> See `research/problem-space/problem-statement.md`.
>
> Step 5 enumerates two miss classes: content *trapped* (exists, wrong place → demand-driven
> filing fires) and bot *inadequate* (falls back to a senior). The 2026-07-27 sponsor kickoff
> established a third, which this funnel cannot represent: **content was never written.**
> Documentation stops when project hours run out, smaller engagements often get no folder, and some
> documents are actively wrong where the platform shipped past a documented workaround.
>
> That is not a rarer branch — it may be the dominant one. Demand-driven filing does nothing
> for it, because there is no artifact to re-home. Any planning that routes content misses
> through step 5 as written will under-count the failure mode that matters most.
>
> Do not extend this funnel. Re-derive it from the problem statement's domain dependency
> (capture → source quality → question surface), which puts the missing branch upstream of
> the funnel entirely.

The v1 funnel has one surface for both personas:

surface: se-frontdoor-slack-channel

## The path

1. **Question arises** — an se-researcher hits a client-solution unknown during async research (not mid-call; latency budget is minutes, per the grill).
2. **Entry** — they ask in the pilot channel (`se-frontdoor-slack-channel`). Historically this step was a DM ping to a senior-se; the funnel exists to bend that edge.
3. **Answer** — Claude Tag responds in-thread with a cited answer: authority-tier label (official doc / team doc / Slack thread), deep link per claim, conflict flag when sources disagree, current-stable version pinning on public-doc answers.
4. **Verify** — the se-researcher opens the citation. Uniform access guarantees the link resolves for them. This step is where trust compounds or dies.
5. **Resolve or escalate** —
   - **Hit**: question answered; no senior ping occurs. This is the deflection event the metric counts.
   - **Miss (content trapped)**: the answer's source doesn't exist in any federated source (a local file, a NotebookLM upload). Demand-driven filing fires: that file gets re-homed to Drive/Confluence, and the question is re-asked.
   - **Miss (bot inadequate)**: the se-researcher falls back to pinging a senior-se — who redirects future repeats to the channel ("ask the bot first"), closing the loop.
6. **Measure** — weekly: senior-se ping volume vs pre-pilot baseline (primary), weekly-active se-researcher count (backup), plus the per-question feedback captured in-thread.

## Funnel-level failure watch

The drop-off to watch is step 3→4: answers that arrive uncited or slower than a shoulder-tap send the se-researcher back to the old path permanently — median enterprise doc-bots fall under 15% weekly-active by month six, and citation quality is the strongest retention lever in the market scan. The pilot's three tests (Shared-Drive visibility, label adequacy, citation quality) all target this edge.
