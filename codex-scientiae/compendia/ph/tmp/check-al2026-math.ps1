. "$PSScriptRoot\..\..\src\md-cleanup.ps1"
$path = "$PSScriptRoot\..\AL2026.md"
$text = [IO.File]::ReadAllText($path) -replace "`r`n", "`n"
$nl = @([regex]::Matches($text, "`n") | ForEach-Object { $_.Index })
$csvLines = 486,730,1582,1807,1813,1831,1903,1925,2293,2327,2632,88
$rows = [System.Collections.Generic.List[object]]::new()
foreach ($m in [regex]::Matches($text, '(?s)\$\$(.+?)\$\$')) {
    $line = 1; foreach ($p in $nl) { if ($p -lt $m.Index) { $line++ } else { break } }
    if ($csvLines -contains $line) {
        $inner = $m.Groups[1].Value
        $b = Get-LatexBalance $inner
        $align = Test-AlignmentOutsideEnv $inner
        $math = Test-IsMath $inner
        $preview = ($inner -replace "`n", ' ').Substring(0, [Math]::Min(100, $inner.Length))
        $rows.Add([pscustomobject]@{ line = $line; full = $b.full; align = $align; math = $math; preview = $preview })
    }
}
$rows | Format-Table -AutoSize
