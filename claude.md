# このプロジェクトの概要説明
## 作成するプロダクト
### ゴール
次の二つをgithub上で公開する
- GUIをでデータの読込み・可視化・計算を行うアプリケーション   
- 上記の機能の中で、Pythonのライブラリに無い機能をライブラリとして実装し公開する。

### 機能概要
**アプリケーションUI部分**
- タブによる機能切替え（データ表示・グラフなど）
- 多言語対応（当初 日本語・英語・中国語）
- ローカルのファイルの読込み
- ローカルへの書出し
- 読み込んだデータのテーブル表示
- 読み込んだデータの可視化
- Pythonコードとのデータのやりとり  


**機能**  
- 各種機械学習・統計方法の計算  
- 別途ライブラリで実装した機能を使用できる

**ライブラリ**
- sklearn等海外のライブラリで実装していない機能
- 特に実験計画法・タグチメソッド関係

### 機能詳細
**アプリケーションUI部分**  
**機能**  
**ライブラリ**
- 実験計画法の直交表の作成


# 構成
## ファイルフォルダの構成
### 機能毎のフォルダ構成
.
├── Claude.md  
├── app  
│   ├── backend  
│   └── （バックエンドファイル） 
│   └── frontend  
├── lib  
├── project  
│   └── projects-registry.json（プロジェクト一覧の設定）
└── doc  
./Claude.md     : 全体が記述されたファイル（このファイル）  
./app           : アプリケーションのフォルダ  
./app/frontend  : Next.jsのフロントエンド（Bolt.newで生成する）  
./app/backend   : Djangoのバックエンドが入るフォルダ
./lib           : ライブラリのフォルダ  
./project       : プロジェクトのデータの入るフォルダ    構造は./doc/Claude_Codeに対する指示/datafolder.md参照
./doc           : ドキュメントのフォルダ 

# 重要な開発ルール（Claude Code全体）

## ドキュメント更新ルール
**Claude Code全体にわたって適用される重要なルール：**
- **1時間に1回、または「ドキュメントの更新」指示があった場合**
- **~/doc/docja.mdを更新（追加）すること**
- 新しく実装した機能、API仕様の変更、設定の変更、発生した問題と解決方法、開発の進捗状況を含める

## API変更時の対応ルール
APIの仕様を変更した場合は以下をすべて実行：
1. ~/app/frontend/BOLT_NEW_INSTRUCTIONS.mdの内容を変更
2. ~/doc/APIja.mdに変更内容を詳細に記述（人間が理解できるよう丁寧に）
3. ~/app/frontend/doc/APIja.mdにも同じ内容を記述（フロントエンド開発者用のAPI仕様書）

**重要**: ~/doc/APIja.mdと~/app/frontend/doc/APIja.mdは常に同じ内容を保つこと。一方を変更した場合は必ず他方も同じ内容に更新する。

## 言語指定の標準ルール
すべてのAPIエンドポイントで統一した言語指定方法を採用：

### 実装方式
- **クエリパラメータ`lang`を使用**
- 例：`POST /api/projects/create?lang=ja`

### サポート言語
- `en`: 英語（デフォルト）
- `ja`: 日本語  
- `zh`: 中国語

### ルール
1. **言語指定がない場合は英語で応答**
2. **エラーメッセージも指定言語で返す**
3. **すべてのAPIエンドポイントで対応必須**
4. **サポートしない言語コードが指定された場合は英語で応答**

### エラーレスポンス標準形式
```json
{
  "error": "ERROR_CODE",           // 言語非依存のエラーコード
  "message": "localized message",  // 指定言語のエラーメッセージ
  "details": {                     // 詳細エラー（オプション）
    "field_name": "field error"
  }
}
```

## フロントエンド変更時のGit操作
frontendフォルダ内のファイルを変更した際は、必ずGitにpushすること

## 開発環境自動管理ルール
**Claude Code起動時とコード変更時の自動サーバー管理：**

### 1. 起動時の自動サーバー起動
Claude Code起動時に以下のスクリプトを自動実行：
```bash
./start-dev.sh
```
- Djangoバックエンド（ポート8000）を起動
- Next.jsフロントエンド（ポート3000-3002）を起動
- 起動状況を確認してログ出力
- PIDファイルでプロセス管理

### 2. コード変更時の再起動判断
以下の変更時はClaude Codeが自動で再起動判断・実行：

**バックエンド再起動が必要な場合**:
- 新しいPythonファイル追加時
- settings.py変更時
- INSTALLED_APPSやミドルウェア変更時
- 新しいライブラリのインストール後
→ `./restart-backend.sh` を実行

**フロントエンド再起動が必要な場合**:
- package.json変更時
- next.config.js変更時
- 環境変数(.env)変更時
- 新しいnpmパッケージインストール後
→ `./restart-frontend.sh` を実行

**両方再起動が必要な場合**:
- 大幅な設定変更時
→ `./stop-dev.sh && ./start-dev.sh` を実行

### 3. 利用可能なスクリプト
- `./start-dev.sh` - 開発環境全体起動
- `./stop-dev.sh` - 開発環境全体停止
- `./restart-backend.sh` - バックエンドのみ再起動
- `./restart-frontend.sh` - フロントエンドのみ再起動

### 4. ログ確認
- バックエンドログ: `logs/backend.log`
- フロントエンドログ: `logs/frontend.log`
- リアルタイム確認: `tail -f logs/*.log`

## 終了時のドキュメント更新ルール
**「終了」という指示を受けた場合の必須作業：**

### 1. 仕様書の更新
- `/Claude.md`に当日の作業内容を追記
- 実装した機能、変更内容、技術仕様を詳細に記録
- 動作確認済み機能と残件を明記

### 2. バグ履歴の記録
- `/doc/history/YYYYMMDD.md`ファイルに当日発生したバグと対応を記録
- **同日に複数回「終了」指示があった場合は同ファイルに追記**
- 発生時刻、症状、原因分析、対応内容、結果を詳細に記録

### 3. ファイル命名規則
- バグ履歴ファイル名: `YYYYMMDD.md`（例：`20250123.md`）
- 同日の場合は既存ファイルに「## 追加セッション（時刻）」として追記

### 4. 必須記録項目
**仕様書更新**:
- 実装概要
- 作業項目詳細
- 技術仕様
- 動作確認済み機能
- 残件・今後の課題

**バグ履歴**:
- 発生したバグの詳細
- 原因分析
- 対応内容
- 技術的学習ポイント
- 今後の改善点

# 2025年1月23日の作業内容

## 実装概要
新規プロジェクト作成ポップアップダイアログの完全実装

## 作業項目詳細

### 1. デザイン仕様書の作成
**ファイル**: `/app/frontend/doc/design/newProjectDialog.md`
**内容**:
- ポップアップダイアログのUI設計仕様
- フォーム要素とバリデーションルール
- ユーザーインタラクションフロー
- レスポンシブ対応とアクセシビリティ要件

### 2. 新規プロジェクト作成ダイアログコンポーネントの実装
**ファイル**: `/app/frontend/components/NewProjectDialog.tsx`
**実装機能**:
- モーダルダイアログ（最大幅600px）
- React Hook Form + Zodによるフォームバリデーション
- 以下のフォーム要素：
  - フォルダ名（必須、英数字・ハイフン・アンダースコア制限）
  - プロジェクト名（必須、最大100文字）
  - 説明（任意、最大500文字）
  - タグ（任意、最大10個、Enterキー/カンマ区切りで追加）
  - ステータス（active/in_progress/completed）

### 3. リアルタイム重複チェック機能
**実装内容**:
- ダイアログ開示時に既存プロジェクトのフォルダ名を取得
- フォルダ名入力時の即座バリデーション（デバウンスなし）
- 重複検出時の即座エラー表示
- MSWモックデータとの連携

**重複チェック対象フォルダ名**:
- `temperature-analysis`
- `machine-learning-demo`
- `data-visualization`

### 4. マルチポイント起動対応
**統合ポイント**:
1. **メニューバーから**: ファイル → プロジェクト → 新規
2. **プロジェクト画面から**:
   - ヘッダーの「+」アイコンボタン
   - 「新規プロジェクト」ボタン
   - プロジェクトなし時の「最初のプロジェクトを作成」ボタン

**変更ファイル**:
- `/app/frontend/app/page.tsx` - ダイアログ状態管理とprops渡し
- `/app/frontend/components/MenuBar.tsx` - メニューからの起動処理
- `/app/frontend/components/ProjectList.tsx` - プロジェクト画面からの起動処理

### 5. 国際化対応とエラーハンドリング
**実装内容**:
- 多言語対応（日本語テキストをハードコーディング）
- バリデーションエラーの即座表示
- API連携エラーのトースト通知
- 成功時のプロジェクト一覧更新

### 6. パフォーマンス問題の解決
**発生した問題**:
- フロントエンド起動時間の遅延
- TypeScriptインポートパスエラー

**解決内容**:
- `tsconfig.json`のパス設定修正: `"@/*": ["./*", "./src/*"]`
- ポート競合の解決（ポート3000使用プロセスの終了）
- i18n関数使用方法の修正（`useI18n`→`getTranslation`）

### 7. MSW（Mock Service Worker）連携
**確認・修正内容**:
- MSWの設定状況確認
- モックデータの確認（3つの既存プロジェクト）
- インポートパス問題の修正
- 重複チェック機能の正常動作確認

## 技術仕様

### 使用技術スタック
- **UI Framework**: Next.js 13 (App Router)
- **UIコンポーネント**: shadcn/ui (Radix UI + Tailwind CSS)
- **フォーム管理**: React Hook Form
- **バリデーション**: Zod
- **状態管理**: React useState/useEffect
- **モック**: MSW (Mock Service Worker)

### API連携
- **エンドポイント**: `GET /api/projects/list` - 既存プロジェクト一覧取得
- **エンドポイント**: `POST /api/projects/create` - 新規プロジェクト作成
- **認証**: なし（開発段階）
- **エラーハンドリング**: Try-catch + トースト通知

### データ構造
```typescript
interface Project {
  id?: number;
  folder_name: string;      // 重複チェック対象
  project_name: string;     // 表示名
  description: string;      // 説明文
  tags: string[];          // タグ配列
  status: string;          // active/in_progress/completed
  created_date?: string;   // 作成日時
  modified_date?: string;  // 更新日時
}
```

## 動作確認済み機能
✅ ポップアップダイアログの表示・非表示
✅ フォームバリデーション（全項目）
✅ リアルタイム重複チェック
✅ タグの追加・削除機能
✅ エラーメッセージ表示
✅ 成功時のトースト通知
✅ マルチポイントからの起動
✅ MSWモックデータとの連携

## 残件・今後の課題
- 実際のバックエンドAPI（Django）との連携テスト ✅ **完了**
- 多言語対応の完全実装（現在は日本語固定）
- プロジェクト作成後のプロジェクトページへの遷移
- ファイルアップロード機能との連携
- エラーログの詳細化

---

## 2025年1月23日 追加セッション（夜間）の作業内容

### 実装概要
実環境開発体制の構築とバックエンドAPI実装

### 追加作業項目詳細

#### 1. バックエンドAPI実装（新規プロジェクト作成）
**ファイル**: `/app/backend/api/views.py`
**実装機能**:
- プロジェクトフォルダ構造の自動作成
- project.jsonファイルの生成
- projects-registry.jsonの更新
- datafolder.mdで定義された仕様通りのフォルダ構造実装

**作成されるフォルダ構造**:
```
project/
└── {folder_name}/
    ├── project.json     # プロジェクト詳細情報
    ├── raw/            # アップロードされた生データ
    ├── db/             # データベースファイル
    ├── analysisdata/   # 分析結果
    └── git/            # 分析履歴
```

#### 2. MSWモック無効化と実環境切り替え
**変更ファイル**: `/app/frontend/app/msw-provider.tsx`
**変更内容**:
- MSW（Mock Service Worker）を無効化
- 実際のDjangoバックエンドAPIとの連携に切り替え
- "MSW disabled - using real backend API" ログ出力

#### 3. 開発環境自動管理システム構築
**作成スクリプト**:
- `start-dev.sh` - 開発環境全体起動（Django + Next.js）
- `stop-dev.sh` - 開発環境全体停止
- `restart-backend.sh` - Djangoサーバーのみ再起動
- `restart-frontend.sh` - Next.jsサーバーのみ再起動

**機能**:
- PIDファイルによるプロセス管理
- ログファイル分離（backend.log / frontend.log）
- ポート自動検出（3000-3002）
- 起動状況の自動確認

#### 4. Claude Code自動管理ルールの設定
**ルール策定**:
- 起動時の自動サーバー起動
- コード変更時の再起動要否判断
- バックエンド/フロントエンド個別再起動対応

**再起動が必要な変更パターン**:
- バックエンド: 新Pythonファイル追加、settings.py変更、ライブラリ追加
- フロントエンド: package.json変更、next.config.js変更、環境変数変更

### 技術仕様（追加分）

#### Django開発環境
- **仮想環境**: Python 3.12 + venv
- **依存関係**: Django 5.2.4, DRF 3.16.0, django-cors-headers 4.7.0
- **自動リロード**: StatReloader有効
- **ポート**: 8000（固定）

#### Next.js開発環境
- **ポート**: 3000-3002（自動検出）
- **モード**: 実環境API連携
- **MSW**: 無効化済み

#### プロジェクトデータ管理
- **レジストリファイル**: `project/projects-registry.json`
- **個別プロジェクト**: `project/{folder_name}/project.json`
- **データ形式**: UTF-8 JSON（ensure_ascii=False）

### 動作確認済み機能（追加分）
✅ Djangoバックエンド起動・API応答確認
✅ Next.jsフロントエンド起動確認
✅ MSWモック無効化
✅ 実環境API連携準備完了
✅ 開発環境自動管理スクリプト動作確認
✅ プロジェクトフォルダ構造作成機能
✅ project.json生成機能
✅ projects-registry.json更新機能

### 新たな残件・今後の課題
- 実環境での新規プロジェクト作成ダイアログのテスト
- フォルダ作成権限とパスの検証
- エラーハンドリングの強化（フォルダ作成失敗時）
- プロジェクト削除時のフォルダ削除機能
- ファイルアップロード機能のraw/フォルダ連携

---

## 2025年7月28日の作業内容

### 実装概要
ファイル説明専用APIシステムの完成とプロジェクトフォルダ仕様書の作成

### 作業項目詳細

#### 1. ファイル説明APIのバグ修正と完成
**発生したバグ**:
- HTTP 415エラー: DjangoのFileViewSetにJSONParserが未設定
- name 'json' is not definedエラー: jsonモジュール未インポート

**修正内容**:
- `/app/backend/api/views.py`にJSONParser追加とjsonモジュールインポート
- `parser_classes = (MultiPartParser, FormParser, JSONParser)`に修正

**結果**: 
- POST/GETエンドポイント正常動作
- `analysisdata/file_descriptions.json`への保存成功
- 日本語ファイル名の正常処理

#### 2. プロジェクトフォルダ仕様書の作成
**ファイル**: `/app/doc/PROJECT_FOLDER_SPECIFICATION.md`

**内容**:
- プロジェクト基本構造定義
- 全JSONファイル仕様（project.json, file_descriptions.json等）
- API エンドポイント一覧
- 命名規則とセキュリティ要件
- バックアップ・アーカイブ処理仕様
- エラーハンドリングとメンテナンス方針

#### 3. 開発環境の安定化
**問題と対応**:
- WSL環境でのpython/python3コマンド問題 → python3使用で解決
- Django仮想環境の適切なアクティベート
- ポート競合問題の解決

### 技術仕様

#### ファイル説明API
- **エンドポイント**: `/api/files/descriptions/{project_folder}/`
- **保存場所**: `{project_folder}/analysisdata/file_descriptions.json`
- **データ形式**:
```json
{
  "filename.csv": {
    "description": "説明",
    "updated": "2025-07-28T23:33:30.790231",
    "author": "システム"
  }
}
```

#### プロジェクト構造標準化
- **必須フォルダ**: `raw/`（生データ）、`analysisdata/`（メタデータ）
- **設定ファイル**: `project.json`（プロジェクト情報）
- **管理ファイル**: `projects-registry.json`（プロジェクト一覧）

### 動作確認済み機能
✅ ファイル説明保存・取得API（POST/GET）
✅ analysisdataフォルダへの専用保存
✅ 日本語ファイル名対応
✅ エラーハンドリング（編集モード終了）
✅ Firefox UI での動作確認
✅ プロジェクトフォルダ仕様書完成

### 残件・今後の課題
- ファイルタグシステムの同様の修正
- UI改善（×ボタン、キーボードショートカット）の継続テスト
- プロジェクト終了ボタン機能のテスト
- 大量ファイル処理時のパフォーマンス最適化
- セキュリティ強化（ファイルパス検証等）
