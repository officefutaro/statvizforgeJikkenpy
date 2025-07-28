from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, JupyterLabViewSet, server_info

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')

urlpatterns = [
    # ファイル管理エンドポイント（固定パターン）
    path('files/tree/<str:project_folder>/', FileViewSet.as_view({'get': 'tree'}), name='file-tree'),
    path('files/upload/<str:project_folder>/', FileViewSet.as_view({'post': 'upload'}), name='file-upload'),
    path('files/search/<str:project_folder>/', FileViewSet.as_view({'get': 'search'}), name='file-search'),
    path('files/delete/<str:project_folder>/', FileViewSet.as_view({'delete': 'delete'}), name='file-delete'),
    path('files/move/<str:project_folder>/', FileViewSet.as_view({'post': 'move'}), name='file-move'),
    path('files/mkdir/<str:project_folder>/', FileViewSet.as_view({'post': 'mkdir'}), name='file-mkdir'),
    path('files/comments/<str:project_folder>/', FileViewSet.as_view({
        'get': 'comments',
        'post': 'add_comment'
    }), name='file-comments'),
    path('files/comments/<str:project_folder>/<str:comment_id>/', FileViewSet.as_view({
        'put': 'update_comment',
        'delete': 'delete_comment'
    }), name='file-comment-detail'),
    
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
]