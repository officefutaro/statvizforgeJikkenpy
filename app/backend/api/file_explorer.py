import os
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

class FileExplorer:
    """プロジェクトのファイル/ディレクトリ構造を管理するクラス"""
    
    def __init__(self):
        self.projects_root = Path(settings.BASE_DIR).parent.parent / 'project'
    
    def get_directory_structure(self, project_folder: str, path: str = '') -> Dict:
        """
        指定されたプロジェクトのディレクトリ構造を取得
        
        Args:
            project_folder: プロジェクトのフォルダ名
            path: プロジェクト内の相対パス（空の場合はrawフォルダをルート）
        
        Returns:
            ディレクトリ構造の辞書
        """
        project_path = self.projects_root / project_folder
        if not project_path.exists():
            return {'error': 'Project not found'}
        
        # デフォルトでrawフォルダをルートとして使用
        if not path:
            raw_path = project_path / 'raw'
            if raw_path.exists():
                target_path = raw_path
                base_path = raw_path  # rawフォルダを基準にする
            else:
                target_path = project_path
                base_path = project_path
        else:
            # パスが指定されている場合は、rawフォルダ内のパス
            raw_path = project_path / 'raw'
            if raw_path.exists():
                target_path = raw_path / path
                base_path = raw_path
            else:
                target_path = project_path / path
                base_path = project_path
        
        if not target_path.exists():
            return {'error': 'Path not found'}
        
        return self._build_tree(target_path, base_path)
    
    def _build_tree(self, current_path: Path, base_path: Path) -> Dict:
        """ディレクトリツリーを再帰的に構築"""
        relative_path = current_path.relative_to(base_path)
        
        node = {
            'name': current_path.name,
            'path': str(relative_path),
            'type': 'directory' if current_path.is_dir() else 'file',
            'size': current_path.stat().st_size if current_path.is_file() else 0,
            'modified': datetime.fromtimestamp(current_path.stat().st_mtime).isoformat(),
            'children': []
        }
        
        if current_path.is_dir():
            try:
                for item in sorted(current_path.iterdir()):
                    # 隠しファイルやシステムファイルをスキップ
                    if item.name.startswith('.') or item.name == '__pycache__':
                        continue
                    node['children'].append(self._build_tree(item, base_path))
            except PermissionError:
                node['error'] = 'Permission denied'
        
        return node
    
    def create_directory(self, project_folder: str, path: str) -> bool:
        """新しいディレクトリを作成"""
        project_path = self.projects_root / project_folder
        if not project_path.exists():
            return False
        
        new_dir = project_path / path
        try:
            new_dir.mkdir(parents=True, exist_ok=True)
            return True
        except Exception:
            return False
    
    def delete_item(self, project_folder: str, path: str) -> bool:
        """ファイルまたはディレクトリを削除"""
        project_path = self.projects_root / project_folder
        target = project_path / path
        
        if not target.exists():
            return False
        
        try:
            if target.is_file():
                target.unlink()
            else:
                import shutil
                shutil.rmtree(target)
            return True
        except Exception:
            return False
    
    def move_item(self, project_folder: str, source: str, destination: str) -> bool:
        """ファイルまたはディレクトリを移動"""
        project_path = self.projects_root / project_folder
        source_path = project_path / source
        dest_path = project_path / destination
        
        if not source_path.exists():
            return False
        
        try:
            source_path.rename(dest_path)
            return True
        except Exception:
            return False
    
    def get_file_info(self, project_folder: str, file_path: str) -> Optional[Dict]:
        """ファイルの詳細情報を取得"""
        project_path = self.projects_root / project_folder
        file_full_path = project_path / file_path
        
        if not file_full_path.exists() or not file_full_path.is_file():
            return None
        
        stat = file_full_path.stat()
        
        return {
            'name': file_full_path.name,
            'path': file_path,
            'size': stat.st_size,
            'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'extension': file_full_path.suffix,
            'mime_type': self._get_mime_type(file_full_path.suffix)
        }
    
    def upload_file(self, project_folder: str, file: UploadedFile, target_path: str = '') -> Dict:
        """ファイルをプロジェクトのrawフォルダにアップロード"""
        project_path = self.projects_root / project_folder
        if not project_path.exists():
            return {'error': 'Project not found', 'success': False}
        
        # rawフォルダを基準にする
        raw_path = project_path / 'raw'
        if not raw_path.exists():
            raw_path.mkdir(parents=True, exist_ok=True)
        
        # アップロード先のパスを決定
        if target_path:
            upload_dir = raw_path / target_path
        else:
            upload_dir = raw_path
        
        # ディレクトリが存在しない場合は作成
        upload_dir.mkdir(parents=True, exist_ok=True)
        
        # ファイル名の重複チェックと処理
        file_path = upload_dir / file.name
        original_name = file.name
        counter = 1
        
        while file_path.exists():
            name_parts = original_name.rsplit('.', 1)
            if len(name_parts) == 2:
                base_name, extension = name_parts
                new_name = f"{base_name}_{counter}.{extension}"
            else:
                new_name = f"{original_name}_{counter}"
            file_path = upload_dir / new_name
            counter += 1
        
        try:
            # ファイルを保存
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            # ファイル情報を返す
            stat = file_path.stat()
            relative_path = file_path.relative_to(raw_path)
            
            return {
                'success': True,
                'file': {
                    'name': file_path.name,
                    'path': str(relative_path),
                    'size': stat.st_size,
                    'uploaded': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'mime_type': self._get_mime_type(file_path.suffix)
                }
            }
        except Exception as e:
            return {'error': f'Failed to upload file: {str(e)}', 'success': False}
    
    def upload_multiple_files(self, project_folder: str, files: List[UploadedFile], target_path: str = '') -> Dict:
        """複数ファイルを一括アップロード"""
        results = {
            'success': True,
            'uploaded_files': [],
            'failed_files': [],
            'total_count': len(files),
            'success_count': 0,
            'error_count': 0
        }
        
        for file in files:
            result = self.upload_file(project_folder, file, target_path)
            if result.get('success'):
                results['uploaded_files'].append(result['file'])
                results['success_count'] += 1
            else:
                results['failed_files'].append({
                    'name': file.name,
                    'error': result.get('error', 'Unknown error')
                })
                results['error_count'] += 1
        
        # 一つでも失敗があった場合は全体を失敗とする
        if results['error_count'] > 0:
            results['success'] = False
        
        return results

    def _get_mime_type(self, extension: str) -> str:
        """ファイル拡張子からMIMEタイプを推定"""
        mime_types = {
            '.py': 'text/x-python',
            '.js': 'text/javascript',
            '.json': 'application/json',
            '.csv': 'text/csv',
            '.txt': 'text/plain',
            '.md': 'text/markdown',
            '.html': 'text/html',
            '.css': 'text/css',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.pdf': 'application/pdf',
            '.zip': 'application/zip',
        }
        return mime_types.get(extension.lower(), 'application/octet-stream')
    
    def search_files(self, project_folder: str, query: str, search_type: str = 'name') -> Dict:
        """
        プロジェクト内のファイルを検索
        
        Args:
            project_folder: プロジェクトのフォルダ名
            query: 検索クエリ
            search_type: 検索タイプ ('name', 'content', 'both')
        
        Returns:
            検索結果の辞書
        """
        project_path = self.projects_root / project_folder
        if not project_path.exists():
            return {'error': 'Project not found', 'results': []}
        
        # rawフォルダを基準にする
        raw_path = project_path / 'raw'
        if not raw_path.exists():
            return {'error': 'Raw folder not found', 'results': []}
        
        results = []
        
        try:
            if search_type in ['name', 'both']:
                # ファイル名で検索
                name_results = self._search_by_name(raw_path, query)
                results.extend(name_results)
            
            if search_type in ['content', 'both']:
                # ファイル内容で検索
                content_results = self._search_by_content(raw_path, query)
                # 重複を避けるため、パスでフィルタリング
                existing_paths = {r['path'] for r in results}
                for result in content_results:
                    if result['path'] not in existing_paths:
                        results.append(result)
            
            # 結果をソート（ファイル名順）
            results.sort(key=lambda x: x['name'].lower())
            
            return {
                'success': True,
                'query': query,
                'search_type': search_type,
                'total_results': len(results),
                'results': results
            }
        except Exception as e:
            return {
                'error': f'Search failed: {str(e)}',
                'results': []
            }
    
    def _search_by_name(self, base_path: Path, query: str) -> List[Dict]:
        """ファイル名による検索"""
        results = []
        query_lower = query.lower()
        
        for item in base_path.rglob('*'):
            if item.is_file() and query_lower in item.name.lower():
                relative_path = item.relative_to(base_path)
                stat = item.stat()
                
                results.append({
                    'name': item.name,
                    'path': str(relative_path),
                    'type': 'file',
                    'size': stat.st_size,
                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    'match_type': 'name',
                    'directory': str(relative_path.parent) if relative_path.parent != Path('.') else ''
                })
        
        return results
    
    def _search_by_content(self, base_path: Path, query: str) -> List[Dict]:
        """ファイル内容による検索"""
        results = []
        query_lower = query.lower()
        
        # テキストファイルの拡張子
        text_extensions = {'.txt', '.py', '.js', '.json', '.csv', '.md', '.html', '.css', '.sql', '.xml', '.yml', '.yaml'}
        
        for item in base_path.rglob('*'):
            if item.is_file() and item.suffix.lower() in text_extensions:
                try:
                    # ファイルサイズチェック（大きすぎるファイルはスキップ）
                    if item.stat().st_size > 10 * 1024 * 1024:  # 10MB制限
                        continue
                    
                    with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if query_lower in content.lower():
                            relative_path = item.relative_to(base_path)
                            stat = item.stat()
                            
                            # マッチした行を取得
                            lines = content.split('\n')
                            matched_lines = []
                            for i, line in enumerate(lines):
                                if query_lower in line.lower():
                                    matched_lines.append({
                                        'line_number': i + 1,
                                        'content': line.strip()[:200]  # 最初の200文字のみ
                                    })
                                    if len(matched_lines) >= 5:  # 最大5行まで
                                        break
                            
                            results.append({
                                'name': item.name,
                                'path': str(relative_path),
                                'type': 'file',
                                'size': stat.st_size,
                                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                                'match_type': 'content',
                                'directory': str(relative_path.parent) if relative_path.parent != Path('.') else '',
                                'matched_lines': matched_lines
                            })
                except (UnicodeDecodeError, PermissionError):
                    # エンコードエラーや権限エラーは無視
                    continue
        
        return results