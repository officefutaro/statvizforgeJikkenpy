# ===============================================
# エラースクリーンショット管理システム PowerShell版
# ===============================================

param(
    [string]$Category = ""
)

# 設定
$WSL_DISTRO = "Ubuntu"
$WSL_BASE_PATH = "/home/futaro/screenshots/errors"

# カテゴリ選択関数
function Show-CategoryMenu {
    $categories = @{
        "1" = "API_ERROR"
        "2" = "BUILD_ERROR" 
        "3" = "RUNTIME_ERROR"
        "4" = "UI_BUG"
        "5" = "TEST_FAIL"
        "6" = "OTHER"
    }
    
    Write-Host "`n=== Error Screenshot Manager ===" -ForegroundColor Cyan
    Write-Host "Select category:" -ForegroundColor Yellow
    Write-Host "1. API Error (404, 500, CORS)" -ForegroundColor White
    Write-Host "2. Build Error (compile, npm)" -ForegroundColor White
    Write-Host "3. Runtime Error (exceptions)" -ForegroundColor White
    Write-Host "4. UI Bug (layout, display)" -ForegroundColor White
    Write-Host "5. Test Failure" -ForegroundColor White
    Write-Host "6. Other" -ForegroundColor White
    Write-Host ""
    
    do {
        $choice = Read-Host "Enter number (1-6)"
    } while ($choice -notmatch "^[1-6]$")
    
    return $categories[$choice]
}

# メイン処理
function Save-ErrorScreenshot {
    param([string]$Category)
    
    # クリップボードチェック
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    
    if (-not [System.Windows.Forms.Clipboard]::ContainsImage()) {
        Write-Host "❌ No image in clipboard! Please take a screenshot first." -ForegroundColor Red
        return
    }
    
    # タイムスタンプ生成
    $dateFolder = Get-Date -Format "yyyy-MM-dd"
    $timestamp = Get-Date -Format "HH-mm-ss"
    $folderName = "${timestamp}_${Category}"
    
    # 一時ファイル保存
    $tempPng = "$env:TEMP\temp_screenshot.png"
    $image = [System.Windows.Forms.Clipboard]::GetImage()
    $image.Save($tempPng, [System.Drawing.Imaging.ImageFormat]::Png)
    
    Write-Host "📷 Screenshot captured..." -ForegroundColor Green
    
    # WSL側パス構築
    $wslFullPath = "${WSL_BASE_PATH}/${dateFolder}/${folderName}"
    
    # WSLディレクトリ作成
    $createCmd = "mkdir -p '$wslFullPath'"
    wsl.exe -d $WSL_DISTRO -- bash -c $createCmd
    
    # Windows → WSL パス変換
    $tempUnixPath = $tempPng -replace "\\", "/" -replace "C:", "/mnt/c" -replace "D:", "/mnt/d"
    
    # ファイルコピー
    $copyCmd = "cp '$tempUnixPath' '$wslFullPath/screenshot.png'"
    wsl.exe -d $WSL_DISTRO -- bash -c $copyCmd
    
    # context.txt作成
    $currentTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $activeWindow = (Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | Select-Object -First 1).MainWindowTitle
    
    $contextContent = @"
Error Time: $currentTime
Category: $Category
Active Window: $activeWindow
System: Windows + WSL2
"@
    
    $tempContext = "$env:TEMP\temp_context.txt"
    $contextContent | Out-File -FilePath $tempContext -Encoding UTF8
    
    $tempContextPath = $tempContext -replace "\\", "/" -replace "C:", "/mnt/c" -replace "D:", "/mnt/d"
    $contextCopyCmd = "cp '$tempContextPath' '$wslFullPath/context.txt'"
    wsl.exe -d $WSL_DISTRO -- bash -c $contextCopyCmd
    
    # README.md作成
    $categoryDesc = switch ($Category) {
        "API_ERROR" { "API Error (404, 500, CORS)" }
        "BUILD_ERROR" { "Build/Compile Error" }
        "RUNTIME_ERROR" { "Runtime Error/Exception" }
        "UI_BUG" { "UI Bug/Layout Issue" }
        "TEST_FAIL" { "Test Failure" }
        default { "Other Error" }
    }
    
    $readmeContent = @"
# Error: $Category

## Time
$currentTime

## Category
$categoryDesc

## Screenshot
![Error](./screenshot.png)

## Status
- [ ] Investigating
- [ ] Fixing
- [ ] Fixed
- [ ] Tested

## Notes
(Add details here)
"@
    
    $readmeCmd = "echo '$readmeContent' > '$wslFullPath/README.md'"
    wsl.exe -d $WSL_DISTRO -- bash -c $readmeCmd
    
    # 一時ファイル削除
    Remove-Item $tempPng -ErrorAction SilentlyContinue
    Remove-Item $tempContext -ErrorAction SilentlyContinue
    
    # 完了通知
    Write-Host "✅ Screenshot saved to: $folderName" -ForegroundColor Green
    [System.Media.SystemSounds]::Asterisk.Play()
    
    # フォルダを開く
    $windowsPath = "\\wsl$\$WSL_DISTRO$WSL_BASE_PATH\$dateFolder"
    Start-Process explorer.exe -ArgumentList $windowsPath
}

# メイン実行
if ($Category -eq "") {
    $Category = Show-CategoryMenu
}

Save-ErrorScreenshot -Category $Category