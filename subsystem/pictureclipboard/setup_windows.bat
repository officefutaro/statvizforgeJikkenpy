@echo off
echo Setting up Error Screenshot Manager on Windows side...

REM Windowsデスクトップにファイル作成
set DESKTOP=%USERPROFILE%\Desktop
set SCRIPT_NAME=ErrorScreenshotManager

echo Creating PowerShell script on Desktop...

(
echo # Error Screenshot Manager - Windows Version
echo param^([string]$Category = ""^)
echo.
echo # Configuration
echo $WSL_DISTRO = "Ubuntu"
echo $WSL_BASE_PATH = "/home/futaro/screenshots/errors"
echo.
echo # Category Selection
echo function Show-CategoryMenu {
echo     $categories = @{
echo         "1" = "API_ERROR"
echo         "2" = "BUILD_ERROR"
echo         "3" = "RUNTIME_ERROR"
echo         "4" = "UI_BUG"
echo         "5" = "TEST_FAIL"
echo         "6" = "OTHER"
echo     }
echo.
echo     Write-Host "`n=== Error Screenshot Manager ===" -ForegroundColor Cyan
echo     Write-Host "Take screenshot first, then select category:" -ForegroundColor Yellow
echo     Write-Host "1. API Error (404, 500, CORS^)" -ForegroundColor White
echo     Write-Host "2. Build Error (compile, npm^)" -ForegroundColor White
echo     Write-Host "3. Runtime Error (exceptions^)" -ForegroundColor White
echo     Write-Host "4. UI Bug (layout, display^)" -ForegroundColor White
echo     Write-Host "5. Test Failure" -ForegroundColor White
echo     Write-Host "6. Other" -ForegroundColor White
echo     Write-Host ""
echo.
echo     do {
echo         $choice = Read-Host "Enter number (1-6^)"
echo     } while ($choice -notmatch "^^[1-6]$"^)
echo.
echo     return $categories[$choice]
echo }
echo.
echo # Main Function
echo function Save-ErrorScreenshot {
echo     param^([string]$Category^)
echo.
echo     Add-Type -AssemblyName System.Windows.Forms
echo     Add-Type -AssemblyName System.Drawing
echo.
echo     if ^(-not [System.Windows.Forms.Clipboard]::ContainsImage^(^)^) {
echo         Write-Host "❌ No image in clipboard! Please take a screenshot first." -ForegroundColor Red
echo         Read-Host "Press Enter to exit"
echo         return
echo     }
echo.
echo     $dateFolder = Get-Date -Format "yyyy-MM-dd"
echo     $timestamp = Get-Date -Format "HH-mm-ss"
echo     $folderName = "${timestamp}_${Category}"
echo.
echo     $tempPng = "$env:TEMP\temp_screenshot.png"
echo     $image = [System.Windows.Forms.Clipboard]::GetImage^(^)
echo     $image.Save^($tempPng, [System.Drawing.Imaging.ImageFormat]::Png^)
echo.
echo     Write-Host "📷 Screenshot captured..." -ForegroundColor Green
echo.
echo     $wslFullPath = "${WSL_BASE_PATH}/${dateFolder}/${folderName}"
echo.
echo     $createCmd = "mkdir -p '$wslFullPath'"
echo     wsl.exe -d $WSL_DISTRO -- bash -c $createCmd
echo.
echo     $tempUnixPath = $tempPng -replace "\\", "/" -replace "C:", "/mnt/c"
echo     $copyCmd = "cp '$tempUnixPath' '$wslFullPath/screenshot.png'"
echo     wsl.exe -d $WSL_DISTRO -- bash -c $copyCmd
echo.
echo     $currentTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
echo     $contextContent = "Error Time: $currentTime`nCategory: $Category`nSystem: Windows + WSL2"
echo.
echo     $tempContext = "$env:TEMP\temp_context.txt"
echo     $contextContent ^| Out-File -FilePath $tempContext -Encoding UTF8
echo.
echo     $tempContextPath = $tempContext -replace "\\", "/" -replace "C:", "/mnt/c"
echo     $contextCopyCmd = "cp '$tempContextPath' '$wslFullPath/context.txt'"
echo     wsl.exe -d $WSL_DISTRO -- bash -c $contextCopyCmd
echo.
echo     Remove-Item $tempPng -ErrorAction SilentlyContinue
echo     Remove-Item $tempContext -ErrorAction SilentlyContinue
echo.
echo     Write-Host "✅ Screenshot saved: $folderName" -ForegroundColor Green
echo     [System.Media.SystemSounds]::Asterisk.Play^(^)
echo.
echo     $windowsPath = "\\wsl$\$WSL_DISTRO$WSL_BASE_PATH\$dateFolder"
echo     Start-Process explorer.exe -ArgumentList $windowsPath
echo }
echo.
echo # Execute
echo if ^($Category -eq ""^) {
echo     $Category = Show-CategoryMenu
echo }
echo Save-ErrorScreenshot -Category $Category
) > "%DESKTOP%\%SCRIPT_NAME%.ps1"

echo Creating batch launcher...
(
echo @echo off
echo echo Starting Error Screenshot Manager...
echo powershell.exe -ExecutionPolicy Bypass -File "%%~dp0%SCRIPT_NAME%.ps1"
echo pause
) > "%DESKTOP%\%SCRIPT_NAME%.bat"

echo.
echo ✅ Setup complete!
echo.
echo Files created on Desktop:
echo - %SCRIPT_NAME%.ps1 (main script)
echo - %SCRIPT_NAME%.bat (launcher)
echo.
echo Usage:
echo 1. Take screenshot (PrintScreen)
echo 2. Double-click %SCRIPT_NAME%.bat
echo 3. Select category (1-6)
echo.
pause