# Sibling-Project Scan — Stage 1 audit

**Primitive**: Slack-surfaced agentic document Q&A — an agent answering natural-language questions via federated retrieval across live doc sources (Atlassian, Drive, Slack, web) with cited, read-only answers

**Scan date**: 2026-07-09

**Result**: 3 sibling projects identified (each ships one component of the primitive; none ships the whole; the Slack surface has no workspace precedent — absence explicitly declared in the scan section)

## Siblings found

| Project | Location | Primitive shipped | ADR/Audit | Evidence of read | Adopted | Diverged |
|---|---|---|---|---|---|---|
| ask-bc | `~/Workspace/dev/wip/ask-bc` | Agentic assistant runtime (Claude tool loop, 22 sandboxed read tools, 7 gated write tools, DO-per-store) | `wip/ask-bc/docs/architecture/decisions/001-codemode-agent-runtime.md` | Full summary in scan section: stepCountIs(10) tool-loop wall on compound queries; Codemode fix (model writes TS, sandbox executes, no inter-call LLM round-trips); Haiku-default/Sonnet-continuation via beforeTurn; credential isolation via codemode.* RPC + globalOutbound:null; 3 alternatives rejected (Vercel Sandbox cold starts, full CF migration rework, plan-executor meta-tool) | Read/write structural separation (strengthened to read-only-only); compound-query latency as a named profiling target | Runtime/DO/credential machinery not adopted — primary path is zero-code (Claude Tag hosts the loop); uniform ACLs remove per-tenant isolation need. doc-search.ts and audited auth posture explicitly rejected |
| knowledge-index | `~/Workspace/dev/archive/knowledge-index` | Vector retrieval (sqlite-vec + pluggable embeddings) exposed as an MCP search server | `archive/knowledge-index/src/mcp-server.ts` (no ADR exists; source is the record) | Scan section summarizes the chunk→embed→sqlite-vec pipeline, the provider abstraction, and the missing Anthropic/Voyage provider | Named as the crawl+index contingency (ADR-0001 trigger 3) | Not used in v1 — federated search chosen over indexing (uniform ACLs + live sources; retrieval-consensus evidence in competitive leg) |
| hackathon-hive mcp-server | `~/Workspace/dev/ref/hackathon-hive/mcp-server` | Classic MCP server with auth (Streamable HTTP, Supabase RLS, modular tool registration) | `ref/hackathon-hive/mcp-server/src/server.ts` (no ADR exists; source is the record) | Scan section summarizes the modular schema+handler-per-file registration pattern | Template if we ever author our own MCP wrapper | Not needed in v1 — build branch consumes existing official remote MCP servers |

## Findings

1. No blocking findings. Scan section present (`research/current-state/workspace-prior-art.md § Sibling-Project Scan`), primitive named specifically, all three artifact paths verified to exist on disk 2026-07-09, each sibling carries a decision-level read summary, and every divergence states its constraint difference ("because our primary path is zero-code", "because uniform ACLs + live sources favor federation", "because official remote MCP servers already exist").
2. Note (non-blocking): knowledge-index and hackathon-hive have no ADRs; their source files are cited as the audit artifacts, consistent with the gate's "ADR or audit document" requirement.

## Verdict

STATUS: PASS
RUN_BY: research-sibling-scanner
DATE: 2026-07-09
