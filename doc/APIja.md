# StatVizForge_JikkenPy API 仕様書

最終更新日: 2025年8月1日  
APIバージョン: 2.0.0  
対応言語: 日本語、英語

## 概要

StatVizForge_JikkenPyは、データ分析プロジェクトを管理し、統計的可視化を行うためのWebアプリケーションです。
本APIはデータプロジェクトのCRUD操作、ファイル管理、JupyterLab統合、表示設定管理などを提供します。

## ベースURL

- **推奨**: `/api/v1/` - APIバージョン1（安定版）
- **レガシー**: `/api/` - 後方互換性のため一時的に保持

## 認証

現在開発中のため認証機能は無効化されていますが、将来的にAPIキー認証とプロジェクト所有者権限が実装予定です。

## エラーレスポンス形式

全てのAPIエンドポイントは以下の統一形式でエラーを返します：

```json
{
  "error": "エラーコード",
  "message": "エラーメッセージ",
  "details": {
    "additional_info": "追加情報"
  },
  "language": "ja"
}
```

---

## 1. プロジェクト関連 API

### 1.1 プロジェクト基本操作

#### プロジェクト一覧取得
```
GET /api/v1/projects/
```

**機能**: projects-registry.jsonの内容を返す  
**パラメータ**: 
- `lang` (クエリ、任意): 言語設定（ja/en）

**レスポンス**:
```json
{
  "version": "1.0.0",
  "last_updated": "2025-08-01T09:58:51.803670",
  "projects": [
    {
      "id": "uuid",
      "folder_name": "testProject",
      "project_name": "テストプロジェクト",
      "description": "プロジェクトの説明",
      "tags": ["tag1", "tag2"],
      "status": "active",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    }
  ]
}
```

#### プロジェクト新規作成
```
POST /api/v1/projects/
```

**機能**: プロジェクトフォルダとproject.jsonを作成し、projects-registry.jsonに追加  
**パラメータ**:
```json
{
  "folder_name": "project_folder",
  "project_name": "プロジェクト名",
  "description": "プロジェクトの説明",
  "tags": ["tag1", "tag2"],
  "status": "active"
}
```

**レスポンス**: 作成されたプロジェクト情報

#### プロジェクト詳細取得
```
GET /api/v1/projects/{id}/
```

**機能**: 指定されたIDのプロジェクト詳細を取得  
**パラメータ**: 
- `id`: プロジェクトID（UUID）
- `lang` (クエリ、任意): 言語設定

**レスポンス**: プロジェクト詳細情報

#### プロジェクト更新
```
PUT /api/v1/projects/{id}/
```

**機能**: プロジェクト情報を更新（フォルダ名変更時は物理フォルダもリネーム）  
**パラメータ**: 
- `id`: プロジェクトID（UUID）
- 更新するフィールド（folder_name, project_name, description, tags等）

**レスポンス**: 更新されたプロジェクト情報

#### プロジェクト削除
```
DELETE /api/v1/projects/{id}/
```

**機能**: プロジェクトをzipアーカイブしてtrashに移動  
**パラメータ**: 
- `id`: プロジェクトID（UUID）

**レスポンス**: 204 No Content

### 1.2 プロジェクト拡張操作

#### 削除済みプロジェクト一覧取得
```
GET /api/v1/projects/deleted/
```

**機能**: trash-registry.jsonから削除済みプロジェクト一覧を取得  
**レスポンス**: 削除済みプロジェクト一覧

#### プロジェクト復元
```
POST /api/v1/projects/{id}/restore/
```

**機能**: trashからzipファイルを展開してプロジェクトを復元  
**パラメータ**: 
- `id`: 削除済みプロジェクトID（UUID）

**レスポンス**: 復元されたプロジェクト情報

#### レジストリ整合性確認
```
POST /api/v1/projects/validate_registry/
```

**機能**: プロジェクトレジストリとフォルダ構造の整合性を確認・修正  
**レスポンス**: 確認・修正結果

---

## 2. ファイル操作 API

### 2.1 ファイル基本操作

#### ディレクトリツリー取得
```
GET /api/v1/files/tree/{project_folder}/
```

**機能**: プロジェクトのディレクトリ構造を取得（コメント情報付き）  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `path` (クエリ、任意): 取得するパス

**レスポンス**: ディレクトリツリー構造

#### ファイルアップロード
```
POST /api/v1/files/upload/{project_folder}/
```

**機能**: プロジェクトにファイルをアップロード  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `files`: アップロードファイル（複数可）
- `target_path` (任意): アップロード先パス

**レスポンス**: アップロード結果

#### ファイル削除
```
DELETE /api/v1/files/delete/{project_folder}/
```

**機能**: ファイルまたはディレクトリを削除  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_path`: 削除するファイルパス

**レスポンス**: 削除結果

#### ファイル移動
```
POST /api/v1/files/move/{project_folder}/
```

**機能**: ファイルまたはディレクトリを移動  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `source_path`: 移動元パス
- `destination_path`: 移動先パス

**レスポンス**: 移動結果

#### ディレクトリ作成
```
POST /api/v1/files/mkdir/{project_folder}/
```

**機能**: 新規ディレクトリを作成  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `dir_path`: 作成するディレクトリパス

**レスポンス**: 作成結果

### 2.2 ファイル検索

#### ファイル検索
```
GET /api/v1/files/search/{project_folder}/
```

**機能**: ファイル名またはファイル内容で検索  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `q` (クエリ): 検索クエリ
- `type` (クエリ): 検索タイプ（name, content, both）

**レスポンス**: 検索結果

### 2.3 ファイル説明・タグ管理

#### ファイル説明管理
```
GET /api/v1/files/descriptions/{project_folder}/
POST /api/v1/files/descriptions/{project_folder}/
```

**GET機能**: ファイルの説明を取得  
**POST機能**: ファイルの説明を保存  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_path`: ファイルパス
- `description` (POST時): ファイル説明

**レスポンス**: ファイル説明情報

#### ファイルタグ管理
```
GET /api/v1/files/tags/{project_folder}/
POST /api/v1/files/tags/{project_folder}/
```

**GET機能**: ファイルタグを取得  
**POST機能**: ファイルタグを保存  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_path` (GET時): 特定ファイルのタグ取得
- `file_path`, `tags` (POST時): タグ保存

**レスポンス**: タグ情報

### 2.4 テーブルデータ操作

#### CSVテーブルデータ取得
```
GET /api/v1/files/table/{project_folder}/
```

**機能**: CSVファイルをテーブル形式で取得（最大1000行）  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_path` (クエリ): CSVファイルパス

**レスポンス**:
```json
{
  "headers": ["列1", "列2", "列3"],
  "rows": [
    ["値1", "値2", "値3"],
    ["値4", "値5", "値6"]
  ]
}
```

#### 列データ型設定
```
GET /api/v1/files/column-types/{project_folder}/
POST /api/v1/files/column-types/{project_folder}/
```

**GET機能**: 列データ型設定を取得  
**POST機能**: 列データ型設定を保存  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_path`: ファイルパス
- `column_types` (POST時): 列データ型設定

**レスポンス**: 列データ型設定

---

## 3. JupyterLab 管理 API

#### JupyterLab起動
```
POST /api/v1/jupyter/start/
```

**機能**: 指定プロジェクトのJupyterLabを起動  
**パラメータ**: 
```json
{
  "project_folder": "プロジェクトフォルダ名"
}
```

**レスポンス**: JupyterLabのURL、ポート情報

#### JupyterLab停止
```
POST /api/v1/jupyter/stop/
```

**機能**: 指定プロジェクトのJupyterLabを停止  
**パラメータ**: 
```json
{
  "project_folder": "プロジェクトフォルダ名"
}
```

**レスポンス**: 停止結果

#### JupyterLab状態確認
```
GET /api/v1/jupyter/status/
```

**機能**: 全JupyterLabインスタンスの状態を取得  
**レスポンス**: 実行中インスタンス一覧

---

## 4. 表表示設定 API

#### 表表示設定管理
```
GET /api/v1/table-settings/settings/{project_folder}/{file_name}/
POST /api/v1/table-settings/settings/{project_folder}/{file_name}/
DELETE /api/v1/table-settings/settings/{project_folder}/{file_name}/
```

**GET機能**: 表表示設定を取得  
**POST機能**: 表表示設定を保存  
**DELETE機能**: 表表示設定を削除  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `file_name`: ファイル名
- `table_config`, `chart_config`, `layout_config`, `column_metadata` (POST時): 各種設定

**レスポンス**: 表表示設定

#### 設定一覧取得
```
GET /api/v1/table-settings/settings/{project_folder}/
```

**機能**: プロジェクト内の全ファイルの表表示設定一覧を取得  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名

**レスポンス**: 設定一覧

#### マウスオーバー設定
```
GET /api/v1/table-settings/mouseover-settings/{project_folder}/
POST /api/v1/table-settings/mouseover-settings/{project_folder}/
```

**GET機能**: マウスオーバー表示設定を取得  
**POST機能**: マウスオーバー表示設定を保存  
**パラメータ**: 
- `project_folder`: プロジェクトフォルダ名
- `displayOptions` (POST時): 表示オプション設定

**レスポンス例**:
```json
{
  "success": true,
  "settings": {
    "displayOptions": [
      {
        "id": "basic_info",
        "enabled": true,
        "category": "basic",
        "displayPosition": "tooltip"
      }
    ]
  }
}
```

---

## 5. システム情報 API

#### サーバー情報取得
```
GET /api/v1/server-info/
```

**機能**: サーバーの基本情報を取得  
**レスポンス**: デバッグモード、環境、バージョン情報

#### テスト用エンドポイント
```
GET /api/v1/test/
```

**機能**: API接続テスト（開発環境のみ）  
**レスポンス**: 
```json
{
  "status": "ok",
  "version": "v1"
}
```

---

## API仕様上の改善提案

### 1. 命名規則の改善

#### 現在の問題点
- エンドポイントURLに一貫性がない（`/api/`と`/api/v1/`の併存）
- ファイル操作で一部のエンドポイントが冗長（`/files/tags/{project_folder}/`）

#### 改善提案
1. **APIバージョニングの統一**: `/api/`を廃止し、`/api/v1/`に統一
2. **RESTful設計の徹底**: リソース指向の設計を統一
3. **パラメータ命名の統一**: snake_caseで統一

### 2. セキュリティの強化

#### 現在の問題点
- 認証機能なし
- ファイルアクセスの制限なし
- パストラバーサル攻撃のリスク

#### 改善提案
1. **APIキー認証の実装**
2. **プロジェクト所有者権限の実装**
3. **ファイルアクセス制限の強化**
4. **入力値検証の徹底**

### 3. エラーハンドリングの改善

#### 現在の問題点
- エラーレスポンス形式の統一が不完全
- HTTPステータスコードの使い分けが不統一

#### 改善提案
1. **エラーレスポンス形式の完全統一**
2. **HTTPステータスコードの正確な使い分け**
3. **多言語対応エラーメッセージの統一**

### 4. パフォーマンスの最適化

#### 改善提案
1. **ページネーション機能の実装**
2. **キャッシュ機能の実装**
3. **レート制限の実装**
4. **大容量ファイル処理の最適化**

---

## 変更履歴

### v2.0.0 (2025-08-01)
- マウスオーバー設定API追加
- APIバージョニング（v1）導入
- セキュリティ強化（バリデーション追加）
- レート制限機能追加
- エラーハンドリング統一

### v1.0.0 (2025-07-31)
- 基本API機能実装
- プロジェクト管理機能
- ファイル操作機能
- JupyterLab統合機能

---

## サポート

質問や問題がある場合は、プロジェクトのGitHubリポジトリでIssueを作成してください。