#!/bin/bash

# ==========================================
# WSL GUI トラブルシューティングスクリプト
# ==========================================

echo "🔍 WSL GUI環境のトラブルシューティングを実行中..."

# カラー出力用の関数
print_success() { echo -e "\033[32m✅ $1\033[0m"; }
print_info() { echo -e "\033[34mℹ️  $1\033[0m"; }
print_warning() { echo -e "\033[33m⚠️  $1\033[0m"; }
print_error() { echo -e "\033[31m❌ $1\033[0m"; }

echo "================================================"
echo "🖥️  WSL環境情報"
echo "================================================"

# WSL環境の確認
print_info "WSL環境情報:"
if [[ -f /proc/version ]]; then
    cat /proc/version
    if grep -q microsoft /proc/version; then
        print_success "WSL環境を確認しました"
    fi
else
    print_error "/proc/version が見つかりません"
fi

echo ""
print_info "WSLバージョン:"
wsl.exe --version 2>/dev/null || echo "WSL バージョン情報を取得できません"

echo ""
echo "================================================"
echo "🎨 GUI サポート状況"
echo "================================================"

# WSLg の確認
print_info "WSLg (Windows 11 GUI サポート) 確認:"
if [[ -n "$WAYLAND_DISPLAY" ]]; then
    print_success "WAYLAND_DISPLAY が設定されています: $WAYLAND_DISPLAY"
elif [[ -n "$DISPLAY" ]]; then
    print_success "DISPLAY が設定されています: $DISPLAY"
else
    print_warning "GUI表示変数が設定されていません"
fi

# X11関連のプロセス確認
print_info "X11関連プロセス:"
ps aux | grep -i x11 | grep -v grep || echo "X11関連プロセスが見つかりません"

echo ""
echo "================================================"
echo "🌐 ネットワーク設定"
echo "================================================"

# ネットワーク設定の確認
print_info "IPアドレス情報:"
ip addr show | grep -E "(inet|eth0|wsl)" || echo "ネットワークインターface情報を取得できません"

print_info "ポート使用状況:"
netstat -tlpn 2>/dev/null | grep -E "(3000|8000|8888)" || echo "開発用ポートは使用されていません"

echo ""
echo "================================================"
echo "📦 インストール済みブラウザ"
echo "================================================"

check_browser() {
    local browser=$1
    local name=$2
    
    if command -v $browser >/dev/null 2>&1; then
        print_success "$name がインストールされています"
        echo "   パス: $(which $browser)"
        case $browser in
            "firefox")
                firefox --version 2>/dev/null || echo "   バージョン情報取得不可"
                ;;
            "chromium-browser")
                chromium-browser --version 2>/dev/null || echo "   バージョン情報取得不可"
                ;;
            "google-chrome")
                google-chrome --version 2>/dev/null || echo "   バージョン情報取得不可"
                ;;
        esac
    else
        print_warning "$name がインストールされていません"
    fi
}

check_browser "firefox" "Firefox"
check_browser "chromium-browser" "Chromium"
check_browser "google-chrome" "Google Chrome"
check_browser "links" "Links"
check_browser "w3m" "w3m"

echo ""
echo "================================================"
echo "🔧 システム依存関係"
echo "================================================"

# 必要なパッケージの確認
print_info "GUI関連パッケージ:"
packages=("xdg-utils" "x11-apps" "mesa-utils" "libgl1-mesa-glx")
for pkg in "${packages[@]}"; do
    if dpkg -l | grep -q "^ii.*$pkg"; then
        print_success "$pkg がインストールされています"
    else
        print_warning "$pkg がインストールされていません"
    fi
done

echo ""
echo "================================================"
echo "🧪 GUI テスト"
echo "================================================"

# 簡単なGUIテスト
print_info "GUI テストを実行中..."

# xeyesテスト（軽量GUI アプリ）
if command -v xeyes >/dev/null 2>&1; then
    print_info "xeyes でGUIテストを実行します（5秒後に自動終了）..."
    timeout 5 xeyes &
    sleep 1
    if pgrep xeyes >/dev/null; then
        print_success "GUI描画テスト成功！"
        pkill xeyes 2>/dev/null || true
    else
        print_error "GUI描画テスト失敗"
    fi
else
    print_warning "xeyes がインストールされていません (sudo apt install x11-apps でインストール可能)"
fi

echo ""
echo "================================================"
echo "🛠️  修復提案"
echo "================================================"

print_info "一般的な問題の修復方法:"

echo ""
echo "1️⃣ WSLg が利用できない場合 (Windows 10 等):"
echo "   - VcXsrv または Xming をWindowsにインストール"
echo "   - ~/.bashrc に以下を追加:"
echo '   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk "{print \$2}"):0'
echo "   export LIBGL_ALWAYS_INDIRECT=1"

echo ""
echo "2️⃣ ブラウザがクラッシュする場合:"
echo "   - 軽量ブラウザを試用: links, w3m"
echo "   - --no-sandbox オプション付きで起動:"
echo "   firefox --no-sandbox"
echo "   chromium-browser --no-sandbox --disable-gpu"

echo ""
echo "3️⃣ ポート接続できない場合:"
echo "   - Windows Defender ファイアウォール設定を確認"
echo "   - WSL2 のポートフォワーディングを設定"

echo ""
echo "4️⃣ 依存関係エラーの場合:"
echo "   sudo apt update && sudo apt upgrade"
echo "   sudo apt install --fix-broken"

echo ""
echo "================================================"
echo "🚀 推奨セットアップコマンド"
echo "================================================"

echo "問題が見つかった場合、以下を順番に実行してください:"
echo ""
echo "# 基本GUI環境のセットアップ"
echo "sudo apt update"
echo "sudo apt install -y x11-apps xdg-utils"
echo ""
echo "# ブラウザのインストール"
echo "sudo apt install -y firefox"
echo ""
echo "# 軽量ブラウザ（バックアップ用）"
echo "sudo apt install -y links w3m"
echo ""
echo "# 設定の反映"
echo "source ~/.bashrc"

echo ""
print_success "🎉 トラブルシューティング完了!"
echo ""
print_info "詳細なサポートが必要な場合は、Microsoft WSL のドキュメントを参照してください:"
echo "https://docs.microsoft.com/ja-jp/windows/wsl/"