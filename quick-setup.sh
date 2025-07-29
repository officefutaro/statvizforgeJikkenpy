#!/bin/bash

# ==========================================
# StatVizForge クイックセットアップ（sudo不要）
# ==========================================

echo "🚀 StatVizForge クイックセットアップを開始します..."

# カラー出力用の関数
print_success() { echo -e "\033[32m✅ $1\033[0m"; }
print_info() { echo -e "\033[34mℹ️  $1\033[0m"; }
print_warning() { echo -e "\033[33m⚠️  $1\033[0m"; }
print_error() { echo -e "\033[31m❌ $1\033[0m"; }

# 現在のシステム状態をチェック
print_info "システム状態をチェック中..."

# WSL環境の確認
if [[ -f /proc/version ]] && grep -q microsoft /proc/version; then
    print_success "WSL環境を確認"
else
    print_error "WSL環境ではありません"
fi

# 既存ブラウザの確認
print_info "インストール済みブラウザをチェック中..."
browsers_found=0

if command -v firefox >/dev/null 2>&1; then
    print_success "Firefox が利用可能"
    browsers_found=$((browsers_found + 1))
else
    print_warning "Firefox がインストールされていません"
fi

if command -v google-chrome >/dev/null 2>&1; then
    print_success "Google Chrome が利用可能"
    browsers_found=$((browsers_found + 1))
else
    print_warning "Google Chrome がインストールされていません"
fi

if command -v chromium-browser >/dev/null 2>&1; then
    print_success "Chromium が利用可能"
    browsers_found=$((browsers_found + 1))
else
    print_warning "Chromium がインストールされていません"
fi

# Node.js環境の確認
print_info "開発環境をチェック中..."
if command -v node >/dev/null 2>&1; then
    print_success "Node.js が利用可能: $(node --version)"
else
    print_warning "Node.js がインストールされていません"
fi

if command -v npm >/dev/null 2>&1; then
    print_success "npm が利用可能: $(npm --version)"
else
    print_warning "npm がインストールされていません"
fi

if command -v python3 >/dev/null 2>&1; then
    print_success "Python3 が利用可能: $(python3 --version)"
else
    print_warning "Python3 がインストールされていません"
fi

# プロジェクト構造の確認
PROJECT_DIR="/home/futaro/project/StatVizForge_JikkenPy"
print_info "プロジェクト構造をチェック中..."

if [[ -d "$PROJECT_DIR" ]]; then
    print_success "プロジェクトディレクトリが存在"
    
    if [[ -d "$PROJECT_DIR/app/backend" ]]; then
        print_success "バックエンドディレクトリが存在"
        
        if [[ -f "$PROJECT_DIR/app/backend/venv/bin/activate" ]]; then
            print_success "Python仮想環境が存在"
        else
            print_warning "Python仮想環境が見つかりません"
        fi
        
        if [[ -f "$PROJECT_DIR/app/backend/manage.py" ]]; then
            print_success "Django管理スクリプトが存在"
        else
            print_warning "Django管理スクリプトが見つかりません"
        fi
    else
        print_error "バックエンドディレクトリが見つかりません"
    fi
    
    if [[ -d "$PROJECT_DIR/app/frontend" ]]; then
        print_success "フロントエンドディレクトリが存在"
        
        if [[ -f "$PROJECT_DIR/app/frontend/package.json" ]]; then
            print_success "package.json が存在"
        else
            print_warning "package.json が見つかりません"
        fi
    else
        print_error "フロントエンドディレクトリが見つかりません"
    fi
else
    print_error "プロジェクトディレクトリが見つかりません: $PROJECT_DIR"
fi

# 開発スクリプトの作成（sudo不要版）
print_info "軽量開発スクリプトを作成中..."

cat > ~/start-dev-simple.sh << 'EOF'
#!/bin/bash

PROJECT_DIR="/home/futaro/project/StatVizForge_JikkenPy"

echo "🚀 StatVizForge 簡易開発環境を起動中..."

# バックエンドの起動
if [[ -d "$PROJECT_DIR/app/backend" ]]; then
    echo "📡 バックエンドサーバーを起動中..."
    cd "$PROJECT_DIR/app/backend"
    
    if [[ -f "venv/bin/activate" ]]; then
        source venv/bin/activate
        echo "✅ 仮想環境をアクティベート"
        
        # バックグラウンドで起動
        python manage.py runserver 127.0.0.1:8000 &
        BACKEND_PID=$!
        echo "✅ バックエンド起動 (PID: $BACKEND_PID)"
    else
        echo "⚠️  仮想環境が見つかりません"
        python3 manage.py runserver 127.0.0.1:8000 &
        BACKEND_PID=$!
        echo "✅ バックエンド起動 (システムPython使用)"
    fi
else
    echo "❌ バックエンドディレクトリが見つかりません"
fi

# フロントエンドの起動（シンプル版）
if [[ -d "$PROJECT_DIR/app/frontend" ]]; then
    echo "🌐 フロントエンド簡易サーバーを起動中..."
    cd "$PROJECT_DIR/app/frontend"
    
    # Node.jsが利用可能な場合はnpm、そうでなければPythonサーバー
    if command -v npm >/dev/null 2>&1 && [[ -f "package.json" ]]; then
        npm run dev &
        FRONTEND_PID=$!
        echo "✅ フロントエンド起動 (Next.js) (PID: $FRONTEND_PID)"
    else
        echo "⚠️  npm/package.json が見つかりません。簡易サーバーを起動します"
        python3 -m http.server 3000 &
        FRONTEND_PID=$!
        echo "✅ 簡易フロントエンド起動 (PID: $FRONTEND_PID)"
    fi
else
    echo "❌ フロントエンドディレクトリが見つかりません"
fi

sleep 5

# ブラウザの起動
echo "🌐 利用可能なブラウザでアクセス中..."
opened=false

if command -v firefox >/dev/null 2>&1; then
    firefox http://localhost:3000 &
    echo "✅ Firefox で http://localhost:3000 を開きました"
    opened=true
elif command -v google-chrome >/dev/null 2>&1; then
    google-chrome http://localhost:3000 &
    echo "✅ Chrome で http://localhost:3000 を開きました"
    opened=true
elif command -v chromium-browser >/dev/null 2>&1; then
    chromium-browser http://localhost:3000 &
    echo "✅ Chromium で http://localhost:3000 を開きました"
    opened=true
fi

if [[ "$opened" == false ]]; then
    echo "⚠️  ブラウザが見つかりません"
    echo "手動で以下のURLにアクセスしてください:"
    echo "  フロントエンド: http://localhost:3000"
    echo "  バックエンド: http://localhost:8000"
fi

echo ""
echo "🎉 簡易開発環境起動完了!"
echo "📊 フロントエンド: http://localhost:3000"
echo "🔧 バックエンドAPI: http://localhost:8000"
echo ""
echo "停止するには Ctrl+C を押すか、以下のコマンドを実行:"
echo "  kill $BACKEND_PID $FRONTEND_PID"

# フォアグラウンドで待機
trap 'echo ""; echo "🛑 停止中..."; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; echo "👋 終了"; exit' INT TERM
wait
EOF

chmod +x ~/start-dev-simple.sh
print_success "簡易開発スクリプトを作成: ~/start-dev-simple.sh"

# ブラウザインストールガイドの作成
cat > ~/install-browsers.md << 'EOF'
# ブラウザインストールガイド

## 手動インストール方法

### Firefox（推奨）
```bash
sudo apt update
sudo apt install firefox
```

### Google Chrome
```bash
# GPGキーの追加
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /usr/share/keyrings/google-chrome-keyring.gpg > /dev/null

# リポジトリの追加
echo "deb [signed-by=/usr/share/keyrings/google-chrome-keyring.gpg arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list

# インストール
sudo apt update
sudo apt install google-chrome-stable
```

### Chromium（軽量版）
```bash
sudo apt install chromium-browser
```

## GUI サポートの設定

### Windows 11 + WSL2（WSLg）
通常は自動で動作します。

### Windows 10 + WSL2（X11 Forwarding）
1. VcXsrv をWindowsにインストール
2. VcXsrvを起動（Disable access control にチェック）
3. ~/.bashrc に以下を追加:
```bash
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
export LIBGL_ALWAYS_INDIRECT=1
```
4. `source ~/.bashrc` で設定を反映

## トラブルシューティング

### ブラウザが起動しない場合
```bash
# セーフモードで起動
firefox --safe-mode
google-chrome --no-sandbox --disable-gpu
```

### DISPLAY エラーの場合
```bash
export DISPLAY=:0
# または
export DISPLAY=localhost:0
```
EOF

print_success "ブラウザインストールガイドを作成: ~/install-browsers.md"

# 結果のサマリー
echo ""
echo "📋 セットアップ結果:"
echo "======================================"
print_info "ブラウザ: $browsers_found 個のブラウザが利用可能"

if [[ $browsers_found -gt 0 ]]; then
    print_success "今すぐ開発を開始できます！"
    echo ""
    echo "🚀 開発環境を起動するには:"
    echo "  ~/start-dev-simple.sh"
else
    print_warning "まずブラウザをインストールしてください"
    echo ""
    echo "📖 インストール方法:"
    echo "  cat ~/install-browsers.md"
    echo ""
    echo "または完全セットアップを実行:"
    echo "  ./setup-wsl-browser-interactive.sh"
fi

echo ""
echo "📁 作成されたファイル:"
echo "  ~/start-dev-simple.sh      - 簡易開発環境起動"
echo "  ~/install-browsers.md      - ブラウザインストールガイド"

print_success "🎉 クイックセットアップ完了!"