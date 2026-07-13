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
