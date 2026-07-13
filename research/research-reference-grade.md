# Reference grading — Stage 1 audit

11 references graded across the research corpus: 6 Quality-track (all vendor-primary documentation, a standards body, and a primary bug report), 5 Convention-only (product references cited strictly as market context, none carrying a design or architecture recommendation). Top risks, in priority order: (1) the federated-over-indexed consensus claim leans partly on practitioner posts — mitigated by OWASP and vendor-primary co-grounding; (2) "canonical" appears 3× in the sources doc — each occurrence audited below and grounded in Anthropic primary docs; (3) no risk found in convention-track leakage into quality claims — the initiative makes no visual-design recommendations at Stage 1.

## Graded reference table

| Reference | Track | Evidence | Used for | Gate-status |
|---|---|---|---|---|
| Anthropic official docs (platform.claude.com; anthropic.com news + engineering) | Quality | Vendor-authored primary documentation: MCP-connector reference, search_result/citations reference, Claude Tag announcement, contextual-retrieval engineering post (URLs in `research/sources/definition-and-grill-2026-07-09.md`) | Claude Tag capabilities; build-path architecture; <200K-token prompt-loading threshold | pass |
| Slack developer docs (docs.slack.dev) | Quality | Vendor-authored primary documentation: AI-apps guidance (agent_view, streaming, feedback_buttons) | Slack UX patterns for the contingent build | pass |
| OWASP LLM Top 10 (2025) | Quality | Standards-body publication; Sensitive Information Disclosure at #2; vector/embedding weaknesses category | The permission-leak risk that retired indexed RAG | pass |
| Google Cloud / Support docs | Quality | Vendor-authored primary documentation: NotebookLM Enterprise API reference (CRUD-only), source-handling help doc | NotebookLM ruled out as a queryable source | pass |
| anthropics/claude-code#53442 | Quality | Primary bug report (OPEN, 2026-04-26) with root-cause parameters named | Shared-Drive blind spot; pilot test #1 | pass |
| Oso authorization post + practitioner retrieval write-ups | Quality | Named-author vendor/practitioner engineering posts with cited incidents (URLs in sources doc) | Federated-vs-indexed ACL analysis | pass |
| Glean | Convention | Market presence; vendor-published Slack-container docs | Market context: premium buy anchor + price floor | pass (convention-only OK for market-context cites) |
| Onyx | Convention | Public MIT repo + vendor connector docs | Market context: the named revival contingency | pass |
| Dust | Convention | Vendor pricing/model docs | Market context | pass |
| Slack Slackbot / Agentforce | Convention | Vendor announcements (2026-03) + tech-press coverage | Market context: incumbent-platform default | pass |
| Guru / Notion AI / Atlassian Rovo | Convention | Vendor docs; surveyed, not load-bearing | Shelf breadth | pass |

## Quality-claim grounding audit

| File | Line | Claim phrase | Supporting refs | Verdict |
|---|---|---|---|---|
| research/sources/definition-and-grill-2026-07-09.md | 3 | "canonical doc for each load-bearing claim" | Anthropic/Google/Slack/OWASP primary docs (all Quality) | pass |
| research/sources/definition-and-grill-2026-07-09.md | 9 | "vendor canonical (Anthropic)" | Anthropic official docs (Quality) | pass |
| research/sources/definition-and-grill-2026-07-09.md | 12 | "Custom-build canonical: … search_result … Citations" | platform.claude.com reference cited inline (Quality) | pass |

No other trigger phrases ("best-in-class", "modern", "industry standard", "best practice", "gold standard", "well-designed", "exemplary", "world-class") appear in the research corpus (grep swept 2026-07-09).

## Findings

1. No blocking findings. Every named reference is classified with concrete evidence; every quality-claim occurrence is grounded in a Quality-track reference; balance is 6 Quality / 5 Convention (45% convention — under the 50% warn threshold); quality grounding is spread across four independent primary sources (no QUALITY_SOLE_SOURCE).

## Verdict

STATUS: PASS
RUN_BY: research-reference-grader
DATE: 2026-07-09
