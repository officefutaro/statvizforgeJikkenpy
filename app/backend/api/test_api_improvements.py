# -*- coding: utf-8 -*-
"""
API改善テスト
優先順位中以上の改善項目に対するテストケース

テスト対象:
1. URL重複解消
2. ファイルタグAPI統一
3. レスポンス形式統一  
4. 未実装機能完成
"""

from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch, mock_open, MagicMock
import json
import tempfile
import shutil
from pathlib import Path
from test_utils.project_backup import DjangoTestCaseMixin


class APIImprovementsTestCase(DjangoTestCaseMixin, APITestCase):
    """API改善項目のテストケース"""
    
    def setUp(self):
        super().setUp()
        self.test_project = 'test_api_improvements'
        self.temp_dir = tempfile.mkdtemp()
        
        # テスト用のファイルタグデータ
        self.test_tags_data = {
            'data/analysis.csv': ['分析データ', '項目データ'],
            'data/timeseries.csv': ['分析データ', '時系列データ'],
            'docs/readme.txt': ['参考資料']
        }
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        super().tearDown()

    # =============================================================================
    # 1. URL重複解消テスト
    # =============================================================================
    
    @patch('api.views.FileExplorer')
    def test_file_deletion_url_unified(self, mock_explorer):
        """ファイル削除APIのURL統一テスト"""
        mock_explorer_instance = MagicMock()
        mock_explorer.return_value = mock_explorer_instance
        mock_explorer_instance.delete_item.return_value = True
        
        # URLs.pyで定義されたエンドポイントを使用
        url = f'/api/files/delete/{self.test_project}/'
        data = {'file_path': 'test_file.txt'}
        
        response = self.client.delete(url, data=data, format='json')
        
        # 正常レスポンスを確認
        self.assertIn(response.status_code, [200, 404])  # プロジェクト存在に依存
        mock_explorer_instance.delete_item.assert_called_once_with(
            self.test_project, 'test_file.txt'
        )
    
    @patch('api.views.FileExplorer')
    def test_file_move_url_unified(self, mock_explorer):
        """ファイル移動APIのURL統一テスト"""
        mock_explorer_instance = MagicMock()
        mock_explorer.return_value = mock_explorer_instance
        mock_explorer_instance.move_item.return_value = True
        
        # URLs.pyで定義されたエンドポイントを使用
        url = f'/api/files/move/{self.test_project}/'
        data = {
            'source_path': 'old_file.txt',
            'destination_path': 'new_file.txt'
        }
        
        response = self.client.post(url, data=data, format='json')
        
        # 正常レスポンスを確認
        self.assertIn(response.status_code, [200, 404])  # プロジェクト存在に依存
        mock_explorer_instance.move_item.assert_called_once_with(
            self.test_project, 'old_file.txt', 'new_file.txt'
        )
    
    @patch('api.views.FileExplorer')
    def test_directory_creation_url_unified(self, mock_explorer):
        """ディレクトリ作成APIのURL統一テスト"""
        mock_explorer_instance = MagicMock()
        mock_explorer.return_value = mock_explorer_instance
        mock_explorer_instance.create_directory.return_value = True
        
        # URLs.pyで定義されたエンドポイントを使用
        url = f'/api/files/mkdir/{self.test_project}/'
        data = {'dir_path': 'new_directory'}
        
        response = self.client.post(url, data=data, format='json')
        
        # 正常レスポンスを確認
        self.assertIn(response.status_code, [200, 404])  # プロジェクト存在に依存
        mock_explorer_instance.create_directory.assert_called_once_with(
            self.test_project, 'new_directory'
        )
    
    @patch('api.views.FileExplorer')
    @patch('api.views.FileCommentManager')
    def test_file_search_url_unified(self, mock_comment_manager, mock_explorer):
        """ファイル検索APIのURL統一テスト"""
        # FileExplorer のモック設定
        mock_explorer_instance = MagicMock()
        mock_explorer.return_value = mock_explorer_instance
        mock_explorer_instance.search_files.return_value = {
            'results': [],
            'total': 0
        }
        
        # FileCommentManager のモック設定
        mock_comment_manager_instance = MagicMock()
        mock_comment_manager.return_value = mock_comment_manager_instance
        mock_comment_manager_instance.get_file_summary.return_value = {}
        
        # URLs.pyで定義されたエンドポイントを使用
        url = f'/api/files/search/{self.test_project}/'
        response = self.client.get(url, {'q': 'test'})
        
        # 正常レスポンスを確認
        self.assertIn(response.status_code, [200, 404])  # プロジェクト存在に依存

    # =============================================================================
    # 2. ファイルタグAPI統一テスト
    # =============================================================================
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_tags_query_parameter_individual(self, mock_file, mock_exists):
        """個別ファイルタグ取得（クエリパラメータ）テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        # クエリパラメータでファイルパスを指定
        url = f'/api/files/tags/{self.test_project}/'
        response = self.client.get(url, {'file_path': 'data/analysis.csv'})
        
        # レスポンス検証
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn('tags', data)
        self.assertEqual(data['tags'], ['分析データ', '項目データ'])
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_tags_query_parameter_all_files(self, mock_file, mock_exists):
        """全ファイルタグ取得（クエリパラメータなし）テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        # クエリパラメータなしで全ファイル取得
        url = f'/api/files/tags/{self.test_project}/'
        response = self.client.get(url)
        
        # レスポンス検証
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn('files', data)
        self.assertEqual(data['files'], self.test_tags_data)
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_tags_save_unified_response(self, mock_file, mock_exists):
        """ファイルタグ保存の統一レスポンステスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps({})
        
        # タグ保存リクエスト
        url = f'/api/files/tags/{self.test_project}/'
        data = {
            'file_path': 'new_file.csv',
            'tags': ['分析データ', '項目データ']
        }
        response = self.client.post(url, data=data, format='json')
        
        # 統一レスポンス形式の確認
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        
        # 必須フィールドの確認
        self.assertTrue(response_data['success'])
        self.assertEqual(response_data['file_path'], 'new_file.csv')
        self.assertEqual(response_data['tags'], ['分析データ', '項目データ'])
        self.assertIn('updated', response_data)

    # =============================================================================
    # 3. レスポンス形式統一テスト
    # =============================================================================
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_tag_search_response_format(self, mock_file, mock_exists):
        """タグ検索レスポンス形式テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        # ファイルパスの存在チェックもモック
        with patch('pathlib.Path.stat') as mock_stat, \
             patch('pathlib.Path.is_file') as mock_is_file:
            
            mock_stat.return_value.st_size = 1024
            mock_stat.return_value.st_mtime = 1609459200.0  # 2021-01-01
            mock_is_file.return_value = True
            
            # タグ検索リクエスト
            url = f'/api/files/search-by-tags/{self.test_project}/'
            response = self.client.get(url, {'tags': ['分析データ']})
            
            # レスポンス形式確認
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
            
            # 統一レスポンス形式の確認
            self.assertTrue(data['success'])
            self.assertIn('query_tags', data)
            self.assertIn('results', data)
            self.assertIn('total', data)
            self.assertEqual(data['query_tags'], ['分析データ'])
            self.assertGreaterEqual(data['total'], 0)
    
    @patch('pathlib.Path.exists')
    def test_error_response_format_consistency(self, mock_exists):
        """エラーレスポンス形式の一貫性テスト"""
        # 存在しないプロジェクトフォルダ
        mock_exists.return_value = False
        
        # タグ検索リクエスト
        url = f'/api/files/search-by-tags/nonexistent_project/'
        response = self.client.get(url, {'tags': ['test']})
        
        # エラーレスポンス確認
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        data = response.json()
        
        # エラーレスポンス形式確認
        self.assertIn('error', data)
        self.assertIn('message', data)

    # =============================================================================
    # 4. 未実装機能完成テスト
    # =============================================================================
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_search_files_by_tags_implementation(self, mock_file, mock_exists):
        """タグ検索機能実装テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        # ファイルパスの存在チェックもモック
        with patch('pathlib.Path.stat') as mock_stat, \
             patch('pathlib.Path.is_file') as mock_is_file:
            
            mock_stat.return_value.st_size = 2048
            mock_stat.return_value.st_mtime = 1609459200.0
            mock_is_file.return_value = True
            
            # 単一タグ検索
            url = f'/api/files/search-by-tags/{self.test_project}/'
            response = self.client.get(url, {'tags': ['分析データ']})
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
            
            # 検索結果の詳細確認
            self.assertTrue(data['success'])
            self.assertEqual(len(data['results']), 2)  # analysis.csv, timeseries.csv
            
            # 結果の詳細フィールド確認
            for result in data['results']:
                self.assertIn('file_path', result)
                self.assertIn('tags', result)
                self.assertIn('matched_tags', result)
                self.assertIn('size', result)
                self.assertIn('type', result)
                self.assertIn('modified', result)
    
    def test_search_files_by_tags_validation(self):
        """タグ検索バリデーションテスト"""
        # タグパラメータなし
        url = f'/api/files/search-by-tags/{self.test_project}/'
        response = self.client.get(url)
        
        # バリデーションエラー確認
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertIn('error', data)
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_search_files_by_tags_multiple_tags(self, mock_file, mock_exists):
        """複数タグ検索テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        with patch('pathlib.Path.stat') as mock_stat, \
             patch('pathlib.Path.is_file') as mock_is_file:
            
            mock_stat.return_value.st_size = 1024
            mock_stat.return_value.st_mtime = 1609459200.0
            mock_is_file.return_value = True
            
            # 複数タグ検索
            url = f'/api/files/search-by-tags/{self.test_project}/'
            response = self.client.get(url, {'tags': ['分析データ', '参考資料']})
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
            
            # 複数タグのOR検索結果確認
            self.assertTrue(data['success'])
            self.assertEqual(len(data['results']), 3)  # 全ファイルが対象

    # =============================================================================
    # 5. 統合テスト
    # =============================================================================
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_tag_workflow_integration(self, mock_file, mock_exists):
        """タグ機能ワークフロー統合テスト"""
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps({})
        
        # 1. タグ保存
        save_url = f'/api/files/tags/{self.test_project}/'
        save_data = {
            'file_path': 'test_file.csv',
            'tags': ['分析データ', '項目データ']
        }
        save_response = self.client.post(save_url, data=save_data, format='json')
        self.assertEqual(save_response.status_code, status.HTTP_200_OK)
        
        # 2. タグ取得
        # 保存されたタグデータを返すようにモック更新
        updated_tags_data = {'test_file.csv': ['分析データ', '項目データ']}
        mock_file.return_value.read.return_value = json.dumps(updated_tags_data)
        
        get_url = f'/api/files/tags/{self.test_project}/'
        get_response = self.client.get(get_url, {'file_path': 'test_file.csv'})
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        get_data = get_response.json()
        self.assertEqual(get_data['tags'], ['分析データ', '項目データ'])
        
        # 3. タグ検索
        with patch('pathlib.Path.stat') as mock_stat, \
             patch('pathlib.Path.is_file') as mock_is_file:
            
            mock_stat.return_value.st_size = 1024
            mock_stat.return_value.st_mtime = 1609459200.0
            mock_is_file.return_value = True
            
            search_url = f'/api/files/search-by-tags/{self.test_project}/'
            search_response = self.client.get(search_url, {'tags': ['分析データ']})
            self.assertEqual(search_response.status_code, status.HTTP_200_OK)
            search_data = search_response.json()
            self.assertTrue(search_data['success'])
            self.assertGreater(search_data['total'], 0)

    # =============================================================================
    # 6. パフォーマンステスト
    # =============================================================================
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_api_response_time_compliance(self, mock_file, mock_exists):
        """API応答時間基準テスト"""
        import time
        
        # モック設定
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = json.dumps(self.test_tags_data)
        
        # レスポンス時間測定
        start_time = time.time()
        url = f'/api/files/tags/{self.test_project}/'
        response = self.client.get(url)
        end_time = time.time()
        
        # レスポンス時間が1秒未満であることを確認
        response_time = end_time - start_time
        self.assertLess(response_time, 1.0, f"応答時間が遅すぎます: {response_time:.3f}秒")
        self.assertEqual(response.status_code, status.HTTP_200_OK)