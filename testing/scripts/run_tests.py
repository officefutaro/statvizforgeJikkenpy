#!/usr/bin/env python
"""
StatVizForge API Test Runner
APIテストの実行とレポート生成
"""

import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner
from django.core.management import execute_from_command_line
import time
from datetime import datetime
from pathlib import Path

def setup_django():
    """Django環境のセットアップ"""
    # スクリプトの場所からバックエンドディレクトリを特定
    script_dir = Path(__file__).parent  # testing/scripts
    testing_dir = script_dir.parent     # testing
    project_root = testing_dir.parent   # project root
    backend_dir = project_root / "app" / "backend"
    
    # バックエンドディレクトリをPythonパスに追加
    sys.path.insert(0, str(backend_dir))
    
    # 作業ディレクトリをバックエンドディレクトリに変更
    os.chdir(backend_dir)
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()

def run_all_tests():
    """全てのテストを実行"""
    print("=" * 60)
    print("StatVizForge API テストスイート")
    print("=" * 60)
    print(f"実行開始時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    start_time = time.time()
    
    # Djangoテストランナーを使用
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=False, keepdb=False)
    
    # テスト実行
    failures = test_runner.run_tests(['api.tests'])
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print()
    print("=" * 60)
    print("テスト実行結果")
    print("=" * 60)
    print(f"実行時間: {execution_time:.2f}秒")
    print(f"失敗数: {failures}")
    
    if failures == 0:
        print("✅ 全てのテストが成功しました！")
        return True
    else:
        print("❌ テストに失敗しました。")
        return False

def run_specific_test(test_name):
    """特定のテストクラスまたはメソッドを実行"""
    print(f"特定テスト実行: {test_name}")
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=False)
    
    failures = test_runner.run_tests([f'api.tests.{test_name}'])
    return failures == 0

def run_lifecycle_test():
    """ライフサイクルテストのみ実行"""
    return run_specific_test('ProjectLifecycleTestCase.test_complete_project_lifecycle')

def run_compatibility_test():
    """互換性テストのみ実行"""
    return run_specific_test('ProjectLifecycleTestCase.test_endpoint_compatibility')

def run_performance_test():
    """パフォーマンステストのみ実行"""
    return run_specific_test('ProjectAPIPerformanceTestCase.test_api_response_time')

def main():
    """メイン実行関数"""
    setup_django()
    
    if len(sys.argv) > 1:
        test_type = sys.argv[1].lower()
        
        if test_type == 'lifecycle':
            success = run_lifecycle_test()
        elif test_type == 'compatibility':
            success = run_compatibility_test()
        elif test_type == 'performance':
            success = run_performance_test()
        elif test_type == 'all':
            success = run_all_tests()
        else:
            print("使用方法:")
            print("  python run_tests.py [all|lifecycle|compatibility|performance]")
            print()
            print("  all          - 全てのテストを実行")
            print("  lifecycle    - プロジェクトライフサイクルテストのみ")
            print("  compatibility - エンドポイント互換性テストのみ")
            print("  performance  - パフォーマンステストのみ")
            return
    else:
        success = run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()