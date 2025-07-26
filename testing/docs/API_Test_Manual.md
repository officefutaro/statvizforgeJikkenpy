# StatVizForge API テストマニュアル

## 目次

1. [はじめに](#はじめに)
2. [テスト環境の準備](#テスト環境の準備)
3. [基本的なテスト実行](#基本的なテスト実行)
4. [詳細なテスト実行方法](#詳細なテスト実行方法)
5. [テスト結果の見方](#テスト結果の見方)
6. [手動テスト](#手動テスト)
7. [トラブルシューティング](#トラブルシューティング)
8. [テストの追加・修正](#テストの追加修正)
9. [CI/CD統合](#cicd統合)

---

## はじめに

このマニュアルは、StatVizForge APIのテストを実行するための完全ガイドです。プログラミング初心者の方でも、ステップバイステップでテストを実行できるように作成されています。

### テストの目的

- **品質保証**: APIが期待通りに動作することを確認
- **回帰テスト**: 新しい変更が既存機能を壊していないことを確認
- **ライフサイクル検証**: プロジェクトの作成→削除→復元の流れを検証
- **互換性確認**: 新旧エンドポイントが正しく動作することを確認

---

## テスト環境の準備

### ステップ1: 前提条件の確認

以下が準備されていることを確認してください：

```bash
# Python 3.12以上
python3 --version

# プロジェクトディレクトリ
ls /home/futaro/project/StatVizForge_JikkenPy/
```

### ステップ2: バックエンドディレクトリに移動

```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
```

### ステップ3: 仮想環境の有効化

```bash
# 仮想環境を有効化
source venv/bin/activate

# 確認（プロンプトに(venv)が表示される）
echo $VIRTUAL_ENV
```

**表示例**:
```
(venv) user@hostname:~/project/StatVizForge_JikkenPy/app/backend$ echo $VIRTUAL_ENV
/home/futaro/project/StatVizForge_JikkenPy/app/backend/venv
```

### ステップ4: 必要なパッケージのインストール

```bash
# テスト用パッケージをインストール
pip install parameterized

# インストール確認
pip list | grep parameterized
```

### ステップ5: テストファイルの確認

```bash
# テストファイルが存在することを確認
ls -la api/tests.py
ls -la ../../../testing/scripts/run_tests.py
ls -la ../../../testing/scripts/test_runner.sh
```

---

## 基本的なテスト実行

### 🚀 初回テスト実行（推奨）

最も簡単な方法でテストを実行します：

```bash
# シェルスクリプトでテスト実行
../../../testing/scripts/test_runner.sh
```

**期待される出力**:
```
================================
  StatVizForge API テストスイート
================================
実行時刻: 2025-07-26 15:30:00
ログファイル: test_results_20250726_153000.log

--- 環境チェック ---
✅ 仮想環境: /home/futaro/project/StatVizForge_JikkenPy/app/backend/venv
✅ Django環境: OK
✅ 必要パッケージ: OK

--- Django APIテスト実行 ---
=== プロジェクト完全ライフサイクルテスト開始 ===

Phase 1: プロジェクト作成
✅ プロジェクト作成成功: 550e8400-e29b-41d4-a716-446655440001
...
```

### テスト実行が成功した場合

```
--- テスト完了 ---
詳細は test_results_20250726_153000.log を確認してください
```

### テスト実行が失敗した場合

```
❌ Django APIテストで失敗
```

失敗した場合は、[トラブルシューティング](#トラブルシューティング)セクションを参照してください。

---

## 詳細なテスト実行方法

### 個別テストの実行

#### 1. ライフサイクルテストのみ実行

```bash
../../testing/scripts/test_runner.sh lifecycle
```

**内容**: プロジェクトの作成→更新→削除→復元の完全なフローをテスト

#### 2. 互換性テストのみ実行

```bash
../../testing/scripts/test_runner.sh compatibility
```

**内容**: RESTful エンドポイント vs 旧エンドポイントの動作比較

#### 3. パフォーマンステストのみ実行

```bash
../../testing/scripts/test_runner.sh performance
```

**内容**: API応答時間が1秒以内であることを確認

#### 4. 手動テスト用情報表示

```bash
../../testing/scripts/test_runner.sh manual
```

**内容**: ブラウザやcurlで手動テストするためのURL一覧を表示

### Python直接実行

シェルスクリプトを使わずに、Pythonで直接実行することも可能です：

```bash
# 全テスト実行
python ../../testing/scripts/run_tests.py all

# 個別テスト実行
python ../../testing/scripts/run_tests.py lifecycle
python ../../testing/scripts/run_tests.py compatibility
python ../../testing/scripts/run_tests.py performance
```

### Django標準コマンド

Djangoの標準テストコマンドも使用できます：

```bash
# 全APIテスト実行
python manage.py test api.tests

# 特定のテストクラスのみ
python manage.py test api.tests.ProjectLifecycleTestCase

# 特定のテストメソッドのみ
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle

# 詳細ログ出力
python manage.py test api.tests --verbosity=2
```

---

## テスト結果の見方

### 成功した場合の出力

```
=== プロジェクト完全ライフサイクルテスト開始 ===

Phase 1: プロジェクト作成
✓ プロジェクト作成成功: 550e8400-e29b-41d4-a716-446655440001

Phase 2: プロジェクト詳細取得
✓ プロジェクト取得成功: テストプロジェクト

Phase 3: プロジェクト更新
✓ プロジェクト更新成功: テストプロジェクト - 更新済み

Phase 4: プロジェクト削除
✓ プロジェクト削除成功: 550e8400-e29b-41d4-a716-446655440001

Phase 5: 削除済み一覧確認
✓ 削除済み一覧取得成功: 1 件

Phase 6: プロジェクト復元
✓ プロジェクト復元成功: テストプロジェクト - 更新済み

Phase 7: 最終状態確認
✓ 最終状態確認成功: 復元日時 2025-07-26T15:30:00

=== プロジェクト完全ライフサイクルテスト完了 ===

----------------------------------------------------------------------
Ran 6 tests in 0.123s

OK
```

### 失敗した場合の出力

```
FAIL: test_complete_project_lifecycle (api.tests.ProjectLifecycleTestCase)
プロジェクト完全ライフサイクルテスト: 作成→更新→削除→復元
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/api/tests.py", line 123, in test_complete_project_lifecycle
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
AssertionError: 400 != 201

----------------------------------------------------------------------
Ran 6 tests in 0.089s

FAILED (failures=1)
```

### ログファイルの確認

詳細なログは自動生成されるファイルで確認できます：

```bash
# 最新のログファイルを確認
ls -lt ../../testing/results/test_results_*.log | head -1

# ログファイルの内容を確認
cat ../../testing/results/test_results_20250726_153000.log
```

---

## 手動テスト

自動テストに加えて、ブラウザやcurlを使った手動テストも重要です。

### 事前準備: サーバー起動

**注意**: 手動テストの前に、別のターミナルでサーバーを起動してください。

```bash
# 新しいターミナルを開いて実行
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### 基本的な手動テスト

#### 1. サーバー起動確認

```bash
curl http://localhost:8000/api/server-info/
```

**期待される結果**:
```json
{
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
```

#### 2. プロジェクト一覧取得

```bash
# RESTful エンドポイント（推奨）
curl http://localhost:8000/api/projects/

# Legacy エンドポイント（互換性確認）
curl http://localhost:8000/api/projects/list
```

#### 3. 削除済みプロジェクト一覧

```bash
# RESTful エンドポイント（推奨）
curl http://localhost:8000/api/projects/deleted/

# Legacy エンドポイント（互換性確認）
curl http://localhost:8000/api/projects/archived
```

#### 4. プロジェクト作成

```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "folder_name": "manual_test_001",
    "project_name": "手動テストプロジェクト",
    "description": "手動テスト用のプロジェクトです",
    "tags": ["manual", "test", "demo"],
    "status": "active"
  }'
```

**期待される結果**:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440002",
  "folder_name": "manual_test_001",
  "project_name": "手動テストプロジェクト",
  "description": "手動テスト用のプロジェクトです",
  "created_date": "2025-07-26T15:30:00",
  "modified_date": "2025-07-26T15:30:00",
  "status": "active",
  "tags": ["manual", "test", "demo"]
}
```

#### 5. プロジェクト削除

```bash
# 上記で作成されたプロジェクトのIDを使用
curl -X DELETE http://localhost:8000/api/projects/550e8400-e29b-41d4-a716-446655440002/
```

#### 6. プロジェクト復元

```bash
# 削除したプロジェクトを復元
curl -X POST http://localhost:8000/api/projects/550e8400-e29b-41d4-a716-446655440002/restore/
```

### ブラウザでの手動テスト

ブラウザでも簡単にテストできます：

1. **サーバー情報**: http://localhost:8000/api/server-info/
2. **プロジェクト一覧**: http://localhost:8000/api/projects/
3. **削除済み一覧**: http://localhost:8000/api/projects/deleted/

---

## トラブルシューティング

### よくある問題と解決方法

#### 1. **仮想環境エラー**

**エラー**:
```
❌ 仮想環境が有効化されていません
```

**解決方法**:
```bash
source venv/bin/activate
# プロンプトに(venv)が表示されることを確認
```

#### 2. **パッケージ不足エラー**

**エラー**:
```
ImportError: No module named 'parameterized'
```

**解決方法**:
```bash
source venv/bin/activate
pip install parameterized
```

#### 3. **Django設定エラー**

**エラー**:
```
django.core.exceptions.ImproperlyConfigured
```

**解決方法**:
```bash
export DJANGO_SETTINGS_MODULE=config.settings
python manage.py check
```

#### 4. **ファイル権限エラー**

**エラー**:
```
Permission denied: ./test_runner.sh
```

**解決方法**:
```bash
chmod +x test_runner.sh
chmod +x run_tests.py
```

#### 5. **テストが途中で停止する**

**診断方法**:
```bash
# 詳細ログで実行
python manage.py test api.tests --verbosity=2

# 特定のテストのみ実行
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle
```

#### 6. **サーバー接続エラー（手動テスト時）**

**エラー**:
```
curl: (7) Failed to connect to localhost port 8000
```

**解決方法**:
1. 別ターミナルでサーバーが起動しているか確認
2. サーバーを起動:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### デバッグ手順

#### 1. 段階的テスト実行

```bash
# 最小限のテストから開始
python manage.py test api.tests.ProjectAPIPerformanceTestCase

# 次に基本テスト
python manage.py test api.tests.ProjectLifecycleTestCase.test_error_handling_scenarios

# 最後に完全テスト
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle
```

#### 2. ログレベルの調整

```bash
# より詳細なログ
python manage.py test api.tests --verbosity=2 --debug-mode

# 最大詳細
python manage.py test api.tests --verbosity=3
```

#### 3. 個別テストメソッドの実行

```bash
# 失敗したテストのみ再実行
python manage.py test api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle
```

---

## テストの追加・修正

### 新しいテストケースの追加

#### 1. 既存テストクラスにメソッド追加

`api/tests.py`を編集：

```python
def test_my_new_feature(self):
    """新機能のテスト"""
    print("\n=== 新機能テスト開始 ===")
    
    # テストロジック
    response = self.client.get('/api/new-endpoint/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    print("✓ 新機能テスト成功")
```

#### 2. 新しいテストクラスの追加

```python
class NewFeatureTestCase(APITestCase):
    """新機能専用のテストクラス"""
    
    def setUp(self):
        """テスト前の準備"""
        # 初期化処理
        pass
    
    def test_new_feature_basic(self):
        """基本機能テスト"""
        # テストコード
        pass
    
    def test_new_feature_error(self):
        """エラーケーステスト"""
        # テストコード
        pass
```

#### 3. パラメータ化テストの追加

```python
@parameterized.expand([
    ("case1", "param1", "expected1"),
    ("case2", "param2", "expected2"),
    ("case3", "param3", "expected3"),
])
def test_parameterized_new(self, case_name, param, expected):
    """パラメータ化された新しいテスト"""
    print(f"\n=== {case_name} テスト ===")
    
    # パラメータを使用したテスト
    result = self._some_operation(param)
    self.assertEqual(result, expected)
```

### テストの修正

#### 1. 既存テストの更新

API仕様が変更された場合、対応するテストを更新：

```python
def test_complete_project_lifecycle(self):
    # 新しい仕様に合わせてテストを更新
    expected_fields = ['id', 'project_name', 'new_field']  # new_field追加
    for field in expected_fields:
        self.assertIn(field, response.data)
```

#### 2. テストデータの更新

```python
def setUp(self):
    self.test_project_data = {
        'folder_name': f'test_project_{uuid.uuid4().hex[:8]}',
        'project_name': 'テストプロジェクト',
        'description': 'ライフサイクルテスト用プロジェクト',
        'tags': ['test', 'lifecycle'],
        'status': 'active',
        'new_field': 'new_value'  # 新しいフィールド追加
    }
```

---

## CI/CD統合

### GitHub Actions設定例

`.github/workflows/api-tests.yml`を作成：

```yaml
name: API Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: |
        cd app/backend
        python -m venv venv
        source venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        pip install parameterized
    
    - name: Run tests
      run: |
        cd app/backend
        source venv/bin/activate
        python run_tests.py all
    
    - name: Upload test results
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: test-results
        path: app/backend/test_results_*.log
```

### GitLab CI設定例

`.gitlab-ci.yml`に追加：

```yaml
api_tests:
  stage: test
  image: python:3.12
  script:
    - cd app/backend
    - python -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - pip install parameterized
    - python run_tests.py all
  artifacts:
    when: always
    paths:
      - app/backend/test_results_*.log
    expire_in: 1 week
  only:
    - main
    - develop
    - merge_requests
```

### Jenkins設定例

```groovy
pipeline {
    agent any
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    cd app/backend
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    pip install parameterized
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    cd app/backend
                    source venv/bin/activate
                    ./test_runner.sh all
                '''
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'app/backend/test_results_*.log', fingerprint: true
        }
    }
}
```

---

## チェックリスト

### テスト実行前のチェック

- [ ] バックエンドディレクトリにいる
- [ ] 仮想環境が有効化されている（`(venv)`が表示）
- [ ] 必要なパッケージがインストールされている
- [ ] テストファイルが存在する
- [ ] 実行権限が設定されている

### テスト実行中のチェック

- [ ] エラーメッセージが表示されていない
- [ ] すべてのフェーズが完了している
- [ ] ✓マークが表示されている
- [ ] 最終的に「OK」が表示されている

### テスト実行後のチェック

- [ ] ログファイルが生成されている
- [ ] 失敗したテストがないか確認
- [ ] パフォーマンスが許容範囲内
- [ ] 手動テストでも動作確認済み

---

## まとめ

このマニュアルに従って、StatVizForge APIの包括的なテストを実行できます。

**重要なポイント**:
1. **必ず仮想環境を有効化する**
2. **自動テストと手動テストの両方を実行する**
3. **エラーが発生したら、トラブルシューティングセクションを参照する**
4. **新機能追加時は、対応するテストも追加する**

質問や問題がある場合は、ログファイルを確認し、必要に応じて詳細なデバッグを実行してください。