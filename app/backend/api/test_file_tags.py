"""
File Tags API Tests
ファイルタグ機能のAPIテスト
"""

from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings
from unittest.mock import patch, mock_open, MagicMock
import json
import tempfile
import os
import sys
from pathlib import Path

# プロジェクトルートを追加
sys.path.append(str(Path(__file__).parent.parent))
from test_utils.project_backup import DjangoTestCaseMixin


class FileTagsAPITestCase(DjangoTestCaseMixin, APITestCase):
    """ファイルタグAPI テストケース"""
    
    def setUp(self):
        """テスト前の準備"""
        self.project_folder = 'test_project'
        self.test_file_path = 'data/analysis.csv'
        
        # テスト用タグデータ
        self.test_tags = ['分析データ', '項目データ']
        
        # モックファイルタグデータ
        self.mock_tags_data = {
            'files': [
                {
                    'file_path': 'data/analysis.csv',
                    'tags': ['分析データ']
                },
                {
                    'file_path': 'scripts/process.py',
                    'tags': ['分析データ', '項目データ']
                }
            ]
        }

    def test_save_file_tags_success(self):
        """ファイルタグ保存成功テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        data = {
            'file_path': self.test_file_path,
            'tags': self.test_tags
        }
        
        with patch('api.views.FileViewSet.save_tags') as mock_save:
            mock_save.return_value = {'success': True}
            
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.data['success'])
            mock_save.assert_called_once()

    def test_save_file_tags_validation_error(self):
        """ファイルタグ保存バリデーションエラーテスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        
        # file_pathが欠損している場合
        data = {
            'tags': self.test_tags
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    def test_save_file_tags_invalid_combination(self):
        """無効なタグ組み合わせテスト（項目データのみ）"""
        url = f'/api/files/tags/{self.project_folder}/'
        data = {
            'file_path': self.test_file_path,
            'tags': ['項目データ']  # 分析データなしで項目データのみ
        }
        
        with patch('api.views.FileViewSet.save_tags') as mock_save:
            mock_save.side_effect = ValueError("項目データタグは分析データタグが必要です")
            
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn('error', response.data)

    def test_get_file_tags_success(self):
        """ファイルタグ取得成功テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        
        with patch('api.views.FileViewSet.get_tags') as mock_get:
            mock_get.return_value = {
                'file_path': self.test_file_path,
                'tags': self.test_tags
            }
            
            response = self.client.get(url, {'file_path': self.test_file_path})
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['file_path'], self.test_file_path)
            self.assertEqual(response.data['tags'], self.test_tags)

    def test_get_all_file_tags_success(self):
        """全ファイルタグ取得成功テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        
        with patch('api.views.FileViewSet.get_all_tags') as mock_get_all:
            mock_get_all.return_value = self.mock_tags_data
            
            response = self.client.get(url)
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data['files']), 2)
            self.assertEqual(response.data['files'][0]['file_path'], 'data/analysis.csv')

    def test_search_files_by_tags_success(self):
        """タグによるファイル検索成功テスト"""
        url = f'/api/files/search-by-tags/{self.project_folder}/'
        
        with patch('api.views.FileViewSet.search_by_tags') as mock_search:
            mock_search.return_value = {
                'success': True,
                'search_tags': ['分析データ'],
                'results': [
                    {
                        'name': 'analysis.csv',
                        'path': 'data/analysis.csv',
                        'type': 'file',
                        'tags': ['分析データ', '項目データ'],
                        'size': 2048,
                        'modified': '2025-07-28T10:00:00'
                    }
                ]
            }
            
            response = self.client.get(url, {'tags': '分析データ'})
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertTrue(response.data['success'])
            self.assertEqual(len(response.data['results']), 1)

    def test_search_files_by_multiple_tags(self):
        """複数タグによる検索テスト"""
        url = f'/api/files/search-by-tags/{self.project_folder}/'
        
        with patch('api.views.FileViewSet.search_by_tags') as mock_search:
            mock_search.return_value = {
                'success': True,
                'search_tags': ['分析データ', '項目データ'],
                'results': []
            }
            
            response = self.client.get(url, {'tags': '分析データ,項目データ'})
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            mock_search.assert_called_once()

    def test_tag_validation_rules(self):
        """タグバリデーションルールテスト"""
        # 分析データタグがある場合のみ項目データタグが許可される
        valid_combinations = [
            ['分析データ'],
            ['分析データ', '項目データ'],
        ]
        
        invalid_combinations = [
            ['項目データ'],  # 分析データなし
            ['分析データ', '分析データ'],  # 重複
            ['不正なタグ'],  # 未定義タグ
        ]

        url = f'/api/files/tags/{self.project_folder}/'
        
        # 有効な組み合わせのテスト
        for tags in valid_combinations:
            with patch('api.views.FileViewSet.save_tags') as mock_save:
                mock_save.return_value = {'success': True}
                
                data = {
                    'file_path': self.test_file_path,
                    'tags': tags
                }
                
                response = self.client.post(url, data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 無効な組み合わせのテスト
        for tags in invalid_combinations:
            with patch('api.views.FileViewSet.save_tags') as mock_save:
                mock_save.side_effect = ValueError("Invalid tag combination")
                
                data = {
                    'file_path': self.test_file_path,
                    'tags': tags
                }
                
                response = self.client.post(url, data, format='json')
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_file_tags_persistence(self):
        """ファイルタグ永続化テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        data = {
            'file_path': self.test_file_path,
            'tags': self.test_tags
        }
        
        # タグ保存をテスト
        with patch('builtins.open', mock_open()) as mock_file:
            with patch('json.dump') as mock_json_dump:
                with patch('api.views.FileViewSet.save_tags') as mock_save:
                    mock_save.return_value = {'success': True}
                    
                    response = self.client.post(url, data, format='json')
                    
                    self.assertEqual(response.status_code, status.HTTP_200_OK)
                    # ファイル書き込みが行われたことを確認
                    mock_file.assert_called()

    def test_project_not_found_error(self):
        """存在しないプロジェクトでのエラーテスト"""
        url = '/api/files/tags/nonexistent_project/'
        data = {
            'file_path': self.test_file_path,
            'tags': self.test_tags
        }
        
        with patch('pathlib.Path.exists', return_value=False):
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_concurrent_tag_operations(self):
        """並行タグ操作テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        
        # 複数のファイルに対する同時タグ操作をシミュレート
        files = [
            ('file1.csv', ['分析データ']),
            ('file2.csv', ['分析データ', '項目データ']),
            ('file3.py', ['分析データ']),
        ]
        
        for file_path, tags in files:
            data = {
                'file_path': file_path,
                'tags': tags
            }
            
            with patch('api.views.FileViewSet.save_tags') as mock_save:
                mock_save.return_value = {'success': True}
                
                response = self.client.post(url, data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_api_error_handling(self):
        """タグAPIエラーハンドリングテスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        data = {
            'file_path': self.test_file_path,
            'tags': self.test_tags
        }
        
        # ファイルI/Oエラーのシミュレート
        with patch('api.views.FileViewSet.save_tags') as mock_save:
            mock_save.side_effect = IOError("Disk full")
            
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertIn('error', response.data)

    def test_tag_api_response_format(self):
        """タグAPIレスポンス形式テスト"""
        url = f'/api/files/tags/{self.project_folder}/'
        data = {
            'file_path': self.test_file_path,
            'tags': self.test_tags
        }
        
        with patch('api.views.FileViewSet.save_tags') as mock_save:
            mock_save.return_value = {
                'success': True,
                'file_path': self.test_file_path,
                'tags': self.test_tags,
                'updated': '2025-07-28T10:00:00'
            }
            
            response = self.client.post(url, data, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # レスポンス形式の確認
            required_fields = ['success', 'file_path', 'tags']
            for field in required_fields:
                self.assertIn(field, response.data)
            
            self.assertTrue(response.data['success'])
            self.assertEqual(response.data['file_path'], self.test_file_path)
            self.assertEqual(response.data['tags'], self.test_tags)