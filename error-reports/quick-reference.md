# エラー報告クイックリファレンス

## Windowsからの保存パス

### エクスプローラーでアクセス
```
\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\
```

## よく使うフォルダ

### フロントエンドエラー
- **重大**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\frontend\critical\`
- **高**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\frontend\high\`
- **中**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\frontend\medium\`

### バックエンドエラー  
- **重大**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\backend\critical\`
- **高**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\backend\high\`

### UIエラー
- **高**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\ui\high\`
- **中**: `\\wsl$\Ubuntu\home\futaro\project\StatVizForge_JikkenPy\error-reports\screenshots\ui\medium\`

## ファイル名の付け方

```
20250802_143022_frontend_login-button-broken.png
20250802_143055_backend_api-500-error.png
20250802_143112_ui_modal-not-opening.png
```

**形式**: `YYYYMMDD_HHMMSS_[カテゴリ]_[問題の説明].png`

## 優先度判断

- **🔴 Critical**: アプリが使えない
- **🟠 High**: 重要な機能が使えない  
- **🟡 Medium**: 一部の機能に問題
- **🟢 Low**: 見た目や軽微な問題