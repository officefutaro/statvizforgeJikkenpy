#!/bin/bash

# ==========================================
# 軽量ブラウザオプション付きセットアップスクリプト
# ==========================================

set -e

echo "🚀 軽量ブラウザオプション付きセットアップを開始します..."

# カラー出力用の関数
print_success() { echo -e "\033[32m✅ $1\033[0m"; }
print_info() { echo -e "\033[34mℹ️  $1\033[0m"; }
print_warning() { echo -e "\033[33m⚠️  $1\033[0m"; }
print_error() { echo -e "\033[31m❌ $1\033[0m"; }

# ブラウザ選択メニュー
print_info "インストールするブラウザを選択してください:"
echo "1) Firefox（推奨、フル機能）"
echo "2) Chromium（軽量、オープンソース）"
echo "3) Links（超軽量、テキストベース）"
echo "4) w3m（軽量、テキストベース）"
echo "5) すべてインストール"
echo "6) カスタム選択"

read -p "選択してください (1-6): " browser_choice

# システム更新
print_info "システムを更新中..."
sudo apt update

# ブラウザインストール関数
install_firefox() {
    print_info "Firefox をインストール中..."
    sudo apt install -y firefox
    print_success "Firefox インストール完了"
}

install_chromium() {
    print_info "Chromium をインストール中..."
    sudo apt install -y chromium-browser
    print_success "Chromium インストール完了"
}

install_links() {
    print_info "Links をインストール中..."
    sudo apt install -y links
    print_success "Links インストール完了"
}

install_w3m() {
    print_info "w3m をインストール中..."
    sudo apt install -y w3m w3m-img
    print_success "w3m インストール完了"
}

# 選択に基づいてインストール
case $browser_choice in
    1)
        install_firefox
        PRIMARY_BROWSER="firefox"
        ;;
    2)
        install_chromium
        PRIMARY_BROWSER="chromium-browser"
        ;;
    3)
        install_links
        PRIMARY_BROWSER="links"
        ;;
    4)
        install_w3m
        PRIMARY_BROWSER="w3m"
        ;;
    5)
        install_firefox
        install_chromium
        install_links
        install_w3m
        PRIMARY_BROWSER="firefox"
        ;;
    6)
        echo "カスタム選択："
        read -p "Firefox をインストールしますか? (y/N): " -n 1 -r
        echo
        [[ $REPLY =~ ^[Yy]$ ]] && install_firefox && PRIMARY_BROWSER="firefox"
        
        read -p "Chromium をインストールしますか? (y/N): " -n 1 -r
        echo
        [[ $REPLY =~ ^[Yy]$ ]] && install_chromium && PRIMARY_BROWSER="chromium-browser"
        
        read -p "Links をインストールしますか? (y/N): " -n 1 -r
        echo
        [[ $REPLY =~ ^[Yy]$ ]] && install_links
        
        read -p "w3m をインストールしますか? (y/N): " -n 1 -r
        echo
        [[ $REPLY =~ ^[Yy]$ ]] && install_w3m
        ;;
    *)
        print_error "無効な選択です"
        exit 1
        ;;
esac

# 軽量開発サーバー起動スクリプトの作成
print_info "軽量開発環境スクリプトを作成中..."
cat > ~/start-statviz-light.sh << EOF
#!/bin/bash

PROJECT_DIR="/home/futaro/project/StatVizForge_JikkenPy"
PRIMARY_BROWSER="$PRIMARY_BROWSER"

echo "🚀 StatVizForge 軽量開発環境を起動中..."

# バックエンドの起動
echo "📡 バックエンドサーバーを起動中..."
cd "\$PROJECT_DIR/app/backend"
if [[ -f "venv/bin/activate" ]]; then
    source venv/bin/activate
    python manage.py runserver 127.0.0.1:8000 &
    BACKEND_PID=\$!
    echo "✅ バックエンド起動完了 (PID: \$BACKEND_PID)"
fi

# 軽量な開発用サーバー（フロントエンドビルド不要）
echo "🌐 軽量フロントエンドサーバーを起動中..."
cd "\$PROJECT_DIR/app/frontend"
python3 -m http.server 3000 &
FRONTEND_PID=\$!
echo "✅ 軽量フロントエンド起動完了 (PID: \$FRONTEND_PID)"

sleep 5

# ブラウザ起動
echo "🌐 ブラウザを起動中..."
case "\$PRIMARY_BROWSER" in
    "firefox")
        firefox http://localhost:3000 &
        firefox http://localhost:8000 &
        ;;
    "chromium-browser")
        chromium-browser http://localhost:3000 &
        chromium-browser http://localhost:8000 &
        ;;
    "links")
        echo "Links でアクセス: links http://localhost:3000"
        links http://localhost:3000 &
        ;;
    "w3m")
        echo "w3m でアクセス: w3m http://localhost:3000"
        w3m http://localhost:3000 &
        ;;
esac

echo "🎉 軽量開発環境起動完了!"
echo "📊 フロントエンド: http://localhost:3000"
echo "🔧 バックエンドAPI: http://localhost:8000"

# クリーンアップ
cleanup() {
    echo "🧹 終了中..."
    [[ -n "\$BACKEND_PID" ]] && kill \$BACKEND_PID 2>/dev/null || true
    [[ -n "\$FRONTEND_PID" ]] && kill \$FRONTEND_PID 2>/dev/null || true
    echo "👋 終了しました"
}

trap cleanup EXIT INT TERM
wait
EOF

chmod +x ~/start-statviz-light.sh

# ブラウザテストスクリプト（軽量版）
cat > ~/test-browsers-light.sh << 'EOF'
#!/bin/bash

echo "🧪 利用可能なブラウザをテスト中..."

test_browser() {
    local browser=$1
    local name=$2
    
    if command -v $browser >/dev/null 2>&1; then
        echo "✅ $name が利用可能です"
        case $browser in
            "links"|"w3m")
                echo "   テキストブラウザ: $browser --version"
                ;;
            *)
                echo "   GUI ブラウザ: $browser --version"
                $browser --version 2>/dev/null || echo "   バージョン情報取得不可"
                ;;
        esac
    else
        echo "❌ $name が見つかりません"
    fi
}

test_browser "firefox" "Firefox"
test_browser "chromium-browser" "Chromium"
test_browser "google-chrome" "Google Chrome"
test_browser "links" "Links"
test_browser "w3m" "w3m"

echo ""
echo "🌐 簡易Webサーバーテスト:"
echo "以下のコマンドで軽量サーバーを起動できます:"
echo "  python3 -m http.server 8080"
echo "  php -S localhost:8080 (PHPがインストールされている場合)"

echo ""
echo "🎉 ブラウザテスト完了!"
EOF

chmod +x ~/test-browsers-light.sh

# エイリアス追加
{
    echo ""
    echo "# StatVizForge 軽量開発用エイリアス"
    echo "alias statviz-light='~/start-statviz-light.sh'"
    echo "alias test-browsers='~/test-browsers-light.sh'"
} >> ~/.bashrc

print_success "🎉 軽量ブラウザ環境のセットアップが完了しました!"
echo ""
echo "📋 利用可能なコマンド:"
echo "  statviz-light    - 軽量開発環境を起動"
echo "  test-browsers    - 利用可能なブラウザをテスト"
echo ""
echo "🚀 今すぐ試すには:"
echo "  source ~/.bashrc && test-browsers"