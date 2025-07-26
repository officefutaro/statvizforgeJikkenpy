# テスト実行スクリプト

このディレクトリには、StatVizForge APIのテストを実行するためのスクリプトが含まれています。

## ファイル構成

- `test_runner.sh` - メインのテスト実行スクリプト（推奨）
- `run_tests.py` - Python版テスト実行スクリプト

## 使用方法

バックエンドディレクトリから実行してください：

```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source venv/bin/activate

# 全テスト実行
../../testing/scripts/test_runner.sh

# 特定のテストのみ実行
../../testing/scripts/test_runner.sh lifecycle
../../testing/scripts/test_runner.sh compatibility
../../testing/scripts/test_runner.sh performance
```

## テスト結果

テスト結果は `/testing/results/` ディレクトリに保存されます：

- `test_results_*.log` - 詳細なテスト実行ログ
- `test_report_*.md` - テスト結果のサマリーレポート

## 詳細なドキュメント

詳細な使用方法は以下のドキュメントを参照してください：

- `/testing/docs/API_Test_Manual.md` - 詳細なテスト実行マニュアル
- `/testing/docs/API_Testing_Guide.md` - テスト開発ガイド
- `/testing/docs/Test_Writing_Examples.md` - テスト記述方法とサンプル