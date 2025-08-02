# エラースクリーンショット管理システム

## 🎯 目的
ClaudeCodeにエラー画面を効率的に共有するための専用管理システム

## ✨ 特徴
- **即座保存**: Win+Shift+E で3秒以内に分類保存
- **体系的管理**: エラー種別・日時で自動整理
- **開発者フレンドリー**: 一目でエラー内容が分かるフォルダ構造
- **StatVizForgeから独立**: 開発プロジェクトと完全分離

## 📁 保存場所
```
WSL側: /home/futaro/screenshots/errors/
Windows側: \\wsl$\Ubuntu\home\futaro\screenshots\errors\
```

## 🚀 セットアップ
1. PowerShellを管理者権限で実行
2. `.\setup.ps1` を実行
3. デスクトップのショートカットからAutoHotkeyスクリプト起動

## ⌨️ 使い方

### 基本操作
1. **エラー発生** → スクリーンショット取得（PrintScreen等）
2. **Win+Shift+E** → カテゴリ選択メニュー表示
3. **数字キー(1-6)** または **マウスクリック** → 保存完了

### ショートカット一覧
| キー | 動作 |
|------|------|
| Win+Shift+E | カテゴリ選択して保存 |
| Ctrl+Shift+E | 前回カテゴリで即保存 |
| Win+Alt+E | 今日のエラー一覧を開く |

### カテゴリ
1. **API Error** - 404, 500, CORS等のAPI関連
2. **Build Error** - npm run build等のビルドエラー
3. **Runtime Error** - 実行時の例外・エラー
4. **UI Bug** - レイアウト崩れ、表示不具合
5. **Test Failure** - テスト失敗
6. **Other** - その他のエラー

## 📂 フォルダ構造例
```
2025-08-01/
├── 09-45-23_API_ERROR/
│   ├── screenshot.png      # エラー画面
│   ├── context.txt        # 発生状況
│   └── README.md          # 詳細説明
├── 14-22-15_BUILD_ERROR/
│   └── ...
└── index.md               # その日の一覧
```

## 🔍 ClaudeCodeへの共有方法
1. エラーフォルダを開く（Win+Alt+E）
2. 該当エラーのscreenshot.pngを選択
3. ClaudeCodeにドラッグ＆ドロップ
4. 必要に応じてcontext.txtの内容も貼り付け

## 💡 Tips
- **連続エラー**: Ctrl+Shift+Eで同じカテゴリに素早く保存
- **一括確認**: その日のindex.mdで全エラーを俯瞰
- **履歴管理**: 日付フォルダで過去のエラーも参照可能

## ⚙️ カスタマイズ
`error_screenshot_manager.ahk`を編集して：
- ホットキー変更
- カテゴリ追加
- 保存先変更

---
開発効率を最大化するエラー管理を実現します！