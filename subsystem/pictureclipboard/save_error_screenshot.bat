@echo off
echo Starting Error Screenshot Manager...

REM Windows側の一時ディレクトリにスクリプトをコピー
set SCRIPT_DIR=%TEMP%\error_screenshot_temp
if not exist "%SCRIPT_DIR%" mkdir "%SCRIPT_DIR%"

REM WSLからWindowsにファイルコピー
wsl.exe -d Ubuntu -- cp "/home/futaro/project/StatVizForge_JikkenPy/subsystem/pictureclipboard/error_screenshot.ps1" "/mnt/c/Users/%USERNAME%/AppData/Local/Temp/error_screenshot_temp/error_screenshot.ps1"

REM PowerShell実行
cd /d "%SCRIPT_DIR%"
powershell.exe -ExecutionPolicy Bypass -File "error_screenshot.ps1"

REM 一時ファイル削除
del "%SCRIPT_DIR%\error_screenshot.ps1" 2>nul

pause