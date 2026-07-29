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

## Gemini Enterprise — added 2026-07-29, and it is the strongest alternative on the shelf

Raised because commerce.com is a Google Workspace shop and Google renamed NotebookLM to **Gemini Notebook** on 2026-07-16. The rename turns out to be the least interesting part; the product next to it is not.

**Take the rename off the table first.** Google's own announcement says "We're renaming NotebookLM to Gemini Notebook. It's the same standalone product, now doing more across the Google ecosystem." What was added is native code execution against notebook sources and sync with the Gemini app. `G5` in `ai-governance-constraints.md` did not turn on the name — it retired the NotebookLM *recommendation* because approval burden stopped discriminating once Claude turned out to be org-wide, and left fitness unassessed. A rename touches neither. **`G5` stands.**

**Gemini Enterprise is a different product and a real competitor to `Ask Commerce`.** A Google Cloud enterprise-search-and-agent platform with permission-aware federated and indexed retrieval over Google and third-party sources. Its connector set overlaps ours almost exactly: Google Drive, Confluence Cloud, Jira, Slack, SharePoint, OneDrive, ServiceNow, Salesforce, Box, Asana, Teams, HubSpot, Zendesk.

**The uncomfortable part, stated plainly: it documents the one thing `AC-1` says we cannot do.** The Google Drive data store supports three scope modes — all drives in the workspace, a folder filter, or **a shared-drive filter**, configured with `SharedDriveIds` under `admin_filter` or `admin_exclusion_filter`. Shared drives are first-class configuration, not an open question. That is precisely the corpus the `Opportunities` shared drive holds and precisely the gap the Annex B request exists to close.

Two architectural details that cut in our favour and were not obvious:

- **The Drive connector federates.** "Data is not copied into the Gemini Enterprise index." Documents must be "accessible, either by placing them in a shared drive that is owned by the domain or by assigning the ownership to a user in the domain." Federation is the pattern this initiative already chose, so on Drive there is no new leak class.
- **The third-party connectors index, and identity sync is not continuous.** ACL data refreshes on schedules ranging from every 30 minutes to every seven days. **That is the ACL-sync-drift leak class this document already retired indexed RAG over** (OWASP 2025 LLM Top 10 #2), with a documented staleness window of up to a week. It applies to Confluence, Jira and Slack — which is to say, to the entire corpus the census measured.

Confluence Cloud specifics, since it is our largest source: it indexes spaces, pages and user information plus attachments and comments, ingests at 20 QPS, caps files at 200 MB, **does not support incremental sync for the spaces entity**, and **excludes archived pages from a full sync**. It also cannot authenticate with a Google Cloud service account.

### Why it still does not displace Ask Commerce

| Argument | Weight |
|---|---|
| **It is a separate paid subscription, and that changes the approval route** | Decisive. `G2` names **Vendor Intake Form — paid subscription or purchase** as its own path, distinct from the AI Use Case Review this initiative takes as an existing-approved-tool/new-data case. Adopting it converts the cheap route into the expensive one — the exact trade `decisions/0001` was built to avoid |
| Being a Workspace shop does not entitle us to it | Corrects the premise. Workspace Business/Enterprise bundles the Gemini app and Notebook access; Gemini Enterprise is a distinct Google Cloud product, priced, sold and deployed separately, per-seat with consumption billing on top |
| Duplicate AI spend beside Claude Enterprise | Same disqualifier that retired Glean. Claude is already deployed org-wide with no gate and sits in the GRC AI Registry at Confidential classification (`G4`) |
| Two ask-your-org surfaces is a new `P4` instance | Answers would diverge between them with no adjudication layer, at the tool tier rather than the document tier. This initiative would be manufacturing the defect it exists to fix |
| It does not touch invalidation | §2 of the plan now holds that invalidation is the only unsolved capability. Gemini Enterprise is a retrieval product; it changes nothing about what gets written down or when a record becomes wrong |

### What it is actually good for

**Leverage on the Drive request, and a named fallback.** Shared-drive scoping being routine configuration in a competing product is evidence the ask in Annex B is ordinary rather than exotic. And `solution-plan.md` §6's weakest branch — *what if AI Operations declines the Drive connection* — now resolves to a specific, costed, already-Workspace-native alternative instead of "the plan needs rethinking." That is a better answer than the one that branch had yesterday.

**Revival condition:** AI Operations declines the Drive connection or cannot make Shared Drives work, **and** the census shows the Drive corpus carries the majority of decision-grade solution knowledge. Both, not either. A Vendor Intake is only worth opening for the corpus that turns out to matter most.

| Reference | Track | Evidence | Used for | Gate-status |
|---|---|---|---|---|
| Gemini Enterprise connector, Drive data-store and editions docs (`docs.cloud.google.com/gemini/enterprise/docs/...`) | Quality | Vendor-authored primary; resolved 2026-07-29 | Shared-drive support; federation vs indexing; identity-sync intervals; Confluence limits | pass |
| `blog.google` NotebookLM → Gemini Notebook announcement (2026-07-16) | Quality | Vendor-authored primary | The rename is a rename; `G5` unaffected | pass |
| Gemini Enterprise pricing at roughly $21–60/user/month | Convention | **Third-party aggregators only.** Google's own pricing page could not be resolved — it truncated on fetch | Order-of-magnitude context for the Vendor Intake argument | **warn** — do not quote a figure to a sponsor. The load-bearing claim is *separate paid subscription*, which the vendor editions doc supports on its own |
| Edition → connector mapping | — | Vendor doc returned an internally inconsistent mapping (Business appears on both sides of the full-vs-select connector split) | Nothing | **unresolved** — if this is ever revived, confirm which edition carries Confluence and Slack before costing anything |

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
