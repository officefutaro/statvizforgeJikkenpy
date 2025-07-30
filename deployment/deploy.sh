#!/bin/bash
# StatVizForge API v2.0 本番環境デプロイスクリプト
# 段階的デプロイメントと自動ロールバック機能付き

set -e

# 設定
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
BACKUP_DIR="/opt/statvizforge/backups"
DEPLOY_LOG="/opt/statvizforge/logs/deploy.log"
ENV_FILE="$SCRIPT_DIR/.env"

# 色付きログ出力
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1" | tee -a "$DEPLOY_LOG"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1" | tee -a "$DEPLOY_LOG"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1" | tee -a "$DEPLOY_LOG"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1" | tee -a "$DEPLOY_LOG"
}

# 前提条件チェック
check_prerequisites() {
    log_info "前提条件をチェックしています..."
    
    # Docker & Docker Compose
    if ! command -v docker &> /dev/null; then
        log_error "Docker がインストールされていません"
        exit 1
    fi
    
    if ! command -v docker compose &> /dev/null; then
        log_error "Docker Compose がインストールされていません"
        exit 1
    fi
    
    # 環境設定ファイル
    if [ ! -f "$ENV_FILE" ]; then
        log_error ".env ファイルが見つかりません"
        log_info ".env.example を参考に .env ファイルを作成してください"
        exit 1
    fi
    
    # 必要ディレクトリの作成
    mkdir -p "$BACKUP_DIR"
    mkdir -p "$(dirname "$DEPLOY_LOG")"
    
    log_success "前提条件チェック完了"
}

# 現在の環境をバックアップ
backup_current_state() {
    log_info "現在の環境をバックアップしています..."
    
    BACKUP_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    BACKUP_PATH="$BACKUP_DIR/backup_$BACKUP_TIMESTAMP"
    
    mkdir -p "$BACKUP_PATH"
    
    # データベースバックアップ
    if docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" ps postgres | grep -q "Up"; then
        log_info "データベースをバックアップ中..."
        docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" exec -T postgres pg_dumpall -c -U statvizforge > "$BACKUP_PATH/database_backup.sql"
        log_success "データベースバックアップ完了"
    fi
    
    # プロジェクトデータバックアップ
    if [ -d "/opt/statvizforge/projects" ]; then
        log_info "プロジェクトデータをバックアップ中..."
        tar -czf "$BACKUP_PATH/projects_backup.tar.gz" -C /opt/statvizforge projects/
        log_success "プロジェクトデータバックアップ完了"
    fi
    
    # 設定ファイルバックアップ
    cp "$ENV_FILE" "$BACKUP_PATH/env_backup"
    
    echo "$BACKUP_PATH" > /tmp/statvizforge_last_backup
    log_success "バックアップ完了: $BACKUP_PATH"
}

# ヘルスチェック
health_check() {
    local max_attempts=30
    local attempt=1
    
    log_info "ヘルスチェックを実行中..."
    
    while [ $attempt -le $max_attempts ]; do
        if curl -f -s http://localhost/health > /dev/null 2>&1; then
            log_success "ヘルスチェック成功 (試行 $attempt/$max_attempts)"
            return 0
        fi
        
        log_info "ヘルスチェック試行 $attempt/$max_attempts 失敗、5秒後に再試行..."
        sleep 5
        ((attempt++))
    done
    
    log_error "ヘルスチェック失敗: $max_attempts 回試行後もサービスが応答しません"
    return 1
}

# デプロイ実行
deploy() {
    log_info "デプロイを開始します..."
    
    # 新しいイメージをビルド
    log_info "新しいDockerイメージをビルド中..."
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" build --no-cache
    
    # 段階的デプロイメント
    log_info "段階的デプロイメントを開始..."
    
    # 1. データベースとRedisを最初に起動
    log_info "データベースサービスを起動中..."
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d postgres redis
    
    # データベース起動待機
    sleep 10
    
    # 2. アプリケーションサービスを起動
    log_info "アプリケーションサービスを起動中..."
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d web
    
    # アプリケーション起動待機
    sleep 15
    
    # 3. Nginx（リバースプロキシ）を起動
    log_info "リバースプロキシを起動中..."
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d nginx
    
    # 4. 監視サービス（オプション）
    log_info "監視サービスを起動中..."
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d prometheus grafana
    
    # 5. JupyterLab（オプション）
    if [ "${JUPYTER_ENABLED:-false}" = "true" ]; then
        log_info "JupyterLabを起動中..."
        docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d jupyter
    fi
    
    log_success "すべてのサービスが起動しました"
}

# ロールバック
rollback() {
    log_warning "ロールバックを実行しています..."
    
    if [ ! -f /tmp/statvizforge_last_backup ]; then
        log_error "バックアップパスが見つかりません"
        exit 1
    fi
    
    BACKUP_PATH=$(cat /tmp/statvizforge_last_backup)
    
    if [ ! -d "$BACKUP_PATH" ]; then
        log_error "バックアップディレクトリが見つかりません: $BACKUP_PATH"
        exit 1
    fi
    
    # サービス停止
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" down
    
    # データベースリストア
    if [ -f "$BACKUP_PATH/database_backup.sql" ]; then
        log_info "データベースをリストア中..."
        docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d postgres
        sleep 10
        docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" exec -T postgres psql -U statvizforge -d statvizforge < "$BACKUP_PATH/database_backup.sql"
    fi
    
    # プロジェクトデータリストア
    if [ -f "$BACKUP_PATH/projects_backup.tar.gz" ]; then
        log_info "プロジェクトデータをリストア中..."
        tar -xzf "$BACKUP_PATH/projects_backup.tar.gz" -C /opt/statvizforge/
    fi
    
    # 設定ファイルリストア
    if [ -f "$BACKUP_PATH/env_backup" ]; then
        cp "$BACKUP_PATH/env_backup" "$ENV_FILE"
    fi
    
    # サービス再起動
    docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" up -d
    
    log_success "ロールバック完了"
}

# メイン実行フロー
main() {
    local command="${1:-deploy}"
    
    case "$command" in
        "deploy")
            log_info "=== StatVizForge API v2.0 本番デプロイ開始 ==="
            check_prerequisites
            backup_current_state
            deploy
            
            if health_check; then
                log_success "=== デプロイ成功! ==="
                log_info "アプリケーションは https://localhost で利用可能です"
                log_info "管理画面: https://localhost/admin/"
                log_info "API: https://localhost/api/v1/"
                log_info "監視: https://localhost:3000 (Grafana)"
            else
                log_error "=== デプロイ失敗 - ロールバックを実行します ==="
                rollback
                exit 1
            fi
            ;;
        "rollback")
            log_warning "=== ロールバック実行 ==="
            rollback
            ;;
        "status")
            log_info "=== サービス状態確認 ==="
            docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" ps
            ;;
        "logs")
            log_info "=== サービスログ表示 ==="
            docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" logs -f "${2:-web}"
            ;;
        "stop")
            log_info "=== サービス停止 ==="
            docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" down
            ;;
        "restart")
            log_info "=== サービス再起動 ==="
            docker compose -f "$SCRIPT_DIR/docker-compose.prod.yml" restart
            ;;
        *)
            echo "使用方法: $0 [deploy|rollback|status|logs [service]|stop|restart]"
            echo ""
            echo "コマンド:"
            echo "  deploy   - 本番環境にデプロイ"
            echo "  rollback - 前回のバックアップにロールバック"
            echo "  status   - サービス状態を確認"
            echo "  logs     - サービスログを表示"
            echo "  stop     - すべてのサービスを停止"
            echo "  restart  - すべてのサービスを再起動"
            exit 1
            ;;
    esac
}

# スクリプト実行
main "$@"