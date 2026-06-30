# tests/

Pester 5 unit tests for the membrane — a ported subset that runs without a bundled corpus. Each file
dot-sources the module(s) under test from `../mcp/…`.

```pwsh
pwsh -File tests/run.ps1                                 # whole suite
pwsh -File tests/run.ps1 -Path tests/masks.Tests.ps1     # one file
```

| file | covers |
|---|---|
| `masks.Tests.ps1` | `mcp/preprocess/masks.ps1` — the closed mask-algebra: algebraic laws over random masks, totality, codepoint safety (SMP / surrogate pairs). |
| `detectors.Tests.ps1` | the math / alignment / gibberish / corruption-type detectors on fixed inputs, with reproduced bugs pinned as regressions. |
| `normalize.Tests.ps1` | `Optimize-MathContent` and `Invoke-MarkdownCleanup` — idempotency and tag/balance preservation. |
| `playbook-coverage.Tests.ps1` | the repair playbook carries a recipe for every corruption type the membrane can emit. |

Corpus-backed tests and the acquisition-lane tests from the source project are intentionally omitted
from this snapshot.
