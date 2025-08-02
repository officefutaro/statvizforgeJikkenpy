#!/bin/bash
# ===============================================
# エラースクリーンショット管理システム
# WSL側セットアップスクリプト
# ===============================================

echo "エラースクリーンショット管理システムのセットアップを開始します..."

# 基本ディレクトリ作成
BASE_DIR="/home/futaro/screenshots/errors"
CATEGORIES_DIR="$BASE_DIR/categories"

echo "ディレクトリ構造を作成中..."

# メインディレクトリ
mkdir -p "$BASE_DIR"
mkdir -p "$CATEGORIES_DIR"

# カテゴリディレクトリ
categories=(
    "API_ERRORS"
    "BUILD_ERRORS"
    "RUNTIME_ERRORS"
    "UI_BUGS"
    "TEST_FAILURES"
    "OTHER"
)

for category in "${categories[@]}"; do
    mkdir -p "$CATEGORIES_DIR/$category"
done

# README.md作成
cat > "$BASE_DIR/README.md" << 'EOF'
# エラースクリーンショット管理システム (WSL版)

## 概要
ClaudeCodeとの連携用にエラー画面を体系的に保存・管理するシステムです。

## 保存場所
- WSL側: `/home/futaro/screenshots/errors/`
- Windows側からのアクセス: `\\wsl$\Ubuntu\home\futaro\screenshots\errors\`

## ディレクトリ構造
```
errors/
├── 2025-08-01/                    # 日付別
│   ├── 09-45-23_API_ERROR/       # 時刻_エラー種別
│   │   ├── screenshot.png        # エラー画面
│   │   ├── context.txt          # 発生状況
│   │   └── README.md            # 詳細説明
│   └── index.md                 # その日の一覧
└── categories/                  # カテゴリ別（将来の拡張用）
```

## 使用方法

### Windows側（AutoHotkey）から
1. エラー画面をスクリーンショット（PrintScreen等）
2. Win+Shift+E でカテゴリ選択
3. 数字キー（1-6）で保存

### ClaudeCodeへの共有
1. Win+Alt+E で今日のエラーフォルダを開く
2. 該当のscreenshot.pngをドラッグ＆ドロップ
3. 必要に応じてcontext.txtも共有

## カテゴリ説明
- API_ERROR: API通信関連（404, 500, CORS等）
- BUILD_ERROR: ビルド・コンパイルエラー
- RUNTIME_ERROR: 実行時エラー・例外
- UI_BUG: UI表示不具合
- TEST_FAIL: テスト失敗
- OTHER: その他

---
Last Updated: $(date '+%Y-%m-%d %H:%M:%S')
EOF

# パーミッション設定
chmod -R 755 "$BASE_DIR"

echo ""
echo "✅ セットアップが完了しました！"
echo ""
echo "保存先: $BASE_DIR"
echo ""
echo "Windows側での使用:"
echo "1. error_screenshot_manager_v2.ahk を実行"
echo "2. エラー画面をスクリーンショット"
echo "3. Win+Shift+E でカテゴリ選択して保存"
echo ""
echo "アクセス方法:"
echo "- WSL: cd $BASE_DIR"
echo "- Windows Explorer: \\\\wsl$\\Ubuntu$BASE_DIR"