# Spillwave Second Brain Marketplace

One Claude Code marketplace for the nine job-function ContentPack plugins.
Each plugin writes OKF Markdown + YAML into the **same** `knowledge/` tree.
Grok Bots, Claude Code, Codex, and local laptop jobs share that tree.

MIT. Dual-host: **Claude Code**, **Grok Build**, and **Codex**.

## Install the suite

```bash
# Claude Code: add the marketplace, then install what you need
/plugin marketplace add SpillwaveSolutions/second-brain-marketplace
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

Then clone the shared knowledge tree:

```bash
# Public starter (Northstar fiction only)
git clone https://github.com/SpillwaveSolutions/second-brain-starter.git

# Private working brain (Grok Bots + laptop jobs write here)
# Ask an org admin if you need access.
git clone git@github.com:SpillwaveSolutions/rick-grok-bot-knowledge.git
```

Point every plugin and every local job at the same `knowledge/` folder.

## Plugins

Plugins are job functions. They do **not** ship with an agent name.

The agent using the plugin decides who it is — or asks the human — then claims that identity:

```bash
python3 scripts/brain.py whoami
# if claimed is false:
#   ask the user "What should I sign as?"
python3 scripts/brain.py whoami --claim "Your Name" --plugin content-media
```

Writes fail until an identity is claimed (`--author`, `SECOND_BRAIN_IDENTITY`, or `knowledge/.identity.json`). There is no default `Grok Bot: …` author.

| Plugin | Job function | What it writes |
|--------|--------------|----------------|
| `second-brain-core` | Shared substrate | Shared OKF schemas, typed edges, deterministic write helpers, and ContextPack engine. |
| `executive-coordination` | Chief of staff | Priorities, decisions, blockers, digests, handoffs. |
| `account-management` | Accounts | Clients, contacts, plans, deliverables, renewals. |
| `sales-pipeline` | Sales | Leads, opportunities, stages, objections, forecasts. |
| `executive-job-search` | Job search | Job leads, roles, interviews, offers, criteria. |
| `consulting-leads` | Consulting inbound | Engagement types, discovery, scopes, qualification. |
| `content-media` | Articles / content | Articles, drafts, series, subscribers, metrics. |
| `news-digest` | News | Items, sources, scheduled digests, trends, follow-up candidates. |
| `gtm-positioning` | Go-to-market | Offers, positioning, ICPs, campaigns, battle cards. |

## How the pieces fit

```
Any agent (claimed identity)  ──writes──►  knowledge/<catalog>/
Laptop job / Codex            ──writes──►  knowledge/   (same tree)
Claude Code / Grok            ──packs───►  bounded ContextPack (2 hops / ~20 nodes)
```

Rules:

1. The model proposes. Schema-enforced scripts commit.
2. An agent never invents `rel` values and never writes types it does not own.
3. Progressive disclosure. Pack from a root. Do not dump the whole tree.
4. Samples use the fictional **Northstar** account and **Lumenfield** employer. No real client names.

## Related engineering plugins

- [project-knowledge-capture](https://github.com/SpillwaveSolutions/project-knowledge-capture) - The why second brain. Decisions, experiments, rationale.
- [system-architecture-capture](https://github.com/SpillwaveSolutions/system-architecture-capture) - The what-is-running second brain.
- [data-engineering-knowledge-capture](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture) - The data-plane second brain.
- [okf-plugin](https://github.com/SpillwaveSolutions/okf-plugin) - Open Knowledge Format graph engine.
- [okf-agent-graph](https://github.com/SpillwaveSolutions/okf-agent-graph) - AGER orchestrator / doer / judge / synthesizer.
- [wiki_ticket_sdd](https://github.com/SpillwaveSolutions/wiki_ticket_sdd) - Visible work log. Append-only ULID JSONL plus fold.

## Docs in the starter

- [second-brain-starter](https://github.com/SpillwaveSolutions/second-brain-starter) - public Northstar graph, agent identities, packing prompts, articles workflow
- [rick-grok-bot-knowledge](https://github.com/SpillwaveSolutions/rick-grok-bot-knowledge) - private working second brain (org members)

## License

MIT. Copyright 2026 Rick Hightower / contributors.
