# エラー報告システム

## 概要
StatVizForge_JikkenPyプロジェクトのバグ修正を効率化するための、シンプルなエラー情報収集・管理システムです。

## フォルダ構造

```
error-reports/
├── screenshots/          # 📸 エラー画面のスクリーンショット（全て一箇所に保存）
├── logs/                 # 📄 関連ログファイル
│   ├── application/      # アプリケーションログ
│   ├── system/          # システムレベルログ
│   └── test/            # テスト実行ログ
├── context/             # 📝 エラー発生時のコンテキスト情報
│   ├── reproduction-steps/  # 再現手順
│   ├── environment/         # 環境情報
│   └── related-files/       # 関連ファイル
└── archive/             # 📦 解決済みエラー情報のアーカイブ
```

## 🎯 設計思想：シンプル + AI分析

- **ユーザー**: スクリーンショットを `screenshots/` に保存するだけ
- **ClaudeCode**: 相談時の文脈からエラーの種類・重要度を自動判断
- **効率化**: 手動分類の手間を排除、迅速なバグ報告を実現

## 使用方法

### 1. エラー発生時の情報収集

#### Windowsからのスクリーンショット保存
1. **エラー発生時に画面キャプチャ**
2. **一箇所に保存するだけ**
   ```
   \\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\
   ```

#### ファイル命名規則
```
YYYYMMDD_HHMMSS_[簡潔な説明].png

例：
20250802_143022_project-list-loading-error.png
20250802_143055_api-timeout-500.png
20250802_143112_button-not-clickable.png
```

### 2. ClaudeCodeによる自動分析

ClaudeCodeに相談する際は以下の情報を提供：

```
「error-reports/screenshots/20250802_143022_project-list-loading-error.png のエラーを解決してください」

+ 状況説明：
- 何をしようとしていたか
- どんなエラーが発生したか  
- いつから発生しているか
- 関連する操作や変更
```

**ClaudeCodeが自動で判断：**
- エラーの種類（フロントエンド/バックエンド/UI/ネットワーク等）
- 重要度（Critical/High/Medium/Low）
- 原因の推定
- 解決手順の提案

### 3. エラー報告手順

1. **スクリーンショット保存**
   ```
   error-reports/screenshots/20250802_143022_project-error.png
   ```

2. **ClaudeCodeに相談**
   ```
   「このエラーを解決してください：error-reports/screenshots/[ファイル名]
   
   状況：[エラーの状況説明]」
   ```

3. **自動でコンテキスト収集**
   - ClaudeCodeが関連ログを確認
   - 環境情報を自動取得
   - 再現手順を推定

### 4. 環境情報収集

```bash
# 環境情報を記録
echo "## 環境情報
- OS: $(uname -a)
- Node.js: $(node --version)
- Python: $(python3 --version)
- ブラウザ: $(google-chrome --version)
- 発生時刻: $(date)
- Git Commit: $(git rev-parse HEAD)

## エラー内容
[エラーの詳細説明]

## 再現条件
[エラーが発生する条件]

## 期待動作
[正常時の期待される動作]
" > error-reports/context/environment/20250802_143022_env-info.md
```

## 管理・運用

### 定期的なアーカイブ
```bash
# 解決済みエラーをアーカイブに移動
mv error-reports/screenshots/frontend/high/20250801_* error-reports/archive/
```

### エラー統計分析
```bash
# カテゴリ別エラー数統計
find error-reports/screenshots -name "*.png" | cut -d'/' -f3-4 | sort | uniq -c
```

## 🖥️ Windowsアクセスパス

### エクスプローラーで直接アクセス（推奨）
```
\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\
```

### PowerShellからアクセス
```powershell
cd "\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots"
```

## 🤖 ClaudeCodeとの連携例

### エラー相談の例
```
「error-reports/screenshots/20250802_143022_project-error.png を見てください。

プロジェクト一覧ページで新規作成ボタンを押すとこのエラーが出ます。
昨日まで正常に動作していました。」
```

### ClaudeCodeの自動分析
- 📸 スクリーンショットを確認
- 🔍 エラーメッセージを解析  
- 📊 関連ログを検索
- ⚡ 解決策を提案
- 📝 再現手順を記録

## 自動化スクリプト

### エラー情報収集スクリプト
```bash
# 新しいエラー報告を作成
./error-reports/scripts/create-error-report.sh [category] [priority] [description]
```

### バックアップスクリプト  
```bash
# エラー情報を外部にバックアップ
./error-reports/scripts/backup-error-reports.sh
```

## 注意事項

1. **個人情報の除去**
   - スクリーンショットに個人情報が含まれていないか確認
   - API キー、パスワード等の機密情報をマスク

2. **ファイルサイズ管理**
   - 画像は適切な解像度で保存（不要に高解像度にしない）
   - 定期的にアーカイブして容量管理

3. **チーム共有**
   - 重要なエラーは即座にチームに共有
   - 解決策も同じフォルダ構造で文書化

## 統合連携

- **GitHub Issues**: エラー報告からIssue自動作成
- **開発ログ**: `_docs/history/` との連携
- **テスト結果**: `testing/results/` との関連付け