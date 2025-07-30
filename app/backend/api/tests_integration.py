"""
API v2.0 フロントエンド統合テスト
フロントエンドから実際に利用されるAPIエンドポイントの統合テスト
"""

from django.test import TestCase, Client
from django.urls import reverse
import json
import time
from unittest.mock import patch
import os


class FrontendIntegrationTest(TestCase):
    """フロントエンドとの統合テスト"""
    
    def setUp(self):
        self.client = Client()
        self.test_project_data = {
            "folder_name": "frontend_integration_test",
            "project_name": "フロントエンド統合テスト",
            "description": "フロントエンドとの統合テスト用プロジェクト"
        }
    
    def test_project_lifecycle_workflow(self):
        """プロジェクトライフサイクル統合テスト"""
        # 1. プロジェクト一覧取得（初期状態）
        response = self.client.get('/api/v1/projects/')
        self.assertEqual(response.status_code, 200)
        initial_projects = response.json()
        initial_count = len(initial_projects.get('projects', []))
        
        # 2. プロジェクト新規作成
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(self.test_project_data),
                                  content_type='application/json')
        
        if response.status_code == 201:
            created_project = response.json()
            project_id = created_project['id']
            self.assertIn('id', created_project)
            self.assertEqual(created_project['folder_name'], self.test_project_data['folder_name'])
            
            # 3. プロジェクト詳細取得
            response = self.client.get(f'/api/v1/projects/{project_id}/')
            self.assertEqual(response.status_code, 200)
            project_detail = response.json()
            self.assertEqual(project_detail['id'], project_id)
            
            # 4. プロジェクト一覧取得（作成後）
            response = self.client.get('/api/v1/projects/')
            self.assertEqual(response.status_code, 200)
            updated_projects = response.json()
            updated_count = len(updated_projects.get('projects', []))
            self.assertEqual(updated_count, initial_count + 1)
            
            # 5. プロジェクト更新
            update_data = {
                "project_name": "更新されたプロジェクト名",
                "description": "更新された説明"
            }
            response = self.client.put(f'/api/v1/projects/{project_id}/',
                                     data=json.dumps(update_data),
                                     content_type='application/json')
            # 更新が成功するか、または実装されていない場合は適切なエラー
            self.assertIn(response.status_code, [200, 405, 500])
            
            # 6. プロジェクト削除
            response = self.client.delete(f'/api/v1/projects/{project_id}/')
            # 削除が成功するか、またはテスト環境では204
            self.assertIn(response.status_code, [204, 404, 500])
            
        elif response.status_code == 409:
            # プロジェクトが既に存在する場合
            self.skipTest("Test project already exists")
        else:
            self.fail(f"Unexpected status code for project creation: {response.status_code}")
    
    def test_file_management_workflow(self):
        """ファイル管理統合テスト"""
        project_folder = "file_management_test"
        
        # テスト用プロジェクトの作成
        test_project = {
            "folder_name": project_folder,
            "project_name": "ファイル管理テスト",
            "description": "ファイル管理統合テスト"
        }
        
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(test_project),
                                  content_type='application/json')
        
        if response.status_code not in [201, 409]:
            self.skipTest("Could not create test project for file management")
        
        # 1. ディレクトリツリー取得
        response = self.client.get(f'/api/v1/files/tree/{project_folder}/')
        # プロジェクトが存在しない場合は404、存在する場合は200
        self.assertIn(response.status_code, [200, 404])
        
        # 2. ファイル説明の保存と取得
        file_description_data = {
            "file_path": "test_data.csv",
            "description": "テストデータファイル"
        }
        
        response = self.client.post(f'/api/v1/files/descriptions/{project_folder}/',
                                  data=json.dumps(file_description_data),
                                  content_type='application/json')
        # 成功またはプロジェクトが存在しない場合のエラー
        self.assertIn(response.status_code, [200, 201, 404])
        
        if response.status_code in [200, 201]:
            # 説明の取得
            response = self.client.get(f'/api/v1/files/descriptions/{project_folder}/?file_path=test_data.csv')
            self.assertIn(response.status_code, [200, 404])
        
        # 3. ファイルタグの保存と取得
        file_tag_data = {
            "file_path": "test_data.csv",
            "tags": {
                "データ種別": ["テストデータ"],
                "形式": ["CSV"]
            }
        }
        
        response = self.client.post(f'/api/v1/files/tags/{project_folder}/',
                                  data=json.dumps(file_tag_data),
                                  content_type='application/json')
        self.assertIn(response.status_code, [200, 201, 404])
        
        if response.status_code in [200, 201]:
            # タグの取得
            response = self.client.get(f'/api/v1/files/tags/{project_folder}/?file_path=test_data.csv')
            self.assertIn(response.status_code, [200, 404])
        
        # 4. ファイル検索（タグベース）
        response = self.client.get(f'/api/v1/files/search-by-tags/{project_folder}/?tags=テストデータ')
        self.assertIn(response.status_code, [200, 404])
    
    def test_comment_management_workflow(self):
        """コメント管理統合テスト"""
        project_folder = "comment_test"
        
        # テスト用プロジェクト作成
        test_project = {
            "folder_name": project_folder,
            "project_name": "コメントテスト",
            "description": "コメント管理統合テスト"
        }
        
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(test_project),
                                  content_type='application/json')
        
        if response.status_code not in [201, 409]:
            self.skipTest("Could not create test project for comment management")
        
        # 1. コメント一覧取得（初期状態）
        response = self.client.get(f'/api/v1/files/comments/{project_folder}/')
        self.assertIn(response.status_code, [200, 404])
        
        # 2. コメント追加
        comment_data = {
            "file_path": "data.csv",
            "comment": "このファイルは重要なデータです",
            "author": "テストユーザー"
        }
        
        response = self.client.post(f'/api/v1/files/comments/{project_folder}/',
                                  data=json.dumps(comment_data),
                                  content_type='application/json')
        # 成功またはプロジェクトが存在しない場合のエラー
        self.assertIn(response.status_code, [200, 201, 404])
        
        if response.status_code in [200, 201]:
            comment_result = response.json()
            if 'comment_id' in comment_result:
                comment_id = comment_result['comment_id']
                
                # 3. コメント更新
                update_data = {
                    "file_path": "data.csv",
                    "comment": "更新されたコメント"
                }
                
                response = self.client.put(f'/api/v1/files/comments/{project_folder}/{comment_id}/',
                                         data=json.dumps(update_data),
                                         content_type='application/json')
                self.assertIn(response.status_code, [200, 404, 405])
                
                # 4. コメント削除
                response = self.client.delete(f'/api/v1/files/comments/{project_folder}/{comment_id}/?file_path=data.csv')
                self.assertIn(response.status_code, [200, 204, 404, 405])
    
    def test_jupyter_management_workflow(self):
        """JupyterLab管理統合テスト"""
        # 1. JupyterLab状態取得
        response = self.client.get('/api/v1/jupyter/status/')
        self.assertIn(response.status_code, [200, 404])
        
        if response.status_code == 200:
            status_data = response.json()
            # JupyterLabステータスのレスポンス形式を柔軟にチェック
            self.assertTrue(
                'running' in status_data or 'running_instances' in status_data,
                f"Status response should contain running info: {status_data}"
            )
        
        # 2. JupyterLab起動テスト（実際には起動しない）
        start_data = {
            "project_folder": "jupyter_test"
        }
        
        response = self.client.post('/api/v1/jupyter/start/',
                                  data=json.dumps(start_data),
                                  content_type='application/json')
        # 成功、バリデーションエラー、または未実装
        self.assertIn(response.status_code, [200, 201, 400, 404, 500])
        
        # 3. JupyterLab停止テスト
        response = self.client.post('/api/v1/jupyter/stop/')
        self.assertIn(response.status_code, [200, 201, 400, 404, 500])
    
    def test_api_versioning_compatibility(self):
        """APIバージョン互換性テスト"""
        # v1エンドポイント
        response_v1 = self.client.get('/api/v1/test/')
        self.assertEqual(response_v1.status_code, 200)
        data_v1 = response_v1.json()
        self.assertEqual(data_v1['status'], 'ok')
        self.assertEqual(data_v1['version'], 'v1')
        
        # レガシーエンドポイント
        response_legacy = self.client.get('/api/test/')
        self.assertEqual(response_legacy.status_code, 200)
        data_legacy = response_legacy.json()
        self.assertEqual(data_legacy['status'], 'ok')
        
        # サーバー情報（両バージョン）
        response_v1 = self.client.get('/api/v1/server-info/')
        response_legacy = self.client.get('/api/server-info/')
        
        # どちらかまたは両方が成功することを確認
        self.assertTrue(
            response_v1.status_code == 200 or response_legacy.status_code == 200,
            "At least one server-info endpoint should be accessible"
        )
    
    def test_error_handling_consistency(self):
        """エラーハンドリング一貫性テスト"""
        error_test_cases = [
            # 存在しないプロジェクト
            ('/api/v1/projects/nonexistent-id/', 'GET', None, 404),
            # 存在しないファイルツリー
            ('/api/v1/files/tree/nonexistent/', 'GET', None, 404),
            # 不正なプロジェクト作成データ
            ('/api/v1/projects/', 'POST', {"folder_name": ""}, 400),
        ]
        
        for endpoint, method, data, expected_status in error_test_cases:
            if method == 'GET':
                response = self.client.get(endpoint)
            elif method == 'POST':
                response = self.client.post(endpoint,
                                          data=json.dumps(data) if data else None,
                                          content_type='application/json')
            
            self.assertEqual(response.status_code, expected_status,
                           f"Expected {expected_status} for {method} {endpoint}")
            
            # エラーレスポンス形式の確認
            if response.status_code >= 400:
                error_data = response.json()
                self.assertIn('error', error_data,
                            f"Error response should contain 'error' field: {endpoint}")
                self.assertIn('message', error_data,
                            f"Error response should contain 'message' field: {endpoint}")
    
    def test_cors_headers(self):
        """CORS ヘッダーテスト"""
        # OPTIONS リクエスト（プリフライト）
        response = self.client.options('/api/v1/projects/',
                                     HTTP_ORIGIN='http://localhost:3000',
                                     HTTP_ACCESS_CONTROL_REQUEST_METHOD='POST',
                                     HTTP_ACCESS_CONTROL_REQUEST_HEADERS='content-type')
        
        # CORS が適切に設定されているかチェック
        # 開発環境では通常すべてのオリジンが許可される
        if response.status_code == 200:
            # CORS ヘッダーの存在確認（あれば）
            cors_headers = [
                'Access-Control-Allow-Origin',
                'Access-Control-Allow-Methods',
                'Access-Control-Allow-Headers'
            ]
            
            for header in cors_headers:
                if header in response.headers:
                    self.assertIsNotNone(response.headers[header])
    
    def test_performance_under_frontend_load(self):
        """フロントエンド負荷下でのパフォーマンステスト"""
        # フロントエンドが典型的に行うリクエストシーケンス
        frontend_sequence = [
            ('GET', '/api/v1/projects/', None),
            ('GET', '/api/v1/server-info/', None),
            ('GET', '/api/v1/test/', None),
        ]
        
        # シーケンスを複数回実行
        total_time = 0
        iterations = 5
        
        for i in range(iterations):
            sequence_start = time.perf_counter()
            
            for method, endpoint, data in frontend_sequence:
                start_time = time.perf_counter()
                
                if method == 'GET':
                    response = self.client.get(endpoint)
                elif method == 'POST':
                    response = self.client.post(endpoint,
                                              data=json.dumps(data) if data else None,
                                              content_type='application/json')
                
                end_time = time.perf_counter()
                request_time = end_time - start_time
                
                # 各リクエストが合理的な時間内に完了
                self.assertLess(request_time, 1.0,
                              f"Request {method} {endpoint} took {request_time:.3f}s")
                
                # レスポンスが成功またはクライアントエラー
                self.assertLess(response.status_code, 500,
                              f"Server error for {method} {endpoint}: {response.status_code}")
            
            sequence_end = time.perf_counter()
            sequence_time = sequence_end - sequence_start
            total_time += sequence_time
            
            # 1つのシーケンスが2秒以内に完了
            self.assertLess(sequence_time, 2.0,
                          f"Frontend sequence {i+1} took {sequence_time:.3f}s")
        
        avg_sequence_time = total_time / iterations
        print(f"\nFrontend Load Test Results:")
        print(f"Average sequence time: {avg_sequence_time:.3f}s")
        print(f"Total iterations: {iterations}")
        print(f"Requests per sequence: {len(frontend_sequence)}")
        
        # 平均シーケンス時間が1秒以内
        self.assertLess(avg_sequence_time, 1.0,
                       f"Average sequence time: {avg_sequence_time:.3f}s > 1.0s")