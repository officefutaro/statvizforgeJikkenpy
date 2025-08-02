# エラー報告システム

## 概要
StatVizForge_JikkenPyプロジェクトのバグ修正を効率化するための、体系的なエラー情報収集・管理システムです。

## フォルダ構造

```
error-reports/
├── screenshots/           # エラー画面のスクリーンショット
│   ├── frontend/         # フロントエンド関連エラー
│   │   ├── critical/     # 🔴 重大：アプリ停止、データ損失
│   │   ├── high/         # 🟠 高：主要機能不動
│   │   ├── medium/       # 🟡 中：一部機能影響
│   │   └── low/          # 🟢 軽微：表示崩れ等
│   ├── backend/          # バックエンド関連エラー
│   │   ├── critical/     # API完全停止、データベース問題
│   │   ├── high/         # 主要API動作不良
│   │   ├── medium/       # 一部API問題
│   │   └── low/          # パフォーマンス問題等
│   ├── network/          # ネットワーク・通信エラー
│   │   ├── critical/     # 完全通信断
│   │   ├── high/         # API通信失敗
│   │   ├── medium/       # 間欠的通信問題
│   │   └── low/          # 遅延問題等
│   ├── ui/               # UI/UX関連問題
│   │   ├── critical/     # 操作不能
│   │   ├── high/         # 主要操作困難
│   │   ├── medium/       # 一部操作問題
│   │   └── low/          # 見た目の問題
│   └── integration/      # 統合テスト・E2Eエラー
│       ├── critical/     # テスト完全失敗
│       ├── high/         # 主要シナリオ失敗
│       ├── medium/       # 一部シナリオ失敗
│       └── low/          # 軽微なテスト問題
├── logs/                 # 関連ログファイル
│   ├── application/      # アプリケーションログ
│   ├── system/          # システムレベルログ
│   └── test/            # テスト実行ログ
├── context/             # エラー発生時のコンテキスト情報
│   ├── reproduction-steps/  # 再現手順
│   ├── environment/         # 環境情報
│   └── related-files/       # 関連ファイル
└── archive/             # 解決済みエラー情報のアーカイブ
```

## 使用方法

### 1. エラー発生時の情報収集

#### Windowsからのスクリーンショット保存
1. **エラー発生時に画面キャプチャ**
2. **適切なカテゴリフォルダに保存**
   ```
   \\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\[カテゴリ]\[優先度]\
   ```

#### ファイル命名規則
```
YYYYMMDD_HHMMSS_[カテゴリ]_[概要].png

例：
20250802_143022_frontend_project-list-loading-error.png
20250802_143055_backend_api-timeout-500.png
20250802_143112_ui_button-not-clickable.png
```

### 2. 優先度の判断基準

| 優先度 | 基準 | 対応目安 |
|--------|------|----------|
| **Critical** 🔴 | アプリ停止、データ損失、セキュリティ問題 | 即座 |
| **High** 🟠 | 主要機能が使用不能 | 24時間以内 |
| **Medium** 🟡 | 一部機能に影響、回避策あり | 1週間以内 |
| **Low** 🟢 | 軽微な問題、UX改善 | 次回リリース |

### 3. エラー報告手順

1. **スクリーンショット保存**
   - 適切なフォルダに画像を保存

2. **コンテキスト情報記録**
   ```bash
   # 再現手順ファイル作成
   echo "エラー再現手順：
   1. プロジェクト一覧を開く
   2. 新規プロジェクト作成ボタンをクリック
   3. エラーダイアログが表示される" > context/reproduction-steps/20250802_143022_project-creation-error.md
   ```

3. **ログファイル保存**
   ```bash
   # エラー発生時点のログを保存
   cp logs/backend.log error-reports/logs/application/20250802_143022_backend.log
   cp logs/frontend.log error-reports/logs/application/20250802_143022_frontend.log
   ```

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

## Windowsアクセスパス

### エクスプローラーから直接アクセス
```
\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\
```

### PowerShellからアクセス
```powershell
cd "\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports"
```

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