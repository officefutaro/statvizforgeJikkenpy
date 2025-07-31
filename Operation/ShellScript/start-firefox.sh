#!/bin/bash

# FireFoxをバックグラウンドで起動するスクリプト

echo "FireFoxをバックグラウンドで起動しています..."

# FireFoxがインストールされているか確認
if ! command -v firefox &> /dev/null; then
    echo "エラー: FireFoxがインストールされていません"
    exit 1
fi

# FireFoxをバックグラウンドで起動
nohup firefox > /dev/null 2>&1 &
FIREFOX_PID=$!

echo "FireFoxが起動しました (PID: $FIREFOX_PID)"

# オプション: 特定のURLで起動する場合は以下のコメントを解除
# nohup firefox "http://localhost:3000" > /dev/null 2>&1 &

# PIDをファイルに保存（停止時に使用）
echo "$FIREFOX_PID" > "$HOME/.firefox.pid"