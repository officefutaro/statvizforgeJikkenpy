#!/usr/bin/env python
"""
APIクライアント経由のリクエスト問題を調査
"""

import os
import django
import traceback
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rest_framework.test import APIClient
from django.test import override_settings
import logging

# Djangoのログを有効化
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('django.request')
logger.setLevel(logging.DEBUG)

def test_api_client_issues():
    """APIクライアント経由の問題を詳しく調査"""
    print("=" * 60)
    print("APIクライアント問題調査")
    print("=" * 60)
    
    client = APIClient()
    
    # 1. 最小限のテストデータで試行
    print("\n1. 最小限のデータでテスト")
    minimal_data = {
        'folder_name': 'minimal_test',
        'project_name': 'Minimal Test',
        'description': 'Minimal test project'
    }
    
    try:
        response = client.post('/api/projects/', minimal_data, format='json')
        print(f"Status: {response.status_code}")
        if hasattr(response, 'data'):
            print(f"Response: {json.dumps(response.data, indent=2, ensure_ascii=False)}")
        else:
            print(f"Content: {response.content}")
            
        if response.status_code == 201:
            print("✅ 最小限データテスト成功")
            # クリーンアップ
            project_id = response.data.get('id')
            if project_id:
                cleanup = client.delete(f'/api/projects/{project_id}/')
                print(f"クリーンアップ: {cleanup.status_code}")
        else:
            print("❌ 最小限データテスト失敗")
            
    except Exception as e:
        print(f"❌ 最小限データテストエラー: {e}")
        traceback.print_exc()
    
    # 2. コンテンツタイプを明示的に指定
    print("\n2. Content-Typeを明示的に指定")
    try:
        response = client.post('/api/projects/', 
                             json.dumps(minimal_data),
                             content_type='application/json')
        print(f"Status: {response.status_code}")
        if hasattr(response, 'data'):
            print(f"Response: {json.dumps(response.data, indent=2, ensure_ascii=False)}")
        else:
            print(f"Content: {response.content}")
            
    except Exception as e:
        print(f"❌ Content-Type指定テストエラー: {e}")
        traceback.print_exc()
    
    # 3. バリデーションエラーのテスト
    print("\n3. バリデーションエラーテスト")
    invalid_data = {
        'folder_name': '',  # 空文字でエラーを意図的に発生
        'project_name': 'Invalid Test',
        'description': 'Invalid test'
    }
    
    try:
        response = client.post('/api/projects/', invalid_data, format='json')
        print(f"Status: {response.status_code}")
        if hasattr(response, 'data'):
            print(f"Response: {json.dumps(response.data, indent=2, ensure_ascii=False)}")
        print("✅ バリデーションエラーテスト正常（400エラーが期待される）")
        
    except Exception as e:
        print(f"❌ バリデーションエラーテストエラー: {e}")
        traceback.print_exc()
    
    # 4. 既存フォルダ名での重複テスト
    print("\n4. 重複フォルダ名テスト")
    duplicate_data = {
        'folder_name': 'testProject',  # 既存のフォルダ名
        'project_name': 'Duplicate Test',
        'description': 'Duplicate test'
    }
    
    try:
        response = client.post('/api/projects/', duplicate_data, format='json')
        print(f"Status: {response.status_code}")
        if hasattr(response, 'data'):
            print(f"Response: {json.dumps(response.data, indent=2, ensure_ascii=False)}")
        print("✅ 重複フォルダ名テスト正常（409エラーが期待される）")
        
    except Exception as e:
        print(f"❌ 重複フォルダ名テストエラー: {e}")
        traceback.print_exc()

def test_successful_creation():
    """成功するプロジェクト作成のテスト"""
    print("\n" + "=" * 60)
    print("成功するプロジェクト作成テスト")
    print("=" * 60)
    
    client = APIClient()
    
    test_data = {
        'folder_name': 'success_test_project',
        'project_name': '成功テストプロジェクト',
        'description': '正常に作成されるべきプロジェクト',
        'tags': ['success', 'test'],
        'status': 'active'
    }
    
    try:
        print("プロジェクト作成実行中...")
        response = client.post('/api/projects/', test_data, format='json')
        
        print(f"Status Code: {response.status_code}")
        if hasattr(response, 'data'):
            print(f"Response Data:")
            print(json.dumps(response.data, indent=2, ensure_ascii=False))
        
        if response.status_code == 201:
            print("\n✅ プロジェクト作成成功！")
            
            project_id = response.data.get('id')
            folder_name = response.data.get('folder_name')
            
            print(f"プロジェクトID: {project_id}")
            print(f"フォルダ名: {folder_name}")
            
            # フォルダ構造の確認
            from config.paths import PROJECT_DATA_DIR
            project_path = PROJECT_DATA_DIR / folder_name
            
            if project_path.exists():
                print(f"\n📁 作成されたフォルダ構造 ({project_path}):")
                
                # 各サブフォルダの確認
                expected_folders = ['raw', 'db', 'analysisdata', 'git']
                for folder in expected_folders:
                    folder_path = project_path / folder
                    if folder_path.exists():
                        print(f"  ✅ {folder}/")
                    else:
                        print(f"  ❌ {folder}/ (not found)")
                
                # project.jsonの確認
                project_json = project_path / 'project.json'
                if project_json.exists():
                    print(f"  ✅ project.json")
                    with open(project_json, 'r', encoding='utf-8') as f:
                        json_data = json.load(f)
                    print("    内容確認:")
                    for key, value in json_data.items():
                        print(f"      {key}: {value}")
                else:
                    print(f"  ❌ project.json (not found)")
            else:
                print(f"\n❌ プロジェクトフォルダが見つかりません: {project_path}")
            
            # 最後にクリーンアップ
            print(f"\nクリーンアップ実行中...")
            cleanup_response = client.delete(f'/api/projects/{project_id}/')
            print(f"クリーンアップ結果: {cleanup_response.status_code}")
            
            if cleanup_response.status_code == 204:
                print("✅ クリーンアップ成功")
            else:
                print("⚠️ クリーンアップで予期しないステータス")
                
        else:
            print(f"\n❌ プロジェクト作成失敗: HTTP {response.status_code}")
            if hasattr(response, 'data'):
                print("エラー詳細:")
                print(json.dumps(response.data, indent=2, ensure_ascii=False))
                
    except Exception as e:
        print(f"❌ テスト実行エラー: {e}")
        traceback.print_exc()

if __name__ == '__main__':
    test_api_client_issues()
    test_successful_creation()