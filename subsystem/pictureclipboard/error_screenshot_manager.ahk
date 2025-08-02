; ===============================================
; エラースクリーンショット管理システム
; ClaudeCode連携用 - 開発エラーの即座保存
; ===============================================

#NoEnv
#SingleInstance Force
SendMode Input
SetWorkingDir %A_ScriptDir%

; グローバル変数
global WSL_USERNAME := "futaro"
global WSL_DISTRO := "Ubuntu"  ; WSLディストリビューション名（wsl -l で確認）
global WSL_BASE_PATH := "/home/" . WSL_USERNAME . "/screenshots/errors"
global TEMP_SAVE_PATH := A_Temp . "\error_screenshots"  ; Windows側一時保存先
global CATEGORIES := ["API_ERROR", "BUILD_ERROR", "RUNTIME_ERROR", "UI_BUG", "TEST_FAIL", "OTHER"]
global LAST_CATEGORY := "OTHER"

; ===============================================
; メインホットキー
; ===============================================

; Win+Shift+E: エラースクショを分類付きで保存
#+e::
    ShowCategoryMenu()
return

; Ctrl+Shift+E: 前回と同じカテゴリで即座保存（連続エラー用）
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
    ; カテゴリ選択メニュー表示
    Menu, CategoryMenu, Add
    Menu, CategoryMenu, DeleteAll
    
    Menu, CategoryMenu, Add, 🔴 API Error (1), MenuHandler
    Menu, CategoryMenu, Add, 🏗️ Build Error (2), MenuHandler
    Menu, CategoryMenu, Add, ⚡ Runtime Error (3), MenuHandler
    Menu, CategoryMenu, Add, 🎨 UI Bug (4), MenuHandler
    Menu, CategoryMenu, Add, 🧪 Test Failure (5), MenuHandler
    Menu, CategoryMenu, Add, ❓ Other (6), MenuHandler
    Menu, CategoryMenu, Add
    Menu, CategoryMenu, Add, 📁 Open Error Folder, OpenErrorFolder
    
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
    ; クリップボードに画像があるか確認
    if (!Clipboard || !DllCall("IsClipboardFormatAvailable", "uint", 2)) {
        MsgBox, 48, Error, No image in clipboard!`n`nPlease take a screenshot first.
        return
    }
    
    ; カテゴリを記憶
    LAST_CATEGORY := category
    
    ; タイムスタンプ生成
    FormatTime, DateFolder, , yyyy-MM-dd
    FormatTime, TimeStamp, , HH-mm-ss
    
    ; フォルダ名とパス生成
    FolderName := TimeStamp . "_" . category
    FullPath := WSL_BASE_PATH . "\" . DateFolder . "\" . FolderName
    
    ; PowerShellスクリプトを生成して実行
    PSScript := GeneratePowerShellScript(FullPath, category)
    
    ; 一時ファイルに保存
    TempFile := A_Temp . "\save_error_screenshot.ps1"
    FileDelete, %TempFile%
    FileAppend, %PSScript%, %TempFile%, UTF-8
    
    ; PowerShell実行
    RunWait, powershell.exe -ExecutionPolicy Bypass -File "%TempFile%",, Hide
    
    ; 通知
    TrayTip, Error Screenshot Saved, %category% error saved to:`n%FolderName%, 3
    
    ; サウンド
    SoundBeep, 1000, 100
    SoundBeep, 1200, 100
}

GeneratePowerShellScript(fullPath, category) {
    ; WSL用のパスに変換
    StringReplace, wslPath, fullPath, \, /, All
    
    script := "
(
# エラースクリーンショット保存スクリプト
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# エラーカテゴリ説明
$categoryDescriptions = @{
    'API_ERROR' = 'API通信エラー（404, 500, CORS等）'
    'BUILD_ERROR' = 'ビルド・コンパイルエラー'
    'RUNTIME_ERROR' = 'ランタイムエラー・例外'
    'UI_BUG' = 'UI表示不具合・レイアウト崩れ'
    'TEST_FAIL' = 'テスト失敗'
    'OTHER' = 'その他のエラー'
}

# Windows側一時ディレクトリ作成
$tempPath = '%TEMP_SAVE_PATH%\%category%_' + (Get-Date -Format 'yyyyMMdd_HHmmss')
New-Item -ItemType Directory -Path $tempPath -Force | Out-Null

# 画像保存（まずWindows側に）
if ([System.Windows.Forms.Clipboard]::ContainsImage()) {
    $image = [System.Windows.Forms.Clipboard]::GetImage()
    $imagePath = Join-Path $tempPath 'screenshot.png'
    $image.Save($imagePath, [System.Drawing.Imaging.ImageFormat]::Png)
    
    # コンテキスト情報収集
    $context = @"
エラー発生時刻: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
カテゴリ: %category%
説明: $($categoryDescriptions['%category%'])

アクティブウィンドウ: $(Get-Process | Where-Object {$_.MainWindowTitle -ne ''} | Select-Object -First 1 -ExpandProperty MainWindowTitle)

システム情報:
- OS: $([System.Environment]::OSVersion.VersionString)
- PowerShell: $($PSVersionTable.PSVersion)
- 実行ユーザー: $env:USERNAME
"@
    
    # context.txt保存
    $contextPath = Join-Path $path 'context.txt'
    $context | Out-File -FilePath $contextPath -Encoding UTF8
    
    # README.md作成
    $readme = @"
# エラー情報: %category%

## 発生時刻
$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

## カテゴリ
$($categoryDescriptions['%category%'])

## スクリーンショット
![Error Screenshot](./screenshot.png)

## 対応状況
- [ ] 原因調査中
- [ ] 修正実施中
- [ ] 修正完了
- [ ] テスト確認済み

## メモ
（ここにエラーの詳細や対応内容を記載）

"@
    
    $readmePath = Join-Path $path 'README.md'
    $readme | Out-File -FilePath $readmePath -Encoding UTF8
    
    # 日付インデックス更新
    $dateFolder = Split-Path $path -Parent
    $indexPath = Join-Path $dateFolder 'index.md'
    $indexEntry = "- [$(Split-Path $path -Leaf)](./$(Split-Path $path -Leaf)/README.md) - $($categoryDescriptions['%category%'])"
    
    if (Test-Path $indexPath) {
        Add-Content -Path $indexPath -Value $indexEntry -Encoding UTF8
    } else {
        $indexHeader = @"
# エラー一覧: $(Get-Date -Format 'yyyy-MM-dd')

## 本日のエラー
"@
        $indexHeader | Out-File -FilePath $indexPath -Encoding UTF8
        Add-Content -Path $indexPath -Value $indexEntry -Encoding UTF8
    }
    
    # カテゴリ別シンボリックリンク作成（WSL側で実行が必要）
    Write-Host "Screenshot saved to: $path"
}
)"
    return script
}

OpenTodayErrors() {
    ; 今日のエラーフォルダを開く
    FormatTime, DateFolder, , yyyy-MM-dd
    FullPath := WSL_BASE_PATH . "\" . DateFolder
    
    if (FileExist(FullPath)) {
        Run, explorer.exe "%FullPath%"
    } else {
        MsgBox, 64, Info, No errors captured today.
    }
}

OpenErrorFolder:
    Run, explorer.exe "%WSL_BASE_PATH%"
return

; ===============================================
; 数字キーショートカット（メニュー表示中）
; ===============================================

#IfWinActive, ahk_class #32768  ; メニュー表示中
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

; WSLパスの存在確認
if (!FileExist(WSL_BASE_PATH)) {
    MsgBox, 48, Setup Required, Error screenshot folder not found!`n`nPlease run in PowerShell:`nNew-Item -ItemType Directory -Path "%WSL_BASE_PATH%" -Force
}

; システムトレイアイコン設定
Menu, Tray, Icon, shell32.dll, 110
Menu, Tray, Tip, Error Screenshot Manager
Menu, Tray, Add, Open Error Folder, OpenErrorFolder
Menu, Tray, Add, Open Today's Errors, OpenTodayErrors
Menu, Tray, Add
Menu, Tray, Add, Exit, ExitApp

ExitApp:
ExitApp

; ===============================================
; 使用方法の表示
; ===============================================

; 初回起動時のヘルプ
if (!FileExist(A_ScriptDir . "\initialized.txt")) {
    FileAppend, initialized, %A_ScriptDir%\initialized.txt
    MsgBox, 64, Error Screenshot Manager, 
    (
使用方法:
    
Win+Shift+E : カテゴリ選択してスクショ保存
Ctrl+Shift+E : 前回と同じカテゴリで即保存
Win+Alt+E : 今日のエラー一覧を開く

カテゴリ選択時は数字キーも使用可能:
1: API Error
2: Build Error  
3: Runtime Error
4: UI Bug
5: Test Failure
6: Other
    )
}