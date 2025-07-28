#!/bin/bash

# JupyterLab専用仮想環境セットアップスクリプト
# StatVizForge - JupyterLab Service Environment

set -e

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
JUPYTER_ENV_DIR="$PROJECT_ROOT/jupyter_env"
JUPYTER_SERVICE_DIR="$PROJECT_ROOT/jupyter_service"

echo "🔬 JupyterLab専用仮想環境をセットアップ中..."

# 1. JupyterLab専用仮想環境を作成
if [ ! -d "$JUPYTER_ENV_DIR" ]; then
    echo "📦 Python仮想環境を作成中..."
    python3 -m venv "$JUPYTER_ENV_DIR"
fi

# 2. 仮想環境をアクティベート
source "$JUPYTER_ENV_DIR/bin/activate"

# 3. JupyterLab + データサイエンス関連パッケージをインストール
echo "📚 JupyterLabとデータサイエンスパッケージをインストール中..."
pip install --upgrade pip

# JupyterLab core
pip install jupyterlab==4.2.5
pip install jupyter-server==2.14.2

# データサイエンス必須パッケージ
pip install numpy==1.26.4
pip install pandas==2.2.2
pip install matplotlib==3.9.2
pip install seaborn==0.13.2
pip install plotly==5.24.1
pip install scipy==1.14.1
pip install scikit-learn==1.5.1

# 統計・可視化追加パッケージ
pip install statsmodels==0.14.2
pip install altair==5.4.1
pip install bokeh==3.4.1

# JupyterLab拡張機能
pip install jupyterlab-git==0.50.1
pip install jupyterlab-variableinspector==3.2.1

# API通信用
pip install requests==2.32.3
pip install httpx==0.27.2

# 4. JupyterLabサービス管理ディレクトリを作成
mkdir -p "$JUPYTER_SERVICE_DIR"
mkdir -p "$JUPYTER_SERVICE_DIR/config"
mkdir -p "$JUPYTER_SERVICE_DIR/logs"
mkdir -p "$JUPYTER_SERVICE_DIR/temp"

# 5. JupyterLab設定ファイルを生成
cat > "$JUPYTER_SERVICE_DIR/config/jupyter_lab_config.py" << 'EOF'
# JupyterLab Configuration for StatVizForge
c = get_config()

# Server configuration
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.open_browser = False
c.ServerApp.allow_remote_access = True
c.ServerApp.allow_root = True

# Security settings
c.ServerApp.token = ''  # Will be set dynamically
c.ServerApp.password = ''  # Will be set dynamically
c.ServerApp.disable_check_xsrf = False

# File access restrictions
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_credentials = True

# Logging
c.Application.log_level = 'INFO'

# Extensions
c.ServerApp.jpserver_extensions = {
    'jupyterlab': True,
    'jupyterlab_git': True,
}
EOF

# 6. JupyterLabサービス管理スクリプト
cat > "$JUPYTER_SERVICE_DIR/jupyter_manager.py" << 'EOF'
#!/usr/bin/env python3
"""
JupyterLab Service Manager for StatVizForge
独立したJupyterLabインスタンス管理
"""

import os
import sys
import json
import socket
import subprocess
import time
import uuid
import logging
from pathlib import Path
from typing import Dict, Optional, Tuple

# 設定
JUPYTER_ENV_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.join(SERVICE_DIR, 'config')
LOGS_DIR = os.path.join(SERVICE_DIR, 'logs')
TEMP_DIR = os.path.join(SERVICE_DIR, 'temp')

# ログ設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOGS_DIR, 'jupyter_manager.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class JupyterLabManager:
    """JupyterLabインスタンス管理クラス"""
    
    def __init__(self):
        self.instances_file = os.path.join(TEMP_DIR, 'jupyter_instances.json')
        self.jupyter_executable = os.path.join(JUPYTER_ENV_PATH, 'bin', 'jupyter-lab')
        
    def find_free_port(self, start_port: int = 8888) -> Optional[int]:
        """利用可能なポートを探す"""
        for port in range(start_port, start_port + 100):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                if s.connect_ex(('localhost', port)) != 0:
                    return port
        return None
    
    def generate_token(self) -> str:
        """セキュリティトークンを生成"""
        return str(uuid.uuid4()).replace('-', '')
    
    def start_instance(self, project_folder: str, working_dir: str) -> Tuple[Optional[Dict], Optional[str]]:
        """JupyterLabインスタンスを起動"""
        try:
            port = self.find_free_port()
            if not port:
                return None, "No available port found"
            
            token = self.generate_token()
            
            # JupyterLab起動コマンド
            cmd = [
                self.jupyter_executable,
                '--config', os.path.join(CONFIG_DIR, 'jupyter_lab_config.py'),
                '--port', str(port),
                '--notebook-dir', working_dir,
                f'--ServerApp.token={token}',
                '--ServerApp.base_url=/',
                f'--Application.log_level=INFO'
            ]
            
            # ログファイル
            log_file = os.path.join(LOGS_DIR, f'jupyter_{project_folder}_{port}.log')
            
            with open(log_file, 'w') as log:
                process = subprocess.Popen(
                    cmd,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    cwd=working_dir,
                    env=dict(os.environ, PYTHONPATH=working_dir)
                )
            
            # 起動確認
            time.sleep(3)
            if process.poll() is not None:
                return None, f"JupyterLab failed to start. Check log: {log_file}"
            
            instance_info = {
                'project_folder': project_folder,
                'port': port,
                'pid': process.pid,
                'token': token,
                'url': f'http://localhost:{port}/?token={token}',
                'working_dir': working_dir,
                'log_file': log_file,
                'started_at': time.time()
            }
            
            # インスタンス情報を保存
            self._save_instance(project_folder, instance_info)
            
            logger.info(f"JupyterLab started for {project_folder} on port {port}")
            return instance_info, None
            
        except Exception as e:
            logger.error(f"Failed to start JupyterLab: {e}")
            return None, str(e)
    
    def stop_instance(self, project_folder: str) -> Tuple[bool, Optional[str]]:
        """JupyterLabインスタンスを停止"""
        try:
            instances = self._load_instances()
            if project_folder not in instances:
                return False, "Instance not found"
            
            instance = instances[project_folder]
            pid = instance['pid']
            
            # プロセスを終了
            try:
                os.kill(pid, 15)  # SIGTERM
                time.sleep(2)
                os.kill(pid, 9)  # SIGKILL if still running
            except ProcessLookupError:
                pass  # プロセスは既に終了している
            
            # インスタンス情報を削除
            del instances[project_folder]
            self._save_instances(instances)
            
            logger.info(f"JupyterLab stopped for {project_folder}")
            return True, None
            
        except Exception as e:
            logger.error(f"Failed to stop JupyterLab: {e}")
            return False, str(e)
    
    def get_instance_status(self, project_folder: str) -> Optional[Dict]:
        """インスタンスの状態を取得"""
        instances = self._load_instances()
        if project_folder not in instances:
            return None
        
        instance = instances[project_folder]
        pid = instance['pid']
        
        # プロセスが生きているかチェック
        try:
            os.kill(pid, 0)  # プロセス存在チェック
            instance['status'] = 'running'
        except ProcessLookupError:
            instance['status'] = 'stopped'
            # 死んだインスタンスを削除
            del instances[project_folder]
            self._save_instances(instances)
            return None
        
        return instance
    
    def list_instances(self) -> Dict:
        """全インスタンスのリストを取得"""
        instances = self._load_instances()
        active_instances = {}
        
        for project_folder, instance in list(instances.items()):
            status = self.get_instance_status(project_folder)
            if status:
                active_instances[project_folder] = status
        
        return active_instances
    
    def _load_instances(self) -> Dict:
        """インスタンス情報をファイルから読み込み"""
        if not os.path.exists(self.instances_file):
            return {}
        
        try:
            with open(self.instances_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    
    def _save_instances(self, instances: Dict):
        """インスタンス情報をファイルに保存"""
        try:
            with open(self.instances_file, 'w') as f:
                json.dump(instances, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save instances: {e}")
    
    def _save_instance(self, project_folder: str, instance_info: Dict):
        """単一インスタンス情報を保存"""
        instances = self._load_instances()
        instances[project_folder] = instance_info
        self._save_instances(instances)

def main():
    """コマンドライン実行用メイン関数"""
    if len(sys.argv) < 2:
        print("Usage: python jupyter_manager.py <command> [args...]")
        print("Commands: start <project_folder> <working_dir>, stop <project_folder>, status [project_folder], list")
        sys.exit(1)
    
    manager = JupyterLabManager()
    command = sys.argv[1]
    
    if command == 'start':
        if len(sys.argv) != 4:
            print("Usage: python jupyter_manager.py start <project_folder> <working_dir>")
            sys.exit(1)
        
        project_folder = sys.argv[2]
        working_dir = sys.argv[3]
        
        instance, error = manager.start_instance(project_folder, working_dir)
        if instance:
            print(json.dumps(instance, indent=2))
        else:
            print(f"Error: {error}", file=sys.stderr)
            sys.exit(1)
    
    elif command == 'stop':
        if len(sys.argv) != 3:
            print("Usage: python jupyter_manager.py stop <project_folder>")
            sys.exit(1)
        
        project_folder = sys.argv[2]
        success, error = manager.stop_instance(project_folder)
        if success:
            print(f"Stopped JupyterLab for {project_folder}")
        else:
            print(f"Error: {error}", file=sys.stderr)
            sys.exit(1)
    
    elif command == 'status':
        if len(sys.argv) == 3:
            project_folder = sys.argv[2]
            status = manager.get_instance_status(project_folder)
            if status:
                print(json.dumps(status, indent=2))
            else:
                print(f"No running instance for {project_folder}")
        else:
            print("Usage: python jupyter_manager.py status <project_folder>")
            sys.exit(1)
    
    elif command == 'list':
        instances = manager.list_instances()
        print(json.dumps(instances, indent=2))
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
EOF

chmod +x "$JUPYTER_SERVICE_DIR/jupyter_manager.py"

# 7. 完了メッセージ
echo "✅ JupyterLab専用環境のセットアップが完了しました！"
echo ""
echo "📁 環境パス:"
echo "   仮想環境: $JUPYTER_ENV_DIR"
echo "   サービス: $JUPYTER_SERVICE_DIR"
echo ""
echo "🚀 使用方法:"
echo "   起動: cd $JUPYTER_SERVICE_DIR && python jupyter_manager.py start <project_folder> <working_dir>"
echo "   停止: cd $JUPYTER_SERVICE_DIR && python jupyter_manager.py stop <project_folder>"
echo "   状態: cd $JUPYTER_SERVICE_DIR && python jupyter_manager.py status <project_folder>"
echo "   一覧: cd $JUPYTER_SERVICE_DIR && python jupyter_manager.py list"
echo ""
echo "⚙️  次のステップ:"
echo "   1. バックエンドAPIをJupyterServiceに接続"
echo "   2. セキュリティ設定の強化"
echo "   3. リソース制限の実装"