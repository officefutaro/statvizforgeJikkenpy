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
        """プロジェクト新規作成 - projects-registry.jsonに追加"""
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
            
            # IDを自動生成（最大ID + 1）
            max_id = max([p.get('id', 0) for p in registry_data['projects']], default=0)
            new_project['id'] = max_id + 1
            
            # 日時を追加
            from datetime import datetime
            now = datetime.now().isoformat()
            new_project['created_date'] = now
            new_project['modified_date'] = now
            
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
    
    def retrieve(self, request, pk=None):
        """プロジェクト詳細取得"""
        try:
            registry_data = load_projects_registry()
            project = next((p for p in registry_data['projects'] if p.get('id') == int(pk)), None)
            
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
            project_index = next((i for i, p in enumerate(registry_data['projects']) if p.get('id') == int(pk)), None)
            
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
        """プロジェクト削除"""
        try:
            registry_data = load_projects_registry()
            project_index = next((i for i, p in enumerate(registry_data['projects']) if p.get('id') == int(pk)), None)
            
            if project_index is None:
                return Response(
                    {'error': 'Project not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # 削除
            from datetime import datetime
            deleted_project = registry_data['projects'].pop(project_index)
            registry_data['last_updated'] = datetime.now().isoformat()
            
            save_projects_registry(registry_data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': f'Failed to delete project: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
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