# バックエンドサーバー起動ガイド

## 概要
StatVizForgeのDjangoバックエンドサーバーを起動する手順です。

## 前提条件
- Python 3.12がインストールされている
- 仮想環境がセットアップ済み（`app/backend/venv`）
- 依存関係がインストール済み

## 起動手順

### 1. 新しいターミナルを開く
現在の作業とは別に、新しいターミナルウィンドウまたはタブを開いてください。

### 2. バックエンドディレクトリに移動
```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
```

### 3. 仮想環境を有効化
```bash
source venv/bin/activate
```

**確認**: プロンプトに`(venv)`が表示されることを確認してください
```
(venv) user@hostname:~/project/StatVizForge_JikkenPy/app/backend$
```

### 4. Django開発サーバーを起動
```bash
python manage.py runserver 0.0.0.0:8000
```

## 正常起動時の出力例

```
Starting archive cleanup...
No trash-registry.json found, skipping cleanup.
Archive cleanup completed. Deleted 0 expired archives.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 26, 2025 - 14:48:00
Django version 5.2.4, using settings 'config.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

## 動作確認

サーバー起動後、別のターミナルで以下のコマンドを実行して動作確認できます：

### 基本APIテスト
```bash
# サーバー情報取得
curl http://172.24.67.130:8000/api/server-info/

# プロジェクト一覧取得（RESTful エンドポイント）
curl http://172.24.67.130:8000/api/projects/

# 削除済みプロジェクト一覧テスト（RESTful エンドポイント）  
curl http://172.24.67.130:8000/api/projects/deleted/

# 旧エンドポイントでのテスト（後方互換性確認）
curl http://172.24.67.130:8000/api/projects/list
curl http://172.24.67.130:8000/api/projects/archived
```

### 期待されるレスポンス

#### サーバー情報（`/api/server-info/`）
```json
{
  "debug_mode": true,
  "environment": "development", 
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
```

#### プロジェクト一覧（`/api/projects/` または `/api/projects/list`）
```json
{
  "version": "1.0.0",
  "last_updated": "2025-07-26T...",
  "projects": [...]
}
```

#### 削除済み一覧（`/api/projects/deleted/` または `/api/projects/archived`）
```json
{
  "version": "1.0.0", 
  "deleted_projects": [...],
  "last_updated": "2025-07-26T..."
}
```

## 利用可能なAPIエンドポイント

### RESTful エンドポイント（推奨）

| メソッド | エンドポイント | 説明 | 実装状況 |
|---------|---------------|------|----------|
| GET | `/api/projects/` | プロジェクト一覧取得 | ✅ |
| POST | `/api/projects/` | プロジェクト作成 | ✅ |
| GET | `/api/projects/deleted/` | 削除済み一覧 | ✅ |
| GET | `/api/projects/{uuid}/` | プロジェクト詳細 | ✅ |
| PUT | `/api/projects/{uuid}/` | プロジェクト更新 | ✅ |
| DELETE | `/api/projects/{uuid}/` | プロジェクト削除 | ✅ |
| POST | `/api/projects/{uuid}/restore/` | プロジェクト復元 | ✅ |
| GET | `/api/server-info/` | サーバー情報 | ✅ |

### 旧エンドポイント（後方互換性）

| メソッド | エンドポイント | 説明 | 実装状況 |
|---------|---------------|------|----------|
| GET | `/api/projects/list` | プロジェクト一覧取得 | ✅ (非推奨) |
| POST | `/api/projects/create` | プロジェクト作成 | ✅ (非推奨) |
| GET | `/api/projects/archived` | 削除済み一覧 | ✅ (非推奨) |

## トラブルシューティング

### 仮想環境が見つからない場合
```bash
# 仮想環境を再作成
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ポート8000が使用中の場合
```bash
# 別のポートで起動
python manage.py runserver 0.0.0.0:8001

# または使用中のプロセスを確認
lsof -i :8000
```

### マイグレーションエラーの場合
```bash
# マイグレーション実行
python manage.py migrate
```

### パッケージが見つからない場合
```bash
# 依存関係を再インストール
pip install -r requirements.txt
```

## サーバーの停止

サーバーを停止するには、サーバーが動いているターミナルで：
```
Ctrl + C
```

## ログの確認

エラーログは以下で確認できます：
```bash
tail -f /home/futaro/project/StatVizForge_JikkenPy/app/backend/django.log
```

## 開発時の注意事項

1. **ファイル変更の自動リロード**: 
   - コードを変更すると自動的にサーバーがリロードされます
   - `Watching for file changes with StatReloader`が表示されている場合は正常です

2. **CORS設定**:
   - 開発環境では全オリジンを許可しています
   - フロントエンド（React）からのリクエストが正常に処理されます

3. **データベース**:
   - SQLiteを使用（`db.sqlite3`）
   - プロジェクトデータは`~/project/projects-registry.json`で管理

4. **削除されたプロジェクト**:
   - `~/project/trash/`フォルダにZIPアーカイブとして保存
   - `trash-registry.json`で管理

## アップデート履歴

| 日付 | バージョン | 変更内容 |
|------|-----------|---------|
| 2025-07-26 | 1.0.0 | 初版作成 |
| 2025-07-26 | 1.1.0 | URLパターン修正（UUID対応）、復元API追加 |
| 2025-07-26 | 1.2.0 | RESTful設計への統一、用語統一（archived→deleted）、後方互換性維持 |

---

**重要**: このガイドの手順に従ってバックエンドサーバーを起動してから、フロントエンドでプロジェクトの削除・復元機能をテストしてください。