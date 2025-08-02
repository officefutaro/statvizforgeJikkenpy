; デバッグ用段階的テスト
#NoEnv
#SingleInstance Force

; 変数テスト
WSL_DISTRO := "Ubuntu"
WSL_BASE_PATH := "/home/futaro/screenshots/errors"

; Step 1: 基本動作テスト
#+1::
    MsgBox, 64, Step 1, Variables loaded OK!`nWSL_DISTRO: %WSL_DISTRO%`nWSL_BASE_PATH: %WSL_BASE_PATH%
return

; Step 2: WSL接続テスト
#+2::
    MsgBox, 64, Step 2, Testing WSL connection...
    RunWait, wsl.exe -d %WSL_DISTRO% -- echo "WSL_OK", Result, Hide
    MsgBox, 64, WSL Result, Result: %Result%
return

; Step 3: WSLディレクトリ作成テスト
#+3::
    MsgBox, 64, Step 3, Creating WSL directory...
    SetupCmd := "mkdir -p '" . WSL_BASE_PATH . "'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %SetupCmd%, Result, Hide
    MsgBox, 64, Directory Created, Command: %SetupCmd%`nResult: %Result%
return

; Step 4: クリップボードテスト
#+4::
    if (!Clipboard || !DllCall("IsClipboardFormatAvailable", "uint", 2)) {
        MsgBox, 48, Step 4, No image in clipboard
    } else {
        MsgBox, 64, Step 4, Image found in clipboard!
    }
return

; Step 5: PowerShellテスト
#+5::
    TempPNG := A_Temp . "\debug_screenshot.png"
    PSCommand := "Add-Type -AssemblyName System.Windows.Forms; Write-Host 'PowerShell OK'"
    RunWait, powershell.exe -Command "%PSCommand%", Result, Hide
    MsgBox, 64, Step 5, PowerShell test`nResult: %Result%
return

MsgBox, 64, Debug Tool, 
(
Debug Steps:
Win+Shift+1 : Variable test
Win+Shift+2 : WSL connection test  
Win+Shift+3 : WSL directory test
Win+Shift+4 : Clipboard test (take screenshot first)
Win+Shift+5 : PowerShell test

Run each step to find where the error occurs.
)