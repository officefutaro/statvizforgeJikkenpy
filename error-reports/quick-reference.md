# エラー報告クイックリファレンス

## 📸 Windowsからの保存（シンプル！）

### エクスプローラーでアクセス
```
\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\
```

**保存場所は1箇所だけ！** 全てのスクリーンショットを上記フォルダに保存してください。

## 📝 ファイル名の付け方

```
20250802_143022_login-button-broken.png
20250802_143055_api-timeout-error.png
20250802_143112_modal-not-opening.png
```

**形式**: `YYYYMMDD_HHMMSS_[問題の説明].png`

## 🤖 ClaudeCodeへの相談方法

### 基本形式
```
「error-reports/screenshots/[ファイル名] のエラーを解決してください」

状況：
- [何をしようとしていたか]
- [どんなエラーが発生したか]
- [いつから発生しているか]
```

### 相談例
```
「error-reports/screenshots/20250802_143022_project-error.png を見てください。

プロジェクト作成時にこのエラーが発生します。
昨日まで正常に動作していました。」
```

## ⚡ メリット

- **手間なし**: フォルダ分類不要、一箇所に保存だけ
- **AI分析**: ClaudeCodeが文脈から自動でエラー分析
- **効率化**: 迅速なバグ報告と解決

## 🎯 ClaudeCodeが自動判断

- エラーの種類（フロントエンド/バックエンド/UI等）
- 重要度（Critical/High/Medium/Low）  
- 原因の推定
- 解決手順の提案