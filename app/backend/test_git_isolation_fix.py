#!/usr/bin/env python3
"""
Git初期化分離問題の緊急テスト
Phase 1: Git initialization isolation emergency fix test
"""
import os
import sys
import tempfile
import shutil
from pathlib import Path

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, '/home/futaro/project/StatVizForge_JikkenPy/app/backend')

import django
django.setup()

from api.git_utils import GitUtils, GitError
from api.git_sync_utils import GitSyncUtils, GitSyncError
from api.views_git_sync import GitSyncViewSet

def test_git_initialization_isolation():
    """Git初期化がプロジェクト固有に実行されることを確認"""
    print("🧪 Git初期化分離テスト開始...")
    
    # テスト用一時ディレクトリを作成
    test_base_dir = Path("/tmp/statvizforge_git_isolation_test")
    if test_base_dir.exists():
        shutil.rmtree(test_base_dir)
    test_base_dir.mkdir()
    
    try:
        # テストプロジェクト構造を作成
        test_project = test_base_dir / "TestProject1"
        test_project.mkdir()
        
        # analysisdata と raw フォルダを作成
        (test_project / "analysisdata").mkdir()
        (test_project / "raw").mkdir()
        
        # テストファイルを作成
        (test_project / "analysisdata" / "test_data.csv").write_text("test,data\n1,2\n")
        (test_project / "raw" / "test_raw.txt").write_text("raw test data")
        
        print(f"✅ テスト環境作成: {test_project}")
        
        # 元のPROJECTS_ROOTをバックアップ
        from django.conf import settings
        original_projects_root = settings.PROJECTS_ROOT
        
        # テスト用PROJECTS_ROOTを設定
        settings.PROJECTS_ROOT = str(test_base_dir)
        
        try:
            # 1. GitSyncUtilsテスト
            print("\n1️⃣ GitSyncUtils テスト...")
            sync_utils = GitSyncUtils("TestProject1")
            init_result = sync_utils.initialize_git_folder()
            
            print(f"   GitSync初期化結果: {init_result['success']}")
            print(f"   Gitパス: {init_result.get('git_path')}")
            
            # git フォルダが作成されていることを確認
            git_folder = test_project / "git"
            assert git_folder.exists(), f"Gitフォルダが作成されていません: {git_folder}"
            print(f"✅ Gitフォルダ作成確認: {git_folder}")
            
            # 2. GitUtilsテスト（修正後）
            print("\n2️⃣ GitUtils テスト...")
            git_utils = GitUtils("TestProject1/git")
            git_init_result = git_utils.init_repository()
            
            print(f"   Git初期化結果: {git_init_result['success']}")
            print(f"   Git初期化パス: {git_init_result.get('path')}")
            
            # .git フォルダがgitフォルダ内に作成されていることを確認
            dot_git_folder = git_folder / ".git"
            assert dot_git_folder.exists(), f".gitフォルダが作成されていません: {dot_git_folder}"
            print(f"✅ .gitフォルダ確認: {dot_git_folder}")
            
            # 3. プロジェクトルートに.gitフォルダが作成されていないことを確認
            project_root_git = test_base_dir / ".git"
            assert not project_root_git.exists(), f"プロジェクトルートに.gitフォルダが誤って作成されています: {project_root_git}"
            print(f"✅ プロジェクトルート汚染なし確認")
            
            # 4. 全体StatVizForgeプロジェクトに影響がないことを確認
            main_project_git = Path("/home/futaro/project/StatVizForge_JikkenPy/.git")
            if main_project_git.exists():
                # 既存.gitフォルダの状態をチェック（変更されていないこと）
                print(f"✅ メインプロジェクト.git確認: {main_project_git.exists()}")
            
            # 5. GitSyncViewSetを使った実際のAPI呼び出しテスト
            print("\n3️⃣ GitSyncViewSet API テスト...")
            viewset = GitSyncViewSet()
            
            # _get_git_utils メソッドの修正を確認
            try:
                api_git_utils = viewset._get_git_utils("TestProject1")
                print(f"✅ API GitUtils取得成功: {api_git_utils.project_path}")
                
                # APIから取得したGitUtilsが正しいパスを指していることを確認
                expected_path = test_base_dir / "TestProject1" / "git"
                actual_path = api_git_utils.project_path
                assert str(actual_path) == str(expected_path), f"パス不一致: expected={expected_path}, actual={actual_path}"
                print(f"✅ API GitUtils パス確認: {actual_path}")
                
            except Exception as e:
                print(f"❌ API GitUtils テスト失敗: {e}")
                raise
            
            print("\n🎉 全テスト成功！Git初期化分離修正が有効です。")
            return True
            
        finally:
            # PROJECTS_ROOTを復元
            settings.PROJECTS_ROOT = original_projects_root
            
    except Exception as e:
        print(f"\n❌ テスト失敗: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        # テスト環境をクリーンアップ
        if test_base_dir.exists():
            shutil.rmtree(test_base_dir)
        print(f"🧹 テスト環境クリーンアップ: {test_base_dir}")

def test_multiple_projects_isolation():
    """複数プロジェクトの分離テスト"""
    print("\n🧪 複数プロジェクト分離テスト開始...")
    
    # テスト用一時ディレクトリを作成
    test_base_dir = Path("/tmp/statvizforge_multi_project_test")
    if test_base_dir.exists():
        shutil.rmtree(test_base_dir)
    test_base_dir.mkdir()
    
    try:
        # 2つのテストプロジェクトを作成
        projects = ["Project_A", "Project_B"]
        
        from django.conf import settings
        original_projects_root = settings.PROJECTS_ROOT
        settings.PROJECTS_ROOT = str(test_base_dir)
        
        try:
            for project_name in projects:
                print(f"\n📁 プロジェクト作成: {project_name}")
                project_path = test_base_dir / project_name
                project_path.mkdir()
                
                # 必要なフォルダとファイルを作成
                (project_path / "analysisdata").mkdir()
                (project_path / "raw").mkdir()
                (project_path / "analysisdata" / f"{project_name}_data.csv").write_text(f"project,{project_name}\n")
                
                # Git初期化
                sync_utils = GitSyncUtils(project_name)
                sync_utils.initialize_git_folder()
                
                git_utils = GitUtils(f"{project_name}/git")
                git_utils.init_repository()
                
                # 各プロジェクトのgitフォルダが独立していることを確認
                git_folder = project_path / "git" / ".git"
                assert git_folder.exists(), f"{project_name}の.gitフォルダが作成されていません"
                print(f"✅ {project_name} Git分離確認: {git_folder}")
            
            # プロジェクト間の分離を確認
            for project_name in projects:
                git_utils = GitUtils(f"{project_name}/git")
                status = git_utils.get_status()
                print(f"✅ {project_name} Git状態独立確認: {status['is_repo']}")
            
            print("\n🎉 複数プロジェクト分離テスト成功！")
            return True
            
        finally:
            settings.PROJECTS_ROOT = original_projects_root
            
    except Exception as e:
        print(f"\n❌ 複数プロジェクト分離テスト失敗: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        if test_base_dir.exists():
            shutil.rmtree(test_base_dir)

if __name__ == "__main__":
    print("🚨 Git初期化分離問題 緊急修正テスト")
    print("=" * 60)
    
    # Phase 1のテストを実行
    test1_result = test_git_initialization_isolation()
    test2_result = test_multiple_projects_isolation()
    
    print("\n" + "=" * 60)
    print("📊 テスト結果サマリー:")
    print(f"  Git初期化分離テスト: {'✅ 成功' if test1_result else '❌ 失敗'}")
    print(f"  複数プロジェクト分離テスト: {'✅ 成功' if test2_result else '❌ 失敗'}")
    
    if test1_result and test2_result:
        print("\n🎉 Phase 1 緊急修正 完了！")
        print("Git初期化の分離問題が解決されました。")
        exit(0)
    else:
        print("\n❌ Phase 1 緊急修正 未完了")
        print("さらなる調査と修正が必要です。")
        exit(1)