"""
プロジェクトフォルダのGit同期機能のAPIビュー
analysisdata と raw フォルダを git フォルダに同期してGit管理
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from .git_sync_utils import GitSyncUtils, GitSyncError
from .git_utils import GitUtils, GitError
from .localization import get_language_from_request
from .utils import create_error_response
import logging

logger = logging.getLogger(__name__)

class GitSyncViewSet(viewsets.ViewSet):
    """プロジェクトフォルダのGit同期APIビューセット"""
    
    def _get_git_sync_utils(self, project_folder: str) -> GitSyncUtils:
        """GitSyncUtilsインスタンスを取得"""
        try:
            return GitSyncUtils(project_folder)
        except GitSyncError as e:
            raise GitSyncError(str(e))
    
    def _get_git_utils(self, project_folder: str) -> GitUtils:
        """GitUtilsインスタンスを取得（git フォルダ用）"""
        try:
            # 重要: プロジェクト固有のgitフォルダでGit操作を実行
            # GitUtilsは直接gitフォルダを操作対象とする
            from django.conf import settings
            from pathlib import Path
            
            # プロジェクトパスを確認し、存在しない場合は作成
            project_path = Path(settings.PROJECTS_ROOT) / project_folder
            if not project_path.exists():
                project_path.mkdir(parents=True, exist_ok=True)
                
            # gitフォルダパスを構築し、存在しない場合は作成
            git_folder_path = project_path / 'git'
            if not git_folder_path.exists():
                git_folder_path.mkdir(parents=True, exist_ok=True)
            
            # GitUtilsにgitフォルダの相対パスを渡す（PROJECTS_ROOTからの相対パス）
            git_relative_path = f"{project_folder}/git"
            return GitUtils(git_relative_path)
        except (GitError, OSError) as e:
            raise GitError(str(e))
    
    def _handle_sync_error(self, e: GitSyncError, language: str, operation: str):
        """Git同期エラーのハンドリング"""
        logger.error(f"Git sync {operation} error: {str(e)}")
        
        error_messages = {
            'ja': {
                'project_not_found': 'プロジェクトが見つかりません',
                'sync_failed': f'Git同期{operation}操作に失敗しました',
                'folder_not_found': 'analysisdata または raw フォルダが見つかりません'
            },
            'en': {
                'project_not_found': 'Project not found',
                'sync_failed': f'Git sync {operation} operation failed',
                'folder_not_found': 'analysisdata or raw folder not found'
            },
            'zh-cn': {
                'project_not_found': '未找到项目',
                'sync_failed': f'Git同步{operation}操作失败',
                'folder_not_found': '未找到 analysisdata 或 raw 文件夹'
            },
            'zh-tw': {
                'project_not_found': '未找到專案',
                'sync_failed': f'Git同步{operation}操作失敗',
                'folder_not_found': '未找到 analysisdata 或 raw 資料夾'
            }
        }
        
        messages = error_messages.get(language, error_messages['en'])
        
        # エラーメッセージから適切なメッセージを選択
        error_str = str(e).lower()
        if 'project folder not found' in error_str:
            message = messages['project_not_found']
        elif 'not found' in error_str:
            message = messages['folder_not_found']
        else:
            message = messages['sync_failed']
        
        return create_error_response(
            'GIT_SYNC_OPERATION_FAILED',
            language,
            details={'error': str(e), 'operation': operation},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    @action(detail=False, methods=['get'], url_path='status/(?P<project_folder>[^/.]+)')
    def get_sync_status(self, request, project_folder=None):
        """プロジェクトフォルダの同期状態を取得"""
        language = get_language_from_request(request)
        
        try:
            sync_utils = self._get_git_sync_utils(project_folder)
            status_data = sync_utils.get_sync_status()
            
            return Response({
                'success': True,
                'operation': 'status',
                **status_data
            })
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'status')
    
    @action(detail=False, methods=['post'], url_path='init/(?P<project_folder>[^/.]+)')
    def init_git_folder(self, request, project_folder=None):
        """Git フォルダを初期化（初回セットアップ）"""
        language = get_language_from_request(request)
        
        try:
            sync_utils = self._get_git_sync_utils(project_folder)
            result = sync_utils.initialize_git_folder()
            
            # Git リポジトリも初期化
            try:
                git_utils = self._get_git_utils(project_folder)
                git_init_result = git_utils.init_repository()
                result['git_repository'] = git_init_result
            except GitError as git_error:
                logger.warning(f"Git repository init failed: {git_error}")
                result['git_repository'] = {
                    'success': False,
                    'error': str(git_error)
                }
            
            return Response({
                'operation': 'init',
                **result
            })
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'init')
    
    @action(detail=False, methods=['post'], url_path='sync/(?P<project_folder>[^/.]+)')
    def sync_to_git(self, request, project_folder=None):
        """analysisdata と raw フォルダを git フォルダに同期"""
        language = get_language_from_request(request)
        
        try:
            sync_utils = self._get_git_sync_utils(project_folder)
            result = sync_utils.sync_to_git_folder()
            
            return Response({
                'operation': 'sync',
                **result
            })
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'sync')
    
    @action(detail=False, methods=['get'], url_path='info/(?P<project_folder>[^/.]+)')
    def get_git_info(self, request, project_folder=None):
        """Git フォルダの詳細情報を取得"""
        language = get_language_from_request(request)
        
        try:
            sync_utils = self._get_git_sync_utils(project_folder)
            info_data = sync_utils.get_git_folder_info()
            
            # Git リポジトリの状態も取得
            git_status = {'exists': False}
            try:
                git_utils = self._get_git_utils(project_folder)
                git_status = git_utils.get_status()
                git_status['exists'] = True
            except GitError:
                pass
            
            return Response({
                'success': True,
                'operation': 'info',
                'folder_info': info_data,
                'git_status': git_status
            })
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'info')
    
    @action(detail=False, methods=['post'], url_path='commit/(?P<project_folder>[^/.]+)')
    def commit_with_sync(self, request, project_folder=None):
        """同期 + Git コミットを実行（ユーザー操作）"""
        language = get_language_from_request(request)
        commit_message = request.data.get('message', '')
        author_name = request.data.get('author_name')
        author_email = request.data.get('author_email')
        
        if not commit_message:
            return create_error_response(
                'COMMIT_MESSAGE_REQUIRED',
                language,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # 1. まず同期を実行
            sync_utils = self._get_git_sync_utils(project_folder)
            sync_result = sync_utils.sync_to_git_folder()
            
            if not sync_result['success']:
                return Response({
                    'success': False,
                    'operation': 'commit',
                    'step': 'sync',
                    'error': 'Sync failed',
                    'sync_result': sync_result
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # 2. Git コミットを実行
            try:
                git_utils = self._get_git_utils(project_folder)
                
                # ファイルを追加
                add_result = git_utils.add_files()
                if not add_result['success']:
                    return Response({
                        'success': False,
                        'operation': 'commit',
                        'step': 'add',
                        'sync_result': sync_result,
                        'add_result': add_result
                    }, status=status.HTTP_400_BAD_REQUEST)
                
                # コミット実行
                commit_result = git_utils.commit(commit_message, author_name, author_email)
                
                return Response({
                    'success': commit_result['success'],
                    'operation': 'commit',
                    'project_folder': project_folder,
                    'message': commit_message,
                    'sync_result': sync_result,
                    'add_result': add_result,
                    'commit_result': commit_result
                })
                
            except GitError as git_error:
                return Response({
                    'success': False,
                    'operation': 'commit',
                    'step': 'git',
                    'sync_result': sync_result,
                    'git_error': str(git_error)
                }, status=status.HTTP_400_BAD_REQUEST)
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'commit')
    
    @action(detail=False, methods=['get'], url_path='diff/(?P<project_folder>[^/.]+)')
    def check_differences(self, request, project_folder=None):
        """analysisdata/raw と git フォルダの差分をチェック"""
        language = get_language_from_request(request)
        
        try:
            sync_utils = self._get_git_sync_utils(project_folder)
            
            # 同期状態を取得
            sync_status = sync_utils.get_sync_status()
            
            # Git の差分も取得（可能な場合）
            git_diff = None
            try:
                git_utils = self._get_git_utils(project_folder)
                git_diff = git_utils.get_diff()
            except GitError:
                pass
            
            return Response({
                'success': True,
                'operation': 'diff',
                'project_folder': project_folder,
                'sync_status': sync_status,
                'git_diff': git_diff
            })
            
        except GitSyncError as e:
            return self._handle_sync_error(e, language, 'diff')
    
    @action(detail=False, methods=['get'], url_path='log/(?P<project_folder>[^/.]+)')
    def get_git_log(self, request, project_folder=None):
        """Git コミット履歴を取得"""
        language = get_language_from_request(request)
        limit = int(request.query_params.get('limit', 10))
        limit = min(max(limit, 1), 50)  # 1-50の範囲に制限
        
        try:
            git_utils = self._get_git_utils(project_folder)
            result = git_utils.get_log(limit)
            
            return Response({
                'success': True,
                'operation': 'log',
                'project_folder': project_folder,
                'limit': limit,
                **result
            })
            
        except GitError as e:
            return create_error_response(
                'GIT_LOG_FAILED',
                language,
                details={'error': str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )