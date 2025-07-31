#!/bin/bash

# バックエンド・フロントエンドをバックグラウンドで起動するスクリプト

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"
BACKEND_DIR="$PROJECT_ROOT/app/backend"
FRONTEND_DIR="$PROJECT_ROOT/app/frontend"

echo "バックエンド・フロントエンドサービスを起動しています..."

# バックエンドの起動
echo "バックエンドを起動中..."
cd "$BACKEND_DIR"

# 仮想環境をアクティベート
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# バックエンドをバックグラウンドで起動（WSL2対応）
nohup python manage.py runserver_wsl > "$PROJECT_ROOT/logs/backend.log" 2>&1 &
BACKEND_PID=$!
echo "バックエンドが起動しました (PID: $BACKEND_PID)"

# フロントエンドの起動
echo "フロントエンドを起動中..."
cd "$FRONTEND_DIR"

# フロントエンドをバックグラウンドで起動
nohup npm run dev > "$PROJECT_ROOT/logs/frontend.log" 2>&1 &
FRONTEND_PID=$!
echo "フロントエンドが起動しました (PID: $FRONTEND_PID)"

# PIDをファイルに保存（停止時に使用）
echo "$BACKEND_PID" > "$PROJECT_ROOT/.backend.pid"
echo "$FRONTEND_PID" > "$PROJECT_ROOT/.frontend.pid"

echo "全てのサービスが起動しました"
echo "バックエンド: http://localhost:8000"
echo "フロントエンド: http://localhost:3000"