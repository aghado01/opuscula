Set-Location 'd:\aghado01\codex-scientiae'
. ./src/md-cleanup.ps1
$files = @(
    'compendia/ph/MR2026.md',
    'compendia/ph/REF-MPH.md',
    'compendia/ph/STGW2024.md',
    'compendia/ph/GVPB2025.md',
    'compendia/ph/references/GVPB2025.md'
)
$results = foreach ($f in $files) {
    foreach ($r in (Find-MathClosureIssues -Path $f)) {
        [pscustomobject]@{ path = $f; line = $r.line; kind = $r.kind; issue = $r.issue; span = $r.span }
    }
}
$results | Format-Table path, line, kind, issue, span -AutoSize -Wrap
Write-Output "Total: $($results.Count)"
