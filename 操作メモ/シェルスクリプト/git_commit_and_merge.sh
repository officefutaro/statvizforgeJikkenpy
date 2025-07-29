#!/bin/bash

# =============================================================================
# Git作業ブランチの変更コミット・メインブランチマージスクリプト
# =============================================================================
# 
# 作成日: 2025-07-29
# 目的: API改善作業の完了後、現在の作業ブランチから変更をコミットし、
#       mainブランチにマージしてリモートにプッシュする
# 
# 前提条件:
# - 現在のブランチ: work-session-20250729-072213
# - 作業内容: API改善、テスト生成、仮想環境整理が完了済み
# - プロジェクトルート: /home/futaro/project/StatVizForge_JikkenPy
# 
# =============================================================================

set -euo pipefail  # エラー時停止、未定義変数エラー、パイプエラー検出

# スクリプト実行ディレクトリの保存
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"

# ログ関数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

error() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1" >&2
    exit 1
}

# プロジェクトルートに移動
cd "$PROJECT_ROOT" || error "プロジェクトルートディレクトリに移動できません: $PROJECT_ROOT"

log "=== Git作業ブランチのコミット・マージ開始 ==="

# 現在のブランチ確認
CURRENT_BRANCH=$(git branch --show-current)
EXPECTED_BRANCH="work-session-20250729-072213"

if [ "$CURRENT_BRANCH" != "$EXPECTED_BRANCH" ]; then
    error "想定外のブランチです。現在: $CURRENT_BRANCH, 期待: $EXPECTED_BRANCH"
fi

log "現在のブランチ確認完了: $CURRENT_BRANCH"

# Gitステータス確認
log "Gitステータス確認中..."
git status --porcelain | head -10

# =============================================================================
# ステップ1: 重要な変更ファイルのみをステージング
# =============================================================================

log "ステップ1: 重要ファイルのステージング開始"

# 追加するファイルリスト
declare -a FILES_TO_ADD=(
    "CLAUDE_INSTRUCTIONS/"
    "app/backend/VIRTUAL_ENVIRONMENTS.md"
    "app/backend/analysis_env/"
    "app/frontend/components/SplitFileExplorer.tsx"
    "app/backend/API_DOCUMENTATION.md"
    "app/backend/api/urls.py"
    "app/backend/api/views.py"
    "app/backend/api/test_api_improvements.py"
    "app/frontend/components/__tests__/ApiImprovements.test.tsx"
    "doc/history/session_20250729.md"
)

# 各ファイルの存在確認とステージング
for file in "${FILES_TO_ADD[@]}"; do
    if [ -e "$file" ]; then
        log "  ✓ 追加: $file"
        git add "$file"
    else
        log "  ⚠ ファイルが見つかりません（スキップ）: $file"
    fi
done

# ステージング内容確認
log "ステージングされたファイル一覧:"
git diff --cached --name-only | while read -r staged_file; do
    log "  - $staged_file"
done

# =============================================================================
# ステップ2: コミット作成
# =============================================================================

log "ステップ2: コミット作成"

# コミットメッセージを作成
COMMIT_MESSAGE="API改善と機能追加の実装

主な変更:
- URL重複解消: @actionデコレータ削除、統一エンドポイント
- ファイルタグAPI統一: クエリパラメータ対応
- レスポンス形式統一: 一貫した成功/エラーレスポンス
- 未実装機能完成: search_files_by_tags実装
- スクロールバー追加: 長いコンテンツ対応
- 仮想環境整理: analysis_env統一
- テスト追加: バックエンド・フロントエンド両方

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# コミット実行
if git diff --cached --quiet; then
    log "⚠ ステージングされた変更がありません。コミットをスキップします。"
else
    git commit -m "$COMMIT_MESSAGE"
    COMMIT_HASH=$(git rev-parse HEAD)
    log "✓ コミット完了: $COMMIT_HASH"
fi

# =============================================================================
# ステップ3: mainブランチへのマージ
# =============================================================================

log "ステップ3: mainブランチへのマージ"

# mainブランチに切り替え
log "mainブランチに切り替え中..."
git checkout main || error "mainブランチへの切り替えに失敗しました"

# リモートからの最新変更を取得（オプション）
log "リモートからの最新変更を取得中..."
if git remote get-url origin &>/dev/null; then
    git fetch origin main || log "⚠ リモートからの取得に失敗しました（継続します）"
else
    log "⚠ originリモートが設定されていません"
fi

# 作業ブランチをマージ
log "作業ブランチをマージ中..."
git merge "$EXPECTED_BRANCH" || error "マージに失敗しました"

# マージ結果確認
MERGE_COMMIT=$(git rev-parse HEAD)
log "✓ マージ完了: $MERGE_COMMIT"

# =============================================================================
# ステップ4: リモートへのプッシュ
# =============================================================================

log "ステップ4: リモートへのプッシュ"

# リモートリポジトリの確認
if git remote get-url origin &>/dev/null; then
    log "originリモートにプッシュ中..."
    
    # プッシュ実行
    if git push origin main; then
        log "✓ プッシュ完了"
    else
        log "⚠ プッシュに失敗しました"
        log "  手動でプッシュが必要な場合があります: git push origin main"
    fi
else
    log "⚠ originリモートが設定されていないため、プッシュをスキップします"
    log "  必要に応じて手動でリモートを設定してプッシュしてください"
fi

# =============================================================================
# ステップ5: 作業ブランチに戻る（オプション）
# =============================================================================

log "ステップ5: 作業ブランチへの復帰"

# 作業ブランチに戻る
log "作業ブランチに戻り中..."
git checkout "$EXPECTED_BRANCH" || error "作業ブランチへの復帰に失敗しました"

log "✓ 作業ブランチに復帰完了: $(git branch --show-current)"

# =============================================================================
# 完了レポート
# =============================================================================

log "=== Git操作完了レポート ==="
log "作業ブランチ: $EXPECTED_BRANCH"
log "マージ先: main"
log "最終状態: $(git branch --show-current)"

# 最近のコミット履歴表示
log "最近のコミット履歴:"
git log --oneline -5 | while read -r commit_line; do
    log "  $commit_line"
done

log "=== Git作業ブランチのコミット・マージ完了 ==="

# スクリプト終了
exit 0