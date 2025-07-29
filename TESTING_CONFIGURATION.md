# テスト設定と自動記録システム
# Testing Configuration and Auto-Recording System

## 概要

StatVizForgeでは、テスト実行時に自動的に結果を記録し、サマリーレポートを生成するシステムを実装しています。

## 設定ファイル

### test-config.json
プロジェクトルートの設定ファイルで、テストの動作を制御します。

```json
{
  "auto_record": {
    "enabled": true,
    "output_directory": "./testing/results",
    "date_format": "YYYYMMDD"
  },
  "project_data_protection": {
    "enabled": true,
    "target_directory": "./project"
  }
}
```

## 自動記録機能

### 実行されるタイミング
- `npm test` 実行時
- `npm run test:full` 実行時  
- `npm run test:report` 実行時

### 出力ファイル
毎回のテスト実行で以下のファイルが自動生成されます：

1. **詳細結果**: `test_results_YYYYMMDD_HHMMSS.json`
   - 全テストの詳細結果
   - カバレッジ情報
   - エラー詳細

2. **サマリーレポート**: `test_summary_YYYYMMDD_HHMMSS.md`
   - 実行結果の概要
   - 成功/失敗の統計
   - 次のアクション提案

3. **最新サマリー**: `latest_summary.md`
   - 最新のテスト結果（常に上書き）

### 出力場所
```
testing/results/
├── test_results_20250728_123456.json
├── test_summary_20250728_123456.md
├── latest_summary.md
└── ... (過去の結果)
```

## プロジェクトデータ保護

### 保護対象
- `/home/futaro/project/StatVizForge_JikkenPy/project/` 全体

### 動作フロー
1. **テスト開始前**: プロジェクトフォルダをバックアップ
2. **テスト実行中**: 安全にテストデータを操作
3. **テスト終了後**: 元の状態に復元
4. **クリーンアップ**: バックアップファイルを削除

### バックアップ場所
```
app/frontend/.test-backups/
├── backup-1753685884508/
└── ... (一時バックアップ)
```

## テスト実行コマンド

### 基本実行（自動記録付き）
```bash
npm test
```

### テストのみ（記録なし）
```bash
npm run test:jest-only
```

### 完全テスト（全種類）
```bash
npm run test:full
```

### 記録のみ実行
```bash
npm run test:report
```

## 設定のカスタマイズ

### 自動記録を無効化
```bash
# 環境変数で制御
TEST_AUTO_RECORD=false npm test
```

### E2Eテストをスキップ
```bash
# E2Eテストを除外
RUN_E2E=false npm run test:full
```

### バックエンドテストをスキップ
```bash
# バックエンドテストを除外
RUN_BACKEND=false npm run test:full
```

## 記録されるデータ

### Jest テスト結果
- 総テスト数
- 成功/失敗数
- 実行時間
- カバレッジ情報
- 失敗詳細

### E2E テスト結果
- ブラウザ別実行結果
- スクリーンショット（失敗時）
- 実行トレース

### バックエンドテスト結果
- Django テスト結果
- API テスト詳細

## トラブルシューティング

### よくある問題

#### 記録ファイルが生成されない
```bash
# 権限確認
ls -la testing/results/

# ディレクトリが存在しない場合
mkdir -p testing/results
```

#### バックアップが失敗する
```bash
# プロジェクトフォルダの存在確認
ls -la project/

# 権限確認
ls -la app/frontend/.test-backups/
```

#### 古いバックアップが残る
```bash
# 手動クリーンアップ
rm -rf app/frontend/.test-backups/backup-*
```

## 設定の変更履歴

| 日付 | 変更内容 | 理由 |
|------|----------|------|
| 2025-07-28 | 初期設定作成 | テスト結果自動記録の実装 |
| 2025-07-28 | プロジェクトパス修正 | 正しいパス(`./project`)に変更 |

## メンテナンス

### 定期的なクリーンアップ
古いテスト結果ファイルは30日後に自動削除されます。

### バックアップ保持期間
テストバックアップは1時間後に自動削除されます。

---

この設定により、テスト実行の度に確実に結果が記録され、プロジェクトデータが保護される環境が提供されます。