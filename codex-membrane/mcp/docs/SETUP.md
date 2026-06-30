# Wiring up the codex-membrane MCP

> How to register `mcp/mcp-server.ps1` with an MCP client (Claude Code) so an agent can drive the
> restoration workflow over the wire. See [the README](../../README.md) for what the system is.

## Prerequisites

- **PowerShell 7+** (`pwsh`). Nothing else — the server is pure PowerShell + .NET regex, self-contained
  via `$PSScriptRoot`.
- If `pwsh` is not on the client's `PATH` (e.g. a portable install), use the **absolute path** to
  `pwsh.exe` as the command instead of the bare name.
- An **ingestion root** to operate on. This portfolio snapshot bundles no corpus, so you supply one: a
  directory of raw `{slug}.json` IR exports (with their `.scratch/`), passed via `-Root`.

## The launch line

```
pwsh -NoProfile -File <repo>/mcp/mcp-server.ps1 -Root <path-to-ingestion>
```

- `-NoProfile` keeps the user profile off stdout (stdout carries JSON-RPC frames **only**; all logs go
  to stderr).
- **`-Root`** is the raw-input boundary the server surveys and repairs. (In the full private repo it
  derives automatically from a co-located `ingestion/`; in this standalone snapshot there is no bundled
  corpus, so pass it explicitly.) If the resolved root does not exist, the server **fails fast in the
  agent's feed**: `initialize` and `tools/list` still succeed (the agent comes up and can orient), but
  every `tools/call` returns an `isError` result carrying the diagnostic and the fix. The same line is
  logged `FATAL` to stderr for the operator.
- **Which subtree to survey is a per-call choice.** Every tool is paper-addressed and resolves papers
  by crawling the whole root, so the same server serves one paper or a whole batch. Narrow a survey
  with an optional `scope` argument on the call — nothing to bake into the registration.

### Runtime `scope` (narrowing a survey per call)

`list_documents`, `get_batch_summary`, and `dispatch` accept an optional `scope` string: a subtree
under the ingestion root to survey. Empty/absent = the whole root. It is path-normalized and confined
to the root (a scope escaping via `..` or an absolute path is rejected). The paper-addressed tools
(`get_summary`, `get_slice`, `propose_edit`, …) resolve papers by name across the whole root and need
no `scope`.

## Register with Claude Code

**Option A — project config (`.mcp.json`):**

```json
{
  "mcpServers": {
    "codex-membrane": {
      "command": "pwsh",
      "args": ["-NoProfile", "-File", "mcp/mcp-server.ps1", "-Root", "<path-to-ingestion>"]
    }
  }
}
```

Relative paths resolve from the project root. Use absolute paths if the client launches from a
different working directory, or if `pwsh` isn't on `PATH` (swap `"command"` for the full `pwsh.exe`
path).

**Option B — CLI:**

```
claude mcp add codex-membrane --scope project -- \
  pwsh -NoProfile -File mcp/mcp-server.ps1 -Root <path-to-ingestion>
```

## Verify

A clean wire-up answers `initialize` and lists the server's tools, logging one startup banner to
stderr:

```powershell
$server = '<repo>/mcp/mcp-server.ps1'
@(
 '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18"}}'
 '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
) | pwsh -NoProfile -File $server -Root <path-to-ingestion>
# expect: id=2 result.tools is populated; stderr: "codex-membrane MCP server up (root=...)"
```

The `initialize` reply also carries an **`instructions`** field — the server's discovery handshake. On
a healthy mount it reads `serving ingestion root '<root>' -- N document(s) discovered, M preprocessed
...`. `mounted but EMPTY -- 0 documents` means the root exists but holds no corpus; an `error: ...`
string means the root is unmounted. Clients inject this into the agent's context, so a misconfigured
root is visible at the handshake, not inferred from an empty survey.

## Notes

- **stdout is sacred** — protocol frames only. Anything else makes the client choke; that's what
  `-NoProfile` and the server's stderr-only logging protect.
- The server is **stateless**; restart it freely. All document state lives in the `.scratch/`
  artifacts under the ingestion root, so a fresh process resumes where the last left off.
- Hand off to **[../PROCEDURE.md](../PROCEDURE.md)** for the workflow (the `list_documents → preprocess
  → … → finalize → review_document` loop).
