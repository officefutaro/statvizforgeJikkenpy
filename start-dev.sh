#!/bin/bash

# StatVizForge開発環境起動スクリプト
# Claude Code起動時に自動実行される

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
BACKEND_DIR="$PROJECT_ROOT/app/backend"
FRONTEND_DIR="$PROJECT_ROOT/app/frontend"

echo "🚀 StatVizForge開発環境を起動中..."

# 既存のプロセスを確認・停止
echo "📋 既存プロセスをチェック中..."
pkill -f "manage.py runserver" 2>/dev/null
pkill -f "next dev" 2>/dev/null
sleep 2

# バックエンド起動
echo "🔧 Djangoバックエンドを起動中..."
cd "$BACKEND_DIR"
if [ ! -d "venv" ]; then
    echo "仮想環境を作成中..."
    python3 -m venv venv
    source venv/bin/activate
    pip install django djangorestframework django-cors-headers
else
    source venv/bin/activate
fi

# バックエンドログファイル
BACKEND_LOG="$PROJECT_ROOT/logs/backend.log"
mkdir -p "$PROJECT_ROOT/logs"

# Django開発サーバー起動（WSL2対応）
nohup python manage.py runserver_wsl > "$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!
echo "Djangoサーバー起動 (PID: $BACKEND_PID) - ログ: $BACKEND_LOG"

# フロントエンド起動
echo "⚛️  Next.jsフロントエンドを起動中..."
cd "$FRONTEND_DIR"

# フロントエンドログファイル
FRONTEND_LOG="$PROJECT_ROOT/logs/frontend.log"

# Next.js開発サーバー起動
nohup npm run dev > "$FRONTEND_LOG" 2>&1 &
FRONTEND_PID=$!
echo "Next.jsサーバー起動 (PID: $FRONTEND_PID) - ログ: $FRONTEND_LOG"

# PIDファイルに保存
echo "$BACKEND_PID" > "$PROJECT_ROOT/.backend.pid"
echo "$FRONTEND_PID" > "$PROJECT_ROOT/.frontend.pid"

# サーバー起動確認
echo "⏳ サーバー起動を確認中..."
sleep 5

# バックエンド確認
if curl -s http://localhost:8000/api/projects/list > /dev/null; then
    echo "✅ バックエンド正常起動 (http://localhost:8000)"
else
    echo "❌ バックエンド起動失敗"
fi

# フロントエンド確認（ポート3000、3001、3002を順次確認）
FRONTEND_PORT=""
for port in 3000 3001 3002; do
    if curl -s http://localhost:$port > /dev/null 2>&1; then
        FRONTEND_PORT=$port
        break
    fi
done

if [ -n "$FRONTEND_PORT" ]; then
    echo "✅ フロントエンド正常起動 (http://localhost:$FRONTEND_PORT)"
    echo "$FRONTEND_PORT" > "$PROJECT_ROOT/.frontend.port"
else
    echo "❌ フロントエンド起動失敗"
fi

echo ""
echo "🎉 開発環境起動完了!"
echo "📊 バックエンド: http://localhost:8000"
echo "🌐 フロントエンド: http://localhost:${FRONTEND_PORT:-3000}"
echo "📝 ログ確認: tail -f $PROJECT_ROOT/logs/*.log"
echo ""
echo "停止するには: ./stop-dev.sh を実行"