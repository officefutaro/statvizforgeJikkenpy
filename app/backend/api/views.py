from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse
from django.conf import settings
from .models import Project, ProjectFile, DataAnalysis
from .serializers import ProjectSerializer, ProjectFileSerializer, DataAnalysisSerializer
from .utils import load_projects_registry, save_projects_registry
from .localization import (
    get_language_from_request, 
    create_error_response, 
    get_field_validation_message
)
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
    
    @action(detail=False, methods=['post'], url_path='upload')
    def upload(self, request):
        """ファイルアップロード"""
        # TODO: ファイルアップロード処理を実装
        return Response({'message': 'Upload endpoint'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], url_path='download')
    def download(self, request, pk=None):
        """ファイルダウンロード"""
        # TODO: ファイルダウンロード処理を実装
        return Response({'message': 'Download endpoint'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'], url_path='list/(?P<project_id>[^/.]+)')
    def list_by_project(self, request, project_id=None):
        """プロジェクト内ファイル一覧"""
        # TODO: プロジェクト別ファイル一覧取得処理を実装
        return Response({'message': f'Files for project {project_id}'}, status=status.HTTP_200_OK)


class DataViewSet(viewsets.ModelViewSet):
    """データ処理API"""
    queryset = DataAnalysis.objects.all()
    serializer_class = DataAnalysisSerializer
    
    @action(detail=False, methods=['post'], url_path='analyze')
    def analyze(self, request):
        """データ分析実行"""
        # TODO: データ分析処理を実装
        return Response({'message': 'Analysis endpoint'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'], url_path='results')
    def get_results(self, request, pk=None):
        """分析結果取得"""
        # TODO: 分析結果取得処理を実装
        return Response({'message': f'Results for analysis {pk}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def server_info(request):
    """サーバー情報取得"""
    return Response({
        'debug_mode': settings.DEBUG,
        'environment': 'development' if settings.DEBUG else 'production',
        'django_version': '5.2.4',
        'api_version': '1.0.0'
    })