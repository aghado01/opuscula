#requires -Version 7.0
# Run the membrane's Pester 5 unit tests.
#   pwsh -File tests/run.ps1                                 # whole suite
#   pwsh -File tests/run.ps1 -Path tests/masks.Tests.ps1     # one file
param([string]$Path = $PSScriptRoot)

$pester = Get-Module -ListAvailable Pester | Where-Object { $_.Version -ge [version]'5.0' } | Select-Object -First 1
if (-not $pester) { Write-Error 'Pester 5+ is required:  Install-Module Pester -MinimumVersion 5.0'; exit 2 }
Import-Module $pester.Path -Force

$cfg = New-PesterConfiguration
$cfg.Run.Path = $Path
$cfg.Run.Exit = $true            # non-zero on any failure (CI-friendly)
$cfg.Output.Verbosity = 'Detailed'
Invoke-Pester -Configuration $cfg
