; ===============================================
; エラースクリーンショット管理システム 修正版
; AutoHotkey v1対応
; ===============================================

#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

; グローバル変数（v1対応）
WSL_DISTRO := "Ubuntu"
WSL_BASE_PATH := "/home/futaro/screenshots/errors"
LAST_CATEGORY := "OTHER"

; ===============================================
; メインホットキー
; ===============================================

; Win+Shift+E
#+e::
    ShowCategoryMenu()
return

; Ctrl+Shift+E
^+e::
    SaveErrorScreenshot(LAST_CATEGORY)
return

; Win+Alt+E
#!e::
    OpenTodayErrors()
return

; ===============================================
; 関数定義
; ===============================================

ShowCategoryMenu() {
    Menu, CategoryMenu, Add
    Menu, CategoryMenu, DeleteAll
    
    Menu, CategoryMenu, Add, API Error (1), MenuHandler
    Menu, CategoryMenu, Add, Build Error (2), MenuHandler
    Menu, CategoryMenu, Add, Runtime Error (3), MenuHandler
    Menu, CategoryMenu, Add, UI Bug (4), MenuHandler
    Menu, CategoryMenu, Add, Test Failure (5), MenuHandler
    Menu, CategoryMenu, Add, Other (6), MenuHandler
    
    Menu, CategoryMenu, Show
}

MenuHandler:
    if (A_ThisMenuItem = "API Error (1)")
        SaveErrorScreenshot("API_ERROR")
    else if (A_ThisMenuItem = "Build Error (2)")
        SaveErrorScreenshot("BUILD_ERROR")
    else if (A_ThisMenuItem = "Runtime Error (3)")
        SaveErrorScreenshot("RUNTIME_ERROR")
    else if (A_ThisMenuItem = "UI Bug (4)")
        SaveErrorScreenshot("UI_BUG")
    else if (A_ThisMenuItem = "Test Failure (5)")
        SaveErrorScreenshot("TEST_FAIL")
    else
        SaveErrorScreenshot("OTHER")
return

SaveErrorScreenshot(category) {
    ; クリップボードチェック
    if (!Clipboard || !DllCall("IsClipboardFormatAvailable", "uint", 2)) {
        MsgBox, 48, Error, No image in clipboard!`n`nPlease take a screenshot first.
        return
    }
    
    LAST_CATEGORY := category
    
    ; タイムスタンプ生成
    FormatTime, DateFolder, , yyyy-MM-dd
    FormatTime, TimeStamp, , HH-mm-ss
    
    ; 一時ファイル名
    TempPNG := A_Temp . "\temp_screenshot.png"
    
    ; PowerShellで画像を一時保存
    PSScript := "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; if ([System.Windows.Forms.Clipboard]::ContainsImage()) { $image = [System.Windows.Forms.Clipboard]::GetImage(); $image.Save('" . TempPNG . "', [System.Drawing.Imaging.ImageFormat]::Png); 'OK' } else { 'NOIMAGE' }"
    
    ; 一時ファイルに画像保存
    RunWait, powershell.exe -Command "%PSScript%", , Hide
    
    if (!FileExist(TempPNG)) {
        MsgBox, 48, Error, Failed to save screenshot from clipboard.
        return
    }
    
    ; WSL側のパス構築
    FolderName := TimeStamp . "_" . category
    WSLFullPath := WSL_BASE_PATH . "/" . DateFolder . "/" . FolderName
    
    ; WSLでディレクトリ作成
    CreateDirCmd := "mkdir -p '" . WSLFullPath . "'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CreateDirCmd%, , Hide
    
    ; Windows一時ファイルをWSLにコピー
    ; C:\Users\... を /mnt/c/Users/... に変換
    TempPath := StrReplace(TempPNG, "\", "/")
    TempPath := StrReplace(TempPath, "C:", "/mnt/c")
    TempPath := StrReplace(TempPath, "D:", "/mnt/d")
    
    CopyCmd := "cp '" . TempPath . "' '" . WSLFullPath . "/screenshot.png'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CopyCmd%, , Hide
    
    ; context.txt作成
    FormatTime, CurrentTime, , yyyy-MM-dd HH:mm:ss
    WinGetActiveTitle, ActiveWindow
    
    ContextContent := "Error Time: " . CurrentTime . "`nCategory: " . category . "`nActive Window: " . ActiveWindow
    
    ; 一時ファイルに書き込んでからWSLにコピー
    TempContext := A_Temp . "\temp_context.txt"
    FileDelete, %TempContext%
    FileAppend, %ContextContent%, %TempContext%, UTF-8
    
    TempContextPath := StrReplace(TempContext, "\", "/")
    TempContextPath := StrReplace(TempContextPath, "C:", "/mnt/c")
    TempContextPath := StrReplace(TempContextPath, "D:", "/mnt/d")
    
    ContextCopyCmd := "cp '" . TempContextPath . "' '" . WSLFullPath . "/context.txt'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %ContextCopyCmd%, , Hide
    
    ; 一時ファイル削除
    FileDelete, %TempPNG%
    FileDelete, %TempContext%
    
    ; 通知
    TrayTip, Screenshot Saved, %category% saved: %FolderName%, 3
    SoundBeep, 1000, 100
    SoundBeep, 1200, 100
}

OpenTodayErrors() {
    FormatTime, DateFolder, , yyyy-MM-dd
    
    ; WSL側でパス存在確認
    CheckCmd := "[ -d '" . WSL_BASE_PATH . "/" . DateFolder . "' ] && echo 'EXISTS' || echo 'NOTEXISTS'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CheckCmd%, Result, Hide
    
    if (InStr(Result, "EXISTS")) {
        ; Windows Explorerで開く
        Run, explorer.exe "\\wsl$\%WSL_DISTRO%%WSL_BASE_PATH%\%DateFolder%"
    } else {
        MsgBox, 64, Info, No errors captured today.
    }
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
Menu, Tray, Tip, Error Screenshot Manager (WSL Fixed)

; 初回起動メッセージ
MsgBox, 64, Error Screenshot Manager, 
(
Fixed Version Loaded!

Hotkeys:
Win+Shift+E : Save with category selection
Ctrl+Shift+E : Quick save (same category)
Win+Alt+E : Open today's errors

First, take a screenshot, then use hotkeys.
)