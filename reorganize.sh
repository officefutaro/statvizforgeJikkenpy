#!/bin/bash

# トップフォルダ整理スクリプト
# StatVizForge_JikkenPy のディレクトリ構造を整理する

set -e

# カラー定義
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# ログ関数
log() {
    echo -e "${2}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

# プロジェクトルート
PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"

log "🚀 トップフォルダ整理開始" "$BLUE"

# 現在のディレクトリに移動
cd "$PROJECT_ROOT"

# バックアップ作成
BACKUP_DIR="${PROJECT_ROOT}_backup_$(date +%Y%m%d_%H%M%S)"
log "📦 バックアップ作成: $BACKUP_DIR" "$YELLOW"
cp -r "$PROJECT_ROOT" "$BACKUP_DIR"

# 新しいディレクトリ構造を作成
log "📁 新しいディレクトリ構造を作成中..." "$BLUE"

mkdir -p _scripts
mkdir -p _config
mkdir -p _ai-instructions
mkdir -p _docs/setup
mkdir -p _docs/api
mkdir -p _docs/history
mkdir -p _docs/misc

# スクリプトファイルの移動
log "📝 スクリプトファイルを移動中..." "$YELLOW"

if [ -f "start-dev.sh" ]; then
    git mv start-dev.sh _scripts/ && log "✓ start-dev.sh moved" "$GREEN"
fi

if [ -f "stop-dev.sh" ]; then
    git mv stop-dev.sh _scripts/ && log "✓ stop-dev.sh moved" "$GREEN"
fi

if [ -f "check-status.sh" ]; then
    git mv check-status.sh _scripts/ && log "✓ check-status.sh moved" "$GREEN"
fi

if [ -f "run-tests.sh" ]; then
    git mv run-tests.sh _scripts/ && log "✓ run-tests.sh moved" "$GREEN"
fi

if [ -f "run-full-test.sh" ]; then
    git mv run-full-test.sh _scripts/ && log "✓ run-full-test.sh moved" "$GREEN"
fi

# 設定ファイルの移動
log "⚙️ 設定ファイルを移動中..." "$YELLOW"

if [ -f ".env" ]; then
    git mv .env _config/ && log "✓ .env moved" "$GREEN"
fi

if [ -f ".env.example" ]; then
    git mv .env.example _config/ && log "✓ .env.example moved" "$GREEN"
fi

if [ -f "requirements.txt" ]; then
    git mv requirements.txt _config/ && log "✓ requirements.txt moved" "$GREEN"
fi

# AI指示書の移動
log "🤖 AI指示書を移動中..." "$YELLOW"

if [ -d "CLAUDE_INSTRUCTIONS" ]; then
    git mv CLAUDE_INSTRUCTIONS _ai-instructions && log "✓ CLAUDE_INSTRUCTIONS → _ai-instructions" "$GREEN"
fi

# ドキュメントの移動・統合
log "📚 ドキュメントを整理中..." "$YELLOW"

# doc/history を _docs/history に移動
if [ -d "doc/history" ]; then
    git mv doc/history/* _docs/history/ 2>/dev/null || true
    rmdir doc/history 2>/dev/null || true
    rmdir doc 2>/dev/null || true
    log "✓ doc/history → _docs/history" "$GREEN"
fi

# その他のMarkdownファイルを移動
for md_file in *.md; do
    if [ -f "$md_file" ] && [ "$md_file" != "README.md" ]; then
        git mv "$md_file" _docs/misc/ && log "✓ $md_file → _docs/misc/" "$GREEN"
    fi
done

# スクリプト内のパス参照を更新
log "🔧 スクリプト内のパス参照を更新中..." "$YELLOW"

# _scripts/内のスクリプトのパス修正
for script in _scripts/*.sh; do
    if [ -f "$script" ]; then
        # 相対パスを絶対パスまたはプロジェクトルート基準に修正
        sed -i 's|^\(\./\)\([^/]\)|../\2|g' "$script" 2>/dev/null || true
        sed -i 's|PROJECT_ROOT=.*|PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"|g' "$script" 2>/dev/null || true
        log "✓ Updated paths in $(basename $script)" "$GREEN"
    fi
done

# 新しいREADME.mdを作成（簡潔版）
log "📄 新しいREADME.mdを作成中..." "$YELLOW"

cat > README.md << 'EOF'
# StatVizForge JikkenPy

データ可視化アプリケーションの実験プロジェクト

## クイックスタート

```bash
# 開発環境起動
./_scripts/start-dev.sh

# 停止
./_scripts/stop-dev.sh

# ステータス確認
./_scripts/check-status.sh
```

## ディレクトリ構成

- `app/` - アプリケーション本体（backend/frontend）
- `_scripts/` - 実行スクリプト
- `_docs/` - ドキュメント
- `_config/` - 設定ファイル
- `_ai-instructions/` - AI用指示書
- `project/` - プロジェクトデータ
- `tests/` - テストコード

詳細な情報は `_docs/README_detailed.md` を参照してください。
EOF

log "✅ トップフォルダ整理完了！" "$GREEN"

# 変更の確認
log "📊 変更内容を確認中..." "$BLUE"
git status

log "🔍 新しい構成:" "$BLUE"
tree -L 2 -a --dirsfirst 2>/dev/null || ls -la

log "✨ 整理完了！バックアップ: $BACKUP_DIR" "$GREEN"
log "📝 変更をコミットするには: git add -A && git commit -m 'トップフォルダ構成整理'" "$YELLOW"

exit 0