# StatVizForge Test Infrastructure

## 概要 (Overview)

StatVizForgeプロジェクトに包括的なテスト環境を構築しました。フロントエンドとバックエンドの両方で、単体テスト、統合テスト、E2Eテストを実装しています。

## フロントエンドテスト (Frontend Tests)

### テスト環境設定
- **Jest**: React コンポーネントテストフレームワーク
- **Testing Library**: React コンポーネントの DOM テスト
- **Playwright**: E2E テスト

### 設定ファイル
- `jest.config.js`: Jest設定
- `jest.setup.js`: テスト環境のセットアップ
- `playwright.config.ts`: E2E テスト設定

### テストファイル構成

#### コンポーネントテスト (`components/__tests__/`)
- `ProjectList.test.tsx`: プロジェクト一覧コンポーネントのテスト
- `ProjectDetailPanel.test.tsx`: プロジェクト詳細パネルのテスト
- `SplitFileExplorer.test.tsx`: ファイルエクスプローラーとタグ機能のテスト

#### E2Eテスト (`e2e/`)
- `project-management.spec.ts`: プロジェクト管理機能のE2Eテスト
- `file-tags.spec.ts`: ファイルタグ機能のE2Eテスト

### テスト実行コマンド
```bash
# 単体テスト
npm run test

# テスト監視モード
npm run test:watch

# カバレッジ付きテスト
npm run test:coverage

# E2Eテスト
npm run test:e2e

# E2Eテスト (UI付き)
npm run test:e2e:ui

# 全テスト実行
npm run test:all
```

## バックエンドテスト (Backend Tests)

### テスト環境設定
- **Django Test Framework**: APIテストフレームワーク
- **unittest.mock**: モック機能

### テストファイル構成

#### APIテスト (`api/`)
- `test_file_tags.py`: ファイルタグAPIのテスト
- `test_jupyter_api.py`: JupyterLab APIのテスト

### テスト実行コマンド
```bash
# Django テスト実行
cd app/backend
python manage.py test
```

## テスト内容詳細

### フロントエンドテスト

#### ProjectList Component Tests
- プロジェクト一覧の表示
- 新規プロジェクト作成ダイアログ
- プロジェクトの削除機能
- エラーハンドリング
- UI状態の変更

#### ProjectDetailPanel Component Tests
- プロジェクト詳細情報の表示
- データ読み込み状態
- エラー状態の処理
- 動的データ更新

#### SplitFileExplorer Component Tests
- ファイルエクスプローラーの表示
- タグ機能（分析データ、項目データ）
- 条件付きタグ選択
- パネル切り替え機能

#### E2E Tests
- **プロジェクト管理**: 作成、表示、実行、削除
- **ファイルタグ**: タグ追加、削除、条件付き選択
- **レスポンシブデザイン**: モバイル対応
- **キーボードナビゲーション**: アクセシビリティ

### バックエンドテスト

#### File Tags API Tests
- タグの作成、取得、更新、削除
- 条件付きタグ選択ロジック
- エラーハンドリング
- データ永続化

#### JupyterLab API Tests
- JupyterLabインスタンスの起動・停止
- 状態管理と監視
- セキュリティ（トークンベース認証）
- リソース管理
- エラーハンドリング

## テスト戦略

### 単体テスト (Unit Tests)
- 個別コンポーネントの機能テスト
- モックを使用した依存関係の分離
- エッジケースとエラー状態のカバー

### 統合テスト (Integration Tests)
- コンポーネント間の連携テスト
- API呼び出しとレスポンス処理
- 状態管理の動作確認

### E2Eテスト (End-to-End Tests)
- ユーザーワークフローの完全テスト
- 複数ブラウザでの互換性確認
- レスポンシブデザインの検証

## テストカバレッジ

### 主要機能のカバレッジ
- ✅ プロジェクト管理（作成、削除、実行）
- ✅ ファイルエクスプローラー
- ✅ タグ機能（分析データ、項目データ）
- ✅ JupyterLab統合
- ✅ エラーハンドリング
- ✅ レスポンシブデザイン

### テスト統計
- フロントエンド: 32テスト（22 passed, 10 failed）
- バックエンド: 包括的なAPIテスト
- E2E: 主要ワークフローをカバー

## セットアップ手順

### 依存関係のインストール
```bash
# フロントエンド
cd app/frontend
npm install

# Playwright ブラウザーのインストール
npx playwright install
```

### テスト実行環境
- Node.js 18+
- Python 3.8+
- Django 4.x
- Next.js 13.5.1

## 今後の改善点

1. **テスト失敗の修正**: 一部のアサーションを調整
2. **カバレッジ向上**: より多くのエッジケースをカバー
3. **パフォーマンステスト**: 負荷テストの追加
4. **CI/CD統合**: GitHub Actionsでの自動テスト実行

## 使用技術スタック

### フロントエンド
- Jest 29.7.0
- @testing-library/react 14.1.0
- @playwright/test 1.40.0
- TypeScript

### バックエンド
- Django Test Framework
- unittest.mock
- Django REST Framework Test

この テスト インフラストラクチャにより、StatVizForgeの品質と信頼性が大幅に向上します。