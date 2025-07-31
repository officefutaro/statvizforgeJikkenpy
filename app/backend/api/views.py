from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.http import FileResponse
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Project, ProjectFile
from .serializers import ProjectSerializer, ProjectFileSerializer
from .utils import load_projects_registry, save_projects_registry
from .registry_validator import validate_and_fix_registry
from .localization import (
    get_language_from_request, 
    create_error_response, 
    get_field_validation_message
)
from .file_explorer import FileExplorer
from .file_comments import FileCommentManager
from .validators import FilePathValidator, APIPermissionValidator
from .authentication import APIKeyAuthentication, IsProjectOwner, ReadOnlyOrProjectOwner
import uuid
import subprocess
import os
import threading
import time
import socket
import json


class ProjectViewSet(viewsets.ModelViewSet):
    """プロジェクト管理API - projects-registry.jsonファイルを直接操作"""
    queryset = Project.objects.none()  # DBは使用しない
    serializer_class = ProjectSerializer
    # 認証と権限（開発中は無効）
    # authentication_classes = [APIKeyAuthentication]
    # permission_classes = [ReadOnlyOrProjectOwner]
    
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
        
        # リクエストデータの取得
        try:
            if hasattr(request, 'data') and request.data:
                new_project = {}
                for key, value in request.data.items():
                    if key == 'tags':
                        # tagsフィールドの特別な処理
                        if isinstance(value, list):
                            new_project[key] = value
                        elif isinstance(value, str):
                            new_project[key] = [value] if value else []
                        else:
                            new_project[key] = []
                    elif isinstance(value, list):
                        new_project[key] = value[0] if value else ''
                    else:
                        new_project[key] = value
            elif hasattr(request, 'POST') and request.POST:
                new_project = {}
                for key, value in request.POST.items():
                    if key == 'tags':
                        new_project[key] = request.POST.getlist(key)
                    else:
                        new_project[key] = value
            else:
                new_project = {}
        except Exception as e:
            return create_error_response(
                'INVALID_REQUEST_DATA',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # フォルダ名のバリデーション
        folder_name = new_project.get('folder_name', '')
        if folder_name:
            try:
                from .validators import FilePathValidator
                FilePathValidator.validate_project_folder(folder_name)
            except ValidationError as e:
                return create_error_response(
                    'INVALID_FOLDER_NAME',
                    language,
                    details={'error': str(e)},
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        
        # バリデーション
        validation_errors = {}
        
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
            
            # デフォルト値の設定
            if 'status' not in new_project:
                new_project['status'] = 'active'
            if 'tags' not in new_project:
                new_project['tags'] = []
            
            # プロジェクトフォルダ構造を作成
            try:
                self._create_project_folder_structure(new_project['folder_name'], new_project)
            except Exception as folder_error:
                return create_error_response(
                    'FAILED_TO_CREATE_FOLDER_STRUCTURE',
                    language,
                    details={'error': str(folder_error)},
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # projects-registry.jsonを更新
            registry_data['projects'].append(new_project)
            registry_data['last_updated'] = now
            save_projects_registry(registry_data)
            
            return Response(new_project, status=status.HTTP_201_CREATED)
        except Exception as e:
            import traceback
            error_details = {
                'error_message': str(e),
                'traceback': traceback.format_exc()
            }
            return create_error_response(
                'FAILED_TO_CREATE_PROJECT',
                language,
                details=error_details,
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
        
        # file_comments.jsonの初期ファイルを作成
        from datetime import datetime
        comments_data = {
            'version': '1.0.0',
            'created': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat(),
            'comments': {}
        }
        
        comments_json_path = project_folder / 'file_comments.json'
        with open(comments_json_path, 'w', encoding='utf-8') as f:
            json.dump(comments_data, f, ensure_ascii=False, indent=2)
    
    def retrieve(self, request, pk=None):
        """プロジェクト詳細取得"""
        try:
            registry_data = load_projects_registry()
            project = next((p for p in registry_data['projects'] if p.get('id') == pk), None)
            
            if not project:
                return create_error_response(
                    'PROJECT_NOT_FOUND',
                    get_language_from_request(request),
                    status_code=status.HTTP_404_NOT_FOUND
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
            
            # 現在のプロジェクト情報を取得
            current_project = registry_data['projects'][project_index]
            old_folder_name = current_project.get('folder_name')
            
            # 更新データを正規化
            from datetime import datetime
            updated_data = {}
            for key, value in request.data.items():
                # tagsは配列のまま保持、他のリストは最初の要素を使用
                if key == 'tags' and isinstance(value, list):
                    updated_data[key] = value
                elif isinstance(value, list) and len(value) > 0:
                    updated_data[key] = value[0]
                else:
                    updated_data[key] = value
            
            # folder_name変更チェック
            new_folder_name = updated_data.get('folder_name', old_folder_name)
            folder_name_changed = old_folder_name != new_folder_name
            
            # フォルダ名変更時の処理
            if folder_name_changed:
                self._handle_folder_rename(old_folder_name, new_folder_name)
            
            # 更新
            updated_project = {**current_project, **updated_data}
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
    
    def _handle_folder_rename(self, old_folder_name, new_folder_name):
        """フォルダ名変更時にコメントファイルとタグファイルを保持する処理"""
        import shutil
        from pathlib import Path
        from config.paths import PROJECT_DATA_DIR
        
        old_project_folder = PROJECT_DATA_DIR / old_folder_name
        new_project_folder = PROJECT_DATA_DIR / new_folder_name
        
        if not old_project_folder.exists():
            return
        
        try:
            # プロジェクトフォルダ全体を新しい名前にリネーム
            shutil.move(str(old_project_folder), str(new_project_folder))
            
            # リネーム成功時、新しいフォルダ内のproject.jsonのfolder_nameを更新
            project_json_path = new_project_folder / 'project.json'
            if project_json_path.exists():
                import json
                with open(project_json_path, 'r', encoding='utf-8') as f:
                    project_data = json.load(f)
                
                project_data['folder_name'] = new_folder_name
                
                with open(project_json_path, 'w', encoding='utf-8') as f:
                    json.dump(project_data, f, ensure_ascii=False, indent=2)
            
        except Exception as e:
            print(f"Failed to rename project folder: {e}")
            # リネームに失敗した場合は元の状態を維持
            raise
    
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

    @action(detail=False, methods=['post'])
    def validate_registry(self, request):
        """プロジェクトレジストリとフォルダ構造の整合性を確認・修正"""
        language = get_language_from_request(request)
        
        try:
            modified, log_messages = validate_and_fix_registry()
            
            return Response({
                'success': True,
                'modified': modified,
                'message': (
                    'Registry validation completed' if language == 'en' else 
                    '整合性確認が完了しました'
                ),
                'log_messages': log_messages,
                'summary': {
                    'issues_found': len(log_messages),
                    'fixes_applied': modified
                }
            })
            
        except Exception as e:
            return create_error_response(
                'REGISTRY_VALIDATION_FAILED',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FileViewSet(viewsets.ModelViewSet):
    """ファイル操作API"""
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_explorer = FileExplorer()
        self.comment_manager = FileCommentManager()
    
    @action(detail=False, methods=['get'], url_path='tree/(?P<project_folder>[^/.]+)')
    def tree(self, request, project_folder=None):
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
    
    
    def comments(self, request, project_folder=None):
        """ファイルコメント取得"""
        language = get_language_from_request(request)
        
        try:
            file_path = request.query_params.get('file_path')
            if file_path:
                # 特定ファイルのコメント取得
                comments = self.comment_manager.get_file_comments(project_folder, file_path)
                return Response({'comments': comments})
            else:
                # 全コメント情報取得
                all_comments = self.comment_manager.get_all_comments(project_folder)
                return Response(all_comments)
        except FileNotFoundError:
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return create_error_response(
                'FAILED_TO_GET_COMMENTS',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def add_comment(self, request, project_folder=None):
        """コメント追加"""
        language = get_language_from_request(request)
        
        file_path = request.data.get('file_path')
        comment_text = request.data.get('comment')
        author = request.data.get('author', 'Anonymous')
        
        if not file_path or not comment_text:
            return create_error_response(
                'FILE_PATH_AND_COMMENT_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.comment_manager.add_comment(project_folder, file_path, comment_text, author)
            if result.get('success'):
                return Response(result, status=status.HTTP_201_CREATED)
            else:
                return create_error_response(
                    'ADD_COMMENT_FAILED',
                    language,
                    details=result,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return create_error_response(
                'ADD_COMMENT_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def update_comment(self, request, project_folder=None, comment_id=None):
        """コメント更新"""
        language = get_language_from_request(request)
        
        file_path = request.data.get('file_path')
        comment_text = request.data.get('comment')
        
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        if not comment_text:
            return create_error_response(
                'COMMENT_TEXT_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.comment_manager.update_comment(project_folder, file_path, comment_id, comment_text)
            if result.get('success'):
                return Response(result)
            else:
                return create_error_response(
                    'UPDATE_COMMENT_FAILED',
                    language,
                    details=result,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return create_error_response(
                'UPDATE_COMMENT_ERROR',
                language,
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def delete_comment(self, request, project_folder=None, comment_id=None):
        """コメント削除"""
        language = get_language_from_request(request)
        
        file_path = request.query_params.get('file_path')
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            result = self.comment_manager.delete_comment(project_folder, file_path, comment_id)
            if result.get('success'):
                return Response(result)
            else:
                return create_error_response(
                    'DELETE_COMMENT_FAILED',
                    language,
                    details=result,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return create_error_response(
                'DELETE_COMMENT_ERROR',
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

    def save_file_description(self, request, project_folder=None):
        """ファイル説明を保存する"""
        language = get_language_from_request(request)
        
        # プロジェクトフォルダのバリデーション
        try:
            project_folder = FilePathValidator.validate_project_folder(project_folder)
        except ValidationError as e:
            return create_error_response(
                'INVALID_PROJECT_FOLDER',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # プロジェクトフォルダの存在確認
        from config.paths import PROJECT_DATA_DIR
        project_path = PROJECT_DATA_DIR / project_folder
        if not project_path.exists():
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        file_path = request.data.get('file_path')
        description = request.data.get('description', '')
        
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # ファイルパスのバリデーション
        try:
            file_path = FilePathValidator.validate_file_path(file_path, project_folder)
        except ValidationError as e:
            return create_error_response(
                'INVALID_FILE_PATH',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # analysisdataフォルダに保存
            analysisdata_path = project_path / 'analysisdata'
            analysisdata_path.mkdir(exist_ok=True)
            
            # ファイル説明専用ファイル
            descriptions_file = analysisdata_path / 'file_descriptions.json'
            
            # 既存の説明データを読み込み
            if descriptions_file.exists():
                try:
                    with open(descriptions_file, 'r', encoding='utf-8') as f:
                        descriptions_data = json.load(f)
                except:
                    descriptions_data = {}
            else:
                descriptions_data = {}
            
            # ファイルパスの正規化（rawフォルダ相対パス）
            normalized_path = file_path.replace('\\', '/')
            
            # 説明を保存
            from datetime import datetime
            descriptions_data[normalized_path] = {
                'description': description,
                'updated': datetime.now().isoformat(),
                'author': 'システム'
            }
            
            # ファイルに書き込み
            with open(descriptions_file, 'w', encoding='utf-8') as f:
                json.dump(descriptions_data, f, indent=2, ensure_ascii=False)
            
            return Response({
                'success': True, 
                'description': description,
                'saved_to': str(descriptions_file)
            })
        
        except Exception as e:
            return create_error_response(
                'FAILED_TO_SAVE_DESCRIPTION',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get_file_description(self, request, project_folder=None):
        """ファイル説明を取得する"""
        file_path = request.query_params.get('file_path')
        if not file_path:
            return Response({'description': ''})
        
        try:
            # プロジェクトフォルダの存在確認
            from config.paths import PROJECT_DATA_DIR
            project_path = PROJECT_DATA_DIR / project_folder
            if not project_path.exists():
                return Response({'description': ''})
            
            # 説明ファイルの読み込み
            descriptions_file = project_path / 'analysisdata' / 'file_descriptions.json'
            if not descriptions_file.exists():
                return Response({'description': ''})
            
            with open(descriptions_file, 'r', encoding='utf-8') as f:
                descriptions_data = json.load(f)
            
            # ファイルパスの正規化
            normalized_path = file_path.replace('\\', '/')
            file_description = descriptions_data.get(normalized_path, {}).get('description', '')
            
            return Response({'description': file_description})
        
        except Exception as e:
            return Response({'description': ''})
    
    def save_file_tags(self, request, project_folder=None):
        """ファイルタグを保存する"""
        language = get_language_from_request(request)
        
        # プロジェクトフォルダの存在確認
        from config.paths import PROJECT_DATA_DIR
        project_path = PROJECT_DATA_DIR / project_folder
        if not project_path.exists():
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        file_path = request.data.get('file_path')
        tags = request.data.get('tags', [])
        
        if not file_path:
            return create_error_response(
                'FILE_PATH_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # ファイルタグ管理システムを使ってタグを保存
            # プロジェクトのfile_tags.jsonに保存
            tags_file = project_path / 'file_tags.json'
            
            # 既存のタグデータを読み込み
            if tags_file.exists():
                try:
                    with open(tags_file, 'r', encoding='utf-8') as f:
                        tags_data = json.load(f)
                except:
                    tags_data = {}
            else:
                tags_data = {}
            
            # ファイルパスの正規化（rawフォルダ相対パス）
            normalized_path = file_path.replace('\\', '/')
            
            # タグを保存
            tags_data[normalized_path] = tags
            
            # ファイルに書き込み
            with open(tags_file, 'w', encoding='utf-8') as f:
                json.dump(tags_data, f, indent=2, ensure_ascii=False)
            
            return Response({
                'success': True,
                'file_path': normalized_path,
                'tags': tags,
                'updated': timezone.now().isoformat()
            })
        
        except Exception as e:
            return create_error_response(
                'FAILED_TO_SAVE_TAGS',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def get_file_tags(self, request, project_folder=None):
        """ファイルのタグを取得する（クエリパラメータ対応）"""
        file_path = request.query_params.get('file_path')
        
        try:
            # プロジェクトフォルダの存在確認
            from config.paths import PROJECT_DATA_DIR
            project_path = PROJECT_DATA_DIR / project_folder
            if not project_path.exists():
                if file_path:
                    return Response({'tags': []})
                else:
                    return Response({'files': {}})
            
            # タグファイルの読み込み
            tags_file = project_path / 'file_tags.json'
            if not tags_file.exists():
                if file_path:
                    return Response({'tags': []})
                else:
                    return Response({'files': {}})
            
            with open(tags_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            if file_path:
                # 個別ファイルのタグ取得
                normalized_path = file_path.replace('\\', '/')
                file_tags = tags_data.get(normalized_path, [])
                return Response({'tags': file_tags})
            else:
                # 全ファイルのタグ取得
                return Response({'files': tags_data})
        
        except Exception as e:
            if file_path:
                return Response({'tags': []})
            else:
                return Response({'files': {}})
    
    def search_files_by_tags(self, request, project_folder=None):
        """タグによるファイル検索"""
        language = get_language_from_request(request)
        tags = request.query_params.getlist('tags')
        
        if not tags:
            return create_error_response(
                'TAGS_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # プロジェクトフォルダの存在確認
            from config.paths import PROJECT_DATA_DIR
            project_path = PROJECT_DATA_DIR / project_folder
            if not project_path.exists():
                return create_error_response(
                    'PROJECT_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            # タグファイルの読み込み
            tags_file = project_path / 'file_tags.json'
            if not tags_file.exists():
                return Response({
                    'success': True,
                    'query_tags': tags,
                    'results': [],
                    'total': 0
                })
            
            with open(tags_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            # タグにマッチするファイルを検索
            results = []
            for file_path, file_tags in tags_data.items():
                # 指定されたタグがファイルのタグに含まれているかチェック
                if any(tag in file_tags for tag in tags):
                    # ファイル情報を取得
                    full_file_path = project_path / 'raw' / file_path
                    if full_file_path.exists():
                        results.append({
                            'file_path': file_path,
                            'tags': file_tags,
                            'matched_tags': [tag for tag in tags if tag in file_tags],
                            'size': full_file_path.stat().st_size if full_file_path.is_file() else 0,
                            'type': 'file' if full_file_path.is_file() else 'directory',
                            'modified': full_file_path.stat().st_mtime
                        })
            
            return Response({
                'success': True,
                'query_tags': tags,
                'results': results,
                'total': len(results)
            })
        
        except Exception as e:
            return create_error_response(
                'SEARCH_FAILED',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=['get'])
    def table(self, request, project_folder=None):
        """CSVファイルをテーブル形式で取得"""
        language = get_language_from_request(request)
        
        try:
            file_path = request.query_params.get('file_path')
            if not file_path:
                return create_error_response(
                    'FILE_PATH_REQUIRED',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            # ファイルパスがraw/で始まらない場合は追加
            if not file_path.startswith('raw/'):
                file_path = f'raw/{file_path}'
            
            from config.paths import PROJECT_DATA_DIR
            project_path = PROJECT_DATA_DIR / project_folder
            full_file_path = project_path / file_path
            
            if not full_file_path.exists():
                return create_error_response(
                    'FILE_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
            
            if not full_file_path.is_file():
                return create_error_response(
                    'NOT_A_FILE',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            # CSVファイルのみサポート
            if not file_path.lower().endswith('.csv'):
                return create_error_response(
                    'UNSUPPORTED_FILE_TYPE',
                    language,
                    details={'supported_types': ['.csv']},
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            import csv
            import io
            
            headers = []
            rows = []
            
            try:
                with open(full_file_path, 'r', encoding='utf-8', newline='') as csvfile:
                    # CSVの方言を自動検出
                    sample = csvfile.read(1024)
                    csvfile.seek(0)
                    sniffer = csv.Sniffer()
                    delimiter = sniffer.sniff(sample).delimiter
                    
                    csvfile.seek(0)
                    reader = csv.reader(csvfile, delimiter=delimiter)
                    
                    # ヘッダーを取得
                    headers = next(reader, [])
                    
                    # データ行を取得（最大1000行まで）
                    for i, row in enumerate(reader):
                        if i >= 1000:  # パフォーマンスのため制限
                            break
                        # 列数をヘッダーに合わせる
                        while len(row) < len(headers):
                            row.append('')
                        rows.append(row[:len(headers)])
                        
            except UnicodeDecodeError:
                # UTF-8で読めない場合はShift_JISを試す
                try:
                    with open(full_file_path, 'r', encoding='shift_jis', newline='') as csvfile:
                        sample = csvfile.read(1024)
                        csvfile.seek(0)
                        sniffer = csv.Sniffer()
                        delimiter = sniffer.sniff(sample).delimiter
                        
                        csvfile.seek(0)
                        reader = csv.reader(csvfile, delimiter=delimiter)
                        headers = next(reader, [])
                        
                        for i, row in enumerate(reader):
                            if i >= 1000:
                                break
                            while len(row) < len(headers):
                                row.append('')
                            rows.append(row[:len(headers)])
                except Exception:
                    return create_error_response(
                        'FILE_ENCODING_ERROR',
                        language,
                        status_code=status.HTTP_400_BAD_REQUEST
                    )
            
            return Response({
                'success': True,
                'file_path': file_path,
                'headers': headers,
                'rows': rows,
                'total_rows': len(rows),
                'is_truncated': len(rows) >= 1000
            })
            
        except Exception as e:
            return create_error_response(
                'TABLE_LOAD_FAILED',
                language,
                details={'error': str(e)},
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
    def delete(self, request, project_folder=None):
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
    def move(self, request, project_folder=None):
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
    def mkdir(self, request, project_folder=None):
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
    def search(self, request, project_folder=None):
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

    @action(detail=False, methods=['get', 'post'], url_path='column-types/(?P<project_folder>[^/.]+)')
    def column_types(self, request, project_folder=None):
        """列データ型設定の取得・保存"""
        language = get_language_from_request(request)
        
        # プロジェクトフォルダの存在確認
        from config.paths import PROJECT_DATA_DIR
        project_path = PROJECT_DATA_DIR / project_folder
        if not project_path.exists():
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        # analysisdataフォルダの確保
        analysisdata_path = project_path / 'analysisdata'
        analysisdata_path.mkdir(exist_ok=True)
        
        # 列データ型設定ファイル
        column_types_file = analysisdata_path / 'column_types.json'
        
        if request.method == 'GET':
            # 列データ型設定を取得
            file_path = request.query_params.get('file_path')
            if not file_path:
                return create_error_response(
                    'FILE_PATH_REQUIRED',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            try:
                if column_types_file.exists():
                    with open(column_types_file, 'r', encoding='utf-8') as f:
                        all_column_types = json.load(f)
                else:
                    all_column_types = {}
                
                # ファイルパスの正規化
                normalized_path = file_path.replace('\\', '/')
                column_types = all_column_types.get(normalized_path, {})
                
                return Response({'column_types': column_types})
            except Exception as e:
                return Response({'column_types': {}})
        
        elif request.method == 'POST':
            # 列データ型設定を保存
            file_path = request.data.get('file_path')
            column_types = request.data.get('column_types', {})
            
            if not file_path:
                return create_error_response(
                    'FILE_PATH_REQUIRED',
                    language,
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            
            try:
                # 既存の設定を読み込み
                if column_types_file.exists():
                    try:
                        with open(column_types_file, 'r', encoding='utf-8') as f:
                            all_column_types = json.load(f)
                    except:
                        all_column_types = {}
                else:
                    all_column_types = {}
                
                # ファイルパスの正規化
                normalized_path = file_path.replace('\\', '/')
                
                # 列データ型設定を更新
                all_column_types[normalized_path] = column_types
                
                # ファイルに保存
                with open(column_types_file, 'w', encoding='utf-8') as f:
                    json.dump(all_column_types, f, indent=2, ensure_ascii=False)
                
                return Response({
                    'success': True,
                    'column_types': column_types,
                    'saved_to': str(column_types_file)
                })
            
            except Exception as e:
                return create_error_response(
                    'FAILED_TO_SAVE_COLUMN_TYPES',
                    language,
                    details={'error': str(e)},
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )





# JupyterLab インスタンス管理
jupyter_instances = {}

def get_wsl_ip():
    """WSLのIPアドレスを取得する"""
    try:
        # WSL内での開発を前提とし、localhostを優先
        # WSL2の場合、WSL内でのアクセスはlocalhostで十分
        if os.path.exists('/proc/version'):
            with open('/proc/version', 'r') as f:
                if 'microsoft' in f.read().lower():  # WSL環境の場合
                    return "localhost"
        
        # その他の場合はIPアドレスを取得
        result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
        if result.returncode == 0:
            ip = result.stdout.strip().split()[0]
            return ip
    except:
        pass
    return "localhost"

def find_free_port(start_port=8888):
    """利用可能なポートを探す"""
    for port in range(start_port, start_port + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
    return None

def start_jupyter_lab(project_folder, working_dir):
    """JupyterLabを起動する"""
    port = find_free_port()
    if not port:
        return None, "No available port found"
    
    try:
        # バックエンドの仮想環境を使用
        venv_path = "/home/futaro/project/StatVizForge_JikkenPy/backend_env"
        jupyter_cmd = f"{venv_path}/bin/jupyter-lab"
        
        cmd = [
            jupyter_cmd,
            "--no-browser",
            "--port", str(port),
            "--ip", "127.0.0.1",  # WSL内アクセスを想定してlocalhostに限定
            "--ServerApp.token=''",  # 新しい設定名
            "--ServerApp.password=''",
            "--ServerApp.allow_origin='*'",  # CORS対応
            "--allow-root",
            f"--notebook-dir={working_dir}"
        ]
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=working_dir
        )
        
        # JupyterLabの起動を待つ
        time.sleep(3)
        
        # プロセスが正常に動作しているかチェック
        if process.poll() is None:
            wsl_ip = get_wsl_ip()
            instance_info = {
                'process': process,
                'port': port,
                'url': f"http://{wsl_ip}:{port}",
                'project_folder': project_folder,
                'working_dir': working_dir,
                'started_at': time.time()
            }
            jupyter_instances[project_folder] = instance_info
            return instance_info, None
        else:
            stdout, stderr = process.communicate()
            return None, f"Failed to start JupyterLab: {stderr.decode()}"
            
    except Exception as e:
        return None, str(e)

class JupyterLabViewSet(viewsets.ViewSet):
    """JupyterLab管理API"""
    
    @action(detail=False, methods=['post'])
    def start(self, request):
        """JupyterLabを起動"""
        language = get_language_from_request(request)
        project_folder = request.data.get('project_folder')
        
        if not project_folder:
            return create_error_response(
                'MISSING_PROJECT_FOLDER',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        # プロジェクトディレクトリのパスを構築
        project_base_path = os.path.join(settings.BASE_DIR, '../../project')
        working_dir = os.path.join(project_base_path, project_folder, 'raw')
        
        if not os.path.exists(working_dir):
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        # 既に起動している場合は既存のインスタンスを返す
        if project_folder in jupyter_instances:
            instance = jupyter_instances[project_folder]
            if instance['process'].poll() is None:  # プロセスがまだ生きている
                return Response({
                    'success': True,
                    'url': instance['url'],
                    'port': instance['port'],
                    'message': 'JupyterLab is already running',
                    'project_folder': project_folder
                })
            else:
                # プロセスが死んでいる場合は削除
                del jupyter_instances[project_folder]
        
        # JupyterLabを起動
        instance, error = start_jupyter_lab(project_folder, working_dir)
        
        if instance:
            return Response({
                'success': True,
                'url': instance['url'],
                'port': instance['port'],
                'message': 'JupyterLab started successfully',
                'project_folder': project_folder
            })
        else:
            return create_error_response(
                'JUPYTER_START_FAILED',
                language,
                details={'error': error},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['post'])
    def stop(self, request):
        """JupyterLabを停止"""
        language = get_language_from_request(request)
        project_folder = request.data.get('project_folder')
        
        if not project_folder:
            return create_error_response(
                'MISSING_PROJECT_FOLDER',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        if project_folder not in jupyter_instances:
            return create_error_response(
                'JUPYTER_NOT_RUNNING',
                language,
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        try:
            instance = jupyter_instances[project_folder]
            instance['process'].terminate()
            instance['process'].wait(timeout=5)
            del jupyter_instances[project_folder]
            
            return Response({
                'success': True,
                'message': 'JupyterLab stopped successfully',
                'project_folder': project_folder
            })
        except Exception as e:
            return create_error_response(
                'JUPYTER_STOP_FAILED',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def status(self, request):
        """JupyterLabの状態を確認"""
        running_instances = []
        
        for project_folder, instance in list(jupyter_instances.items()):
            if instance['process'].poll() is None:  # プロセスが生きている
                running_instances.append({
                    'project_folder': project_folder,
                    'url': instance['url'],
                    'port': instance['port'],
                    'started_at': instance['started_at']
                })
            else:
                # 死んでいるプロセスを削除
                del jupyter_instances[project_folder]
        
        return Response({
            'running_instances': running_instances,
            'total_count': len(running_instances)
        })

@api_view(['GET'])
def server_info(request):
    """サーバー情報取得"""
    return Response({
        'debug_mode': settings.DEBUG,
        'environment': 'development' if settings.DEBUG else 'production',
        'django_version': '5.2.4',
        'api_version': '1.0.0'
    })


@api_view(['GET'])
def get_jupyter_status(request):
    """全JupyterLabインスタンスの状態を取得"""
    running_instances = []
    
    for project_folder, instance in list(jupyter_instances.items()):
        if instance['process'].poll() is None:
            running_instances.append({
                'project_folder': project_folder,
                'url': instance['url'],
                'port': instance['port'],
                'started_at': instance['started_at']
            })
        else:
            del jupyter_instances[project_folder]
    
    return Response({
        'running_instances': running_instances,
        'total_count': len(running_instances)
    })


@api_view(['POST'])
def start_jupyter_lab(request):
    """指定されたプロジェクトのJupyterLabを起動"""
    language = get_language_from_request(request)
    project_folder = request.data.get('project_folder')
    
    if not project_folder:
        return create_error_response(
            'MISSING_PROJECT_FOLDER',
            language,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    project_base_path = os.path.join(settings.BASE_DIR, '../../project')
    working_dir = os.path.join(project_base_path, project_folder, 'raw')
    
    if not os.path.exists(working_dir):
        return create_error_response(
            'PROJECT_NOT_FOUND',
            language,
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    if project_folder in jupyter_instances:
        instance = jupyter_instances[project_folder]
        if instance['process'].poll() is None:
            return Response({
                'success': True,
                'url': instance['url'],
                'port': instance['port'],
                'message': 'JupyterLab is already running',
                'project_folder': project_folder
            })
        else:
            del jupyter_instances[project_folder]
    
    instance, error = start_jupyter_lab(project_folder, working_dir)
    
    if instance:
        return Response({
            'success': True,
            'url': instance['url'],
            'port': instance['port'],
            'message': 'JupyterLab started successfully',
            'project_folder': project_folder
        })
    else:
        return create_error_response(
            'JUPYTER_START_FAILED',
            language,
            details={'error': error},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['POST'])
def stop_jupyter_lab(request):
    """指定されたプロジェクトのJupyterLabを停止"""
    language = get_language_from_request(request)
    project_folder = request.data.get('project_folder')
    
    if not project_folder:
        return create_error_response(
            'MISSING_PROJECT_FOLDER',
            language,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    if project_folder not in jupyter_instances:
        return create_error_response(
            'JUPYTER_NOT_RUNNING',
            language,
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    try:
        instance = jupyter_instances[project_folder]
        instance['process'].terminate()
        instance['process'].wait(timeout=5)
        del jupyter_instances[project_folder]
        
        return Response({
            'success': True,
            'message': 'JupyterLab stopped successfully',
            'project_folder': project_folder
        })
    except Exception as e:
        return create_error_response(
            'JUPYTER_STOP_FAILED',
            language,
            details={'error': str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# jupyter_service は JupyterLabViewSet のインスタンスとして使用
jupyter_service = JupyterLabViewSet()


class TableDisplaySettingsViewSet(viewsets.ViewSet):
    """表表示設定管理API"""
    
    @action(detail=False, methods=['get', 'post'], url_path='settings/(?P<project_folder>[^/.]+)/(?P<file_name>[^/.]+)')
    def table_settings(self, request, project_folder=None, file_name=None):
        """表表示設定の取得・保存"""
        language = get_language_from_request(request)
        
        if request.method == 'GET':
            # 設定を取得
            try:
                from .models import TableDisplaySettings
                settings_obj = TableDisplaySettings.objects.filter(
                    project_folder=project_folder,
                    file_name=file_name
                ).first()
                
                if settings_obj:
                    return Response({
                        'success': True,
                        'settings': {
                            'id': str(settings_obj.id),
                            'project_folder': settings_obj.project_folder,
                            'file_name': settings_obj.file_name,
                            'table_config': settings_obj.table_config,
                            'chart_config': settings_obj.chart_config,
                            'layout_config': settings_obj.layout_config,
                            'column_metadata': settings_obj.column_metadata,
                            'created_at': settings_obj.created_at.isoformat(),
                            'updated_at': settings_obj.updated_at.isoformat()
                        }
                    })
                else:
                    return Response({
                        'success': True,
                        'settings': None
                    })
            except Exception as e:
                return create_error_response(
                    'FAILED_TO_GET_SETTINGS',
                    language,
                    details={'error': str(e)},
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        
        elif request.method == 'POST':
            # 設定を保存
            try:
                from .models import TableDisplaySettings
                
                table_config = request.data.get('table_config', {})
                chart_config = request.data.get('chart_config', {})
                layout_config = request.data.get('layout_config', {})
                column_metadata = request.data.get('column_metadata', {})
                
                # 既存の設定を取得または新規作成
                settings_obj, created = TableDisplaySettings.objects.get_or_create(
                    project_folder=project_folder,
                    file_name=file_name,
                    defaults={
                        'table_config': table_config,
                        'chart_config': chart_config,
                        'layout_config': layout_config,
                        'column_metadata': column_metadata
                    }
                )
                
                if not created:
                    # 既存の設定を更新
                    settings_obj.table_config = table_config
                    settings_obj.chart_config = chart_config
                    settings_obj.layout_config = layout_config
                    settings_obj.column_metadata = column_metadata
                    settings_obj.save()
                
                return Response({
                    'success': True,
                    'settings': {
                        'id': str(settings_obj.id),
                        'project_folder': settings_obj.project_folder,
                        'file_name': settings_obj.file_name,
                        'table_config': settings_obj.table_config,
                        'chart_config': settings_obj.chart_config,
                        'layout_config': settings_obj.layout_config,
                        'column_metadata': settings_obj.column_metadata,
                        'created_at': settings_obj.created_at.isoformat(),
                        'updated_at': settings_obj.updated_at.isoformat()
                    },
                    'created': created
                })
            except Exception as e:
                return create_error_response(
                    'FAILED_TO_SAVE_SETTINGS',
                    language,
                    details={'error': str(e)},
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    
    @action(detail=False, methods=['delete'], url_path='settings/(?P<project_folder>[^/.]+)/(?P<file_name>[^/.]+)')
    def delete_settings(self, request, project_folder=None, file_name=None):
        """表表示設定の削除"""
        language = get_language_from_request(request)
        
        try:
            from .models import TableDisplaySettings
            settings_obj = TableDisplaySettings.objects.filter(
                project_folder=project_folder,
                file_name=file_name
            ).first()
            
            if settings_obj:
                settings_obj.delete()
                return Response({'success': True, 'message': 'Settings deleted successfully'})
            else:
                return create_error_response(
                    'SETTINGS_NOT_FOUND',
                    language,
                    status_code=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return create_error_response(
                'FAILED_TO_DELETE_SETTINGS',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'], url_path='settings/(?P<project_folder>[^/.]+)')
    def list_settings(self, request, project_folder=None):
        """プロジェクト内の全ファイルの表表示設定一覧を取得"""
        language = get_language_from_request(request)
        
        try:
            from .models import TableDisplaySettings
            settings_list = TableDisplaySettings.objects.filter(
                project_folder=project_folder
            ).order_by('-updated_at')
            
            settings_data = []
            for settings_obj in settings_list:
                settings_data.append({
                    'id': str(settings_obj.id),
                    'project_folder': settings_obj.project_folder,
                    'file_name': settings_obj.file_name,
                    'created_at': settings_obj.created_at.isoformat(),
                    'updated_at': settings_obj.updated_at.isoformat()
                })
            
            return Response({
                'success': True,
                'settings': settings_data,
                'total': len(settings_data)
            })
        except Exception as e:
            return create_error_response(
                'FAILED_TO_LIST_SETTINGS',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )