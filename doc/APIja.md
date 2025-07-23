# StatVizForge API仕様書

## 基本情報

**作成日時**: 2025年7月20日  
**バージョン**: 1.0.0  
**ベースURL**: `http://172.24.67.130:8000/api`  
**フレームワーク**: Django REST Framework  

## 認証
現在は認証なし（開発段階）

## 共通仕様

### 言語指定
すべてのAPIエンドポイントで、クエリパラメータ`lang`により応答言語を指定できます。

**サポート言語**:
- `en`: 英語（デフォルト）
- `ja`: 日本語
- `zh`: 中国語

**使用例**:
```
GET /api/projects/list?lang=ja
POST /api/projects/create?lang=zh
```

**言語が指定されない場合**: 英語で応答します。

### HTTPステータスコード
- `200 OK`: 成功
- `201 Created`: 新規作成成功
- `400 Bad Request`: リクエストエラー
- `404 Not Found`: リソースが見つからない
- `409 Conflict`: リソースの競合（例：重複するフォルダ名）
- `500 Internal Server Error`: サーバーエラー

### 共通レスポンス形式
```json
{
  "data": {},
  "error": null,
  "message": "success"
}
```

### エラーレスポンス形式
```json
{
  "error": "ERROR_CODE",
  "message": "ローカライズされたエラーメッセージ",
  "details": {
    "field_name": "フィールド固有のエラー"
  }
}
```

---

## 1. プロジェクト管理API

### エンドポイント: `/api/projects/`

**重要**: このAPIは`~/project/projects-registry.json`ファイルを直接操作します。データベースは使用しません。

#### 1.1 プロジェクト一覧取得
**メソッド**: `GET`  
**URL**: `/api/projects/list`  
**説明**: projects-registry.jsonファイルの内容をそのまま返す

**レスポンス例**:
```json
{
  "version": "1.0.0",
  "last_updated": "2025-07-21T11:30:00",
  "projects": [
    {
      "id": 1,
      "folder_name": "sales_analysis_2024",
      "project_name": "2024年売上分析",
      "description": "年間売上データの分析と予測",
      "created_date": "2025-01-20T10:30:00",
      "modified_date": "2025-01-20T15:45:00",
      "status": "active",
      "tags": ["売上", "分析", "予測"]
    }
  ]
}
```

#### 1.2 プロジェクト詳細取得
**メソッド**: `GET`  
**URL**: `/api/projects/{id}/`  
**説明**: 指定されたIDのプロジェクト詳細を取得

**パラメータ**:
- `id` (required): プロジェクトID

#### 1.3 プロジェクト新規作成
**メソッド**: `POST`  
**URL**: `/api/projects/create`  
**説明**: 新しいプロジェクトを作成し、projects-registry.jsonファイルに追加

**リクエストボディ**:
```json
{
  "folder_name": "customer_segmentation",
  "project_name": "顧客セグメンテーション分析",
  "description": "RFM分析による顧客分類",
  "tags": ["顧客", "セグメンテーション", "RFM"],
  "status": "active"
}
```

**必須フィールド**:
- `folder_name`: 一意のフォルダ名
- `project_name`: プロジェクト名
- `description`: プロジェクトの説明

**レスポンス例**:
```json
{
  "id": 2,
  "folder_name": "customer_segmentation",
  "project_name": "顧客セグメンテーション分析",
  "description": "RFM分析による顧客分類",
  "created_date": "2025-07-22T09:30:00",
  "modified_date": "2025-07-22T09:30:00",
  "status": "active",
  "tags": ["顧客", "セグメンテーション", "RFM"]
}
```

**注意事項**:
- IDは自動的に生成されます（最大ID + 1）
- created_dateとmodified_dateは自動的に現在時刻が設定されます

**エラーレスポンス例**:

400 Bad Request（バリデーションエラー）:
```json
{
  "error": "VALIDATION_ERROR",
  "message": "Invalid input data",  // langパラメータに応じて変化
  "details": {
    "folder_name": "This field is required",
    "project_name": "Project name must be 255 characters or less"
  }
}
```

409 Conflict（重複エラー）:
```json
{
  "error": "DUPLICATE_FOLDER",
  "message": "A project with this folder name already exists",  // langパラメータに応じて変化
  "field": "folder_name"
}
```

500 Internal Server Error:
```json
{
  "error": "INTERNAL_ERROR",
  "message": "An unexpected error occurred. Please try again later",  // langパラメータに応じて変化
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

#### 1.4 プロジェクト更新
**メソッド**: `PUT`  
**URL**: `/api/projects/{id}/`  
**説明**: 既存プロジェクトの情報を更新

#### 1.5 プロジェクト削除
**メソッド**: `DELETE`  
**URL**: `/api/projects/{id}/`  
**説明**: 指定されたプロジェクトを削除

---

## 2. ファイル操作API

### エンドポイント: `/api/files/`

#### 2.1 ファイルアップロード
**メソッド**: `POST`  
**URL**: `/api/files/upload/`  
**説明**: プロジェクトにファイルをアップロード

**リクエスト形式**: `multipart/form-data`
```
file: [ファイルデータ]
project_id: [プロジェクトID]
```

**現在の実装状況**: 🚧 未実装（空のエンドポイント）

#### 2.2 ファイルダウンロード
**メソッド**: `GET`  
**URL**: `/api/files/{id}/download/`  
**説明**: 指定されたファイルをダウンロード

**現在の実装状況**: 🚧 未実装（空のエンドポイント）

#### 2.3 プロジェクト内ファイル一覧
**メソッド**: `GET`  
**URL**: `/api/files/list/{project_id}/`  
**説明**: 指定されたプロジェクト内のファイル一覧を取得

**現在の実装状況**: 🚧 未実装（空のエンドポイント）

---

## 3. データ処理API

### エンドポイント: `/api/data/`

#### 3.1 データ分析実行
**メソッド**: `POST`  
**URL**: `/api/data/analyze/`  
**説明**: データ分析処理を実行

**現在の実装状況**: 🚧 未実装（空のエンドポイント）

#### 3.2 分析結果取得
**メソッド**: `GET`  
**URL**: `/api/data/{id}/results/`  
**説明**: 分析結果を取得

**現在の実装状況**: 🚧 未実装（空のエンドポイント）

---

## データベースモデル

### Project モデル
| フィールド名 | 型 | 説明 | 制約 |
|-------------|----|----|------|
| id | Integer | 主キー | 自動生成 |
| folder_name | CharField(255) | フォルダ名 | 必須、一意 |
| project_name | CharField(255) | プロジェクト名 | 必須 |
| description | TextField | 説明 | 任意 |
| created_date | DateTimeField | 作成日時 | 自動設定 |
| modified_date | DateTimeField | 更新日時 | 自動更新 |
| status | CharField(50) | ステータス | デフォルト: "active" |
| tags | JSONField | タグ配列 | デフォルト: [] |

---

## 設定情報

### CORS設定
- 開発環境: 全オリジン許可（`CORS_ALLOW_ALL_ORIGINS = True`）
- 本番環境: 特定オリジンのみ許可

---

## 今後の実装予定

### 優先度: 高
1. ファイルアップロード機能の実装
2. ファイルダウンロード機能の実装
3. プロジェクト内ファイル一覧機能の実装

### 優先度: 中
1. データ分析実行機能の実装
2. 分析結果取得機能の実装
3. 認証機能の追加

---

## サーバー情報API

### エンドポイント: `/api/server-info/`

**メソッド**: `GET`  
**URL**: `/api/server-info/`  
**説明**: サーバーの動作環境情報を取得

**レスポンス例**:
```json
{
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
```

---

## 変更履歴

| 日時 | バージョン | 変更内容 | 担当者 |
|------|-----------|---------|--------|
| 2025-07-20 | 1.0.0 | 初版作成、基本API仕様定義 | Claude Code |
| 2025-07-20 | 1.0.1 | サーバー情報API追加、API履歴記録機能追加（開発モードのみ） | Claude Code |
| 2025-07-21 | 1.1.0 | プロジェクト管理APIをprojects-registry.jsonファイル直接操作に変更 | Claude Code |
| 2025-07-22 | 1.2.0 | プロジェクト一覧取得を/api/projects/list、新規作成を/api/projects/createに変更 | Claude Code |
| 2025-07-22 | 1.3.0 | 言語指定機能追加（langクエリパラメータ）、エラーレスポンス形式の標準化 | Claude Code |