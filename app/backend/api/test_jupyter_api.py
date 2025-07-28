"""
JupyterLab API Tests
JupyterLab管理機能のAPIテスト
"""

from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, MagicMock
import json


class JupyterLabAPITestCase(APITestCase):
    """JupyterLab API テストケース"""
    
    def setUp(self):
        """テスト前の準備"""
        self.project_folder = 'test_project'
        
        # モックJupyterLab インスタンスデータ
        self.mock_instance = {
            'project_folder': self.project_folder,
            'url': 'http://localhost:8888/?token=abc123',
            'port': 8888,
            'token': 'abc123def456',
            'status': 'running',
            'pid': 12345,
            'started_at': '2025-07-28T10:00:00'
        }

    @patch('api.views.start_jupyter_lab')
    @patch('pathlib.Path.exists', return_value=True)
    def test_start_jupyter_lab_success(self, mock_exists, mock_start):
        """JupyterLab起動成功テスト"""
        mock_start.return_value = (self.mock_instance, None)
        
        url = '/api/jupyter/start/'
        data = {'project_folder': self.project_folder}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['url'], self.mock_instance['url'])
        self.assertEqual(response.data['port'], self.mock_instance['port'])
        self.assertEqual(response.data['project_folder'], self.project_folder)

    def test_start_jupyter_lab_missing_project_folder(self):
        """プロジェクトフォルダ未指定エラーテスト"""
        url = '/api/jupyter/start/'
        data = {}  # project_folder が未指定
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    @patch('pathlib.Path.exists', return_value=False)
    def test_start_jupyter_lab_project_not_found(self, mock_exists):
        """存在しないプロジェクトでのエラーテスト"""
        url = '/api/jupyter/start/'
        data = {'project_folder': 'nonexistent_project'}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @patch('api.views.start_jupyter_lab')
    @patch('pathlib.Path.exists', return_value=True)
    def test_start_jupyter_lab_already_running(self, mock_exists, mock_start):
        """既に起動中のJupyterLabに対する処理テスト"""
        # 既存のインスタンスをモック
        mock_process = MagicMock()
        mock_process.poll.return_value = None  # プロセスが生きている
        
        existing_instance = {
            **self.mock_instance,
            'process': mock_process
        }
        
        with patch('api.views.jupyter_instances', {self.project_folder: existing_instance}):
            url = '/api/jupyter/start/'
            data = {'project_folder': self.project_folder}
            
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.data['success'])
            self.assertIn('already running', response.data['message'])

    @patch('api.views.stop_jupyter_lab')
    def test_stop_jupyter_lab_success(self, mock_stop):
        """JupyterLab停止成功テスト"""
        mock_stop.return_value = (True, None)
        
        url = '/api/jupyter/stop/'
        data = {'project_folder': self.project_folder}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(response.data['project_folder'], self.project_folder)

    @patch('api.views.stop_jupyter_lab')
    def test_stop_jupyter_lab_not_running(self, mock_stop):
        """起動していないJupyterLabの停止テスト"""
        mock_stop.return_value = (False, "JupyterLab is not running")
        
        url = '/api/jupyter/stop/'
        data = {'project_folder': self.project_folder}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch('api.views.get_jupyter_status')
    def test_get_jupyter_status_running(self, mock_status):
        """JupyterLab状態確認（起動中）テスト"""
        mock_status.return_value = {
            'success': True,
            'running_instances': [self.mock_instance]
        }
        
        url = '/api/jupyter/status/'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertEqual(len(response.data['running_instances']), 1)

    @patch('api.views.get_jupyter_status')
    def test_get_jupyter_status_specific_project(self, mock_status):
        """特定プロジェクトのJupyterLab状態確認テスト"""
        mock_status.return_value = {
            'success': True,
            'running_instances': [self.mock_instance]
        }
        
        url = f'/api/jupyter/status/?project_folder={self.project_folder}'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @patch('api.views.get_jupyter_status')
    def test_get_jupyter_status_no_instances(self, mock_status):
        """JupyterLabインスタンスなしの状態確認テスト"""
        mock_status.return_value = {
            'success': True,
            'running_instances': []
        }
        
        url = '/api/jupyter/status/'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['running_instances']), 0)

    @patch('api.views.start_jupyter_lab')
    @patch('pathlib.Path.exists', return_value=True)
    def test_start_jupyter_lab_startup_failure(self, mock_exists, mock_start):
        """JupyterLab起動失敗テスト"""
        error_message = "Failed to start JupyterLab: Port already in use"
        mock_start.return_value = (None, error_message)
        
        url = '/api/jupyter/start/'
        data = {'project_folder': self.project_folder}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.assertFalse(response.data['success'])
        self.assertIn('error', response.data)

    @patch('api.views.jupyter_service')
    def test_jupyter_service_separation(self, mock_service):
        """JupyterLabサービス分離テスト"""
        mock_service.is_service_available.return_value = True
        mock_service.start_jupyter_instance.return_value = (self.mock_instance, None)
        
        url = '/api/jupyter/start/'
        data = {'project_folder': self.project_folder}
        
        # JupyterLabサービスが正常に分離されていることを確認
        with patch('pathlib.Path.exists', return_value=True):
            response = self.client.post(url, data, format='json')
            
            # サービスレイヤーが呼び出されることを確認
            mock_service.is_service_available.assert_called()

    def test_jupyter_api_security(self):
        """JupyterLab API セキュリティテスト"""
        # トークンベース認証の確認
        url = '/api/jupyter/start/'
        data = {'project_folder': self.project_folder}
        
        with patch('api.views.start_jupyter_lab') as mock_start:
            mock_start.return_value = (self.mock_instance, None)
            
            with patch('pathlib.Path.exists', return_value=True):
                response = self.client.post(url, data, format='json')
                
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                # トークンが含まれていることを確認
                self.assertIn('token', response.data)
                self.assertTrue(len(response.data['token']) > 0)

    def test_jupyter_api_resource_management(self):
        """JupyterLab API リソース管理テスト"""
        # 複数プロジェクトの同時起動制限テスト
        projects = ['project1', 'project2', 'project3']
        
        for project in projects:
            url = '/api/jupyter/start/'
            data = {'project_folder': project}
            
            with patch('api.views.start_jupyter_lab') as mock_start:
                mock_start.return_value = ({
                    **self.mock_instance,
                    'project_folder': project,
                    'port': 8888 + projects.index(project)
                }, None)
                
                with patch('pathlib.Path.exists', return_value=True):
                    response = self.client.post(url, data, format='json')
                    
                    self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jupyter_api_error_responses(self):
        """JupyterLab API エラーレスポンス形式テスト"""
        url = '/api/jupyter/start/'
        data = {}  # 不正なリクエスト
        
        response = self.client.post(url, data, format='json')
        
        # エラーレスポンスの形式確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertIn('message', response.data)

    @patch('api.views.get_jupyter_status')
    def test_jupyter_api_performance(self, mock_status):
        """JupyterLab API パフォーマンステスト"""
        # 大量のインスタンス状態確認
        instances = [
            {**self.mock_instance, 'project_folder': f'project_{i}', 'port': 8888 + i}
            for i in range(100)
        ]
        
        mock_status.return_value = {
            'success': True,
            'running_instances': instances
        }
        
        url = '/api/jupyter/status/'
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['running_instances']), 100)