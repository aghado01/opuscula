# AGENTS.md — operating codex-membrane

This repository is an MCP server you *operate*, not a codebase you read. Wired to a client (see
[mcp/docs/SETUP.md](mcp/docs/SETUP.md)), the server injects its canonical workflow —
[mcp/PROCEDURE.md](mcp/PROCEDURE.md) — into your context as the `restoration_procedure` prompt. That
document is the source of truth; this file is orientation.

## Three laws

1. **Navigate, don't scan.** Find work through the work-list (`get_hotspots`, `dispatch`) or `search`.
   Never load a document to look for what to fix — the tools surface it.
2. **Slice, don't slurp.** Pull exactly the unit you're pointed to with `get_slice`. You hold one unit
   at a time.
3. **Edit, don't regenerate.** Repair with `propose_edit` — a surgical find/replace. Send only the
   change, never a regenerated chunk.

## The loop

Survey (`list_documents` → `get_batch_summary`) → `preprocess` a paper → the repair loop (the
orchestrator `dispatch`es leased *pointers* to workers; each worker `get_slice` → `propose_edit` /
restructure → reports; the orchestrator `apply`s the clean proposals) → `finalize` →
`review_document` → `publish`. You hold nothing between iterations — the `.scratch/` artifacts are
your memory. A single document with no swarm is the same loop at depth 1: you are the worker.

Full detail — escalation paths and the per-corruption-type repair recipes — lives in
[mcp/PROCEDURE.md](mcp/PROCEDURE.md); the output format in
[mcp/docs/STANDARDS.md](mcp/docs/STANDARDS.md).

> Portfolio-snapshot note: the server is self-contained (PowerShell 7+) but operates on an *ingestion
> root* you pass via `-Root`; no corpus is bundled here. See the companion `codex-scientiae`
> opusculum for sample outputs.
