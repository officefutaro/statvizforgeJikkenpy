# StatVizForge 技術ドキュメント

## 📚 ドキュメント構成

このフォルダには StatVizForge プロジェクトの技術ドキュメントが含まれています。

### 🎯 対象読者
- **開発者**: 機能実装・保守担当者
- **アーキテクト**: システム設計・技術選定担当者  
- **テスター**: 品質保証・テスト実装担当者
- **運用者**: デプロイ・監視・運用担当者

### 📖 ドキュメント一覧

#### 🏗️ アーキテクチャ
- [システムアーキテクチャ](./architecture/README.md) - 全体設計・技術スタック
- [データベース設計](./architecture/database.md) - ER図・テーブル仕様
- [API設計](./architecture/api.md) - REST API仕様・認証

#### 🎨 フロントエンド
- [コンポーネント設計](./frontend/components.md) - React コンポーネント仕様
- [状態管理](./frontend/state-management.md) - Context・hooks設計
- [スタイリング](./frontend/styling.md) - Tailwind CSS・UI方針

#### ⚙️ バックエンド  
- [Django アプリケーション](./backend/django-apps.md) - アプリ構成・モデル
- [API実装](./backend/api-implementation.md) - ViewSet・シリアライザー
- [データ処理](./backend/data-processing.md) - ファイル処理・分析ロジック

#### 🧪 テスト
- [テスト戦略](./testing/strategy.md) - テスト方針・カバレッジ目標
- [ユニットテスト](./testing/unit-tests.md) - Jest・Django Test実装
- [E2Eテスト](./testing/e2e-tests.md) - Playwright実装・シナリオ
- [GUIテスト](./testing/gui-tests.md) - GUI操作テスト仕様

#### 🚀 デプロイ・運用
- [開発環境構築](./deployment/development.md) - ローカル開発環境
- [本番デプロイ](./deployment/production.md) - Docker・CI/CD
- [監視・ログ](./deployment/monitoring.md) - メトリクス・アラート

#### 📋 開発ガイド
- [コーディング規約](./development/coding-standards.md) - 言語別規約・命名規則
- [Git ワークフロー](./development/git-workflow.md) - ブランチ戦略・コミット規約
- [レビュープロセス](./development/review-process.md) - PR・コードレビュー

#### 🔧 新機能実装ガイド
- [ConfigurableTableViewer](./features/configurable-table-viewer.md) - 高度表示機能
- [動的チャート](./features/dynamic-charts.md) - ホバー連動・リアルタイム更新
- [順序設定](./features/ordinal-ordering.md) - ドラッグ&ドロップ・自動並び替え

#### 🐛 トラブルシューティング
- [よくある問題](./troubleshooting/common-issues.md) - FAQ・解決策
- [パフォーマンス](./troubleshooting/performance.md) - 最適化・ボトルネック
- [互換性](./troubleshooting/compatibility.md) - ブラウザ・OS対応

## 🎨 ドキュメント表示方法

### 1. 開発中のプレビュー
```bash
# Markdown プレビュー（VS Code）
Ctrl+Shift+V

# ローカルサーバー起動
npx serve docs/
```

### 2. 統合表示システム
- **Next.js アプリ内**: `/docs` ルートで表示
- **静的サイト生成**: GitHub Pages自動公開
- **検索機能**: Algolia DocSearch統合

### 3. 自動更新システム
- **コミット連動**: 実装変更時にドキュメント更新通知
- **CI統合**: テスト成功時にドキュメント自動更新
- **バージョン管理**: 機能リリース毎のドキュメントスナップショット

## 📝 ドキュメント作成・更新ルール

### 作成タイミング
- ✅ 新機能実装時: 仕様・実装ガイド作成
- ✅ バグ修正時: トラブルシューティング更新  
- ✅ リファクタリング時: アーキテクチャ更新
- ✅ テスト追加時: テスト仕様更新

### 品質基準
- **完全性**: 実装内容を100%カバー
- **正確性**: コードと仕様の完全一致
- **実用性**: 開発者が実際に使える内容
- **保守性**: 継続的な更新が容易

### 更新プロセス
1. **実装**: 機能実装と同時にドキュメント作成
2. **レビュー**: PR時にドキュメントも同時レビュー  
3. **テスト**: ドキュメント内容の動作確認
4. **公開**: マージ時に自動公開

---

**最終更新**: 2025年7月30日  
**管理者**: StatVizForge 開発チーム