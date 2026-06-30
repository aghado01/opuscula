# AGENTS.md — using codex-scientiae

This repository is a **read** corpus: structured reference knowledge for a tool-using agent to retrieve
and cite, not a workspace to edit. The documents are already repaired to a consistent standard; your
job is to find and use them.

## Navigate, don't crawl

Navigation is **telescoping**. Start at [CONTENTS.md](CONTENTS.md) → a collection's root
([codices/CODICES.md](codices/CODICES.md), [compendia/COMPENDIA.md](compendia/COMPENDIA.md)) → the
per-document `CONTENTS` → the chapter or section you need. Each level points one level down; follow the
index rather than listing directories.

## What the format guarantees

Every document follows one standard, so you can rely on it when parsing or citing:

- Math is dollar-delimited LaTeX — `$…$` inline, `$$…$$` display — in pure semantic syntax (no
  render-only macros), so it reads correctly as tokens.
- Tabular data is standard markdown pipe tables; references live in a per-document sidecar; headings
  carry a clean, consistent hierarchy.

These are produced and enforced by the **codex-membrane** pipeline (the companion opusculum); the
output contract is its `STANDARDS`.

> Portfolio snapshot: a curated subset of a larger corpus, under development — expect gaps, and the
> occasional un-repaired wart.
