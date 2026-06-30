# codex-membrane

A pure-PowerShell MCP server that repairs machine-extracted scientific PDFs into faithful,
LaTeX-consistent markdown. It takes the JSON intermediate representation a PDF converter emits
(`docling` / `opendataloader-pdf`, hybrid math-enrichment mode) and drives a "seeing" agent and its
sub-agent swarm to resolve what the deterministic pass cannot — chunk by chunk, against an audited
work-list.

> **Draft / functional.** Validated end-to-end over the wire on struct-tree and non-struct-tree
> papers; not production-certified, and outputs may still carry warts (table handling is the next
> piece). Written natively in PowerShell — portable to pure Python. Depends on `opendataloader-pdf`
> (hybrid docling backend) to produce the controlled input; it's named in `requirements.txt` as the
> honest prerequisite for reproducing a run.
>
> This is a snapshot vignette for portfolio review — one of two opuscula under the parent `opuscula/`.
> Its companion, `codex-scientiae`, is a sample of the corpus this pipeline produces.

## The shape

```
raw {slug}.json                                        deliverable
  │  preprocess (8 deterministic stages)                 ▲  finalize
  ▼                                                      │
.scratch/{slug}.chunks.jsonl  ──►  membrane MCP  ──►  {slug}.md + references/
   (graded chunk stream)            (a seeing agent)     (LaTeX-consistent markdown)
```

The **preprocess** pipeline is deterministic — `project-ir → headings → collapse → zones → sections →
normalize → fidelity → repair` — and lands an enriched, per-chunk *graded* stream (a fidelity signal
locating the hardest regions) beside the source. The **membrane** is the MCP surface a seeing agent
drives to resolve what's left; **finalize**/**publish** assemble and promote the deliverable.

## The discipline

- **Navigate → slice → edit → proofread.** Most tools return metadata + pointers; content comes back
  only where content is the point. The orchestrator stays body-blind — it reasons over the work-list,
  not the prose.
- **Artifacts are ground truth.** State lives in the `.scratch/` artifacts (the chunk stream, plus a
  ledger, inventory, and audit), not the process — an amnesic agent re-grounds from a projection and
  resumes.
- **Anti-clobber by construction.** Repairs are per-chunk proposals, leased before work and folded in
  only when clean; every pre-image is kept.

## Layout

```
mcp/
  mcp-server.ps1   entry — pure PowerShell + .NET regex, self-contained via $PSScriptRoot
  PROCEDURE.md     the agent workflow, served as the restoration_procedure prompt
  server/          serving — projections, discovery
  preprocess/      the 8-stage deterministic pipeline (+ masks, enrichment)
  repair/          md-repair · md-cleanup · restructure · playbook (repair recipes-as-data)
  deliver/         finalize · publish
  oracle/          latex · latex-ingest — deterministic arXiv-LaTeX-source → markdown
                   (LaTeX is already structured, so math passes through verbatim; no agent, no repair)
  lib/             jsonl · crawl — local filesystem utilities
  docs/            SETUP · STANDARDS · WORKFLOW · CHECKLIST
```

## Docs

- [mcp/PROCEDURE.md](mcp/PROCEDURE.md) — the agent's restoration workflow (the canonical loop).
- [mcp/docs/SETUP.md](mcp/docs/SETUP.md) — wiring the MCP to a client.
- [mcp/docs/STANDARDS.md](mcp/docs/STANDARDS.md) — the markdown / LaTeX output format.
- [mcp/docs/WORKFLOW.md](mcp/docs/WORKFLOW.md) · [mcp/docs/CHECKLIST.md](mcp/docs/CHECKLIST.md) —
  repair strategy and the finalize audit.
