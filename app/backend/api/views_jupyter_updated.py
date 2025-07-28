"""
Updated JupyterLabViewSet using separated JupyterLab Service
既存のviews.pyのJupyterLabViewSetをこの内容で置き換えてください
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from .localization import get_language_from_request, create_error_response
from .jupyter_service import jupyter_service
import os
import logging

logger = logging.getLogger(__name__)


class JupyterLabViewSet(viewsets.ViewSet):
    """JupyterLab管理API - 分離されたJupyterLabサービスを使用"""
    
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
        
        # JupyterLabサービスが利用可能かチェック
        if not jupyter_service.is_service_available():
            return create_error_response(
                'JUPYTER_SERVICE_UNAVAILABLE',
                language,
                details={
                    'message': 'JupyterLab service is not properly set up',
                    'service_info': jupyter_service.get_service_info()
                },
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        # プロジェクトディレクトリのパスを構築
        project_base_path = os.path.join(settings.BASE_DIR, '../../project')
        working_dir = os.path.join(project_base_path, project_folder, 'raw')
        
        if not os.path.exists(working_dir):
            return create_error_response(
                'PROJECT_NOT_FOUND',
                language,
                details={'working_dir': working_dir},
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        # 既に起動している場合は既存のインスタンスを返す
        existing_instance, error = jupyter_service.get_jupyter_status(project_folder)
        if existing_instance:
            logger.info(f"JupyterLab already running for project: {project_folder}")
            return Response({
                'success': True,
                'url': existing_instance['url'],
                'port': existing_instance['port'],
                'token': existing_instance['token'],
                'message': 'JupyterLab is already running',
                'project_folder': project_folder,
                'started_at': existing_instance['started_at']
            })
        
        # JupyterLabを起動
        instance, error = jupyter_service.start_jupyter_lab(project_folder, working_dir)
        
        if instance:
            return Response({
                'success': True,
                'url': instance['url'],
                'port': instance['port'],
                'token': instance['token'],
                'message': 'JupyterLab started successfully',
                'project_folder': project_folder,
                'started_at': instance['started_at'],
                'log_file': instance.get('log_file')
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
        
        # JupyterLabサービスが利用可能かチェック
        if not jupyter_service.is_service_available():
            return create_error_response(
                'JUPYTER_SERVICE_UNAVAILABLE',
                language,
                details={'service_info': jupyter_service.get_service_info()},
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        # インスタンスが実行中かチェック
        existing_instance, error = jupyter_service.get_jupyter_status(project_folder)
        if not existing_instance:
            return create_error_response(
                'JUPYTER_NOT_RUNNING',
                language,
                details={'project_folder': project_folder},
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        # JupyterLabを停止
        success, error = jupyter_service.stop_jupyter_lab(project_folder)
        
        if success:
            return Response({
                'success': True,
                'message': 'JupyterLab stopped successfully',
                'project_folder': project_folder
            })
        else:
            return create_error_response(
                'JUPYTER_STOP_FAILED',
                language,
                details={'error': error},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def status(self, request):
        """JupyterLabの状態を確認"""
        language = get_language_from_request(request)
        
        # JupyterLabサービスが利用可能かチェック
        if not jupyter_service.is_service_available():
            return create_error_response(
                'JUPYTER_SERVICE_UNAVAILABLE',
                language,
                details={'service_info': jupyter_service.get_service_info()},
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        # 特定のプロジェクトの状態を確認
        project_folder = request.query_params.get('project_folder')
        if project_folder:
            instance, error = jupyter_service.get_jupyter_status(project_folder)
            if instance:
                return Response({
                    'project_folder': project_folder,
                    'status': 'running',
                    'url': instance['url'],
                    'port': instance['port'],
                    'token': instance['token'],
                    'started_at': instance['started_at'],
                    'working_dir': instance['working_dir']
                })
            else:
                return Response({
                    'project_folder': project_folder,
                    'status': 'stopped'
                })
        
        # 全インスタンスの状態を取得
        instances, error = jupyter_service.list_jupyter_instances()
        
        if instances is not None:
            running_instances = []
            for project_folder, instance in instances.items():
                running_instances.append({
                    'project_folder': project_folder,
                    'url': instance['url'],
                    'port': instance['port'],
                    'token': instance['token'],
                    'started_at': instance['started_at'],
                    'working_dir': instance['working_dir']
                })
            
            return Response({
                'service_available': True,
                'running_instances': running_instances,
                'total_count': len(running_instances)
            })
        else:
            return create_error_response(
                'JUPYTER_STATUS_FAILED',
                language,
                details={'error': error},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def service_info(self, request):
        """JupyterLabサービスの詳細情報を取得"""
        service_info = jupyter_service.get_service_info()
        
        return Response({
            'jupyter_service': service_info,
            'recommendations': {
                'setup_required': not service_info['service_available'],
                'setup_command': 'bash jupyter_env_setup.sh' if not service_info['service_available'] else None
            }
        })


# 使用方法:
# 1. jupyter_env_setup.sh を実行してJupyterLab環境をセットアップ
# 2. views.py の既存JupyterLabViewSetをこのコードで置き換え
# 3. jupyter_service.py をapi/ディレクトリに配置
# 4. Djangoサーバーを再起動