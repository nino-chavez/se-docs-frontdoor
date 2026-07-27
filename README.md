<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="se-docs-frontdoor — seven scattered doc sources gather into one Slack channel running Claude Tag in read-only mode, which answers with source citations, authority labels, and a conflict flag. Success is measured as senior-SE ping deflection.">
</p>

## What this is

Sales engineers at commerce.com assemble client solutions out of documents scattered across Jira, Confluence, Google Drive, Slack threads, NotebookLM, local files, and internal doc sites. Most of the research time goes into finding and cross-referencing, not reasoning. When that fails, the fallback is pinging one of the two or three senior SEs who hold the tribal knowledge.

This repository plans one fix: a single Slack channel that answers those questions, cites its sources, and labels how authoritative each source is.

**The deliverable is a configured Slack channel, not shipped software.** Claude Tag — Anthropic's Claude-in-Slack app — already runs on commerce's existing Claude Enterprise seats. The work here is the pilot design and the decision record behind it. Nothing under `apps/` is the product.

Private, internal planning repo. It runs on [Blueprint](https://github.com/nino-chavez/blueprint), a delivery methodology that stages work as research → design → prototype → validate → ship.

## Where it stands

Stage 1 (research) closed on 2026-07-09. Stage 2 (design principles, then the pilot protocol) is next.

The state is checkable rather than asserted. `actor-output.yml` declares every actor, the outcome they need, and the output that serves it; a gate grades whether those outputs actually exist:

```console
$ npm run manifest:gate
actor-output.yml: PENDING (route actor-output; 0 errors, 3 pending, 0 warns)
```

| Output | What it is | State |
| --- | --- | --- |
| `docs/se-team-brief.html` | Decision brief for the SE leadership sponsor | ready |
| `HANDOFF.md` | Session recovery — where work stopped, what's next | ready |
| `decisions/0001-…` | The configure-first decision record | accepted |
| Slack front door | The configured channel itself | planned |
| Pilot protocol | Three tests plus a corpus census | planned |
| Measurement plan | Deflection baseline and weekly-active backup signal | planned |

One precondition is unmet **on purpose**. The gate refuses to let the channel go live until `research/pilot/baseline-pings.md` exists, because the pilot's success signal — fewer "quick question" pings to senior SEs — becomes permanently unmeasurable if launch happens before the baseline is captured.

## Why configure instead of build

Blueprint's Stage 2 normally produces a working prototype. This initiative deliberately does not, and [ADR-0001](decisions/0001-configure-first-pilot-as-prototype.md) records why.

The riskiest assumptions here are not answerable in code. Can the Enterprise connector actually see Shared Drives? Are prompt-level authority labels good enough, or do they lose too much? Is citation quality acceptable against the real corpus? Every one of those is only testable by configuring Claude Tag against live sources. A built prototype would have tested the fallback while leaving the primary path unexamined.

Buying was retired outright. Uniform ACLs removed the one requirement a purchased tool uniquely served, and existing Claude Enterprise spend removes the seat-economics argument.

### What would restart a build

A thin custom app — Slack Bolt, the Messages API, federated retrieval tools returning `search_result` blocks — is contingent on the pilot failing in one of four named ways:

1. **Shared-Drive blindness** — the connector cannot see Shared Drives.
2. **Tier-label inadequacy** — prompt-level authority labels and conflict-surfacing prove too lossy.
3. **Scoping gaps** — Tag cannot restrict search to named SE channels, or cannot cover the CMS-backed internal doc sites.
4. **Telemetry ceiling** — deflection measurement needs per-question logging Tag does not expose, and manual survey plus senior self-report prove insufficient.

### Commitments that bind either branch

- **Read-only v1 is a hard line.** No writes of any kind. Revisiting is a v2 decision with its own ADR.
- Wide corpus with authority-tier labels. Conflicts get surfaced and flagged, never silently resolved.
- Citations on every answer, deep-linked where the source allows.
- Async-first. No call-time fast lane in v1.
- Demand-driven filing: when the bot misses on trapped content, that content moves into Drive or Confluence. No pre-migration sweep.
- Answer from current-stable docs; label version-specific content.

## Working in this repo

The first useful action is grading the manifest, not installing anything.

```bash
npm install

npm run manifest:gate   # readiness — does a real output serve every outcome? (expect PENDING)
npm run manifest:check  # lint the manifest without grading readiness
npm run reader:check    # audit rendered surfaces against reader-contract.json
npm run dev             # serve the Blueprint portal locally
```

The Blueprint reviewer runner is not stamped into initiatives. Run it from the methodology source:

```bash
node ~/Workspace/dev/tools/blueprint/template/tools/run-reviewers.mjs
```

Two gotchas worth knowing before you edit: persona job-to-be-done entries must stay in list shape (`jtbd:` followed by `- surface: …`), because the forge-provenance reviewer parses only that shape; and `portal-chrome-canonical` reports `TEMPLATE_MISSING` against the methodology repo itself, which is an upstream issue rather than a defect here.

## Repo map

| Path | What's there |
| --- | --- |
| `decisions/` | Decision records. ADR-0001 is the configure-first call. |
| `research/` | Stage 1 corpus — personas, buy landscape, current-state source map, and the founding session's 16-question grill ledger. |
| `docs/` | `se-team-brief.html`, the brief for SE leadership. |
| `actor-output.yml` | The live contract: actors, outcomes, outputs, preconditions. |
| `HANDOFF.md` | Session state and next steps. |
| `apps/portal/` | Blueprint's stamped Astro portal, at Tier 0 — no data sources wired, so it renders the decisions catalog and little else. Methodology chrome, not the product. |
| `packages/`, `tools/` | Portal UI and design tokens; the reader-contract audit script. |

## Not in v1

Named out of scope so they do not creep back in:

- **Synthesis deliverables** — solution overviews, RFP drafting. Lookup first; synthesis is v2.
- **Write-back of any kind** — including gap-filing tickets and KB writes.
- **A call-time fast lane** — prompt-cached core for mid-call latency. v1 is async-first.
- **Non-SE audiences** — support, CS, partners. Expansion waits until SE deflection actually moves.

## Before go-live

Two human dependencies, both outside this repo: a Claude Enterprise admin to grant connector toggles and create the pilot channel, and two or three senior SEs recruited as deflection champions who redirect quick questions with "ask the bot first."
