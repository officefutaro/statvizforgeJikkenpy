"""
プロジェクトレジストリとフォルダ構造の整合性確認・修正機能
"""
import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple

from config.paths import PROJECT_DATA_DIR
from .utils import load_projects_registry, save_projects_registry


def validate_and_fix_registry():
    """
    プロジェクトレジストリとフォルダ構造の整合性を確認し、必要に応じて修正する
    
    Returns:
        Tuple[bool, List[str]]: (修正が行われたかどうか, 修正ログ)
    """
    print("[Registry Validator] プロジェクトレジストリの整合性確認を開始...")
    
    modified = False
    log_messages = []
    
    try:
        # プロジェクトデータディレクトリの存在確認
        project_data_path = Path(PROJECT_DATA_DIR)
        if not project_data_path.exists():
            project_data_path.mkdir(parents=True, exist_ok=True)
            log_messages.append(f"プロジェクトデータディレクトリを作成: {PROJECT_DATA_DIR}")
            modified = True
        
        # レジストリファイルの読み込み
        try:
            registry_data = load_projects_registry()
        except Exception as e:
            log_messages.append(f"レジストリファイル読み込みエラー: {e}")
            registry_data = create_empty_registry()
            modified = True
        
        # 1. アクティブプロジェクトの整合性確認
        active_fixes = fix_active_projects(registry_data, project_data_path)
        if active_fixes[0]:
            modified = True
            log_messages.extend(active_fixes[1])
        
        # 2. アーカイブプロジェクトの整合性確認
        archive_fixes = fix_archived_projects(registry_data, project_data_path)
        if archive_fixes[0]:
            modified = True
            log_messages.extend(archive_fixes[1])
        
        # 3. 孤立フォルダの処理
        orphan_fixes = handle_orphaned_folders(registry_data, project_data_path)
        if orphan_fixes[0]:
            modified = True
            log_messages.extend(orphan_fixes[1])
        
        # 4. 重複IDの修正
        duplicate_fixes = fix_duplicate_ids(registry_data)
        if duplicate_fixes[0]:
            modified = True
            log_messages.extend(duplicate_fixes[1])
        
        # 修正があった場合はレジストリを保存
        if modified:
            registry_data['last_updated'] = datetime.now().isoformat()
            save_projects_registry(registry_data)
            log_messages.append("レジストリファイルを更新しました")
        
        if log_messages:
            print("[Registry Validator] 整合性確認完了:")
            for msg in log_messages:
                print(f"  - {msg}")
        else:
            print("[Registry Validator] レジストリは正常です")
        
        return modified, log_messages
        
    except Exception as e:
        error_msg = f"整合性確認中にエラーが発生: {e}"
        print(f"[Registry Validator] {error_msg}")
        return False, [error_msg]


def create_empty_registry() -> Dict[str, Any]:
    """空のレジストリ構造を作成"""
    return {
        "version": "1.0.0",
        "last_updated": datetime.now().isoformat(),
        "retention_months": 13,
        "projects": [],
        "archived_projects": [],
        "reserved_folders": [
            "node_modules", "dist", "build", ".git", 
            "backend", "frontend", "trash", "recycle_bin", 
            "deleted", ".trash"
        ]
    }


def fix_active_projects(registry_data: Dict[str, Any], project_data_path: Path) -> Tuple[bool, List[str]]:
    """アクティブプロジェクトの整合性を修正"""
    modified = False
    log_messages = []
    projects_to_remove = []
    projects_to_archive = []
    
    for i, project in enumerate(registry_data.get('projects', [])):
        folder_name = project.get('folder_name')
        project_id = project.get('id')
        
        if not folder_name or not project_id:
            projects_to_remove.append(i)
            log_messages.append(f"不完全なプロジェクトデータを削除: {project}")
            continue
        
        project_folder = project_data_path / folder_name
        
        # フォルダが存在しない場合
        if not project_folder.exists():
            # アーカイブに移動
            archive_project = dict(project)
            archive_project.update({
                'archive_filename': f"{folder_name}_auto_archived.zip",
                'archive_path': str(project_data_path / 'trash' / f"{folder_name}_auto_archived.zip"),
                'archive_size': 0,
                'deletion_date': datetime.now().isoformat(),
                'reason': 'フォルダが存在しないため自動アーカイブ'
            })
            projects_to_archive.append(archive_project)
            projects_to_remove.append(i)
            log_messages.append(f"存在しないフォルダのプロジェクトをアーカイブ: {folder_name}")
            continue
        
        # 必要なサブフォルダの確認・作成
        required_subfolders = ['raw', 'analysisdata', 'db', 'git']
        for subfolder in required_subfolders:
            subfolder_path = project_folder / subfolder
            if not subfolder_path.exists():
                subfolder_path.mkdir(parents=True, exist_ok=True)
                log_messages.append(f"サブフォルダを作成: {folder_name}/{subfolder}")
                modified = True
        
        # project.jsonの確認・作成
        project_json_path = project_folder / 'project.json'
        if not project_json_path.exists():
            create_project_json(project_json_path, project)
            log_messages.append(f"project.jsonを作成: {folder_name}")
            modified = True
    
    # プロジェクトの削除（逆順で削除してインデックスがずれないようにする）
    for i in reversed(projects_to_remove):
        del registry_data['projects'][i]
        modified = True
    
    # アーカイブプロジェクトの追加
    if 'archived_projects' not in registry_data:
        registry_data['archived_projects'] = []
    registry_data['archived_projects'].extend(projects_to_archive)
    
    if projects_to_remove or projects_to_archive:
        modified = True
    
    return modified, log_messages


def fix_archived_projects(registry_data: Dict[str, Any], project_data_path: Path) -> Tuple[bool, List[str]]:
    """アーカイブプロジェクトの整合性を修正"""
    modified = False
    log_messages = []
    
    trash_path = project_data_path / 'trash'
    if not trash_path.exists():
        trash_path.mkdir(parents=True, exist_ok=True)
        log_messages.append("trashフォルダを作成")
        modified = True
    
    archived_projects_to_remove = []
    
    for i, archived_project in enumerate(registry_data.get('archived_projects', [])):
        archive_filename = archived_project.get('archive_filename')
        archive_path = archived_project.get('archive_path')
        
        if archive_filename and archive_path:
            archive_file_path = Path(archive_path)
            if not archive_file_path.exists():
                # アーカイブファイルが存在しない場合は記録から削除
                archived_projects_to_remove.append(i)
                log_messages.append(f"存在しないアーカイブファイルの記録を削除: {archive_filename}")
    
    # アーカイブプロジェクトの削除（逆順で削除）
    for i in reversed(archived_projects_to_remove):
        del registry_data['archived_projects'][i]
        modified = True
    
    return modified, log_messages


def handle_orphaned_folders(registry_data: Dict[str, Any], project_data_path: Path) -> Tuple[bool, List[str]]:
    """孤立フォルダ（レジストリにないフォルダ）の処理"""
    modified = False
    log_messages = []
    
    if not project_data_path.exists():
        return modified, log_messages
    
    # レジストリ内のフォルダ名を収集
    registered_folders = set()
    for project in registry_data.get('projects', []):
        if project.get('folder_name'):
            registered_folders.add(project['folder_name'])
    
    # 予約フォルダ
    reserved_folders = set(registry_data.get('reserved_folders', []))
    
    # 実際のフォルダを確認
    for item in project_data_path.iterdir():
        if not item.is_dir():
            continue
        
        folder_name = item.name
        
        # 隠しフォルダや予約フォルダは無視
        if folder_name.startswith('.') or folder_name in reserved_folders:
            continue
        
        # レジストリに登録されていない孤立フォルダ
        if folder_name not in registered_folders:
            # project.jsonがある場合は復元を試みる
            project_json_path = item / 'project.json'
            if project_json_path.exists() and project_json_path.is_file():
                try:
                    restored_project = restore_project_from_folder(item, folder_name)
                    if restored_project:
                        registry_data['projects'].append(restored_project)
                        log_messages.append(f"孤立フォルダからプロジェクトを復元: {folder_name}")
                        modified = True
                        continue
                except Exception as e:
                    log_messages.append(f"フォルダ復元エラー {folder_name}: {e}")
            
            # 復元できない場合はアーカイブ
            try:
                archive_orphaned_folder(item, project_data_path, folder_name)
                log_messages.append(f"孤立フォルダをアーカイブ: {folder_name}")
                modified = True
            except Exception as e:
                log_messages.append(f"孤立フォルダアーカイブエラー {folder_name}: {e}")
    
    return modified, log_messages


def fix_duplicate_ids(registry_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """重複IDの修正"""
    modified = False
    log_messages = []
    
    seen_ids = set()
    projects_to_fix = []
    
    for i, project in enumerate(registry_data.get('projects', [])):
        project_id = project.get('id')
        if not project_id:
            projects_to_fix.append(i)
        elif project_id in seen_ids:
            projects_to_fix.append(i)
            log_messages.append(f"重複ID検出: {project_id} (プロジェクト: {project.get('project_name', 'Unknown')})")
        else:
            seen_ids.add(project_id)
    
    # 重複IDまたは欠損IDを修正
    for i in projects_to_fix:
        import uuid
        new_id = str(uuid.uuid4())
        old_id = registry_data['projects'][i].get('id', 'None')
        registry_data['projects'][i]['id'] = new_id
        log_messages.append(f"ID修正: {old_id} -> {new_id}")
        modified = True
    
    return modified, log_messages


def restore_project_from_folder(folder_path: Path, folder_name: str) -> Dict[str, Any]:
    """フォルダからプロジェクト情報を復元"""
    project_json_path = folder_path / 'project.json'
    
    try:
        with open(project_json_path, 'r', encoding='utf-8') as f:
            project_data = json.load(f)
        
        # 必要なフィールドの確認・補完
        import uuid
        restored_project = {
            'id': project_data.get('id', str(uuid.uuid4())),
            'folder_name': folder_name,
            'project_name': project_data.get('project_name', folder_name),
            'description': project_data.get('description', '復元されたプロジェクト'),
            'tags': project_data.get('tags', []),
            'status': 'active',
            'created_date': project_data.get('created_date', datetime.now().isoformat()),
            'modified_date': datetime.now().isoformat()
        }
        
        return restored_project
        
    except Exception as e:
        print(f"プロジェクト復元エラー {folder_name}: {e}")
        return None


def archive_orphaned_folder(folder_path: Path, project_data_path: Path, folder_name: str):
    """孤立フォルダをアーカイブ"""
    import zipfile
    
    trash_path = project_data_path / 'trash'
    trash_path.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_filename = f"{folder_name}_orphaned_{timestamp}.zip"
    archive_path = trash_path / archive_filename
    
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in folder_path.rglob('*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(folder_path)
                zipf.write(file_path, relative_path)
    
    # 元のフォルダを削除
    shutil.rmtree(folder_path)


def create_project_json(project_json_path: Path, project_data: Dict[str, Any]):
    """project.jsonファイルを作成"""
    project_json_content = {
        'id': project_data.get('id'),
        'project_name': project_data.get('project_name'),
        'description': project_data.get('description', ''),
        'tags': project_data.get('tags', []),
        'created_date': project_data.get('created_date'),
        'modified_date': project_data.get('modified_date'),
        'version': '1.0'
    }
    
    with open(project_json_path, 'w', encoding='utf-8') as f:
        json.dump(project_json_content, f, ensure_ascii=False, indent=2)