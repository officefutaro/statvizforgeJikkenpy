# 🚨 重要チェックリスト - 毎回必ず確認

## セッション開始時の必須確認事項

- [ ] 新しいブランチ作成
- [ ] `doc/history/session_YYYYMMDD.md` 作成/更新

## コード修正時の必須確認事項

### React関連修正時
- [ ] `react-hooks-best-practices.md` 確認
- [ ] ESLint実行 (`npm run lint`)
- [ ] Hooks初期化順序チェック

### API関連修正時
- [ ] **新しいAPIエンドポイント作成時は `api-proxy-creation-guide.md` 必須確認**
- [ ] `lib/api-config.ts` のエンドポイント定義を更新
- [ ] 統一プロキシテンプレート使用確認
- [ ] フロントエンド・バックエンドAPI整合性テスト実施
- [ ] `test_generation_rules.md` 参照

### プロジェクトデータ関連修正時
- [ ] `project_data_protection.md` のガイドライン適用
- [ ] file_comments.json保護確認
- [ ] タグ・メタデータ保護確認

### WSL2/ネットワーク関連修正時
- [ ] `wsl2_network_setup.md` 参照
- [ ] Windows Chrome アクセス確認

## テスト・確認時の必須事項

- [ ] 全サービスシャットダウン後の新規プロセステスト
- [ ] コミット前の動作確認
- [ ] テスト結果の履歴記録

## 緊急時の最優先確認事項

1. **データ消失リスク** → `project_data_protection.md`
2. **API接続エラー** → `wsl2_network_setup.md`
3. **React初期化エラー** → `react-hooks-best-practices.md`

---
**🔥 このチェックリストを無視すると高確率で問題が発生します**