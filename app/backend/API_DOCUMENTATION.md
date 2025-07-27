# StatVizForge API Documentation

## 概要
StatVizForge APIは、プロジェクト管理とファイル操作を提供するRESTful APIです。
クリーンアップされ、一貫性のある設計により、プロジェクトライフサイクル全体をサポートします。

## ベースURL
```
http://localhost:8000/api/
```

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

## 変更履歴

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