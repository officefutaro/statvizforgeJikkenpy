#!/bin/bash

# StatVizForge API Test Runner Script
# APIテストの実行とレポート生成

set -e  # エラー時に停止

# 色の定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ログファイル（testing/resultsディレクトリに保存）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTING_DIR="$(dirname "$SCRIPT_DIR")"
PROJECT_ROOT="$(dirname "$TESTING_DIR")"
BACKEND_DIR="$PROJECT_ROOT/app/backend"
TEST_RESULTS_DIR="$TESTING_DIR/results"
LOG_FILE="$TEST_RESULTS_DIR/test_results_$(date '+%Y%m%d_%H%M%S').log"

# 必要なディレクトリ作成
mkdir -p "$TEST_RESULTS_DIR"

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  StatVizForge API テストスイート${NC}"
    echo -e "${BLUE}================================${NC}"
    echo -e "実行時刻: $(date '+%Y-%m-%d %H:%M:%S')"
    echo -e "ログファイル: ${LOG_FILE}"
    echo ""
}

print_section() {
    echo -e "${YELLOW}--- $1 ---${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

check_environment() {
    print_section "環境チェック"
    
    # バックエンドディレクトリに移動
    cd "$BACKEND_DIR" || {
        print_error "バックエンドディレクトリが見つかりません: $BACKEND_DIR"
        exit 1
    }
    
    # 仮想環境チェック
    if [[ "$VIRTUAL_ENV" == "" ]]; then
        print_error "仮想環境が有効化されていません"
        echo "以下のコマンドを実行してください:"
        echo "cd $BACKEND_DIR"
        echo "source venv/bin/activate"
        exit 1
    fi
    print_success "仮想環境: $VIRTUAL_ENV"
    
    # Djangoチェック
    if ! python -c "import django" 2>/dev/null; then
        print_error "Djangoが見つかりません"
        exit 1
    fi
    print_success "Django環境: OK"
    
    # 必要なパッケージチェック
    if ! python -c "import parameterized" 2>/dev/null; then
        print_error "parameterizedパッケージが見つかりません"
        echo "pip install parameterized を実行してください"
        exit 1
    fi
    print_success "必要パッケージ: OK"
    
    echo ""
}

run_django_tests() {
    print_section "Django APIテスト実行"
    
    if python "$SCRIPT_DIR/run_tests.py" all 2>&1 | tee -a "$LOG_FILE"; then
        print_success "Django APIテスト完了"
        return 0
    else
        print_error "Django APIテストで失敗"
        return 1
    fi
}

run_manual_tests() {
    print_section "手動テスト用URL確認"
    
    # サーバーが起動しているかチェック
    if curl -s -f "http://localhost:8000/api/server-info/" > /dev/null 2>&1; then
        print_success "サーバー起動確認: http://localhost:8000"
        
        echo "手動テスト用URL:"
        echo "  プロジェクト一覧 (RESTful): http://localhost:8000/api/projects/"
        echo "  プロジェクト一覧 (Legacy):  http://localhost:8000/api/projects/list"
        echo "  削除済み一覧 (RESTful):    http://localhost:8000/api/projects/deleted/"
        echo "  削除済み一覧 (Legacy):     http://localhost:8000/api/projects/archived"
        echo "  サーバー情報:              http://localhost:8000/api/server-info/"
        echo ""
    else
        print_error "サーバーが起動していません"
        echo "別ターミナルで以下を実行してください:"
        echo "python manage.py runserver"
        return 1
    fi
}

run_specific_test() {
    local test_type=$1
    print_section "$test_type テスト実行"
    
    if python "$SCRIPT_DIR/run_tests.py" "$test_type" 2>&1 | tee -a "$LOG_FILE"; then
        print_success "$test_type テスト完了"
        return 0
    else
        print_error "$test_type テストで失敗"
        return 1
    fi
}

show_help() {
    echo "使用方法: $0 [オプション]"
    echo ""
    echo "オプション:"
    echo "  all          全てのテストを実行 (デフォルト)"
    echo "  lifecycle    プロジェクトライフサイクルテストのみ"
    echo "  compatibility エンドポイント互換性テストのみ"
    echo "  performance  パフォーマンステストのみ"
    echo "  manual       手動テスト用の情報表示"
    echo "  help         このヘルプを表示"
    echo ""
    echo "例:"
    echo "  $0                    # 全テスト実行"
    echo "  $0 lifecycle         # ライフサイクルテストのみ"
    echo "  $0 manual            # 手動テスト用情報"
}

generate_report() {
    print_section "テストレポート生成"
    
    REPORT_FILE="$TEST_RESULTS_DIR/test_report_$(date '+%Y%m%d_%H%M%S').md"
    
    echo "=== テスト実行レポート ===" > "$REPORT_FILE"
    echo "実行日時: $(date '+%Y-%m-%d %H:%M:%S')" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    echo "## テスト結果" >> "$REPORT_FILE"
    
    if [ -f "$LOG_FILE" ]; then
        echo "\`\`\`" >> "$REPORT_FILE"
        cat "$LOG_FILE" >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
    fi
    
    print_success "レポート生成完了: $REPORT_FILE"
}

main() {
    print_header
    check_environment
    
    case "${1:-all}" in
        "all")
            run_django_tests
            run_manual_tests
            ;;
        "lifecycle"|"compatibility"|"performance")
            run_specific_test "$1"
            ;;
        "manual")
            run_manual_tests
            ;;
        "help"|"-h"|"--help")
            show_help
            exit 0
            ;;
        *)
            print_error "不明なオプション: $1"
            show_help
            exit 1
            ;;
    esac
    
    generate_report
    
    print_section "テスト完了"
    echo "詳細は ${LOG_FILE} を確認してください"
}

# スクリプト実行
main "$@"