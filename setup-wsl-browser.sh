#!/bin/bash

# ==========================================
# StatVizForge WSL開発環境セットアップスクリプト
# ==========================================

set -e  # エラー時に停止

echo "🚀 StatVizForge WSL開発環境のセットアップを開始します..."

# カラー出力用の関数
print_success() {
    echo -e "\033[32m✅ $1\033[0m"
}

print_info() {
    echo -e "\033[34mℹ️  $1\033[0m"
}

print_warning() {
    echo -e "\033[33m⚠️  $1\033[0m"
}

print_error() {
    echo -e "\033[31m❌ $1\033[0m"
}

# WSL環境の確認
print_info "WSL環境を確認中..."
if [[ ! -f /proc/version ]] || ! grep -q microsoft /proc/version; then
    print_error "WSL環境が検出されませんでした。このスクリプトはWSL環境で実行してください。"
    exit 1
fi
print_success "WSL2環境を確認しました"

# システムの更新
print_info "システムパッケージを更新中..."
sudo apt update && sudo apt upgrade -y
print_success "システム更新完了"

# 必要なパッケージのインストール
print_info "基本パッケージをインストール中..."
sudo apt install -y \
    curl \
    wget \
    gnupg \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    lsb-release \
    xdg-utils

print_success "基本パッケージインストール完了"

# GUI サポートの確認（Windows 11 WSL2の場合）
print_info "GUI サポートを確認中..."
if command -v wslg >/dev/null 2>&1 || [[ -n "$DISPLAY" ]] || [[ -n "$WAYLAND_DISPLAY" ]]; then
    print_success "GUI サポートが利用可能です"
    GUI_AVAILABLE=true
else
    print_warning "GUI サポートが検出されませんでした。X11 Forwarding設定が必要かもしれません"
    GUI_AVAILABLE=false
fi

# Firefoxのインストール
print_info "Firefoxをインストール中..."
sudo apt install -y firefox
print_success "Firefox インストール完了"

# Google Chromeのインストール（オプション）
print_info "Google Chromeをインストールしますか？ (y/N)"
read -r -n 1 -s chrome_install
echo
if [[ $chrome_install =~ ^[Yy]$ ]]; then
    print_info "Google Chromeをインストール中..."
    
    # Google Chrome用のGPGキーを追加
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
    
    # Google Chromeのリポジトリを追加
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
    
    # パッケージリストを更新してChromeをインストール
    sudo apt update
    sudo apt install -y google-chrome-stable
    
    print_success "Google Chrome インストール完了"
else
    print_info "Google Chrome のインストールをスキップしました"
fi

# 開発用ディレクトリの確認
PROJECT_DIR="/home/futaro/project/StatVizForge_JikkenPy"
if [[ -d "$PROJECT_DIR" ]]; then
    print_success "プロジェクトディレクトリを確認しました: $PROJECT_DIR"
else
    print_warning "プロジェクトディレクトリが見つかりません: $PROJECT_DIR"
fi

# 開発環境起動スクリプトの作成
print_info "開発環境起動スクリプトを作成中..."
cat > ~/start-statviz-dev.sh << 'EOF'
#!/bin/bash

# StatVizForge 開発環境起動スクリプト
PROJECT_DIR="/home/futaro/project/StatVizForge_JikkenPy"

echo "🚀 StatVizForge 開発環境を起動中..."

# プロジェクトディレクトリの存在確認
if [[ ! -d "$PROJECT_DIR" ]]; then
    echo "❌ プロジェクトディレクトリが見つかりません: $PROJECT_DIR"
    exit 1
fi

# バックエンドの起動
echo "📡 バックエンドサーバーを起動中..."
cd "$PROJECT_DIR/app/backend"
if [[ -f "venv/bin/activate" ]]; then
    source venv/bin/activate
    python manage.py runserver_wsl &
    BACKEND_PID=$!
    echo "✅ バックエンド起動完了 (PID: $BACKEND_PID, Port: 8000)"
else
    echo "⚠️  仮想環境が見つかりません。手動でバックエンドを起動してください。"
fi

# フロントエンドの起動
echo "🌐 フロントエンドサーバーを起動中..."
cd "$PROJECT_DIR/app/frontend"
if [[ -f "package.json" ]]; then
    npm run dev &
    FRONTEND_PID=$!
    echo "✅ フロントエンド起動完了 (PID: $FRONTEND_PID, Port: 3000)"
else
    echo "⚠️  package.jsonが見つかりません。手動でフロントエンドを起動してください。"
fi

# サーバー起動を待機
echo "⏳ サーバー起動を待機中..."
sleep 8

# ブラウザの起動
echo "🌐 ブラウザを起動中..."
if command -v firefox >/dev/null 2>&1; then
    firefox http://localhost:3000 &
    echo "✅ Firefox で http://localhost:3000 を開きました"
elif command -v google-chrome >/dev/null 2>&1; then
    google-chrome http://localhost:3000 &
    echo "✅ Chrome で http://localhost:3000 を開きました"
else
    echo "⚠️  ブラウザが見つかりません。手動で http://localhost:3000 にアクセスしてください"
fi

echo ""
echo "🎉 開発環境起動完了!"
echo "📊 フロントエンド: http://localhost:3000"
echo "🔧 バックエンドAPI: http://localhost:8000"
echo "📝 管理画面: http://localhost:8000/admin"
echo ""
echo "終了するには Ctrl+C を押してください"

# プロセス終了時のクリーンアップ
cleanup() {
    echo ""
    echo "🧹 開発環境を終了中..."
    if [[ -n "$BACKEND_PID" ]]; then
        kill $BACKEND_PID 2>/dev/null || true
        echo "✅ バックエンドプロセスを終了しました"
    fi
    if [[ -n "$FRONTEND_PID" ]]; then
        kill $FRONTEND_PID 2>/dev/null || true
        echo "✅ フロントエンドプロセスを終了しました"
    fi
    echo "👋 開発環境を終了しました"
}

trap cleanup EXIT INT TERM

# フォアグラウンドで待機
wait
EOF

chmod +x ~/start-statviz-dev.sh
print_success "開発環境起動スクリプトを作成しました: ~/start-statviz-dev.sh"

# ブラウザテストスクリプトの作成
print_info "ブラウザテストスクリプトを作成中..."
cat > ~/test-browser.sh << 'EOF'
#!/bin/bash

echo "🧪 ブラウザ機能をテスト中..."

# Firefox テスト
if command -v firefox >/dev/null 2>&1; then
    echo "✅ Firefox が利用可能です"
    firefox --version
    
    echo "🌐 Firefox でテストページを開きます..."
    firefox --new-tab "data:text/html,<h1>WSL Firefox Test</h1><p>Firefox is working in WSL!</p>" &
    sleep 2
else
    echo "❌ Firefox が見つかりません"
fi

# Chrome テスト
if command -v google-chrome >/dev/null 2>&1; then
    echo "✅ Google Chrome が利用可能です"
    google-chrome --version
    
    echo "🌐 Chrome でテストページを開きます..."
    google-chrome --new-tab "data:text/html,<h1>WSL Chrome Test</h1><p>Chrome is working in WSL!</p>" &
    sleep 2
else
    echo "❌ Google Chrome が見つかりません"
fi

echo "🎉 ブラウザテスト完了!"
EOF

chmod +x ~/test-browser.sh
print_success "ブラウザテストスクリプトを作成しました: ~/test-browser.sh"

# 便利なエイリアスの設定
print_info "便利なエイリアスを追加中..."
{
    echo ""
    echo "# StatVizForge 開発用エイリアス"
    echo "alias statviz-dev='~/start-statviz-dev.sh'"
    echo "alias statviz-test='~/test-browser.sh'"
    echo "alias statviz-backend='cd /home/futaro/project/StatVizForge_JikkenPy/app/backend && source venv/bin/activate'"
    echo "alias statviz-frontend='cd /home/futaro/project/StatVizForge_JikkenPy/app/frontend'"
    echo "alias statviz-project='cd /home/futaro/project/StatVizForge_JikkenPy'"
} >> ~/.bashrc

print_success "エイリアスを ~/.bashrc に追加しました"

# X11 Forwarding の設定確認（WSLgが使えない場合）
if [[ "$GUI_AVAILABLE" == false ]]; then
    print_warning "WSLg が利用できない場合の設定方法:"
    echo ""
    echo "1. Windows側でX11サーバー（VcXsrv等）をインストール"
    echo "2. 以下を ~/.bashrc に追加:"
    echo "   export DISPLAY=\$(cat /etc/resolv.conf | grep nameserver | awk '{print \$2}'):0"
    echo "   export LIBGL_ALWAYS_INDIRECT=1"
    echo ""
fi

# 設定完了
print_success "🎉 WSL開発環境のセットアップが完了しました!"
echo ""
echo "📋 利用可能なコマンド:"
echo "  statviz-dev      - 開発環境を起動"
echo "  statviz-test     - ブラウザをテスト"
echo "  statviz-backend  - バックエンドディレクトリに移動"
echo "  statviz-frontend - フロントエンドディレクトリに移動"
echo "  statviz-project  - プロジェクトルートに移動"
echo ""
echo "🚀 今すぐ試すには:"
echo "  source ~/.bashrc && statviz-test"
echo ""
print_info "ブラウザが正常に動作することを確認してから statviz-dev で開発を開始してください。"