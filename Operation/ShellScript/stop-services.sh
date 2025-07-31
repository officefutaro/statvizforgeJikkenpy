#!/bin/bash

# バックエンド・フロントエンドのバックグラウンドプロセスを終了するスクリプト

echo "バックエンド・フロントエンドサービスを停止しています..."

# バックエンドの停止
backend_pids=$(ps aux | grep -E 'python.*manage.py runserver|gunicorn' | grep -v grep | awk '{print $2}')
if [ ! -z "$backend_pids" ]; then
    echo "バックエンドプロセスを停止中..."
    echo "$backend_pids" | xargs kill -9 2>/dev/null
    echo "バックエンドが停止しました"
else
    echo "バックエンドプロセスが見つかりません"
fi

# フロントエンドの停止
frontend_pids=$(ps aux | grep -E 'node.*next|npm run dev|npm run start' | grep -v grep | awk '{print $2}')
if [ ! -z "$frontend_pids" ]; then
    echo "フロントエンドプロセスを停止中..."
    echo "$frontend_pids" | xargs kill -9 2>/dev/null
    echo "フロントエンドが停止しました"
else
    echo "フロントエンドプロセスが見つかりません"
fi

echo "全てのサービスが停止しました"