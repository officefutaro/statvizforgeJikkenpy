# StatVizForge_JikkenPy プロジェクトフォルダ構造説明

**作成日**: 2025年7月28日  
**バージョン**: 1.0.0

## 概要

StatVizForge_JikkenPyは、実験計画法（DOE）と統計分析のためのWebアプリケーションです。本ドキュメントでは、プロジェクト全体のフォルダ構造について説明します。

## 全体構造

```
StatVizForge_JikkenPy/
├── app/                                # アプリケーション本体
│   ├── backend/                        # Django バックエンド
│   ├── frontend/                       # Next.js フロントエンド
│   ├── config.json                     # アプリケーション設定
│   └── doc/                           # アプリケーション仕様書
├── project/                           # ユーザープロジェクトデータ
├── doc/                              # プロジェクト全体ドキュメント
├── lib/                              # 共通ライブラリ
├── testing/                          # テスト関連
├── logs/                             # ログファイル
├── backend_env/                      # バックエンド用Python仮想環境（予備）
├── jupyter_env/                      # JupyterLab専用Python仮想環境
├── jupyter_service/                  # JupyterLabサービス管理
└── [設定・起動スクリプト]             # 各種設定ファイル
```

## 詳細説明

### 1. app/ - アプリケーション本体

#### backend/ - Django バックエンド
```
app/backend/
├── api/                              # REST API アプリケーション
│   ├── views.py                      # API エンドポイント
│   ├── models.py                     # データモデル
│   ├── serializers.py                # データシリアライザー
│   ├── urls.py                       # URL設定
│   ├── utils.py                      # ユーティリティ関数
│   ├── middleware/                   # カスタムミドルウェア
│   └── test_*.py                     # テストファイル
├── config/                           # Django設定
│   ├── settings.py                   # メイン設定
│   ├── urls.py                       # ルートURL設定
│   ├── paths.py                      # パス設定
│   └── wsgi.py, asgi.py             # WSGIサーバー設定
├── test_utils/                       # テストユーティリティ
├── venv/                            # Python仮想環境
├── manage.py                        # Django管理コマンド
├── requirements.txt                 # Python依存関係
└── db.sqlite3                       # SQLiteデータベース
```

#### frontend/ - Next.js フロントエンド
```
app/frontend/
├── app/                             # Next.js App Router
│   ├── api/                         # API Routes (プロキシ)
│   ├── layout.tsx                   # 共通レイアウト
│   ├── page.tsx                     # ホームページ
│   └── globals.css                  # グローバルスタイル
├── components/                      # Reactコンポーネント
│   ├── ui/                          # shadcn/ui コンポーネント
│   ├── ProjectList.tsx              # プロジェクト一覧
│   ├── FileExplorer.tsx             # ファイルエクスプローラー
│   ├── FileComments.tsx             # ファイルコメント機能
│   └── [その他UI部品]
├── contexts/                        # React Context
├── lib/                            # ライブラリとユーティリティ
├── src/                            # 追加ソース
│   ├── services/                    # APIクライアント
│   └── mocks/                       # モックデータ
├── doc/                            # フロントエンド仕様書
├── test-utils/                     # テストユーティリティ
├── e2e/                            # E2Eテスト
├── package.json                    # npm依存関係
├── next.config.js                  # Next.js設定
├── tailwind.config.ts              # Tailwind CSS設定
└── tsconfig.json                   # TypeScript設定
```

### 2. project/ - ユーザープロジェクトデータ

```
project/
├── projects-registry.json           # プロジェクト管理レジストリ
├── projects-registry.backup.*      # レジストリバックアップ
├── trash/                          # 削除済みプロジェクト
│   ├── trash-registry.json         # 削除プロジェクト管理
│   └── *.zip                       # アーカイブファイル
└── {プロジェクト名}/                # 各ユーザープロジェクト
    ├── project.json                # プロジェクト設定
    ├── raw/                        # 生データ
    ├── analysisdata/               # 分析データ・メタデータ
    ├── db/                         # データベースファイル
    └── git/                        # Gitリポジトリ
```

**詳細仕様**: `app/doc/PROJECT_FOLDER_SPECIFICATION.md` を参照

### 3. doc/ - プロジェクト全体ドキュメント

```
doc/
├── APIja.md                        # API仕様書（日本語）
├── Backend_Startup_Guide.md        # バックエンド起動ガイド
├── integrated-dev-environment-ja.md # 統合開発環境説明
├── docja.md                        # ドキュメント索引（日本語）
├── Claude_Codeに対する指示/        # AI開発支援資料
├── アプリケーション/                # アプリケーション仕様
├── ライブラリ関係検討/              # ライブラリ選定資料
├── 実験計画法/                     # DOE理論・実装資料
├── trydatalink/                    # データ分析事例
└── history/                        # 開発履歴
```

### 4. lib/ - 共通ライブラリ

```
lib/
└── jikkenpy/                       # 実験計画法ライブラリ（開発中）
    ├── __init__.py
    └── designs/                    # 実験計画生成モジュール
        ├── generator.py
        └── __init__.py
```

### 5. testing/ - テスト関連

```
testing/
├── README.md                       # テスト実行ガイド
├── docs/                          # テスト文書
│   ├── API_Test_Manual.md          # API テスト手順書
│   ├── API_Testing_Guide.md        # APIテストガイド
│   └── Test_Writing_Examples.md    # テスト作成例
├── scripts/                       # テストスクリプト
│   ├── run_tests.py               # テスト実行スクリプト
│   └── test_runner.sh             # シェルテストランナー
└── results/                       # テスト結果
    ├── latest_summary.md          # 最新テスト結果サマリー
    ├── test_results_*.json        # 詳細テスト結果
    └── test_summary_*.md          # 日別テスト結果
```

### 6. その他の重要ファイル

```
StatVizForge_JikkenPy/
├── claude.md                      # AI開発支援メモ
├── start-dev.sh                   # 開発サーバー起動
├── stop-dev.sh                    # 開発サーバー停止
├── restart-backend.sh             # バックエンド再起動
├── restart-frontend.sh            # フロントエンド再起動
├── quick-setup.sh                 # クイックセットアップ
├── logs/                          # アプリケーションログ
│   ├── backend.log
│   └── frontend.log
├── PROJECT_DATA_PROTECTION.md     # データ保護方針
├── TESTING_CONFIGURATION.md       # テスト設定
├── TEST_INFRASTRUCTURE.md         # テストインフラ仕様
└── jupyter_env_setup.sh          # JupyterLab環境セットアップスクリプト
```

### 7. JupyterLab環境

```
jupyter_env/                       # JupyterLab専用仮想環境
├── bin/                          # 実行可能ファイル
├── lib/                          # Pythonライブラリ
└── [Python仮想環境ファイル]

jupyter_service/                   # JupyterLabサービス管理
├── config/                       # JupyterLab設定
│   └── jupyter_lab_config.py     # JupyterLab設定ファイル
├── logs/                         # JupyterLabログ
├── temp/                         # 一時ファイル
│   └── jupyter_instances.json    # 実行中のインスタンス情報
└── jupyter_manager.py            # JupyterLabインスタンス管理スクリプト

backend_env/                      # バックエンド用Python仮想環境（予備）
└── [Python仮想環境ファイル]
```

**JupyterLab環境の特徴：**
- 各プロジェクトフォルダごとに独立したJupyterLabインスタンスを起動
- ポートとトークンによるセキュアなアクセス管理
- データサイエンス用ライブラリ（pandas, numpy, matplotlib等）を事前インストール
- バックエンドAPIとの連携によるプロジェクトファイル管理

## 開発環境

### バックエンド (Django)
- **言語**: Python 3.12+
- **フレームワーク**: Django 5.0+
- **データベース**: SQLite (開発), PostgreSQL (本番想定)
- **API**: Django REST Framework

### フロントエンド (Next.js)
- **言語**: TypeScript
- **フレームワーク**: Next.js 14+ (App Router)
- **UI**: Tailwind CSS + shadcn/ui
- **状態管理**: React Context + useState/useEffect

### JupyterLab環境
- **言語**: Python 3.12+
- **フレームワーク**: JupyterLab 4.2.5
- **主要ライブラリ**: NumPy, Pandas, Matplotlib, Seaborn, Plotly, SciPy, scikit-learn
- **管理**: 独立した仮想環境でプロジェクトごとにインスタンス管理

### 開発ツール
- **テスト**: Jest (ユニット), Playwright (E2E)
- **リンター**: ESLint, Ruff (Python)
- **型チェック**: TypeScript, mypy (Python)

## 起動方法

### 開発環境一括起動
```bash
./start-dev.sh
```

### 個別起動
```bash
# バックエンド
cd app/backend
source venv/bin/activate
python manage.py runserver

# フロントエンド
cd app/frontend
npm run dev

# JupyterLab（プロジェクトごと）
cd jupyter_service
python jupyter_manager.py start <project_folder> <working_dir>
```

## データフロー

1. **フロントエンド** → プロキシAPI (`app/api/*`) → **バックエンドAPI** (`/api/*`)
2. **ユーザーデータ** は `project/` フォルダに保存
3. **アプリケーション設定** は `app/config.json`
4. **プロジェクト管理** は `project/projects-registry.json`
5. **JupyterLab** → 各プロジェクトフォルダで独立インスタンス → バックエンドAPI連携

## セキュリティ

- プロジェクトフォルダ外へのアクセス制限
- ファイルアップロード拡張子制限  
- パス検証によるディレクトリトラバーサル防止
- API認証・認可（将来実装予定）

## 関連ドキュメント

- [プロジェクトフォルダ仕様書](app/doc/PROJECT_FOLDER_SPECIFICATION.md)
- [API仕様書](doc/APIja.md)
- [フロントエンドアーキテクチャ](app/frontend/doc/architecture-ja.md)
- [バックエンド起動ガイド](doc/Backend_Startup_Guide.md)
- [テストガイド](testing/docs/API_Testing_Guide.md)
- [JupyterLab環境セットアップ](jupyter_env_setup.sh)

---

このプロジェクトは実験計画法を活用したデータ分析支援を目的として開発されています。詳細な技術仕様や使用方法については、各フォルダ内のドキュメントを参照してください。