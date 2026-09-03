$f = "C:\Users\JESOA TOMPO\.cline\data\workspaces\chat\shopify-theme\templates\index.json"
$lines = [System.Collections.Generic.List[string]](Get-Content $f)

# Trouver les bornes de la section featured-product
$start = -1; $end = -1
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '"featured-product"') { $start = $i }
    if ($start -ge 0 -and $lines[$i] -match '"image-banner"') { $end = $i; break }
}
Write-Output "START=$start END=$end"
if ($start -lt 0 -or $end -lt 0) { Write-Output "MARKERS_NOT_FOUND"; exit 1 }

# Supprimer le bloc featured-product (de START jusqu'a la ligne avant image-banner)
$lines.RemoveRange($start, $end - $start)

# Nouveau bloc featured-collection
$new = [System.Collections.Generic.List[string]]@(
'    "featured-collection": {',
'      "type": "featured-collection",',
'      "settings": {',
'        "title": "Nouveautes",',
'        "heading_size": "h2",',
'        "description": "<p>Notre selection du moment</p>",',
'        "show_description": true,',
'        "description_style": "subtitle",',
'        "collection": "nouveautes",',
'        "products_to_show": 4,',
'        "columns_desktop": 4,',
'        "columns_mobile": "2",',
'        "swipe_on_mobile": true,',
'        "enable_desktop_slider": false,',
'        "full_width": false,',
'        "show_view_all": true,',
'        "view_all_style": "solid",',
'        "color_scheme": "scheme-1",',
'        "image_ratio": "adapt",',
'        "padding_top": 36,',
'        "padding_bottom": 36',
'      }',
'    },'
)
$lines.InsertRange($start, $new)

# Mettre a jour l'ordre des sections
for ($i = 0; $i -lt $lines.Count; $i++) {
    $lines[$i] = $lines[$i] -replace '"featured-product",', '"featured-collection",'
}

Set-Content -Path $f -Value $lines -Encoding UTF8
Write-Output "DONE"