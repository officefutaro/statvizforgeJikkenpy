# マウスオーバー統計表示機能 詳細仕様

**機能名**: マウスオーバー統計表示（MouseOver Statistics Display）  
**バージョン**: 2.0.0  
**最終更新**: 2025年8月1日

## 📋 機能概要

CSVデータ表示時に、セル上にマウスカーソルを置くことで、そのデータ列に関する統計情報をリアルタイムで表示する高度な分析機能です。

## ✅ 利用可能条件

### 必須条件
- [ ] **ファイル形式**: CSV形式のデータファイル
- [ ] **プロジェクト**: 有効なプロジェクト内のファイル
- [ ] **データ**: 最低1行以上のデータが存在
- [ ] **バックエンドAPI**: `/api/v1/table-settings/mouseover-settings/` が正常動作

### 推奨条件
- [ ] **データサイズ**: 10,000行以下（パフォーマンス最適化のため）
- [ ] **列数**: 50列以下（表示品質のため）
- [ ] **数値データ**: 統計計算可能な数値列の存在

### システム要件
- [ ] **ブラウザ**: Chrome 90+, Firefox 88+, Safari 14+
- [ ] **JavaScript**: 有効化必須
- [ ] **メモリ**: 最低512MB以上の利用可能メモリ
- [ ] **CPU**: 統計計算処理のため中程度以上の性能

### 設定ファイル要件
- [ ] **設定ファイル**: `{プロジェクト}/.mouseover-settings.json` の存在
- [ ] **権限**: 設定ファイルの読み取り権限
- [ ] **フォーマット**: 有効なJSON形式

## 🎯 機能詳細

### 表示モード

#### 1. ツールチップモード (tooltip)
- **表示位置**: マウスカーソル近くの小さなポップアップ
- **表示内容**: 基本統計情報（平均、中央値、最大最小値）
- **適用場面**: 簡単な情報確認
- **パフォーマンス**: 軽量・高速

#### 2. サイドバーモード (sidebar)
- **表示位置**: 画面右側の固定パネル
- **表示内容**: 詳細統計情報（全ての統計指標）
- **適用場面**: 詳細分析・比較検討
- **パフォーマンス**: 中程度

#### 3. オーバーレイモード (overlay)
- **表示位置**: テーブル上の半透明レイヤー
- **表示内容**: グラフィカルな統計表示
- **適用場面**: データ分布の視覚的確認
- **パフォーマンス**: 重い（大量データでは注意）

### 統計指標

#### 基本統計
- **平均値** (Mean): 数値データの算術平均
- **中央値** (Median): データの中央に位置する値
- **最頻値** (Mode): 最も頻繁に出現する値
- **最大値** (Max): データの最大値
- **最小値** (Min): データの最小値
- **データ数** (Count): 有効データの個数
- **欠損値数** (Null Count): 空白・null値の個数

#### 分散統計
- **標準偏差** (Standard Deviation): データのばらつき度合い
- **分散** (Variance): 標準偏差の二乗値
- **四分位数** (Quartiles): Q1, Q2, Q3の値
- **範囲** (Range): 最大値 - 最小値
- **四分位範囲** (IQR): Q3 - Q1

#### 高度統計
- **歪度** (Skewness): データ分布の非対称性
- **尖度** (Kurtosis): データ分布の尖り具合
- **パーセンタイル** (Percentiles): 任意の百分位数
- **異常値検出** (Outliers): 統計的異常値の識別

### データ型別対応

#### 数値型 (Numeric)
- **対応統計**: 全ての統計指標が利用可能
- **表示形式**: 小数点以下2桁まで表示
- **特殊処理**: 異常値の自動検出・マーキング

#### 文字列型 (String)
- **対応統計**: カウント、最頻値、ユニーク数
- **表示形式**: 文字数制限（20文字まで）
- **特殊処理**: 文字列長の統計

#### 日付型 (Date)
- **対応統計**: 最新日、最古日、期間範囲
- **表示形式**: YYYY-MM-DD形式
- **特殊処理**: 日付範囲の可視化

#### 順序型 (Ordinal)
- **対応統計**: カスタム順序での並び順統計
- **表示形式**: カスタム順序に基づく表示
- **特殊処理**: 順序関係の維持

## ⚙️ 設定ファイル仕様

### ファイル場所
```
project/{プロジェクト名}/.mouseover-settings.json
```

### 基本構造
```json
{
  "version": "1.0.0",
  "last_updated": "2025-08-01T12:00:00Z",
  "displayOptions": [...],
  "globalSettings": {...}
}
```

### displayOptions 詳細設定

#### basic_info オプション
```json
{
  "id": "basic_info",
  "enabled": true,
  "category": "basic",
  "displayPosition": "tooltip",
  "name": "基本情報",
  "description": "データ型、値の範囲など",
  "options": {
    "showDataType": true,
    "showValueRange": true,
    "showSampleValues": true,
    "maxSampleCount": 3
  }
}
```

#### statistics オプション
```json
{
  "id": "statistics",
  "enabled": true,
  "category": "statistics",
  "displayPosition": "sidebar",
  "name": "統計情報",
  "description": "平均、中央値、標準偏差など",
  "options": {
    "showMean": true,
    "showMedian": true,
    "showMode": true,
    "showStdDev": true,
    "showVariance": false,
    "showQuartiles": true,
    "showSkewness": false,
    "showKurtosis": false,
    "showMin": true,
    "showMax": true,
    "showCount": true,
    "showNullCount": true,
    "showRange": true,
    "showIQR": false,
    "decimalPlaces": 2
  }
}
```

#### distribution オプション
```json
{
  "id": "distribution",
  "enabled": false,
  "category": "advanced",
  "displayPosition": "overlay",
  "name": "分布情報",
  "description": "ヒストグラム、パーセンタイルなど",
  "options": {
    "showHistogram": true,
    "histogramBins": 10,
    "showPercentiles": true,
    "percentileValues": [25, 50, 75, 90, 95],
    "showOutliers": true,
    "outlierMethod": "iqr",
    "showDensityCurve": false
  }
}
```

#### data_quality オプション
```json
{
  "id": "data_quality",
  "enabled": false,
  "category": "quality",
  "displayPosition": "overlay",
  "name": "データ品質",
  "description": "欠損値、異常値の検出",
  "options": {
    "showMissingValues": true,
    "showMissingPercentage": true,
    "showOutliers": true,
    "showDuplicates": false,
    "showDataConsistency": true,
    "outlierThreshold": 2.0,
    "duplicateThreshold": 0.05
  }
}
```

### globalSettings 詳細設定
```json
{
  "globalSettings": {
    "defaultDisplayMode": "tooltip",
    "animationEnabled": true,
    "animationDuration": 200,
    "showOnlyForNumericColumns": false,
    "delayMs": 300,
    "hideDelayMs": 100,
    "maxDisplayItems": 10,
    "theme": "light",
    "fontSize": "14px",
    "maxWidth": "300px",
    "zIndex": 1000,
    "backgroundColor": "#ffffff",
    "borderColor": "#cccccc",
    "textColor": "#333333",
    "enableCaching": true,
    "cacheTimeout": 60000,
    "enableDebugMode": false
  }
}
```

## 🔧 カスタマイズ例

### 軽量設定（高速表示）
```json
{
  "displayOptions": [
    {
      "id": "basic_info",
      "enabled": true,
      "displayPosition": "tooltip"
    }
  ],
  "globalSettings": {
    "delayMs": 100,
    "animationEnabled": false,
    "enableCaching": true
  }
}
```

### 詳細分析設定（全機能有効）
```json
{
  "displayOptions": [
    {
      "id": "statistics",
      "enabled": true,
      "displayPosition": "sidebar",
      "options": {
        "showMean": true,
        "showMedian": true,
        "showStdDev": true,
        "showQuartiles": true,
        "showSkewness": true,
        "showKurtosis": true
      }
    },
    {
      "id": "distribution",
      "enabled": true,
      "displayPosition": "overlay"
    }
  ]
}
```

### データ品質チェック設定
```json
{
  "displayOptions": [
    {
      "id": "data_quality",
      "enabled": true,
      "displayPosition": "sidebar",
      "options": {
        "showMissingValues": true,
        "showOutliers": true,
        "showDuplicates": true,
        "outlierThreshold": 1.5
      }
    }
  ]
}
```

## 🚀 パフォーマンス最適化

### 推奨設定
- **大量データ（10,000行以上）**: tooltipモードのみ使用
- **リアルタイム分析**: キャッシュ有効化
- **低スペック環境**: アニメーション無効化

### 制限事項
- **最大行数**: 100,000行まで
- **最大列数**: 100列まで
- **同時表示**: 1つの統計パネルのみ
- **メモリ使用量**: 統計データで最大100MB

## 🐛 トラブルシューティング

### よくある問題

#### 統計情報が表示されない
**原因**: 設定ファイルの読み込みエラー  
**解決**: JSON形式の確認、ファイル権限の確認

#### 表示が遅い
**原因**: 大量データでの重い統計計算  
**解決**: displayModeを"tooltip"に変更、キャッシュ有効化

#### 数値が正しくない
**原因**: データ型の自動判定ミス  
**解決**: 列メタデータでデータ型を明示的に指定

## 📊 使用例

### 売上データ分析
```
列: 月別売上金額
統計: 平均￥1,250,000、中央値￥1,180,000、標準偏差￥340,000
分布: 正規分布に近い、異常値2個検出
```

### 顧客年齢データ
```
列: 顧客年齢
統計: 平均42.3歳、中央値39歳、最頻値35歳
分布: 右に歪んだ分布、高齢層に異常値あり
```

## 🔄 今後の拡張予定

- **機械学習統計**: 相関分析、回帰統計
- **時系列統計**: トレンド分析、季節性検出
- **多変量統計**: 主成分分析、クラスター分析
- **インタラクティブグラフ**: 統計グラフの操作機能

---

**関連ドキュメント**:
- [機能ガイド](../FEATURE_GUIDE.md)
- [設定テンプレート](../../MOUSEOVER_SETTINGS_TEMPLATE.json)
- [API仕様書](../APIja.md)