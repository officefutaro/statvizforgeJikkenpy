; ===============================================
; エラースクリーンショット管理システム v2
; WSL環境対応版 - wsl.exe経由でファイル操作
; ===============================================

#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

; グローバル変数
global WSL_DISTRO := "Ubuntu"  ; 使用するWSLディストリビューション
global WSL_BASE_PATH := "/home/futaro/screenshots/errors"
global CATEGORIES := ["API_ERROR", "BUILD_ERROR", "RUNTIME_ERROR", "UI_BUG", "TEST_FAIL", "OTHER"]
global LAST_CATEGORY := "OTHER"

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

; Win+Alt+E: 今日のエラー一覧を開く（WSL経由）
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
    if (A_ThisMenuItem ~= "API Error")
        SaveErrorScreenshot("API_ERROR")
    else if (A_ThisMenuItem ~= "Build Error")
        SaveErrorScreenshot("BUILD_ERROR")
    else if (A_ThisMenuItem ~= "Runtime Error")
        SaveErrorScreenshot("RUNTIME_ERROR")
    else if (A_ThisMenuItem ~= "UI Bug")
        SaveErrorScreenshot("UI_BUG")
    else if (A_ThisMenuItem ~= "Test Failure")
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
    PSScript := "
    (
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    if ([System.Windows.Forms.Clipboard]::ContainsImage()) {
        $image = [System.Windows.Forms.Clipboard]::GetImage()
        $image.Save('%TempPNG%', [System.Drawing.Imaging.ImageFormat]::Png)
        'OK'
    } else {
        'NOIMAGE'
    }
    )"
    
    ; 一時ファイルに画像保存
    RunWait, powershell.exe -Command "%PSScript%", , Hide
    
    if (!FileExist(TempPNG)) {
        MsgBox, 48, Error, Failed to save screenshot from clipboard.
        return
    }
    
    ; WSL側のパス構築
    FolderName := TimeStamp . "_" . category
    WSLFullPath := WSL_BASE_PATH . "/" . DateFolder . "/" . FolderName
    
    ; WSLでディレクトリ作成とファイルコピー
    CreateDirCmd := "mkdir -p '" . WSLFullPath . "'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CreateDirCmd%, , Hide
    
    ; Windows側の一時ファイルをWSLにコピー
    ; wsl.exeの作業ディレクトリを考慮してパスを調整
    CopyCmd := "cp '/mnt/" . StrLower(SubStr(A_Temp, 1, 1)) . SubStr(A_Temp, 3) . "/temp_screenshot.png' '" . WSLFullPath . "/screenshot.png'"
    StringReplace, CopyCmd, CopyCmd, \, /, All
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CopyCmd%, , Hide
    
    ; context.txtを作成
    FormatTime, CurrentTime, , yyyy-MM-dd HH:mm:ss
    ActiveWindow := ""
    WinGetActiveTitle, ActiveWindow
    
    ContextContent := "エラー発生時刻: " . CurrentTime . "`n"
    ContextContent .= "カテゴリ: " . category . "`n"
    ContextContent .= "アクティブウィンドウ: " . ActiveWindow . "`n"
    
    ; context.txtをWSLに作成
    ContextCmd := "echo '" . ContextContent . "' > '" . WSLFullPath . "/context.txt'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%ContextCmd%", , Hide
    
    ; README.mdを作成
    ReadmeContent := "# エラー情報: " . category . "\n\n"
    ReadmeContent .= "## 発生時刻\n" . CurrentTime . "\n\n"
    ReadmeContent .= "## スクリーンショット\n![Error Screenshot](./screenshot.png)\n\n"
    ReadmeContent .= "## 対応状況\n- [ ] 原因調査中\n- [ ] 修正実施中\n- [ ] 修正完了\n- [ ] テスト確認済み\n\n"
    ReadmeContent .= "## メモ\n（ここにエラーの詳細や対応内容を記載）\n"
    
    ReadmeCmd := "echo '" . ReadmeContent . "' > '" . WSLFullPath . "/README.md'"
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%ReadmeCmd%", , Hide
    
    ; 日付インデックス更新
    IndexPath := WSL_BASE_PATH . "/" . DateFolder . "/index.md"
    IndexEntry := "- [" . FolderName . "](./" . FolderName . "/README.md) - " . GetCategoryDescription(category)
    
    ; index.mdが存在するかチェック
    CheckIndexCmd := "[ -f '" . IndexPath . "' ] && echo 'EXISTS' || echo 'NOTEXISTS'"
    IndexExists := ""
    RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CheckIndexCmd%", IndexExists, Hide
    
    if (InStr(IndexExists, "NOTEXISTS")) {
        ; 新規作成
        IndexHeader := "# エラー一覧: " . DateFolder . "\n\n## 本日のエラー\n"
        CreateIndexCmd := "echo '" . IndexHeader . IndexEntry . "' > '" . IndexPath . "'"
        RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%CreateIndexCmd%", , Hide
    } else {
        ; 追記
        AppendIndexCmd := "echo '" . IndexEntry . "' >> '" . IndexPath . "'"
        RunWait, wsl.exe -d %WSL_DISTRO% -- bash -c "%AppendIndexCmd%", , Hide
    }
    
    ; 一時ファイル削除
    FileDelete, %TempPNG%
    
    ; 通知
    TrayTip, Error Screenshot Saved, %category% saved to:`n%FolderName%, 3
    SoundBeep, 1000, 100
    SoundBeep, 1200, 100
}

GetCategoryDescription(category) {
    if (category = "API_ERROR")
        return "API通信エラー（404, 500, CORS等）"
    else if (category = "BUILD_ERROR")
        return "ビルド・コンパイルエラー"
    else if (category = "RUNTIME_ERROR")
        return "ランタイムエラー・例外"
    else if (category = "UI_BUG")
        return "UI表示不具合・レイアウト崩れ"
    else if (category = "TEST_FAIL")
        return "テスト失敗"
    else
        return "その他のエラー"
}

OpenTodayErrors() {
    ; WSL側のパスをWindows Explorerで開く
    FormatTime, DateFolder, , yyyy-MM-dd
    
    ; WSL側でパスが存在するか確認
    CheckCmd := "[ -d '" . WSL_BASE_PATH . "/" . DateFolder . "' ] && echo 'EXISTS' || echo 'NOTEXISTS'"
    Result := ""
    RunWait, wsl.exe -d %WSL_DISTRO% -- %CheckCmd%, Result, Hide
    
    if (InStr(Result, "EXISTS")) {
        ; Windows Explorerで開く（\\wsl$経由）
        Run, explorer.exe "\\wsl$\%WSL_DISTRO%%WSL_BASE_PATH%\%DateFolder%"
    } else {
        MsgBox, 64, Info, No errors captured today.
    }
}

; ===============================================
; 数字キーショートカット
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
; 起動時の初期設定
; ===============================================

; WSL側のディレクトリ作成
SetupCmd := "mkdir -p '" . WSL_BASE_PATH . "/categories' && echo 'OK'"
SetupResult := ""
RunWait, wsl.exe -d %WSL_DISTRO% -- %SetupCmd%, SetupResult, Hide

if (!InStr(SetupResult, "OK")) {
    MsgBox, 48, Setup Error, Failed to create WSL directories.`n`nPlease check WSL is running and accessible.
    ExitApp
}

; システムトレイ設定
Menu, Tray, Icon, shell32.dll, 110
Menu, Tray, Tip, Error Screenshot Manager (WSL)
Menu, Tray, Add, Open Error Folder, OpenErrorFolder
Menu, Tray, Add
Menu, Tray, Add, Exit, ExitApp

OpenErrorFolder:
    Run, explorer.exe "\\wsl$\%WSL_DISTRO%%WSL_BASE_PATH%"
return

ExitApp:
ExitApp

; 初回起動時のヘルプ
if (!FileExist(A_ScriptDir . "\initialized.txt")) {
    FileAppend, initialized, %A_ScriptDir%\initialized.txt
    MsgBox, 64, Error Screenshot Manager (WSL), 
    (
WSL対応版 - 使用方法:
    
Win+Shift+E : カテゴリ選択してスクショ保存
Ctrl+Shift+E : 前回と同じカテゴリで即保存
Win+Alt+E : 今日のエラー一覧を開く

保存先: %WSL_BASE_PATH% (WSL側)

カテゴリ選択時は数字キーも使用可能:
1: API Error
2: Build Error  
3: Runtime Error
4: UI Bug
5: Test Failure
6: Other
    )
}