from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, JupyterLabViewSet, TableDisplaySettingsViewSet, server_info
from .views_image_upload import upload_project_image, list_project_images, delete_project_image
from .views_git import GitViewSet
from .views_git_sync import GitSyncViewSet

# APIルーターの設定
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', FileViewSet, basename='file')
router.register(r'jupyter', JupyterLabViewSet, basename='jupyter')
router.register(r'table-settings', TableDisplaySettingsViewSet, basename='table-settings')
router.register(r'git', GitViewSet, basename='git')
router.register(r'git-sync', GitSyncViewSet, basename='git-sync')

# URLパターンの定義
urlpatterns = [
    # システム情報 (v1バージョニング対応)
    path('server-info/', server_info, name='server_info'),
    
    # プロジェクト関連エンドポイント
    path('projects/list', ProjectViewSet.as_view({'get': 'list'}), name='project-list'),
    
    # デバッグ用エンドポイント（開発環境のみ）
    path('test/', lambda request: JsonResponse({'status': 'ok', 'version': 'v1'}), name='test'),
    
    # 手動でスラッシュなしのタグエンドポイントを追加
    path('files/tags/<str:project_folder>', FileViewSet.as_view({'get': 'file_tags', 'post': 'file_tags'}), name='file-tags-no-slash'),
    path('files/descriptions/<str:project_folder>', FileViewSet.as_view({'get': 'file_descriptions', 'post': 'file_descriptions'}), name='file-descriptions-no-slash'),
    path('files/search-by-tags/<str:project_folder>/', FileViewSet.as_view({'get': 'search_files_by_tags'}), name='file-search-by-tags'),
    
    # テーブルデータ取得エンドポイントを追加
    path('files/table/<str:project_folder>/', FileViewSet.as_view({'get': 'table'}), name='file-table-with-folder'),
    
    # マルチウィンドウ対応エンドポイント
    path('multi-window/', include('api.multi_window_urls')),
    
    # 画像アップロード機能
    path('projects/images/upload/', upload_project_image, name='upload-project-image'),
    path('projects/<str:project_id>/images/', list_project_images, name='list-project-images'),
    path('projects/<str:project_id>/images/<str:filename>', delete_project_image, name='delete-project-image'),
    
] + router.urls