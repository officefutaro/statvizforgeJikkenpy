# テスト記述方法とサンプル

## テスト内容の記述場所

### メインテストファイル
- **場所**: `/app/backend/api/tests.py`
- **構造**: Django APITestCase クラス内にテストメソッドを記述

### テスト実行ファイル
- **場所**: `/testing/scripts/`
  - `test_runner.sh` - メインのテスト実行スクリプト
  - `run_tests.py` - Python版テスト実行スクリプト

### テスト結果ファイル
- **場所**: `/testing/results/`
  - `test_results_*.log` - テスト実行ログ
  - `test_report_*.md` - テスト結果レポート

## 基本的なテスト記述パターン

### 1. 単純なAPIテスト

```python
def test_プロジェクト作成_基本(self):
    """プロジェクト作成の基本テスト"""
    
    # テストデータ準備
    project_data = {
        'folder_name': 'test_basic_project',
        'project_name': '基本テストプロジェクト',
        'description': '基本テスト用の説明',
        'tags': ['test', 'basic'],
        'status': 'active'
    }
    
    # API実行
    response = self.client.post('/api/projects/', project_data)
    
    # 結果検証
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(response.data['project_name'], project_data['project_name'])
    self.assertIsNotNone(response.data['id'])
    self.assertIsNotNone(response.data['created_date'])
```

### 2. エラーケーステスト

```python
def test_プロジェクト作成_エラーケース(self):
    """不正データでのプロジェクト作成テスト"""
    
    # 不正なテストデータ
    invalid_data = {
        # folder_name が欠落
        'project_name': 'エラーテストプロジェクト',
        'description': 'エラーテスト用'
    }
    
    # API実行
    response = self.client.post('/api/projects/', invalid_data)
    
    # エラー結果検証
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertIn('error', response.data)
```

### 3. 複数ステップテスト

```python
def test_プロジェクト更新フロー(self):
    """プロジェクト作成→更新→確認のフロー"""
    
    # Step 1: プロジェクト作成
    create_data = {
        'folder_name': 'update_test_project',
        'project_name': '更新テストプロジェクト',
        'description': '更新前の説明',
        'status': 'active'
    }
    create_response = self.client.post('/api/projects/', create_data)
    self.assertEqual(create_response.status_code, 201)
    project_id = create_response.data['id']
    
    # Step 2: プロジェクト更新
    update_data = {
        'project_name': '更新済みプロジェクト',
        'description': '更新後の説明',
        'status': 'completed'
    }
    update_response = self.client.put(f'/api/projects/{project_id}/', update_data)
    self.assertEqual(update_response.status_code, 200)
    
    # Step 3: 更新結果確認
    get_response = self.client.get(f'/api/projects/{project_id}/')
    self.assertEqual(get_response.status_code, 200)
    self.assertEqual(get_response.data['project_name'], update_data['project_name'])
    self.assertEqual(get_response.data['description'], update_data['description'])
    self.assertNotEqual(
        get_response.data['modified_date'], 
        create_response.data['created_date']
    )
```

## 特殊なテストパターン

### 4. パラメータ化テスト

```python
from parameterized import parameterized

@parameterized.expand([
    ("小さなプロジェクト", "small", ["tag1"], "active"),
    ("中程度プロジェクト", "medium", ["tag1", "tag2"], "in_progress"),
    ("大きなプロジェクト", "large", ["tag1", "tag2", "tag3"], "completed"),
])
def test_プロジェクト作成_サイズ別(self, name, size, tags, status):
    """プロジェクトサイズ別の作成テスト"""
    
    project_data = {
        'folder_name': f'test_{size}_project',
        'project_name': name,
        'description': f'{size}サイズのプロジェクト',
        'tags': tags,
        'status': status
    }
    
    response = self.client.post('/api/projects/', project_data)
    
    self.assertEqual(response.status_code, 201)
    self.assertEqual(response.data['project_name'], name)
    self.assertEqual(response.data['tags'], tags)
    self.assertEqual(response.data['status'], status)
```

### 5. モックを使用したテスト

```python
from unittest.mock import patch, mock_open

@patch('api.utils.load_projects_registry')
@patch('api.utils.save_projects_registry')
@patch('builtins.open', new_callable=mock_open)
@patch('pathlib.Path.exists')
def test_プロジェクト削除_ファイルシステム(self, mock_exists, mock_file, mock_save, mock_load):
    """ファイルシステム操作を含む削除テスト"""
    
    # モックの設定
    mock_load.return_value = {
        'version': '1.0.0',
        'projects': [
            {
                'id': 'test-id-123',
                'folder_name': 'test_project',
                'project_name': 'テストプロジェクト'
            }
        ]
    }
    mock_exists.return_value = True
    
    # 削除実行
    response = self.client.delete('/api/projects/test-id-123/')
    
    # 結果検証
    self.assertEqual(response.status_code, 204)
    mock_save.assert_called_once()  # save_projects_registryが呼ばれたか確認
```

## テストヘルパーメソッドの活用

### 6. ヘルパーメソッドを使った効率的なテスト

```python
class ProjectLifecycleTestCase(APITestCase):
    
    def _create_test_project(self, name_suffix=""):
        """テストプロジェクト作成ヘルパー"""
        project_data = {
            'folder_name': f'test_project_{name_suffix}_{uuid.uuid4().hex[:8]}',
            'project_name': f'テストプロジェクト{name_suffix}',
            'description': f'テスト用プロジェクト{name_suffix}',
            'tags': ['test', name_suffix] if name_suffix else ['test'],
            'status': 'active'
        }
        
        response = self.client.post('/api/projects/', project_data)
        self.assertEqual(response.status_code, 201)
        return response.data
    
    def _delete_project(self, project_id):
        """プロジェクト削除ヘルパー"""
        response = self.client.delete(f'/api/projects/{project_id}/')
        self.assertEqual(response.status_code, 204)
    
    def _restore_project(self, project_id):
        """プロジェクト復元ヘルパー"""
        response = self.client.post(f'/api/projects/{project_id}/restore/')
        self.assertEqual(response.status_code, 200)
        return response.data
    
    def test_複数プロジェクト_ライフサイクル(self):
        """ヘルパーメソッドを使った複数プロジェクトテスト"""
        
        # 複数プロジェクト作成
        project1 = self._create_test_project("_1")
        project2 = self._create_test_project("_2")
        project3 = self._create_test_project("_3")
        
        # 選択的削除
        self._delete_project(project1['id'])
        self._delete_project(project3['id'])
        
        # 削除済み確認
        deleted_response = self.client.get('/api/projects/deleted/')
        self.assertEqual(len(deleted_response.data['deleted_projects']), 2)
        
        # 復元
        restored = self._restore_project(project1['id'])
        self.assertEqual(restored['id'], project1['id'])
```

## 実際のAPIエンドポイントテスト

### 7. RESTfulエンドポイント vs Legacy エンドポイント

```python
def test_エンドポイント互換性_一覧取得(self):
    """新旧エンドポイントの互換性テスト"""
    
    # RESTfulエンドポイント
    restful_response = self.client.get('/api/projects/')
    self.assertEqual(restful_response.status_code, 200)
    
    # Legacyエンドポイント
    legacy_response = self.client.get('/api/projects/list')
    self.assertEqual(legacy_response.status_code, 200)
    
    # 同じ構造のレスポンスかチェック
    self.assertEqual(
        list(restful_response.data.keys()),
        list(legacy_response.data.keys())
    )
    self.assertEqual(
        restful_response.data['version'],
        legacy_response.data['version']
    )
```

### 8. 削除・復元フローテスト

```python
def test_削除復元フロー_完全版(self):
    """削除から復元までの完全フローテスト"""
    
    # プロジェクト作成
    project = self._create_test_project()
    project_id = project['id']
    original_name = project['project_name']
    
    # アクティブ一覧に存在することを確認
    active_list = self.client.get('/api/projects/')
    active_ids = [p['id'] for p in active_list.data['projects']]
    self.assertIn(project_id, active_ids)
    
    # 削除実行
    self._delete_project(project_id)
    
    # アクティブ一覧から消えていることを確認
    active_list_after = self.client.get('/api/projects/')
    active_ids_after = [p['id'] for p in active_list_after.data['projects']]
    self.assertNotIn(project_id, active_ids_after)
    
    # 削除済み一覧に存在することを確認
    deleted_list = self.client.get('/api/projects/deleted/')
    deleted_ids = [p['id'] for p in deleted_list.data['deleted_projects']]
    self.assertIn(project_id, deleted_ids)
    
    # 復元実行
    restored_project = self._restore_project(project_id)
    
    # 復元されたプロジェクトの確認
    self.assertEqual(restored_project['id'], project_id)
    self.assertEqual(restored_project['project_name'], original_name)
    self.assertIsNotNone(restored_project.get('restored_date'))
    
    # アクティブ一覧に戻っていることを確認
    active_list_final = self.client.get('/api/projects/')
    active_ids_final = [p['id'] for p in active_list_final.data['projects']]
    self.assertIn(project_id, active_ids_final)
    
    # 削除済み一覧から消えていることを確認
    deleted_list_final = self.client.get('/api/projects/deleted/')
    deleted_ids_final = [p['id'] for p in deleted_list_final.data['deleted_projects']]
    self.assertNotIn(project_id, deleted_ids_final)
```

## テストの追加場所

### 既存のテストクラスに追加

```python
# api/tests.py の ProjectLifecycleTestCase クラス内に追加
class ProjectLifecycleTestCase(APITestCase):
    # ... 既存のメソッド ...
    
    def test_新しいテストケース(self):
        """新しいテストケースの説明"""
        # ここに新しいテスト内容を記述
        pass
```

### 新しいテストクラスを追加

```python
# api/tests.py の最後に追加
class NewFeatureTestCase(APITestCase):
    """新機能専用のテストクラス"""
    
    def setUp(self):
        """テスト前の準備"""
        # 初期化処理
        pass
    
    def test_新機能_基本動作(self):
        """新機能の基本動作テスト"""
        # テスト内容
        pass
```

## テスト実行とデバッグ

### 特定のテストのみ実行

```bash
# 特定のテストメソッドのみ
python manage.py test api.tests.ProjectLifecycleTestCase.test_新しいテストケース

# 特定のテストクラスのみ
python manage.py test api.tests.NewFeatureTestCase

# 詳細ログ付き
python manage.py test api.tests.ProjectLifecycleTestCase.test_新しいテストケース --verbosity=2
```

## テストの品質向上

### 良いテストの特徴

1. **明確な名前**: `test_プロジェクト作成_正常ケース`
2. **適切なコメント**: 何をテストしているかが明確
3. **独立性**: 他のテストに依存しない
4. **再現性**: 何度実行しても同じ結果
5. **適切なアサーション**: 期待する結果を明確に検証

### 避けるべきパターン

```python
# ❌ 悪い例
def test_something(self):
    response = self.client.get('/api/projects/')
    self.assertTrue(response.status_code == 200)  # 曖昧
    
# ✅ 良い例
def test_プロジェクト一覧取得_正常レスポンス(self):
    """プロジェクト一覧取得が正常に動作することを確認"""
    response = self.client.get('/api/projects/')
    
    # ステータスコード確認
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    # レスポンス構造確認
    self.assertIn('version', response.data)
    self.assertIn('projects', response.data)
    self.assertIsInstance(response.data['projects'], list)
```

この記述方法に従って、`api/tests.py`に新しいテストケースを追加していけます。