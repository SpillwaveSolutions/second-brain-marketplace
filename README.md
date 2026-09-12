# Spillwave Second Brain Marketplace

One Claude Code marketplace for the eight job-function ContentPack plugins plus core.
Each plugin writes OKF Markdown + YAML into the **same** `knowledge/` tree.
Grok Bots, Claude Code, Codex, Deep Agents, and local laptop jobs share that tree.

MIT. Multi-host: **Claude Code**, **Grok Build**, **Codex**, **Cursor**, **Agent Plugins 1.0**, **Grok Bot**, **LangChain Deep Agents**.


## Install the suite

```bash
# Claude Code: add (or refresh) the marketplace, then install what you need
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
/plugin marketplace update SpillwaveSolutions/second-brain-marketplace

# Foundation — noun-ownership cut (24 Aug 2026)
/plugin install okf-graph-eng@spillwave-second-brain
/plugin install project-knowledge-capture@spillwave-second-brain
/plugin install system-architecture-capture@spillwave-second-brain
/plugin install data-engineering-knowledge-capture@spillwave-second-brain
/plugin install research-knowledge-capture@spillwave-second-brain
/plugin install okf-agent-graph@spillwave-second-brain
/plugin install worklog@spillwave-second-brain

# Shared core + eight job-function ContentPacks
/plugin install second-brain-core@spillwave-second-brain
/plugin install executive-coordination@spillwave-second-brain
/plugin install account-management@spillwave-second-brain
/plugin install sales-pipeline@spillwave-second-brain
/plugin install executive-job-search@spillwave-second-brain
/plugin install consulting-leads@spillwave-second-brain
/plugin install content-media@spillwave-second-brain
/plugin install news-digest@spillwave-second-brain
/plugin install gtm-positioning@spillwave-second-brain

# Or install a single plugin from its own repo
/plugin marketplace add SpillwaveSolutions/content-media
/plugin install content-media@SpillwaveSolutions

# Skilz CLI
skilz install SpillwaveSolutions/second-brain-core
skilz install SpillwaveSolutions/content-media
```

### Already installed? Refresh pins

Claude Code caches the marketplace snapshot. `/plugin` **Available** can lag GitHub, and **In use** stays on the version you originally installed until you update.

After this catalog (`0.4.10`) the foundation **Available** pins are:

| Pack | Pin |
|------|-----|
| `second-brain-core` | **0.3.8** |
| `okf-graph-eng` | **0.8.2** |
| `project-knowledge-capture` | **0.9.4** |
| `system-architecture-capture` | **0.5.5** |
| `data-engineering-knowledge-capture` | **0.5.2** |
| `research-knowledge-capture` | **0.2.7** |
| `okf-agent-graph` | **0.8.1** |

```bash
/plugin marketplace update SpillwaveSolutions/second-brain-marketplace
/plugin update second-brain-core@spillwave-second-brain
/plugin update okf-graph-eng@spillwave-second-brain
/plugin update project-knowledge-capture@spillwave-second-brain
/plugin update system-architecture-capture@spillwave-second-brain
/plugin update data-engineering-knowledge-capture@spillwave-second-brain
/plugin update research-knowledge-capture@spillwave-second-brain
/plugin update okf-agent-graph@spillwave-second-brain
```

Existing graphs that still have domain nouns in the engine, or data jobs typed `Workflow`: [noun-ownership migration](https://github.com/SpillwaveSolutions/okf-plugin/blob/main/docs/user_guide/noun-ownership-migration.md).

Cursor (including Grok Bot cloud agents):

```text
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
/plugin install content-media
```

Each pack ships `.cursor-plugin/plugin.json` and `docs/CURSOR.md`. A Cursor session opened on the knowledge tree still follows the write protocol even without a plugin install.

Use the public starter for fiction-only samples:


```bash
git clone https://github.com/SpillwaveSolutions/second-brain-starter.git
```

Point every plugin at **your** existing local `knowledge/` folder. This marketplace never names a private remote. Concurrent writers on different machines should open an isolation session (`brain_session.py open`) so writes land as PRs. See second-brain-core `docs/ISOLATION.md`.

## Plugins

| Plugin | Agent identity | What it writes |
|--------|----------------|----------------|
| `second-brain-core` | grok-bot/second-brain-core | Shared OKF schemas, typed edges, deterministic write helpers, isolation, ContextPack engine. |
| `executive-coordination` | grok-bot/executive-coordination | Chief-of-staff ContentPack: priorities, decisions, blockers, digests, handoffs. |
| `account-management` | grok-bot/account-management | Account and relationship ContentPack: clients, contacts, plans, deliverables, renewals. |
| `sales-pipeline` | grok-bot/sales-pipeline | Sales pipeline ContentPack: leads, opportunities, stages, objections, forecasts. |
| `executive-job-search` | grok-bot/executive-job-search | Executive job-search ContentPack: job leads, roles, interviews, offers, criteria. |
| `consulting-leads` | grok-bot/consulting-leads | Inbound consulting-lead ContentPack: engagement types, discovery, scopes, qualification. |
| `content-media` | grok-bot/content-media | Content and audience ContentPack: articles, drafts, series, subscribers, metrics. |
| `news-digest` | grok-bot/news-digest | News digest ContentPack: items, sources, scheduled digests, trends, follow-up candidates. |
| `gtm-positioning` | grok-bot/gtm-positioning | Go-to-market ContentPack: offers, positioning, ICPs, campaigns, battle cards. |

## How the pieces fit

```
Grok Bot: Articles  ──writes──►  knowledge/articles/     (session worktree + PR)
Grok Bot: Sales     ──writes──►  knowledge/sales-leads/
Laptop job (Codex)  ──writes──►  knowledge/   (same tree)
Claude Code         ──packs───►  bounded ContextPack (2 hops / ~20 nodes)
Deep Agents         ──skills──►  same scripts, same isolation
```

Rules:

1. The model proposes. Schema-enforced scripts commit.
2. An agent never invents `rel` values and never writes types it does not own.
3. Progressive disclosure. Pack from a root. Do not dump the whole tree.
4. Samples use the fictional **Northstar** account and **Lumenfield** employer. No real client names.
5. Concurrent writers isolate via worktree + PR. They do not share one mutable main tip.

## Foundation plugins (now in this marketplace)

Install the engineering substrate the same way as a job pack. These pins are the 12 Sep 2026 query-time retriever cut.

| Plugin | Repo | Pin |
|--------|------|-----|
| `second-brain-core` | [second-brain-core](https://github.com/SpillwaveSolutions/second-brain-core) | **0.3.8** |
| `okf-graph-eng` | [okf-plugin](https://github.com/SpillwaveSolutions/okf-plugin) | **0.8.2** |
| `project-knowledge-capture` | [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) | **0.9.4** |
| `system-architecture-capture` | [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) | **0.5.5** |
| `data-engineering-knowledge-capture` | [data-engineering-knowledge-capture](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture) | **0.5.2** |
| `research-knowledge-capture` | [research-knowledge-capture](https://github.com/SpillwaveSolutions/research-knowledge-capture) | **0.2.7** |
| `okf-agent-graph` | [okf-agent-graph](https://github.com/SpillwaveSolutions/okf-agent-graph) | **0.8.1** |
| `worklog` | [wiki_ticket_sdd](https://github.com/SpillwaveSolutions/wiki_ticket_sdd) | 0.24.10 |

For Q&A, the parent spawns a `*-retriever` child (`knowledge-retriever` / `architecture-retriever` / `data-retriever` / `research-retriever`) and keeps a summary card. Do not pack inline in the parent for Q&A. The contract lives in second-brain-core **0.3.8** (`docs/RETRIEVAL.md`; `sbc_common.py pack --tiny --summary`).

Existing second brains: [okf-plugin noun-ownership migration](https://github.com/SpillwaveSolutions/okf-plugin/blob/main/docs/user_guide/noun-ownership-migration.md).

Onboarding for any host: [second-brain-core docs/ONBOARDING.md](https://github.com/SpillwaveSolutions/second-brain-core/blob/main/docs/ONBOARDING.md).

## Related engineering plugins


- [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) - The why second brain. Decisions, experiments, rationale.
- [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) - The what-is-running second brain.
- [data-engineering-knowledge-capture](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture) - The data-plane second brain.
- [research-knowledge-capture](https://github.com/SpillwaveSolutions/research-knowledge-capture) - The research second brain. Areas, subjects, claims, evidence, findings.
- [okf-plugin](https://github.com/SpillwaveSolutions/okf-plugin) - Open Knowledge Format graph engine.
- [okf-agent-graph](https://github.com/SpillwaveSolutions/okf-agent-graph) - AGER orchestrator / doer / judge / synthesizer.
- [wiki_ticket_sdd](https://github.com/SpillwaveSolutions/wiki_ticket_sdd) - Visible work log. Append-only ULID JSONL plus fold.

## Onboarding a Grok Bot

Each plugin now ships `docs/ONBOARDING.md`. Give a new Grok Bot that file first. It covers:

- History of the LLM-wiki / second-brain effort (OKF, WikiTicket, PKC, SAC, DEKC, RKC, AGER, ContentPacks)
- Destination state: cloud Grok Bots and local laptop agents reading and writing the same git-native tree
- Identity, isolation, deterministic write boundary, progressive disclosure
- Every public repository in this suite plus the foundation layer

Start with [second-brain-core docs/ONBOARDING.md](https://github.com/SpillwaveSolutions/second-brain-core/blob/main/docs/ONBOARDING.md).

## Docs in the starter

- [second-brain-starter](https://github.com/SpillwaveSolutions/second-brain-starter) - public Northstar graph, agent identities, packing prompts, articles workflow

## License

MIT. Copyright 2026 Rick Hightower / contributors.
