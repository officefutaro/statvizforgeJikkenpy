#!/usr/bin/env python3
"""
Project Registry Cleanup Script
プロジェクトレジストリクリーンアップスクリプト
"""

import json
import os
from pathlib import Path
from datetime import datetime

def cleanup_projects_registry():
    """プロジェクトレジストリのクリーンアップ"""
    
    registry_path = Path("projects-registry.json")
    project_dir = Path(".")
    
    if not registry_path.exists():
        print("❌ projects-registry.json が見つかりません")
        return
        
    # レジストリファイルを読み込み
    with open(registry_path, 'r', encoding='utf-8') as f:
        registry = json.load(f)
    
    print(f"📊 処理前: {len(registry.get('projects', []))} 個のプロジェクト")
    
    # 実際に存在するフォルダを確認
    existing_folders = set()
    for item in project_dir.iterdir():
        if item.is_dir() and item.name not in ['trash', '.git', '__pycache__']:
            existing_folders.add(item.name)
    
    print(f"📁 実際のフォルダ: {sorted(existing_folders)}")
    
    # バックアップ作成
    backup_path = f"projects-registry.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    print(f"💾 バックアップ作成: {backup_path}")
    
    # クリーンアップ処理
    valid_projects = []
    removed_count = 0
    fixed_count = 0
    
    for project in registry.get('projects', []):
        folder_name = project.get('folder_name')
        
        # フォルダが存在しないプロジェクトを除外
        if folder_name not in existing_folders:
            print(f"🗑️  削除: {folder_name} (フォルダが存在しない)")
            removed_count += 1
            continue
            
        # データ型の修正
        if isinstance(project.get('project_name'), list):
            project['project_name'] = project['project_name'][0] if project['project_name'] else folder_name
            print(f"🔧 修正: {folder_name} の project_name を配列から文字列に変更")
            fixed_count += 1
            
        if isinstance(project.get('tags'), str):
            project['tags'] = [project['tags']] if project['tags'] else []
            print(f"🔧 修正: {folder_name} の tags を文字列から配列に変更")
            fixed_count += 1
            
        if not isinstance(project.get('tags'), list):
            project['tags'] = []
            print(f"🔧 修正: {folder_name} の tags を空配列に設定")
            fixed_count += 1
            
        valid_projects.append(project)
    
    # レジストリ更新
    registry['projects'] = valid_projects
    registry['last_updated'] = datetime.now().isoformat()
    
    # ファイル保存
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    
    print(f"✅ クリーンアップ完了:")
    print(f"   - 削除: {removed_count} 個")
    print(f"   - 修正: {fixed_count} 個")
    print(f"   - 残存: {len(valid_projects)} 個")

if __name__ == '__main__':
    cleanup_projects_registry()