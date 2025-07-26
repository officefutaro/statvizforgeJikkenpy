"""
API Tests for StatVizForge Project Management
プロジェクトライフサイクルと複数パターンのテスト
"""

from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings
from parameterized import parameterized
import json
import uuid
from unittest.mock import patch, mock_open
from pathlib import Path


class ProjectLifecycleTestCase(APITestCase):
    """プロジェクト完全ライフサイクルテスト"""
    
    def setUp(self):
        """テスト前の準備"""
        self.test_project_data = {
            'folder_name': f'test_project_{uuid.uuid4().hex[:8]}',
            'project_name': 'テストプロジェクト',
            'description': 'ライフサイクルテスト用プロジェクト',
            'tags': ['test', 'lifecycle'],
            'status': 'active'
        }
        
        # モックデータ
        self.mock_registry = {
            'version': '1.0.0',
            'last_updated': '2025-07-26T10:00:00',
            'projects': []
        }
        
        self.mock_trash_registry = {
            'version': '1.0.0',
            'last_updated': '2025-07-26T10:00:00',
            'deleted_projects': []
        }

    @patch('api.utils.load_projects_registry')
    @patch('api.utils.save_projects_registry')
    @patch('builtins.open', new_callable=mock_open)
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.mkdir')
    def test_complete_project_lifecycle(self, mock_mkdir, mock_exists, mock_file, 
                                      mock_save, mock_load):
        """プロジェクト完全ライフサイクルテスト: 作成→更新→削除→復元"""
        
        # セットアップ
        mock_load.return_value = self.mock_registry.copy()
        mock_exists.return_value = True
        
        print("\n=== プロジェクト完全ライフサイクルテスト開始 ===")
        
        # Phase 1: プロジェクト作成
        print("\nPhase 1: プロジェクト作成")
        project = self._create_project()
        self.assertIsNotNone(project['id'])
        self.assertEqual(project['project_name'], self.test_project_data['project_name'])
        print(f"✓ プロジェクト作成成功: {project['id']}")
        
        # Phase 2: プロジェクト詳細取得
        print("\nPhase 2: プロジェクト詳細取得")
        retrieved_project = self._get_project(project['id'])
        self.assertEqual(retrieved_project['id'], project['id'])
        print(f"✓ プロジェクト取得成功: {retrieved_project['project_name']}")
        
        # Phase 3: プロジェクト更新
        print("\nPhase 3: プロジェクト更新")
        updated_project = self._update_project(project['id'])
        self.assertIn('更新済み', updated_project['project_name'])
        print(f"✓ プロジェクト更新成功: {updated_project['project_name']}")
        
        # Phase 4: プロジェクト削除
        print("\nPhase 4: プロジェクト削除")
        self._delete_project(project['id'])
        print(f"✓ プロジェクト削除成功: {project['id']}")
        
        # Phase 5: 削除済み一覧確認
        print("\nPhase 5: 削除済み一覧確認")
        deleted_projects = self._get_deleted_projects()
        print(f"✓ 削除済み一覧取得成功: {len(deleted_projects.get('deleted_projects', []))} 件")
        
        # Phase 6: プロジェクト復元
        print("\nPhase 6: プロジェクト復元")
        restored_project = self._restore_project(project['id'])
        self.assertEqual(restored_project['id'], project['id'])
        print(f"✓ プロジェクト復元成功: {restored_project['project_name']}")
        
        # Phase 7: 最終状態確認
        print("\nPhase 7: 最終状態確認")
        final_project = self._get_project(project['id'])
        self.assertEqual(final_project['id'], project['id'])
        self.assertIsNotNone(final_project.get('restored_date'))
        print(f"✓ 最終状態確認成功: 復元日時 {final_project.get('restored_date', 'N/A')}")
        
        print("\n=== プロジェクト完全ライフサイクルテスト完了 ===")

    @parameterized.expand([
        ("RESTful_endpoints", "/api/projects/", "/api/projects/deleted/"),
        ("Legacy_endpoints", "/api/projects/list", "/api/projects/archived"),
    ])
    @patch('api.utils.load_projects_registry')
    @patch('api.utils.save_projects_registry')
    @patch('builtins.open', new_callable=mock_open)
    @patch('pathlib.Path.exists')
    def test_endpoint_compatibility(self, pattern_name, list_url, deleted_url, 
                                  mock_exists, mock_file, mock_save, mock_load):
        """RESTful vs Legacy エンドポイント互換性テスト"""
        
        mock_load.return_value = self.mock_registry.copy()
        mock_exists.return_value = True
        
        print(f"\n=== {pattern_name} 互換性テスト開始 ===")
        
        # プロジェクト一覧取得テスト
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('version', response.data)
        self.assertIn('projects', response.data)
        print(f"✓ {list_url} - 一覧取得成功")
        
        # 削除済み一覧取得テスト
        response = self.client.get(deleted_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(f"✓ {deleted_url} - 削除済み一覧取得成功")
        
        print(f"=== {pattern_name} 互換性テスト完了 ===")

    @patch('api.utils.load_projects_registry')
    @patch('api.utils.save_projects_registry')
    @patch('builtins.open', new_callable=mock_open)
    @patch('pathlib.Path.exists')
    @patch('pathlib.Path.mkdir')
    def test_multiple_projects_interaction(self, mock_mkdir, mock_exists, 
                                         mock_file, mock_save, mock_load):
        """複数プロジェクトの相互作用テスト"""
        
        mock_load.return_value = self.mock_registry.copy()
        mock_exists.return_value = True
        
        print("\n=== 複数プロジェクト相互作用テスト開始 ===")
        
        # 複数プロジェクト作成
        projects = []
        for i in range(3):
            project_data = self.test_project_data.copy()
            project_data['folder_name'] = f'test_multi_{i}_{uuid.uuid4().hex[:8]}'
            project_data['project_name'] = f'マルチテストプロジェクト{i+1}'
            
            project = self._create_project(project_data)
            projects.append(project)
            print(f"✓ プロジェクト{i+1}作成: {project['project_name']}")
        
        # 一部削除（1番目と3番目）
        self._delete_project(projects[0]['id'])
        self._delete_project(projects[2]['id'])
        print(f"✓ プロジェクト削除: {projects[0]['project_name']}, {projects[2]['project_name']}")
        
        # 1番目のプロジェクトを復元
        restored = self._restore_project(projects[0]['id'])
        print(f"✓ プロジェクト復元: {restored['project_name']}")
        
        print("=== 複数プロジェクト相互作用テスト完了 ===")

    def test_error_handling_scenarios(self):
        """エラーハンドリングシナリオテスト"""
        
        print("\n=== エラーハンドリングテスト開始 ===")
        
        # 存在しないプロジェクト取得
        fake_id = str(uuid.uuid4())
        response = self.client.get(f'/api/projects/{fake_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト取得 - 404エラー確認")
        
        # 存在しないプロジェクト削除
        response = self.client.delete(f'/api/projects/{fake_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト削除 - 404エラー確認")
        
        # 存在しないプロジェクト復元
        response = self.client.post(f'/api/projects/{fake_id}/restore/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト復元 - 404エラー確認")
        
        # 不正なリクエストデータ
        invalid_data = {'invalid_field': 'value'}
        response = self.client.post('/api/projects/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("✓ 不正なリクエストデータ - 400エラー確認")
        
        print("=== エラーハンドリングテスト完了 ===")

    def test_language_parameter_handling(self):
        """言語パラメータ処理テスト（エラーメッセージのみ）"""
        
        print("\n=== 言語パラメータテスト開始 ===")
        
        fake_id = str(uuid.uuid4())
        
        # 日本語エラーメッセージ
        response = self.client.get(f'/api/projects/{fake_id}/?lang=ja')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        if 'message' in response.data:
            print(f"✓ 日本語エラーメッセージ: {response.data['message']}")
        
        # 英語エラーメッセージ
        response = self.client.get(f'/api/projects/{fake_id}/?lang=en')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        if 'message' in response.data:
            print(f"✓ 英語エラーメッセージ: {response.data['message']}")
        
        print("=== 言語パラメータテスト完了 ===")

    # ヘルパーメソッド
    def _create_project(self, data=None):
        """プロジェクト作成ヘルパー"""
        project_data = data or self.test_project_data
        response = self.client.post('/api/projects/', project_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def _get_project(self, project_id):
        """プロジェクト取得ヘルパー"""
        response = self.client.get(f'/api/projects/{project_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def _update_project(self, project_id):
        """プロジェクト更新ヘルパー"""
        update_data = {
            'project_name': f'{self.test_project_data["project_name"]} - 更新済み',
            'description': '更新されたプロジェクト説明'
        }
        response = self.client.put(f'/api/projects/{project_id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def _delete_project(self, project_id):
        """プロジェクト削除ヘルパー"""
        response = self.client.delete(f'/api/projects/{project_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def _get_deleted_projects(self):
        """削除済みプロジェクト一覧取得ヘルパー"""
        response = self.client.get('/api/projects/deleted/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data

    def _restore_project(self, project_id):
        """プロジェクト復元ヘルパー"""
        response = self.client.post(f'/api/projects/{project_id}/restore/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data


class ProjectAPIPerformanceTestCase(APITestCase):
    """パフォーマンステスト"""
    
    @patch('api.utils.load_projects_registry')
    def test_api_response_time(self, mock_load):
        """API応答時間テスト"""
        import time
        
        mock_load.return_value = {
            'version': '1.0.0',
            'projects': []
        }
        
        print("\n=== パフォーマンステスト開始 ===")
        
        # プロジェクト一覧取得時間測定
        start_time = time.time()
        response = self.client.get('/api/projects/')
        end_time = time.time()
        
        response_time = end_time - start_time
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(response_time, 1.0)  # 1秒以内
        
        print(f"✓ プロジェクト一覧取得応答時間: {response_time:.3f}秒")
        print("=== パフォーマンステスト完了 ===")


class ProjectValidationTestCase(APITestCase):
    """プロジェクトバリデーションテスト - 実際のテスト記述例"""
    
    def test_プロジェクト名バリデーション(self):
        """プロジェクト名の長さと文字種バリデーション"""
        print("\n=== プロジェクト名バリデーションテスト開始 ===")
        
        # 正常ケース
        valid_data = {
            'folder_name': 'valid_project_folder',
            'project_name': '正常なプロジェクト名',
            'description': '正常な説明',
            'tags': ['valid'],
            'status': 'active'
        }
        response = self.client.post('/api/projects/', valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("✓ 正常なプロジェクト名 - 成功")
        
        # 空文字エラーケース
        invalid_empty = valid_data.copy()
        invalid_empty['project_name'] = ''
        response = self.client.post('/api/projects/', invalid_empty)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("✓ 空文字プロジェクト名 - エラー確認")
        
        # 長すぎる名前エラーケース
        invalid_long = valid_data.copy()
        invalid_long['project_name'] = 'あ' * 256  # 255文字超過
        response = self.client.post('/api/projects/', invalid_long)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("✓ 長すぎるプロジェクト名 - エラー確認")
        
        print("=== プロジェクト名バリデーションテスト完了 ===")
    
    def test_重複フォルダ名チェック(self):
        """フォルダ名の重複チェック"""
        print("\n=== 重複フォルダ名チェックテスト開始 ===")
        
        # 最初のプロジェクト作成
        first_project = {
            'folder_name': 'duplicate_test_folder',
            'project_name': '最初のプロジェクト',
            'description': '最初のプロジェクトの説明',
            'status': 'active'
        }
        response1 = self.client.post('/api/projects/', first_project)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        print("✓ 最初のプロジェクト作成成功")
        
        # 同じフォルダ名で2番目のプロジェクト作成（エラーになるはず）
        second_project = {
            'folder_name': 'duplicate_test_folder',  # 同じフォルダ名
            'project_name': '2番目のプロジェクト',
            'description': '2番目のプロジェクトの説明',
            'status': 'active'
        }
        response2 = self.client.post('/api/projects/', second_project)
        self.assertEqual(response2.status_code, status.HTTP_409_CONFLICT)
        self.assertIn('DUPLICATE_FOLDER', response2.data.get('error', ''))
        print("✓ 重複フォルダ名エラー確認")
        
        print("=== 重複フォルダ名チェックテスト完了 ===")
    
    @parameterized.expand([
        ("空のタグ配列", []),
        ("単一タグ", ["tag1"]),
        ("複数タグ", ["tag1", "tag2", "tag3"]),
        ("日本語タグ", ["日本語", "テスト", "サンプル"]),
        ("英数字タグ", ["test", "sample", "demo123"]),
    ])
    def test_タグ配列バリデーション(self, test_name, tags):
        """様々なタグ配列のバリデーション"""
        print(f"\n=== タグバリデーションテスト: {test_name} ===")
        
        project_data = {
            'folder_name': f'tag_test_{hash(str(tags)) % 10000}',
            'project_name': f'タグテスト - {test_name}',
            'description': f'{test_name}のテスト',
            'tags': tags,
            'status': 'active'
        }
        
        response = self.client.post('/api/projects/', project_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['tags'], tags)
        print(f"✓ {test_name} - 成功: {tags}")


class ProjectIntegrationTestCase(APITestCase):
    """統合テスト - より複雑なシナリオ"""
    
    def test_同時削除復元操作(self):
        """複数プロジェクトの同時削除・復元操作"""
        print("\n=== 同時削除復元操作テスト開始 ===")
        
        # 5つのプロジェクトを作成
        projects = []
        for i in range(5):
            project_data = {
                'folder_name': f'concurrent_test_{i}_{uuid.uuid4().hex[:8]}',
                'project_name': f'並行テストプロジェクト{i+1}',
                'description': f'並行処理テスト用プロジェクト{i+1}',
                'tags': [f'concurrent', f'test{i+1}'],
                'status': 'active'
            }
            response = self.client.post('/api/projects/', project_data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            projects.append(response.data)
            print(f"✓ プロジェクト{i+1}作成完了")
        
        # 奇数番目のプロジェクトを削除
        deleted_projects = []
        for i in range(0, 5, 2):  # 0, 2, 4番目
            response = self.client.delete(f'/api/projects/{projects[i]["id"]}/')
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            deleted_projects.append(projects[i])
            print(f"✓ プロジェクト{i+1}削除完了")
        
        # 削除済み一覧確認
        deleted_list = self.client.get('/api/projects/deleted/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        deleted_ids = [p['id'] for p in deleted_list.data.get('deleted_projects', [])]
        for deleted_project in deleted_projects:
            self.assertIn(deleted_project['id'], deleted_ids)
        print(f"✓ 削除済み一覧確認: {len(deleted_projects)}件")
        
        # 最初の削除プロジェクトを復元
        first_deleted = deleted_projects[0]
        response = self.client.post(f'/api/projects/{first_deleted["id"]}/restore/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], first_deleted['id'])
        print(f"✓ プロジェクト復元完了: {response.data['project_name']}")
        
        # 最終状態確認
        active_list = self.client.get('/api/projects/')
        active_ids = [p['id'] for p in active_list.data['projects']]
        
        # 復元されたプロジェクトがアクティブ一覧にある
        self.assertIn(first_deleted['id'], active_ids)
        
        # 偶数番目のプロジェクト（削除されていない）もアクティブ一覧にある
        for i in range(1, 5, 2):  # 1, 3番目
            self.assertIn(projects[i]['id'], active_ids)
        
        print("=== 同時削除復元操作テスト完了 ===")
    
    def test_プロジェクトライフサイクル_エラー混在(self):
        """正常操作とエラー操作が混在するライフサイクル"""
        print("\n=== エラー混在ライフサイクルテスト開始 ===")
        
        # 正常プロジェクト作成
        valid_project = {
            'folder_name': 'error_mix_test_valid',
            'project_name': '正常プロジェクト',
            'description': '正常なプロジェクト',
            'status': 'active'
        }
        response = self.client.post('/api/projects/', valid_project)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        valid_id = response.data['id']
        print("✓ 正常プロジェクト作成")
        
        # 存在しないプロジェクトの操作エラー
        fake_id = str(uuid.uuid4())
        
        # 存在しないプロジェクト取得エラー
        response = self.client.get(f'/api/projects/{fake_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト取得エラー確認")
        
        # 存在しないプロジェクト更新エラー
        response = self.client.put(f'/api/projects/{fake_id}/', {'project_name': 'new name'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト更新エラー確認")
        
        # 正常プロジェクトの更新は成功
        response = self.client.put(f'/api/projects/{valid_id}/', {'project_name': '更新済み正常プロジェクト'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✓ 正常プロジェクト更新成功")
        
        # 正常プロジェクトの削除
        response = self.client.delete(f'/api/projects/{valid_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print("✓ 正常プロジェクト削除成功")
        
        # 削除済みプロジェクトの再削除エラー
        response = self.client.delete(f'/api/projects/{valid_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 削除済みプロジェクト再削除エラー確認")
        
        # 削除済みプロジェクトの復元成功
        response = self.client.post(f'/api/projects/{valid_id}/restore/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✓ 削除済みプロジェクト復元成功")
        
        # 存在しないプロジェクトの復元エラー
        response = self.client.post(f'/api/projects/{fake_id}/restore/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("✓ 存在しないプロジェクト復元エラー確認")
        
        print("=== エラー混在ライフサイクルテスト完了 ===")


if __name__ == '__main__':
    import django
    from django.test.utils import get_runner
    from django.conf import settings
    
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["api.tests"])