; ===============================================
; エラースクリーンショット管理システム 最終版
; ===============================================

#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

; グローバル変数
WSL_DISTRO := "Ubuntu"
WSL_BASE_PATH := "/home/futaro/screenshots/errors"
LAST_CATEGORY := "OTHER"

; ===============================================
; メインホットキー
; ===============================================

; F9: エラースクショを分類付きで保存
F9::
    ShowCategoryMenu()
return

; F10: 前回と同じカテゴリで即座保存
F10::
    SaveErrorScreenshot(LAST_CATEGORY)
return

; F11: 今日のエラー一覧を開く
F11::
    OpenTodayErrors()
return

; ===============================================
; 関数定義
; ===============================================

ShowCategoryMenu() {
    ; クリップボードチェック（メニュー表示前に）
    if (!Clipboard || !DllCall("IsClipboardFormatAvailable", "uint", 2)) {
        MsgBox, 48, Error, No image in clipboard!`n`nPlease take a screenshot first.
        return
    }
    
    Menu, CategoryMenu, Add
    Menu, CategoryMenu, DeleteAll
    
    Menu, CategoryMenu, Add, 🔴 API Error (1), MenuHandler
    Menu, CategoryMenu, Add, 🏗️ Build Error (2), MenuHandler  
    Menu, CategoryMenu, Add, ⚡ Runtime Error (3), MenuHandler
    Menu, CategoryMenu, Add, 🎨 UI Bug (4), MenuHandler
    Menu, CategoryMenu, Add, 🧪 Test Failure (5), MenuHandler
    Menu, CategoryMenu, Add, ❓ Other (6), MenuHandler
    
    Menu, CategoryMenu, Show
}

MenuHandler:
    if InStr(A_ThisMenuItem, "API Error")
        SaveErrorScreenshot("API_ERROR")
    else if InStr(A_ThisMenuItem, "Build Error")
        SaveErrorScreenshot("BUILD_ERROR")
    else if InStr(A_ThisMenuItem, "Runtime Error")
        SaveErrorScreenshot("RUNTIME_ERROR")
    else if InStr(A_ThisMenuItem, "UI Bug")
        SaveErrorScreenshot("UI_BUG")
    else if InStr(A_ThisMenuItem, "Test Failure")
        SaveErrorScreenshot("TEST_FAIL")
    else
        SaveErrorScreenshot("OTHER")
return

SaveErrorScreenshot(category) {
    LAST_CATEGORY := category
    
    ; タイムスタンプ生成
    FormatTime, DateFolder, , yyyy-MM-dd
    FormatTime, TimeStamp, , HH-mm-ss
    
    ; 一時ファイル名
    TempPNG := A_Temp . "\temp_screenshot.png"
    
    ; PowerShellで画像を一時保存
    PSCommand := "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; if ([System.Windows.Forms.Clipboard]::ContainsImage()) { $image = [System.Windows.Forms.Clipboard]::GetImage(); $image.Save('" . TempPNG . "', [System.Drawing.Imaging.ImageFormat]::Png); Write-Host 'OK' } else { Write-Host 'NOIMAGE' }"
    
    RunWait, powershell.exe -Command "%PSCommand%", , Hide
    
    if (!FileExist(TempPNG)) {
        MsgBox, 48, Error, Failed to save screenshot from clipboard.
        return
    }
    
    ; WSL側のパス構築
    FolderName := TimeStamp . "_" . category
    WSLFullPath := WSL_BASE_PATH . "/" . DateFolder . "/" . FolderName
    
    ; WSLでディレクトリ作成
    CreateDirCmd := "mkdir -p '" . WSLFullPath . "'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CreateDirCmd%", , Hide
    
    ; Windows一時ファイルをWSLにコピー
    TempUnixPath := ConvertToWSLPath(TempPNG)
    CopyCmd := "cp '" . TempUnixPath . "' '" . WSLFullPath . "/screenshot.png'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CopyCmd%", , Hide
    
    ; context.txt作成
    FormatTime, CurrentTime, , yyyy-MM-dd HH:mm:ss
    WinGetActiveTitle, ActiveWindow
    
    ContextContent := "Error Time: " . CurrentTime . "`nCategory: " . category . "`nActive Window: " . ActiveWindow
    
    TempContext := A_Temp . "\temp_context.txt"
    FileDelete, %TempContext%
    FileAppend, %ContextContent%, %TempContext%, UTF-8
    
    TempContextPath := ConvertToWSLPath(TempContext)
    ContextCopyCmd := "cp '" . TempContextPath . "' '" . WSLFullPath . "/context.txt'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%ContextCopyCmd%", , Hide
    
    ; 一時ファイル削除
    FileDelete, %TempPNG%
    FileDelete, %TempContext%
    
    ; 通知
    TrayTip, Screenshot Saved, %category%: %FolderName%, 3
    SoundBeep, 1000, 100
    SoundBeep, 1200, 100
}

ConvertToWSLPath(windowsPath) {
    unixPath := StrReplace(windowsPath, "\", "/")
    unixPath := StrReplace(unixPath, "C:", "/mnt/c")
    unixPath := StrReplace(unixPath, "D:", "/mnt/d")
    return unixPath
}

OpenTodayErrors() {
    FormatTime, DateFolder, , yyyy-MM-dd
    Run, explorer.exe "\\wsl$\%WSL_DISTRO%%WSL_BASE_PATH%\%DateFolder%"
}

; ===============================================
; 数字キーショートカット（メニュー表示中）
; ===============================================

#IfWinActive, ahk_class #32768
1::SaveErrorScreenshot("API_ERROR")
2::SaveErrorScreenshot("BUILD_ERROR")
3::SaveErrorScreenshot("RUNTIME_ERROR")
4::SaveErrorScreenshot("UI_BUG")
5::SaveErrorScreenshot("TEST_FAIL")
6::SaveErrorScreenshot("OTHER")
#IfWinActive

; ===============================================
; 起動時設定
; ===============================================

; システムトレイ設定
Menu, Tray, Icon, shell32.dll, 110
Menu, Tray, Tip, Error Screenshot Manager (Final)

; 起動完了メッセージ
Sleep, 200
MsgBox, 64, Error Screenshot Manager, 
(
Ready for ClaudeCode!

Hotkeys:
F9  : Category menu (take screenshot first!)
F10 : Quick save (same category)
F11 : Open today's errors

Usage:
1. Take screenshot (PrintScreen)
2. Press F9 → Select category
3. Screenshots saved to WSL automatically

WSL Path: %WSL_BASE_PATH%
)