#!/usr/bin/env python
"""
API テストランナー - 新しいAPIに従った統合テスト
"""

import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

def run_tests():
    """テストを実行"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=False)
    
    print("=== StatVizForge API テスト開始 ===")
    print("新しいクリーンアップされたAPIの包括的テスト")
    print()
    
    # 個別テストクラスを実行
    test_modules = [
        'api.tests.ProjectLifecycleTestCase',
        'api.tests.FileManagementTestCase', 
        'api.tests.FileCommentsTestCase',
        'api.tests.APIIntegrationTestCase',
        'api.tests.ProjectValidationTestCase',
        'api.tests.ProjectIntegrationTestCase',
        'api.tests.ProjectAPIPerformanceTestCase'
    ]
    
    failures = 0
    for module in test_modules:
        print(f"\n{'='*50}")
        print(f"実行中: {module}")
        print('='*50)
        
        result = test_runner.run_tests([module])
        failures += result
        
        if result == 0:
            print(f"✅ {module} - 全テスト合格")
        else:
            print(f"❌ {module} - {result}件のテスト失敗")
    
    print(f"\n{'='*50}")
    print("テスト結果サマリー")
    print('='*50)
    
    if failures == 0:
        print("🎉 全テスト合格！APIは正常に動作しています。")
        return True
    else:
        print(f"⚠️  合計 {failures} 件のテスト失敗")
        return False

if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)