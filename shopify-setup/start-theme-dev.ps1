$themeDir = 'C:\Users\JESOA TOMPO\.cline\data\workspaces\chat\shopify-theme'
$shopifyCmd = 'C:\Users\JESOA TOMPO\AppData\Roaming\npm\shopify.cmd'
$outLog = 'C:\Users\JESOA TOMPO\AppData\Local\Temp\theme-dev-final-out.log'
$errLog = 'C:\Users\JESOA TOMPO\AppData\Local\Temp\theme-dev-final-err.log'

Start-Process -FilePath $shopifyCmd -ArgumentList 'theme','dev','--store','pfd2zx-7h.myshopify.com','--store-password','lalyum' -WorkingDirectory $themeDir -RedirectStandardOutput $outLog -RedirectStandardError $errLog -WindowStyle Hidden

Write-Output "Theme dev started"
Start-Sleep -Seconds 5
Get-Content $errLog -Tail 10 -ErrorAction SilentlyContinue