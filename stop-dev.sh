#!/bin/bash

# StatVizForge開発環境停止スクリプト

PROJECT_ROOT="/home/futaro/project/StatVizForge_JikkenPy"

echo "🛑 StatVizForge開発環境を停止中..."

# PIDファイルから停止
if [ -f "$PROJECT_ROOT/.backend.pid" ]; then
    BACKEND_PID=$(cat "$PROJECT_ROOT/.backend.pid")
    if kill -0 $BACKEND_PID 2>/dev/null; then
        kill $BACKEND_PID
        echo "Djangoサーバー停止 (PID: $BACKEND_PID)"
    fi
    rm -f "$PROJECT_ROOT/.backend.pid"
fi

if [ -f "$PROJECT_ROOT/.frontend.pid" ]; then
    FRONTEND_PID=$(cat "$PROJECT_ROOT/.frontend.pid")
    if kill -0 $FRONTEND_PID 2>/dev/null; then
        kill $FRONTEND_PID
        echo "Next.jsサーバー停止 (PID: $FRONTEND_PID)"
    fi
    rm -f "$PROJECT_ROOT/.frontend.pid"
    rm -f "$PROJECT_ROOT/.frontend.port"
fi

# 念のため強制停止
pkill -f "manage.py runserver" 2>/dev/null
pkill -f "next dev" 2>/dev/null

echo "✅ 開発環境停止完了"