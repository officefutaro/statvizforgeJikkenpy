#!/usr/bin/env python
"""
プロジェクト作成機能の詳細デバッグ
"""

import os
import django
import tempfile
import traceback
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rest_framework.test import APIClient
from django.conf import settings
from pathlib import Path

def debug_project_creation():
    """プロジェクト作成の詳細デバッグ"""
    client = APIClient()
    
    print("=" * 60)
    print("プロジェクト作成機能 詳細デバッグ")
    print("=" * 60)
    
    # 1. 現在の設定確認
    print("\n1. 現在の設定確認")
    print(f"BASE_DIR: {settings.BASE_DIR}")
    
    try:
        from config.paths import PROJECT_DATA_DIR
        print(f"PROJECT_DATA_DIR: {PROJECT_DATA_DIR}")
        print(f"PROJECT_DATA_DIR exists: {PROJECT_DATA_DIR.exists()}")
        print(f"PROJECT_DATA_DIR writable: {os.access(PROJECT_DATA_DIR, os.W_OK) if PROJECT_DATA_DIR.exists() else 'N/A'}")
    except Exception as e:
        print(f"PROJECT_DATA_DIR error: {e}")
    
    # 2. 既存プロジェクト確認
    print("\n2. 既存プロジェクト確認")
    try:
        from api.utils import load_projects_registry
        registry = load_projects_registry()
        print(f"Registry version: {registry.get('version')}")
        print(f"Existing projects: {len(registry.get('projects', []))}")
        for project in registry.get('projects', []):
            print(f"  - {project.get('folder_name')}: {project.get('project_name')}")
    except Exception as e:
        print(f"Registry load error: {e}")
        traceback.print_exc()
    
    # 3. 基本的なプロジェクト作成テスト
    print("\n3. 基本的なプロジェクト作成テスト")
    
    test_project = {
        'folder_name': 'debug_test_project',
        'project_name': 'デバッグテストプロジェクト',
        'description': 'デバッグ用プロジェクト',
        'tags': ['debug', 'test'],
        'status': 'active'
    }
    
    try:
        print("リクエスト送信中...")
        response = client.post('/api/projects/', test_project)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.items())}")
        
        if hasattr(response, 'data'):
            print(f"Response Data: {json.dumps(response.data, indent=2, ensure_ascii=False)}")
        else:
            print(f"Response Content: {response.content}")
            
        # 成功した場合、フォルダ構造を確認
        if response.status_code == 201:
            print("\n✅ プロジェクト作成成功！")
            project_id = response.data.get('id')
            folder_name = response.data.get('folder_name')
            
            # フォルダ構造確認
            print(f"\n4. 作成されたフォルダ構造確認 ({folder_name})")
            try:
                project_path = PROJECT_DATA_DIR / folder_name
                if project_path.exists():
                    print(f"プロジェクトフォルダ: {project_path}")
                    for item in project_path.iterdir():
                        if item.is_dir():
                            print(f"  📁 {item.name}/")
                        else:
                            print(f"  📄 {item.name} ({item.stat().st_size} bytes)")
                            
                    # project.jsonの内容確認
                    project_json = project_path / 'project.json'
                    if project_json.exists():
                        print(f"\nproject.json内容:")
                        with open(project_json, 'r', encoding='utf-8') as f:
                            content = json.load(f)
                            print(json.dumps(content, indent=2, ensure_ascii=False))
                else:
                    print("❌ プロジェクトフォルダが見つかりません")
            except Exception as e:
                print(f"フォルダ構造確認エラー: {e}")
                traceback.print_exc()
                
        else:
            print(f"\n❌ プロジェクト作成失敗: {response.status_code}")
            
    except Exception as e:
        print(f"テスト実行エラー: {e}")
        traceback.print_exc()
    
    # 4. フォルダ構造の詳細説明
    print("\n" + "=" * 60)
    print("プロジェクトフォルダ構造の詳細説明")
    print("=" * 60)
    
    print("""
🏗️ StatVizForge プロジェクト標準フォルダ構造:

📁 /project/[project_folder_name]/
├── 📄 project.json          # プロジェクトメタデータ
├── 📁 raw/                 # 生データ (ユーザーアップロードファイル)
├── 📁 db/                  # データベースファイル 
├── 📁 analysisdata/        # 分析結果・中間データ
└── 📁 git/                 # バージョン管理用

各フォルダの役割:
┌─────────────────┬──────────────────────────────────┐
│ フォルダ名       │ 用途                              │
├─────────────────┼──────────────────────────────────┤
│ raw/            │ • ユーザーがアップロードした生データ  │
│                 │ • CSV, Excel, JSON, 画像ファイル等  │
│                 │ • ファイルエクスプローラーの基準点    │
├─────────────────┼──────────────────────────────────┤
│ db/             │ • SQLiteデータベースファイル        │
│                 │ • データ変換後の構造化データ         │
├─────────────────┼──────────────────────────────────┤
│ analysisdata/   │ • 分析結果のファイル                │
│                 │ • グラフ、レポート、中間計算結果     │
├─────────────────┼──────────────────────────────────┤
│ git/            │ • プロジェクトのバージョン管理        │
│                 │ • 分析スクリプトの履歴管理          │
└─────────────────┴──────────────────────────────────┘

project.json の構造:
{
  "folder_name": "プロジェクトフォルダ名",
  "project_name": "表示用プロジェクト名", 
  "description": "プロジェクトの説明",
  "created_date": "作成日時 (ISO8601)",
  "modified_date": "更新日時 (ISO8601)", 
  "tags": ["タグ1", "タグ2"],
  "status": "active | archived | deleted"
}
""")

def check_file_permissions():
    """ファイル権限の詳細チェック"""
    print("\n" + "=" * 60)
    print("ファイルシステム権限チェック")
    print("=" * 60)
    
    try:
        from config.paths import PROJECT_DATA_DIR
        
        print(f"PROJECT_DATA_DIR: {PROJECT_DATA_DIR}")
        print(f"Absolute path: {PROJECT_DATA_DIR.absolute()}")
        print(f"Exists: {PROJECT_DATA_DIR.exists()}")
        
        if PROJECT_DATA_DIR.exists():
            stat = PROJECT_DATA_DIR.stat()
            print(f"Owner readable: {bool(stat.st_mode & 0o400)}")
            print(f"Owner writable: {bool(stat.st_mode & 0o200)}")
            print(f"Owner executable: {bool(stat.st_mode & 0o100)}")
            print(f"Directory permissions: {oct(stat.st_mode)}")
            
            # テストファイル作成テスト
            test_file = PROJECT_DATA_DIR / 'permission_test.txt'
            try:
                with open(test_file, 'w') as f:
                    f.write('permission test')
                print("✅ ファイル作成テスト成功")
                test_file.unlink()  # クリーンアップ
                print("✅ ファイル削除テスト成功")
            except Exception as e:
                print(f"❌ ファイル作成/削除テスト失敗: {e}")
        else:
            print("❌ PROJECT_DATA_DIR が存在しません")
            # 親ディレクトリの権限確認
            parent = PROJECT_DATA_DIR.parent
            print(f"Parent directory: {parent}")
            print(f"Parent exists: {parent.exists()}")
            if parent.exists():
                print(f"Parent writable: {os.access(parent, os.W_OK)}")
                
    except Exception as e:
        print(f"権限チェックエラー: {e}")
        traceback.print_exc()

if __name__ == '__main__':
    debug_project_creation()
    check_file_permissions()