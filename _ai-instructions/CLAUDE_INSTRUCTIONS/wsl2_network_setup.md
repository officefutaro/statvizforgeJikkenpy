# WSL2ネットワーク設定ガイド

## 概要
WSL2環境でDjangoバックエンドをWindows Chromeからアクセス可能にするための設定とトラブルシューティング。

## 問題の背景
- **WSL2はネットワーク分離されている**ため、`127.0.0.1`バインドではWindows側からアクセス不可
- **フロントエンド(Next.js)は`*:3000`でバインド**されるため問題なし
- **バックエンド(Django)はデフォルト`127.0.0.1:8000`**でWindowsからアクセス不可

## 実装済み解決策

### 1. カスタムrunserverコマンド
**ファイル**: `app/backend/api/management/commands/runserver_wsl.py`

- 自動的に`0.0.0.0:8000`でバインド
- Windows Chrome対応を強制
- 分かりやすい警告メッセージ表示

```bash
# 使用方法
python manage.py runserver_wsl         # 自動的に0.0.0.0:8000
python manage.py runserver_wsl --force-localhost  # 127.0.0.1:8000（デバッグ用）
```

### 2. 起動スクリプト自動修正
**修正されたファイル**:
- `start-dev.sh` → `runserver_wsl`使用
- `restart-backend.sh` → `runserver_wsl`使用

### 3. Django設定追加
**ファイル**: `app/backend/config/settings.py`
```python
# WSL2対応設定
RUNSERVER_DEFAULT_ADDR = '0.0.0.0'
RUNSERVER_DEFAULT_PORT = '8000'
```

## アクセス方法

### WSL内のFirefoxから
```
http://localhost:3000  (フロントエンド)
http://localhost:8000  (バックエンド)
```

### Windows Chromeから
```
http://localhost:3000     (フロントエンド - ポートフォワーディング)
http://localhost:8000     (バックエンド - ポートフォワーディング)

または直接IPアドレス:
http://172.24.67.130:3000  (WSLのIP確認: hostname -I)
http://172.24.67.130:8000
```

## トラブルシューティング

### 1. "Request interrupted by user" エラー
**原因**: バックエンドが`127.0.0.1`でバインドされている

**確認方法**:
```bash
ss -tulnp | grep :8000
```

**正常**: `0.0.0.0:8000`でLISTEN
**異常**: `127.0.0.1:8000`でLISTEN

**解決策**:
```bash
# プロセス停止
pkill -f "manage.py runserver"

# 正しい起動
cd app/backend && source venv/bin/activate
python manage.py runserver_wsl
```

### 2. ポートフォワーディング確認
```bash
# WSL2のポートフォワーディング状況確認
netsh interface portproxy show all

# 手動でポートフォワーディング追加（通常は自動）
netsh interface portproxy add v4tov4 listenport=8000 listenaddress=0.0.0.0 connectport=8000 connectaddress=172.24.67.130
```

### 3. Windowsファイアウォール確認
Windows Defenderで以下ポートが許可されているか確認:
- TCP 3000 (フロントエンド)
- TCP 8000 (バックエンド)

## 予防策

### 1. 起動スクリプト使用の徹底
```bash
# 推奨
./start-dev.sh
./restart-backend.sh

# 非推奨（問題が再発する可能性）
python manage.py runserver  # 127.0.0.1バインドになる
```

### 2. 定期チェックコマンド
```bash
# バインドアドレス確認
ss -tulnp | grep -E ":(3000|8000)"

# 期待値:
# tcp LISTEN *:3000      (フロントエンド)
# tcp LISTEN 0.0.0.0:8000 (バックエンド)
```

### 3. 自動テストの組み込み
開発環境起動時に自動でWSL2対応チェックを実行:
- バックエンドが`0.0.0.0`でバインドされているか
- Windows側からアクセス可能か

## 開発者向けベストプラクティス

### 1. 必ずWSL2対応コマンド使用
```bash
# ✅ 正しい
python manage.py runserver_wsl

# ❌ 問題が発生する可能性
python manage.py runserver
python manage.py runserver 127.0.0.1:8000
```

### 2. ログでバインドアドレス確認
起動ログで以下を確認:
```
Starting development server at http://0.0.0.0:8000/  # ✅
Starting development server at http://127.0.0.1:8000/  # ❌
```

### 3. 両環境でテスト
- WSL Firefox でアクセステスト
- Windows Chrome でアクセステスト

## 技術的詳細

### WSL2ネットワーク仕組み
1. **WSL2は軽量仮想マシン**として動作
2. **独自のIPアドレス範囲**を持つ（例: 172.24.x.x）
3. **Windowsが自動ポートフォワーディング**を設定
4. **`0.0.0.0`バインドが必要**でWindows側からアクセス可能

### ポートバインディング詳細
```bash
# 127.0.0.1:8000 → WSL内のみアクセス可能
# 0.0.0.0:8000   → WSL内 + Windows からアクセス可能
```

---

**最終更新**: 2025年7月31日  
**対応バージョン**: WSL2, Django 5.2.4, Next.js 13.5.1