# API 仕様書

**最終更新**: 2025-07-29  
**バージョン**: 1.2.0

## 目次
1. [プロジェクト管理API](#プロジェクト管理api)
2. [ファイル管理API](#ファイル管理api)
3. [JupyterLab管理API](#jupyterlab管理api)
4. [問題点と改善案](#問題点と改善案)

---

## プロジェクト管理API

### 1. プロジェクト一覧取得
- **エンドポイント**: `GET /api/projects/`
- **機能**: プロジェクト一覧を取得
- **クエリパラメータ**: 
  - `lang`: 言語指定 (ja/en)
- **レスポンス**: projects-registry.json の内容

### 2. プロジェクト作成
- **エンドポイント**: `POST /api/projects/`
- **機能**: 新規プロジェクト作成
- **リクエストボディ**:
  ```json
  {
    "folder_name": "string",
    "project_name": "string", 
    "description": "string",
    "tags": ["string"],
    "status": "active"
  }
  ```

### 3. プロジェクト詳細取得
- **エンドポイント**: `GET /api/projects/{project_id}/`
- **機能**: 指定プロジェクトの詳細情報取得

### 4. プロジェクト更新
- **エンドポイント**: `PUT /api/projects/{project_id}/`
- **機能**: プロジェクト情報更新

### 5. プロジェクト削除
- **エンドポイント**: `DELETE /api/projects/{project_id}/`
- **機能**: プロジェクトをtrashに移動（zipアーカイブ化）

### 6. 削除済みプロジェクト一覧
- **エンドポイント**: `GET /api/projects/deleted/`
- **機能**: trash内の削除済みプロジェクト一覧取得

### 7. プロジェクト復元
- **エンドポイント**: `POST /api/projects/{project_id}/restore/`
- **機能**: trash内のプロジェクトを復元

---

## ファイル管理API

### 1. ディレクトリツリー取得
- **エンドポイント**: `GET /api/files/tree/{project_folder}/`
- **クエリパラメータ**: 
  - `path`: 取得するパス (デフォルト: ルート)
- **機能**: プロジェクト内のディレクトリ構造取得

### 2. ファイルアップロード
- **エンドポイント**: `POST /api/files/upload/{project_folder}/`
- **機能**: ファイルのアップロード
- **Content-Type**: `multipart/form-data`

### 3. ファイル検索
- **エンドポイント**: `GET /api/files/search/{project_folder}/`
- **クエリパラメータ**:
  - `q`: 検索クエリ
- **機能**: ファイル名による検索

### 4. ファイル削除
- **エンドポイント**: `DELETE /api/files/delete/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "file_path": "string"
  }
  ```

### 5. ファイル移動
- **エンドポイント**: `POST /api/files/move/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "source_path": "string",
    "target_path": "string"
  }
  ```

### 6. ディレクトリ作成
- **エンドポイント**: `POST /api/files/mkdir/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "dir_path": "string"
  }
  ```

### 7. ファイルコメント管理
#### 7.1 コメント取得
- **エンドポイント**: `GET /api/files/comments/{project_folder}/`
- **クエリパラメータ**:
  - `file_path`: ファイルパス

#### 7.2 コメント追加
- **エンドポイント**: `POST /api/files/comments/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "file_path": "string",
    "comment": "string"
  }
  ```

#### 7.3 コメント更新
- **エンドポイント**: `PUT /api/files/comments/{project_folder}/{comment_id}/`

#### 7.4 コメント削除
- **エンドポイント**: `DELETE /api/files/comments/{project_folder}/{comment_id}/`

### 8. ファイル説明管理
#### 8.1 説明取得
- **エンドポイント**: `GET /api/files/descriptions/{project_folder}/`
- **クエリパラメータ**:
  - `file_path`: ファイルパス

#### 8.2 説明保存
- **エンドポイント**: `POST /api/files/descriptions/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "file_path": "string",
    "description": "string"
  }
  ```

### 9. ファイルタグ管理
#### 9.1 全ファイルタグ取得
- **エンドポイント**: `GET /api/files/tags/{project_folder}/`
- **機能**: プロジェクト内全ファイルのタグ情報取得

#### 9.2 個別ファイルタグ取得
- **エンドポイント**: `GET /api/files/tags/{project_folder}/`
- **クエリパラメータ**:
  - `file_path`: ファイルパス
- **機能**: 指定ファイルのタグ取得

#### 9.3 ファイルタグ保存
- **エンドポイント**: `POST /api/files/tags/{project_folder}/`
- **リクエストボディ**:
  ```json
  {
    "file_path": "string",
    "tags": ["分析データ", "項目データ"]
  }
  ```
- **タグルール**:
  - 分析データ (トップレベル)
    - 時系列データ (サブレベル)
    - 項目データ (サブレベル)
  - 参考資料 (トップレベル)

#### 9.4 タグによるファイル検索
- **エンドポイント**: `GET /api/files/search-by-tags/{project_folder}/`
- **クエリパラメータ**:
  - `tags`: 検索対象タグ（複数可、カンマ区切り）

---

## JupyterLab管理API

### 1. JupyterLab起動
- **エンドポイント**: `POST /api/jupyter/start/`
- **リクエストボディ**:
  ```json
  {
    "project_folder": "string"
  }
  ```

### 2. JupyterLab停止
- **エンドポイント**: `POST /api/jupyter/stop/`
- **リクエストボディ**:
  ```json
  {
    "project_folder": "string"
  }
  ```

### 3. JupyterLab状態確認
- **エンドポイント**: `GET /api/jupyter/status/`
- **機能**: 実行中のJupyterLabインスタンス一覧取得

### 4. サーバー情報取得
- **エンドポイント**: `GET /api/server-info/`
- **機能**: APIサーバーの基本情報取得

---

## 問題点と改善案

### 🔴 重要な問題点

#### 1. **URLパターンの重複と混乱**
**問題**: 
- `urls.py`でファイル管理APIが二重定義されている
- 同じ機能に対して複数のエンドポイントが存在

**具体例**:
```python
# 重複例1: ファイル削除
path('files/delete/<str:project_folder>/', ...)  # Line 15
@action(detail=False, methods=['delete'], url_path='delete/(?P<project_folder>[^/.]+)')
def delete_file(self, request, project_folder=None):  # views.py

# 重複例2: ファイル移動
path('files/move/<str:project_folder>/', ...)  # Line 16  
@action(detail=False, methods=['post'], url_path='move/(?P<project_folder>[^/.]+)')
def move_file(self, request, project_folder=None):  # views.py
```

**改善案**:
- 重複するエンドポイント定義を削除
- 統一されたURL体系に整理（urls.pyの固定パターンを採用）

#### 2. **ファイルタグAPIの不整合**
**問題**:
- パラメータ付きとパラメータなしで異なる動作
- `file_path`の指定方法が不統一

**現在**:
```
GET /api/files/tags/{project_folder}/                # 全ファイル
GET /api/files/tags/{project_folder}/{file_path}/    # 個別ファイル（削除推奨）
POST /api/files/tags/{project_folder}/               # 保存
```

**改善案**:
```
GET /api/files/tags/{project_folder}/                # 全ファイル
GET /api/files/tags/{project_folder}/?file_path=xxx  # 個別ファイル（クエリ統一）
POST /api/files/tags/{project_folder}/               # 保存
```

#### 3. **レスポンス形式の不統一**
**問題**:
- 成功/失敗レスポンスの形式が統一されていない
- エラーメッセージの国際化が部分的

**改善案**:
```json
// 統一レスポンス形式
{
  "success": boolean,
  "data": object | null,
  "error": {
    "code": "string",
    "message": "string",
    "details": object | null
  } | null,
  "meta": {
    "timestamp": "ISO8601",
    "version": "string"
  }
}
```

#### 4. **メソッド名と機能の不一致**
**問題**:
- `get_file_tags` vs `save_file_tags` の命名不統一
- `search_files_by_tags` の実装が未完了

**改善案**:
- 命名規則の統一（get_*, save_*, search_*）
- 未実装機能の完成

### 🟡 改善提案

#### 5. **APIバージョニング**
**現状**: バージョン管理なし
**提案**: 
```
/api/v1/projects/
/api/v1/files/
/api/v1/jupyter/
```

#### 6. **認証・権限管理**
**現状**: 認証なし
**提案**: 
- プロジェクトレベルでのアクセス制御
- 読み取り専用/読み書き権限の分離

#### 7. **リクエスト制限・レート制限**
**現状**: 制限なし
**提案**:
- ファイルアップロードサイズ制限明記
- API呼び出し頻度制限

#### 8. **非同期処理の明確化**
**現状**: 同期処理のみ
**提案**:
- 大きなファイル操作の非同期化
- 進行状況の取得API

### 🟢 良い点

1. **多言語対応**: 全APIで言語パラメータ対応
2. **RESTful設計**: 基本的なREST原則に準拠
3. **エラーハンドリング**: 適切な例外処理
4. **ファイル安全性**: 不正パスアクセスの防止
5. **タグ階層システム**: 分析データ→項目データの条件付きタグ

### 📋 推奨される改善順序

1. **緊急**: URL重複の解消（urls.py整理）
2. **高**: ファイルタグAPIの統一（パスパラメータ→クエリパラメータ）
3. **高**: レスポンス形式の統一
4. **中**: 未実装機能の完成（search_files_by_tags等）
5. **低**: バージョニング導入
6. **将来**: 認証・権限管理追加
- フロントエンドAPIプロキシ経由でのアクセスを推奨
- 現在の実装状況は「実装状況と今後の予定」セクションを参照

## ベースURL
```
# フロントエンドAPIプロキシ経由（推奨）
http://localhost:3000/api/

# バックエンド直接アクセス（非推奨）
http://localhost:8000/api/
```

## API命名規則
- **RESTful設計**: リソース名は複数形の名詞を使用
- **一貫性**: 全エンドポイントでパターンを統一
- **アクセス方法**: フロントエンドAPIプロキシ経由を推奨

## フロントエンドAPIプロキシ
フロントエンドはNext.js APIルートを使用してバックエンドAPIへのプロキシを提供します：

### 利用可能なプロキシエンドポイント:
- `/api/projects/` - プロジェクト管理
- `/api/files/[...slug]` - ファイル管理（動的ルーティング）
- `/api/server-info/` - サーバー情報

### 未実装のプロキシエンドポイント:
- `/api/jupyter/[...slug]` - JupyterLab管理 ❌ **未実装**

### プロキシの特徴:
- 自動的なタイムアウト処理（8秒）
- エラーレスポンスの正規化
- FormDataとJSONの両方をサポート
- バックエンド接続失敗時のフォールバック

### 現在の制限事項:
- JupyterLab APIは直接バックエンドアクセスが必要
- タグAPIはバックエンド未実装のため利用不可

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
GET /api/files/trees/{project_folder}
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
POST /api/files/uploads/{project_folder}
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
GET /api/files/searches/{project_folder}?q={query}&type={search_type}
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
DELETE /api/files/deletions/{project_folder}
```

**リクエスト例:**
```json
{
  "file_path": "data/old_file.csv"
}
```

### 5. ファイル/ディレクトリ移動
```http
POST /api/files/movements/{project_folder}
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
POST /api/files/directories/{project_folder}
```

**リクエスト例:**
```json
{
  "dir_path": "new_folder/subfolder"
}
```

---

## JupyterLab 管理 API

### 1. JupyterLabインスタンス作成（起動）
```http
POST /api/jupyter/instances/
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

### 2. JupyterLabインスタンス削除（停止）
```http
DELETE /api/jupyter/instances/{project_folder}
```

**レスポンス例:**
```json
{
  "success": true,
  "message": "JupyterLab stopped successfully",
  "project_folder": "my_project"
}
```

### 3. JupyterLabインスタンス状態取得
```http
GET /api/jupyter/instances/
GET /api/jupyter/instances/{project_folder}
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

### ⚠️ 命名不整合（要修正）
- ファイル説明保存API: フロントエンド `/files/comment/`, バックエンド `/files/comments/`
- API呼び出し混在: 一部直接バックエンド、一部プロキシ経由

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