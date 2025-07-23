#!/bin/bash

# フロントエンド単体再起動スクリプト
# Claude Codeが必要時に実行

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
FRONTEND_DIR="$PROJECT_ROOT/app/frontend"

echo "🔄 Next.jsフロントエンドを再起動中..."

# 既存のフロントエンドプロセス停止
if [ -f "$PROJECT_ROOT/.frontend.pid" ]; then
    FRONTEND_PID=$(cat "$PROJECT_ROOT/.frontend.pid")
    if kill -0 $FRONTEND_PID 2>/dev/null; then
        kill $FRONTEND_PID
        echo "既存Next.jsサーバー停止 (PID: $FRONTEND_PID)"
        sleep 2
    fi
fi

pkill -f "next dev" 2>/dev/null
sleep 1

# フロントエンド再起動
cd "$FRONTEND_DIR"

FRONTEND_LOG="$PROJECT_ROOT/logs/frontend.log"
mkdir -p "$PROJECT_ROOT/logs"

nohup npm run dev > "$FRONTEND_LOG" 2>&1 &
FRONTEND_PID=$!
echo "$FRONTEND_PID" > "$PROJECT_ROOT/.frontend.pid"

echo "⏳ フロントエンド起動確認中..."
sleep 5

# ポート確認
FRONTEND_PORT=""
for port in 3000 3001 3002; do
    if curl -s http://localhost:$port > /dev/null 2>&1; then
        FRONTEND_PORT=$port
        break
    fi
done

if [ -n "$FRONTEND_PORT" ]; then
    echo "✅ フロントエンド再起動完了 (PID: $FRONTEND_PID, Port: $FRONTEND_PORT)"
    echo "$FRONTEND_PORT" > "$PROJECT_ROOT/.frontend.port"
else
    echo "❌ フロントエンド再起動失敗"
    exit 1
fi