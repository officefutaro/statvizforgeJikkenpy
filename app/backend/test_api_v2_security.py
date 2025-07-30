#!/usr/bin/env python
"""
API v2.0 セキュリティテストスクリプト
ファイルパスバリデーション、プロジェクトフォルダ名検証などのセキュリティ機能をテスト
"""

import requests
import json
import sys
from datetime import datetime
from typing import Dict, List, Tuple

# APIベースURL
BASE_URL = "http://localhost:8000/api/v1"
LEGACY_URL = "http://localhost:8000/api"

class SecurityTestRunner:
    def __init__(self):
        self.results = []
        self.passed = 0
        self.failed = 0
    
    def test_file_path_validation(self):
        """ファイルパスバリデーションのテスト"""
        print("\n=== ファイルパスバリデーションテスト ===")
        
        # テストケース：危険なパス
        dangerous_paths = [
            ("../../../etc/passwd", "ディレクトリトラバーサル攻撃"),
            ("/etc/passwd", "絶対パス"),
            ("..\\..\\windows\\system32", "Windows形式のトラバーサル"),
            ("file\0.csv", "Null文字"),
            ("file\n.csv", "改行文字"),
            ("~/.ssh/id_rsa", "ホームディレクトリ展開"),
        ]
        
        # 正常なパス
        valid_paths = [
            ("data/file.csv", "通常のファイルパス"),
            ("folder/subfolder/file.txt", "ネストしたパス"),
            ("file_name-123.csv", "有効な文字のみ"),
        ]
        
        # プロジェクト作成（テスト用）
        project_data = {
            "folder_name": "security_test_project",
            "project_name": "セキュリティテスト",
            "description": "セキュリティテスト用プロジェクト"
        }
        
        response = requests.post(f"{BASE_URL}/projects/", json=project_data)
        if response.status_code == 201:
            print("✅ テスト用プロジェクト作成成功")
        
        # 危険なパスのテスト
        for path, description in dangerous_paths:
            data = {"file_path": path, "description": "テスト"}
            response = requests.post(
                f"{BASE_URL}/files/descriptions/security_test_project/",
                json=data
            )
            
            if response.status_code == 400:
                self.passed += 1
                print(f"✅ {description}: 適切にブロック ({path})")
            else:
                self.failed += 1
                print(f"❌ {description}: ブロックされず ({path}) - Status: {response.status_code}")
        
        # 正常なパスのテスト
        for path, description in valid_paths:
            data = {"file_path": path, "description": "テスト"}
            response = requests.post(
                f"{BASE_URL}/files/descriptions/security_test_project/",
                json=data
            )
            
            if response.status_code in [200, 201]:
                self.passed += 1
                print(f"✅ {description}: 正常に処理 ({path})")
            else:
                self.failed += 1
                print(f"❌ {description}: 誤ってブロック ({path}) - Status: {response.status_code}")
    
    def test_project_folder_validation(self):
        """プロジェクトフォルダ名バリデーションのテスト"""
        print("\n=== プロジェクトフォルダ名バリデーションテスト ===")
        
        # テストケース
        test_cases = [
            ("valid_project-123", True, "英数字とハイフン、アンダースコア"),
            ("invalid/project", False, "スラッシュを含む"),
            ("project with spaces", False, "スペースを含む"),
            ("プロジェクト", False, "日本語文字"),
            ("project@test", False, "特殊文字"),
            ("a" * 101, False, "100文字超過"),
            ("test.project", False, "ドットを含む"),
            ("PROJECT_TEST", True, "大文字を含む"),
        ]
        
        for folder_name, should_succeed, description in test_cases:
            project_data = {
                "folder_name": folder_name,
                "project_name": f"テスト: {description}",
                "description": "バリデーションテスト"
            }
            
            response = requests.post(f"{BASE_URL}/projects/", json=project_data)
            
            if should_succeed:
                if response.status_code == 201:
                    self.passed += 1
                    print(f"✅ {description}: 正常に作成 ({folder_name})")
                    # クリーンアップ
                    if "id" in response.json():
                        requests.delete(f"{BASE_URL}/projects/{response.json()['id']}/")
                else:
                    self.failed += 1
                    print(f"❌ {description}: 作成失敗 ({folder_name}) - Status: {response.status_code}")
            else:
                if response.status_code == 400:
                    self.passed += 1
                    print(f"✅ {description}: 適切に拒否 ({folder_name})")
                else:
                    self.failed += 1
                    print(f"❌ {description}: 拒否されず ({folder_name}) - Status: {response.status_code}")
    
    def test_api_versioning(self):
        """APIバージョニングのテスト"""
        print("\n=== APIバージョニングテスト ===")
        
        # v1エンドポイント
        response_v1 = requests.get(f"{BASE_URL}/projects/")
        if response_v1.status_code == 200:
            self.passed += 1
            print("✅ v1エンドポイント: 正常動作")
        else:
            self.failed += 1
            print(f"❌ v1エンドポイント: エラー - Status: {response_v1.status_code}")
        
        # レガシーエンドポイント（後方互換性）
        response_legacy = requests.get(f"{LEGACY_URL}/projects/")
        if response_legacy.status_code == 200:
            self.passed += 1
            print("✅ レガシーエンドポイント: 後方互換性維持")
        else:
            self.failed += 1
            print(f"❌ レガシーエンドポイント: エラー - Status: {response_legacy.status_code}")
        
        # 同じ結果が返ることを確認
        if response_v1.status_code == 200 and response_legacy.status_code == 200:
            if response_v1.json() == response_legacy.json():
                self.passed += 1
                print("✅ バージョン間の一貫性: 同じ結果")
            else:
                self.failed += 1
                print("❌ バージョン間の一貫性: 異なる結果")
    
    def test_error_response_format(self):
        """統一エラーレスポンス形式のテスト"""
        print("\n=== エラーレスポンス形式テスト ===")
        
        # 様々なエラーを発生させる
        error_cases = [
            (f"{BASE_URL}/projects/invalid-uuid/", "GET", None, 404, "存在しないプロジェクト"),
            (f"{BASE_URL}/files/tree/nonexistent/", "GET", None, 404, "存在しないフォルダ"),
            (f"{BASE_URL}/projects/", "POST", {"folder_name": ""}, 400, "必須フィールド欠如"),
        ]
        
        for url, method, data, expected_status, description in error_cases:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, json=data)
            
            if response.status_code == expected_status:
                try:
                    error_data = response.json()
                    if "error" in error_data and "message" in error_data:
                        self.passed += 1
                        print(f"✅ {description}: 統一エラー形式")
                    else:
                        self.failed += 1
                        print(f"❌ {description}: エラー形式が不統一")
                except:
                    self.failed += 1
                    print(f"❌ {description}: JSONパースエラー")
            else:
                self.failed += 1
                print(f"❌ {description}: 予期しないステータス - {response.status_code}")
    
    def generate_report(self):
        """テスト結果レポートの生成"""
        print("\n" + "=" * 50)
        print("セキュリティテスト結果サマリー")
        print("=" * 50)
        print(f"実行日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"合格: {self.passed}")
        print(f"失敗: {self.failed}")
        print(f"合計: {self.passed + self.failed}")
        print(f"成功率: {(self.passed / (self.passed + self.failed) * 100):.1f}%")
        
        return self.passed, self.failed
    
    def run_all_tests(self):
        """すべてのテストを実行"""
        print("API v2.0 セキュリティテスト開始")
        print("=" * 50)
        
        self.test_api_versioning()
        self.test_project_folder_validation()
        self.test_file_path_validation()
        self.test_error_response_format()
        
        return self.generate_report()


if __name__ == "__main__":
    runner = SecurityTestRunner()
    passed, failed = runner.run_all_tests()
    
    # 終了コード：失敗があれば1、すべて成功なら0
    sys.exit(0 if failed == 0 else 1)