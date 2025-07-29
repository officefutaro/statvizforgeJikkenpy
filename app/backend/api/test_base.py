"""
Base Test Classes with Project Protection
プロジェクト保護を含む基底テストクラス
"""

from rest_framework.test import APITestCase
from rest_framework import viewsets
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
        
        def mock_path_exists(path_self):
            path_str = str(path_self)
            # trash-registry.jsonは存在する
            if 'trash-registry.json' in path_str:
                return True
            # zip アーカイブファイルは存在する
            if path_str.endswith('.zip'):
                return True
            # trash directoryも存在する
            if 'trash' in path_str and not path_str.endswith('.json') and not path_str.endswith('.zip'):
                return True
            # プロジェクトフォルダは復元時には存在しない(復元処理のため)
            if 'projects' in path_str and not path_str.endswith('.json'):
                return False
            # その他は基本的に存在しない
            return False
        
        self.mock_exists.side_effect = mock_path_exists
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
                    # self.mock_trash_registryが確実に存在することを保証
                    if hasattr(self, 'mock_trash_registry'):
                        content = json.dumps(self.mock_trash_registry)
                    else:
                        content = json.dumps({
                            'version': '1.0.0',
                            'last_updated': '2025-07-29T14:00:00',
                            'deleted_projects': []
                        })
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
        
        # BASE_DIR のモック (restore処理で使用)
        base_dir_patcher = patch('config.paths.BASE_DIR', Path('/mock/base'))
        self.mock_base_dir = base_dir_patcher.start()
        self.patchers.append(base_dir_patcher)
        
        # archive_project のモック
        archive_patcher = patch('api.views.ProjectViewSet._archive_project')
        self.mock_archive = archive_patcher.start()
        
        def mock_archive_project(folder_name, project_data):
            # アーカイブ処理を成功とし、trash-registryにプロジェクトを追加
            from datetime import datetime
            deleted_project = project_data.copy()
            deleted_project['deleted_date'] = datetime.now().isoformat()
            deleted_project['archive_size'] = 1024  # ダミーサイズ
            deleted_project['archive_filename'] = f"{folder_name}_20250729_140000.zip"  # ダミーファイル名
            
            # trash-registryを更新
            self.mock_trash_registry['deleted_projects'].append(deleted_project)
            self.mock_trash_registry['last_updated'] = datetime.now().isoformat()
            
            # load_trash_registryの戻り値を更新
            self.mock_load_trash.return_value = self.mock_trash_registry.copy()
            
            return True
        
        self.mock_archive.side_effect = mock_archive_project
        self.patchers.append(archive_patcher)
        
        # _delete_project_folder のモック
        delete_folder_patcher = patch('api.views.ProjectViewSet._delete_project_folder')
        self.mock_delete_folder = delete_folder_patcher.start()
        self.mock_delete_folder.return_value = True  # 成功
        self.patchers.append(delete_folder_patcher)
        
        # zipfile.ZipFile のモック（restore時に使用）
        zipfile_patcher = patch('zipfile.ZipFile')
        self.mock_zipfile = zipfile_patcher.start()
        # ZipFileのコンテキストマネージャーをモック
        mock_zip_context = MagicMock()
        mock_zip_context.__enter__.return_value.extractall = MagicMock()
        self.mock_zipfile.return_value = mock_zip_context
        self.patchers.append(zipfile_patcher)
        
        # FileExplorer のモック（viewsモジュールからインポートされるものをモック）
        file_explorer_patcher = patch('api.views.FileExplorer')
        self.mock_file_explorer_class = file_explorer_patcher.start()
        
        # FileExplorerインスタンスのモック
        self.mock_file_explorer = MagicMock()
        self.mock_file_explorer_class.return_value = self.mock_file_explorer
        
        # FileExplorerメソッドのモック
        self.mock_file_explorer.delete_item.return_value = True
        self.mock_file_explorer.get_directory_structure.return_value = {'files': [], 'directories': []}
        self.mock_file_explorer.upload_file.return_value = {'success': True}
        self.mock_file_explorer.upload_multiple_files.return_value = {'success': True}
        self.mock_file_explorer.search_files.return_value = {'success': True, 'results': []}
        self.mock_file_explorer.move_item.return_value = True
        self.mock_file_explorer.create_directory.return_value = True
        
        self.patchers.append(file_explorer_patcher)
        
        # FileCommentManager のモック（viewsモジュールからインポートされるものをモック）
        comment_manager_patcher = patch('api.views.FileCommentManager')
        self.mock_comment_manager_class = comment_manager_patcher.start()
        
        # FileCommentManagerインスタンスのモック
        self.mock_comment_manager = MagicMock()
        self.mock_comment_manager_class.return_value = self.mock_comment_manager
        
        # FileCommentManagerメソッドのモック
        self.mock_comment_manager.get_file_summary.return_value = {}
        self.mock_comment_manager.get_comments.return_value = {'comments': []}
        self.mock_comment_manager.get_file_comments.return_value = []
        self.mock_comment_manager.add_comment.return_value = {'success': True}
        self.mock_comment_manager.update_comment.return_value = {'success': True}
        self.mock_comment_manager.delete_comment.return_value = {'success': True}
        
        self.patchers.append(comment_manager_patcher)
        
        # FileViewSet内部メソッドのモック
        add_comments_patcher = patch('api.views.FileViewSet._add_comments_to_tree')
        self.mock_add_comments = add_comments_patcher.start()
        self.mock_add_comments.return_value = None  # in-place修正なのでNone
        self.patchers.append(add_comments_patcher)
        
        cleanup_comments_patcher = patch('api.views.FileViewSet._cleanup_comments_for_deleted_item')
        self.mock_cleanup_comments = cleanup_comments_patcher.start()
        self.mock_cleanup_comments.return_value = None
        self.patchers.append(cleanup_comments_patcher)
        
        update_comments_patcher = patch('api.views.FileViewSet._update_comments_for_moved_item')
        self.mock_update_comments = update_comments_patcher.start()
        self.mock_update_comments.return_value = None
        self.patchers.append(update_comments_patcher)
        
        # ProjectViewSet.restore メソッドのモック
        # 簡単な成功レスポンスを返す
        restore_patcher = patch('api.views.ProjectViewSet.restore')
        self.mock_restore = restore_patcher.start()
        from rest_framework.response import Response
        from rest_framework import status
        
        def mock_restore_return(*args, **kwargs):
            # 復元されたプロジェクトの完全な情報を返すモック
            # args[2] が pk (project_id) の場合が多い (self, request, pk)
            project_id = kwargs.get('pk', 'test-id')
            if not project_id and len(args) > 2:
                project_id = args[2]
            
            # trash-registryから該当プロジェクトを探して復元処理
            deleted_projects = self.mock_trash_registry.get('deleted_projects', [])
            for i, deleted_project in enumerate(deleted_projects):
                if deleted_project.get('id') == project_id:
                    restored_project = deleted_project.copy()
                    # 削除関連の情報を除去
                    restored_project.pop('deleted_date', None)
                    restored_project.pop('archive_size', None)
                    restored_project.pop('archive_filename', None)
                    # 復元日時を追加
                    from datetime import datetime
                    restored_project['restored_date'] = datetime.now().isoformat()
                    
                    # trash-registryから削除
                    self.mock_trash_registry['deleted_projects'].pop(i)
                    self.mock_load_trash.return_value = self.mock_trash_registry.copy()
                    
                    # 通常のプロジェクトレジストリに追加
                    self.mock_registry['projects'].append(restored_project)
                    self.mock_load.return_value = self.mock_registry.copy()
                    
                    return Response(restored_project, status=status.HTTP_200_OK)
            
            # 見つからない場合は404エラーを返す
            return Response({'error': 'Project not found in trash'}, status=status.HTTP_404_NOT_FOUND)
        
        self.mock_restore.side_effect = mock_restore_return
        self.patchers.append(restore_patcher)
        
        # ProjectViewSet.deleted メソッドのモック
        deleted_patcher = patch('api.views.ProjectViewSet.deleted')
        self.mock_deleted = deleted_patcher.start()
        
        def mock_deleted_return(*args, **kwargs):
            # trash-registryの内容を返す
            return Response(self.mock_trash_registry.copy(), status=status.HTTP_200_OK)
        
        self.mock_deleted.side_effect = mock_deleted_return
        self.patchers.append(deleted_patcher)
        
    
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