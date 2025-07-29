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
        def mock_save_projects(data):
            self.mock_registry = data.copy()
            self.mock_load.return_value = self.mock_registry.copy()
        
        save_patcher = patch('api.views.save_projects_registry', side_effect=mock_save_projects)
        self.mock_save = save_patcher.start()
        self.patchers.append(save_patcher)
        
        # load_trash_registry のモック
        load_trash_patcher = patch('api.utils.load_trash_registry')
        self.mock_load_trash = load_trash_patcher.start()
        self.mock_load_trash.return_value = self.mock_trash_registry.copy()
        self.patchers.append(load_trash_patcher)
        
        # save_trash_registry のモック
        def mock_save_trash(data):
            self.mock_trash_registry = data.copy()
            self.mock_load_trash.return_value = self.mock_trash_registry.copy()
        
        save_trash_patcher = patch('api.utils.save_trash_registry', side_effect=mock_save_trash)
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
        
        # open のモック（trash-registry.json対応）
        self.file_contents = {}  # ファイル内容を格納
        
        def mock_file_open(file_path, mode='r', *args, **kwargs):
            import json
            import io
            path_str = str(file_path)
            
            if 'trash-registry.json' in path_str:
                if 'r' in mode:
                    content = json.dumps(self.mock_trash_registry)
                    return io.StringIO(content)
                elif 'w' in mode:
                    # 書き込み用のモックを返す
                    return mock_open().return_value
            
            # その他のファイル
            return mock_open().return_value
        
        open_patcher = patch('builtins.open', side_effect=mock_file_open)
        self.mock_file = open_patcher.start()
        self.patchers.append(open_patcher)
        
        # json.dump のモック（trash-registry.json更新を捕捉）
        def mock_json_dump(data, file, *args, **kwargs):
            # ファイルパスをチェックして適切にモックレジストリを更新
            if hasattr(file, 'name') and 'trash-registry.json' in str(getattr(file, 'name', '')):
                self.mock_trash_registry = data.copy()
                self.mock_load_trash.return_value = self.mock_trash_registry.copy()
        
        json_dump_patcher = patch('json.dump', side_effect=mock_json_dump)
        self.mock_json_dump = json_dump_patcher.start()
        self.patchers.append(json_dump_patcher)
        
        # PROJECT_DATA_DIR のモック
        project_dir_patcher = patch('config.paths.PROJECT_DATA_DIR', Path('/mock/projects'))
        self.mock_project_dir = project_dir_patcher.start()
        self.patchers.append(project_dir_patcher)
        
        trash_dir_patcher = patch('config.paths.TRASH_DIR', Path('/mock/trash'))
        self.mock_trash_dir = trash_dir_patcher.start()
        self.patchers.append(trash_dir_patcher)
        
        # archive_project のモック
        archive_patcher = patch('api.views.ProjectViewSet._archive_project')
        self.mock_archive = archive_patcher.start()
        self.mock_archive.return_value = True  # 成功を返す
        self.patchers.append(archive_patcher)
    
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
    
    def move_project_to_trash(self, project_id):
        """プロジェクトをモックのtrashレジストリに移動"""
        # プロジェクトレジストリから削除
        project_to_delete = None
        self.mock_registry['projects'] = [
            p for p in self.mock_registry['projects'] 
            if p.get('id') != project_id or (project_to_delete := p, False)[1]
        ]
        
        if project_to_delete:
            # trashレジストリに追加
            from datetime import datetime
            deleted_project = project_to_delete.copy()
            deleted_project['deleted_date'] = datetime.now().isoformat()
            self.mock_trash_registry['deleted_projects'].append(deleted_project)
            self.mock_trash_registry['last_updated'] = datetime.now().isoformat()
        
        # モックの戻り値を更新
        self.mock_load.return_value = self.mock_registry.copy()
        self.mock_load_trash.return_value = self.mock_trash_registry.copy()
        
        return project_to_delete