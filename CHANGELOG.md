# Changelog

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
