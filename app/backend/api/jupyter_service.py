"""
JupyterLab Service Interface
バックエンドAPIとJupyterLabサービス間の橋渡し
"""

import os
import subprocess
import json
import logging
from typing import Dict, Optional, Tuple
from django.conf import settings

logger = logging.getLogger(__name__)

class JupyterLabService:
    """JupyterLabサービスとの通信を管理するクラス"""
    
    def __init__(self):
        # JupyterLabサービスのパス
        project_root = os.path.join(settings.BASE_DIR, '../..')
        self.jupyter_service_dir = os.path.join(project_root, 'jupyter_service')
        self.jupyter_manager_script = os.path.join(self.jupyter_service_dir, 'jupyter_manager.py')
        
        # JupyterLab専用仮想環境のPython
        self.jupyter_python = os.path.join(project_root, 'jupyter_env', 'bin', 'python')
        
        # サービスが存在するかチェック
        if not os.path.exists(self.jupyter_manager_script):
            logger.error(f"JupyterLab manager script not found: {self.jupyter_manager_script}")
            logger.error("Please run jupyter_env_setup.sh to setup JupyterLab service")
    
    def _run_jupyter_command(self, command: list) -> Tuple[bool, Optional[Dict], Optional[str]]:
        """JupyterLabマネージャーコマンドを実行"""
        try:
            cmd = [self.jupyter_python, self.jupyter_manager_script] + command
            
            logger.info(f"Executing JupyterLab command: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.jupyter_service_dir,
                timeout=30
            )
            
            if result.returncode == 0:
                # 成功した場合、JSONレスポンスを解析
                try:
                    response_data = json.loads(result.stdout) if result.stdout.strip() else None
                    return True, response_data, None
                except json.JSONDecodeError:
                    # JSON以外のレスポンス（例：停止成功メッセージ）
                    return True, {'message': result.stdout.strip()}, None
            else:
                # エラーが発生した場合
                error_msg = result.stderr.strip() or result.stdout.strip()
                logger.error(f"JupyterLab command failed: {error_msg}")
                return False, None, error_msg
                
        except subprocess.TimeoutExpired:
            error_msg = "JupyterLab command timed out"
            logger.error(error_msg)
            return False, None, error_msg
        except Exception as e:
            error_msg = f"Failed to execute JupyterLab command: {str(e)}"
            logger.error(error_msg)
            return False, None, error_msg
    
    def start_jupyter_lab(self, project_folder: str, working_dir: str) -> Tuple[Optional[Dict], Optional[str]]:
        """JupyterLabインスタンスを起動"""
        
        # working_dirの存在確認
        if not os.path.exists(working_dir):
            return None, f"Working directory does not exist: {working_dir}"
        
        success, data, error = self._run_jupyter_command(['start', project_folder, working_dir])
        
        if success and data:
            logger.info(f"JupyterLab started successfully for project: {project_folder}")
            return data, None
        else:
            logger.error(f"Failed to start JupyterLab for project: {project_folder}, error: {error}")
            return None, error
    
    def stop_jupyter_lab(self, project_folder: str) -> Tuple[bool, Optional[str]]:
        """JupyterLabインスタンスを停止"""
        success, data, error = self._run_jupyter_command(['stop', project_folder])
        
        if success:
            logger.info(f"JupyterLab stopped successfully for project: {project_folder}")
            return True, None
        else:
            logger.error(f"Failed to stop JupyterLab for project: {project_folder}, error: {error}")
            return False, error
    
    def get_jupyter_status(self, project_folder: str) -> Tuple[Optional[Dict], Optional[str]]:
        """JupyterLabインスタンスの状態を取得"""
        success, data, error = self._run_jupyter_command(['status', project_folder])
        
        if success:
            return data, None
        else:
            # statusコマンドでは、インスタンスが存在しない場合もエラーとして扱われる
            # この場合は正常な状態として None を返す
            if "No running instance" in (error or ""):
                return None, None
            return None, error
    
    def list_jupyter_instances(self) -> Tuple[Optional[Dict], Optional[str]]:
        """全JupyterLabインスタンスの一覧を取得"""
        success, data, error = self._run_jupyter_command(['list'])
        
        if success:
            return data or {}, None
        else:
            return None, error
    
    def is_service_available(self) -> bool:
        """JupyterLabサービスが利用可能かチェック"""
        return (
            os.path.exists(self.jupyter_manager_script) and
            os.path.exists(self.jupyter_python)
        )
    
    def get_service_info(self) -> Dict:
        """JupyterLabサービスの情報を取得"""
        return {
            'service_available': self.is_service_available(),
            'jupyter_service_dir': self.jupyter_service_dir,
            'jupyter_manager_script': self.jupyter_manager_script,
            'jupyter_python': self.jupyter_python,
            'manager_script_exists': os.path.exists(self.jupyter_manager_script),
            'python_executable_exists': os.path.exists(self.jupyter_python)
        }


# グローバルインスタンス
jupyter_service = JupyterLabService()