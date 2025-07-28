# プロジェクトデータ保護システム
# Project Data Protection System

## 概要 (Overview)

StatVizForgeのテスト実行時に、既存のプロジェクトフォルダのデータが変更・削除されることを防ぐためのデータ保護システムです。

## 機能 (Features)

### 自動バックアップ・リストア
- テスト実行前に`projects`フォルダ全体を自動バックアップ
- テスト完了後に元の状態を自動復元
- テストが失敗した場合でも確実にデータを復元

### 階層化された保護
1. **グローバル保護**: テストスイート全体での保護
2. **テストファイル保護**: 各テストファイル単位での保護  
3. **個別テスト保護**: 各テスト実行単位での保護

### テスト用データ作成
- テスト専用の一時プロジェクトを作成
- 実際のプロジェクトデータに影響を与えない

## 使用方法

### フロントエンドテスト (Jest)

#### 自動適用（推奨）
Jest設定により全テストで自動的に適用されます：

```typescript
// jest.config.js で設定済み
globalSetup: '<rootDir>/test-utils/globalSetup.ts',
globalTeardown: '<rootDir>/test-utils/globalTeardown.ts',
```

#### 手動適用
個別のテストファイルで使用する場合：

```typescript
import { withProjectProtection } from '@/test-utils/testHelpers'

describe('MyComponent', () => {
  const protection = withProjectProtection()
  
  beforeEach(async () => {
    await protection.beforeEach()
  })

  afterEach(async () => {
    await protection.afterEach()
  })

  afterAll(async () => {
    await protection.afterAll()
  })

  // テスト用プロジェクトの作成
  it('should work with test project', async () => {
    const projectPath = await protection.createTestProject('test_project', {
      'main.py': 'print("test")',
      'data.csv': 'col1,col2\nval1,val2'
    })
    
    // テスト実行...
  })
})
```

### E2Eテスト (Playwright)

```typescript
// playwright.config.ts で設定済み
globalSetup: require.resolve('./test-utils/e2e-globalSetup.ts'),
globalTeardown: require.resolve('./test-utils/e2e-globalTeardown.ts'),
```

個別テストでの使用：

```typescript
import { E2ETestProtection } from '../test-utils/testHelpers'

test.describe('Project Management', () => {
  test.beforeAll(async () => {
    await E2ETestProtection.setup()
  })

  test.afterAll(async () => {
    await E2ETestProtection.teardown()
  })

  // テスト実行...
})
```

### バックエンドテスト (Django)

#### ミックスインの使用
```python
from test_utils.project_backup import DjangoTestCaseMixin

class MyAPITestCase(DjangoTestCaseMixin, APITestCase):
    """自動的にプロジェクトデータが保護されます"""
    
    def test_api_functionality(self):
        # テスト用プロジェクトを作成
        project_path = self.create_test_project('test_project', {
            'main.py': 'print("test")',
            'config.json': '{"test": true}'
        })
        
        # テスト実行...
```

#### デコレーターの使用
```python
from test_utils.project_backup import with_project_protection

@with_project_protection
class MyTestCase(APITestCase):
    # 自動的にプロジェクトデータが保護されます
```

## ファイル構造

```
app/
├── frontend/
│   ├── test-utils/
│   │   ├── projectBackup.ts       # メインバックアップ機能
│   │   ├── globalSetup.ts         # Jest グローバルセットアップ
│   │   ├── globalTeardown.ts      # Jest グローバルティアダウン
│   │   ├── testHelpers.ts         # テストヘルパー関数
│   │   ├── e2e-globalSetup.ts     # E2E グローバルセットアップ
│   │   └── e2e-globalTeardown.ts  # E2E グローバルティアダウン
│   ├── jest.config.js             # 更新済み（グローバル設定含む）
│   └── playwright.config.ts       # 更新済み（グローバル設定含む）
└── backend/
    └── test_utils/
        └── project_backup.py      # Django用バックアップ機能
```

## 保護される内容

### 対象ディレクトリ
- `StatVizForge_JikkenPy/projects/` - 全プロジェクトフォルダ

### 保護されるデータ
- プロジェクトフォルダとその全内容
- ファイル構造
- ファイル内容
- メタデータ
- タグ情報

### バックアップ場所
- **フロントエンド**: `app/frontend/.test-backups/`
- **バックエンド**: システム一時ディレクトリ（自動クリーンアップ）

## 設定オプション

### タイムアウト設定
```typescript
// Jest設定
testTimeout: 30000, // 30秒

// Playwright設定  
actionTimeout: 30000,
navigationTimeout: 30000,
```

### 並列実行制御
```typescript
// Playwright - プロジェクトデータ保護のため無効化
fullyParallel: false,
workers: 1,
```

### 自動クリーンアップ
- 1時間以上経過した古いバックアップファイルを自動削除
- テスト完了時にバックアップファイルを自動削除

## トラブルシューティング

### よくある問題

#### バックアップ作成エラー
```
❌ バックアップ作成エラー: Permission denied
```

**解決方法**: ディレクトリの書き込み権限を確認してください。

#### 復元エラー
```
❌ バックアップ復元エラー: Backup directory not found
```

**解決方法**: テストが中断された可能性があります。手動で`projects`フォルダを確認してください。

#### ディスク容量不足
```
❌ バックアップ作成エラー: No space left on device
```

**解決方法**: 
1. 古いバックアップファイルを削除
2. `ProjectBackupManager.cleanupOldBackups()`を実行

### デバッグモード

環境変数でデバッグ情報を有効化：

```bash
# 詳細ログ出力
DEBUG_PROJECT_BACKUP=true npm run test

# バックアップを保持（クリーンアップしない）
KEEP_TEST_BACKUPS=true npm run test
```

## セキュリティ考慮事項

- バックアップファイルは一時的にのみ保存
- 機密データは含まれないことを確認済み
- アクセス権限は最小限に制限

## パフォーマンス最適化

- 大きなプロジェクトの場合、バックアップ時間が延長される可能性
- 必要に応じてテストを分割して実行
- 定期的な古いバックアップファイルのクリーンアップ

## 今後の改善予定

1. **増分バックアップ**: 変更されたファイルのみバックアップ
2. **圧縮バックアップ**: ディスク使用量の削減
3. **リモートバックアップ**: ネットワークストレージ対応
4. **設定ファイル**: カスタム設定オプションの追加

このシステムにより、テスト実行が既存のプロジェクトデータに与える影響を完全に排除し、安全なテスト環境を提供します。