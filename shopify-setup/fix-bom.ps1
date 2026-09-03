$path = "C:\Users\JESOA TOMPO\.cline\data\workspaces\chat\shopify-theme\templates\index.json"
$text = [System.IO.File]::ReadAllText($path)
# Supprimer le BOM eventuel
if ($text.Length -gt 0 -and [int][char]$text[0] -eq 0xFEFF) {
    $text = $text.Substring(1)
}
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($path, $text, $utf8NoBom)
Write-Output "BOM_REMOVED"
