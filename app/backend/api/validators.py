"""
APIセキュリティバリデーター
"""
import os
from pathlib import Path
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class FilePathValidator:
    """ファイルパスのセキュリティバリデーション"""
    
    @staticmethod
    def validate_file_path(file_path: str, project_folder: str) -> str:
        """
        ファイルパスの妥当性を検証し、安全な相対パスを返す
        
        Args:
            file_path: 検証するファイルパス
            project_folder: プロジェクトフォルダ名
            
        Returns:
            str: 安全な相対パス
            
        Raises:
            ValidationError: 無効なパスの場合
        """
        if not file_path:
            raise ValidationError(_("ファイルパスが指定されていません"))
        
        # パスの正規化前に危険なパターンをチェック
        if '..' in file_path or file_path.startswith('/') or file_path.startswith('\\'):
            raise ValidationError(_("無効なファイルパスです（ディレクトリトラバーサル検出）"))
        
        # パスの正規化
        normalized_path = os.path.normpath(file_path)
        
        # 正規化後も再度チェック
        if '..' in normalized_path or normalized_path.startswith('/'):
            raise ValidationError(_("無効なファイルパスです"))
        
        # 危険な文字のチェック（null文字、改行、チルダ）
        dangerous_chars = ['~', '\0', '\n', '\r', '\x00']
        for char in dangerous_chars:
            if char in file_path:
                raise ValidationError(_("ファイルパスに無効な文字が含まれています"))
        
        return normalized_path
    
    @staticmethod
    def validate_project_folder(folder_name: str) -> str:
        """
        プロジェクトフォルダ名の妥当性を検証
        
        Args:
            folder_name: 検証するフォルダ名
            
        Returns:
            str: 検証済みのフォルダ名
            
        Raises:
            ValidationError: 無効なフォルダ名の場合
        """
        if not folder_name:
            raise ValidationError(_("プロジェクトフォルダ名が指定されていません"))
        
        # 英数字、ハイフン、アンダースコアのみ許可
        import re
        if not re.match(r'^[a-zA-Z0-9_-]+$', folder_name):
            raise ValidationError(_("プロジェクトフォルダ名には英数字、ハイフン、アンダースコアのみ使用できます"))
        
        # 長さ制限
        if len(folder_name) > 100:
            raise ValidationError(_("プロジェクトフォルダ名は100文字以内で指定してください"))
        
        return folder_name


class APIPermissionValidator:
    """API権限バリデーション"""
    
    @staticmethod
    def check_file_access_permission(user, project_folder: str, file_path: str) -> bool:
        """
        ファイルアクセス権限のチェック
        
        Args:
            user: リクエストユーザー
            project_folder: プロジェクトフォルダ名
            file_path: ファイルパス
            
        Returns:
            bool: アクセス可能な場合True
        """
        # 現在は認証なしのため、常にTrue
        # 将来的にはユーザーとプロジェクトの関連をチェック
        return True
    
    @staticmethod
    def check_project_permission(user, project_id: str, action: str) -> bool:
        """
        プロジェクト操作権限のチェック
        
        Args:
            user: リクエストユーザー
            project_id: プロジェクトID
            action: 実行するアクション（'read', 'write', 'delete'）
            
        Returns:
            bool: 権限がある場合True
        """
        # 現在は認証なしのため、常にTrue
        # 将来的にはユーザーロールベースの権限チェック
        return True