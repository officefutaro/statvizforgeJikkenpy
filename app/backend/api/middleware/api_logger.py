import json
import os
from datetime import datetime
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class APILoggerMiddleware(MiddlewareMixin):
    """開発モード時にAPI呼び出しを記録するミドルウェア"""
    
    def process_request(self, request):
        """リクエスト処理前"""
        if settings.DEBUG and request.path.startswith('/api/'):
            # リクエストボディを保存（後で使用）
            try:
                request._body_data = request.body.decode('utf-8') if request.body else ''
            except:
                request._body_data = 'Binary data'
        return None
    
    def process_response(self, request, response):
        """レスポンス処理後"""
        if settings.DEBUG and request.path.startswith('/api/'):
            try:
                # 現在時刻
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # リクエスト情報
                method = request.method
                path = request.path
                
                # リクエストボディ
                request_body = ''
                if method in ['POST', 'PUT', 'PATCH']:
                    request_body = getattr(request, '_body_data', '')
                    if not request_body and hasattr(request, 'data'):
                        request_body = json.dumps(dict(request.data), ensure_ascii=False)
                
                # クエリパラメータ
                query_params = dict(request.GET) if request.GET else {}
                
                # レスポンス内容
                response_content = ''
                if hasattr(response, 'content'):
                    try:
                        response_content = json.loads(response.content.decode('utf-8'))
                        response_content = json.dumps(response_content, ensure_ascii=False, indent=2)
                    except:
                        response_content = response.content.decode('utf-8', errors='ignore')
                
                # ログエントリ作成
                log_entry = f"""
[{timestamp}] {method} {path}
リクエスト: {request_body if request_body else query_params}
レスポンス: {response_content}
ステータス: {response.status_code}
---
"""
                
                # ファイルに追記
                log_path = os.path.join(settings.BASE_DIR, 'apihistory.md')
                with open(log_path, 'a', encoding='utf-8') as f:
                    f.write(log_entry)
                    
            except Exception as e:
                # ログ記録でエラーが発生してもAPIは正常に動作させる
                print(f"API Logger Error: {e}")
                
        return response