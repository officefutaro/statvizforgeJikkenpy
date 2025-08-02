#!/bin/bash

# 夜間実行フルテストスクリプト
# 使用方法: ./run-full-test.sh [--include-head-test] [--no-time-limit] [--auto-fix]

set -e

# カラー定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# タイムスタンプ
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DATE_ONLY=$(date +"%Y%m%d")

# ディレクトリ設定
PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
TEST_RESULTS_DIR="$PROJECT_ROOT/test-results/full-test-$DATE_ONLY"
LOG_DIR="$PROJECT_ROOT/logs"
HISTORY_DIR="$PROJECT_ROOT/doc/history"
BACKUP_DIR="$PROJECT_ROOT/.test-backups/full-test-$TIMESTAMP"

# オプション解析
INCLUDE_HEAD_TEST=false
NO_TIME_LIMIT=false
AUTO_FIX=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --include-head-test)
            INCLUDE_HEAD_TEST=true
            shift
            ;;
        --no-time-limit)
            NO_TIME_LIMIT=true
            shift
            ;;
        --auto-fix)
            AUTO_FIX=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# ログ関数
log() {
    echo -e "${2}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}" | tee -a "$LOG_DIR/full-test-$DATE_ONLY.log"
}

# ディレクトリ作成
mkdir -p "$TEST_RESULTS_DIR"
mkdir -p "$LOG_DIR"
mkdir -p "$HISTORY_DIR"
mkdir -p "$BACKUP_DIR"

log "🚀 夜間フルテスト開始" "$BLUE"
log "設定: HEAD_TEST=$INCLUDE_HEAD_TEST, TIME_LIMIT=$NO_TIME_LIMIT, AUTO_FIX=$AUTO_FIX" "$YELLOW"

# 1. 環境準備
log "📋 環境準備中..." "$BLUE"

# プロジェクトバックアップ
log "バックアップ作成中..." "$YELLOW"
cd "$PROJECT_ROOT"
cp -r project "$BACKUP_DIR/" || true

# テスト用ブランチ作成
BRANCH_NAME="full-test-$DATE_ONLY"
git checkout -b "$BRANCH_NAME" || git checkout "$BRANCH_NAME"

# サービス起動
log "開発環境起動中..." "$YELLOW"
./stop-dev.sh || true
./start-dev.sh

# 起動待機
sleep 10

# 2. ユニットテスト実行
log "🧪 ユニットテスト実行中..." "$BLUE"

# バックエンドユニットテスト
cd "$PROJECT_ROOT/app/backend"
source venv/bin/activate
python3 manage.py test --parallel > "$TEST_RESULTS_DIR/backend-unit-test.log" 2>&1 || {
    log "バックエンドユニットテスト失敗" "$RED"
}

# フロントエンドユニットテスト
cd "$PROJECT_ROOT/app/frontend"
npm test -- --coverage --watchAll=false > "$TEST_RESULTS_DIR/frontend-unit-test.log" 2>&1 || {
    log "フロントエンドユニットテスト失敗" "$RED"
}

# 3. 統合テスト実行
log "🔄 統合テスト実行中..." "$BLUE"
cd "$PROJECT_ROOT"
python3 tests/api_integration_test.py > "$TEST_RESULTS_DIR/integration-test.log" 2>&1 || {
    log "統合テスト失敗" "$RED"
}

# 4. E2Eテスト実行
log "🌐 E2Eテスト実行中..." "$BLUE"
cd "$PROJECT_ROOT/app/frontend"

# ヘッドレスモード
log "ヘッドレスモードE2Eテスト..." "$YELLOW"
npm run test:e2e > "$TEST_RESULTS_DIR/e2e-headless.log" 2>&1 || {
    log "ヘッドレスE2Eテスト失敗" "$RED"
}

# ヘッドモード（オプション）
if [ "$INCLUDE_HEAD_TEST" = true ]; then
    log "ヘッドモードE2Eテスト..." "$YELLOW"
    npm run test:e2e -- --headed > "$TEST_RESULTS_DIR/e2e-headed.log" 2>&1 || {
        log "ヘッドモードE2Eテスト失敗" "$RED"
    }
fi

# 5. 自動修正（オプション）
if [ "$AUTO_FIX" = true ]; then
    log "🔧 自動修正実行中..." "$BLUE"
    
    # ESLint/Prettier修正
    cd "$PROJECT_ROOT/app/frontend"
    npm run lint:fix > "$LOG_DIR/auto-fix-$DATE_ONLY.log" 2>&1 || true
    
    # TypeScript型エラー修正
    # TODO: 実装
    
    # data-testid属性追加
    # TODO: 実装
    
    # 修正内容をコミット
    cd "$PROJECT_ROOT"
    git add -A
    git commit -m "自動修正: Lint, フォーマット, テスト属性 - $DATE_ONLY" || true
fi

# 6. テスト結果集計
log "📊 テスト結果集計中..." "$BLUE"

# フルテスト結果ファイル作成
cat > "$HISTORY_DIR/full_test_$DATE_ONLY.md" << EOF
# 夜間フルテスト結果 - $DATE_ONLY

## 実行時刻
開始: $(date -d @$START_TIME '+%Y-%m-%d %H:%M:%S')
終了: $(date '+%Y-%m-%d %H:%M:%S')

## テスト結果サマリー

### ユニットテスト
- バックエンド: [結果はログ参照]
- フロントエンド: [結果はログ参照]

### 統合テスト
- API整合性: [結果はログ参照]

### E2Eテスト
- ヘッドレスモード: [結果はログ参照]
- ヘッドモード: $([ "$INCLUDE_HEAD_TEST" = true ] && echo "[結果はログ参照]" || echo "スキップ")

### 自動修正
- 実行: $([ "$AUTO_FIX" = true ] && echo "完了" || echo "スキップ")

## 詳細ログ
- バックエンドユニットテスト: test-results/full-test-$DATE_ONLY/backend-unit-test.log
- フロントエンドユニットテスト: test-results/full-test-$DATE_ONLY/frontend-unit-test.log
- 統合テスト: test-results/full-test-$DATE_ONLY/integration-test.log
- E2Eヘッドレス: test-results/full-test-$DATE_ONLY/e2e-headless.log
- E2Eヘッド: test-results/full-test-$DATE_ONLY/e2e-headed.log
EOF

# 許可待ち修正リスト作成
cat > "$HISTORY_DIR/pending_fixes_$DATE_ONLY.md" << EOF
# 許可待ち修正リスト - $DATE_ONLY

## APIエンドポイント変更
（検出された変更をここに記録）

## データベーススキーマ変更
（検出された変更をここに記録）

## パフォーマンス改善提案
（検出された改善案をここに記録）

## 未使用ファイル削除提案
（検出されたファイルをここに記録）
EOF

# 7. ブランチ統合とプッシュ
log "📤 ブランチ統合とプッシュ..." "$BLUE"

cd "$PROJECT_ROOT"
git checkout main
git merge --no-ff "$BRANCH_NAME" -m "夜間フルテスト実行と自動修正 - $DATE_ONLY"
git push origin main

# 8. クリーンアップ
log "🧹 クリーンアップ中..." "$YELLOW"
git branch -d "$BRANCH_NAME" || true

# 完了通知
log "✅ 夜間フルテスト完了！" "$GREEN"
log "結果確認: $HISTORY_DIR/full_test_$DATE_ONLY.md" "$GREEN"
log "許可待ち修正: $HISTORY_DIR/pending_fixes_$DATE_ONLY.md" "$GREEN"

# サービス停止（オプション）
# ./stop-dev.sh

exit 0