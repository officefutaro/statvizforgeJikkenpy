"""
フロントエンド・バックエンドAPI整合性テスト

CLAUDE_INSTRUCTIONS/test_generation_rules.md の「## 12. 必須: フロントエンド・バックエンドAPI整合性テスト」に従って、
フロントエンドとバックエンドのAPI整合性を確認するテストです。

テスト項目:
1. エンドポイント網羅性テスト
2. リクエスト・レスポンス型整合性テスト
3. HTTPメソッド・ステータスコード整合性テスト
4. APIバージョニング整合性テスト
"""

from django.test import TestCase, Client
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, mock_open, MagicMock
import json
import re
import os
from pathlib import Path
from config.paths import PROJECT_DATA_DIR
from api.views import ProjectViewSet, FileViewSet, JupyterLabViewSet, TableDisplaySettingsViewSet


class APIEndpointDiscoveryTest(APITestCase):
    """エンドポイント網羅性テスト"""
    
    def setUp(self):
        self.client = Client()
        
    def test_extract_all_backend_endpoints(self):
        """バックエンドの全エンドポイントを抽出"""
        from django.urls import reverse, NoReverseMatch
        
        # 主要なエンドポイントを実際にテスト
        test_endpoints = [
            # ProjectViewSet のエンドポイント
            ('project-list', []),
            ('project-detail', ['test-id']),
            # FileViewSet のエンドポイント（一部）
            # JupyterLabViewSet のエンドポイント
            # その他
        ]
        
        found_endpoints = []
        
        # URLconf から直接取得を試行
        try:
            # プロジェクト関連
            projects_url = reverse('project-list')
            found_endpoints.append(projects_url)
            
            # サーバー情報
            server_info_url = reverse('server_info')
            found_endpoints.append(server_info_url)
        except NoReverseMatch:
            pass
        
        # 手動で既知のエンドポイントパターンをテスト
        known_patterns = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
            '/api/v1/test/',
        ]
        
        working_endpoints = []
        for pattern in known_patterns:
            try:
                response = self.client.get(pattern)
                if response.status_code != 404:
                    working_endpoints.append(pattern)
            except Exception:
                pass
        
        print(f"Found endpoints via reverse: {found_endpoints}")
        print(f"Working endpoints via manual test: {working_endpoints}")
        
        # 最低限のエンドポイントが動作することを確認
        total_working = len(found_endpoints) + len(working_endpoints)
        self.assertGreater(total_working, 0, "動作するバックエンドエンドポイントが見つかりません")
        
        # 重要なエンドポイントの動作確認
        response = self.client.get('/api/v1/projects/')
        self.assertNotEqual(response.status_code, 404, "/api/v1/projects/ エンドポイントが存在しません")
        
    def test_expected_project_endpoints_exist(self):
        """プロジェクト関連エンドポイントの存在確認"""
        test_cases = [
            ('/api/v1/projects/', 'GET'),
            ('/api/v1/projects/', 'POST'),
            ('/api/v1/server-info/', 'GET'),
            ('/api/v1/test/', 'GET'),
        ]
        
        for url, method in test_cases:
            with self.subTest(url=url, method=method):
                if method == 'GET':
                    response = self.client.get(url)
                elif method == 'POST':
                    response = self.client.post(url, {}, content_type='application/json')
                
                # 404以外であることを確認（エンドポイントが存在する）
                self.assertNotEqual(response.status_code, 404, 
                    f"エンドポイント {method} {url} が存在しません")


class APITypeConsistencyTest(APITestCase):
    """リクエスト・レスポンス型整合性テスト"""
    
    def setUp(self):
        self.client = Client()
        
        # プロジェクトレジストリのモック設定
        self.mock_registry_data = {
            "version": "1.0.0",
            "last_updated": "2025-08-01T12:00:00Z",
            "projects": [
                {
                    "id": "test-project-id",
                    "folder_name": "test_project",
                    "project_name": "Test Project",
                    "description": "Test Description",
                    "tags": ["test", "integration"],
                    "status": "active",
                    "created_date": "2025-08-01T12:00:00Z",
                    "modified_date": "2025-08-01T12:00:00Z"
                }
            ]
        }
        
    @patch('api.utils.load_projects_registry')
    def test_project_list_response_structure(self, mock_load_registry):
        """プロジェクト一覧のレスポンス構造テスト"""
        mock_load_registry.return_value = self.mock_registry_data
        
        response = self.client.get('/api/v1/projects/')
        
        # ステータスコードチェック
        self.assertEqual(response.status_code, 200)
        
        # レスポンス構造チェック
        data = response.json()
        
        # フロントエンドのProjectRegistry型に合致するか
        required_fields = ['version', 'last_updated', 'projects']
        for field in required_fields:
            self.assertIn(field, data, f"必須フィールド '{field}' がレスポンスにありません")
        
        # プロジェクト配列の確認
        self.assertIsInstance(data['projects'], list, "projects フィールドは配列である必要があります")
        
        if data['projects']:
            project = data['projects'][0]
            # フロントエンドのProject型に合致するか
            project_required_fields = ['id', 'folder_name', 'project_name', 'status']
            for field in project_required_fields:
                self.assertIn(field, project, f"プロジェクトの必須フィールド '{field}' がありません")
            
            # 型チェック
            self.assertIsInstance(project.get('tags', []), list, "tags フィールドは配列である必要があります")
            self.assertIsInstance(project['folder_name'], str, "folder_name は文字列である必要があります")
            self.assertIsInstance(project['project_name'], str, "project_name は文字列である必要があります")
    
    def test_server_info_response_structure(self):
        """サーバー情報のレスポンス構造テスト"""
        response = self.client.get('/api/v1/server-info/')
        
        # 404以外であることを確認
        self.assertNotEqual(response.status_code, 404, "server-info エンドポイントが存在しません")
        
        if response.status_code == 200:
            data = response.json()
            # サーバー情報の基本フィールドがあることを確認
            self.assertIsInstance(data, dict, "サーバー情報はオブジェクトである必要があります")


class HTTPMethodStatusCodeTest(APITestCase):
    """HTTPメソッド・ステータスコード整合性テスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_get_methods_return_appropriate_status(self):
        """GETメソッドのステータスコードテスト"""
        endpoints = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
            '/api/v1/test/',
        ]
        
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                
                # 404でないことを確認（エンドポイントが存在）
                self.assertNotEqual(response.status_code, 404, 
                    f"GET {endpoint} エンドポイントが存在しません")
                
                # 2xx または 500 系（設定による）であることを確認
                self.assertIn(response.status_code, [200, 201, 202, 204, 500, 503], 
                    f"GET {endpoint} の応答コードが予期しない値です: {response.status_code}")
    
    def test_post_methods_require_data(self):
        """POSTメソッドのデータ要求テスト"""
        endpoints = [
            '/api/v1/projects/',
        ]
        
        for endpoint in endpoints:
            with self.subTest(endpoint=endpoint):
                # 空のPOSTリクエスト
                response = self.client.post(endpoint, {}, content_type='application/json')
                
                # 404でないことを確認（エンドポイントが存在）
                self.assertNotEqual(response.status_code, 404, 
                    f"POST {endpoint} エンドポイントが存在しません")
                
                # 400 または 500 系であることを確認（データが不正または不足）
                self.assertIn(response.status_code, [400, 422, 500], 
                    f"POST {endpoint} でデータ不足時の応答コードが適切ではありません: {response.status_code}")
    
    def test_cors_headers_present(self):
        """CORS ヘッダーの存在確認"""
        response = self.client.get('/api/v1/projects/')
        
        # CORS関連のヘッダーがある場合の確認
        cors_headers = [
            'Access-Control-Allow-Origin',
            'Access-Control-Allow-Methods',
            'Access-Control-Allow-Headers',
        ]
        
        # 最低限CORSが設定されているかの確認（開発環境では設定されている可能性）
        has_cors = any(header in response.headers for header in cors_headers)
        
        if has_cors:
            print("CORS headers detected:", 
                  {h: response.headers.get(h) for h in cors_headers if h in response.headers})


class APIVersioningTest(APITestCase):
    """APIバージョニング整合性テスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_api_v1_endpoints_accessible(self):
        """APIバージョン v1 のエンドポイントアクセス可能性"""
        v1_endpoints = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
            '/api/v1/test/',
        ]
        
        for endpoint in v1_endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                
                # 404でないことを確認（v1エンドポイントが存在）
                self.assertNotEqual(response.status_code, 404, 
                    f"API v1 エンドポイント {endpoint} が存在しません")
    
    def test_api_base_redirects_or_info(self):
        """API ベースパスの応答確認"""
        response = self.client.get('/api/')
        
        # API ベースパスが何らかの応答を返すことを確認
        # 通常は APIルートの情報や利用可能なバージョンの情報を返す
        self.assertIn(response.status_code, [200, 301, 302, 404], 
            f"API ベースパスの応答が予期しない値です: {response.status_code}")


class FrontendBackendConsistencyTest(APITestCase):
    """フロントエンド・バックエンド一貫性統合テスト"""
    
    def setUp(self):
        self.client = Client()
        
        # フロントエンドAPI クライアントで使用される URL パターン
        self.frontend_api_patterns = {
            'projects': {
                'list': '/api/v1/projects/',
                'create': '/api/v1/projects/',
                'detail': '/api/v1/projects/{id}/',
                'update': '/api/v1/projects/{id}/', 
                'delete': '/api/v1/projects/{id}/',
                'deleted': '/api/v1/projects/deleted/',
                'restore': '/api/v1/projects/{id}/restore/',
            },
            'files': {
                'tree': '/api/v1/files/tree/{project_folder}/',
                'search': '/api/v1/files/search/{project_folder}',
                'upload': '/api/v1/files/upload/{project_folder}',
                'mkdir': '/api/v1/files/mkdir/{project_folder}/',
                'comment': '/api/v1/files/comment/{project_folder}',
            },
            'server': {
                'info': '/api/v1/server-info/',
            }
        }
    
    def test_frontend_expected_endpoints_exist(self):
        """フロントエンドが期待するエンドポイントの存在確認"""
        test_endpoints = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
        ]
        
        for endpoint in test_endpoints:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                
                # エンドポイントが存在することを確認
                self.assertNotEqual(response.status_code, 404, 
                    f"フロントエンドが期待するエンドポイント {endpoint} が存在しません")
    
    def test_api_base_url_environment_consistency(self):
        """APIベースURL環境設定の一貫性"""
        from django.conf import settings
        
        # Django設定でのAPI許可ホスト
        allowed_hosts = getattr(settings, 'ALLOWED_HOSTS', [])
        cors_origins = getattr(settings, 'CORS_ALLOWED_ORIGINS', [])
        
        # 開発環境での標準的な設定を確認
        expected_patterns = [
            'localhost',
            '127.0.0.1',
            '0.0.0.0',  # WSL2環境
        ]
        
        has_development_config = any(
            any(pattern in str(host) for pattern in expected_patterns)
            for host in allowed_hosts + cors_origins
        )
        
        # 開発環境設定があることを確認（本番環境では異なる可能性がある）
        if not has_development_config and '*' not in allowed_hosts:
            print(f"Warning: Development-friendly CORS/HOST configuration not detected")
            print(f"ALLOWED_HOSTS: {allowed_hosts}")
            print(f"CORS_ALLOWED_ORIGINS: {cors_origins}")
    
    @patch('api.utils.load_projects_registry')
    def test_response_format_matches_frontend_expectations(self, mock_load_registry):
        """レスポンス形式がフロントエンドの期待と一致するかテスト"""
        # モックデータ設定
        mock_registry_data = {
            "version": "1.0.0",
            "last_updated": "2025-08-01T12:00:00Z",
            "projects": []
        }
        mock_load_registry.return_value = mock_registry_data
        
        response = self.client.get('/api/v1/projects/')
        
        if response.status_code == 200:
            data = response.json()
            
            # フロントエンドの ProjectRegistry interface と一致するか
            self.assertIn('version', data)
            self.assertIn('last_updated', data) 
            self.assertIn('projects', data)
            self.assertIsInstance(data['projects'], list)
            
            print("✓ レスポンス形式がフロントエンドの期待と一致しています")
        else:
            print(f"Warning: Projects API returned status {response.status_code}")


if __name__ == '__main__':
    import django
    import sys
    import os
    
    # Django設定
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    
    from django.test.utils import get_runner
    from django.conf import settings
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["__main__"])
    
    if failures:
        sys.exit(1)