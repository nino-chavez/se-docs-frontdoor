# Definition + grill session — 2026-07-09

First-party source artifact for `blueprint.yml:pilot_profile.walkthrough_citation`. Captures the founding session: three parallel research tracks, two adversarial verifications, one 16-question grill. Everything below was derived in-session against primary sources; URLs cite the canonical doc for each load-bearing claim.

## The idea (operator's words, condensed)

commerce.com sales engineers rely on isolated, distributed documents for client-solution research. Build a front door — a Slack channel or bot with Claude as the agent — to query across all available docs.

## Research track 1 — vendor canonical (Anthropic)

- **Claude Tag** (successor to Claude in Slack; forced migration 2026-08-03) is this product off-the-shelf: `@Claude` in channels, access to enabled connectors, per-channel scoped identities, org + per-channel spend limits, audit log. Beta, Team/Enterprise only. https://www.anthropic.com/news/introducing-claude-tag
- Custom-build canonical: Slack Bolt app → Messages API tool use → retrieval tools returning `search_result` content blocks → **Citations API works for free** (ZDR-eligible; incompatible with structured outputs). https://platform.claude.com/docs/en/build-with-claude/search-results
- MCP connector (beta `mcp-client-2025-11-20`): URL-transport remote MCP servers in the API. Official remote servers exist for **Atlassian, Notion, Linear, Slack**. **None for Google Drive / SharePoint / Salesforce** — those need custom tools on native APIs. https://platform.claude.com/docs/en/agents-and-tools/mcp-connector
- Threshold rule: corpus < ~200K tokens (≈500 pages) → prompt-stuff with caching, skip retrieval entirely. https://www.anthropic.com/engineering/contextual-retrieval
- Agent SDK is a coding/filesystem harness — mismatched for doc-QA. Managed Agents (`managed-agents-2026-04-01`) = hosted loop + OAuth vaults if we don't want to run refresh ourselves.

## Research track 2 — market scan

- Buy shelf: Slack native Slackbot/Agentforce (2026-03 overhaul; Salesforce-model, ACLs undocumented), Glean (best 3rd-party surface, ~$60k/yr floor), Onyx (open-source, $0–20/seat, ACL-sync connectors, runs Claude), Dust ($30–150/seat, Claude-native).
- Retrieval consensus 2025-26: **agentic/federated search inheriting caller OAuth beats indexed RAG on permissions** — ACL-sync drift leak is OWASP LLM Top 10 **#2** with real incidents (EchoLeak, vector-DB bypass). Index only weak-search sources. https://www.osohq.com/post/right-approach-to-authorization-in-rag
- Adoption data **[UNSOURCED — flagged by reference grading 2026-07-27]**: median enterprise doc-bot < 15% weekly-active by month 6; citations are the #1 adoption driver; feedback capture + HITL on low-confidence answers are standard mitigations. This is the only bullet in this section without a URL, and this document's own line 3 attests that URLs cite the canonical doc for each load-bearing claim. Do not cite these figures. `research/problem-space/problem-statement.md` no longer rests on them.
- Slack UX canon: `agent_view` container, `assistant.threads.setStatus`, streaming via `chat.startStream`, `feedback_buttons`, deep-linked citations, explicit human-escalation path. https://docs.slack.dev/ai/ai-apps-best-practices

## Research track 3 — internal prior art (~/Workspace/dev)

- **No Slack code anywhere** — that surface is greenfield.
- `wip/ask-bc/workers/agent-runtime/src/index.ts` — strong agent-runtime reference (tool loop, model routing, per-tenant creds, write-confirm gate). Its "doc search" is a hardcoded ~50-entry keyword array — **not** a retrieval precedent. Auth posture failed a prior security audit — reuse the shape, not the posture.
- `archive/knowledge-index` — the vector-RAG reference (sqlite-vec + MCP search tool, pluggable embeddings; no Anthropic provider yet). The contingent indexing seam. **[ARTIFACT GONE — verified 2026-07-27]** path no longer exists as of 2026-07-27; the record of the 2026-07-09 read stands but is no longer checkable. See `research/current-state/workspace-prior-art.md` § Sibling 2.
- `ref/hackathon-hive/mcp-server` — MCP-with-auth template.

## Organizational facts (via Alex Vela's GEM enablement-triage POC doc)

- commerce (=BigCommerce) runs **Claude in Slack on Enterprise seats** with the **Atlassian/Jira MCP connector live** and performing writes (EDU project). Admin rails for a Tag pilot already exist.
- His system is write-heavy triage (form → rubric → Jira mutations) — opposite problem class; his Make.com polling bridge exists only because Claude in Slack has no event trigger, which is irrelevant here (SE questions are user-initiated).
- Flag passed to him: the 2026-08-03 Tag migration lands at his go-live and may break his @-mention trigger/identity model.

## Verifications (adversarial, against official docs)

1. **NotebookLM is not a queryable source.** No consumer API; Enterprise API (Pre-GA) is CRUD-only — Google's own docs state no programmatic querying. Notebook sources are internal **copies**, not in Drive; only Drive-imported originals stay independently searchable. Fix is a norm, not code: originals live in Drive, notebooks import from Drive. https://docs.cloud.google.com/gemini/enterprise/docs/choose-product · https://support.google.com/notebooklm/answer/16215270
2. **Claude Drive connector Shared-Drive blind spot.** anthropics/claude-code#53442 (OPEN, 2026-04-26): Cowork/MCP Drive connector omits `supportsAllDrives`/`corpora=allDrives` → My Drive works, Shared Drives return empty. claude.ai Enterprise connector behavior **undocumented** → pilot test #2. Custom Drive tool fixes it with three query params. Connector is also text-only extraction (no embedded images/comments).

## Grill ledger (16 questions, 2026-07-09 — operator answers, all locked)

| Decision | Answer | Consequence |
|---|---|---|
| ACL posture | **Uniform — every SE sees every doc in scope** | Per-user OAuth dead; shared-credential safe; acting-identity test demoted to formality; buy lane fully dead |
| Seat coverage | **All SEs have Claude Enterprise seats** | Tag reaches everyone; Claude Projects available to all as interim |
| Ownership | **SE team ask** — leadership would sponsor; long-term owner TBD | Design for handoff; portal audience = SE leadership |
| Corpus size | **Genuinely unknown** | Pilot includes corpus census; 200K prompt-stuff escape hatch stays live |
| Answer shape | **Lookup first, synthesis v2** | v1 = search-and-cite; retrieval must return reusable source blocks |
| V1 corpus | **Wide, with authority-tier labels** (official > team > thread) | Prompt-instructable in Tag; deterministic only in custom bot — pilot tests if prompt-level suffices |
| Conflicts | **Surface both + flag, never silently pick** | Conflict flags double as doc-hygiene signal |
| Slack as source | **Both files and threads; threads matter** | Scope Slack search to named SE channels, not workspace-wide |
| Write-back | **READ-ONLY v1, hard line** | Design commitment; differentiates from Alex's write-heavy lane |
| Latency | **Async-first; both eventually** | No two-speed architecture in v1 |
| Pass metric | **Senior-SE deflection** | Baseline 2-3 seniors' ping volume pre-launch; their "ask the bot first" redirect is the adoption engine |
| Senior buy-in | **They'd champion it** | Recruit before go-live — go/no-go condition for the metric |
| Filing (local files / NotebookLM uploads) | **Demand-driven — let it surface** | No pre-migration; when the bot misses a trapped file, that file gets filed |
| Version drift (public dev docs) | **Real — pin to current-stable**, label version-specific answers | Instruction-set rule |
| Internal doc sites | **Mix** — Confluence part covered; CMS part traffic-gated | Crawl only if pilot questions actually route there |
| Sanction level | (subsumed by ownership) SE team ask | Admin sponsor needed for connector toggles + pilot channel |

## Verdict

Configure-first is overwhelming. Stage 2 = **Claude Tag pilot** in one SE channel. Pilot tests: (1) Shared-Drive visibility through the Enterprise connector, (2) prompt-level authority-tier labeling + conflict-surfacing adequacy, (3) citation quality on a week of real SE questions, (4) acting identity (formality, given uniform ACLs), plus a corpus census. The thin-build (Bolt + Messages API + federated tools + `search_result` citations) is the contingent branch behind named failure triggers — see ADR-0001.
