"""
Django テスト用プロジェクトデータ保護システム
Django Project Data Protection System for Tests
"""

import os
import shutil
import tempfile
import json
from pathlib import Path
from datetime import datetime
from django.conf import settings


class ProjectBackupManager:
    """プロジェクトデータのバックアップ・リストア管理"""
    
    def __init__(self):
        self.projects_dir = Path(settings.BASE_DIR).parent.parent / 'project'
        self.backup_dir = None
        self.original_projects_existed = False
    
    def create_backup(self):
        """プロジェクトフォルダのバックアップを作成"""
        try:
            # 一時ディレクトリを作成
            self.backup_dir = Path(tempfile.mkdtemp(prefix='django_test_backup_'))
            
            # プロジェクトディレクトリが存在するかチェック
            if self.projects_dir.exists():
                self.original_projects_existed = True
                
                # プロジェクトフォルダ全体をバックアップ
                shutil.copytree(self.projects_dir, self.backup_dir / 'projects')
                print(f"✅ プロジェクトバックアップ作成完了: {self.backup_dir}")
            else:
                self.original_projects_existed = False
                print("📁 プロジェクトフォルダが存在しないため、バックアップをスキップ")
                
        except Exception as error:
            print(f"❌ バックアップ作成エラー: {error}")
            raise error
    
    def restore_backup(self):
        """バックアップからプロジェクトフォルダを復元"""
        try:
            # 現在のプロジェクトフォルダを削除
            if self.projects_dir.exists():
                shutil.rmtree(self.projects_dir)
            
            # バックアップが存在する場合は復元
            if self.original_projects_existed and self.backup_dir and (self.backup_dir / 'projects').exists():
                shutil.copytree(self.backup_dir / 'projects', self.projects_dir)
                print("✅ プロジェクトフォルダ復元完了")
            else:
                print("📁 元々プロジェクトフォルダが存在しなかったため、復元をスキップ")
                
        except Exception as error:
            print(f"❌ バックアップ復元エラー: {error}")
            raise error
    
    def cleanup_backup(self):
        """バックアップファイルをクリーンアップ"""
        try:
            if self.backup_dir and self.backup_dir.exists():
                shutil.rmtree(self.backup_dir)
                print("🧹 バックアップファイル削除完了")
        except Exception as error:
            print(f"⚠️ バックアップクリーンアップエラー: {error}")
    
    def create_test_project(self, project_name, files=None):
        """テスト用の一時プロジェクトを作成"""
        if files is None:
            files = {}
        
        test_project_path = self.projects_dir / project_name
        test_project_path.mkdir(parents=True, exist_ok=True)
        
        # デフォルトファイルを作成
        default_files = {
            'README.md': f'# {project_name}\n\nThis is a test project created for testing purposes.',
            'main.py': '# Test Python file\nprint("Hello, World!")',
            'data.csv': 'column1,column2,column3\nvalue1,value2,value3\ntest1,test2,test3',
            'config.json': json.dumps({
                'project_name': project_name,
                'created_for_testing': True,
                'timestamp': datetime.now().isoformat()
            }, indent=2)
        }
        
        # ファイルを作成
        all_files = {**default_files, **files}
        for filename, content in all_files.items():
            file_path = test_project_path / filename
            file_path.write_text(content, encoding='utf-8')
        
        print(f"📁 テスト用プロジェクト作成: {project_name}")
        return str(test_project_path)


class DjangoTestCaseMixin:
    """Django TestCase用のプロジェクトデータ保護ミックスイン"""
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.backup_manager = ProjectBackupManager()
        cls.backup_manager.create_backup()
    
    @classmethod
    def tearDownClass(cls):
        cls.backup_manager.restore_backup()
        cls.backup_manager.cleanup_backup()
        super().tearDownClass()
    
    def setUp(self):
        super().setUp()
        # 各テスト前にもバックアップを作成（より安全のため）
        self.test_backup_manager = ProjectBackupManager()
        self.test_backup_manager.create_backup()
    
    def tearDown(self):
        # 各テスト後にリストア
        if hasattr(self, 'test_backup_manager'):
            self.test_backup_manager.restore_backup()
            self.test_backup_manager.cleanup_backup()
        super().tearDown()
    
    def create_test_project(self, project_name, files=None):
        """テスト用プロジェクトを作成するヘルパーメソッド"""
        return self.test_backup_manager.create_test_project(project_name, files)


def with_project_protection(test_class):
    """プロジェクトデータ保護デコレーター"""
    class ProtectedTestClass(DjangoTestCaseMixin, test_class):
        pass
    
    return ProtectedTestClass