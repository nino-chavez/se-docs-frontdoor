# Prior art

Canonical research-variant Stage 2 leg (`blueprint.yml:stages.stage_2.requires`).

## In this directory

| File | What it covers |
| --- | --- |
| [`capture-domain-prior-art.md`](capture-domain-prior-art.md) | **Domain E — capture.** Tooling and patterns that record knowledge at the point of work. Scanned 2026-07-27 to close a gap the founding scan left, since that scan covered retrieval only. |

## Elsewhere in the corpus

Retrieval-side and external prior art was written before this directory existed and stays where the reviewer contracts expect it:

| Artifact | What it covers |
| --- | --- |
| [`../current-state/workspace-prior-art.md`](../current-state/workspace-prior-art.md) | Internal **retrieval** implementations across `~/Workspace/dev` — the `ask-bc` agent-runtime reference (tool loop, model routing, per-tenant creds; its "doc search" is a hardcoded keyword array, so **not** a retrieval precedent, and its auth posture failed a prior security audit), the `knowledge-index` vector-RAG reference as the contingent indexing seam (**artifact gone as of 2026-07-27** — the fallback for ADR-0001 trigger 3 now has no reference implementation), and an MCP-with-auth template. Holds the **§ Sibling-Project Scan** section that `research-sibling-scanner` resolves. |
| [`../sibling-scan.md`](../sibling-scan.md) | The scanner's own output artifact. Path is fixed by the reviewer spec. |
| [`../competitive/buy-landscape.md`](../competitive/buy-landscape.md) | External prior art — the buy shelf, retired. Lives under `competitive/` because that is its own canonical Stage 2 leg. |

**Why those three were not moved here:** `research/sibling-scan.md` cites `research/current-state/workspace-prior-art.md § Sibling-Project Scan` by path, and `research-sibling-scanner` reads and rewrites `research/sibling-scan.md` at that exact location. Relocating either would break a reviewer contract to satisfy a directory name.
