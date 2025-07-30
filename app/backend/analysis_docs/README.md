# 分析ドキュメント管理システム

## 📋 概要

このディレクトリは StatVizForge における**分析手法・ガイド・ベストプラクティス**を管理する共通ドキュメントシステムです。分析タイプ先行で構造化され、多言語対応を前提とした設計になっています。

## 🌍 多言語対応方針

### 対応言語
- **ja**: 日本語（デフォルト）
- **en**: 英語
- **zh**: 中国語（簡体字）

### 言語追加時の手順
1. `_config/languages.json` に新言語追加
2. 各分析フォルダに `{言語コード}.md` ファイル作成
3. `_config/navigation.json` にナビゲーション追加

## 📁 ディレクトリ構造

```
analysis_docs/
├── README.md                    # このファイル
├── _config/                     # 設定ファイル
│   ├── languages.json          # 対応言語定義
│   ├── categories.json         # 分析カテゴリ定義
│   └── navigation.json         # ナビゲーション構造
├── exploratory/                 # 探索的分析
│   ├── data-profiling/
│   │   ├── README.md           # 概要（日本語）
│   │   ├── ja.md              # 日本語詳細版
│   │   ├── en.md              # 英語版
│   │   ├── examples/          # サンプルコード
│   │   └── media/             # 図表・画像
│   └── _category.json         # カテゴリメタデータ
├── statistical/                 # 統計分析
├── predictive/                  # 予測分析
├── visualization/               # 可視化分析
└── templates/                   # ドキュメントテンプレート
```

## 📝 ドキュメント作成ルール

### 1. 新しい分析タイプの追加

#### ステップ1: フォルダ作成
```bash
mkdir analysis_docs/{分析タイプ}/{分析名}/
```

#### ステップ2: 必須ファイル作成
```bash
# 基本構造
touch analysis_docs/{分析タイプ}/{分析名}/README.md    # 概要
touch analysis_docs/{分析タイプ}/{分析名}/ja.md       # 日本語版
mkdir analysis_docs/{分析タイプ}/{分析名}/examples/    # サンプル
mkdir analysis_docs/{分析タイプ}/{分析名}/media/       # 画像
```

#### ステップ3: メタデータ設定
各フォルダに `_meta.json` を作成：
```json
{
  "id": "exploratory.data-profiling",
  "title": {
    "ja": "データプロファイリング",
    "en": "Data Profiling",
    "zh": "数据概况分析"
  },
  "description": {
    "ja": "データの基本的な統計情報と品質を把握する手法",
    "en": "Methods to understand basic statistics and quality of data"
  },
  "difficulty": "beginner|intermediate|advanced",
  "tags": ["essential", "data-quality", "statistics"],
  "languages": ["ja", "en"],
  "lastUpdated": "2025-01-30",
  "version": "1.0.0"
}
```

### 2. ドキュメント命名規則

#### ファイル名規則
- **言語ファイル**: `{言語コード}.md` (例: `ja.md`, `en.md`)
- **概要ファイル**: `README.md` (デフォルト言語)
- **サンプルコード**: `examples/{機能名}.py` または `examples/{機能名}.ipynb`
- **画像ファイル**: `media/{説明内容}_{言語}.png`

#### フォルダ名規則
- **ケバブケース使用**: `data-profiling`, `correlation-analysis`
- **動詞+名詞形式**: `explore-patterns`, `analyze-trends`
- **英語基本、日本語併記可**: `clustering-analysis` (クラスター分析)

### 3. 分析カテゴリ定義

#### 主要カテゴリ
- **exploratory**: 探索的分析（EDA、データプロファイリング）
- **statistical**: 統計分析（相関、回帰、検定）
- **predictive**: 予測分析（機械学習、時系列予測）
- **visualization**: 可視化分析（ダッシュボード、チャート設計）
- **advanced**: 高度分析（深層学習、最適化）

#### カテゴリ追加手順
1. `_config/categories.json` に新カテゴリ定義追加
2. 対応するフォルダ作成
3. `_category.json` でカテゴリメタデータ設定

### 4. コンテンツ構造規則

#### 標準的なMarkdown構造
```markdown
# {分析手法名}

## 📋 概要
- 分析の目的・適用場面
- 必要なデータ形式
- 期待される成果

## 🎯 使用場面
- 具体的な適用シナリオ
- 業界・ドメイン別事例
- データタイプ別推奨度

## 🔧 実装手順
### 1. データ準備
### 2. 分析実行
### 3. 結果解釈

## 📊 サンプルコード
```python
# 実行可能なサンプル
```

## 📈 結果の解釈
- 出力の読み方
- 注意点・制限事項
- ベストプラクティス

## 🔗 関連リンク
- 参考文献
- 関連分析手法
- 外部ツール
```

### 5. 多言語対応規則

#### 翻訳優先度
1. **高優先度**: 基本的な探索分析、統計手法
2. **中優先度**: 可視化、予測分析
3. **低優先度**: 高度分析、特殊手法

#### 翻訳品質基準
- **専門用語統一**: 用語集（`_config/glossary.json`）準拠
- **文体統一**: 敬語不使用、簡潔な記述
- **コード部分**: コメントのみ翻訳、変数名は英語維持

### 6. バージョン管理規則

#### セマンティックバージョニング
- **Major (1.0.0)**: 構造的変更、互換性なし
- **Minor (1.1.0)**: 新機能追加、後方互換性あり
- **Patch (1.1.1)**: バグ修正、誤字修正

#### 更新時の手順
1. `_meta.json` のバージョン更新
2. `lastUpdated` 日付更新
3. 変更ログ（`CHANGELOG.md`）記録

### 7. 品質保証規則

#### レビュー必須項目
- [ ] メタデータの正確性
- [ ] コードサンプルの動作確認
- [ ] 多言語版の内容一致
- [ ] 画像・図表の適切性
- [ ] 外部リンクの有効性

#### 自動チェック項目
- Markdownリンター通過
- 画像ファイルサイズ < 1MB
- コードブロックの構文チェック

## 🚀 使用方法

### 開発者向け
```python
# Django でドキュメント読み込み
from analysis_docs.loader import AnalysisDocLoader

loader = AnalysisDocLoader()
doc = loader.get_document('exploratory/data-profiling', lang='ja')
```

### API経由アクセス
```http
GET /api/analysis-docs/exploratory/data-profiling?lang=ja
GET /api/analysis-docs/categories
GET /api/analysis-docs/search?q=correlation&lang=en
```

### フロントエンド統合
```typescript
import { useAnalysisDoc } from '@/hooks/useAnalysisDoc'

const { doc, loading } = useAnalysisDoc('statistical/correlation', 'ja')
```

## 📊 統計・監視

### ドキュメント統計
- 総ドキュメント数: 自動集計
- 言語カバレッジ: 翻訳済み割合
- 更新頻度: 月次統計

### アクセス分析
- 人気ドキュメントランキング
- 言語別利用統計
- 検索キーワード分析

---

**作成日**: 2025年1月30日  
**最終更新**: 2025年1月30日  
**管理者**: StatVizForge 開発チーム  
**レビュー者**: データ分析チーム