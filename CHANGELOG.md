# Changelog

## 0.4.3 — 2026-08-24

- Pin **data-engineering-knowledge-capture 0.4.2** (Fabric reverse-engineering walk fixes: [#44](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/issues/44) / [#45](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/45)).
- Catalog metadata **0.4.3**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Other foundation pins unchanged (okf-graph-eng 0.8.1, PKC 0.8.1, SAC 0.5.1, AGER 0.7.1).


## 0.4.2 — 2026-08-24

- Pin foundation packs to the **migration-guide patch**:
  - okf-graph-eng **0.8.1**
  - project-knowledge-capture **0.8.1**
  - system-architecture-capture **0.5.1**
  - data-engineering-knowledge-capture **0.4.1**
  - okf-agent-graph **0.7.1**
- Catalog metadata **0.4.2**. Root and `.claude-plugin/marketplace.json` stay in sync.


## 0.4.1 — 2026-08-24

- Pin foundation packs to the **noun-ownership cut**:
  - okf-graph-eng **0.8.0** (Catalog + ContextPack only)
  - project-knowledge-capture **0.8.0** (TicketLink + work types)
  - system-architecture-capture **0.5.0** (139 architecture nouns)
  - data-engineering-knowledge-capture **0.4.0** (data plane; jobs are IngestionJob)
  - okf-agent-graph **0.7.0** (agent/harness nouns; WriteEvent is not AGER)
- Re-synced `.claude-plugin/marketplace.json` with root `marketplace.json` (had been left at catalog 0.3.7 / 15 plugins after 0.4.0).
- README: foundation install + `/plugin marketplace update` + `/plugin update` for stale In-use pins.

## 0.4.0

- Add nine AGER translator plugins to the catalog (v0.1.1).


## 0.3.9

- WikiTicket SDD on ContentPacks/AGER/DEKC; catalog versions to matching tags.


## 0.3.8

- Catalog bump: three-host hooks releases (Codex + Cursor-native).


## 0.3.7 — 2026-08-17

- **Cursor host.** Every pack now ships `.cursor-plugin` + `docs/CURSOR.md`.
- Pins: core **0.3.5**, executive-coordination **0.3.3**, eight job packs **0.3.2**,
  okf-graph-eng **0.7.3**, PKC **0.7.3**, SAC **0.4.3**, DEKC **0.3.3**,
  AGER **0.6.3**, worklog **0.24.2**.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.

## 0.3.6 — 2026-08-17


- Pin **okf-graph-eng 0.7.2** (PostToolUse is fail-closed validate, not curate).
- Core stays **0.3.3**. PKC **0.7.2**. SAC **0.4.2**. DEKC **0.3.2**. AGER **0.6.2**.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.
- Implements part of [okf-plugin#55](https://github.com/SpillwaveSolutions/okf-plugin/issues/55).

## 0.3.5 — 2026-08-16

- Pin **system-architecture-capture 0.4.2** (ContextPack token budget).
- Pin **data-engineering-knowledge-capture 0.3.2** (ContextPack token budget).
- Pin **okf-agent-graph 0.6.2** (local AGER packer, same fail-closed 1/4-window contract).
- Core stays **0.3.3**. PKC stays **0.7.2**.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.
- Implements part of [okf-plugin#55](https://github.com/SpillwaveSolutions/okf-plugin/issues/55).

## 0.3.4 — 2026-08-16

- Pin **project-knowledge-capture 0.7.2** (ContextPack token budget: 1/4 window, fail-closed; bodies off unless pack root; auto-inject stays silent over budget).
- Core stays **0.3.3**. Other foundation pins unchanged.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.
- Implements part of [okf-plugin#55](https://github.com/SpillwaveSolutions/okf-plugin/issues/55).

## 0.3.3 — 2026-08-16

- Pin **second-brain-core 0.3.3** (ContextPack token budget: 1/4 window, fail-closed; bodies off unless pack root).
- Job packs stay **0.3.1**. Other foundation pins unchanged.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.

## 0.3.2 — 2026-08-16


- Sync marketplace pins to **post-Wave-C identity** versions (fail-closed `--author` / `SECOND_BRAIN_IDENTITY` + WriteEvent on knowledge writes):
  - second-brain-core **0.3.2**
  - okf-graph-eng **0.7.1**
  - project-knowledge-capture **0.7.1**
  - system-architecture-capture **0.4.1**
  - data-engineering-knowledge-capture **0.3.1**
  - okf-agent-graph **0.6.1**
  - worklog **0.24.1**
- Job packs remain **0.3.1**.
- Root `marketplace.json` and `.claude-plugin/marketplace.json` stay in sync.
- Implements part of [okf-plugin#55](https://github.com/SpillwaveSolutions/okf-plugin/issues/55).

## 0.3.1 — 2026-08-16

- Marketplace lists the **foundation layer** (okf-plugin, PKC, SAC, DEKC, AGER, WikiTicket) for discovery.
- ContentPack entries stamped 0.3.1 (privacy-scrub Wave B).
- `.claude-plugin/marketplace.json` synced with the root marketplace (was stale at 0.1.0).


## 0.3.0 - 2026-08-15

- Every ContentPack now ships `docs/ONBOARDING.md`: LLM-wiki history, destination state, public repo list.
- Full type ownership in each `docs/GROK_BOT.md` (every registry noun).
- Linked Northstar sample graphs that pack in 2 hops.
- Frontmatter parser walks typed links without PyYAML.
- Plugin versions aligned at 0.3.0.

## 0.2.0 - 2026-08-15

- Isolation: worktree + PR protocol documented. Concurrent writers do not share main.
- Hosts: Grok Bot and LangChain Deep Agents bindings on every pack.
- Eight job-function plugins plus core (not nine jobs).
- Marketplace never names a private knowledge remote.

## 0.1.0 - 2026-08-14

- Initial suite marketplace for the eight job-function ContentPack plugins plus core.
