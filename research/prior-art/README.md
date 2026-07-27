# Prior art

Canonical research-variant Stage 2 location (`blueprint.yml:stages.stage_2.requires`). The prior-art content for this initiative was written before the variant change and lives at the paths below. It is **not** duplicated here — these are pointers.

| Artifact | What it covers |
| --- | --- |
| [`../current-state/workspace-prior-art.md`](../current-state/workspace-prior-art.md) | Internal implementations across `~/Workspace/dev` — the `ask-bc` agent-runtime reference (tool loop, model routing, per-tenant creds; its "doc search" is a hardcoded keyword array, so **not** a retrieval precedent, and its auth posture failed a prior security audit), the `knowledge-index` vector-RAG reference as the contingent indexing seam, and an MCP-with-auth template. Contains the **§ Sibling-Project Scan** section that `research-sibling-scanner` resolves. |
| [`../sibling-scan.md`](../sibling-scan.md) | The scanner's own output artifact. Path is fixed by the reviewer spec; do not move it. |
| [`../competitive/buy-landscape.md`](../competitive/buy-landscape.md) | External prior art — the buy shelf, retired. Lives under `competitive/` because that is its own canonical Stage 2 leg. |

**Why pointers and not a move:** `research/sibling-scan.md` cites `research/current-state/workspace-prior-art.md § Sibling-Project Scan` by path, and `research-sibling-scanner` reads and rewrites `research/sibling-scan.md` at that exact location. Relocating either would break a reviewer contract to satisfy a directory name.

## Gap flagged by the 2026-07-27 restatement

The prior-art scan covered **retrieval** implementations, because the founding problem was framed as retrieval friction. It did not scan for **capture** prior art — tooling or process that records solution knowledge at the point of work. That is domain E in `../problem-space/problem-statement.md`, and it is unscanned.

Two specific unknowns the scan should have caught but could not, because they were not in scope at the time:

1. The internal assistant the sponsor referenced twice as "ask commerce" / CLA (kickoff 00:09:27, 00:33:23). Unverified, and BD-3 in the problem statement. If it exists it is the single most important piece of prior art for this initiative.
2. Whatever the delivery/IPM function already uses to record project state — named in the kickoff as a source (IPM notes) but never examined as a system.

Both are inputs the next research pass needs, not gaps in the original scan's execution.
