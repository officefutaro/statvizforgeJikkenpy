"""
アーカイブファイルのクリーンアップユーティリティ
起動時に保存期間を超えたアーカイブファイルを削除
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from config.paths import BASE_DIR
from .utils import load_projects_registry, save_projects_registry


def cleanup_expired_archives():
    """保存期間を超えたアーカイブファイルを削除"""
    print("Starting archive cleanup...")
    
    # パス設定
    trash_dir = BASE_DIR / 'project' / 'trash'
    trash_registry_path = trash_dir / 'trash-registry.json'
    
    # trash-registry.jsonが存在しない場合は終了
    if not trash_registry_path.exists():
        print("No trash-registry.json found, skipping cleanup.")
        return
    
    # projects-registry.jsonから保存期間を取得
    try:
        registry_data = load_projects_registry()
        retention_months = registry_data.get('retention_months', 13)
    except Exception as e:
        print(f"Failed to load retention_months, using default 13: {e}")
        retention_months = 13
    
    # 削除期限日時を計算
    expiry_date = datetime.now() - timedelta(days=retention_months * 30)
    
    # trash-registry.jsonを読み込み
    try:
        with open(trash_registry_path, 'r', encoding='utf-8') as f:
            trash_registry = json.load(f)
    except Exception as e:
        print(f"Failed to load trash-registry.json: {e}")
        return
    
    # 削除対象のプロジェクトを特定
    deleted_projects = trash_registry.get('deleted_projects', [])
    projects_to_keep = []
    projects_to_delete = []
    deleted_folder_names = []
    
    for project in deleted_projects:
        deletion_date_str = project.get('deletion_date')
        if not deletion_date_str:
            projects_to_keep.append(project)
            continue
        
        try:
            deletion_date = datetime.fromisoformat(deletion_date_str.replace('Z', '+00:00'))
            if deletion_date < expiry_date:
                projects_to_delete.append(project)
                deleted_folder_names.append(project.get('folder_name'))
            else:
                projects_to_keep.append(project)
        except Exception as e:
            print(f"Failed to parse deletion date for {project.get('folder_name')}: {e}")
            projects_to_keep.append(project)
    
    # 期限切れファイルを削除
    deleted_count = 0
    for project in projects_to_delete:
        archive_filename = project.get('archive_filename')
        if archive_filename:
            archive_path = trash_dir / archive_filename
            try:
                if archive_path.exists():
                    os.remove(archive_path)
                    deleted_count += 1
                    print(f"Deleted expired archive: {archive_filename}")
            except Exception as e:
                print(f"Failed to delete archive {archive_filename}: {e}")
    
    # trash-registry.jsonを更新
    if deleted_count > 0:
        trash_registry['deleted_projects'] = projects_to_keep
        trash_registry['last_updated'] = datetime.now().isoformat()
        
        try:
            with open(trash_registry_path, 'w', encoding='utf-8') as f:
                json.dump(trash_registry, f, ensure_ascii=False, indent=2)
            print(f"Updated trash-registry.json, removed {len(projects_to_delete)} entries")
        except Exception as e:
            print(f"Failed to update trash-registry.json: {e}")
    
    # projects-registry.jsonのarchived_projectsを更新
    if deleted_folder_names:
        try:
            registry_data = load_projects_registry()
            archived_projects = registry_data.get('archived_projects', [])
            
            # 削除されたフォルダ名を除外
            updated_archived = [
                p for p in archived_projects 
                if p.get('folder_name') not in deleted_folder_names
            ]
            
            if len(updated_archived) < len(archived_projects):
                registry_data['archived_projects'] = updated_archived
                registry_data['last_updated'] = datetime.now().isoformat()
                save_projects_registry(registry_data)
                print(f"Updated projects-registry.json, removed {len(archived_projects) - len(updated_archived)} archived entries")
        except Exception as e:
            print(f"Failed to update projects-registry.json: {e}")
    
    print(f"Archive cleanup completed. Deleted {deleted_count} expired archives.")