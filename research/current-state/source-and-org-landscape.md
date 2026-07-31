# Current state — source landscape and org facts

Stage 1 current-state leg. Facts verified 2026-07-09; sources in `research/sources/definition-and-grill-2026-07-09.md`.

## The doc sources SEs actually use (operator inventory)

| Source | Search API reality | Coverage path | Status |
|---|---|---|---|
| Jira / Confluence | Real (Atlassian remote MCP, official) | Connector already live in our org | Ready |
| Google Drive | Real (Drive API) | Anthropic Drive connector (admin toggle) | Pending Shared-Drive test |
| Lucidchart | Real (Lucid MCP server, provider-hosted) | Official Claude connector exists, OAuth + DCR, inherits Lucid permissions | **Added 2026-07-31** (`S-6a`). Named by Mark as one of three major sources. **Two open questions**: whether an MCP connector can attach to a Claude *enterprise-search* project at all, and whether adding it triggers the `G2` AppSec review — it is an MCP, so on the face of it, yes |
| ~~Figma~~ | — | — | **Withdrawn 2026-07-31.** Was my speculation in the sync ("maybe Figma. I don't know what else", 00:04:31), not a report. Mark's answer names Lucid instead. Do not carry Figma as a source until someone names it independently |
| Slack channels | Real (Slack search) | Slack connector, scoped to named SE channels | Ready |
| Public dev docs | It's the public web | Web search, version-pinned by instruction | Ready |
| Internal doc sites | Mixed — part Confluence-backed, part CMS | Confluence part covered; CMS part traffic-gated | Partial |
| NotebookLM | None (verified — no query API, sources are internal copies) | Norm: originals live in Drive | Not a source |
| One-off local files | None | Demand-driven filing into Drive/Confluence | Norm |

## Org facts (the rails that already exist)

- Claude in Slack runs on **Claude Enterprise seats, org-wide**; every SE is seated.
- The **Atlassian/Jira MCP connector is live and performing writes** today (an adjacent internal POC creates and transitions Jira tickets from Slack).
- Claude Tag (successor product) force-migrates the legacy Slack app on **2026-08-03**; a pilot lands on the successor, not the deprecated surface.
- Access posture is **uniform**: every SE can open every doc in scope (grill, 2026-07-09). No per-client/region restrictions bind v1.

## Known constraints and open items

- **Shared-Drive visibility**: anthropics/claude-code#53442 (OPEN) shows a Claude Drive connector variant that silently sees only My Drive. Enterprise-connector behavior undocumented. Pilot test #1.
- **Corpus size unknown**: nobody has counted. If the load-bearing core is under ~200K tokens (~500 pages), Anthropic's published guidance is prompt-loading with caching over any retrieval build — the pilot includes a corpus census to settle this.
- **Drive connector extracts text only** — embedded images and comments in docs do not come through.
- The incumbent "system" is the shoulder-tap to 2–3 senior SEs; their ping volume is the baseline metric and must be captured before go-live.
