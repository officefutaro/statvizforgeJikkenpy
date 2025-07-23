import os
import json
from pathlib import Path
from django.conf import settings


def get_projects_registry_path():
    """projects-registry.jsonのパスを取得"""
    # プロジェクトルートディレクトリを取得
    project_root = Path(settings.BASE_DIR).parent.parent
    return project_root / 'project' / 'projects-registry.json'


def load_projects_registry():
    """projects-registry.jsonを読み込む"""
    registry_path = get_projects_registry_path()
    
    if not registry_path.exists():
        # ファイルが存在しない場合は初期データを作成
        initial_data = {
            "version": "1.0.0",
            "last_updated": "",
            "projects": []
        }
        save_projects_registry(initial_data)
        return initial_data
    
    with open(registry_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_projects_registry(data):
    """projects-registry.jsonに保存"""
    registry_path = get_projects_registry_path()
    
    # ディレクトリが存在しない場合は作成
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def update_projects_registry(projects):
    """プロジェクト一覧を更新"""
    from datetime import datetime
    
    data = load_projects_registry()
    data['projects'] = projects
    data['last_updated'] = datetime.now().isoformat()
    save_projects_registry(data)
    return data