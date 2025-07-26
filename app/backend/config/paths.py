"""
プロジェクト全体で使用するパス定義
"""
from pathlib import Path

# プロジェクトルート
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
BASE_DIR = PROJECT_ROOT  # BASE_DIRエイリアスを追加

# 各ディレクトリ
APP_DIR = PROJECT_ROOT / 'app'
BACKEND_DIR = APP_DIR / 'backend'
FRONTEND_DIR = APP_DIR / 'frontend'
PROJECT_DATA_DIR = PROJECT_ROOT / 'project'
DOC_DIR = PROJECT_ROOT / 'doc'
LIB_DIR = PROJECT_ROOT / 'lib'

# 重要なファイル
PROJECTS_REGISTRY_FILE = PROJECT_DATA_DIR / 'projects-registry.json'
API_HISTORY_FILE = BACKEND_DIR / 'apihistory.md'