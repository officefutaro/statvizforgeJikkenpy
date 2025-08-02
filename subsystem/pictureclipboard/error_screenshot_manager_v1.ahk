; ===============================================
; エラースクリーンショット管理システム
; AutoHotkey v1.1.37 完全対応版
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

; Win+Shift+E: エラースクショを分類付きで保存
#+e::
    ShowCategoryMenu()
return

; Ctrl+Shift+E: 前回と同じカテゴリで即座保存
^+e::
    SaveErrorScreenshot(LAST_CATEGORY)
return

; Win+Alt+E: 今日のエラー一覧を開く
#!e::
    OpenTodayErrors()
return

; ===============================================
; 関数定義
; ===============================================

ShowCategoryMenu() {
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
    
    ; PowerShellで画像を一時保存（v1対応）
    PSCommand := "Add-Type -AssemblyName System.Windows.Forms; Add-Type -AssemblyName System.Drawing; if ([System.Windows.Forms.Clipboard]::ContainsImage()) { $image = [System.Windows.Forms.Clipboard]::GetImage(); $image.Save('" . TempPNG . "', [System.Drawing.Imaging.ImageFormat]::Png); Write-Host 'OK' } else { Write-Host 'NOIMAGE' }"
    
    ; 一時ファイルに画像保存
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
    ; パス変換処理
    TempUnixPath := ConvertToWSLPath(TempPNG)
    CopyCmd := "cp '" . TempUnixPath . "' '" . WSLFullPath . "/screenshot.png'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CopyCmd%", , Hide
    
    ; context.txt作成
    FormatTime, CurrentTime, , yyyy-MM-dd HH:mm:ss
    WinGetActiveTitle, ActiveWindow
    
    ContextContent := "Error Time: " . CurrentTime . "`nCategory: " . category . "`nActive Window: " . ActiveWindow . "`nSystem: Windows + WSL2"
    
    ; 一時ファイル作成
    TempContext := A_Temp . "\temp_context.txt"
    FileDelete, %TempContext%
    FileAppend, %ContextContent%, %TempContext%, UTF-8
    
    ; WSLにコピー
    TempContextPath := ConvertToWSLPath(TempContext)
    ContextCopyCmd := "cp '" . TempContextPath . "' '" . WSLFullPath . "/context.txt'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%ContextCopyCmd%", , Hide
    
    ; README.md作成
    CreateReadme(WSLFullPath, category, CurrentTime)
    
    ; 日付インデックス更新
    UpdateDailyIndex(DateFolder, FolderName, category)
    
    ; 一時ファイル削除
    FileDelete, %TempPNG%
    FileDelete, %TempContext%
    
    ; 通知
    TrayTip, Screenshot Saved, %category% saved:`n%FolderName%, 3
    SoundBeep, 1000, 100
    SoundBeep, 1200, 100
}

ConvertToWSLPath(windowsPath) {
    ; C:\Users\... を /mnt/c/Users/... に変換
    unixPath := StrReplace(windowsPath, "\", "/")
    unixPath := StrReplace(unixPath, "C:", "/mnt/c")
    unixPath := StrReplace(unixPath, "D:", "/mnt/d")
    unixPath := StrReplace(unixPath, "E:", "/mnt/e")
    return unixPath
}

CreateReadme(wslPath, category, timestamp) {
    categoryDesc := GetCategoryDescription(category)
    ReadmeContent := "# Error: " . category . "`n`n## Time`n" . timestamp . "`n`n## Category`n" . categoryDesc . "`n`n## Screenshot`n![Error](./screenshot.png)`n`n## Status`n- [ ] Investigating`n- [ ] Fixing`n- [ ] Fixed`n- [ ] Tested`n`n## Notes`n(Add details here)"
    
    ReadmeCmd := "echo '" . ReadmeContent . "' > '" . wslPath . "/README.md'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%ReadmeCmd%", , Hide
}

UpdateDailyIndex(dateFolder, folderName, category) {
    IndexPath := WSL_BASE_PATH . "/" . dateFolder . "/index.md"
    categoryDesc := GetCategoryDescription(category)
    IndexEntry := "- [" . folderName . "](./" . folderName . "/README.md) - " . categoryDesc
    
    ; index.md存在確認
    CheckCmd := "[ -f '" . IndexPath . "' ] && echo 'EXISTS' || echo 'NOTEXISTS'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CheckCmd%", Result, Hide
    
    if InStr(Result, "NOTEXISTS") {
        ; 新規作成
        IndexHeader := "# Errors: " . dateFolder . "`n`n## Today's Errors`n" . IndexEntry
        CreateCmd := "echo '" . IndexHeader . "' > '" . IndexPath . "'"
        RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CreateCmd%", , Hide
    } else {
        ; 追記
        AppendCmd := "echo '" . IndexEntry . "' >> '" . IndexPath . "'"
        RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%AppendCmd%", , Hide
    }
}

GetCategoryDescription(category) {
    if (category = "API_ERROR")
        return "API Error (404, 500, CORS)"
    else if (category = "BUILD_ERROR")
        return "Build/Compile Error"
    else if (category = "RUNTIME_ERROR")
        return "Runtime Error/Exception"
    else if (category = "UI_BUG")
        return "UI Bug/Layout Issue"
    else if (category = "TEST_FAIL")
        return "Test Failure"
    else
        return "Other Error"
}

OpenTodayErrors() {
    FormatTime, DateFolder, , yyyy-MM-dd
    
    ; WSL側でパス存在確認
    CheckCmd := "[ -d '" . WSL_BASE_PATH . "/" . DateFolder . "' ] && echo 'EXISTS' || echo 'NOTEXISTS'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CheckCmd%", Result, Hide
    
    if InStr(Result, "EXISTS") {
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

; WSL接続テスト
TestCmd := "echo 'WSL_TEST_OK'"
RunWait, wsl.exe -d %WSL_DISTRO% -- %TestCmd%, TestResult, Hide

if !InStr(TestResult, "WSL_TEST_OK") {
    MsgBox, 48, WSL Error, WSL connection failed!`n`nPlease check:`n1. WSL is installed`n2. Ubuntu distribution exists`n3. WSL is running
    ExitApp
}

; ベースディレクトリ作成
SetupCmd := "mkdir -p '" . WSL_BASE_PATH . "'"
RunWait, wsl.exe -d %WSL_DISTRO% -- %SetupCmd%, , Hide

; システムトレイ設定
Menu, Tray, Icon, shell32.dll, 110
Menu, Tray, Tip, Error Screenshot Manager (v1.1.37)
Menu, Tray, Add, Open Error Folder, OpenErrorFolder
Menu, Tray, Add
Menu, Tray, Add, Exit, ExitApp

OpenErrorFolder:
    Run, explorer.exe "\\wsl$\%WSL_DISTRO%%WSL_BASE_PATH%"
return

ExitApp:
ExitApp

; 初回起動メッセージ
if (!FileExist(A_ScriptDir . "\initialized.txt")) {
    FileAppend, initialized, %A_ScriptDir%\initialized.txt
    MsgBox, 64, Error Screenshot Manager v1.1.37, 
    (
Ready to capture errors!

Hotkeys:
Win+Shift+E : Category menu
Ctrl+Shift+E : Quick save
Win+Alt+E : Open today's errors

Usage:
1. Take screenshot (PrintScreen)
2. Win+Shift+E → Select category
3. Files saved to WSL automatically

WSL Path: %WSL_BASE_PATH%
    )
}