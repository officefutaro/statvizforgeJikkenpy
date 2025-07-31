#!/bin/bash

# WSL2ネットワーク設定チェックスクリプト
# バックエンドが正しく0.0.0.0でバインドされているかチェック

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"

echo "🌐 WSL2ネットワーク設定チェック開始..."

# 1. バックエンドポートバインディング確認
echo "📡 バックエンドポートバインディング確認..."
BACKEND_BIND=$(ss -tulnp | grep :8000 | head -1)

if echo "$BACKEND_BIND" | grep -q "0.0.0.0:8000"; then
    echo "✅ バックエンド正常: 0.0.0.0:8000でバインド"
    BACKEND_OK=true
elif echo "$BACKEND_BIND" | grep -q "127.0.0.1:8000"; then
    echo "❌ バックエンド問題: 127.0.0.1:8000でバインド"
    echo "   Windows Chromeからアクセス不可"
    BACKEND_OK=false
else
    echo "❌ バックエンドが起動していません"
    BACKEND_OK=false
fi

# 2. フロントエンドポートバインディング確認
echo "📡 フロントエンドポートバインディング確認..."
FRONTEND_BIND=$(ss -tulnp | grep :3000 | head -1)

if echo "$FRONTEND_BIND" | grep -q "\*:3000"; then
    echo "✅ フロントエンド正常: *:3000でバインド"
    FRONTEND_OK=true
else
    echo "❌ フロントエンドポートバインディング異常"
    FRONTEND_OK=false
fi

# 3. WSL IPアドレス確認
echo "🔍 WSL IPアドレス確認..."
WSL_IP=$(hostname -I | awk '{print $1}')
echo "   WSL IP: $WSL_IP"

# 4. アクセステスト
echo "🧪 アクセステスト実行..."

# バックエンドテスト
if curl -s --max-time 3 http://localhost:8000/api/v1/projects/ > /dev/null 2>&1; then
    echo "✅ バックエンドWSL内アクセス: OK"
else
    echo "❌ バックエンドWSL内アクセス: 失敗"
fi

# フロントエンドテスト
if curl -s --max-time 3 http://localhost:3000 > /dev/null 2>&1; then
    echo "✅ フロントエンドWSL内アクセス: OK"
else
    echo "❌ フロントエンドWSL内アクセス: 失敗"
fi

# 5. 修正提案
echo ""
echo "📋 チェック結果サマリー:"

if [ "$BACKEND_OK" = true ] && [ "$FRONTEND_OK" = true ]; then
    echo "✅ すべて正常 - WSL2とWindows Chrome両方からアクセス可能"
    echo ""
    echo "🌐 アクセスURL:"
    echo "   WSL Firefox:    http://localhost:3000"
    echo "   Windows Chrome: http://localhost:3000 または http://$WSL_IP:3000"
    exit 0
else
    echo "❌ 問題が検出されました"
    echo ""
    echo "🔧 修正方法:"
    
    if [ "$BACKEND_OK" = false ]; then
        echo "  1. バックエンドを正しく起動:"
        echo "     cd $PROJECT_ROOT/app/backend"
        echo "     source venv/bin/activate"
        echo "     python manage.py runserver_wsl"
        echo ""
        echo "  または起動スクリプト使用:"
        echo "     $PROJECT_ROOT/restart-backend.sh"
    fi
    
    if [ "$FRONTEND_OK" = false ]; then
        echo "  2. フロントエンド再起動:"
        echo "     cd $PROJECT_ROOT/app/frontend"
        echo "     npm run dev"
    fi
    
    echo ""
    echo "📖 詳細情報: $PROJECT_ROOT/CLAUDE_INSTRUCTIONS/wsl2_network_setup.md"
    exit 1
fi