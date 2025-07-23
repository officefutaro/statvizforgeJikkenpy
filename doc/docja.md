# StatVizForge_JikkenPy 開発ドキュメント

## プロジェクト概要
このプロジェクトは、GUIでデータの読込み・可視化・計算を行うアプリケーションと、Pythonライブラリの開発を目的としています。

## データ管理方式の決定

### プロジェクトデータの保存形式
- **選択した形式**: JSON
- **理由**: 
  - Project.jsonと同じ形式で統一性がある
  - 人間にも読みやすい
  - Pythonで扱いやすい
  - 階層構造を自然に表現できる

### projects-registry.json の構造
```json
{
  "version": "1.0.0",
  "last_updated": "2025-01-20T10:30:00Z",
  "projects": [
    {
      "folder_name": "example_project_001",
      "project_name": "サンプルデータ分析",
      "description": "アプリケーションの動作確認用サンプルプロジェクト",
      "created_date": "2025-01-20T10:30:00Z",
      "modified_date": "2025-01-20T10:30:00Z",
      "tags": ["サンプル", "デモ"],
      "status": "active"
    }
  ]
}
```

**配置場所**: `/project/projects-registry.json`

## バックエンド構築

### Django REST API環境のセットアップ

#### 1. 仮想環境の準備
```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt
```

#### 2. 必要なパッケージ (requirements.txt)
```
asgiref==3.9.1
Django==5.2.4
django-cors-headers==4.7.0
djangorestframework==3.16.0
python-decouple==3.8
sqlparse==0.5.3
```

### Django プロジェクト構造
```
app/backend/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── api/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```

### 実装したAPIエンドポイント

#### プロジェクト管理API (`/api/projects/`)
- `GET /api/projects/` - プロジェクト一覧
- `POST /api/projects/` - 新規作成
- `GET /api/projects/{id}/` - 詳細取得
- `PUT /api/projects/{id}/` - 更新
- `DELETE /api/projects/{id}/` - 削除

#### ファイル操作API (`/api/files/`)
- `POST /api/files/upload/` - アップロード
- `GET /api/files/{id}/download/` - ダウンロード
- `GET /api/files/list/{project_id}/` - プロジェクト内ファイル一覧

#### データ処理API (`/api/data/`)
- `POST /api/data/analyze/` - データ分析実行
- `GET /api/data/{id}/results/` - 結果取得

### モデル定義

#### Project モデル
- folder_name: プロジェクトフォルダ名
- project_name: プロジェクト名
- description: 説明
- created_date: 作成日時
- modified_date: 更新日時
- status: ステータス
- tags: タグ（JSON配列）

#### ProjectFile モデル
- project: 関連プロジェクト
- file: ファイル本体
- file_name: ファイル名
- file_type: ファイルタイプ
- uploaded_at: アップロード日時

#### DataAnalysis モデル
- project: 関連プロジェクト
- analysis_type: 分析タイプ
- parameters: パラメータ（JSON）
- status: ステータス
- result: 結果（JSON）
- created_at: 作成日時
- completed_at: 完了日時

## フロントエンドとの接続

### WSL環境でのアクセス設定
1. WSLのIPアドレス確認: `172.24.67.130`
2. Djangoサーバーの起動: `python manage.py runserver 0.0.0.0:8000`
3. ALLOWED_HOSTSの設定: 開発環境では全てのホストを許可

### CORS設定
開発環境では`CORS_ALLOW_ALL_ORIGINS = True`に設定し、全てのオリジンからのアクセスを許可。

### アクセスURL
- API: http://172.24.67.130:8000/api/
- 管理画面: http://172.24.67.130:8000/admin/

## 開発ルール

### 重要な規則

#### 1. API仕様変更時の対応
APIの仕様を変更した場合は必ず以下のファイルを更新すること：
```
~/app/frontend/BOLT_NEW_INSTRUCTIONS.md
```

#### 2. フロントエンド変更時のGit操作
frontendフォルダ内のファイルを変更した際は、必ず以下のコマンドでGitにpushすること：

```bash
# 変更したファイルを確認
git status

# 変更をステージング
git add app/frontend/

# コミット（メッセージは変更内容に応じて適切に記述）
git commit -m "Update frontend: [変更内容の説明]"

# リモートリポジトリにプッシュ
git push origin main
```

## 開発環境の起動手順

### バックエンド
```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

### データベースの初期化
```bash
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
```

## テスト用ファイル
- `/app/backend/api_test.html` - APIテスト用HTML
- `/app/backend/frontend_integration.md` - フロントエンド統合ガイド
- `/app/frontend/BOLT_NEW_INSTRUCTIONS.md` - Bolt.new用の開発指示書

## 最近の更新内容（2025-07-21）

### API仕様の大幅変更
- プロジェクト管理APIが`~/project/projects-registry.json`ファイルを直接操作するように変更
- データベースを使用せず、JSONファイルでプロジェクト情報を管理
- `/api/projects/`エンドポイントがprojects-registry.jsonの内容をそのまま返すように変更

### ファイル配置の変更
- `projects-registry.json`を`/app/backend/`から`/project/`に移動
- プロジェクトデータとアプリケーション設定の分離

### 新機能の追加
- API履歴記録機能（開発モードのみ）
- サーバー情報API（`/api/server-info/`）

## 今後の作業
1. 各APIエンドポイントの実装を具体化
2. ファイルアップロード・ダウンロード機能の実装
3. データ分析機能の実装
4. フロントエンドとの連携テスト