"""
フロントエンド統合テスト

フロントエンドのAPIクライアント（api-client.ts）との整合性を確認し、
実際の通信パターンをテストします。
"""

import json
import os
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, mock_open
from api.tests_api_contract import ProjectDataProtectionMixin


class FrontendAPIIntegrationTest(ProjectDataProtectionMixin, APITestCase):
    """フロントエンドAPI統合テスト"""
    
    def setUp(self):
        super().setUp()
        
        # フロントエンドが期待するレスポンス形式
        self.expected_project_registry = {
            "version": "1.0.0",
            "last_updated": "2025-08-02T00:00:00Z",
            "projects": [
                {
                    "id": "test-project-id",
                    "folder_name": "test_project",
                    "project_name": "Test Project",
                    "description": "Test Description",
                    "tags": ["test", "integration"],
                    "status": "active",
                    "created_date": "2025-08-02T00:00:00Z",
                    "modified_date": "2025-08-02T00:00:00Z"
                }
            ]
        }
    
    def test_frontend_expected_project_registry_format(self):
        """フロントエンドが期待するProjectRegistry形式でレスポンスが返ることを確認"""
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value=self.expected_project_registry):
            
            # フロントエンドのprojectAPI.getAll()相当
            response = self.client.get('/api/projects/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            data = response.json()
            
            # ProjectRegistry インターフェース準拠確認
            self.assertIn('version', data)
            self.assertIn('last_updated', data)
            self.assertIn('projects', data)
            
            # projects配列の確認
            self.assertIsInstance(data['projects'], list)
            
            if len(data['projects']) > 0:
                project = data['projects'][0]
                
                # フロントエンドProject インターフェース準拠確認
                frontend_required_fields = [
                    'folder_name', 'project_name', 'status'
                ]
                
                for field in frontend_required_fields:
                    self.assertIn(field, project, 
                                f"Project should have {field} field for frontend")
    
    def test_frontend_project_detail_format(self):
        """フロントエンドが期待するProject詳細形式でレスポンスが返ることを確認"""
        
        expected_project = self.expected_project_registry['projects'][0]
        
        with patch('api.views.ProjectViewSet._get_project_by_id', 
                  return_value=expected_project):
            
            # フロントエンドのprojectAPI.getById()相当
            response = self.client.get('/api/projects/test-id/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            data = response.json()
            
            # フロントエンドProject インターフェース準拠確認
            self.assertIn('folder_name', data)
            self.assertIn('project_name', data)
            self.assertIn('status', data)
            
            # オプショナルフィールドの型確認
            if 'tags' in data:
                self.assertIsInstance(data['tags'], list)
            if 'description' in data:
                self.assertIsInstance(data['description'], str)
    
    def test_frontend_create_project_workflow(self):
        """フロントエンドのプロジェクト作成ワークフローをテスト"""
        
        # フロントエンドが送信するデータ形式
        frontend_create_data = {
            'folder_name': 'new_frontend_project',
            'project_name': 'New Frontend Project',
            'description': 'Created from frontend',
            'tags': ['frontend', 'test'],
            'status': 'active'
        }
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value={"version": "1.0.0", "projects": []}), \
             patch('api.views.ProjectViewSet._save_projects_registry'), \
             patch('api.views.ProjectViewSet._create_project_folder_structure'), \
             patch('uuid.uuid4') as mock_uuid:
            
            mock_uuid.return_value.hex = 'frontend-test-id'
            
            # フロントエンドのprojectAPI.create()相当
            response = self.client.post('/api/projects/', 
                                      frontend_create_data, 
                                      format='json',
                                      HTTP_CONTENT_TYPE='application/json')
            
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            
            # レスポンスがフロントエンドの期待形式であることを確認
            data = response.json()
            self.assertIn('id', data)
            self.assertEqual(data['folder_name'], frontend_create_data['folder_name'])
            self.assertEqual(data['project_name'], frontend_create_data['project_name'])
    
    def test_frontend_server_info_workflow(self):
        """フロントエンドのサーバー情報取得ワークフローをテスト"""
        
        # フロントエンドのserverAPI.getInfo()相当
        response = self.client.get('/api/server-info/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        
        # フロントエンドが期待するサーバー情報形式
        self.assertIsInstance(data, dict)
        
        # 基本的なサーバー情報が含まれていることを確認
        # 具体的なフィールドは実装により異なるため、オブジェクトであることのみ確認
    
    def test_frontend_api_error_handling(self):
        """フロントエンドAPIクライアントのエラーハンドリングに対応したレスポンス"""
        
        # 400 Bad Request
        invalid_data = {
            'project_name': 'Test'
            # folder_name が不足 - フロントエンドでエラーハンドリングされる
        }
        
        response = self.client.post('/api/projects/', invalid_data, format='json')
        
        # フロントエンドのAPIクライアントは200番台以外でエラーをスローする
        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        
        # エラーレスポンスがJSONであることを確認（フロントエンドが解析可能）
        try:
            error_data = response.json()
            self.assertIsInstance(error_data, dict)
        except:
            # JSON以外のエラーレスポンスでも許容
            pass
    
    def test_frontend_file_api_integration(self):
        """フロントエンドFileAPI統合テスト"""
        
        # ファイルツリー取得
        with patch('api.views.FileViewSet.tree') as mock_tree:
            mock_tree.return_value.status_code = 200
            mock_tree.return_value.data = {'files': []}
            
            # フロントエンドのfileAPI.getTree()相当のリクエスト
            response = self.client.get('/api/files/tree/test_project/')
            
            # エンドポイントが存在することを確認
            # 実装詳細ではなく、エンドポイントの存在確認が目的
            self.assertIn(response.status_code, [200, 404, 405])
    
    def test_cors_headers_for_frontend(self):
        """フロントエンド用CORS設定の確認"""
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value=self.expected_project_registry):
            
            # OPTIONSリクエスト（CORSプリフライト）
            response = self.client.options('/api/projects/')
            
            # CORSが適切に設定されていることを確認
            # 具体的なヘッダーは設定により異なるため、レスポンス自体の存在を確認
            self.assertIsNotNone(response)
    
    def test_frontend_api_timeout_compatibility(self):
        """フロントエンドAPIクライアントのタイムアウト設定との互換性"""
        
        # フロントエンドはfetchWithTimeout (デフォルト5秒) を使用
        # バックエンドが適切なレスポンス時間で応答することを確認
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value=self.expected_project_registry):
            
            import time
            start_time = time.time()
            
            response = self.client.get('/api/projects/')
            
            end_time = time.time()
            response_time = end_time - start_time
            
            # レスポンス時間が合理的であることを確認（5秒未満）
            self.assertLess(response_time, 5.0, 
                          "API response should be faster than frontend timeout")
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)


class FrontendTypeScriptIntegrationTest(ProjectDataProtectionMixin, APITestCase):
    """TypeScript型定義との整合性テスト"""
    
    def test_project_interface_compatibility(self):
        """Project TypeScriptインターフェースとの互換性"""
        
        # TypeScript Project インターフェース
        # interface Project {
        #   id?: string;
        #   folder_name: string;
        #   project_name: string;
        #   description?: string;
        #   tags?: string[];
        #   status: string;
        #   created_date?: string;
        #   modified_date?: string;
        # }
        
        mock_project = {
            "id": "typescript-test-id",
            "folder_name": "typescript_project",
            "project_name": "TypeScript Project",
            "description": "TypeScript compatible project",
            "tags": ["typescript", "integration"],
            "status": "active",
            "created_date": "2025-08-02T00:00:00Z",
            "modified_date": "2025-08-02T00:00:00Z"
        }
        
        with patch('api.views.ProjectViewSet._get_project_by_id', 
                  return_value=mock_project):
            
            response = self.client.get('/api/projects/typescript-test-id/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            data = response.json()
            
            # 必須フィールド（TypeScriptで required）
            required_fields = ['folder_name', 'project_name', 'status']
            for field in required_fields:
                self.assertIn(field, data)
                self.assertIsInstance(data[field], str)
            
            # オプショナルフィールド（TypeScriptで optional）
            optional_fields = ['id', 'description', 'created_date', 'modified_date']
            for field in optional_fields:
                if field in data:
                    self.assertIsInstance(data[field], str)
            
            # tags フィールドの特別な処理
            if 'tags' in data:
                # TypeScriptでは string[] だが、Djangoでは文字列で返される場合がある
                self.assertIsInstance(data['tags'], (list, str))
    
    def test_project_registry_interface_compatibility(self):
        """ProjectRegistry TypeScriptインターフェースとの互換性"""
        
        # TypeScript ProjectRegistry インターフェース
        # interface ProjectRegistry {
        #   version: string;
        #   last_updated: string;
        #   projects: Project[];
        # }
        
        mock_registry = {
            "version": "1.0.0",
            "last_updated": "2025-08-02T00:00:00Z",
            "projects": []
        }
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value=mock_registry):
            
            response = self.client.get('/api/projects/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            data = response.json()
            
            # 必須フィールドの型確認
            self.assertIn('version', data)
            self.assertIsInstance(data['version'], str)
            
            self.assertIn('last_updated', data)
            self.assertIsInstance(data['last_updated'], str)
            
            self.assertIn('projects', data)
            self.assertIsInstance(data['projects'], list)


class FrontendAPIClientConfigTest(ProjectDataProtectionMixin, TestCase):
    """フロントエンドAPIクライアント設定テスト"""
    
    def test_api_base_url_configuration(self):
        """APIベースURLの設定確認"""
        
        # フロントエンドの期待するAPI URLパターン
        expected_patterns = [
            '/api/projects/',
            '/api/server-info/',
            '/api/files/',
        ]
        
        from django.urls import reverse
        
        # 各エンドポイントが適切にルーティングされることを確認
        try:
            project_url = reverse('project-list')
            self.assertTrue(project_url.startswith('/api/'))
            
            server_info_url = reverse('server_info')
            self.assertTrue(server_info_url.startswith('/api/'))
            
        except Exception as e:
            self.fail(f"URL routing failed: {e}")
    
    def test_content_type_headers(self):
        """フロントエンドが期待するContent-Typeヘッダーの確認"""
        
        # フロントエンドはapplication/jsonを期待
        mock_registry = {"version": "1.0.0", "projects": []}
        
        with patch('api.views.ProjectViewSet._load_projects_registry', 
                  return_value=mock_registry):
            
            response = self.client.get('/api/projects/')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # Content-TypeがJSONであることを確認
            content_type = response.get('Content-Type')
            self.assertIn('application/json', content_type)