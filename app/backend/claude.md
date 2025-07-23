# 重要
APIの仕様を変更した場合は必ず
~/app/frontend/BOLT_NEW_INSTRUCTIONS.md
の内容を変更すること。

# API変更時のドキュメント更新
APIの変更時は~/doc/APIja.mdに変更した内容を記述すること。
このファイルは人間が読んで理解するためのファイルのため、丁寧に記述すること。

記述内容：
- 変更した日時
- 変更したAPIエンドポイント
- 変更理由
- 変更前後の仕様比較
- 影響範囲
- フロントエンド側で必要な対応

# API履歴記録機能（開発モードのみ）
開発モード（DEBUG=True）の時は、すべてのAPI呼び出しを自動的に記録する。

## 記録ファイル
- **ファイル名**: ~/app/backend/apihistory.md
- **形式**: Markdownファイル

## 記録内容
```
[日時] [メソッド] [エンドポイント]
リクエスト: {リクエスト内容}
レスポンス: {レスポンス内容}
ステータス: {HTTPステータスコード}
---
```

## 実装詳細
- **ミドルウェア**: api.middleware.api_logger.APILoggerMiddleware
- **対象**: /api/で始まるすべてのエンドポイント
- **動作条件**: settings.DEBUG = True の時のみ
- **エラー処理**: ログ記録でエラーが発生してもAPIは正常に動作する

## 注意事項
- 本番環境（DEBUG=False）では動作しない
- ファイルサイズが大きくなる可能性があるため、定期的に確認が必要
- バイナリデータは "Binary data" として記録される

# 定期ドキュメント更新
Claude Code全体にわたって以下のルールを適用：
- 1時間に1回、または「ドキュメントの更新」指示があった場合
- ~/doc/docja.mdを更新（追加）すること
- 新しく実装した機能、API仕様の変更、設定の変更、発生した問題と解決方法、開発の進捗状況を含める

# フロントエンド変更時の手順
frontendフォルダ内のファイルを変更した際は、必ず以下のコマンドでGitにpushすること：

```bash
# 変更したファイルを確認
git status

# 変更をステージング
git add app/frontend/

# コミット（メッセージは変更内容に応じて適切に記述）
git commit -m "Update frontend: [変更内容の説明]"

# リモートリポジトリにプッシュ
git push origin main
```

## 具体例
```bash
# BOLT_NEW_INSTRUCTIONS.mdを更新した場合
git add app/frontend/BOLT_NEW_INSTRUCTIONS.md
git commit -m "Update frontend: API仕様書を更新"
git push origin main

# 複数ファイルを変更した場合
git add app/frontend/
git commit -m "Update frontend: APIサービス追加とドキュメント更新"
git push origin main
```