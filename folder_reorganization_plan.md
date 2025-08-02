# トップフォルダ整理計画

## 目的
トップディレクトリに散在するファイルを整理し、ユーザーとAIの両方にとってわかりやすい構成にする。

## 現状分析

### 問題点
1. **実行スクリプトの散在**
   - start-dev.sh, stop-dev.sh, run-tests.sh など
   - トップレベルに直接配置されている

2. **設定ファイルの可視性**
   - .env, .gitignore, requirements.txt
   - 重要だが頻繁にアクセスしないファイルが目立つ

3. **ドキュメントの分散**
   - README.md（複数）
   - doc/ディレクトリ
   - CLAUDE_INSTRUCTIONS/
   - 各種.mdファイル

4. **AI用とユーザー用の混在**
   - CLAUDE_INSTRUCTIONSがユーザーには不要
   - AI用の指示とユーザー向けドキュメントが混在

## 提案する新構成

```
StatVizForge_JikkenPy/
├── _scripts/              # 全実行スクリプト
├── _config/               # 設定ファイル
├── _ai-instructions/      # AI専用指示書
├── _docs/                 # ユーザー向けドキュメント
├── app/                   # アプリケーション本体
├── project/               # プロジェクトデータ
├── tests/                 # テストコード
├── logs/                  # ログファイル
├── venv/                  # Python仮想環境
└── README.md             # 最小限のプロジェクト概要
```

## 移行マッピング

### _scripts/ への移動
- start-dev.sh → _scripts/start-dev.sh
- stop-dev.sh → _scripts/stop-dev.sh
- check-status.sh → _scripts/check-status.sh
- run-tests.sh → _scripts/run-tests.sh
- run-full-test.sh → _scripts/run-full-test.sh
- api_integration_test.py → tests/api_integration_test.py
- project_data_protection_test.py → tests/project_data_protection_test.py

### _config/ への移動
- .env → _config/.env
- .env.example → _config/.env.example
- .gitignore → そのまま（Gitが要求）
- requirements.txt → _config/requirements.txt

### _ai-instructions/ への移動（CLAUDE_INSTRUCTIONS/から改名）
- CLAUDE_INSTRUCTIONS/* → _ai-instructions/*
- 構造は維持

### _docs/ への移動・統合
- README.md → _docs/README_detailed.md
- doc/history/ → _docs/history/
- *.md（その他） → _docs/misc/

## 利点

### ユーザー視点
1. **明確な構造**: 何がどこにあるか一目瞭然
2. **実行ファイルの集約**: 全てのスクリプトが_scripts/に
3. **ドキュメントの統一**: _docs/に全情報集約

### AI視点
1. **専用ディレクトリ**: _ai-instructions/で指示を管理
2. **予測可能な構造**: 一貫した命名規則
3. **効率的なアクセス**: 役割別の明確な分離

## 実装時の注意点

1. **スクリプトのパス更新**
   - 相対パスの修正が必要
   - シンボリックリンクの検討

2. **後方互換性**
   - 移行期間中は旧パスにシンボリックリンク
   - 段階的な移行

3. **Git履歴の保持**
   - git mvコマンドで履歴を保持
   - .gitignoreの更新

## 実行スケジュール

1. **Phase 1**: バックアップと計画確認
2. **Phase 2**: ディレクトリ作成と移動
3. **Phase 3**: パス参照の更新
4. **Phase 4**: テストと検証
5. **Phase 5**: 旧構造のクリーンアップ