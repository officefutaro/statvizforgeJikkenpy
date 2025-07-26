# StatVizForge テスト統合ディレクトリ

このディレクトリには、StatVizForge APIのテストに関連するすべてのファイルが統合されています。

## ディレクトリ構成

```
testing/
├── scripts/           # テスト実行スクリプト
│   ├── test_runner.sh    # メインのテスト実行スクリプト
│   ├── run_tests.py      # Python版テスト実行スクリプト
│   └── README.md         # スクリプトの使用方法
├── results/           # テスト結果保存ディレクトリ
│   ├── test_results_*.log  # 詳細な実行ログ
│   ├── test_report_*.md    # サマリーレポート
│   └── README.md           # ファイル形式の説明
├── docs/              # テスト関連ドキュメント
│   ├── API_Test_Manual.md       # 詳細なテスト実行マニュアル
│   ├── API_Testing_Guide.md     # テスト開発ガイド
│   └── Test_Writing_Examples.md # テスト記述方法とサンプル
└── README.md          # このファイル
```

## クイックスタート

### 1. 環境準備
```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source venv/bin/activate
pip install parameterized  # 初回のみ
```

### 2. テスト実行
```bash
# 全テスト実行
../../testing/scripts/test_runner.sh

# 特定のテストのみ実行
../../testing/scripts/test_runner.sh lifecycle
../../testing/scripts/test_runner.sh compatibility
../../testing/scripts/test_runner.sh performance
```

### 3. 結果確認
```bash
# 最新の結果確認
ls -lt ../../testing/results/test_results_*.log | head -1

# ログ内容表示
cat ../../testing/results/test_results_YYYYMMDD_HHMMSS.log
```

## 主要な機能

### テストの種類
- **ライフサイクルテスト**: プロジェクトの作成→更新→削除→復元の完全フロー
- **互換性テスト**: RESTful vs Legacy エンドポイントの動作確認
- **パフォーマンステスト**: API応答時間の測定
- **エラーハンドリングテスト**: 不正データや存在しないリソースの処理
- **バリデーションテスト**: 入力データの検証

### サポートする実行方法
1. **シェルスクリプト実行** (推奨): `test_runner.sh`
2. **Python直接実行**: `run_tests.py`
3. **Django標準コマンド**: `python manage.py test`

## ドキュメント

### 初心者向け
- [`docs/API_Test_Manual.md`](docs/API_Test_Manual.md) - ステップバイステップの実行マニュアル

### 開発者向け
- [`docs/API_Testing_Guide.md`](docs/API_Testing_Guide.md) - テスト開発・拡張ガイド
- [`docs/Test_Writing_Examples.md`](docs/Test_Writing_Examples.md) - テスト記述方法とサンプルコード

## CI/CD統合

このテストスイートはGitHub Actions、GitLab CI、JenkinsなどのCI/CDパイプラインに組み込み可能です。

### GitHub Actions例
```yaml
- name: Run API Tests
  run: |
    cd app/backend
    source venv/bin/activate
    ../../testing/scripts/test_runner.sh all
```

詳細は [`docs/API_Test_Manual.md`](docs/API_Test_Manual.md) の「CI/CD統合」セクションを参照してください。

## トラブルシューティング

よくある問題と解決方法は [`docs/API_Test_Manual.md`](docs/API_Test_Manual.md) の「トラブルシューティング」セクションを参照してください。

## 変更履歴

| 日付 | バージョン | 変更内容 |
|------|-----------|----------|
| 2025-07-26 | 2.0.0 | テスト関連ファイルを統合ディレクトリに整理 |
| 2025-07-26 | 1.0.0 | 初版作成、基本テストスイート実装 |