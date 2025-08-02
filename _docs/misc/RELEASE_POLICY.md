# StatVizForge リリースポリシー

**最終更新**: 2025年8月1日  
**バージョン**: v2.0.0

## 📦 フォルダ分類・公開ポリシー

### 🎯 基本方針

1. **エンドユーザー**: 使用に必要な情報のみ提供
2. **開発者**: 技術仕様や開発指示は分離
3. **データ**: ユーザーデータは初回起動時に生成
4. **運用**: 確認用スクリプトは開発専用

---

## 📂 フォルダ分類

### 🟢 **リリース時に公開するフォルダ**

#### 1. **`app/`** - アプリケーション本体
```
app/
├── backend/                    # バックエンドアプリケーション
├── frontend/                   # フロントエンドアプリケーション
└── docs/                       # 📚 ユーザー向けドキュメント（新設）
    ├── user-guide/             # 使い方ガイド
    ├── features/               # 機能詳細説明
    ├── configuration/          # 設定方法
    └── troubleshooting/        # トラブルシューティング
```

#### 2. **`deployment/`** - デプロイメント設定
```
deployment/
├── docker-compose.prod.yml     # 本番環境設定
├── README.md                   # デプロイ手順
└── setup/                      # セットアップスクリプト
```

#### 3. **ルートファイル** - セットアップ・実行用
```
/
├── README.md                   # プロジェクト概要
├── start-dev.sh               # 開発サーバー起動
├── stop-dev.sh                # 開発サーバー停止
├── quick-setup.sh             # 簡単セットアップ
└── MOUSEOVER_SETTINGS_TEMPLATE.json # 設定テンプレート
```

---

### 🔴 **リリース時に除外するフォルダ**

#### 1. **`docs/`** - 開発・仕様ドキュメント
**理由**: 開発指示、技術仕様、AI指示が混在
```
docs/                           # 🔴 開発専用に変更
├── development/                # 開発指針
├── specifications/             # 技術仕様
├── api-documentation/          # API仕様
└── internal-notes/             # 内部メモ
```

#### 2. **`Operation/`** - 運用確認スクリプト
**理由**: 開発・確認用のスクリプト
```
Operation/                      # 🔴 開発確認用
├── ShellScript/               # 各種確認スクリプト
└── Memo/                      # 運用メモ
```

#### 3. **`project/`** - ユーザーデータ領域
**理由**: 完全にユーザー固有のデータ、初回起動時に生成
```
project/                        # 🔴 初回起動時に自動生成
├── projects-registry.json     # プロジェクト管理ファイル
├── cleanup_registry.py        # 整合性スクリプト
└── (各ユーザープロジェクト)   # ユーザーのプロジェクトデータ
```

#### 4. **開発専用フォルダ**
```
🔴 CLAUDE_INSTRUCTIONS/         # AI開発指示
🔴 testing/                     # テスト関連
🔴 logs/                        # 開発ログ
🔴 doc/                         # 技術仕様書（docsに統合）
🔴 venv/                        # Python仮想環境
🔴 screenshoit/                 # スクリーンショット
🔴 (各種開発・テストファイル)    # デバッグ、テスト用
```

---

## 🏗️ **新しい構造提案**

### **リリース版構造**
```
StatVizForge_JikkenPy/          # 📦 リリースパッケージ
├── README.md                   # 🎯 プロジェクト概要・セットアップ手順
├── app/                        # 💾 アプリケーション本体
│   ├── backend/               # バックエンド
│   ├── frontend/              # フロントエンド
│   └── docs/                  # 📚 ユーザー向けドキュメント
│       ├── README.md          # ドキュメント索引
│       ├── user-guide/        # 使い方ガイド
│       ├── features/          # 機能詳細
│       ├── configuration/     # 設定方法
│       └── troubleshooting/   # トラブル解決
├── deployment/                # 🚀 デプロイメント設定
├── start-dev.sh              # 🚀 開発サーバー起動
├── stop-dev.sh               # 🛑 開発サーバー停止
├── quick-setup.sh            # ⚡ 簡単セットアップ
└── MOUSEOVER_SETTINGS_TEMPLATE.json # ⚙️ 設定テンプレート
```

### **開発版構造（非公開）**
```
StatVizForge_JikkenPy/          # 🔧 開発環境
├── (リリース版と同じ構造)
├── docs/                       # 📋 開発・仕様ドキュメント
│   ├── development/           # 開発方針・指針
│   ├── specifications/        # 技術仕様・API仕様
│   ├── ai-instructions/       # AI開発指示
│   └── history/               # 開発履歴
├── Operation/                 # ⚙️ 開発確認用スクリプト
├── testing/                   # 🧪 テスト関連
├── logs/                      # 📝 開発ログ
└── project/                   # 📁 開発用プロジェクトデータ
```

---

## 🎯 **初回起動時の自動設定**

### **project/ フォルダの自動生成**
```bash
# 初回起動時に以下を自動作成
mkdir -p project/
touch project/projects-registry.json
cp scripts/cleanup_registry.py project/
echo '{"version": "1.0.0", "projects": [], "archived_projects": []}' > project/projects-registry.json
```

### **設定ファイルの初期化**
```bash
# 設定テンプレートのコピー
cp MOUSEOVER_SETTINGS_TEMPLATE.json project/.mouseover-settings-template.json
```

---

## 📋 **実装アクション**

### **Phase 1: 構造変更**
1. [ ] `app/docs/` フォルダ作成
2. [ ] 現在の `docs/` を開発専用に変更
3. [ ] ユーザー向けドキュメントを `app/docs/` に移動

### **Phase 2: 除外設定**
1. [ ] `Operation/` を開発専用に分類
2. [ ] `project/` を初回起動時生成に変更
3. [ ] リリース用 `.gitignore` 作成

### **Phase 3: 初回起動設定**
1. [ ] 初回起動時の `project/` 生成機能実装
2. [ ] セットアップスクリプトの更新
3. [ ] ユーザーガイドの作成

---

## 🔄 **ドキュメント移行計画**

### **現在の `docs/` → `app/docs/` 移行**
```
現在の docs/FEATURE_GUIDE.md → app/docs/user-guide/README.md
現在の docs/features/ → app/docs/features/
```

### **現在の `docs/` → 開発専用 `docs/` 再構成**
```
現在の doc/APIja.md → docs/specifications/api-reference.md
CLAUDE_INSTRUCTIONS/ → docs/ai-instructions/
```

---

## ✅ **品質基準**

### **リリース版の条件**
- [ ] エンドユーザーが理解できる明確な文書
- [ ] 開発内容・AI指示が含まれていない
- [ ] セットアップが30分以内で完了
- [ ] 初回起動でデータフォルダが自動生成される

### **除外条件**
- [ ] 開発者・AI向けの指示文書
- [ ] テスト・デバッグ用ファイル
- [ ] 個人的なメモ・履歴ファイル
- [ ] ユーザー固有のデータファイル

---

**このポリシーにより、エンドユーザーには必要最小限の情報のみが提供され、開発の複雑さが適切に隠蔽されます。**