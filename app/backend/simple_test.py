#!/usr/bin/env python
"""
簡単なAPIテスト
"""

import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
import tempfile
import json

class SimpleAPITest(APITestCase):
    def setUp(self):
        self.mock_registry = {'version': '1.0.0', 'projects': []}

    @patch('api.utils.load_projects_registry')
    @patch('api.utils.save_projects_registry')
    @patch('api.views.ProjectViewSet._create_project_folder_structure')
    def test_project_creation(self, mock_create_folder, mock_save, mock_load):
        """プロジェクト作成テスト"""
        print("\n=== プロジェクト作成テスト開始 ===")
        
        mock_load.return_value = self.mock_registry.copy()
        mock_save.return_value = None
        mock_create_folder.return_value = None
        
        project_data = {
            'folder_name': 'test_project_simple',
            'project_name': 'Simple Test Project',
            'description': 'A simple test project',
            'tags': ['test'],
            'status': 'active'
        }
        
        response = self.client.post('/api/projects/', project_data)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == status.HTTP_201_CREATED:
            print("✅ プロジェクト作成成功")
            print(f"Project ID: {response.data.get('id', 'N/A')}")
            print(f"Project Name: {response.data.get('project_name', 'N/A')}")
            return True
        else:
            print("❌ プロジェクト作成失敗")
            print(f"Error: {response.data}")
            return False

    @patch('api.file_explorer.FileExplorer.get_directory_structure')
    @patch('api.file_comments.FileCommentManager.get_file_summary')
    def test_file_tree_retrieval(self, mock_comments, mock_tree):
        """ファイルツリー取得テスト"""
        print("\n=== ファイルツリー取得テスト開始 ===")
        
        mock_tree.return_value = {
            'name': 'raw',
            'path': '',
            'type': 'directory',
            'size': 0,
            'modified': '2025-07-27T10:00:00',
            'children': []
        }
        mock_comments.return_value = {}
        
        response = self.client.get('/api/files/tree/test_project')
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == status.HTTP_200_OK:
            print("✅ ファイルツリー取得成功")
            print(f"Root Directory: {response.data.get('name', 'N/A')}")
            return True
        else:
            print("❌ ファイルツリー取得失敗")
            print(f"Error: {response.data}")
            return False

    @patch('api.file_explorer.FileExplorer.search_files')
    @patch('api.file_comments.FileCommentManager.get_file_summary')
    def test_file_search(self, mock_comments, mock_search):
        """ファイル検索テスト"""
        print("\n=== ファイル検索テスト開始 ===")
        
        mock_search.return_value = {
            'success': True,
            'query': 'test',
            'search_type': 'name',
            'total_results': 1,
            'results': [
                {
                    'name': 'test.txt',
                    'path': 'test.txt',
                    'type': 'file',
                    'size': 100,
                    'modified': '2025-07-27T10:00:00',
                    'match_type': 'name',
                    'directory': ''
                }
            ]
        }
        mock_comments.return_value = {}
        
        response = self.client.get('/api/files/search/test_project?q=test&type=name')
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == status.HTTP_200_OK:
            print("✅ ファイル検索成功")
            print(f"Results Found: {response.data.get('total_results', 0)}")
            return True
        else:
            print("❌ ファイル検索失敗")
            print(f"Error: {response.data}")
            return False

    @patch('api.file_comments.FileCommentManager.add_comment')
    def test_comment_creation(self, mock_add_comment):
        """コメント追加テスト"""
        print("\n=== コメント追加テスト開始 ===")
        
        mock_add_comment.return_value = {
            'success': True,
            'comment': {
                'id': 'test_comment',
                'text': 'Test comment',
                'author': 'Test User',
                'created_at': '2025-07-27T10:00:00'
            }
        }
        
        comment_data = {
            'file_path': 'test.txt',
            'comment': 'Test comment',
            'author': 'Test User'
        }
        
        response = self.client.post('/api/files/comments/test_project', comment_data)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == status.HTTP_201_CREATED:
            print("✅ コメント追加成功")
            print(f"Comment ID: {response.data.get('comment', {}).get('id', 'N/A')}")
            return True
        else:
            print("❌ コメント追加失敗")
            print(f"Error: {response.data}")
            return False

    def test_server_info(self):
        """サーバー情報取得テスト"""
        print("\n=== サーバー情報取得テスト開始 ===")
        
        response = self.client.get('/api/server-info/')
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == status.HTTP_200_OK:
            print("✅ サーバー情報取得成功")
            print(f"Environment: {response.data.get('environment', 'N/A')}")
            print(f"API Version: {response.data.get('api_version', 'N/A')}")
            return True
        else:
            print("❌ サーバー情報取得失敗")
            print(f"Error: {response.data}")
            return False

def run_simple_tests():
    """簡単なテストスイートを実行"""
    print("=" * 60)
    print("StatVizForge API 簡易テストスイート")
    print("=" * 60)
    
    test_instance = SimpleAPITest('setUp')  # メソッド名を指定
    test_instance.setUp()
    test_instance._pre_setup()  # Django テストの前準備
    
    tests = [
        ('プロジェクト作成', test_instance.test_project_creation),
        ('ファイルツリー取得', test_instance.test_file_tree_retrieval),
        ('ファイル検索', test_instance.test_file_search),
        ('コメント追加', test_instance.test_comment_creation),
        ('サーバー情報取得', test_instance.test_server_info),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            result = test_func()
            results[test_name] = '✅ 成功' if result else '❌ 失敗'
        except Exception as e:
            results[test_name] = f'❌ エラー: {str(e)}'
            print(f"Exception in {test_name}: {e}")
    
    print("\n" + "=" * 60)
    print("テスト結果サマリー")
    print("=" * 60)
    
    success_count = 0
    total_count = len(results)
    
    for test_name, result in results.items():
        print(f"{test_name}: {result}")
        if '✅' in result:
            success_count += 1
    
    print(f"\n合計: {success_count}/{total_count} テスト成功")
    
    if success_count == total_count:
        print("🎉 すべてのテストが成功しました！")
    else:
        print(f"⚠️  {total_count - success_count} 件のテストが失敗しました。")
    
    return results

if __name__ == '__main__':
    results = run_simple_tests()