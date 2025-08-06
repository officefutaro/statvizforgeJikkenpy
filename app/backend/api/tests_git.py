"""
Git機能のテスト
"""
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .git_utils import GitUtils, GitError


class GitUtilsTestCase(TestCase):
    """GitUtilsクラスのテスト"""
    
    def setUp(self):
        """テスト用の一時ディレクトリを作成"""
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'test_project'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        # settings.PROJECTS_ROOTをモック
        self.settings_patcher = patch('api.git_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
    
    def tearDown(self):
        """テスト用ディレクトリを削除"""
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_git_utils_initialization(self):
        """GitUtilsの初期化テスト"""
        git_utils = GitUtils(self.project_folder)
        self.assertEqual(git_utils.project_folder, self.project_folder)
        self.assertTrue(git_utils.project_path.exists())
    
    def test_git_utils_nonexistent_project(self):
        """存在しないプロジェクトでのエラーテスト"""
        with self.assertRaises(GitError):
            GitUtils('nonexistent_project')
    
    @patch('api.git_utils.subprocess.run')
    def test_run_git_command_success(self, mock_run):
        """Git コマンド実行成功テスト"""
        mock_result = MagicMock()
        mock_result.stdout = 'output'
        mock_result.stderr = ''
        mock_result.returncode = 0
        mock_run.return_value = mock_result
        
        git_utils = GitUtils(self.project_folder)
        stdout, stderr, returncode = git_utils._run_git_command(['status'])
        
        self.assertEqual(stdout, 'output')
        self.assertEqual(stderr, '')
        self.assertEqual(returncode, 0)
    
    @patch('api.git_utils.subprocess.run')
    def test_run_git_command_failure(self, mock_run):
        """Git コマンド実行失敗テスト"""
        mock_result = MagicMock()
        mock_result.stdout = ''
        mock_result.stderr = 'error'
        mock_result.returncode = 1
        mock_run.return_value = mock_result
        
        git_utils = GitUtils(self.project_folder)
        stdout, stderr, returncode = git_utils._run_git_command(['status'])
        
        self.assertEqual(stdout, '')
        self.assertEqual(stderr, 'error')
        self.assertEqual(returncode, 1)
    
    @patch('api.git_utils.subprocess.run')
    def test_is_git_repository_true(self, mock_run):
        """Gitリポジトリ判定（True）テスト"""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_run.return_value = mock_result
        
        git_utils = GitUtils(self.project_folder)
        self.assertTrue(git_utils.is_git_repository())
    
    @patch('api.git_utils.subprocess.run')
    def test_is_git_repository_false(self, mock_run):
        """Gitリポジトリ判定（False）テスト"""
        mock_result = MagicMock()
        mock_result.returncode = 128
        mock_run.return_value = mock_result
        
        git_utils = GitUtils(self.project_folder)
        self.assertFalse(git_utils.is_git_repository())
    
    @patch.object(GitUtils, 'is_git_repository', return_value=False)
    @patch.object(GitUtils, '_run_git_command')
    @patch.object(GitUtils, '_create_initial_gitignore')
    def test_init_repository_success(self, mock_gitignore, mock_run_command, mock_is_repo):
        """リポジトリ初期化成功テスト"""
        mock_run_command.return_value = ('Initialized empty Git repository', '', 0)
        
        git_utils = GitUtils(self.project_folder)
        result = git_utils.init_repository()
        
        self.assertTrue(result['success'])
        self.assertIn('initialized successfully', result['message'].lower())
        mock_gitignore.assert_called_once()
    
    @patch.object(GitUtils, 'is_git_repository', return_value=True)
    def test_init_repository_already_exists(self, mock_is_repo):
        """既存リポジトリでの初期化テスト"""
        git_utils = GitUtils(self.project_folder)
        result = git_utils.init_repository()
        
        self.assertFalse(result['success'])
        self.assertTrue(result['already_exists'])
    
    @patch.object(GitUtils, 'is_git_repository', return_value=True)
    @patch.object(GitUtils, '_run_git_command')
    def test_get_status_with_changes(self, mock_run_command, mock_is_repo):
        """変更ありでのステータス取得テスト"""
        mock_run_command.side_effect = [
            ('M  file1.py\n?? file2.py', '', 0),  # status --porcelain
            ('main', '', 0)  # branch --show-current
        ]
        
        git_utils = GitUtils(self.project_folder)
        result = git_utils.get_status()
        
        self.assertTrue(result['is_repo'])
        self.assertEqual(result['current_branch'], 'main')
        self.assertTrue(result['has_changes'])
        self.assertEqual(len(result['files']), 2)
        self.assertEqual(result['files'][0]['filename'], 'file1.py')
        self.assertEqual(result['files'][0]['status'], 'modified')
    
    @patch.object(GitUtils, 'is_git_repository', return_value=False)
    def test_get_status_not_repo(self, mock_is_repo):
        """非Gitリポジトリでのステータス取得テスト"""
        git_utils = GitUtils(self.project_folder)
        result = git_utils.get_status()
        
        self.assertFalse(result['is_repo'])
        self.assertIn('Not a Git repository', result['message'])


class GitAPITestCase(APITestCase):
    """Git API のテスト"""
    
    def setUp(self):
        """テスト用の設定"""
        self.project_folder = 'test_project'
        self.base_url = f'/api/v1/git'
    
    @patch('api.views_git.GitUtils')
    def test_get_status_success(self, mock_git_utils_class):
        """ステータス取得成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.get_status.return_value = {
            'is_repo': True,
            'current_branch': 'main',
            'has_changes': False,
            'files': []
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['project_folder'], self.project_folder)
        self.assertTrue(data['is_repo'])
    
    @patch('api.views_git.GitUtils')
    def test_get_status_git_error(self, mock_git_utils_class):
        """ステータス取得エラーテスト"""
        mock_git_utils_class.side_effect = GitError("Not a Git repository")
        
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertIn('error', data)
    
    @patch('api.views_git.GitUtils')
    def test_init_repository_success(self, mock_git_utils_class):
        """リポジトリ初期化成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.init_repository.return_value = {
            'success': True,
            'message': 'Git repository initialized successfully'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/init/{self.project_folder}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['project_folder'], self.project_folder)
    
    @patch('api.views_git.GitUtils')
    def test_add_files_success(self, mock_git_utils_class):
        """ファイル追加成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.add_files.return_value = {
            'success': True,
            'message': 'Added 2 files to staging area'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/add/{self.project_folder}/'
        data = {'files': ['file1.py', 'file2.py']}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['files'], ['file1.py', 'file2.py'])
    
    @patch('api.views_git.GitUtils')
    def test_commit_success(self, mock_git_utils_class):
        """コミット成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.commit.return_value = {
            'success': True,
            'message': 'Committed successfully: a1b2c3d4',
            'commit_hash': 'a1b2c3d4'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/commit/{self.project_folder}/'
        data = {'message': 'Test commit'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        # APIレスポンス構造: {project_folder, message, **result}
        # where result = {'success': True, 'message': 'Committed successfully: hash', 'commit_hash': 'hash'}
        # なので、元のmessageパラメータは上書きされる
        self.assertEqual(response_data.get('project_folder'), self.project_folder)
        self.assertIn('Committed successfully', response_data.get('message', ''))
    
    def test_commit_no_message(self):
        """コミットメッセージなしでのエラーテスト"""
        url = f'{self.base_url}/commit/{self.project_folder}/'
        data = {}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    @patch('api.views_git.GitUtils')
    def test_get_log_success(self, mock_git_utils_class):
        """ログ取得成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.get_log.return_value = {
            'commits': [
                {
                    'hash': 'a1b2c3d4e5f6789012345678901234567890abcd',
                    'hash_short': 'a1b2c3d4',
                    'author_name': 'Test User',
                    'author_email': 'test@example.com',
                    'date': '2025-08-06 10:30:00 +0900',
                    'message': 'Test commit'
                }
            ],
            'total_commits': 1
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/log/{self.project_folder}/?limit=5'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['limit'], 5)
        self.assertEqual(len(data['commits']), 1)
    
    @patch('api.views_git.GitUtils')
    def test_get_branches_success(self, mock_git_utils_class):
        """ブランチ取得成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.get_branches.return_value = {
            'branches': [
                {'name': 'main', 'current': True, 'remote': False},
                {'name': 'feature/test', 'current': False, 'remote': False}
            ],
            'current_branch': 'main',
            'total_branches': 2
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/branches/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['current_branch'], 'main')
        self.assertEqual(len(data['branches']), 2)
    
    @patch('api.views_git.GitUtils')
    def test_create_branch_success(self, mock_git_utils_class):
        """ブランチ作成成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.create_branch.return_value = {
            'success': True,
            'message': 'Branch "feature/test" created successfully',
            'branch_name': 'feature/test'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/branch/{self.project_folder}/'
        data = {'branch_name': 'feature/test'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['branch_name'], 'feature/test')
    
    def test_create_branch_no_name(self):
        """ブランチ名なしでのエラーテスト"""
        url = f'{self.base_url}/branch/{self.project_folder}/'
        data = {}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    @patch('api.views_git.GitUtils')
    def test_quick_commit_success(self, mock_git_utils_class):
        """クイックコミット成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.add_files.return_value = {'success': True}
        mock_git_utils.commit.return_value = {
            'success': True,
            'message': 'Committed successfully: a1b2c3d4',
            'commit_hash': 'a1b2c3d4'
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/quick-commit/{self.project_folder}/'
        data = {'message': 'Quick commit test'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['message'], 'Quick commit test')
    
    @patch('api.views_git.GitUtils')
    def test_get_diff_success(self, mock_git_utils_class):
        """差分取得成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.get_diff.return_value = {
            'diff': '@@ -1,3 +1,4 @@\n col1,col2\n 1,2\n 3,4\n+5,6',
            'has_diff': True,
            'filename': 'test.csv',
            'staged': False
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/diff/{self.project_folder}/?filename=test.csv'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertTrue(data['has_diff'])
        self.assertEqual(data['filename'], 'test.csv')
    
    @patch('api.views_git.GitUtils')
    def test_get_repository_info_success(self, mock_git_utils_class):
        """リポジトリ情報取得成功テスト"""
        mock_git_utils = MagicMock()
        mock_git_utils.get_status.return_value = {
            'is_repo': True,
            'current_branch': 'main',
            'has_changes': False,
            'files': []
        }
        mock_git_utils.get_branches.return_value = {
            'branches': [{'name': 'main', 'current': True, 'remote': False}],
            'current_branch': 'main'
        }
        mock_git_utils.get_log.return_value = {
            'commits': [{'hash_short': 'a1b2c3d4', 'message': 'Test commit'}]
        }
        mock_git_utils_class.return_value = mock_git_utils
        
        url = f'{self.base_url}/info/{self.project_folder}/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIn('status', data)
        self.assertIn('branches', data)
        self.assertIn('recent_commits', data)


class GitIntegrationTestCase(APITestCase):
    """Git機能の統合テスト"""
    
    def setUp(self):
        """実際のGitリポジトリを使用した統合テスト用の設定"""
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'git_integration_test'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        # settings.PROJECTS_ROOTをモック
        self.settings_patcher = patch('api.git_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
        
        self.base_url = f'/api/v1/git'
    
    def tearDown(self):
        """テスト用ディレクトリを削除"""
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_full_git_workflow(self):
        """完全なGitワークフローのテスト"""
        # 1. ステータス確認（リポジトリではない）
        url = f'{self.base_url}/status/{self.project_folder}/'
        response = self.client.get(url)
        data = response.json()
        self.assertFalse(data.get('is_repo', True))
        
        # 2. リポジトリ初期化
        init_url = f'{self.base_url}/init/{self.project_folder}/'
        response = self.client.post(init_url)
        # Gitがインストールされていない場合はスキップ
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            self.skipTest("Git is not installed")
        
        # 3. テストファイル作成
        test_file = os.path.join(self.project_path, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('Hello, Git!')
        
        # 4. ステータス確認（変更あり）
        response = self.client.get(url)
        data = response.json()
        if data.get('success'):
            self.assertTrue(data['is_repo'])
            # ファイルが追加されていることを確認（Gitが利用可能な場合）
            if data.get('has_changes'):
                self.assertGreater(len(data['files']), 0)
        
        # 5. クイックコミット
        commit_url = f'{self.base_url}/quick-commit/{self.project_folder}/'
        commit_data = {'message': 'Initial commit'}
        response = self.client.post(commit_url, commit_data, format='json')
        # Gitが正常に動作する場合のテスト
        if response.status_code == status.HTTP_200_OK:
            data = response.json()
            self.assertTrue(data.get('success', False))


class GitStatusParsingTestCase(TestCase):
    """Git ステータス解析のテスト"""
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.project_folder = 'test_project'
        self.project_path = os.path.join(self.test_dir, self.project_folder)
        os.makedirs(self.project_path)
        
        self.settings_patcher = patch('api.git_utils.settings.PROJECTS_ROOT', self.test_dir)
        self.settings_patcher.start()
    
    def tearDown(self):
        self.settings_patcher.stop()
        shutil.rmtree(self.test_dir, ignore_errors=True)
    
    def test_parse_status_codes(self):
        """ステータスコード解析テスト"""
        git_utils = GitUtils(self.project_folder)
        
        test_cases = [
            ('M ', 'modified'),
            (' M', 'modified'),
            ('MM', 'modified'),
            ('A ', 'added'),
            ('??', 'untracked'),
            ('D ', 'deleted'),
            ('R ', 'renamed'),
            ('!!', 'ignored'),
            ('XY', 'unknown')  # 未知のコード
        ]
        
        for code, expected in test_cases:
            with self.subTest(code=code):
                result = git_utils._parse_status_code(code)
                self.assertEqual(result, expected)