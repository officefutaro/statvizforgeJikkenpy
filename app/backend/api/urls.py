from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, DataViewSet, server_info

router = DefaultRouter()
router.register(r'files', FileViewSet, basename='file')
router.register(r'data', DataViewSet, basename='data')

urlpatterns = [
    path('', include(router.urls)),
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
    
    # 後方互換性のための旧エンドポイント（非推奨）
    path('projects/list', ProjectViewSet.as_view({'get': 'list'}), name='project-list-legacy'),
    path('projects/create', ProjectViewSet.as_view({'post': 'create'}), name='project-create-legacy'),
    path('projects/archived', ProjectViewSet.as_view({'get': 'deleted'}), name='project-archived-legacy'),
    
    path('server-info/', server_info, name='server_info'),
]