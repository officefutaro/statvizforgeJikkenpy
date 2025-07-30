"""
API認証と認可の基盤
"""
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed


class APIKeyAuthentication(BaseAuthentication):
    """
    APIキー認証（将来の実装用）
    現在は開発モードのため、すべてのリクエストを許可
    """
    
    def authenticate(self, request):
        """
        リクエストの認証
        
        Args:
            request: HTTPリクエスト
            
        Returns:
            tuple: (user, auth) または None
        """
        # 開発モードでは認証をスキップ
        if getattr(request, '_force_auth_user', None):
            return (request._force_auth_user, None)
        
        # 将来的にはヘッダーからAPIキーを取得して検証
        # api_key = request.META.get('HTTP_X_API_KEY')
        # if api_key:
        #     return self.authenticate_credentials(api_key)
        
        return None
    
    def authenticate_credentials(self, key):
        """
        APIキーの検証（将来の実装用）
        """
        # TODO: APIキーの検証ロジックを実装
        raise AuthenticationFailed('Invalid API key')


class IsProjectOwner(BasePermission):
    """
    プロジェクトオーナー権限（将来の実装用）
    """
    
    def has_permission(self, request, view):
        """
        ビューレベルの権限チェック
        """
        # 開発モードでは全て許可
        return True
    
    def has_object_permission(self, request, view, obj):
        """
        オブジェクトレベルの権限チェック
        """
        # 開発モードでは全て許可
        return True
        
        # 将来的には以下のような実装
        # if hasattr(obj, 'owner'):
        #     return obj.owner == request.user
        # return True


class ReadOnlyOrProjectOwner(BasePermission):
    """
    読み取り専用またはプロジェクトオーナー権限
    """
    
    def has_permission(self, request, view):
        # 開発モードでは全て許可
        return True
        
        # 将来的には以下のような実装
        # if request.method in ['GET', 'HEAD', 'OPTIONS']:
        #     return True
        # return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # 読み取り操作は全て許可
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # 開発モードでは書き込みも許可
        return True
        
        # 将来的にはオーナーチェック
        # if hasattr(obj, 'owner'):
        #     return obj.owner == request.user
        # return False