# Changelog

## 0.4.14 — 2026-09-12

Pin **okf-time-series 0.3.3** (dogfood gates). Sample fix, opt-in path
printing, `ots smoke`, and cheap-model fail-closed. `okf-pointers` stays
**0.2.0**. No other pins change.

- Pin **okf-time-series 0.3.3** (dogfood gates).
  - Sample: no `.telemetry.md`; hour rollover keeps the same slug (no `__002`).
  - `status`/`check` print walked `.okf-history` paths on `not_opted_in`.
  - `ots smoke` — check → once → tick → summarize --stub → check.
  - Setup fails closed on non-pin models (Sonnet/Sol/Terra/…).
  - Installers must open `plugin.json` and confirm **0.3.3**. 0.3.1 is the killed emit-schema path.
  - Release: [v0.3.3](https://github.com/SpillwaveSolutions/okf-time-series/releases/tag/v0.3.3)
- `okf-pointers` stays **0.2.0**.
- Catalog metadata **0.4.14**. Root and `.claude-plugin/marketplace.json` stay in sync.

## 0.4.13 — 2026-09-12

Add **okf-time-series** and **okf-pointers** as foundation packs. OTS is
snapshot-first telemetry (install is not capture). Pointers is the join plane:
`Link` is a sibling of `TypedEdge`. `okf-remote` stays out of this cut.

- Add **okf-time-series 0.3.2** (OTS). Snapshot-first telemetry: `sessions/.source.jsonl` is the immutable vendor copy; opt-in via `.okf-history` or `ots-tail opt-in`. Two summarize editions. Pointers overnight batch and Langfuse remain out of scope.
  - Release: [v0.3.2](https://github.com/SpillwaveSolutions/okf-time-series/releases/tag/v0.3.2)
- Add **okf-pointers 0.2.0**. Join plane: `Link` is a sibling of `TypedEdge` (`link_type`, not `rel`). Closed inverse taxonomy. Endpoints are never mutated.
  - Release: [v0.2.0](https://github.com/SpillwaveSolutions/okf-pointers/releases/tag/v0.2.0)
- Catalog metadata **0.4.13**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Follow-up: `okf-remote` is not pinned here.

## 0.4.12 — 2026-09-12

Pin **data-engineering-knowledge-capture 0.5.3** (plan-and-fan-out orch/ELT). Capture-time
reverse-engineering now plans first, then fans out signal-gated orchestration and ELT
walkers. Query-time `data-retriever` is unchanged. No other pins change.

- Pin **data-engineering-knowledge-capture 0.5.3** (plan-and-fan-out orch/ELT).
  - Release: [v0.5.3](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/releases/tag/v0.5.3)
  - Merge: [data-engineering-knowledge-capture#56](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/56)
- Catalog metadata **0.4.12**. Root and `.claude-plugin/marketplace.json` stay in sync.

## 0.4.11 — 2026-09-12

Pin **system-architecture-capture 0.5.6** (plan-then-fan-out walkers). Capture-time
reverse-engineering now plans first, then fans out signal-gated language and IaC
walkers. Query-time `architecture-retriever` is unchanged. No other pins change.

- Pin **system-architecture-capture 0.5.6** (plan-then-fan-out walkers).
  - Release: [v0.5.6](https://github.com/SpillwaveSolutions/system-architecture-capture/releases/tag/v0.5.6)
  - Merge: [system-architecture-capture#42](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/42)
- Catalog metadata **0.4.11**. Root and `.claude-plugin/marketplace.json` stay in sync.

## 0.4.10 — 2026-09-12

Pin **second-brain-core 0.3.8** now that the query-time retrieval contract is
published. Parent agents keep a Retrieval card; `sbc_common.py pack --tiny
--summary` is the compact pack. Pack-specific `*-retriever` agents stay in
PKC / SAC / DEKC / RKC. No other pins change.

- Pin **second-brain-core 0.3.8** (retrieval contract + `pack --tiny --summary`).
  - Release: [v0.3.8](https://github.com/SpillwaveSolutions/second-brain-core/releases/tag/v0.3.8)
- Catalog metadata **0.4.10**. Root and `.claude-plugin/marketplace.json` stay in sync.

## 0.4.9 — 2026-09-12

Query-time retriever pin bump, plus Research Knowledge Capture as a foundation pack.
Parent agents spawn a `*-retriever` child (pkc / sac / dekc / research) and keep a
summary card. Do not pack inline for Q&A.

- Pin **project-knowledge-capture 0.9.4** (`knowledge-retriever`; `pkc_pack.py --summary`).
  - Release: [v0.9.4](https://github.com/SpillwaveSolutions/project-knowledge-capture/releases/tag/v0.9.4)
  - Merge: [project-knowledge-capture#76](https://github.com/SpillwaveSolutions/project-knowledge-capture/pull/76)
- Pin **system-architecture-capture 0.5.5** (`architecture-retriever`; `sac_pack.py --summary`).
  - Release: [v0.5.5](https://github.com/SpillwaveSolutions/system-architecture-capture/releases/tag/v0.5.5)
  - Merge: [system-architecture-capture#41](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/41)
- Pin **data-engineering-knowledge-capture 0.5.2** (`data-retriever`; `dekc_pack.py --summary`).
  - Release: [v0.5.2](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/releases/tag/v0.5.2)
  - Merge: [data-engineering-knowledge-capture#55](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/55)
- Add **research-knowledge-capture 0.2.7** (RKC). Layer 0 research second brain: areas, subjects, ResearchQuestion, Claim, Evidence, Finding. Query-time `research-retriever` returns a summary card only.
  - Release: [v0.2.7](https://github.com/SpillwaveSolutions/research-knowledge-capture/releases/tag/v0.2.7)
  - Merge: [research-knowledge-capture#28](https://github.com/SpillwaveSolutions/research-knowledge-capture/pull/28)
- Pin **worklog 0.24.10** (already published; catalog was still on 0.24.9). Catch-up so `--pins` matches upstream. Not part of the retriever cut.
  - Release: [v0.24.10](https://github.com/SpillwaveSolutions/wiki_ticket_sdd/releases/tag/v0.24.10)
- Catalog metadata **0.4.9**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Follow-up: `okf-remote` / `okf-pointers` / `okf-time-series` are not pinned here. They are not yet discussed as foundation packs.

## 0.4.8 — 2026-09-01

Pin catch-up for the two foundation plugins the 0.4.7 pass deliberately held.
Neither carried the catalog or rg defects, so 0.4.7 left them alone, and both
pins then fell behind their own published releases. No plugin code changes here.
The catalog now names the release each plugin actually ships.

- Pin **okf-agent-graph 0.8.1** (was 0.7.1, two releases behind: plugin discovery for Claude, Grok, Codex, and Agent Plugins 1.0, then nested bundle links and a quieter AGKC scan).
  - Release: [v0.8.1](https://github.com/SpillwaveSolutions/okf-agent-graph/releases/tag/v0.8.1) / [v0.8.0](https://github.com/SpillwaveSolutions/okf-agent-graph/releases/tag/v0.8.0)
- Pin **worklog 0.24.9** (was 0.24.4, five patches behind: mermaid-first design docs, Claude Code packaging pins, silent-skip gates, then 0.24.8 and 0.24.9).
  - Release: [v0.24.9](https://github.com/SpillwaveSolutions/wiki_ticket_sdd/releases/tag/v0.24.9)
- Catalog metadata **0.4.8**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Every other pin verified against its latest non-draft, non-prerelease upstream release and left unchanged. The catalog now matches upstream on all 24 plugins.

## 0.4.7 — 2026-08-31

Catalog and rg correctness across the three capture plugins. All three carried
the same two defects: a YAML scalar title (`title: 421`) crashed catalog
rendering after concepts had already been written, and the rg-backed reverse
index silently dropped edges when the bundle was addressed through a symlink,
while still reporting `reverse_index: rg`.

- Pin **project-knowledge-capture 0.9.3** (both fixes; PKC has two catalog renderers, both patched).
  - Release: [v0.9.3](https://github.com/SpillwaveSolutions/project-knowledge-capture/releases/tag/v0.9.3)
  - Merge: [project-knowledge-capture#75](https://github.com/SpillwaveSolutions/project-knowledge-capture/pull/75) / [#74](https://github.com/SpillwaveSolutions/project-knowledge-capture/pull/74)
- Pin **system-architecture-capture 0.5.4** (both fixes; found first here).
  - Release: [v0.5.4](https://github.com/SpillwaveSolutions/system-architecture-capture/releases/tag/v0.5.4)
  - Merge: [system-architecture-capture#39](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/39) / [#38](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/38) / [#37](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/37)
- Pin **data-engineering-knowledge-capture 0.5.1** (both fixes).
  - Release: [v0.5.1](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/releases/tag/v0.5.1)
  - Merge: [data-engineering-knowledge-capture#54](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/54) / [#53](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/53)
- Catalog metadata **0.4.7**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Other foundation pins unchanged (okf-graph-eng 0.8.2, AGER 0.7.1, worklog 0.24.4). AGER, RKC, and WikiTicket SDD were checked for both defects and carry neither: AGER and RKC render no catalog labels from frontmatter titles and use no rg reverse index, and okf-graph-eng resolves the bundle path in `main()` before the rg backlink path is reached.

## 0.4.6 — 2026-08-30

- Pin **project-knowledge-capture 0.9.1** (retrieval-ladder patch: cold index no longer O(N²); index search no longer `Path.resolve()`s the universe; setup consent test is PATH-isolated).
  - Release: [v0.9.1](https://github.com/SpillwaveSolutions/project-knowledge-capture/releases/tag/v0.9.1)
  - Merge: [project-knowledge-capture#68](https://github.com/SpillwaveSolutions/project-knowledge-capture/pull/68) / [#67](https://github.com/SpillwaveSolutions/project-knowledge-capture/pull/67)
- Pin **system-architecture-capture 0.5.3** (rg-backed pack inbound).
  - Release: [v0.5.3](https://github.com/SpillwaveSolutions/system-architecture-capture/releases/tag/v0.5.3)
  - Merge: [system-architecture-capture#34](https://github.com/SpillwaveSolutions/system-architecture-capture/pull/34)
- Catalog metadata **0.4.6**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Other foundation pins unchanged (okf-graph-eng 0.8.2, DEKC 0.5.0, AGER 0.7.1, worklog 0.24.4).

## 0.4.5 — 2026-08-30

- Pin **data-engineering-knowledge-capture 0.5.0** (retrieval ladder: disposable SQLite/FTS5 index + ripgrep prefilter; JSON `knowledge/.index/` removed).
  - Release: [v0.5.0](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/releases/tag/v0.5.0)
  - Merge: [data-engineering-knowledge-capture#49](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/pull/49)
- Catalog metadata **0.4.5**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Other foundation pins unchanged (okf-graph-eng 0.8.2, PKC 0.9.0, SAC 0.5.2, AGER 0.7.1, worklog 0.24.4).

## 0.4.4 — 2026-08-30

- Pin foundation packs to the **retrieval-ladder** releases (Git + Markdown stays source of truth; rg / SQLite FTS5 are disposable accelerators):
  - okf-graph-eng **0.8.2** ([rg-backed backlinks](https://github.com/SpillwaveSolutions/okf-plugin/releases/tag/v0.8.2))
  - project-knowledge-capture **0.9.0** ([rg prefilter + SQLite/FTS5 index](https://github.com/SpillwaveSolutions/project-knowledge-capture/releases/tag/v0.9.0))
  - system-architecture-capture **0.5.2** ([rg prefilter for search](https://github.com/SpillwaveSolutions/system-architecture-capture/releases/tag/v0.5.2))
  - data-engineering-knowledge-capture **0.4.3** ([doctor toolchain: rg / FTS5](https://github.com/SpillwaveSolutions/data-engineering-knowledge-capture/releases/tag/v0.4.3))
- Catalog metadata **0.4.4**. Root and `.claude-plugin/marketplace.json` stay in sync.
- Other foundation pins unchanged (okf-agent-graph 0.7.1, worklog 0.24.4). research-graph is not in this catalog.


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
