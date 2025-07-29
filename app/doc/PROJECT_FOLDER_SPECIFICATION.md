# プロジェクトフォルダ仕様書

**バージョン**: 1.0.0  
**作成日**: 2025年7月28日  
**更新日**: 2025年7月28日  

## 概要

本ドキュメントは、StatVizForge_JikkenPyにおけるプロジェクトフォルダの構造と仕様を定義します。すべてのプロジェクト関連の機能は、この仕様に従って実装・運用されます。

## 基本構造

### プロジェクトルートディレクトリ
```
/project/
├── projects-registry.json          # プロジェクト管理レジストリ
├── projects-registry.backup.*      # レジストリバックアップファイル
├── trash/                          # 削除済みプロジェクトアーカイブ
│   ├── trash-registry.json         # 削除済みプロジェクト管理
│   └── *.zip                       # アーカイブされたプロジェクト
└── {project_folder_name}/          # 各プロジェクトフォルダ
```

### 個別プロジェクトフォルダ構造
```
{project_folder_name}/
├── project.json                    # プロジェクト設定ファイル（必須）
├── raw/                           # 生データ保存フォルダ（必須）
│   ├── *.csv                      # CSVファイル
│   ├── *.json                     # JSONファイル
│   ├── *.txt                      # テキストファイル
│   └── subfolder/                 # サブフォルダ（任意の階層）
├── analysisdata/                  # 分析データ・メタデータ保存フォルダ（自動作成）
│   ├── file_descriptions.json    # ファイル説明データ
│   ├── file_tags.json            # ファイルタグデータ
│   └── analysis_results/          # 分析結果ファイル
├── db/                           # データベース関連ファイル（自動作成）
│   └── *.db                      # SQLiteファイル等
├── git/                          # Git関連ファイル（自動作成）
│   └── .git                      # Gitリポジトリ
└── [その他任意のフォルダ]          # ユーザー定義フォルダ
```

## ファイル仕様

### 1. project.json（プロジェクト設定ファイル）

**場所**: `{project_folder_name}/project.json`  
**必須**: Yes  
**形式**: JSON

```json
{
  "folder_name": "project_folder_name",
  "project_name": "表示用プロジェクト名",
  "description": "プロジェクトの説明",
  "created_date": "2025-07-28T19:10:51.399660",
  "modified_date": "2025-07-28T19:10:51.399660",
  "tags": ["tag1", "tag2"],
  "status": "active"
}
```

**フィールド定義**:
- `folder_name`: フォルダ名（英数字、アンダースコア）
- `project_name`: 表示用プロジェクト名（日本語可）
- `description`: プロジェクトの説明文
- `created_date`: 作成日時（ISO 8601形式）
- `modified_date`: 最終更新日時（ISO 8601形式）
- `tags`: プロジェクトタグの配列
- `status`: プロジェクトステータス（"active" | "archived" | "deleted"）

### 2. projects-registry.json（プロジェクト管理レジストリ）

**場所**: `/project/projects-registry.json`  
**必須**: Yes  
**形式**: JSON

```json
{
  "version": "1.0.0",
  "last_updated": "2025-07-28T19:10:51.399660",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "project_folder",
      "project_name": "プロジェクト名",
      "description": "説明",
      "tags": ["tag1"],
      "status": "active",
      "id": "uuid-string",
      "created_date": "2025-07-28T19:10:51.399660",
      "modified_date": "2025-07-28T19:10:51.399660"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "archived_project",
      "project_name": "アーカイブされたプロジェクト",
      "description": "説明",
      "tags": ["archived"],
      "status": "active",
      "id": "uuid-string",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "archived_project_20250727_103756.zip",
      "archive_path": "/path/to/archive.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "削除理由"
    }
  ],
  "reserved_folders": [
    "node_modules", "dist", "build", ".git",
    "backend", "frontend", "trash", "recycle_bin",
    "deleted", ".trash"
  ]
}
```

### 3. file_descriptions.json（ファイル説明データ）

**場所**: `{project_folder_name}/analysisdata/file_descriptions.json`  
**自動作成**: Yes  
**形式**: JSON

```json
{
  "filename.csv": {
    "description": "ファイルの説明",
    "updated": "2025-07-28T23:33:30.790231",
    "author": "システム"
  },
  "subfolder/nested_file.py": {
    "description": "サブフォルダ内ファイルの説明",
    "updated": "2025-07-28T23:35:15.123456",
    "author": "システム"
  }
}
```

### 4. file_tags.json（ファイルタグデータ）

**場所**: `{project_folder_name}/analysisdata/file_tags.json`  
**自動作成**: Yes  
**形式**: JSON

```json
{
  "filename.csv": {
    "tags": ["分析データ", "項目データ"],
    "updated": "2025-07-28T23:34:00.000000",
    "author": "システム"
  }
}
```

### 5. trash-registry.json（削除済みプロジェクト管理）

**場所**: `/project/trash/trash-registry.json`  
**自動作成**: Yes  
**形式**: JSON

```json
{
  "version": "1.0.0",
  "deleted_projects": [
    {
      "folder_name": "deleted_project",
      "project_name": "削除されたプロジェクト",
      "description": "説明",
      "archive_filename": "deleted_project_20250727_103756.zip",
      "archive_path": "/path/to/archive.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除",
      "id": "uuid-string"
    }
  ],
  "last_updated": "2025-07-28T19:10:51.399660"
}
```

## フォルダ命名規則

### プロジェクトフォルダ名
- **形式**: 英数字、アンダースコア（_）、ハイフン（-）のみ
- **文字数**: 1-50文字
- **例**: `ichikawa`, `test_project`, `data-analysis-2025`

### 予約フォルダ名
以下のフォルダ名は使用禁止：
```
node_modules, dist, build, .git, backend, frontend, 
trash, recycle_bin, deleted, .trash
```

## API エンドポイント仕様

### プロジェクト管理
- `GET /api/projects/` - プロジェクト一覧取得
- `POST /api/projects/` - プロジェクト作成
- `GET /api/projects/{id}/` - プロジェクト詳細取得
- `PUT /api/projects/{id}/` - プロジェクト更新
- `DELETE /api/projects/{id}/` - プロジェクト削除
- `POST /api/projects/{id}/restore/` - プロジェクト復元

### ファイル管理
- `GET /api/files/tree/{project_folder}/` - ディレクトリツリー取得
- `POST /api/files/upload/{project_folder}/` - ファイルアップロード
- `DELETE /api/files/delete/{project_folder}/` - ファイル削除
- `POST /api/files/move/{project_folder}/` - ファイル移動
- `POST /api/files/mkdir/{project_folder}/` - フォルダ作成

### ファイル説明・タグ管理
- `GET /api/files/descriptions/{project_folder}/` - ファイル説明取得
- `POST /api/files/descriptions/{project_folder}/` - ファイル説明保存
- `GET /api/files/tags/{project_folder}/` - ファイルタグ取得
- `POST /api/files/tags/{project_folder}/` - ファイルタグ保存

## データ保存仕様

### ファイルパス正規化
- バックスラッシュ（`\`）をスラッシュ（`/`）に統一
- プロジェクトフォルダからの相対パスで保存
- 例: `raw/data.csv`, `raw/subfolder/file.txt`

### 文字エンコーディング
- すべてのJSONファイル: UTF-8
- `ensure_ascii=False`で日本語を保持

### 日時形式
- ISO 8601形式を使用: `2025-07-28T23:33:30.790231`
- タイムゾーン情報は省略（ローカル時間として扱う）

## バックアップとアーカイブ

### プロジェクト削除時の処理
1. プロジェクトフォルダ全体をZIP圧縮
2. `/project/trash/`フォルダに移動
3. `projects-registry.json`の`archived_projects`に記録
4. 元フォルダを削除

### アーカイブファイル命名規則
```
{project_folder_name}_{YYYYMMDD}_{HHMMSS}.zip
```
例: `ichikawa_20250728_191051.zip`

### 保存期間
- デフォルト: 13ヶ月
- `projects-registry.json`の`retention_months`で設定

## セキュリティ考慮事項

### ファイルアップロード制限
- 危険な拡張子の制限（`.exe`, `.bat`, `.sh`等）
- ファイルサイズ制限
- ディレクトリトラバーサル攻撃防止

### パス検証
- プロジェクトフォルダ外へのアクセス禁止
- 相対パス（`../`）の使用禁止
- 絶対パスの使用禁止

### アクセス制御
- プロジェクトフォルダ内のファイルのみアクセス可能
- システムファイルへのアクセス禁止

## エラーハンドリング

### プロジェクト作成時
- フォルダ名重複チェック
- 予約フォルダ名チェック
- ディスク容量チェック

### ファイル操作時
- ファイル存在確認
- 権限チェック
- パス妥当性検証

### データ整合性
- JSONファイル破損時の復旧処理
- レジストリとフォルダの同期チェック
- 不整合データの自動修正

## メンテナンス

### 定期タスク
- アーカイブファイルの期限切れ削除
- データ整合性チェック
- ディスク容量監視

### ログ出力
- プロジェクト作成/削除ログ
- ファイル操作ログ
- エラーログ

## 変更履歴

| バージョン | 日付 | 変更内容 |
|------------|------|----------|
| 1.0.0 | 2025-07-28 | 初版作成、ファイル説明・タグ機能追加 |

---

**注意**: この仕様書に従い、すべてのプロジェクト関連機能を実装・運用してください。仕様変更時は必ずこのドキュメントを更新し、バージョン番号を上げてください。