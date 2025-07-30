"""
API v2.0 セキュリティテスト - Django Test Framework版
"""

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json
from .validators import FilePathValidator
from django.core.exceptions import ValidationError


class SecurityValidationTest(TestCase):
    """セキュリティバリデーションのテスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_file_path_validation(self):
        """ファイルパスバリデーションのテスト"""
        # 危険なパス
        dangerous_paths = [
            "../../../etc/passwd",
            "/etc/passwd", 
            "..\\..\\windows\\system32",
            "file\0.csv",
            "file\n.csv",
            "~/.ssh/id_rsa",
        ]
        
        for path in dangerous_paths:
            with self.assertRaises(ValidationError):
                FilePathValidator.validate_file_path(path, "test_project")
        
        # 正常なパス
        valid_paths = [
            "data/file.csv",
            "folder/subfolder/file.txt",
            "file_name-123.csv",
        ]
        
        for path in valid_paths:
            try:
                result = FilePathValidator.validate_file_path(path, "test_project")
                self.assertEqual(result, path)
            except ValidationError:
                self.fail(f"Valid path {path} was rejected")
    
    def test_project_folder_validation(self):
        """プロジェクトフォルダ名バリデーションのテスト"""
        # 無効なフォルダ名
        invalid_names = [
            "invalid/project",
            "project with spaces",
            "プロジェクト",
            "project@test", 
            "a" * 101,  # 100文字超過
            "test.project",
        ]
        
        for name in invalid_names:
            with self.assertRaises(ValidationError):
                FilePathValidator.validate_project_folder(name)
        
        # 有効なフォルダ名
        valid_names = [
            "valid_project-123",
            "PROJECT_TEST",
            "test123",
            "my-project_v1",
        ]
        
        for name in valid_names:
            try:
                result = FilePathValidator.validate_project_folder(name)
                self.assertEqual(result, name)
            except ValidationError:
                self.fail(f"Valid folder name {name} was rejected")


class APIVersioningTest(TestCase):
    """APIバージョニングのテスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_api_versioning_endpoints(self):
        """APIバージョンエンドポイントのテスト"""
        # v1エンドポイント
        response = self.client.get('/api/v1/test/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['version'], 'v1')
        
        # レガシーエンドポイント（後方互換性）
        response = self.client.get('/api/test/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'ok')


class ProjectSecurityTest(TestCase):
    """プロジェクト関連のセキュリティテスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_project_creation_validation(self):
        """プロジェクト作成時のバリデーション"""
        # 無効なフォルダ名でのプロジェクト作成
        invalid_data = {
            "folder_name": "invalid/project",
            "project_name": "テストプロジェクト",
            "description": "テスト"
        }
        
        response = self.client.post('/api/v1/projects/', 
                                  data=json.dumps(invalid_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        # 有効なデータでのプロジェクト作成
        valid_data = {
            "folder_name": "valid_test_project",
            "project_name": "テストプロジェクト",
            "description": "テスト"
        }
        
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(valid_data),
                                  content_type='application/json')
        # プロジェクトが既に存在する場合は409、新規作成の場合は201
        self.assertIn(response.status_code, [201, 409])
    
    def test_nonexistent_project_access(self):
        """存在しないプロジェクトへのアクセステスト"""
        response = self.client.get('/api/v1/projects/nonexistent-uuid/')
        self.assertEqual(response.status_code, 404)
        
        # レスポンス形式の確認
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data)


class FileSecurityTest(TestCase):
    """ファイル関連のセキュリティテスト"""
    
    def setUp(self):
        self.client = Client()
        # テスト用プロジェクトの作成
        self.project_data = {
            "folder_name": "security_test_project",
            "project_name": "セキュリティテスト",
            "description": "セキュリティテスト用プロジェクト"
        }
    
    def test_dangerous_file_path_rejection(self):
        """危険なファイルパスの拒否テスト"""
        dangerous_paths = [
            "../../../etc/passwd",
            "/etc/passwd",
            "..\\..\\windows\\system32",
        ]
        
        for path in dangerous_paths:
            data = {
                "file_path": path,
                "description": "テスト"
            }
            
            response = self.client.post(
                '/api/v1/files/descriptions/security_test_project/',
                data=json.dumps(data),
                content_type='application/json'
            )
            
            # 400 Bad Requestまたは404 Not Found（プロジェクトが存在しない場合）
            self.assertIn(response.status_code, [400, 404])


class ErrorResponseTest(TestCase):
    """エラーレスポンス形式のテスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_error_response_format(self):
        """統一エラーレスポンス形式のテスト"""
        # 存在しないプロジェクト
        response = self.client.get('/api/v1/projects/invalid-uuid/')
        self.assertEqual(response.status_code, 404)
        
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data)
        
        # 存在しないファイルパス
        response = self.client.get('/api/v1/files/tree/nonexistent/')
        self.assertEqual(response.status_code, 404)
        
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data)
    
    def test_validation_error_format(self):
        """バリデーションエラーの形式テスト"""
        # 必須フィールド欠如
        invalid_data = {"folder_name": ""}  # 空のフォルダ名
        
        response = self.client.post('/api/v1/projects/',
                                  data=json.dumps(invalid_data),
                                  content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('message', data)


class PerformanceTest(TestCase):
    """パフォーマンステスト"""
    
    def setUp(self):
        self.client = Client()
    
    def test_response_time(self):
        """レスポンス時間のテスト"""
        import time
        
        endpoints = [
            '/api/v1/projects/',
            '/api/v1/server-info/',
            '/api/v1/test/',
        ]
        
        for endpoint in endpoints:
            start = time.time()
            response = self.client.get(endpoint)
            duration = time.time() - start
            
            # 1秒以内の応答を期待
            self.assertLess(duration, 1.0, 
                          f"Endpoint {endpoint} took {duration:.2f}s (>1.0s)")
            
            # ステータスコードが200または404（存在しないリソース）
            self.assertIn(response.status_code, [200, 404])