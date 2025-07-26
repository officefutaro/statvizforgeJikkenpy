# StatVizForge API テストガイド

## 概要

StatVizForge APIの品質を保証するためのテストスイートです。プロジェクトのライフサイクル全体（作成→更新→削除→復元）をテストし、複数のエンドポイントパターンとエラーハンドリングを検証します。

## テストの種類

### 1. **プロジェクトライフサイクルテスト**
```
作成 → 取得 → 更新 → 削除 → 復元 → 最終確認
```
- 完全なプロジェクトライフサイクルをシミュレート
- 各ステップでの状態変化を検証
- 時間的変化（created_date, modified_date, restored_date）を確認

### 2. **エンドポイント互換性テスト**
```
RESTful vs Legacy エンドポイントの並行テスト
```
- 新しいRESTfulエンドポイント（`/api/projects/`）
- 旧エンドポイント（`/api/projects/list`）
- 同じ機能で同じ結果が得られることを確認

### 3. **複数プロジェクト相互作用テスト**
```
複数プロジェクト作成 → 一部削除 → 一部復元
```
- プロジェクト間の相互作用をテスト
- 削除・復元が他のプロジェクトに影響しないことを確認

### 4. **エラーハンドリングテスト**
```
存在しないID → 不正データ → 権限エラー等
```
- 適切なHTTPステータスコード返却
- わかりやすいエラーメッセージ

### 5. **パフォーマンステスト**
```
応答時間測定 → 1秒以内の応答確認
```

## テスト実行方法

### 1. 環境準備

```bash
# バックエンドディレクトリに移動
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend

# 仮想環境を有効化
source venv/bin/activate

# 必要なパッケージをインストール（初回のみ）
pip install parameterized
```

### 2. テスト実行

#### **方法A: シェルスクリプト実行（推奨）**
```bash
# 全てのテストを実行
../../testing/scripts/test_runner.sh

# 特定のテストのみ実行
../../testing/scripts/test_runner.sh lifecycle      # ライフサイクルテスト
../../testing/scripts/test_runner.sh compatibility  # 互換性テスト
../../testing/scripts/test_runner.sh performance    # パフォーマンステスト
../../testing/scripts/test_runner.sh manual         # 手動テスト用情報表示
```

#### **方法B: Pythonスクリプト実行**
```bash
# 全てのテストを実行
python ../../testing/scripts/run_tests.py all

# 特定のテストのみ実行
python ../../testing/scripts/run_tests.py lifecycle
python ../../testing/scripts/run_tests.py compatibility
python ../../testing/scripts/run_tests.py performance
```

#### **方法C: Django標準コマンド**
```bash
# 全てのAPIテストを実行
python manage.py test api.tests

# 特定のテストクラスのみ
python manage.py test api.tests.ProjectLifecycleTestCase

# 特定のテストメソッドのみ
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle
```

### 3. テスト結果の確認

#### **成功例**
```
=== プロジェクト完全ライフサイクルテスト開始 ===

Phase 1: プロジェクト作成
✓ プロジェクト作成成功: 550e8400-e29b-41d4-a716-446655440001

Phase 2: プロジェクト詳細取得
✓ プロジェクト取得成功: テストプロジェクト

...

=== プロジェクト完全ライフサイクルテスト完了 ===

Ran 6 tests in 0.123s
OK
```

#### **失敗例**
```
FAIL: test_complete_project_lifecycle
AssertionError: Expected 201, got 400
```

## テストケース詳細

### ProjectLifecycleTestCase

#### `test_complete_project_lifecycle()`
**目的**: プロジェクトの完全なライフサイクルをテスト

**手順**:
1. プロジェクト作成（POST `/api/projects/`）
2. プロジェクト詳細取得（GET `/api/projects/{id}/`）
3. プロジェクト更新（PUT `/api/projects/{id}/`）
4. プロジェクト削除（DELETE `/api/projects/{id}/`）
5. 削除済み一覧確認（GET `/api/projects/deleted/`）
6. プロジェクト復元（POST `/api/projects/{id}/restore/`）
7. 最終状態確認（GET `/api/projects/{id}/`）

**検証項目**:
- 各ステップで適切なHTTPステータスコード
- レスポンスデータの整合性
- 時間的変化（日時フィールド）の更新

#### `test_endpoint_compatibility()`
**目的**: RESTful vs Legacy エンドポイントの互換性確認

**パラメータ化テスト**:
- RESTful: `/api/projects/`, `/api/projects/deleted/`
- Legacy: `/api/projects/list`, `/api/projects/archived`

**検証項目**:
- 同じ機能で同じレスポンス構造
- 同じHTTPステータスコード

#### `test_multiple_projects_interaction()`
**目的**: 複数プロジェクトの相互作用テスト

**手順**:
1. 3つのプロジェクトを作成
2. 1番目と3番目を削除
3. 1番目を復元
4. 各段階での状態確認

#### `test_error_handling_scenarios()`
**目的**: エラーハンドリングの確認

**テストケース**:
- 存在しないプロジェクトID → 404
- 不正なリクエストデータ → 400
- 存在しないプロジェクトの削除 → 404
- 存在しないプロジェクトの復元 → 404

#### `test_language_parameter_handling()`
**目的**: 言語パラメータの処理確認

**テストケース**:
- `?lang=ja` → 日本語エラーメッセージ
- `?lang=en` → 英語エラーメッセージ

## 手動テスト

自動テストに加えて、ブラウザやcurlでの手動テストも実行できます。

### 1. サーバー起動確認
```bash
curl http://localhost:8000/api/server-info/
```

### 2. プロジェクト一覧取得
```bash
# RESTful エンドポイント
curl http://localhost:8000/api/projects/

# Legacy エンドポイント
curl http://localhost:8000/api/projects/list
```

### 3. 削除済みプロジェクト一覧
```bash
# RESTful エンドポイント
curl http://localhost:8000/api/projects/deleted/

# Legacy エンドポイント
curl http://localhost:8000/api/projects/archived
```

### 4. プロジェクト作成
```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "folder_name": "test_manual",
    "project_name": "手動テストプロジェクト",
    "description": "手動テスト用",
    "tags": ["manual", "test"],
    "status": "active"
  }'
```

## CI/CDでの使用

### GitHub Actions例
```yaml
name: API Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.12
    - name: Install dependencies
      run: |
        cd app/backend
        python -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        pip install parameterized
    - name: Run tests
      run: |
        cd app/backend
        source venv/bin/activate
        ../../testing/scripts/test_runner.sh all
```

## トラブルシューティング

### よくある問題

#### 1. **ImportError: No module named 'parameterized'**
```bash
source venv/bin/activate
pip install parameterized
```

#### 2. **django.core.exceptions.ImproperlyConfigured**
```bash
export DJANGO_SETTINGS_MODULE=config.settings
```

#### 3. **テストが途中で停止する**
- ファイルパーミッションを確認
- 仮想環境が正しく有効化されているか確認

#### 4. **モックが正しく動作しない**
- `@patch`デコレータの順序を確認
- モックオブジェクトの戻り値を確認

### デバッグ方法

#### 1. **詳細ログ出力**
```bash
python manage.py test api.tests --verbosity=2
```

#### 2. **特定テストのみ実行**
```bash
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle
```

#### 3. **デバッガー使用**
```python
import pdb; pdb.set_trace()  # テストコード内に追加
```

## テスト拡張

### 新しいテストケースの追加

1. **新しいテストメソッドを追加**
```python
def test_new_feature(self):
    """新機能のテスト"""
    # テストコード
```

2. **新しいテストクラスを追加**
```python
class NewFeatureTestCase(APITestCase):
    def test_something(self):
        # テストコード
```

3. **パラメータ化テストの拡張**
```python
@parameterized.expand([
    ("case1", "param1"),
    ("case2", "param2"),
    ("case3", "param3"),  # 新しいケース追加
])
def test_parameterized(self, case_name, param):
    # テストコード
```

## テストカバレッジ

現在のテストカバレッジ:
- ✅ プロジェクト作成
- ✅ プロジェクト取得
- ✅ プロジェクト更新
- ✅ プロジェクト削除
- ✅ プロジェクト復元
- ✅ エンドポイント互換性
- ✅ エラーハンドリング
- ✅ 言語パラメータ
- ✅ パフォーマンス

### 今後追加予定:
- ファイルアップロード/ダウンロード
- データ分析実行
- 認証機能
- 権限管理

## 変更履歴

| 日付 | バージョン | 変更内容 |
|------|-----------|---------|
| 2025-07-26 | 1.0.0 | 初版作成、基本テストスイート実装 |

---

**重要**: テストを実行する前に、必ずバックエンドサーバーが停止していることを確認してください。テストは独立したテスト環境で実行されます。