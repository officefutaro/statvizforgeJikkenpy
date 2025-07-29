"""
Base Test Classes with Project Protection
プロジェクト保護を含む基底テストクラス
"""

from rest_framework.test import APITestCase
from unittest.mock import patch, mock_open, MagicMock
import uuid
from pathlib import Path

class MockedFileSystemTestCase(APITestCase):
    """ファイルシステムをモックする基底テストケース"""
    
    def setUp(self):
        """各テストの前にモックを設定"""
        super().setUp()
        
        # プロジェクトレジストリのモックデータ
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
        
        # パッチャーの設定
        self.patchers = []
        
        # load_projects_registry のモック
        load_patcher = patch('api.views.load_projects_registry')
        self.mock_load = load_patcher.start()
        self.mock_load.return_value = self.mock_registry.copy()
        self.patchers.append(load_patcher)
        
        # save_projects_registry のモック
        save_patcher = patch('api.views.save_projects_registry')
        self.mock_save = save_patcher.start()
        self.patchers.append(save_patcher)
        
        # load_trash_registry のモック
        load_trash_patcher = patch('api.utils.load_trash_registry')
        self.mock_load_trash = load_trash_patcher.start()
        self.mock_load_trash.return_value = self.mock_trash_registry.copy()
        self.patchers.append(load_trash_patcher)
        
        # save_trash_registry のモック
        save_trash_patcher = patch('api.utils.save_trash_registry')
        self.mock_save_trash = save_trash_patcher.start()
        self.patchers.append(save_trash_patcher)
        
        # ファイルシステム操作のモック
        path_exists_patcher = patch('pathlib.Path.exists')
        self.mock_exists = path_exists_patcher.start()
        self.mock_exists.return_value = True
        self.patchers.append(path_exists_patcher)
        
        path_mkdir_patcher = patch('pathlib.Path.mkdir')
        self.mock_mkdir = path_mkdir_patcher.start()
        self.patchers.append(path_mkdir_patcher)
        
        # shutil操作のモック
        shutil_move_patcher = patch('shutil.move')
        self.mock_move = shutil_move_patcher.start()
        self.patchers.append(shutil_move_patcher)
        
        shutil_rmtree_patcher = patch('shutil.rmtree')
        self.mock_rmtree = shutil_rmtree_patcher.start()
        self.patchers.append(shutil_rmtree_patcher)
        
        # open のモック
        open_patcher = patch('builtins.open', new_callable=mock_open)
        self.mock_file = open_patcher.start()
        self.patchers.append(open_patcher)
        
        # json.dump のモック
        json_dump_patcher = patch('json.dump')
        self.mock_json_dump = json_dump_patcher.start()
        self.patchers.append(json_dump_patcher)
        
        # PROJECT_DATA_DIR のモック
        project_dir_patcher = patch('config.paths.PROJECT_DATA_DIR', Path('/mock/projects'))
        self.mock_project_dir = project_dir_patcher.start()
        self.patchers.append(project_dir_patcher)
        
        trash_dir_patcher = patch('config.paths.TRASH_DIR', Path('/mock/trash'))
        self.mock_trash_dir = trash_dir_patcher.start()
        self.patchers.append(trash_dir_patcher)
    
    def tearDown(self):
        """各テストの後にモックを停止"""
        if hasattr(self, 'patchers'):
            for patcher in self.patchers:
                patcher.stop()
        super().tearDown()
    
    def create_test_project_data(self, folder_suffix=None):
        """テスト用プロジェクトデータを生成"""
        if folder_suffix is None:
            folder_suffix = uuid.uuid4().hex[:8]
        
        return {
            'folder_name': f'test_project_{folder_suffix}',
            'project_name': 'テストプロジェクト',
            'description': 'テスト用プロジェクト',
            'tags': ['test'],
            'status': 'active'
        }
    
    def add_project_to_mock_registry(self, project_data):
        """モックレジストリにプロジェクトを追加"""
        project = project_data.copy()
        if 'id' not in project:
            project['id'] = str(uuid.uuid4())
        if 'created_date' not in project:
            project['created_date'] = '2025-07-26T10:00:00'
        if 'modified_date' not in project:
            project['modified_date'] = '2025-07-26T10:00:00'
        
        self.mock_registry['projects'].append(project)
        self.mock_load.return_value = self.mock_registry.copy()
        return project