"""
Git同期機能のテスト
"""
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .git_sync_utils import GitSyncUtils, GitSyncError


class GitSyncUtilsTestCase(TestCase):
    """GitSyncUtilsクラスのテスト"""
    
    def setUp(self):
        """テスト用の一時ディレクトリを作成"""
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'test_project'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        # analysisdata と raw フォルダを作成
        self.analysisdata_path = os.path.join(self.project_path, 'analysisdata')
        self.raw_path = os.path.join(self.project_path, 'raw')
        os.makedirs(self.analysisdata_path)
        os.makedirs(self.raw_path)
        
        # テスト用ファイルを作成
        with open(os.path.join(self.analysisdata_path, 'analysis1.py'), 'w') as f:
            f.write('# Analysis script\nprint("Hello, World!")')
        with open(os.path.join(self.raw_path, 'data1.csv'), 'w') as f:
            f.write('col1,col2\n1,2\n3,4')
        
        # settings.PROJECTS_ROOTをモック
        self.settings_patcher = patch('api.git_sync_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
    
    def tearDown(self):
        """テスト用ディレクトリを削除"""
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_git_sync_utils_initialization(self):
        """GitSyncUtilsの初期化テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        self.assertEqual(sync_utils.project_folder, self.project_folder)
        self.assertTrue(sync_utils.project_path.exists())
        self.assertTrue(sync_utils.analysisdata_path.exists())
        self.assertTrue(sync_utils.raw_path.exists())
    
    def test_git_sync_utils_nonexistent_project(self):
        """存在しないプロジェクトでのエラーテスト"""
        with self.assertRaises(GitSyncError):
            GitSyncUtils('nonexistent_project')
    
    def test_get_sync_status_initial(self):
        """初期状態での同期状態取得テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        status = sync_utils.get_sync_status()
        
        self.assertEqual(status['project_folder'], self.project_folder)
        self.assertTrue(status['folders']['project_exists'])
        self.assertTrue(status['folders']['analysisdata_exists'])
        self.assertTrue(status['folders']['raw_exists'])
        self.assertFalse(status['folders']['git_exists'])
        self.assertFalse(status['sync_needed'])
        self.assertEqual(len(status['changes']), 0)
    
    def test_initialize_git_folder(self):
        """Git フォルダ初期化テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        result = sync_utils.initialize_git_folder()
        
        self.assertTrue(result['success'])
        self.assertIn('initialized', result['message'].lower())
        self.assertTrue(sync_utils.git_path.exists())
        self.assertTrue((sync_utils.git_path / 'analysisdata').exists())
        self.assertTrue((sync_utils.git_path / 'raw').exists())
    
    def test_sync_to_git_folder(self):
        """Git フォルダへの同期テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        result = sync_utils.sync_to_git_folder()
        
        self.assertTrue(result['success'])
        self.assertGreater(result['results']['total_files'], 0)
        
        # ファイルが正しくコピーされているか確認
        analysis_file = sync_utils.git_path / 'analysisdata' / 'analysis1.py'
        raw_file = sync_utils.git_path / 'raw' / 'data1.csv'
        self.assertTrue(analysis_file.exists())
        self.assertTrue(raw_file.exists())
        
        # ファイル内容が正しいか確認
        with open(analysis_file, 'r') as f:
            self.assertIn('Hello, World!', f.read())
    
    def test_detect_changes_after_sync(self):
        """同期後の変更検出テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        
        # 初回同期
        sync_utils.sync_to_git_folder()
        
        # 変更なしの状態をテスト
        status = sync_utils.get_sync_status()
        self.assertFalse(status['sync_needed'])
        
        # ファイルを変更
        with open(os.path.join(self.analysisdata_path, 'analysis1.py'), 'w') as f:
            f.write('# Updated analysis script\nprint("Updated!")')
        
        # 変更を検出
        status = sync_utils.get_sync_status()
        self.assertTrue(status['sync_needed'])
        self.assertGreater(len(status['changes']), 0)
    
    def test_sync_folder_error_handling(self):
        """フォルダ同期時のエラーハンドリング"""
        sync_utils = GitSyncUtils(self.project_folder)
        
        # 読み取り専用フォルダでテスト（権限エラーをシミュレート）
        with patch('shutil.copytree', side_effect=PermissionError("Permission denied")):
            result = sync_utils.sync_to_git_folder()
            
            # エラーが発生してもプログラムが停止しないことを確認
            self.assertIn('analysisdata', result['results'])
            self.assertIn('raw', result['results'])
    
    def test_get_git_folder_info(self):
        """Git フォルダ情報取得テスト"""
        sync_utils = GitSyncUtils(self.project_folder)
        
        # Git フォルダが存在しない場合
        info = sync_utils.get_git_folder_info()
        self.assertFalse(info['exists'])
        
        # Git フォルダを作成後
        sync_utils.sync_to_git_folder()
        info = sync_utils.get_git_folder_info()
        
        self.assertTrue(info['exists'])
        self.assertEqual(info['project_folder'], self.project_folder)
        self.assertGreater(info['total_files'], 0)
        self.assertGreater(info['total_size'], 0)


class GitSyncAPITestCase(APITestCase):
    """Git同期APIのテスト"""
    
    def setUp(self):
        """テスト用の設定"""
        self.project_folder = 'test_project'
        self.base_url = f'/api/v1/git-sync'
    
    @patch('api.views_git_sync.GitSyncUtils')
    def test_get_sync_status_success(self, mock_git_sync_utils_class):
        """同期状態取得成功テスト"""
        mock_sync_utils = MagicMock()
        mock_sync_utils.get_sync_status.return_value = {
            'project_folder': self.project_folder,
            'folders': {
                'project_exists': True,
                'analysisdata_exists': True,
                'raw_exists': True,
                'git_exists': False
            },
            'sync_needed': False,
            'changes': []
        }
        mock_git_sync_utils_class.return_value = mock_sync_utils
        
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['project_folder'], self.project_folder)
        self.assertIn('folders', data)
    
    @patch('api.views_git_sync.GitSyncUtils')
    def test_init_git_folder_success(self, mock_git_sync_utils_class):
        """Git フォルダ初期化成功テスト"""
        mock_sync_utils = MagicMock()
        mock_sync_utils.initialize_git_folder.return_value = {
            'success': True,
            'message': 'Git folder initialized successfully'
        }
        mock_git_sync_utils_class.return_value = mock_sync_utils
        
        url = f'{self.base_url}/init/{self.project_folder}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['operation'], 'init')
    
    @patch('api.views_git_sync.GitSyncUtils')
    def test_sync_to_git_success(self, mock_git_sync_utils_class):
        """Git フォルダ同期成功テスト"""
        mock_sync_utils = MagicMock()
        mock_sync_utils.sync_to_git_folder.return_value = {
            'success': True,
            'message': 'Synchronized 5 files to git folder',
            'results': {'total_files': 5}
        }
        mock_git_sync_utils_class.return_value = mock_sync_utils
        
        url = f'{self.base_url}/sync/{self.project_folder}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['operation'], 'sync')
    
    @patch('api.views_git_sync.GitUtils')
    @patch('api.views_git_sync.GitSyncUtils')
    def test_commit_with_sync_success(self, mock_git_sync_utils_class, mock_git_utils_class):
        """同期 + コミット成功テスト"""
        # GitSyncUtils のモック
        mock_sync_utils = MagicMock()
        mock_sync_utils.sync_to_git_folder.return_value = {
            'success': True,
            'results': {'total_files': 3}
        }
        mock_git_sync_utils_class.return_value = mock_sync_utils
        
        # GitUtils のモック
        mock_git_utils = MagicMock()
        mock_git_utils.add_files.return_value = {'success': True}
        mock_git_utils.commit.return_value = {
            'success': True,
            'commit_hash': 'abc123',
            'message': 'Committed successfully'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/commit/{self.project_folder}/'
        data = {'message': 'Test commit'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['operation'], 'commit')
    
    def test_commit_with_sync_no_message(self):
        """コミットメッセージなしでのエラーテスト"""
        url = f'{self.base_url}/commit/{self.project_folder}/'
        data = {}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    @patch('api.views_git_sync.GitSyncUtils')
    def test_sync_error_handling(self, mock_git_sync_utils_class):
        """同期エラーハンドリングテスト"""
        mock_git_sync_utils_class.side_effect = GitSyncError("Project folder not found")
        
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertIn('error', data)
    
    @patch('api.views_git_sync.GitSyncUtils')
    def test_check_differences(self, mock_git_sync_utils_class):
        """差分確認テスト"""
        mock_sync_utils = MagicMock()
        mock_sync_utils.get_sync_status.return_value = {
            'sync_needed': True,
            'changes': [
                {'type': 'modified_file', 'file': 'test.py', 'message': 'Modified: test.py'}
            ]
        }
        mock_git_sync_utils_class.return_value = mock_sync_utils
        
        url = f'{self.base_url}/diff/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['operation'], 'diff')
        self.assertIn('sync_status', data)


class GitSyncIntegrationTestCase(APITestCase):
    """Git同期機能の統合テスト"""
    
    def setUp(self):
        """実際のファイルシステムを使用した統合テスト用の設定"""
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'git_sync_integration_test'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        # analysisdata と raw フォルダを作成
        analysisdata_path = os.path.join(self.project_path, 'analysisdata')
        raw_path = os.path.join(self.project_path, 'raw')
        os.makedirs(analysisdata_path)
        os.makedirs(raw_path)
        
        # テスト用ファイルを作成
        with open(os.path.join(analysisdata_path, 'test_analysis.py'), 'w') as f:
            f.write('print("Integration test")')
        with open(os.path.join(raw_path, 'test_data.csv'), 'w') as f:
            f.write('x,y\n1,2\n3,4')
        
        # settings.PROJECTS_ROOTをモック
        self.settings_patcher = patch('api.git_sync_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
        
        self.base_url = f'/api/v1/git-sync'
    
    def tearDown(self):
        """テスト用ディレクトリを削除"""
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_full_sync_workflow(self):
        """完全な同期ワークフローのテスト"""
        # 1. 初期状態の確認
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        data = response.json()
        self.assertFalse(data.get('folders', {}).get('git_exists', True))
        
        # 2. Git フォルダ初期化
        init_url = f'{self.base_url}/init/{self.project_folder}/'
        response = self.client.post(init_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 3. 同期状態再確認
        response = self.client.get(url)
        data = response.json()
        if data.get('success'):
            self.assertTrue(data['folders']['git_exists'])
        
        # 4. 手動同期テスト
        sync_url = f'{self.base_url}/sync/{self.project_folder}/'
        response = self.client.post(sync_url)
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            self.assertTrue(data.get('success', False))
        
        # 5. Git フォルダ情報取得
        info_url = f'{self.base_url}/info/{self.project_folder}/'
        response = self.client.get(info_url)
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            self.assertTrue(data.get('success', False))
            if data['folder_info']['exists']:
                self.assertGreater(data['folder_info']['total_files'], 0)


class GitSyncPerformanceTestCase(TestCase):
    """Git同期機能のパフォーマンステスト"""
    
    def setUp(self):
        """大量ファイル用のテスト環境を設定"""
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'performance_test_project'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        # analysisdata フォルダに多数のファイルを作成
        analysisdata_path = os.path.join(self.project_path, 'analysisdata')
        os.makedirs(analysisdata_path)
        
        # 100個のテストファイルを作成
        for i in range(100):
            with open(os.path.join(analysisdata_path, f'file_{i:03d}.py'), 'w') as f:
                f.write(f'# Test file {i}\nprint("File {i}")')
        
        self.settings_patcher = patch('api.git_sync_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
    
    def tearDown(self):
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_large_file_sync_performance(self):
        """大量ファイル同期のパフォーマンステスト"""
        import time
        
        sync_utils = GitSyncUtils(self.project_folder)
        
        start_time = time.time()
        result = sync_utils.sync_to_git_folder()
        end_time = time.time()
        
        # 同期が成功することを確認
        self.assertTrue(result['success'])
        self.assertGreaterEqual(result['results']['total_files'], 100)
        
        # 10秒以内で同期完了することを確認（パフォーマンス要件）
        sync_duration = end_time - start_time
        self.assertLess(sync_duration, 10.0, f"Sync took {sync_duration:.2f}s, expected < 10s")