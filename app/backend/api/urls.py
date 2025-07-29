from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, JupyterLabViewSet, server_info

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', FileViewSet, basename='file')
router.register(r'jupyter', JupyterLabViewSet, basename='jupyter')

urlpatterns = [
    # テスト用シンプルパターン
    path('test/', lambda request: JsonResponse({'status': 'ok'}), name='test'),
    path('test-delete/', lambda request: JsonResponse({'method': request.method, 'status': 'ok'}), name='test-delete'),
    path('test-fileviewset/<str:project_folder>/', FileViewSet.as_view({'delete': 'delete'}), name='test-fileviewset'),
    
    # 固定パターンを先頭に配置（router.urlsの前に処理される）
    
    # 固定パターンは不要 - router.urlsが自動生成
    path('files/comments/<str:project_folder>/', FileViewSet.as_view({
        'get': 'comments',
        'post': 'add_comment'
    }), name='file-comments'),
    path('files/comments/<str:project_folder>/<str:comment_id>/', FileViewSet.as_view({
        'put': 'update_comment',
        'delete': 'delete_comment'
    }), name='file-comment-detail'),
    
    # ファイル説明関連エンドポイント
    path('files/descriptions/<str:project_folder>/', FileViewSet.as_view({
        'get': 'get_file_description',
        'post': 'save_file_description'
    }), name='file-descriptions'),
    
    # ファイルタグ関連エンドポイント
    path('files/tags/<str:project_folder>/', FileViewSet.as_view({
        'get': 'get_file_tags',
        'post': 'save_file_tags'
    }), name='file-tags'),
    path('files/search-by-tags/<str:project_folder>/', FileViewSet.as_view({
        'get': 'search_files_by_tags'
    }), name='file-search-by-tags'),
    path('files/table/<str:project_folder>/', FileViewSet.as_view({
        'get': 'table'
    }), name='file-table'),
    
    # RESTful プロジェクト管理エンドポイント
    path('projects/', ProjectViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='project-list-create'),
    path('projects/deleted/', ProjectViewSet.as_view({'get': 'deleted'}), name='project-deleted'),
    path('projects/<str:pk>/', ProjectViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='project-detail'),
    path('projects/<str:pk>/restore/', ProjectViewSet.as_view({'post': 'restore'}), name='project-restore'),
    
    # JupyterLab管理エンドポイント
    path('jupyter/start/', JupyterLabViewSet.as_view({'post': 'start'}), name='jupyter-start'),
    path('jupyter/stop/', JupyterLabViewSet.as_view({'post': 'stop'}), name='jupyter-stop'),
    path('jupyter/status/', JupyterLabViewSet.as_view({'get': 'status'}), name='jupyter-status'),
    
    path('server-info/', server_info, name='server_info'),
] + router.urls