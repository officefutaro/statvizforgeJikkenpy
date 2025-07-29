from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    
    def ready(self):
        """アプリケーション起動時の処理"""
        # 開発サーバーの再読み込みによる重複実行を防ぐ
        import os
        if os.environ.get('RUN_MAIN') == 'true':
            # 1. プロジェクトレジストリの整合性チェック
            from .registry_validator import validate_and_fix_registry
            try:
                validate_and_fix_registry()
            except Exception as e:
                print(f"Registry validation failed: {e}")
            
            # 2. 期限切れアーカイブのクリーンアップ
            from .cleanup import cleanup_expired_archives
            try:
                cleanup_expired_archives()
            except Exception as e:
                print(f"Archive cleanup failed: {e}")