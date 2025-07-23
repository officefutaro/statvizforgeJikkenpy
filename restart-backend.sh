#!/bin/bash

# バックエンド単体再起動スクリプト
# Claude Codeが必要時に実行

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
BACKEND_DIR="$PROJECT_ROOT/app/backend"

echo "🔄 Djangoバックエンドを再起動中..."

# 既存のバックエンドプロセス停止
if [ -f "$PROJECT_ROOT/.backend.pid" ]; then
    BACKEND_PID=$(cat "$PROJECT_ROOT/.backend.pid")
    if kill -0 $BACKEND_PID 2>/dev/null; then
        kill $BACKEND_PID
        echo "既存Djangoサーバー停止 (PID: $BACKEND_PID)"
        sleep 2
    fi
fi

pkill -f "manage.py runserver" 2>/dev/null
sleep 1

# バックエンド再起動
cd "$BACKEND_DIR"
source venv/bin/activate

BACKEND_LOG="$PROJECT_ROOT/logs/backend.log"
mkdir -p "$PROJECT_ROOT/logs"

nohup python manage.py runserver 0.0.0.0:8000 > "$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!
echo "$BACKEND_PID" > "$PROJECT_ROOT/.backend.pid"

echo "⏳ バックエンド起動確認中..."
sleep 3

if curl -s http://localhost:8000/api/projects/list > /dev/null; then
    echo "✅ バックエンド再起動完了 (PID: $BACKEND_PID)"
else
    echo "❌ バックエンド再起動失敗"
    exit 1
fi