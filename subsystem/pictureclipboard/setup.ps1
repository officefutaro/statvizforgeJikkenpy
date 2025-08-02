# ===============================================
# エラースクリーンショット管理システム セットアップ
# ===============================================

Write-Host "エラースクリーンショット管理システムのセットアップを開始します..." -ForegroundColor Cyan

# 基本ディレクトリ作成
$baseDir = "\\wsl$\Ubuntu\home\futaro\screenshots\errors"
$categoriesDir = "$baseDir\categories"

Write-Host "ディレクトリ構造を作成中..."

# メインディレクトリ
New-Item -ItemType Directory -Path $baseDir -Force | Out-Null
New-Item -ItemType Directory -Path $categoriesDir -Force | Out-Null

# カテゴリディレクトリ
$categories = @(
    "API_ERRORS",
    "BUILD_ERRORS", 
    "RUNTIME_ERRORS",
    "UI_BUGS",
    "TEST_FAILURES",
    "OTHER"
)

foreach ($category in $categories) {
    New-Item -ItemType Directory -Path "$categoriesDir\$category" -Force | Out-Null
}

# README.md作成
$readme = @"
# エラースクリーンショット管理システム

## 概要
ClaudeCodeとの連携用にエラー画面を体系的に保存・管理するシステムです。

## ディレクトリ構造
- **日付別フォルダ (YYYY-MM-DD)**: その日のエラーを時系列で保存
- **categories/**: エラー種別ごとのシンボリックリンク（整理用）

## 使用方法

### ホットキー
- **Win+Shift+E**: カテゴリ選択メニューを表示してスクショ保存
- **Ctrl+Shift+E**: 前回と同じカテゴリで即座に保存（連続エラー用）
- **Win+Alt+E**: 今日のエラー一覧フォルダを開く

### カテゴリ
1. **API_ERROR**: API通信関連（404, 500, CORS等）
2. **BUILD_ERROR**: ビルド・コンパイルエラー
3. **RUNTIME_ERROR**: 実行時エラー・例外
4. **UI_BUG**: UI表示不具合
5. **TEST_FAIL**: テスト失敗
6. **OTHER**: その他

## 保存される情報
各エラーごとに以下が保存されます：
- `screenshot.png`: エラー画面のスクリーンショット
- `context.txt`: 発生時刻、アクティブウィンドウ等の情報
- `README.md`: エラーの説明と対応状況記録用

## ClaudeCodeとの連携
1. エラー発生時にスクリーンショットを撮る
2. Win+Shift+E でカテゴリを選択して保存
3. 該当フォルダの画像をClaudeCodeにドラッグ＆ドロップ
4. context.txtの情報も必要に応じて共有

---
Last Updated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
"@

$readme | Out-File -FilePath "$baseDir\README.md" -Encoding UTF8

# AutoHotkeyスクリプトのショートカット作成
$shortcutPath = "$env:USERPROFILE\Desktop\Error Screenshot Manager.lnk"
$targetPath = "$PSScriptRoot\error_screenshot_manager.ahk"

if (Test-Path $targetPath) {
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut($shortcutPath)
    $Shortcut.TargetPath = $targetPath
    $Shortcut.IconLocation = "shell32.dll,110"
    $Shortcut.Description = "エラースクリーンショット管理システム"
    $Shortcut.Save()
    Write-Host "デスクトップにショートカットを作成しました" -ForegroundColor Green
}

# スタートアップ登録の確認
$startupPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
Write-Host "`n自動起動に登録しますか？ (Y/N): " -NoNewline -ForegroundColor Yellow
$response = Read-Host

if ($response -eq 'Y') {
    Copy-Item $shortcutPath "$startupPath\Error Screenshot Manager.lnk" -Force
    Write-Host "スタートアップに登録しました" -ForegroundColor Green
}

Write-Host "`nセットアップが完了しました！" -ForegroundColor Green
Write-Host @"

使用開始方法:
1. デスクトップの「Error Screenshot Manager」をダブルクリック
2. エラー画面をスクリーンショット（PrintScreen等）
3. Win+Shift+E でカテゴリを選択して保存

保存先: $baseDir
"@ -ForegroundColor Cyan

pause