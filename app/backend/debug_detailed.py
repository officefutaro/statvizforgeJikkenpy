#!/usr/bin/env python
"""
より詳細なエラー調査
"""

import os
import django
import traceback
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# ログレベルを設定
logging.basicConfig(level=logging.DEBUG)

from api.views import ProjectViewSet
from api.utils import load_projects_registry, save_projects_registry
from unittest.mock import Mock
import uuid
from datetime import datetime

def test_project_creation_directly():
    """直接APIビューをテストして詳細エラーを確認"""
    print("=" * 60)
    print("直接API呼び出しテスト")
    print("=" * 60)
    
    # モックリクエストを作成
    mock_request = Mock()
    mock_request.data = {
        'folder_name': 'direct_test_project',
        'project_name': '直接テストプロジェクト',
        'description': '直接テスト用プロジェクト',
        'tags': ['test'],
        'status': 'active'
    }
    mock_request.META = {'HTTP_ACCEPT_LANGUAGE': 'ja'}
    
    # ViewSetを直接呼び出し
    view = ProjectViewSet()
    
    try:
        print("1. プロジェクトレジストリ読み込みテスト")
        registry = load_projects_registry()
        print(f"✅ レジストリ読み込み成功: {len(registry.get('projects', []))} projects")
        
        print("\n2. フォルダ構造作成テスト")
        test_data = {
            'folder_name': 'structure_test',
            'project_name': 'テストプロジェクト',
            'description': 'テスト説明',
            'created_date': datetime.now().isoformat(),
            'modified_date': datetime.now().isoformat(),
            'tags': ['test'],
            'status': 'active'
        }
        
        try:
            view._create_project_folder_structure('structure_test', test_data)
            print("✅ フォルダ構造作成成功")
            
            # 作成されたファイルを確認
            from config.paths import PROJECT_DATA_DIR
            test_project_path = PROJECT_DATA_DIR / 'structure_test'
            if test_project_path.exists():
                print(f"作成されたフォルダ: {test_project_path}")
                for item in test_project_path.iterdir():
                    print(f"  - {item.name}")
                    
                # クリーンアップ
                import shutil
                shutil.rmtree(test_project_path)
                print("✅ テストフォルダクリーンアップ完了")
            else:
                print("❌ テストフォルダが見つかりません")
                
        except Exception as e:
            print(f"❌ フォルダ構造作成エラー: {e}")
            traceback.print_exc()
        
        print("\n3. レジストリ保存テスト")
        try:
            # テスト用のレジストリデータ
            test_registry = registry.copy()
            test_project = {
                'id': str(uuid.uuid4()),
                'folder_name': 'save_test',
                'project_name': 'セーブテスト',
                'description': 'セーブテスト',
                'created_date': datetime.now().isoformat(),
                'modified_date': datetime.now().isoformat(),
                'tags': [],
                'status': 'active'
            }
            
            test_registry['projects'].append(test_project)
            save_projects_registry(test_registry)
            print("✅ レジストリ保存テスト成功")
            
            # 元に戻す
            save_projects_registry(registry)
            print("✅ レジストリリストア完了")
            
        except Exception as e:
            print(f"❌ レジストリ保存エラー: {e}")
            traceback.print_exc()
        
        print("\n4. 完全な作成フローテスト")
        try:
            response = view.create(mock_request)
            print(f"レスポンスステータス: {response.status_code}")
            print(f"レスポンスデータ: {response.data}")
            
            if response.status_code == 201:
                print("✅ 完全な作成フロー成功")
                
                # クリーンアップ
                project_id = response.data.get('id')
                if project_id:
                    cleanup_response = view.destroy(Mock(META={'HTTP_ACCEPT_LANGUAGE': 'ja'}), pk=project_id)
                    print(f"クリーンアップ: {cleanup_response.status_code}")
            else:
                print(f"❌ 完全な作成フロー失敗: {response.status_code}")
                print(f"エラー詳細: {response.data}")
                
        except Exception as e:
            print(f"❌ 完全な作成フローエラー: {e}")
            traceback.print_exc()
            
    except Exception as e:
        print(f"❌ 全体テストエラー: {e}")
        traceback.print_exc()

def analyze_existing_projects():
    """既存プロジェクトの詳細分析"""
    print("\n" + "=" * 60)
    print("既存プロジェクト詳細分析")
    print("=" * 60)
    
    try:
        from config.paths import PROJECT_DATA_DIR
        print(f"プロジェクトデータディレクトリ: {PROJECT_DATA_DIR}")
        
        for item in PROJECT_DATA_DIR.iterdir():
            if item.is_dir() and item.name != 'trash':
                print(f"\n📁 プロジェクト: {item.name}")
                print(f"  パス: {item}")
                
                # project.jsonの確認
                project_json = item / 'project.json'
                if project_json.exists():
                    import json
                    try:
                        with open(project_json, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        print(f"  プロジェクト名: {data.get('project_name')}")
                        print(f"  作成日: {data.get('created_date')}")
                        print(f"  ステータス: {data.get('status')}")
                    except Exception as e:
                        print(f"  ❌ project.json読み込みエラー: {e}")
                else:
                    print("  ❌ project.jsonが見つかりません")
                
                # サブフォルダの確認
                print("  サブフォルダ:")
                for subitem in item.iterdir():
                    if subitem.is_dir():
                        file_count = len(list(subitem.iterdir())) if subitem.exists() else 0
                        print(f"    📁 {subitem.name}/ ({file_count} items)")
                    else:
                        size = subitem.stat().st_size if subitem.exists() else 0
                        print(f"    📄 {subitem.name} ({size} bytes)")
    
    except Exception as e:
        print(f"❌ 既存プロジェクト分析エラー: {e}")
        traceback.print_exc()

if __name__ == '__main__':
    test_project_creation_directly()
    analyze_existing_projects()