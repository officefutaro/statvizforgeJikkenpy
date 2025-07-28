import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
from django.conf import settings

class FileCommentManager:
    """プロジェクトファイルのコメント管理クラス"""
    
    def __init__(self):
        self.projects_root = Path(settings.BASE_DIR).parent.parent / 'project'
    
    def get_comments_file_path(self, project_folder: str) -> Path:
        """プロジェクトのコメントファイルパスを取得"""
        project_path = self.projects_root / project_folder
        return project_path / 'file_comments.json'
    
    def load_comments(self, project_folder: str) -> Dict:
        """プロジェクトのコメント情報を読み込み"""
        # プロジェクトフォルダが存在するかチェック
        project_path = self.projects_root / project_folder
        if not project_path.exists():
            raise FileNotFoundError(f"Project folder '{project_folder}' not found")
        
        comments_file = self.get_comments_file_path(project_folder)
        
        if not comments_file.exists():
            return {
                'version': '1.0.0',
                'created': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'comments': {}
            }
        
        try:
            with open(comments_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {
                'version': '1.0.0',
                'created': datetime.now().isoformat(),
                'last_updated': datetime.now().isoformat(),
                'comments': {}
            }
    
    def save_comments(self, project_folder: str, comments_data: Dict) -> bool:
        """コメント情報を保存"""
        try:
            comments_file = self.get_comments_file_path(project_folder)
            comments_file.parent.mkdir(parents=True, exist_ok=True)
            
            comments_data['last_updated'] = datetime.now().isoformat()
            
            with open(comments_file, 'w', encoding='utf-8') as f:
                json.dump(comments_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def add_comment(self, project_folder: str, file_path: str, comment_text: str, author: str = 'Anonymous') -> Dict:
        """ファイルにコメントを追加"""
        comments_data = self.load_comments(project_folder)
        
        # ファイルパスの正規化（rawフォルダ相対パス）
        normalized_path = file_path.replace('\\', '/')
        
        # ファイルのコメントリストを取得または作成
        if normalized_path not in comments_data['comments']:
            comments_data['comments'][normalized_path] = []
        
        # 新しいコメントを作成
        new_comment = {
            'id': str(uuid.uuid4()),
            'text': comment_text,
            'author': author,
            'created': datetime.now().isoformat(),
            'edited': None
        }
        
        comments_data['comments'][normalized_path].append(new_comment)
        
        if self.save_comments(project_folder, comments_data):
            return {'success': True, 'comment': new_comment}
        else:
            return {'success': False, 'error': 'Failed to save comment'}
    
    def get_file_comments(self, project_folder: str, file_path: str) -> List[Dict]:
        """特定ファイルのコメント一覧を取得"""
        comments_data = self.load_comments(project_folder)
        normalized_path = file_path.replace('\\', '/')
        return comments_data['comments'].get(normalized_path, [])
    
    def get_all_comments(self, project_folder: str) -> Dict:
        """プロジェクト内の全コメント情報を取得"""
        return self.load_comments(project_folder)
    
    def update_comment(self, project_folder: str, file_path: str, comment_id: str, new_text: str) -> Dict:
        """コメントを更新"""
        comments_data = self.load_comments(project_folder)
        normalized_path = file_path.replace('\\', '/')
        
        if normalized_path not in comments_data['comments']:
            return {'success': False, 'error': 'File not found'}
        
        # コメントを検索して更新
        for comment in comments_data['comments'][normalized_path]:
            if comment['id'] == comment_id:
                comment['text'] = new_text
                comment['edited'] = datetime.now().isoformat()
                
                if self.save_comments(project_folder, comments_data):
                    return {'success': True, 'comment': comment}
                else:
                    return {'success': False, 'error': 'Failed to save comment'}
        
        return {'success': False, 'error': 'Comment not found'}
    
    def delete_comment(self, project_folder: str, file_path: str, comment_id: str) -> Dict:
        """コメントを削除"""
        comments_data = self.load_comments(project_folder)
        normalized_path = file_path.replace('\\', '/')
        
        if normalized_path not in comments_data['comments']:
            return {'success': False, 'error': 'File not found'}
        
        # コメントを検索して削除
        original_count = len(comments_data['comments'][normalized_path])
        comments_data['comments'][normalized_path] = [
            comment for comment in comments_data['comments'][normalized_path] 
            if comment['id'] != comment_id
        ]
        
        # コメントが削除されたかチェック
        if len(comments_data['comments'][normalized_path]) < original_count:
            # リストが空になった場合はキーも削除
            if not comments_data['comments'][normalized_path]:
                del comments_data['comments'][normalized_path]
            
            if self.save_comments(project_folder, comments_data):
                return {'success': True}
            else:
                return {'success': False, 'error': 'Failed to save changes'}
        
        return {'success': False, 'error': 'Comment not found'}
    
    def get_file_summary(self, project_folder: str) -> Dict:
        """ファイル別コメント数の要約を取得"""
        comments_data = self.load_comments(project_folder)
        summary = {}
        
        for file_path, comments in comments_data['comments'].items():
            summary[file_path] = {
                'comment_count': len(comments),
                'last_comment': comments[-1]['created'] if comments else None,
                'has_comments': len(comments) > 0
            }
        
        return summary