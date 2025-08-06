"""
Git操作のユーティリティ関数
プロジェクトフォルダ内でのGit操作を安全に実行
"""
import os
import subprocess
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from django.conf import settings


class GitError(Exception):
    """Git操作のエラー"""
    pass


class GitUtils:
    """Git操作のユーティリティクラス"""
    
    def __init__(self, project_folder: str):
        """
        Args:
            project_folder: プロジェクトフォルダ名
        """
        self.project_folder = project_folder
        self.project_path = Path(settings.PROJECTS_ROOT) / project_folder
        
        if not self.project_path.exists():
            raise GitError(f"Project folder not found: {project_folder}")
    
    def _run_git_command(self, command: List[str], cwd: Optional[Path] = None) -> Tuple[str, str, int]:
        """
        Gitコマンドを実行
        
        Args:
            command: Gitコマンドのリスト
            cwd: 実行ディレクトリ (デフォルト: プロジェクトパス)
            
        Returns:
            Tuple[stdout, stderr, return_code]
        """
        if cwd is None:
            cwd = self.project_path
            
        # 重要: パスが存在していることを確認
        if not cwd.exists():
            cwd.mkdir(parents=True, exist_ok=True)
            
        try:
            # デバッグ用ログ出力
            import logging
            logger = logging.getLogger(__name__)
            logger.info(f"Executing git command: {' '.join(['git'] + command)} in directory: {cwd}")
            
            # 重要: Gitコマンドをプロジェクト固有に制限するための環境変数設定
            env = os.environ.copy()
            
            # プロジェクトgitフォルダ内の.gitフォルダを明示的に指定
            git_dir = cwd / '.git'
            if git_dir.exists():
                env['GIT_DIR'] = str(git_dir)
                env['GIT_WORK_TREE'] = str(cwd)
                logger.info(f"Setting GIT_DIR={git_dir}, GIT_WORK_TREE={cwd}")
            else:
                # .gitフォルダが存在しない場合、親ディレクトリ検索を無効化
                env['GIT_CEILING_DIRECTORIES'] = str(cwd.parent)
                logger.info(f"Setting GIT_CEILING_DIRECTORIES={cwd.parent}")
            
            result = subprocess.run(
                ['git'] + command,
                cwd=str(cwd),  # 文字列で渡すことで確実に実行
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',  # 文字エンコーディングエラーの対処
                env=env,  # 適切な環境変数を設定
                timeout=30
            )
            
            # デバッグ用: 結果をログ出力
            logger.info(f"Git command result - Return code: {result.returncode}, Stdout: {result.stdout.strip()}, Stderr: {result.stderr.strip()}")
            
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except subprocess.TimeoutExpired:
            raise GitError("Git command timed out")
        except FileNotFoundError:
            raise GitError("Git command not found. Please install Git.")
    
    def is_git_repository(self) -> bool:
        """Gitリポジトリかどうかを確認"""
        # プロジェクトフォルダが存在しない場合はGitリポジトリではない
        if not self.project_path.exists():
            return False
        
        # 重要: 直接.gitフォルダの存在をチェックし、Gitコマンドに依存しない
        git_dir = self.project_path / '.git'
        return git_dir.exists()
    
    def init_repository(self) -> Dict[str, any]:
        """新しいGitリポジトリを初期化"""
        # 重要: プロジェクト固有のgitフォルダでのみGit初期化を実行
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Initializing Git repository in: {self.project_path}")
        
        if self.is_git_repository():
            logger.info(f"Git repository already exists in: {self.project_path}")
            return {
                'success': False,
                'message': 'Already a Git repository',
                'already_exists': True,
                'path': str(self.project_path)
            }
        
        # gitフォルダが存在しない場合は作成
        if not self.project_path.exists():
            logger.info(f"Creating git folder: {self.project_path}")
            self.project_path.mkdir(parents=True, exist_ok=True)
        
        # プロジェクトフォルダのみgit initを実行（重要！）
        stdout, stderr, returncode = self._run_git_command(['init'], cwd=self.project_path)
        
        if returncode != 0:
            logger.error(f"Git init failed in {self.project_path}: {stderr}")
            raise GitError(f"Failed to initialize Git repository: {stderr}")
        
        logger.info(f"Git init successful in {self.project_path}: {stdout}")
        
        # 初期コミットの準備
        self._create_initial_gitignore()
        
        return {
            'success': True,
            'message': 'Git repository initialized successfully',
            'path': str(self.project_path),
            'output': stdout
        }
    
    def _create_initial_gitignore(self):
        """初期の.gitignoreファイルを作成"""
        gitignore_content = '''# StatVizForge generated files
*.pyc
__pycache__/
.DS_Store
Thumbs.db
.vscode/
.idea/

# Data analysis outputs
*.log
*.tmp
.ipynb_checkpoints/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
'''
        gitignore_path = self.project_path / '.gitignore'
        if not gitignore_path.exists():
            gitignore_path.write_text(gitignore_content)
    
    def get_status(self) -> Dict[str, any]:
        """リポジトリの状態を取得"""
        if not self.is_git_repository():
            return {
                'is_repo': False,
                'message': 'Not a Git repository'
            }
        
        # ファイル状態を取得
        stdout, stderr, returncode = self._run_git_command(['status', '--porcelain'])
        
        if returncode != 0:
            raise GitError(f"Failed to get status: {stderr}")
        
        # ブランチ情報を取得
        branch_stdout, branch_stderr, branch_returncode = self._run_git_command(['branch', '--show-current'])
        current_branch = branch_stdout if branch_returncode == 0 else 'unknown'
        
        # ファイル状態を解析
        files = []
        for line in stdout.split('\n'):
            if line.strip():
                status_code = line[:2]
                filename = line[3:]
                files.append({
                    'filename': filename,
                    'status': self._parse_status_code(status_code),
                    'status_code': status_code
                })
        
        return {
            'is_repo': True,
            'current_branch': current_branch,
            'files': files,
            'has_changes': len(files) > 0
        }
    
    def _parse_status_code(self, code: str) -> str:
        """Git status codeを人間が読める形式に変換"""
        status_map = {
            'M ': 'modified',
            ' M': 'modified',
            'MM': 'modified',
            'A ': 'added',
            ' A': 'added',
            'D ': 'deleted',
            ' D': 'deleted',
            'R ': 'renamed',
            ' R': 'renamed',
            'C ': 'copied',
            ' C': 'copied',
            '??': 'untracked',
            '!!': 'ignored'
        }
        return status_map.get(code, 'unknown')
    
    def add_files(self, files: List[str] = None) -> Dict[str, any]:
        """ファイルをステージング領域に追加"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        if files is None:
            # 全ファイルを追加
            command = ['add', '.']
        else:
            # 指定されたファイルを追加
            command = ['add'] + files
        
        stdout, stderr, returncode = self._run_git_command(command)
        
        if returncode != 0:
            raise GitError(f"Failed to add files: {stderr}")
        
        return {
            'success': True,
            'message': f'Added {"all files" if files is None else f"{len(files)} files"} to staging area'
        }
    
    def commit(self, message: str, author_name: str = None, author_email: str = None) -> Dict[str, any]:
        """変更をコミット"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        # 作者情報を設定（提供された場合）
        if author_name and author_email:
            self._run_git_command(['config', 'user.name', author_name])
            self._run_git_command(['config', 'user.email', author_email])
        
        stdout, stderr, returncode = self._run_git_command(['commit', '-m', message])
        
        if returncode != 0:
            if 'nothing to commit' in stderr:
                return {
                    'success': False,
                    'message': 'Nothing to commit, working tree clean',
                    'nothing_to_commit': True
                }
            raise GitError(f"Failed to commit: {stderr}")
        
        # コミットハッシュを取得
        hash_stdout, _, _ = self._run_git_command(['rev-parse', 'HEAD'])
        commit_hash = hash_stdout[:8] if hash_stdout else 'unknown'
        
        return {
            'success': True,
            'message': f'Committed successfully: {commit_hash}',
            'commit_hash': commit_hash
        }
    
    def get_log(self, limit: int = 10) -> Dict[str, any]:
        """コミット履歴を取得"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        command = ['log', f'--max-count={limit}', '--pretty=format:%H|%an|%ae|%ad|%s', '--date=iso']
        stdout, stderr, returncode = self._run_git_command(command)
        
        if returncode != 0:
            if 'does not have any commits yet' in stderr:
                return {
                    'commits': [],
                    'message': 'No commits yet'
                }
            raise GitError(f"Failed to get log: {stderr}")
        
        commits = []
        for line in stdout.split('\n'):
            if line.strip():
                parts = line.split('|', 4)
                if len(parts) == 5:
                    commits.append({
                        'hash': parts[0],
                        'hash_short': parts[0][:8],
                        'author_name': parts[1],
                        'author_email': parts[2],
                        'date': parts[3],
                        'message': parts[4]
                    })
        
        return {
            'commits': commits,
            'total_commits': len(commits)
        }
    
    def get_branches(self) -> Dict[str, any]:
        """ブランチ一覧を取得"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        stdout, stderr, returncode = self._run_git_command(['branch', '-a'])
        
        if returncode != 0:
            raise GitError(f"Failed to get branches: {stderr}")
        
        branches = []
        current_branch = None
        
        for line in stdout.split('\n'):
            line = line.strip()
            if line:
                if line.startswith('* '):
                    current_branch = line[2:]
                    branches.append({
                        'name': line[2:],
                        'current': True,
                        'remote': line.startswith('* remotes/')
                    })
                else:
                    branches.append({
                        'name': line,
                        'current': False,
                        'remote': line.startswith('remotes/')
                    })
        
        return {
            'branches': branches,
            'current_branch': current_branch,
            'total_branches': len(branches)
        }
    
    def create_branch(self, branch_name: str, checkout: bool = True) -> Dict[str, any]:
        """新しいブランチを作成"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        # ブランチを作成
        stdout, stderr, returncode = self._run_git_command(['branch', branch_name])
        
        if returncode != 0:
            raise GitError(f"Failed to create branch: {stderr}")
        
        result = {
            'success': True,
            'message': f'Branch "{branch_name}" created successfully',
            'branch_name': branch_name
        }
        
        # チェックアウトする場合
        if checkout:
            checkout_result = self.checkout_branch(branch_name)
            result['checked_out'] = checkout_result['success']
        
        return result
    
    def checkout_branch(self, branch_name: str) -> Dict[str, any]:
        """ブランチをチェックアウト"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        stdout, stderr, returncode = self._run_git_command(['checkout', branch_name])
        
        if returncode != 0:
            raise GitError(f"Failed to checkout branch: {stderr}")
        
        return {
            'success': True,
            'message': f'Checked out to branch "{branch_name}"',
            'branch_name': branch_name
        }
    
    def get_diff(self, filename: str = None, staged: bool = False) -> Dict[str, any]:
        """差分を取得"""
        if not self.is_git_repository():
            raise GitError("Not a Git repository")
        
        command = ['diff']
        if staged:
            command.append('--staged')
        if filename:
            command.append(filename)
        
        stdout, stderr, returncode = self._run_git_command(command)
        
        return {
            'diff': stdout,
            'has_diff': bool(stdout.strip()),
            'filename': filename,
            'staged': staged
        }


def get_git_utils(project_folder: str) -> GitUtils:
    """GitUtilsインスタンスを取得"""
    return GitUtils(project_folder)