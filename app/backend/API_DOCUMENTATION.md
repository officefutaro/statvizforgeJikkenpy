# StatVizForge API Documentation

## 概要
StatVizForge APIは、プロジェクト管理とファイル操作を提供するRESTful APIです。
クリーンアップされ、一貫性のある設計により、プロジェクトライフサイクル全体をサポートします。

## ベースURL
```
# バックエンド直接アクセス
http://localhost:8000/api/

# フロントエンドAPIプロキシ経由（推奨）
http://localhost:3000/api/
```

## フロントエンドAPIプロキシ
フロントエンドはNext.js APIルートを使用してバックエンドAPIへのプロキシを提供します：

### 利用可能なプロキシエンドポイント:
- `/api/projects/` - プロジェクト管理
- `/api/files/[...slug]` - ファイル管理（動的ルーティング）
- `/api/server-info/` - サーバー情報

### プロキシの特徴:
- 自動的なタイムアウト処理（8秒）
- エラーレスポンスの正規化
- FormDataとJSONの両方をサポート
- バックエンド接続失敗時のフォールバック

### JupyterLab APIプロキシ ❌ **未実装**
JupyterLab関係のAPIは現在プロキシ経由でアクセスできません。

## 認証
現在は認証不要（開発環境）

## レスポンス形式
- 成功: JSON形式
- エラー: 多言語対応エラーメッセージ（日本語/英語）

---

## プロジェクト管理 API

### 1. プロジェクト一覧取得
```http
GET /api/projects/
```

**レスポンス例:**
```json
{
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:00:00",
  "projects": [
    {
      "id": "uuid-string",
      "folder_name": "my_project",
      "project_name": "My Project",
      "description": "Project description",
      "tags": ["tag1", "tag2"],
      "status": "active",
      "created_date": "2025-07-27T10:00:00",
      "modified_date": "2025-07-27T10:00:00"
    }
  ]
}
```

### 2. プロジェクト作成
```http
POST /api/projects/
```

**リクエスト例:**
```json
{
  "folder_name": "new_project",
  "project_name": "New Project",
  "description": "Project description",
  "tags": ["analysis", "demo"],
  "status": "active"
}
```

**レスポンス:** `201 Created` + 作成されたプロジェクト情報

### 3. プロジェクト詳細取得
```http
GET /api/projects/{id}/
```

### 4. プロジェクト更新
```http
PUT /api/projects/{id}/
```

**リクエスト例:**
```json
{
  "project_name": "Updated Project Name",
  "description": "Updated description"
}
```

### 5. プロジェクト削除（アーカイブ）
```http
DELETE /api/projects/{id}/
```
- プロジェクトフォルダをZIPアーカイブしてtrashに移動
- レスポンス: `204 No Content`

### 6. 削除済みプロジェクト一覧
```http
GET /api/projects/deleted/
```

### 7. プロジェクト復元
```http
POST /api/projects/{id}/restore/
```

---

## ファイル管理 API

### 1. ディレクトリツリー取得
```http
GET /api/files/tree/{project_folder}
```

**レスポンス例:**
```json
{
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 1024,
      "modified": "2025-07-27T10:00:00",
      "comment_count": 2,
      "has_comments": true,
      "children": []
    }
  ]
}
```

### 2. ファイルアップロード
```http
POST /api/files/upload/{project_folder}
```

**リクエスト:** `multipart/form-data`
- `files`: アップロードするファイル（複数可）
- `target_path`: アップロード先パス（オプション）

**レスポンス例:**
```json
{
  "success": true,
  "uploaded_files": [
    {
      "name": "data.csv",
      "path": "data.csv",
      "size": 1024,
      "uploaded": "2025-07-27T10:00:00",
      "mime_type": "text/csv"
    }
  ],
  "success_count": 1,
  "error_count": 0
}
```

### 3. ファイル検索
```http
GET /api/files/search/{project_folder}?q={query}&type={search_type}
```

**パラメータ:**
- `q`: 検索クエリ（必須）
- `type`: 検索タイプ（`name`, `content`, `both`）

**レスポンス例:**
```json
{
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 2,
  "results": [
    {
      "name": "test.py",
      "path": "scripts/test.py",
      "type": "file",
      "size": 500,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": "scripts",
      "comment_count": 1,
      "has_comments": true,
      "matched_lines": [
        {
          "line_number": 5,
          "content": "def test_function():"
        }
      ]
    }
  ]
}
```

### 4. ファイル/ディレクトリ削除
```http
DELETE /api/files/delete/{project_folder}
```

**リクエスト例:**
```json
{
  "file_path": "data/old_file.csv"
}
```

### 5. ファイル/ディレクトリ移動
```http
POST /api/files/move/{project_folder}
```

**リクエスト例:**
```json
{
  "source_path": "data.csv",
  "destination_path": "processed/data.csv"
}
```

### 6. ディレクトリ作成
```http
POST /api/files/mkdir/{project_folder}
```

**リクエスト例:**
```json
{
  "dir_path": "new_folder/subfolder"
}
```

---

## JupyterLab 管理 API

### 1. JupyterLab起動
```http
POST /api/jupyter/start/
```

**リクエスト例:**
```json
{
  "project_folder": "my_project"
}
```

**レスポンス例:**
```json
{
  "success": true,
  "url": "http://localhost:8888/?token=abc123",
  "port": 8888,
  "token": "abc123def456",
  "message": "JupyterLab started successfully",
  "project_folder": "my_project"
}
```

### 2. JupyterLab停止
```http
POST /api/jupyter/stop/
```

**リクエスト例:**
```json
{
  "project_folder": "my_project"
}
```

**レスポンス例:**
```json
{
  "success": true,
  "message": "JupyterLab stopped successfully",
  "project_folder": "my_project"
}
```

### 3. JupyterLab状態確認
```http
GET /api/jupyter/status/
```

**クエリパラメータ:**
- `project_folder`: プロジェクトフォルダ名（オプション）

**レスポンス例:**
```json
{
  "success": true,
  "running_instances": [
    {
      "project_folder": "my_project",
      "url": "http://localhost:8888/?token=abc123",
      "port": 8888,
      "token": "abc123def456",
      "status": "running",
      "pid": 12345,
      "started_at": "2025-07-28T10:00:00"
    }
  ]
}
```

**注意:**
- JupyterLabは分離された仮想環境で実行されます
- プロジェクトごとに独立したインスタンスが起動します
- トークンベースの認証が使用されます

---

## ファイルタグ API

### 1. ファイルタグ保存・更新 ❌ **未実装**
```http
POST /api/files/tags/{project_folder}
```

**リクエスト例:**
```json
{
  "file_path": "data/analysis.csv",
  "tags": ["分析データ", "項目データ"]
}
```

**レスポンス例:**
```json
{
  "success": true,
  "file_path": "data/analysis.csv",
  "tags": ["分析データ", "項目データ"],
  "updated": "2025-07-28T10:00:00"
}
```

### 2. ファイルタグ取得 ❌ **未実装**
```http
GET /api/files/tags/{project_folder}?file_path={file_path}
```

### 3. 全ファイルタグ取得 ❌ **未実装**
```http
GET /api/files/tags/{project_folder}
```

### 4. タグによるファイル検索 ❌ **未実装**
```http
GET /api/files/search-by-tags/{project_folder}?tags={tag1,tag2}
```

**利用可能なタグ:**
- `分析データ` (Analysis Data) - プライマリタグ
- `項目データ` (Item Data) - セカンダリタグ（分析データタグが設定されている場合のみ選択可能）

**タグルール:**
- `分析データ`タグが設定されている場合のみ、`項目データ`タグを追加可能
- タグは重複不可
- 1つのファイルに対して複数のタグを設定可能

---

## ファイルコメント API

### 1. ファイルコメント取得
```http
GET /api/files/comments/{project_folder}?file_path={file_path}
```

### 2. 全コメント取得
```http
GET /api/files/comments/{project_folder}
```

### 3. コメント追加
```http
POST /api/files/comments/{project_folder}
```

**リクエスト例:**
```json
{
  "file_path": "data.csv",
  "comment": "This file contains customer data",
  "author": "Data Analyst"
}
```

### 4. コメント更新
```http
PUT /api/files/comments/{project_folder}/{comment_id}
```

**リクエスト例:**
```json
{
  "file_path": "data.csv",
  "comment": "Updated comment text"
}
```

### 5. コメント削除
```http
DELETE /api/files/comments/{project_folder}/{comment_id}?file_path={file_path}
```

---

## システム API

### サーバー情報取得
```http
GET /api/server-info/
```

**レスポンス例:**
```json
{
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
```

---

## エラーレスポンス

### 形式
```json
{
  "error": "ERROR_CODE",
  "message": "Human readable message in requested language",
  "details": {
    "field_name": "Validation error details"
  }
}
```

### 主なエラーコード
- `PROJECT_NOT_FOUND`: プロジェクトが見つからない
- `DUPLICATE_FOLDER`: フォルダ名重複
- `VALIDATION_ERROR`: バリデーションエラー
- `SEARCH_QUERY_REQUIRED`: 検索クエリが必要
- `FILE_PATH_REQUIRED`: ファイルパスが必要
- `UPLOAD_FAILED`: アップロード失敗
- `TAG_VALIDATION_ERROR`: タグバリデーションエラー
- `INVALID_TAG_COMBINATION`: 無効なタグ組み合わせ（項目データタグは分析データタグが必要）
- `DUPLICATE_TAG`: 重複タグエラー

---

## 言語サポート
APIは多言語エラーメッセージをサポートします。

**言語指定方法:**
- クエリパラメータ: `?lang=ja` または `?lang=en`
- HTTPヘッダー: `Accept-Language: ja` または `Accept-Language: en`

---

## テスト

### テスト実行
```bash
cd /app/backend
python run_tests.py
```

### 個別テスト実行
```bash
python manage.py test api.tests.ProjectLifecycleTestCase
python manage.py test api.tests.FileManagementTestCase
python manage.py test api.tests.FileCommentsTestCase
```

---

## 実装状況と今後の予定

### ✅ 実装済み (Backend + Frontend)
- プロジェクト管理API（CRUD操作）
- ファイル管理API（ツリー、アップロード、検索、削除、移動、ディレクトリ作成）
- ファイルコメントAPI（CRUD操作）
- JupyterLab管理API（起動、停止、状態確認）
- サーバー情報API
- フロントエンドAPIプロキシ（プロジェクト、ファイル、サーバー情報）

### ❌ フロントエンド実装済み・バックエンド未実装
- ファイルタグAPI（保存、取得、検索）
- ファイル説明保存API（現在は comment として実装）

### ❌ 今後の実装予定
- JupyterLab APIプロキシ（フロントエンド）
- プロジェクト実行API（実行開始、停止、ログ取得）
- ファイル内容編集API
- プロジェクトテンプレート管理API
- ユーザー認証API
- プロジェクト共有・コラボレーション機能

### 🔧 改善が必要な項目
- エラーハンドリングの統一
- レスポンス形式の一貫性向上
- パフォーマンス最適化
- セキュリティ強化

---

## バックエンド実装チェックリスト

### 緊急実装が必要:
1. **ファイルタグAPI** - フロントエンドが既に実装済み
   - `POST /api/files/tags/{project_folder}`
   - `GET /api/files/tags/{project_folder}`
   - `GET /api/files/search-by-tags/{project_folder}`

2. **JupyterLab APIプロキシ** - フロントエンドからの直接アクセスが必要
   - `/api/jupyter/[...slug]` プロキシルート

### 中期実装予定:
1. プロジェクト実行管理API
2. ファイル内容編集API  
3. より詳細なエラーレスポンス

---

## 変更履歴

### v1.2.0 (2025-07-28)
- ✅ ファイルタグ機能追加
- ✅ 条件付きタグ選択機能（分析データ→項目データ）
- ✅ タグによるファイル検索機能
- ✅ プロジェクト詳細表示パネル実装
- ✅ 左右パネル切り替え機能

### v1.1.0 (2025-07-27)
- ✅ レガシーエンドポイント削除
- ✅ 未実装エンドポイント削除
- ✅ API命名規則統一
- ✅ ファイル検索機能追加
- ✅ 包括的テストスイート作成

### v1.0.0
- 基本的なプロジェクト管理機能
- ファイルアップロード機能
- コメント機能