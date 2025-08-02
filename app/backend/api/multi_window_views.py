"""
マルチウィンドウ対応 Django API Views
SSE (Server-Sent Events) + HTTP API による実装
"""

import json
import time
import threading
from typing import Dict, Any, List
from datetime import datetime, timedelta
from django.http import JsonResponse, StreamingHttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
import logging

logger = logging.getLogger(__name__)

# =============================================================================
# グローバル状態管理（メモリベース）
# =============================================================================

class MultiWindowState:
    """
    マルチウィンドウ状態管理
    本来はRedisなどの外部ストレージを使用すべきだが、
    少人数での使用を想定してメモリベースで実装
    """
    
    def __init__(self):
        self.windows: Dict[str, Dict[str, Any]] = {}
        self.projects: Dict[str, Dict[str, Any]] = {}
        self.sse_clients: Dict[str, Any] = {}  # SSE接続クライアント
        self.lock = threading.Lock()
        
        # クリーンアップ用
        self.cleanup_interval = 300  # 5分
        self.last_cleanup = time.time()
    
    def add_window(self, window_id: str, window_info: Dict[str, Any]):
        """ウィンドウ追加"""
        with self.lock:
            self.windows[window_id] = {
                **window_info,
                'last_activity': time.time(),
                'created_at': time.time()
            }
            logger.info(f"Window added: {window_id} ({window_info.get('type', 'unknown')})")
    
    def remove_window(self, window_id: str):
        """ウィンドウ削除"""
        with self.lock:
            if window_id in self.windows:
                del self.windows[window_id]
                logger.info(f"Window removed: {window_id}")
    
    def update_project(self, project_id: str, updates: Dict[str, Any], window_id: str):
        """プロジェクト状態更新"""
        with self.lock:
            if project_id not in self.projects:
                self.projects[project_id] = {
                    'selectedFiles': [],
                    'tableView': {
                        'filter': {},
                        'sort': None,
                        'pageSize': 20,
                        'currentPage': 1,
                    },
                    'analysisView': {
                        'chartType': 'bar',
                        'selectedColumns': [],
                        'filters': {},
                    },
                    'lastModified': 0,
                    'modifiedBy': '',
                }
            
            # 更新適用
            current_state = self.projects[project_id]
            timestamp = time.time() * 1000  # ミリ秒
            
            # Last Write Wins: より新しいタイムスタンプの更新のみ適用
            if timestamp > current_state.get('lastModified', 0):
                # Deep merge for nested objects
                for key, value in updates.items():
                    if key in current_state and isinstance(current_state[key], dict) and isinstance(value, dict):
                        current_state[key].update(value)
                    else:
                        current_state[key] = value
                
                current_state['lastModified'] = timestamp
                current_state['modifiedBy'] = window_id
                
                logger.info(f"Project updated: {project_id} by {window_id}")
                return True
            else:
                logger.info(f"Project update ignored (older timestamp): {project_id}")
                return False
    
    def get_project_state(self, project_id: str) -> Dict[str, Any]:
        """プロジェクト状態取得"""
        with self.lock:
            return self.projects.get(project_id, {})
    
    def cleanup_inactive_windows(self):
        """非アクティブウィンドウのクリーンアップ"""
        current_time = time.time()
        if current_time - self.last_cleanup < self.cleanup_interval:
            return
        
        with self.lock:
            inactive_windows = []
            cutoff_time = current_time - 600  # 10分間非アクティブ
            
            for window_id, window_info in self.windows.items():
                if window_info.get('last_activity', 0) < cutoff_time:
                    inactive_windows.append(window_id)
            
            for window_id in inactive_windows:
                del self.windows[window_id]
                logger.info(f"Cleaned up inactive window: {window_id}")
            
            self.last_cleanup = current_time
    
    def add_sse_client(self, client_id: str, response_generator):
        """SSEクライアント追加"""
        with self.lock:
            self.sse_clients[client_id] = {
                'generator': response_generator,
                'connected_at': time.time()
            }
    
    def remove_sse_client(self, client_id: str):
        """SSEクライアント削除"""
        with self.lock:
            if client_id in self.sse_clients:
                del self.sse_clients[client_id]
    
    def broadcast_update(self, update: Dict[str, Any], exclude_window: str = None):
        """全SSEクライアントに更新を配信"""
        with self.lock:
            message = f"data: {json.dumps(update)}\n\n"
            disconnected_clients = []
            
            for client_id, client_info in self.sse_clients.items():
                # 送信者は除外
                if exclude_window and client_id == exclude_window:
                    continue
                
                try:
                    generator = client_info['generator']
                    # ここでgeneratorにメッセージを送信する仕組みが必要
                    # 実際の実装ではQueue等を使用
                except Exception as e:
                    logger.error(f"Failed to send to SSE client {client_id}: {e}")
                    disconnected_clients.append(client_id)
            
            # 切断されたクライアントを削除
            for client_id in disconnected_clients:
                del self.sse_clients[client_id]

# グローバルインスタンス
multi_window_state = MultiWindowState()

# =============================================================================
# HTTP API Views
# =============================================================================

@method_decorator(csrf_exempt, name='dispatch')
class MultiWindowSyncView(View):
    """
    マルチウィンドウ同期 HTTP API
    POST /api/sync
    """
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            update_type = data.get('type')
            window_id = data.get('windowId')
            project_id = data.get('projectId')
            timestamp = data.get('timestamp', time.time() * 1000)
            
            if not all([update_type, window_id]):
                return JsonResponse({
                    'error': 'Missing required fields: type, windowId'
                }, status=400)
            
            # クリーンアップ実行
            multi_window_state.cleanup_inactive_windows()
            
            # 更新タイプ別処理
            if update_type == 'WINDOW_OPENED':
                window_info = data.get('windowInfo', {})
                multi_window_state.add_window(window_id, window_info)
                
                # 他のクライアントに通知
                broadcast_data = {
                    'type': 'WINDOW_OPENED',
                    'windowId': window_id,
                    'projectId': project_id,
                    'timestamp': timestamp,
                    'windowInfo': window_info,
                }
                multi_window_state.broadcast_update(broadcast_data, exclude_window=window_id)
                
            elif update_type == 'WINDOW_CLOSED':
                multi_window_state.remove_window(window_id)
                
                # 他のクライアントに通知
                broadcast_data = {
                    'type': 'WINDOW_CLOSED',
                    'windowId': window_id,
                    'projectId': project_id,
                    'timestamp': timestamp,
                }
                multi_window_state.broadcast_update(broadcast_data, exclude_window=window_id)
                
            elif update_type == 'PROJECT_UPDATE':
                updates = data.get('data', {})
                if project_id and updates:
                    success = multi_window_state.update_project(project_id, updates, window_id)
                    
                    if success:
                        # 他のクライアントに通知
                        broadcast_data = {
                            'type': 'PROJECT_UPDATE',
                            'windowId': window_id,
                            'projectId': project_id,
                            'timestamp': timestamp,
                            'data': updates,
                        }
                        multi_window_state.broadcast_update(broadcast_data, exclude_window=window_id)
                
            elif update_type == 'HEARTBEAT':
                # ハートビート受信（アクティビティ更新）
                if window_id in multi_window_state.windows:
                    multi_window_state.windows[window_id]['last_activity'] = time.time()
            
            return JsonResponse({
                'success': True,
                'timestamp': timestamp,
                'windows_count': len(multi_window_state.windows),
                'projects_count': len(multi_window_state.projects),
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error(f"MultiWindowSyncView error: {e}")
            return JsonResponse({'error': str(e)}, status=500)

# =============================================================================
# SSE (Server-Sent Events) View
# =============================================================================

class MultiWindowSSEView(View):
    """
    マルチウィンドウ SSE配信
    GET /api/events/multi-window
    """
    
    def get(self, request):
        def event_stream():
            client_id = f"sse_{int(time.time())}_{id(threading.current_thread())}"
            
            try:
                # SSEヘッダー設定
                yield "data: {\"type\": \"connected\", \"clientId\": \"" + client_id + "\"}\n\n"
                
                # クライアント登録
                multi_window_state.add_sse_client(client_id, None)  # generator は後で実装
                
                # Keep-alive ループ
                last_heartbeat = time.time()
                
                while True:
                    current_time = time.time()
                    
                    # 30秒ごとにハートビート送信
                    if current_time - last_heartbeat > 30:
                        yield f"data: {{\"type\": \"heartbeat\", \"timestamp\": {current_time * 1000}}}\n\n"
                        last_heartbeat = current_time
                    
                    # 実際の実装では、ここでキューから更新メッセージを取得
                    # 今回はシンプルに sleep で代用
                    time.sleep(1)
                    
            except GeneratorExit:
                # クライアント切断時のクリーンアップ
                multi_window_state.remove_sse_client(client_id)
                logger.info(f"SSE client disconnected: {client_id}")
            except Exception as e:
                logger.error(f"SSE stream error: {e}")
                multi_window_state.remove_sse_client(client_id)
        
        response = StreamingHttpResponse(
            event_stream(),
            content_type='text/event-stream'
        )
        
        # SSE必須ヘッダー
        response['Cache-Control'] = 'no-cache'
        response['Connection'] = 'keep-alive'
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Cache-Control'
        
        return response

# =============================================================================
# プロジェクト状態取得 API
# =============================================================================

class ProjectStateView(View):
    """
    プロジェクト状態取得 API
    GET /api/multi-window/projects/{project_id}/state
    """
    
    def get(self, request, project_id):
        try:
            state = multi_window_state.get_project_state(project_id)
            return JsonResponse({
                'projectId': project_id,
                'state': state,
                'timestamp': time.time() * 1000,
            })
        except Exception as e:
            logger.error(f"ProjectStateView error: {e}")
            return JsonResponse({'error': str(e)}, status=500)

# =============================================================================
# ウィンドウ一覧取得 API
# =============================================================================

class WindowListView(View):
    """
    アクティブウィンドウ一覧取得 API
    GET /api/multi-window/windows
    """
    
    def get(self, request):
        try:
            multi_window_state.cleanup_inactive_windows()
            
            windows = []
            with multi_window_state.lock:
                for window_id, window_info in multi_window_state.windows.items():
                    windows.append({
                        'id': window_id,
                        'type': window_info.get('type'),
                        'projectId': window_info.get('projectId'),
                        'title': window_info.get('title'),
                        'lastActivity': window_info.get('last_activity'),
                        'isActive': time.time() - window_info.get('last_activity', 0) < 60,  # 1分以内
                    })
            
            return JsonResponse({
                'windows': windows,
                'count': len(windows),
                'timestamp': time.time() * 1000,
            })
        except Exception as e:
            logger.error(f"WindowListView error: {e}")
            return JsonResponse({'error': str(e)}, status=500)