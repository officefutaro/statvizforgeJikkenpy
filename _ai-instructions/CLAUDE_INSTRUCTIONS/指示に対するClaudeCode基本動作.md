# このルールに従うこと、このリンク先まで確認のこと

# 開始指示時実施項目
1. doc/history/session_YYYYMMDD.md ファイルを作成し、実施事項を追記。すでにある場合はこのファイルに追記。  
1. 新しいブランチを作成し、ユーザーとの対話の都度更新する
1. **プロンプト記録**: 全てのユーザープロンプトおよびClaudeの提案内容をdoc/history/session_YYYYMMDD.mdに記録する
   - ユーザーからの指示・質問を原文のまま記録
   - Claudeが提示した作業計画・解決策・提案内容を記録
   - 実行したコマンドや変更内容の要約を記録
   - 途中停止時の状況と未完了タスクを明記
   - 再開時に円滑な継続が可能なよう、コンテキスト情報を詳細に記載

# API確認時
APIの確認やテストに指示されたときの対応
テストは　CLAUDE_INSTRUCTIONS/test_generation_rules.md　参照
**プロジェクトデータ保護は　CLAUDE_INSTRUCTIONS/project_data_protection.md　参照**
1. APIの一覧を作成する。  
1. doc/APIja.md　ほかAPIの一覧を更新  
1. APIの命名規則や仕様をチェック。ユーザーに改善提案  
1. ユーザーの指示をうけ変更
1. テストの作成  
1. **必須**: フロントエンド・バックエンドAPI整合性テストの実施
   - test_generation_rules.md の「## 12. 必須: フロントエンド・バックエンドAPI整合性テスト」に従って実行
   - エンドポイント網羅性テスト
   - 型整合性テスト  
   - HTTPメソッド・ステータスコード整合性テスト
   - APIバージョニング整合性テスト
1. **必須**: プロジェクトデータ保護の確認
   - project_data_protection.md のガイドラインに従ってデータ保護を実施
   - テスト前後でprojectフォルダの内容変更がないことを確認
   - コメント、タグ、メタデータの消失防止策が動作することを検証
1. doc/APIja.md　ほかAPIの一覧を更新  
1. mainにブランチをマージし、githubにコミット＆プッシュ
1. テストの実行  
1. テストを行いながら問題点があった場合は全てがOKになるまで繰り返す  
1. テスト及び改善点、結果はdoc/history/test_YYYYMMDD.md　に記録
1. **必須**: API整合性テスト結果をdoc/history/api_integration_YYYYMMDD.mdに記録
1. テストが終わったら、mainにブランチをマージし、githubにコミット＆プッシュ
1. 新しいブランチを作成し、以後は一つの指示がある都度コミットする。


# プログラム修正指示時
　CLAUDE_INSTRUCTIONS/auto_branch_workflow.md　を参照
**プロジェクトデータ保護は　CLAUDE_INSTRUCTIONS/project_data_protection.md　参照**
**WSL2ネットワーク設定は　CLAUDE_INSTRUCTIONS/wsl2_network_setup.md　参照**
**React Hooks修正時は　CLAUDE_INSTRUCTIONS/react-hooks-best-practices.md　参照**
1. 指示毎にコミットする。  
1. doc/history/session_YYYYMMDD.md ファイルを作成し、実施事項を追記。すでにある場合はこのファイルに追記。  
1. **APIに関連する修正の場合**: フロントエンド・バックエンドAPI整合性テストを実施
   - test_generation_rules.md の「## 12. 必須: フロントエンド・バックエンドAPI整合性テスト」に従って実行
   - 修正がAPIに影響する場合は必ずテスト実行
   - 結果をdoc/history/api_integration_YYYYMMDD.mdに記録
1. **プロジェクトデータに影響する修正の場合**: プロジェクトデータ保護を確認
   - project_data_protection.md のガイドラインに従ってデータ保護策を適用
   - プロジェクト作成・更新・削除処理の修正時は特に注意
   - コメント、タグ、メタデータの保護が適切に動作することを確認
1. **新機能実装時**: ヘッドモードでのE2Eテストを必ず実施
   - `npm run test:e2e -- --headed` を実行
   - 視覚的な問題がないことを確認
   - 全てのテストが成功してからユーザーに完了報告
1. ユーザーに確認を促すときは全てのサービスをシャットダウンし、新規プロセスで試す。  
1. ユーザーから確認を依頼された場合も同様に全てのサービスをシャットダウンし、新規プロセスで試す。  

# 終了指示事
上記ファイルの更新を確認し終了する。