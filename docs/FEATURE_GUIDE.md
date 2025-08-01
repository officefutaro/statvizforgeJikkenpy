# StatVizForge 機能ガイド

**最終更新日**: 2025年8月1日  
**対象バージョン**: v2.0.0

---

## 📂 詳細機能ドキュメント

複雑な機能については、専用の詳細ドキュメントを参照してください：

- **[マウスオーバー統計表示機能](features/mouseover-statistics.md)** - 高度な統計分析機能の完全仕様

---

## 📊 表表示機能（TableViewer）

### 基本表示機能
- **場所**: プロジェクト → ファイル → CSV選択
- **機能**: CSVファイルをテーブル形式で表示
- **操作**: 列幅調整、ソート、フィルタ

### 🌟 高機能ビューア（Advanced Viewer）
**ボタン名**: 「高機能ビューア」（日本語）/ "Advanced Viewer"（英語）  
**アイコン**: ✨ Sparkles  
**場所**: CSVテーブル表示画面の右上ツールバー

#### ✅ 利用可能条件
- **ファイル形式**: CSV形式のデータファイル
- **プロジェクト**: 有効なプロジェクト内のファイル  
- **データ**: 最低1行以上のデータが存在
- **バックエンドAPI**: マウスオーバー設定APIが正常動作
- **ブラウザ**: JavaScript有効化必須

#### 機能概要
1. **マウスオーバー統計表示**
   - セル上にマウスを置くと統計情報を表示
   - 平均値、中央値、標準偏差、四分位数など
   - サイドバー、ツールチップ、オーバーレイの表示モード選択可能

2. **高度な設定機能**
   - 列データ型の詳細設定
   - カスタム順序設定（順序データ用）
   - グラフ表示との連携

**📋 詳細仕様**: [マウスオーバー統計表示機能](features/mouseover-statistics.md)を参照

#### 設定ファイル
- **保存場所**: `project/{プロジェクト名}/`
- **ファイル名**: `.mouseover-settings.json`（隠しファイル）
- **テンプレート**: `MOUSEOVER_SETTINGS_TEMPLATE.json`

## 🎯 現在の問題と解決方法

### 問題: 高機能ビューアが起動しない
**エラー**: `500 Internal Server Error` at `/api/v1/table-settings/mouseover-settings/`

**原因**: バックエンドAPIの実装不備

**対処法**:
1. バックエンドAPIの修正が必要
2. 一時的な回避策: 基本テーブル表示を使用

## 📁 設定ファイル形式（人間が編集可能）

### マウスオーバー設定ファイル
**ファイルパス**: `project/{プロジェクト名}/table-settings/mouseover_settings.json`

```json
{
  "version": "1.0.0",
  "last_updated": "2025-08-01T12:00:00Z",
  "displayOptions": [
    {
      "id": "basic_info",
      "enabled": true,
      "category": "basic",
      "displayPosition": "tooltip",
      "name": "基本情報",
      "description": "データ型、値の範囲など"
    },
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
        "showStdDev": true,
        "showQuartiles": true,
        "showSkewness": false,
        "showKurtosis": false
      }
    },
    {
      "id": "data_quality",
      "enabled": false,
      "category": "quality",
      "displayPosition": "overlay",
      "name": "データ品質",
      "description": "欠損値、異常値の検出"
    }
  ],
  "globalSettings": {
    "defaultDisplayMode": "tooltip",
    "animationEnabled": true,
    "showOnlyForNumericColumns": false,
    "delayMs": 300
  }
}
```

### 表表示設定ファイル
**ファイルパス**: `project/{プロジェクト名}/table-settings/{ファイル名}_settings.json`

```json
{
  "id": "project_filename_timestamp",
  "projectFolder": "project_name",
  "fileName": "data.csv",
  "createdAt": "2025-08-01T12:00:00Z",
  "updatedAt": "2025-08-01T12:00:00Z",
  "tableConfig": {
    "visibleColumns": ["column1", "column2", "column3"],
    "columnOrder": ["column1", "column2", "column3"],
    "columnWidths": {
      "column1": 150,
      "column2": 200,
      "column3": 100
    },
    "sortConfig": {
      "column": "column1",
      "direction": "asc"
    },
    "filters": {
      "column1": {
        "type": "text",
        "value": "filter_value"
      }
    },
    "pageSize": 50
  },
  "chartConfig": {
    "enabled": true,
    "type": "bar",
    "xAxis": "column1",
    "yAxis": "column2",
    "colorScheme": "blue",
    "showLegend": true,
    "showGrid": true
  },
  "layoutConfig": {
    "split": "horizontal",
    "tableRatio": 0.6,
    "chartRatio": 0.4,
    "hoverMode": "sidebar"
  },
  "columnMetadata": {
    "column1": {
      "name": "column1",
      "dataType": "numeric",
      "displayName": "列1",
      "format": "decimal",
      "decimalPlaces": 2
    },
    "column2": {
      "name": "column2",
      "dataType": "ordinal",
      "displayName": "列2",
      "ordinalConfig": {
        "customOrder": ["低", "中", "高"],
        "sortDirection": "custom",
        "autoDetectOrder": false
      }
    }
  }
}
```

## 🔧 手動設定の編集方法

### 1. マウスオーバー統計の有効化/無効化
```json
{
  "displayOptions": [
    {
      "id": "statistics",
      "enabled": true,  // ← true/falseで切り替え
      "options": {
        "showMean": true,     // 平均値表示
        "showMedian": true,   // 中央値表示
        "showStdDev": false   // 標準偏差非表示
      }
    }
  ]
}
```

### 2. 表示モードの変更
```json
{
  "displayOptions": [
    {
      "displayPosition": "tooltip"  // "tooltip" | "sidebar" | "overlay"
    }
  ]
}
```

### 3. 列の表示/非表示
```json
{
  "tableConfig": {
    "visibleColumns": ["必要な列名のみ記載"]
  }
}
```

### 4. 列の順序変更
```json
{
  "tableConfig": {
    "columnOrder": ["表示したい順番で列名を記載"]
  }
}
```

## 📞 トラブルシューティング

### Q: 高機能ビューアボタンが見つからない
**A**: CSVファイルを開いている状態で、画面右上のツールバーを確認してください。✨アイコンのボタンです。

### Q: マウスオーバーしても統計情報が表示されない
**A**: 現在バックエンドAPIにエラーがあります。修正が必要です。

### Q: 設定が保存されない
**A**: プロジェクトフォルダに`table-settings`ディレクトリが存在することを確認してください。

### Q: カスタム設定を適用したい
**A**: 上記のJSONファイル形式に従って、プロジェクトフォルダ内の設定ファイルを直接編集してください。

---

## 🎯 今後の改善予定

1. **バックエンドAPIエラーの修正**
2. **設定UI の改善**
3. **より多くの統計指標の追加**
4. **グラフ表示機能の強化**

---

**注意**: 設定ファイルを手動編集する際は、JSON形式が正しいことを確認してください。不正なJSONは機能を停止させる可能性があります。