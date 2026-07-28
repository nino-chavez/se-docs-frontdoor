# Competitive landscape — the buy shelf, and why it retired

Stage 1 competitive leg. Full market-scan findings with per-claim URLs live in `research/sources/definition-and-grill-2026-07-09.md` § Research track 2; this doc is the graded synthesis.

## The competitive set

The pilot's real competition is not a product — it is the **shoulder-tap to a senior SE**, the incumbent behavior the deflection metric measures. The product shelf, evaluated as of mid-2026:

| Option | One-line | Why it retired |
|---|---|---|
| Claude Tag (Anthropic) | The official Claude-in-Slack successor: @Claude in channels with connector access, per-channel identities, spend limits, audit log | Not a rival — this IS the Tier 0 candidate; org already has seats + a live connector |
| Slack Slackbot / Agentforce (Salesforce) | Slack-native agent layer after the 2026-03 overhaul; routes across 6,000+ apps as an MCP client | Salesforce's model (not Claude), permission architecture unpublished; org's AI spend is already Anthropic |
| Glean | Enterprise-search platform, 100+ permission-aware connectors, polished Slack container | ~$60k/yr floor, sales-led; duplicate spend next to existing Claude Enterprise |
| Onyx (ex-Danswer) | Open-source (MIT) self-hostable enterprise search + Slack bot; syncs source ACLs into its index; can run Claude as its model | ACL-sync is its differentiator — and our access posture is uniform, so the differentiator buys nothing. Named revival condition: indexed-RAG-with-ACL-sync across many weak-search sources (ADR-0001) |
| Dust | Agent platform (MIT core), Claude among its models, $30–150/seat credit-metered | Sits between Onyx and a thin self-build without beating either on our inventory |

## The retrieval-architecture comparison (build patterns, not products)

- **Federated/agentic search** — the agent queries each source's own search API at question time. Wins on permission safety (nothing copied, each source enforces its own gate at call time), freshness (no index lag), and ops (no pipeline). Slower per answer (multiple live queries).
- **Indexed RAG** — ingest + embed into a vector store with ACL sync. Wins on latency and cross-source ranking at large corpus scale; loses on the ACL-sync-drift leak class, which OWASP's 2025 LLM Top 10 ranks #2 with documented incidents.
- **Fit for this initiative**: moderate source count, all with real search APIs, uniform ACLs, freshness-sensitive → federated, with indexing held as a scoped contingency for weak-search sources only.

## The capture shelf — added 2026-07-28, and it should have been here from the start

Everything above scans the **retrieval** shelf. The capture shelf was never scanned, which left `solution-plan.md` §2 asserting "the capture problem is not solved" against an unexamined market. Partly wrong, and the correction is useful because it narrows what is actually differentiated.

**What ships commercially today.** Guru's own product page claims "verification workflows" with "built-in review cycles and expert recommendations," lifecycle controls, agents that "verify and unverify info *for* you," and a system that "identifies knowledge gaps and suggests content updates automatically." Third-party reviews describe ticket monitoring that turns a resolved ticket into a draft card in one click; IrisAgent markets `AutoKB` as writing articles from resolved tickets. So **derive-a-draft-from-an-artifact, route it to a named owner, expire it on a clock** is a shipping category, not an open problem. §2 cannot claim otherwise.

**What did not turn up.** Guru's page contains no mention of product changelogs, known-limitation registers, or invalidating a document because a shipped capability made it wrong. The category's staleness model is **time-based and owner-prompted** — review cycles, expiration dates, gap suggestions. That is the model `P6` and `solution-plan.md` §4 already argue is insufficient, and the market appears to agree with the framing while not having solved it.

**So the differentiated claim is narrower and stronger than the one §2 was making.** Not *capture is unsolved* — it is *invalidation-by-evidence is unsolved*: joining shipped platform capabilities against documents that predate them, and maintaining negative knowledge as a first-class record rather than as prose someone remembers to revise. That is also a much smaller thing to build than a capture system, which strengthens rather than weakens the recommendation.

| Reference | Track | Evidence | Used for | Gate-status |
|---|---|---|---|---|
| Guru product documentation (`getguru.com/reference/ai-knowledge-base`) | Quality | Vendor-authored primary; resolved 2026-07-28 | Verification-workflow and gap-suggestion capabilities exist commercially; **absence** of changelog/invalidation claims | pass — but absence from one page is weak evidence of absence from the product. Upgrade before this appears in any external-facing claim |
| Guru ticket→draft-card monitoring; IrisAgent `AutoKB` | Convention | Third-party reviews and a competitor's marketing, not vendor-primary | Breadth of the capture shelf only | **warn** — one source is a direct competitor describing Guru. Not load-bearing; do not cite as fact |

## Reference grading table

Track classification per the two-track framework (convention = "users/market recognize it"; quality = "the claim is anchored in an authoritative source"). Product references below are cited as competitive context; authority references carry the load-bearing claims.

| Reference | Track | Evidence | Used for | Gate-status |
|---|---|---|---|---|
| Anthropic official docs (platform.claude.com, anthropic.com news/engineering) | Quality | Vendor-authored primary documentation: MCP connector reference, search_result/citations reference, contextual-retrieval engineering post (URLs in sources doc) | Claude Tag capabilities; build-path architecture; the <200K-token prompt-loading threshold | pass |
| Slack developer docs (docs.slack.dev) | Quality | Vendor-authored primary documentation: AI-apps guidance (agent_view, streaming, feedback_buttons) | Slack UX patterns for the contingent build | pass |
| OWASP LLM Top 10 (2025) | Quality | Standards-body publication; Sensitive Information Disclosure ranked #2, vector/embedding weaknesses category added | The permission-leak risk claim that retired indexed RAG | pass |
| Google Cloud / Google Support docs | Quality | Vendor-authored primary documentation: NotebookLM Enterprise API reference (CRUD-only, no query endpoint), source-handling help doc | NotebookLM ruled out as a queryable source | pass |
| anthropics/claude-code#53442 | Quality | Primary bug report (OPEN, 2026-04-26) with root-cause params named | Shared-Drive blind-spot risk; pilot test #1 | pass |
| Oso authorization post; practitioner write-ups on federated vs indexed retrieval | Quality | Named-author vendor/practitioner engineering posts with cited incidents (URLs in sources doc) | Federated-over-indexed consensus claim | pass |
| Glean | Convention | Market presence; vendor-published Slack-container docs | Competitive context: the premium buy anchor and its price floor | pass (convention-only is fine for market-context cites) |
| Onyx | Convention | Public MIT repo + vendor connector docs | Competitive context: the named contingency product | pass |
| Dust | Convention | Vendor-published pricing/model docs | Competitive context | pass |
| Slack Slackbot / Agentforce | Convention | Vendor announcements (2026-03) + tech-press coverage | Competitive context: the incumbent-platform default to name in any pitch | pass |
| Guru, Notion AI, Atlassian Rovo | Convention | Vendor docs; surveyed in sources doc, not load-bearing here | Breadth of the scanned shelf | pass |

No design-quality recommendations in this initiative rest on convention-track references: the product names anchor market context only, and every architectural claim traces to a vendor-primary or standards-body source above.
