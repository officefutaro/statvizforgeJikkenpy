"""
マルチウィンドウ対応 URL設定
"""

from django.urls import path
from .multi_window_views import (
    MultiWindowSyncView,
    MultiWindowSSEView,
    ProjectStateView,
    WindowListView,
)

urlpatterns = [
    # HTTP API エンドポイント
    path('sync/', MultiWindowSyncView.as_view(), name='multi_window_sync'),
    
    # SSE配信エンドポイント
    path('events/multi-window/', MultiWindowSSEView.as_view(), name='multi_window_sse'),
    
    # 状態取得エンドポイント
    path('projects/<str:project_id>/state/', ProjectStateView.as_view(), name='project_state'),
    path('windows/', WindowListView.as_view(), name='window_list'),
]