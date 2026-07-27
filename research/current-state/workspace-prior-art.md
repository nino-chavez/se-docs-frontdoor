# Workspace prior art — what already exists and what we take from it

## Sibling-Project Scan

**The primitive**: Slack-surfaced agentic document Q&A — an agent that answers natural-language questions by federated retrieval across live doc sources (Atlassian, Drive, Slack, web) and returns cited answers, read-only.

**Scan scope**: `~/Workspace/dev/{apps,wip,tools,archive,ref}/`, swept 2026-07-09 (full sweep report summarized in `research/sources/definition-and-grill-2026-07-09.md` § Research track 3).

**Result**: no sibling ships the full primitive. Three partial siblings each ship one component; the Slack surface has no prior art anywhere in the workspace.

### Sibling 1 — ask-bc (agent-runtime component)

- **Location**: `~/Workspace/dev/wip/ask-bc`
- **What they shipped**: production-grade agentic assistant for BigCommerce merchants — Claude tool-calling loop on a Cloudflare Worker (Durable Object per store), 22 read tools in a sandbox, 7 write tools behind a two-turn confirm gate.
- **ADR**: `~/Workspace/dev/wip/ask-bc/docs/architecture/decisions/001-codemode-agent-runtime.md` — read end-to-end 2026-07-09.
- **What the ADR decided and why** (evidence of read): ask-bc's original Vercel AI SDK tool-loop hit a documented wall — compound queries chain 5–10 serial LLM round-trips and die at the `stepCountIs(10)` cap, degrading into partial answers. The accepted fix was Codemode (`@cloudflare/think` + `@cloudflare/codemode`): the model writes TypeScript that chains twenty API calls with parallelism and in-memory joins inside a sandboxed Dynamic Worker, no LLM round-trip between them. Model strategy: Haiku 4.5 default, Sonnet 4.6 on continuation turns via the `beforeTurn` hook. Credentials never enter generated code — the sandbox sees only `codemode.*` RPC proxies, `globalOutbound: null`. Three alternatives were rejected: Vercel Sandbox executor (200–800ms cold starts vs <10ms Dynamic Workers, and 2–3 days rebuilding what Think ships), full Cloudflare migration (3–5 days re-validating OAuth/iframe/CSP work with zero demo value), and a plan-executor meta-tool (no in-memory aggregation, no credential isolation).
- **Adopted**: the read/write structural separation (our version is stricter — no write tools exist at all, read-only hard line per ADR-0001); the wall itself as a design input — if pilot questions turn out to chain many source searches per answer, serial tool-loop latency is the first thing to profile, and parallel tool dispatch or Codemode-style batching is the known fix.
- **Diverged**: we do not adopt the Cloudflare DO runtime, model-routing, or credential-proxy machinery for v1 — **because our primary path is zero-code** (Claude Tag hosts the loop) and our contingent build is a thin retrieval bot with single-digit read tools and uniform ACLs (shared credential, no per-tenant isolation needed). ask-bc's runtime shape becomes relevant only if the build branch activates AND compound-query latency proves real. Also explicitly NOT adopted: ask-bc's `doc-search.ts` — a hardcoded ~50-entry keyword array that is not a retrieval precedent — and its auth posture, which a prior security audit flagged (plaintext secret handling, permissive CORS, shared token).

### Sibling 2 — knowledge-index (retrieval component)

- **Location**: `~/Workspace/dev/archive/knowledge-index` — **[ARTIFACT GONE — verified 2026-07-27]** the entire `~/Workspace/dev/archive/` directory no longer exists. Confirmed three ways: the path is absent while sibling `~/Workspace/dev/ref` resolves; a filesystem-wide search for `*knowledge-index*` returns nothing; and `~/.config/git/ignore` holds only `.claude/settings.local.json` and `.worktrees/`, so this is not an ignore-rule artifact. Workspace drift since 2026-07-09, not research that degraded.
- **What they shipped**: vector-embedding knowledge index with semantic search over workspace markdown — better-sqlite3 + sqlite-vec local vector store, pluggable embedding providers (local transformers or OpenAI), exposed as an MCP server with `search_knowledge` / `index_status` / `reindex` tools plus a CLI.
- **Audit artifact**: `~/Workspace/dev/archive/knowledge-index/src/mcp-server.ts` — no longer readable (see above). It was reviewed 2026-07-09 and the read summary below stands as the record of that review, but the claim is **no longer independently checkable**. Treat it as testimony, not as a verifiable citation.
- **What it teaches** (evidence of read): the chunk→embed→sqlite-vec→search pipeline works as a small local system with a clean provider abstraction (`src/embeddings/{local,openai,provider}.ts`); no Anthropic/Voyage provider ships, so adopting it means adding one.
- **Diverged**: we do not index in v1 — **because the retrieval consensus and our uniform-ACL, live-source inventory favor federated search** (no index to go stale, no copy to leak). knowledge-index *was* the named contingency if the CMS-backed internal-site portion ever needs a crawl+index seam (ADR-0001 trigger 3). **That fallback now points at nothing.** If trigger 3 ever fires, the contingent architecture has no reference implementation in this workspace and would be designed from scratch — which raises the cost of that branch and should be weighed when the census tells us whether internal doc sites are in pilot traffic.

### Sibling 3 — hackathon-hive mcp-server (MCP-with-auth component)

- **Location**: `~/Workspace/dev/ref/hackathon-hive/mcp-server`
- **What they shipped**: classic MCP server (`@modelcontextprotocol/sdk`) on Vercel serverless over Streamable HTTP — Supabase Postgres with RLS, bearer-token auth, 12 tools registered modularly (schema+handler pair per file).
- **Audit artifact**: `~/Workspace/dev/ref/hackathon-hive/mcp-server/src/server.ts` (no ADR exists; the source is the record) — reviewed 2026-07-09.
- **What it teaches** (evidence of read): the cleanest local template for "MCP server with auth and a DB" — modular tool registration keeps per-tool schema+handler pairs single-file.
- **Diverged**: not needed in v1 — **because the build branch consumes existing official remote MCP servers (Atlassian, Slack) rather than authoring a new one**. Becomes relevant only if we ever wrap a source that lacks an official MCP server (e.g., a CMS-backed internal site) as our own MCP tool.

### Slack surface

No Slack bot, `@slack/bolt` dependency, webhook, or `chat.postMessage` usage exists anywhere in the workspace. The Slack surface is greenfield with no internal precedent — which is a further point for the configure-first path, since Claude Tag supplies the surface.
