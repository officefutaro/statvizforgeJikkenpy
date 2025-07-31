from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, FileViewSet, JupyterLabViewSet, TableDisplaySettingsViewSet, server_info

# APIルーターの設定
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', FileViewSet, basename='file')
router.register(r'jupyter', JupyterLabViewSet, basename='jupyter')
router.register(r'table-settings', TableDisplaySettingsViewSet, basename='table-settings')

# URLパターンの定義
urlpatterns = [
    # システム情報
    path('server-info/', server_info, name='server_info'),
    
    # デバッグ用エンドポイント（開発環境のみ）
    path('test/', lambda request: JsonResponse({'status': 'ok', 'version': 'v1'}), name='test'),
    
    # 手動でスラッシュなしのタグエンドポイントを追加
    path('files/tags/<str:project_folder>', FileViewSet.as_view({'get': 'file_tags', 'post': 'file_tags'}), name='file-tags-no-slash'),
    path('files/descriptions/<str:project_folder>', FileViewSet.as_view({'get': 'file_descriptions', 'post': 'file_descriptions'}), name='file-descriptions-no-slash'),
    
    # テーブルデータ取得エンドポイントを追加
    path('files/table/<str:project_folder>/', FileViewSet.as_view({'get': 'table'}), name='file-table-with-folder'),
    
] + router.urls