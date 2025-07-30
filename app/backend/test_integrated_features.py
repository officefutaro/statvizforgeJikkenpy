#!/usr/bin/env python3
"""
統合機能テスト: 3つの機能の統合テスト
1. マウスオーバー連動グラフ表示機能
2. 設定ボタンと表示項目変更機能
3. 順序量データの順序決定機能
"""

import os
import sys
import django
import json
from pathlib import Path

# Djangoセットアップ
sys.path.append('/home/futaro/project/StatVizForge_JikkenPy/app/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.models import TableDisplaySettings
from rest_framework.test import APIClient
from rest_framework import status

class IntegratedFeaturesTest(TestCase):
    """統合機能テスト"""
    
    def setUp(self):
        """テストセットアップ"""
        self.client = APIClient()
        self.project_folder = "test_project"
        self.file_name = "test_data.csv"
        
        # テスト用の表示設定データ
        self.test_settings = {
            "table_config": {
                "visibleColumns": ["name", "age", "grade", "score"],
                "columnOrder": ["name", "age", "grade", "score"],
                "columnWidths": {"name": 150, "age": 100, "grade": 120, "score": 100},
                "sortConfig": {"column": "score", "direction": "desc"},
                "filters": {},
                "pageSize": 20
            },
            "chart_config": {
                "enabled": True,
                "type": "bar",
                "xAxis": "grade",
                "yAxis": "score",
                "colorScheme": "blue",
                "showLegend": True,
                "showGrid": True,
                "hoverDetails": {
                    "enabled": True,
                    "showTrend": True,
                    "showBreakdown": True,
                    "showComparison": True
                }
            },
            "layout_config": {
                "split": "horizontal",
                "tableRatio": 0.6,
                "chartRatio": 0.4,
                "hoverMode": "sidebar"
            },
            "column_metadata": {
                "name": {
                    "name": "name",
                    "dataType": "nominal",
                    "displayName": "氏名"
                },
                "age": {
                    "name": "age",
                    "dataType": "ratio",
                    "displayName": "年齢",
                    "numericConfig": {
                        "format": "decimal",
                        "decimalPlaces": 0
                    }
                },
                "grade": {
                    "name": "grade",
                    "dataType": "ordinal",
                    "displayName": "学年",
                    "ordinalConfig": {
                        "customOrder": ["1年生", "2年生", "3年生", "4年生"],
                        "sortDirection": "custom",
                        "autoDetectOrder": False
                    }
                },
                "score": {
                    "name": "score",
                    "dataType": "ratio",
                    "displayName": "得点",
                    "numericConfig": {
                        "format": "decimal",
                        "decimalPlaces": 1
                    }
                }
            }
        }
    
    def test_01_settings_crud_operations(self):
        """設定のCRUD操作テスト"""
        print("テスト1: 設定のCRUD操作")
        
        # 1. 設定の新規作成
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/',
            data=self.test_settings,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertTrue(data['created'])
        self.assertIn('settings', data)
        
        settings_id = data['settings']['id']
        print(f"   ✅ 設定作成成功 (ID: {settings_id[:8]}...)")
        
        # 2. 設定の取得
        response = self.client.get(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['settings'])
        self.assertEqual(data['settings']['id'], settings_id)
        print("   ✅ 設定取得成功")
        
        # 3. 設定の更新
        updated_settings = self.test_settings.copy()
        updated_settings['chart_config']['type'] = 'line'
        updated_settings['layout_config']['split'] = 'vertical'
        
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/',
            data=updated_settings,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertFalse(data['created'])  # 更新なのでFalse
        self.assertEqual(data['settings']['chart_config']['type'], 'line')
        print("   ✅ 設定更新成功")
        
        # 4. プロジェクト設定一覧取得
        response = self.client.get(
            f'/api/table-settings/settings/{self.project_folder}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['total'], 1)
        self.assertEqual(len(data['settings']), 1)
        print("   ✅ 設定一覧取得成功")
        
        # 5. 設定の削除
        response = self.client.delete(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        print("   ✅ 設定削除成功")
        
        # 6. 削除後の確認
        response = self.client.get(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIsNone(data['settings'])
        print("   ✅ 削除確認成功")
    
    def test_02_ordinal_data_ordering(self):
        """順序量データの順序設定テスト"""
        print("\nテスト2: 順序量データの順序設定")
        
        # 順序量データの設定を作成
        ordinal_settings = self.test_settings.copy()
        
        # カスタム順序を設定
        custom_order = ["初級", "中級", "上級", "エキスパート"]
        ordinal_settings['column_metadata']['level'] = {
            "name": "level",
            "dataType": "ordinal",
            "displayName": "レベル",
            "ordinalConfig": {
                "customOrder": custom_order,
                "sortDirection": "custom",
                "autoDetectOrder": False
            }
        }
        
        # 設定を保存
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/',
            data=ordinal_settings,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        
        # 順序量設定が正しく保存されているか確認
        saved_config = data['settings']['column_metadata']['level']['ordinalConfig']
        self.assertEqual(saved_config['customOrder'], custom_order)
        self.assertEqual(saved_config['sortDirection'], 'custom')
        print("   ✅ 順序量データ設定保存成功")
        
        # 順序を変更
        new_order = ["エキスパート", "上級", "中級", "初級"]
        ordinal_settings['column_metadata']['level']['ordinalConfig']['customOrder'] = new_order
        
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/{self.file_name}/',
            data=ordinal_settings,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        updated_config = data['settings']['column_metadata']['level']['ordinalConfig']
        self.assertEqual(updated_config['customOrder'], new_order)
        print("   ✅ 順序量データ順序変更成功")
    
    def test_03_chart_and_hover_configuration(self):
        """チャート・ホバー設定テスト"""
        print("\nテスト3: チャート・ホバー設定")
        
        # 複数のチャートタイプを設定してテスト
        chart_types = ['bar', 'line', 'pie', 'scatter', 'area']
        
        for chart_type in chart_types:
            settings = self.test_settings.copy()
            settings['chart_config']['type'] = chart_type
            settings['chart_config']['hoverDetails']['enabled'] = True
            
            response = self.client.post(
                f'/api/table-settings/settings/{self.project_folder}/chart_{chart_type}.csv/',
                data=settings,
                format='json'
            )
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            data = response.json()
            self.assertTrue(data['success'])
            self.assertEqual(data['settings']['chart_config']['type'], chart_type)
            print(f"   ✅ {chart_type}チャート設定成功")
        
        # すべてのチャート設定が保存されていることを確認
        response = self.client.get(
            f'/api/table-settings/settings/{self.project_folder}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['total'], len(chart_types))
        print(f"   ✅ 全チャート設定保存確認 ({len(chart_types)}件)")
    
    def test_04_layout_configuration(self):
        """レイアウト設定テスト"""
        print("\nテスト4: レイアウト設定")
        
        # 各レイアウト分割モードをテスト
        split_modes = ['horizontal', 'vertical', 'overlay']
        hover_modes = ['tooltip', 'sidebar', 'overlay', 'split']
        
        for split_mode in split_modes:
            for hover_mode in hover_modes:
                settings = self.test_settings.copy()
                settings['layout_config']['split'] = split_mode
                settings['layout_config']['hoverMode'] = hover_mode
                settings['layout_config']['tableRatio'] = 0.7
                settings['layout_config']['chartRatio'] = 0.3
                
                response = self.client.post(
                    f'/api/table-settings/settings/{self.project_folder}/layout_{split_mode}_{hover_mode}.csv/',
                    data=settings,
                    format='json'
                )
                
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                data = response.json()
                self.assertTrue(data['success'])
                
                saved_layout = data['settings']['layout_config']
                self.assertEqual(saved_layout['split'], split_mode)
                self.assertEqual(saved_layout['hoverMode'], hover_mode)
                self.assertEqual(saved_layout['tableRatio'], 0.7)
                
                print(f"   ✅ レイアウト設定成功 ({split_mode}+{hover_mode})")
    
    def test_05_data_type_integration(self):
        """データタイプ統合テスト"""
        print("\nテスト5: データタイプ統合")
        
        # すべてのデータタイプを含む設定
        comprehensive_settings = {
            "table_config": self.test_settings['table_config'],
            "chart_config": self.test_settings['chart_config'],
            "layout_config": self.test_settings['layout_config'],
            "column_metadata": {
                "id": {
                    "name": "id",
                    "dataType": "text",
                    "displayName": "ID"
                },
                "name": {
                    "name": "name",
                    "dataType": "nominal", 
                    "displayName": "名前"
                },
                "age": {
                    "name": "age",
                    "dataType": "ratio",
                    "displayName": "年齢",
                    "numericConfig": {
                        "format": "decimal",
                        "decimalPlaces": 0
                    }
                },
                "height": {
                    "name": "height", 
                    "dataType": "interval",
                    "displayName": "身長",
                    "numericConfig": {
                        "format": "decimal",
                        "decimalPlaces": 1,
                        "unit": "cm"
                    }
                },
                "level": {
                    "name": "level",
                    "dataType": "ordinal",
                    "displayName": "レベル",
                    "ordinalConfig": {
                        "customOrder": ["初心者", "中級者", "上級者", "専門家"],
                        "sortDirection": "custom",
                        "autoDetectOrder": False
                    }
                },
                "created_at": {
                    "name": "created_at",
                    "dataType": "datetime",
                    "displayName": "作成日時",
                    "datetimeConfig": {
                        "format": "YYYY-MM-DD HH:mm:ss",
                        "timezone": "Asia/Tokyo"
                    }
                }
            }
        }
        
        # 統合設定を保存
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/comprehensive_data.csv/',
            data=comprehensive_settings,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        
        # 各データタイプの設定が正しく保存されているか確認
        saved_metadata = data['settings']['column_metadata']
        
        # text型
        self.assertEqual(saved_metadata['id']['dataType'], 'text')
        print("   ✅ text型データ設定成功")
        
        # nominal型
        self.assertEqual(saved_metadata['name']['dataType'], 'nominal')
        print("   ✅ nominal型データ設定成功")
        
        # ratio型
        self.assertEqual(saved_metadata['age']['dataType'], 'ratio')
        self.assertIn('numericConfig', saved_metadata['age'])
        print("   ✅ ratio型データ設定成功")
        
        # interval型
        self.assertEqual(saved_metadata['height']['dataType'], 'interval')
        self.assertEqual(saved_metadata['height']['numericConfig']['unit'], 'cm')
        print("   ✅ interval型データ設定成功")
        
        # ordinal型
        self.assertEqual(saved_metadata['level']['dataType'], 'ordinal')
        self.assertIn('ordinalConfig', saved_metadata['level'])
        expected_order = ["初心者", "中級者", "上級者", "専門家"]
        self.assertEqual(saved_metadata['level']['ordinalConfig']['customOrder'], expected_order)
        print("   ✅ ordinal型データ設定成功")
        
        # datetime型
        self.assertEqual(saved_metadata['created_at']['dataType'], 'datetime')
        self.assertIn('datetimeConfig', saved_metadata['created_at'])
        print("   ✅ datetime型データ設定成功")
    
    def test_06_error_handling(self):
        """エラーハンドリングテスト"""
        print("\nテスト6: エラーハンドリング")
        
        # 存在しない設定の取得
        response = self.client.get(
            f'/api/table-settings/settings/nonexistent_project/nonexistent_file.csv/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertIsNone(data['settings'])
        print("   ✅ 存在しない設定の取得処理成功")
        
        # 存在しない設定の削除
        response = self.client.delete(
            f'/api/table-settings/settings/nonexistent_project/nonexistent_file.csv/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        print("   ✅ 存在しない設定の削除エラー処理成功")
        
        # 不正なデータでの設定保存
        invalid_settings = {"invalid": "data"}
        
        response = self.client.post(
            f'/api/table-settings/settings/{self.project_folder}/invalid_test.csv/',
            data=invalid_settings,
            format='json'
        )
        
        # 不正データでも基本的な保存は成功する（JSONFieldのため）
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("   ✅ 不正データ保存処理成功")

def run_tests():
    """テスト実行"""
    print("=" * 60)
    print("🧪 統合機能テスト開始")
    print("=" * 60) 
    
    # Django testの実行
    from django.test.utils import get_runner
    from django.conf import settings
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # 特定のテストクラスを実行
    failures = test_runner.run_tests(["test_integrated_features.IntegratedFeaturesTest"])
    
    if failures:
        print(f"\n❌ テスト失敗: {failures}件の失敗")
        return False
    else:
        print(f"\n✅ 全テスト成功!")
        return True

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)