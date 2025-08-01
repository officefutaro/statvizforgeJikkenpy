# StatVizForge フォルダ分類提案

**作成日**: 2025年8月1日  
**目的**: リリース用と開発用フォルダの明確な区分

## 📦 リリース時にユーザーに公開するフォルダ

### ✅ **必須公開フォルダ**

#### 1. **`docs/`** - ユーザードキュメント
```
docs/
├── README.md                    # ドキュメント索引
├── FEATURE_GUIDE.md            # 機能使用ガイド
└── features/                   # 詳細機能ドキュメント
    └── mouseover-statistics.md # マウスオーバー統計仕様
```
**役割**: エンドユーザー向けの完全な使用説明書

#### 2. **`app/`** - アプリケーション本体
```
app/
├── backend/                    # バックエンドアプリケーション
│   ├── api/                   # API実装
│   ├── config/                # 設定ファイル
│   ├── manage.py              # Django管理スクリプト
│   ├── requirements.txt       # Python依存関係
│   └── setup_venv.sh          # 環境構築スクリプト
└── frontend/                  # フロントエンドアプリケーション
    ├── components/            # React コンポーネント
    ├── app/                   # Next.js アプリケーション
    ├── package.json           # Node.js依存関係
    └── README.md              # フロントエンド説明
```
**役割**: 実行可能なアプリケーション本体

#### 3. **~~`project/`~~** - ❌ 初回起動時に自動生成
```
project/                      # 🔴 初回起動時に自動生成（公開しない）
├── projects-registry.json     # プロジェクト管理ファイル
├── cleanup_registry.py       # レジストリ整合性スクリプト
└── (ユーザープロジェクトフォルダ) # 完全にユーザー固有データ
```
**理由**: ユーザーデータのため初回起動時に設定

#### 4. **~~`Operation/`~~** - ❌ 開発専用に変更
```
Operation/                    # 🔴 開発確認用（公開しない）
├── ShellScript/
│   ├── start-services.sh     # 開発確認用スクリプト
│   └── stop-services.sh      # 開発確認用スクリプト
└── Memo/
    └── シェルスクリプト解説.md # 開発メモ
```
**理由**: 確認用スクリプトのため開発専用

#### 5. **設定・テンプレートファイル**
```
/
├── MOUSEOVER_SETTINGS_TEMPLATE.json  # マウスオーバー設定テンプレート
├── start-dev.sh                      # 開発サーバー起動
├── stop-dev.sh                       # 開発サーバー停止
├── quick-setup.sh                    # 簡単セットアップ
└── README.md                         # プロジェクト概要
```

### 📋 **参考公開フォルダ**

#### 6. **~~`doc/`~~** - ❌ 開発専用に変更
```
doc/                          # 🔴 開発・技術仕様用（公開しない）
├── APIja.md                   # API仕様書（開発者向け）
├── project_folder_structure.md # プロジェクト構造（開発者向け）
└── Backend_Startup_Guide.md   # バックエンド起動ガイド（開発者向け）
```
**理由**: 技術仕様・開発指示が混在、ユーザー向けは`app/docs/`に移動

#### 7. **`deployment/`** - デプロイメント設定
```
deployment/
├── docker-compose.prod.yml   # 本番環境Docker設定
├── Dockerfile.prod           # 本番環境Dockerfile
├── nginx/                    # Webサーバー設定
└── README.md                 # デプロイメント手順
```
**役割**: 本番環境構築用（システム管理者向け）

---

## 🔒 開発時のみ使用（リリース時は除外）

### ❌ **開発専用フォルダ**

#### 1. **`docs/`** - 現在は開発指示が混在（要整理）
```
docs/                         # 🔴 開発・仕様ドキュメント（開発専用に変更）
├── FEATURE_GUIDE.md          # → app/docs/user-guide/ に移動
├── features/                 # → app/docs/features/ に移動
└── README.md                 # ドキュメント索引
```
**理由**: 開発指示や仕様が混在、ユーザー向けは`app/docs/`に分離

#### 2. **`CLAUDE_INSTRUCTIONS/`** - AI開発指示書
```
CLAUDE_INSTRUCTIONS/
├── 指示に対するClaudeCode基本動作.md
├── コーディング規約.md
├── project_data_protection.md
└── test_generation_rules.md
```
**理由**: AI開発用の内部指示、エンドユーザーには不要

#### 3. **`testing/`** - 開発テスト関連
```
testing/
├── docs/                     # テスト仕様書
├── results/                  # テスト結果
├── scripts/                  # テストスクリプト
└── README.md
```
**理由**: 開発時のテスト用、ユーザーの実行環境では不要

#### 4. **`logs/`** - ログファイル
```
logs/
├── backend.log               # バックエンドログ
└── frontend.log              # フロントエンドログ
```
**理由**: 開発時のデバッグ用、実行時は自動生成される

#### 5. **`doc/`** - 技術仕様書
```
doc/                          # 🔴 開発・技術仕様用
├── APIja.md                   # API仕様書（開発者向け）
├── project_folder_structure.md # プロジェクト構造
└── (その他技術仕様)
```
**理由**: 開発者・技術者向けの詳細仕様

#### 6. **`Operation/`** - 確認用スクリプト
```
Operation/                    # 🔴 開発確認用
├── ShellScript/               # 各種確認スクリプト
└── Memo/                      # 運用メモ
```
**理由**: 開発・確認用のスクリプト

#### 7. **`project/`** - ユーザーデータ領域
```
project/                      # 🔴 初回起動時に自動生成
├── projects-registry.json     # プロジェクト管理ファイル
└── (ユーザープロジェクト)      # 完全にユーザー固有データ
```
**理由**: ユーザーデータのため公開せず、初回起動時に設定

#### 4. **開発・デバッグファイル**
```
app/backend/
├── apihistory.md             # API履歴（開発用）
├── comprehensive_api_test.py # 包括テスト
├── debug_*.py                # デバッグスクリプト
├── test_*.py                 # 各種テストファイル
├── db.sqlite3                # 開発用データベース
└── django.log                # Django開発ログ

app/frontend/
├── coverage/                 # テストカバレッジ
├── playwright-report/        # E2Eテスト結果
├── __tests__/                # 単体テスト
├── e2e/                      # E2Eテスト
├── dev-log.txt               # 開発ログ
└── node_modules/             # 依存関係（自動生成）
```
**理由**: 開発・テスト専用、本番環境では不要

#### 5. **設定・履歴ファイル**
```
/
├── claude.md                 # AI開発メモ
├── WSL_SESSION_STATE_*.md    # セッション状態記録
├── 毎朝のルーチンワーク.md   # 開発ルーチン
├── PROJECT_DATA_PROTECTION.md # 開発指針
├── TESTING_CONFIGURATION.md  # テスト設定
├── TEST_INFRASTRUCTURE.md    # テストインフラ
├── error_mix_test_valid/     # テスト用プロジェクト
├── screenshoit/              # スクリーンショット
├── venv/                     # Python仮想環境
└── .git/                     # Git履歴
```

#### 6. **履歴・作業ファイル**
```
doc/history/                  # 開発履歴
doc/obsidian/                 # 個人メモ
doc/Claude_Codeに対する指示/   # AI指示
project/trash/                # 削除済みプロジェクト
```

---

## 🏗️ **推奨フォルダ構造（リリース版）**

```
StatVizForge_JikkenPy/
├── README.md                        # プロジェクト概要
├── docs/                           # 📚 ユーザードキュメント
├── app/                            # 💾 アプリケーション本体
├── project/                        # 📁 プロジェクトデータ領域
├── Operation/                      # ⚙️ 運用スクリプト
├── deployment/                     # 🚀 デプロイメント設定
├── doc/                           # 📋 技術仕様書（参考）
├── MOUSEOVER_SETTINGS_TEMPLATE.json # ⚙️ 設定テンプレート
├── start-dev.sh                   # 🚀 開発サーバー起動
├── stop-dev.sh                    # 🛑 開発サーバー停止
└── quick-setup.sh                 # ⚡ 簡単セットアップ
```

## 📦 **リリース準備時の作業**

### 1. **除外対象の確認**
```bash
# 開発専用フォルダを確認
ls -la CLAUDE_INSTRUCTIONS/
ls -la testing/
ls -la logs/
```

### 2. **クリーンアップスクリプト作成**
```bash
# release-prepare.sh の作成
rm -rf CLAUDE_INSTRUCTIONS/
rm -rf testing/
rm -rf logs/
rm -rf app/backend/debug_*.py
rm -rf app/backend/test_*.py
rm -rf app/frontend/coverage/
# etc...
```

### 3. **必要ファイルの最終確認**
- [ ] docs/ - 完全な使用説明書
- [ ] app/ - 動作するアプリケーション
- [ ] README.md - 明確なセットアップ手順
- [ ] 設定テンプレート - カスタマイズ用

### 4. **サイズ最適化**
- [ ] node_modules/ の削除（npm install で再生成）
- [ ] Python __pycache__/ の削除
- [ ] 不要な画像・動画ファイルの削除

この分類により、エンドユーザーにとって必要な情報のみが提供され、開発の複雑さが隠蔽されます。