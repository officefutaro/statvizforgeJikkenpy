"""
プロジェクトフォルダの analysisdata と raw を git フォルダに同期する機能
"""
import os
import shutil
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class GitSyncError(Exception):
    """Git同期のエラー"""
    pass

class GitSyncUtils:
    """プロジェクトフォルダのGit同期ユーティリティ"""
    
    def __init__(self, project_folder: str):
        """
        Args:
            project_folder: プロジェクトフォルダ名
        """
        self.project_folder = project_folder
        self.project_path = Path(settings.PROJECTS_ROOT) / project_folder
        self.git_path = self.project_path / 'git'
        self.analysisdata_path = self.project_path / 'analysisdata'
        self.raw_path = self.project_path / 'raw'
        
        if not self.project_path.exists():
            raise GitSyncError(f"Project folder not found: {project_folder}")
    
    def get_sync_status(self) -> Dict[str, any]:
        """同期状態を取得"""
        try:
            # フォルダの存在確認
            folders_status = {
                'project_exists': self.project_path.exists(),
                'analysisdata_exists': self.analysisdata_path.exists(),
                'raw_exists': self.raw_path.exists(),
                'git_exists': self.git_path.exists(),
            }
            
            # Git フォルダが存在する場合、同期状態をチェック
            sync_needed = False
            changes = []
            
            if folders_status['git_exists']:
                changes = self._detect_changes()
                sync_needed = len(changes) > 0
            
            # フォルダサイズ情報
            sizes = {}
            for folder_name, path in [
                ('analysisdata', self.analysisdata_path),
                ('raw', self.raw_path),
                ('git', self.git_path)
            ]:
                if path.exists():
                    sizes[folder_name] = self._get_folder_size(path)
                else:
                    sizes[folder_name] = 0
            
            return {
                'project_folder': self.project_folder,
                'folders': folders_status,
                'sync_needed': sync_needed,
                'changes': changes,
                'sizes': sizes,
                'last_sync': self._get_last_sync_time()
            }
            
        except Exception as e:
            logger.error(f"Failed to get sync status for {self.project_folder}: {e}")
            raise GitSyncError(f"Failed to get sync status: {str(e)}")
    
    def sync_to_git_folder(self) -> Dict[str, any]:
        """analysisdata と raw フォルダを git フォルダに同期"""
        try:
            # Git フォルダを作成（存在しない場合）
            self.git_path.mkdir(exist_ok=True)
            
            sync_results = {
                'analysisdata': None,
                'raw': None,
                'total_files': 0,
                'total_size': 0
            }
            
            # analysisdata フォルダを同期
            if self.analysisdata_path.exists():
                result = self._sync_folder('analysisdata', self.analysisdata_path, self.git_path / 'analysisdata')
                sync_results['analysisdata'] = result
                sync_results['total_files'] += result['files_count']
                sync_results['total_size'] += result['size']
            
            # raw フォルダを同期
            if self.raw_path.exists():
                result = self._sync_folder('raw', self.raw_path, self.git_path / 'raw')
                sync_results['raw'] = result
                sync_results['total_files'] += result['files_count']
                sync_results['total_size'] += result['size']
            
            # 同期時刻を記録
            self._save_sync_metadata(sync_results)
            
            return {
                'success': True,
                'message': f'Synchronized {sync_results["total_files"]} files to git folder',
                'project_folder': self.project_folder,
                'results': sync_results,
                'sync_time': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Failed to sync {self.project_folder} to git folder: {e}")
            raise GitSyncError(f"Failed to sync to git folder: {str(e)}")
    
    def _sync_folder(self, folder_name: str, source_path: Path, dest_path: Path) -> Dict[str, any]:
        """単一フォルダの同期"""
        try:
            # 対象フォルダを削除して再作成（完全同期）
            if dest_path.exists():
                shutil.rmtree(dest_path)
            
            # フォルダをコピー
            shutil.copytree(source_path, dest_path)
            
            # 統計情報を取得
            files_count = sum(1 for _ in dest_path.rglob('*') if _.is_file())
            folder_size = self._get_folder_size(dest_path)
            
            return {
                'folder': folder_name,
                'files_count': files_count,
                'size': folder_size,
                'success': True
            }
            
        except Exception as e:
            logger.error(f"Failed to sync folder {folder_name}: {e}")
            return {
                'folder': folder_name,
                'files_count': 0,
                'size': 0,
                'success': False,
                'error': str(e)
            }
    
    def _detect_changes(self) -> List[Dict[str, any]]:
        """変更点を検出"""
        changes = []
        
        try:
            # analysisdata の変更をチェック
            if self.analysisdata_path.exists():
                changes.extend(self._compare_folders('analysisdata', 
                                                   self.analysisdata_path, 
                                                   self.git_path / 'analysisdata'))
            
            # raw の変更をチェック  
            if self.raw_path.exists():
                changes.extend(self._compare_folders('raw',
                                                   self.raw_path,
                                                   self.git_path / 'raw'))
                
        except Exception as e:
            logger.error(f"Failed to detect changes: {e}")
        
        return changes
    
    def _compare_folders(self, folder_name: str, source_path: Path, dest_path: Path) -> List[Dict[str, any]]:
        """フォルダ間の差分を比較"""
        changes = []
        
        if not dest_path.exists():
            changes.append({
                'type': 'folder_missing',
                'folder': folder_name,
                'message': f'{folder_name} folder not synced yet'
            })
            return changes
        
        try:
            # ファイル一覧を取得
            source_files = {f.relative_to(source_path): f for f in source_path.rglob('*') if f.is_file()}
            dest_files = {f.relative_to(dest_path): f for f in dest_path.rglob('*') if f.is_file()}
            
            # 新規・変更ファイルをチェック
            for rel_path, source_file in source_files.items():
                if rel_path not in dest_files:
                    changes.append({
                        'type': 'new_file',
                        'folder': folder_name,
                        'file': str(rel_path),
                        'message': f'New file: {rel_path}'
                    })
                else:
                    dest_file = dest_files[rel_path]
                    # ファイルサイズと更新時刻で変更を検出
                    if (source_file.stat().st_size != dest_file.stat().st_size or
                        source_file.stat().st_mtime > dest_file.stat().st_mtime):
                        changes.append({
                            'type': 'modified_file',
                            'folder': folder_name,
                            'file': str(rel_path),
                            'message': f'Modified file: {rel_path}'
                        })
            
            # 削除されたファイルをチェック
            for rel_path in dest_files.keys():
                if rel_path not in source_files:
                    changes.append({
                        'type': 'deleted_file',
                        'folder': folder_name,
                        'file': str(rel_path),
                        'message': f'Deleted file: {rel_path}'
                    })
                    
        except Exception as e:
            logger.error(f"Failed to compare folders {folder_name}: {e}")
            changes.append({
                'type': 'error',
                'folder': folder_name,
                'message': f'Error comparing folders: {str(e)}'
            })
        
        return changes
    
    def _get_folder_size(self, path: Path) -> int:
        """フォルダサイズを取得（バイト）"""
        try:
            return sum(f.stat().st_size for f in path.rglob('*') if f.is_file())
        except Exception as e:
            logger.error(f"Failed to get folder size for {path}: {e}")
            return 0
    
    def _save_sync_metadata(self, sync_results: Dict[str, any]):
        """同期メタデータを保存"""
        try:
            metadata = {
                'last_sync': datetime.now().isoformat(),
                'sync_results': sync_results,
                'project_folder': self.project_folder
            }
            
            metadata_file = self.git_path / '.sync_metadata.json'
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            logger.error(f"Failed to save sync metadata: {e}")
    
    def _get_last_sync_time(self) -> Optional[str]:
        """最後の同期時刻を取得"""
        try:
            metadata_file = self.git_path / '.sync_metadata.json'
            if metadata_file.exists():
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = json.load(f)
                    return metadata.get('last_sync')
        except Exception as e:
            logger.error(f"Failed to get last sync time: {e}")
        
        return None
    
    def initialize_git_folder(self) -> Dict[str, any]:
        """Git フォルダを初期化"""
        try:
            # Git フォルダが既に存在するかチェック
            if self.git_path.exists() and any(self.git_path.iterdir()):
                return {
                    'success': False,
                    'message': 'Git folder already exists and is not empty',
                    'already_exists': True
                }
            
            # Git フォルダを作成
            self.git_path.mkdir(exist_ok=True)
            
            # 初回同期を実行
            sync_result = self.sync_to_git_folder()
            
            return {
                'success': True,
                'message': 'Git folder initialized and synced successfully',
                'project_folder': self.project_folder,
                'git_path': str(self.git_path),
                'sync_result': sync_result
            }
            
        except Exception as e:
            logger.error(f"Failed to initialize git folder for {self.project_folder}: {e}")
            raise GitSyncError(f"Failed to initialize git folder: {str(e)}")
    
    def get_git_folder_info(self) -> Dict[str, any]:
        """Git フォルダの詳細情報を取得"""
        try:
            if not self.git_path.exists():
                return {
                    'exists': False,
                    'message': 'Git folder does not exist'
                }
            
            # フォルダ構造を取得
            structure = {
                'analysisdata': self._get_folder_structure(self.git_path / 'analysisdata'),
                'raw': self._get_folder_structure(self.git_path / 'raw')
            }
            
            # 統計情報
            total_files = sum(len(info['files']) for info in structure.values() if info['exists'])
            total_size = sum(info['size'] for info in structure.values() if info['exists'])
            
            return {
                'exists': True,
                'project_folder': self.project_folder,
                'git_path': str(self.git_path),
                'structure': structure,
                'total_files': total_files,
                'total_size': total_size,
                'last_sync': self._get_last_sync_time()
            }
            
        except Exception as e:
            logger.error(f"Failed to get git folder info: {e}")
            raise GitSyncError(f"Failed to get git folder info: {str(e)}")
    
    def _get_folder_structure(self, path: Path) -> Dict[str, any]:
        """フォルダ構造を取得"""
        if not path.exists():
            return {
                'exists': False,
                'files': [],
                'size': 0
            }
        
        try:
            files = []
            for file_path in path.rglob('*'):
                if file_path.is_file():
                    relative_path = file_path.relative_to(path)
                    files.append({
                        'path': str(relative_path),
                        'size': file_path.stat().st_size,
                        'modified': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                    })
            
            return {
                'exists': True,
                'files': files,
                'file_count': len(files),
                'size': sum(f['size'] for f in files)
            }
            
        except Exception as e:
            logger.error(f"Failed to get folder structure for {path}: {e}")
            return {
                'exists': True,
                'files': [],
                'file_count': 0,
                'size': 0,
                'error': str(e)
            }

def get_git_sync_utils(project_folder: str) -> GitSyncUtils:
    """GitSyncUtilsインスタンスを取得"""
    return GitSyncUtils(project_folder)