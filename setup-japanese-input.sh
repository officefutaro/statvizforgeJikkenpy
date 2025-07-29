#!/bin/bash

# ==========================================
# WSL日本語入力セットアップスクリプト
# ==========================================

echo "🇯🇵 WSL日本語入力環境のセットアップを開始します..."

# カラー出力用の関数
print_success() { echo -e "\033[32m✅ $1\033[0m"; }
print_info() { echo -e "\033[34mℹ️  $1\033[0m"; }
print_warning() { echo -e "\033[33m⚠️  $1\033[0m"; }
print_error() { echo -e "\033[31m❌ $1\033[0m"; }

# 現在の状況確認
print_info "現在の日本語入力環境を確認中..."

# fcitx-mozcのインストール（推奨）
print_info "fcitx-mozcをインストールしますか？（推奨） (y/N)"
read -r -n 1 -s install_fcitx
echo
if [[ $install_fcitx =~ ^[Yy]$ ]]; then
    print_info "fcitx-mozcをインストール中..."
    sudo apt update
    sudo apt install -y fcitx-mozc fcitx-config-gtk fonts-noto-cjk
    print_success "fcitx-mozc インストール完了"
    
    # 環境変数の設定
    print_info "環境変数を設定中..."
    cat >> ~/.bashrc << 'EOF'

# Japanese Input Method (fcitx)
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export DefaultIMModule=fcitx

# Auto-start fcitx
if [ "$XDG_SESSION_TYPE" = "x11" ] || [ -n "$DISPLAY" ]; then
    fcitx-autostart > /dev/null 2>&1
fi
EOF
    print_success "環境変数設定完了"
fi

# ibus-mozcのインストール（代替案）
if [[ ! $install_fcitx =~ ^[Yy]$ ]]; then
    print_info "ibus-mozcをインストールしますか？ (y/N)"
    read -r -n 1 -s install_ibus
    echo
    if [[ $install_ibus =~ ^[Yy]$ ]]; then
        print_info "ibus-mozcをインストール中..."
        sudo apt update
        sudo apt install -y ibus-mozc fonts-noto-cjk
        print_success "ibus-mozc インストール完了"
        
        # 環境変数の設定
        print_info "環境変数を設定中..."
        cat >> ~/.bashrc << 'EOF'

# Japanese Input Method (ibus)
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export DefaultIMModule=ibus

# Auto-start ibus
if [ "$XDG_SESSION_TYPE" = "x11" ] || [ -n "$DISPLAY" ]; then
    ibus-daemon -drx > /dev/null 2>&1
fi
EOF
        print_success "環境変数設定完了"
    fi
fi

# フォントキャッシュの更新
print_info "フォントキャッシュを更新中..."
fc-cache -fv > /dev/null 2>&1
print_success "フォントキャッシュ更新完了"

# 設定ファイルの作成
print_info "日本語入力トラブルシューティングガイドを作成中..."
cat > ~/japanese-input-guide.md << 'EOF'
# WSL日本語入力ガイド

## セットアップ後の手順

### 1. WSLを再起動
```bash
# Windowsのコマンドプロンプトまたは PowerShell で実行
wsl --shutdown
```

### 2. 環境変数の反映
```bash
source ~/.bashrc
```

### 3. 日本語入力の起動

#### fcitxの場合
```bash
fcitx-autostart
fcitx-configtool  # 設定画面
```

#### ibusの場合
```bash
ibus-daemon -drx
ibus-setup  # 設定画面
```

### 4. Firefoxでの設定
1. Firefoxを再起動
2. 右クリック → 「入力メソッド」から fcitx または ibus を選択
3. Ctrl+Space または 半角/全角キー で日本語入力を切り替え

## トラブルシューティング

### 日本語入力が動作しない場合

1. **プロセスの確認**
```bash
# fcitxの場合
ps aux | grep fcitx

# ibusの場合
ps aux | grep ibus
```

2. **手動起動**
```bash
# fcitxの場合
fcitx -r -d

# ibusの場合
ibus-daemon -drx
```

3. **環境変数の確認**
```bash
echo $GTK_IM_MODULE
echo $QT_IM_MODULE
echo $XMODIFIERS
```

### WSLg (Windows 11) の場合
通常は追加設定不要ですが、動作しない場合：
```bash
export DISPLAY=:0
export WAYLAND_DISPLAY=wayland-0
```

### X11 Forwarding (Windows 10) の場合
VcXsrv等のXサーバーが必要です。

## 代替案：Windows側のIMEを使用

WSL内での日本語入力が困難な場合、Windows側で入力してコピー&ペーストする方法もあります。

1. Windows側のメモ帳等で日本語を入力
2. Ctrl+C でコピー
3. WSL/Firefoxで Ctrl+Shift+V でペースト（またはShift+Insert）
EOF

print_success "ガイドを作成しました: ~/japanese-input-guide.md"

# 結果サマリー
echo ""
echo "📋 セットアップ完了!"
echo "========================================"
print_info "次のステップ:"
echo "1. source ~/.bashrc を実行"
echo "2. fcitx-autostart または ibus-daemon -drx を実行"
echo "3. Firefoxを再起動"
echo "4. 入力フィールドで Ctrl+Space で日本語入力を切り替え"
echo ""
print_info "詳細は ~/japanese-input-guide.md を参照してください"

# WSL再起動の推奨
echo ""
print_warning "完全に適用するにはWSLの再起動を推奨します："
echo "Windowsで: wsl --shutdown"
echo "その後WSLを再度起動してください"