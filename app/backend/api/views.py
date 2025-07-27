from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.conf import settings
from .models import Project, ProjectFile
from .serializers import ProjectSerializer, ProjectFileSerializer
from .utils import load_projects_registry, save_projects_registry
from .localization import (
    get_language_from_request, 
    create_error_response, 
    get_field_validation_message
)
from .file_explorer import FileExplorer
from .file_comments import FileCommentManager
import uuid


class ProjectViewSet(viewsets.ModelViewSet):
    """プロジェクト管理API - projects-registry.jsonファイルを直接操作"""
    queryset = Project.objects.none()  # DBは使用しない
    serializer_class = ProjectSerializer
    
    def list(self, request):
        """プロジェクト一覧取得 - projects-registry.jsonの内容を返す"""
        language = get_language_from_request(request)
        try:
            registry_data = load_projects_registry()
            return Response(registry_data)
        except Exception as e:
            return create_error_response(
                'FAILED_TO_LOAD_PROJECTS',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def create(self, request):
        """プロジェクト新規作成 - projects-registry.jsonに追加、プロジェクトフォルダとproject.jsonを作成"""
        language = get_language_from_request(request)
        
        # バリデーション
        validation_errors = {}
        new_project = request.data
        
        # 必須フィールドチェック
        required_fields = ['folder_name', 'project_name', 'description']
        for field in required_fields:
            if not new_project.get(field):
                validation_errors[field] = get_field_validation_message(
                    field, 'required', language
                )
        
        # プロジェクト名の長さチェック
        if new_project.get('project_name') and len(new_project['project_name']) > 255:
            validation_errors['project_name'] = get_field_validation_message(
                'project_name', 'max_length', language
            )
        
        if validation_errors:
            return create_error_response(
                'VALIDATION_ERROR',
                language,
                details=validation_errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            registry_data = load_projects_registry()
            
            # フォルダ名の重複チェック
            existing_folders = [p.get('folder_name') for p in registry_data['projects']]
            if new_project['folder_name'] in existing_folders:
                return create_error_response(
                    'DUPLICATE_FOLDER',
                    language,
                    status_code=status.HTTP_409_CONFLICT
                )
            
            # UUIDを自動生成
            new_project['id'] = str(uuid.uuid4())
            
            # 日時を追加
            from datetime import datetime
            now = datetime.now().isoformat()
            new_project['created_date'] = now
            new_project['modified_date'] = now
            
            # プロジェクトフォルダ構造を作成
            self._create_project_folder_structure(new_project['folder_name'], new_project)
            
            # projects-registry.jsonを更新
            registry_data['projects'].append(new_project)
            registry_data['last_updated'] = now
            save_projects_registry(registry_data)
            
            return Response(new_project, status=status.HTTP_201_CREATED)
        except Exception as e:
            return create_error_response(
                'FAILED_TO_CREATE_PROJECT',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _create_project_folder_structure(self, folder_name, project_data):
        """プロジェクトフォルダ構造を作成"""
        import os
        import json
        from pathlib import Path
        from config.paths import PROJECT_DATA_DIR
        
        # プロジェクトフォルダパス
        project_folder = PROJECT_DATA_DIR / folder_name
        
        # フォルダ構造を作成
        project_folder.mkdir(exist_ok=True)
        (project_folder / 'raw').mkdir(exist_ok=True)
        (project_folder / 'db').mkdir(exist_ok=True)
        (project_folder / 'analysisdata').mkdir(exist_ok=True)
        (project_folder / 'git').mkdir(exist_ok=True)
        
        # project.jsonファイルを作成
        project_json_data = {
            'folder_name': project_data['folder_name'],
            'project_name': project_data['project_name'],
            'description': project_data['description'],
            'created_date': project_data['created_date'],
            'modified_date': project_data['modified_date'],
            'tags': project_data.get('tags', []),
            'status': project_data.get('status', 'active')
        }
        
        project_json_path = project_folder / 'project.json'
        with open(project_json_path, 'w', encoding='utf-8') as f:
            json.dump(project_json_data, f, ensure_ascii=False, indent=2)
    
    def retrieve(self, request, pk=None):
        """プロジェクト詳細取得"""
        try:
            registry_data = load_projects_registry()
            project = next((p for p in registry_data['projects'] if p.get('id') == pk), None)
            
            if not project:
                return Response(
                    {'error': 'Project not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            return Response(project)
        except Exception as e:
            return Response(
                {'error': f'Failed to retrieve project: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def update(self, request, pk=None):
        """プロジェクト更新"""
        try:
            registry_data = load_projects_registry()
            project_index = next((i for i, p in enumerate(registry_data['projects']) if p.get('id') == pk), None)
            
            if project_index is None:
                return Response(
                    {'error': 'Project not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # 更新
            from datetime import datetime
            updated_project = {**registry_data['projects'][project_index], **request.data}
            updated_project['modified_date'] = datetime.now().isoformat()
            registry_data['projects'][project_index] = updated_project
            registry_data['last_updated'] = datetime.now().isoformat()
            
            save_projects_registry(registry_data)
            return Response(updated_project)
        except Exception as e:
            return Response(
                {'error': f'Failed to update project: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def destroy(self, request, pk=None):
        """プロジェクト削除 - プロジェクトをzipアーカイブしてtrashに移動"""
        language = get_language_from_request(request)
        
        try:
            registry_data = load_projects_registry()
            project_index = next((i for i, p in enumerate(registry_data['projects']) if p.get('id') == pk), None)
            
            if project_index is None:
                return create_error_response(
                    'PROJECT_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            # 削除対象プロジェクト情報を取得
            from datetime import datetime
            deleted_project = registry_data['projects'][project_index]
            folder_name = deleted_project['folder_name']
            
            # プロジェクトフォルダをzipアーカイブ
            archived = self._archive_project(folder_name, deleted_project)
            
            if not archived:
                return create_error_response(
                    'FAILED_TO_ARCHIVE_PROJECT',
                    language,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # プロジェクトフォルダを削除
            self._delete_project_folder(folder_name)
            
            # projects-registry.jsonから削除
            deleted_project['deletion_date'] = datetime.now().isoformat()
            deleted_project['reason'] = 'ユーザー削除'
            
            # アーカイブ済みプロジェクトリストに追加
            if 'archived_projects' not in registry_data:
                registry_data['archived_projects'] = []
            registry_data['archived_projects'].append(deleted_project)
            
            # アクティブプロジェクトから削除
            registry_data['projects'].pop(project_index)
            registry_data['last_updated'] = datetime.now().isoformat()
            
            save_projects_registry(registry_data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return create_error_response(
                'FAILED_TO_DELETE_PROJECT',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _archive_project(self, folder_name, project_data):
        """プロジェクトフォルダをzipアーカイブしてtrashに保存"""
        import zipfile
        import os
        import json
        from pathlib import Path
        from datetime import datetime
        from config.paths import PROJECT_DATA_DIR, BASE_DIR
        
        # プロジェクトフォルダパス
        project_folder = PROJECT_DATA_DIR / folder_name
        
        if not project_folder.exists():
            return False
        
        # trashディレクトリ確認・作成
        trash_dir = BASE_DIR / 'project' / 'trash'
        trash_dir.mkdir(parents=True, exist_ok=True)
        
        # zipファイル名（フォルダ名_日時.zip）
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        zip_filename = f"{folder_name}_{timestamp}.zip"
        zip_path = trash_dir / zip_filename
        
        try:
            # zipファイル作成
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # プロジェクトフォルダ内のすべてのファイルを追加
                for root, dirs, files in os.walk(project_folder):
                    for file in files:
                        file_path = Path(root) / file
                        arcname = file_path.relative_to(project_folder.parent)
                        zipf.write(file_path, arcname)
            
            # プロジェクトデータに追加情報を保存
            project_data['archive_filename'] = zip_filename
            project_data['archive_path'] = str(zip_path)
            project_data['archive_size'] = os.path.getsize(zip_path)
            
            # trash-registry.jsonを更新
            trash_registry_path = trash_dir / 'trash-registry.json'
            trash_registry = {'version': '1.0.0', 'deleted_projects': []}
            
            if trash_registry_path.exists():
                with open(trash_registry_path, 'r', encoding='utf-8') as f:
                    trash_registry = json.load(f)
            
            # 削除プロジェクト情報を追加
            deleted_info = {
                'id': project_data.get('id'),
                'folder_name': folder_name,
                'project_name': project_data.get('project_name'),
                'archive_filename': zip_filename,
                'archive_size': project_data['archive_size'],
                'deletion_date': datetime.now().isoformat(),
                'original_created_date': project_data.get('created_date'),
                'tags': project_data.get('tags', []),
                'description': project_data.get('description', '')
            }
            
            trash_registry['deleted_projects'].append(deleted_info)
            trash_registry['last_updated'] = datetime.now().isoformat()
            
            # trash-registry.jsonを保存
            with open(trash_registry_path, 'w', encoding='utf-8') as f:
                json.dump(trash_registry, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"Failed to archive project: {e}")
            return False
    
    def _delete_project_folder(self, folder_name):
        """プロジェクトフォルダを削除"""
        import shutil
        from pathlib import Path
        from config.paths import PROJECT_DATA_DIR
        
        project_folder = PROJECT_DATA_DIR / folder_name
        
        if project_folder.exists():
            try:
                shutil.rmtree(project_folder)
                return True
            except Exception as e:
                print(f"Failed to delete project folder: {e}")
                return False
        return True
    
    @action(detail=False, methods=['get'])
    def deleted(self, request):
        """削除済みプロジェクト一覧を取得"""
        language = get_language_from_request(request)
        
        try:
            from pathlib import Path
            import json
            from config.paths import BASE_DIR
            
            trash_dir = BASE_DIR / 'project' / 'trash'
            trash_registry_path = trash_dir / 'trash-registry.json'
            
            if not trash_registry_path.exists():
                return Response({
                    'version': '1.0.0',
                    'deleted_projects': [],
                    'last_updated': None
                })
            
            with open(trash_registry_path, 'r', encoding='utf-8') as f:
                trash_registry = json.load(f)
            
            return Response(trash_registry)
        except Exception as e:
            return create_error_response(
                'FAILED_TO_LOAD_DELETED_PROJECTS',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        """プロジェクトを復元 - trashからzipファイルを展開して復元"""
        language = get_language_from_request(request)
        
        try:
            from pathlib import Path
            import json
            import zipfile
            import shutil
            from datetime import datetime
            from config.paths import BASE_DIR, PROJECT_DATA_DIR
            
            # trash-registry.jsonを読み込み
            trash_dir = BASE_DIR / 'project' / 'trash'
            trash_registry_path = trash_dir / 'trash-registry.json'
            
            if not trash_registry_path.exists():
                return create_error_response(
                    'NO_DELETED_PROJECTS',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            with open(trash_registry_path, 'r', encoding='utf-8') as f:
                trash_registry = json.load(f)
            
            # 対象プロジェクトを検索
            deleted_project = None
            project_index = None
            for i, project in enumerate(trash_registry.get('deleted_projects', [])):
                if project['id'] == pk:
                    deleted_project = project
                    project_index = i
                    break
            
            if not deleted_project:
                return create_error_response(
                    'DELETED_PROJECT_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            # zipファイルの確認
            zip_filename = deleted_project['archive_filename']
            zip_path = trash_dir / zip_filename
            
            if not zip_path.exists():
                return create_error_response(
                    'ARCHIVE_FILE_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            # プロジェクトフォルダが既に存在するかチェック
            folder_name = deleted_project['folder_name']
            project_folder = PROJECT_DATA_DIR / folder_name
            
            if project_folder.exists():
                return create_error_response(
                    'PROJECT_FOLDER_ALREADY_EXISTS',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            # zipファイルを展開
            try:
                with zipfile.ZipFile(zip_path, 'r') as zipf:
                    zipf.extractall(PROJECT_DATA_DIR.parent)
            except Exception as e:
                return create_error_response(
                    'FAILED_TO_EXTRACT_ARCHIVE',
                    language,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # projects-registry.jsonに復元
            registry_data = load_projects_registry()
            
            # 復元するプロジェクトデータを作成
            restored_project = {
                'id': deleted_project['id'],
                'folder_name': deleted_project['folder_name'],
                'project_name': deleted_project['project_name'],
                'description': deleted_project.get('description', ''),
                'tags': deleted_project.get('tags', []),
                'status': 'active',
                'created_date': deleted_project.get('original_created_date', datetime.now().isoformat()),
                'modified_date': datetime.now().isoformat(),
                'restored_date': datetime.now().isoformat()
            }
            
            registry_data['projects'].append(restored_project)
            registry_data['last_updated'] = datetime.now().isoformat()
            
            save_projects_registry(registry_data)
            
            # trash-registry.jsonから削除
            trash_registry['deleted_projects'].pop(project_index)
            trash_registry['last_updated'] = datetime.now().isoformat()
            
            with open(trash_registry_path, 'w', encoding='utf-8') as f:
                json.dump(trash_registry, f, ensure_ascii=False, indent=2)
            
            # アーカイブファイルを削除（オプション：保持する場合はこの行をコメントアウト）
            # zip_path.unlink()
            
            return Response(restored_project)
            
        except Exception as e:
            return create_error_response(
                'FAILED_TO_RESTORE_PROJECT',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FileViewSet(viewsets.ModelViewSet):
    """ファイル操作API"""
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_explorer = FileExplorer()
        self.comment_manager = FileCommentManager()
    
    @action(detail=False, methods=['get'], url_path='tree/(?P<project_folder>[^/.]+)')
    def directory_tree(self, request, project_folder=None):
        """プロジェクトのディレクトリツリーを取得"""
        language = get_language_from_request(request)
        path = request.query_params.get('path', '')
        
        try:
            tree_data = self.file_explorer.get_directory_structure(project_folder, path)
            if 'error' in tree_data:
                return create_error_response(
                    'PATH_NOT_FOUND' if tree_data['error'] == 'Path not found' else 'PROJECT_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            # コメント情報を追加
            comment_summary = self.comment_manager.get_file_summary(project_folder)
            self._add_comments_to_tree(tree_data, comment_summary)
            
            return Response(tree_data)
        except Exception as e:
            return create_error_response(
                'FAILED_TO_GET_DIRECTORY',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['post'], url_path='upload/(?P<project_folder>[^/.]+)')
    def upload(self, request, project_folder=None):
        """ファイルアップロード"""
        language = get_language_from_request(request)
        
        if not project_folder:
            return create_error_response(
                'PROJECT_FOLDER_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        files = request.FILES.getlist('files')
        if not files:
            return create_error_response(
                'NO_FILES_PROVIDED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        target_path = request.data.get('target_path', '')
        
        try:
            if len(files) == 1:
                # 単一ファイル
                result = self.file_explorer.upload_file(project_folder, files[0], target_path)
            else:
                # 複数ファイル
                result = self.file_explorer.upload_multiple_files(project_folder, files, target_path)
            
            if result.get('success'):
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return create_error_response(
                    'UPLOAD_FAILED',
                    language,
                    details=result,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return create_error_response(
                'UPLOAD_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    
    def _add_comments_to_tree(self, node: dict, comment_summary: dict, current_path: str = ''):
        """ツリーノードにコメント情報を追加する再帰関数"""
        node_path = current_path + '/' + node['name'] if current_path else node['name']
        node_path = node_path.lstrip('/')
        
        # このノードのコメント情報を追加
        if node_path in comment_summary:
            node['comment_count'] = comment_summary[node_path]['comment_count']
            node['has_comments'] = comment_summary[node_path]['has_comments']
        else:
            node['comment_count'] = 0
            node['has_comments'] = False
        
        # 子ノードも処理
        if 'children' in node:
            for child in node['children']:
                self._add_comments_to_tree(child, comment_summary, node_path)

    @action(detail=False, methods=['get', 'post'], url_path='comments/(?P<project_folder>[^/.]+)')
    def file_comments(self, request, project_folder=None):
        """ファイルコメント管理"""
        language = get_language_from_request(request)
        
        if request.method == 'GET':
            file_path = request.query_params.get('file_path')
            if file_path:
                # 特定ファイルのコメント取得
                comments = self.comment_manager.get_file_comments(project_folder, file_path)
                return Response({'comments': comments})
            else:
                # 全コメント情報取得
                all_comments = self.comment_manager.get_all_comments(project_folder)
                return Response(all_comments)
        
        elif request.method == 'POST':
            # 新しいコメント追加
            file_path = request.data.get('file_path')
            comment_text = request.data.get('comment')
            author = request.data.get('author', 'Anonymous')
            
            if not file_path or not comment_text:
                return create_error_response(
                    'MISSING_REQUIRED_FIELDS',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            result = self.comment_manager.add_comment(project_folder, file_path, comment_text, author)
            
            if result['success']:
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return create_error_response(
                    'FAILED_TO_ADD_COMMENT',
                    language,
                    details=result,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    @action(detail=False, methods=['put', 'delete'], url_path='comments/(?P<project_folder>[^/.]+)/(?P<comment_id>[^/.]+)')
    def comment_detail(self, request, project_folder=None, comment_id=None):
        """個別コメントの更新・削除"""
        language = get_language_from_request(request)
        file_path = request.data.get('file_path') or request.query_params.get('file_path')
        
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        if request.method == 'PUT':
            # コメント更新
            new_text = request.data.get('comment')
            if not new_text:
                return create_error_response(
                    'COMMENT_TEXT_REQUIRED',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            result = self.comment_manager.update_comment(project_folder, file_path, comment_id, new_text)
            
            if result['success']:
                return Response(result)
            else:
                return create_error_response(
                    'FAILED_TO_UPDATE_COMMENT',
                    language,
                    details=result,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        elif request.method == 'DELETE':
            # コメント削除
            result = self.comment_manager.delete_comment(project_folder, file_path, comment_id)
            
            if result['success']:
                return Response({'success': True})
            else:
                return create_error_response(
                    'FAILED_TO_DELETE_COMMENT',
                    language,
                    details=result,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    @action(detail=False, methods=['delete'], url_path='delete/(?P<project_folder>[^/.]+)')
    def delete_file(self, request, project_folder=None):
        """ファイル・ディレクトリ削除"""
        language = get_language_from_request(request)
        file_path = request.data.get('file_path') or request.query_params.get('file_path')
        
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.file_explorer.delete_item(project_folder, file_path)
            if result:
                # コメントも一緒に削除（ファイルの場合）
                self._cleanup_comments_for_deleted_item(project_folder, file_path)
                
                return Response({
                    'success': True,
                    'message': 'Item deleted successfully'
                })
            else:
                return create_error_response(
                    'DELETE_FAILED',
                    language,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return create_error_response(
                'DELETE_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'], url_path='move/(?P<project_folder>[^/.]+)')
    def move_file(self, request, project_folder=None):
        """ファイル・ディレクトリ移動"""
        language = get_language_from_request(request)
        source_path = request.data.get('source_path')
        destination_path = request.data.get('destination_path')
        
        if not source_path or not destination_path:
            return create_error_response(
                'SOURCE_AND_DESTINATION_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.file_explorer.move_item(project_folder, source_path, destination_path)
            if result:
                # コメントのパスも更新
                self._update_comments_for_moved_item(project_folder, source_path, destination_path)
                
                return Response({
                    'success': True,
                    'message': 'Item moved successfully',
                    'new_path': destination_path
                })
            else:
                return create_error_response(
                    'MOVE_FAILED',
                    language,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return create_error_response(
                'MOVE_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['post'], url_path='mkdir/(?P<project_folder>[^/.]+)')
    def create_directory(self, request, project_folder=None):
        """新規ディレクトリ作成"""
        language = get_language_from_request(request)
        dir_path = request.data.get('dir_path')
        
        if not dir_path:
            return create_error_response(
                'DIRECTORY_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.file_explorer.create_directory(project_folder, dir_path)
            if result:
                return Response({
                    'success': True,
                    'message': 'Directory created successfully',
                    'path': dir_path
                })
            else:
                return create_error_response(
                    'CREATE_DIRECTORY_FAILED',
                    language,
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as e:
            return create_error_response(
                'CREATE_DIRECTORY_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def _cleanup_comments_for_deleted_item(self, project_folder: str, file_path: str):
        """削除されたアイテムのコメントをクリーンアップ"""
        try:
            comments_data = self.comment_manager.load_comments(project_folder)
            paths_to_remove = []
            
            # 削除されたパスとその子パスのコメントを特定
            for comment_path in comments_data['comments'].keys():
                if comment_path == file_path or comment_path.startswith(file_path + '/'):
                    paths_to_remove.append(comment_path)
            
            # コメントを削除
            for path in paths_to_remove:
                del comments_data['comments'][path]
            
            self.comment_manager.save_comments(project_folder, comments_data)
        except Exception:
            # コメント削除に失敗してもファイル削除は成功とする
            pass

    def _update_comments_for_moved_item(self, project_folder: str, old_path: str, new_path: str):
        """移動されたアイテムのコメントパスを更新"""
        try:
            comments_data = self.comment_manager.load_comments(project_folder)
            updated_comments = {}
            
            # パスを更新
            for comment_path, comments in comments_data['comments'].items():
                if comment_path == old_path:
                    # 完全一致の場合
                    updated_comments[new_path] = comments
                elif comment_path.startswith(old_path + '/'):
                    # 子パスの場合
                    relative_path = comment_path[len(old_path):]
                    updated_comments[new_path + relative_path] = comments
                else:
                    # 無関係なパス
                    updated_comments[comment_path] = comments
            
            comments_data['comments'] = updated_comments
            self.comment_manager.save_comments(project_folder, comments_data)
        except Exception:
            # コメント更新に失敗してもファイル移動は成功とする
            pass

    @action(detail=False, methods=['get'], url_path='search/(?P<project_folder>[^/.]+)')
    def search_files(self, request, project_folder=None):
        """ファイル検索"""
        language = get_language_from_request(request)
        query = request.query_params.get('q', '').strip()
        search_type = request.query_params.get('type', 'name')  # name, content, both
        
        if not query:
            return create_error_response(
                'SEARCH_QUERY_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        if search_type not in ['name', 'content', 'both']:
            return create_error_response(
                'INVALID_SEARCH_TYPE',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            results = self.file_explorer.search_files(project_folder, query, search_type)
            
            if 'error' in results:
                return create_error_response(
                    'SEARCH_FAILED',
                    language,
                    details={'error': results['error']},
                    status_code=status.HTTP_404_NOT_FOUND if 'not found' in results['error'].lower() else status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # コメント情報を追加
            comment_summary = self.comment_manager.get_file_summary(project_folder)
            for result in results['results']:
                file_path = result['path']
                if file_path in comment_summary:
                    result['comment_count'] = comment_summary[file_path]['comment_count']
                    result['has_comments'] = comment_summary[file_path]['has_comments']
                else:
                    result['comment_count'] = 0
                    result['has_comments'] = False
            
            return Response(results)
        except Exception as e:
            return create_error_response(
                'SEARCH_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





@api_view(['GET'])
def server_info(request):
    """サーバー情報取得"""
    return Response({
        'debug_mode': settings.DEBUG,
        'environment': 'development' if settings.DEBUG else 'production',
        'django_version': '5.2.4',
        'api_version': '1.0.0'
    })