# ConfigurableTableViewer 技術仕様書

## 📋 概要

ConfigurableTableViewer は StatVizForge の高度な表表示機能を提供するメインコンポーネントです。マウスオーバー連動、設定管理、順序決定の3つの核心機能を統合しています。

## 🎯 機能概要

### 1. マウスオーバー連動グラフ表示
- **リアルタイム更新**: テーブル行のホバー時にチャートが動的更新
- **詳細情報表示**: ホバー時の関連データ・トレンド情報表示
- **5種類のチャート**: 棒・線・円・散布図・エリアチャート対応

### 2. 設定ボタンと表示項目変更
- **統合設定ダイアログ**: 表・チャート・レイアウトの包括管理
- **リアルタイム反映**: 設定変更の即座な画面反映
- **永続化**: 設定内容のデータベース保存

### 3. 順序量データの順序決定
- **ドラッグ&ドロップ**: 直感的な順序変更UI
- **自動並び替え**: 推奨順序・頻度順・アルファベット順
- **プレビュー表示**: 変更結果の事前確認

## 📁 ファイル構成

```
components/
├── ConfigurableTableViewer.tsx     # メインコンポーネント
├── DynamicChart.tsx               # 動的チャート表示
├── TableSettingsDialog.tsx       # 設定ダイアログ
└── OrdinalOrderSettings.tsx      # 順序設定ダイアログ

types/
└── data-types.ts                 # 型定義

utils/
└── data-sorting.ts              # データ処理ユーティリティ

__tests__/
├── ConfigurableTableViewer.test.tsx
└── DynamicChart.test.tsx

e2e/
└── configurable-table-viewer.spec.ts
```

## 🔧 技術スタック

### フロントエンド
- **React 18**: 関数コンポーネント・hooks
- **TypeScript**: 完全型安全性
- **Tailwind CSS**: ユーティリティファースト
- **Recharts**: データ可視化ライブラリ
- **react-beautiful-dnd**: ドラッグ&ドロップ

### バックエンド
- **Django**: REST API・データ永続化
- **PostgreSQL/SQLite**: 設定データストレージ
- **Django REST Framework**: API実装

### テスト
- **Jest**: 単体テスト・コンポーネントテスト
- **Testing Library**: DOM操作テスト
- **Playwright**: E2Eテスト・GUI操作テスト

## 🏗️ アーキテクチャ

### コンポーネント階層
```
ConfigurableTableViewer
├── TableArea (メインテーブル表示)
├── ChartArea (DynamicChart)
├── SettingsDialog (TableSettingsDialog)
│   ├── DisplayTab (表示設定)
│   ├── ChartTab (チャート設定)
│   └── LayoutTab (レイアウト設定)
└── OrdinalDialog (OrdinalOrderSettings)
    ├── AutoSortButtons (自動並び替え)
    ├── DragDropList (手動並び替え)
    └── PreviewArea (プレビュー表示)
```

### データフロー
```
1. データ取得 → 2. 設定適用 → 3. 表示処理 → 4. ユーザー操作 → 5. 設定更新
     ↑                                                               ↓
     ←←←←←←←←←←←← 6. データベース保存 ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```

## 📊 データ構造

### TableDisplaySettings
```typescript
interface TableDisplaySettings {
  id: string
  projectFolder: string
  fileName: string
  createdAt: string
  updatedAt: string
  
  tableConfig: {
    visibleColumns: string[]
    columnOrder: string[]
    columnWidths: Record<string, number>
    sortConfig: { column: string; direction: 'asc' | 'desc' } | null
    filters: Record<string, any>
    pageSize: number
  }
  
  chartConfig: {
    enabled: boolean
    type: 'bar' | 'line' | 'pie' | 'scatter' | 'area'
    xAxis: string
    yAxis: string | string[]
    groupBy?: string
    colorScheme: string
    showLegend: boolean
    showGrid: boolean
    hoverDetails: {
      enabled: boolean
      showTrend: boolean
      showBreakdown: boolean
      showComparison: boolean
    }
  }
  
  layoutConfig: {
    split: 'horizontal' | 'vertical' | 'overlay'
    tableRatio: number
    chartRatio: number
    hoverMode: 'tooltip' | 'sidebar' | 'overlay' | 'split'
  }
  
  columnMetadata: Record<string, ColumnMetadata>
}
```

### ColumnMetadata
```typescript
interface ColumnMetadata {
  name: string
  dataType: 'nominal' | 'ordinal' | 'interval' | 'ratio' | 'datetime' | 'text'
  displayName: string
  
  ordinalConfig?: {
    customOrder: string[]
    sortDirection: 'asc' | 'desc' | 'custom'
    autoDetectOrder: boolean
  }
  
  numericConfig?: {
    format: 'decimal' | 'currency' | 'percentage'
    decimalPlaces: number
    unit?: string
  }
  
  datetimeConfig?: {
    format: string
    timezone?: string
  }
}
```

## 🎨 UI/UX 設計

### レスポンシブ対応
- **デスクトップ**: 水平分割レイアウト (表60% + チャート40%)
- **タブレット**: 垂直分割レイアウト (表70% + チャート30%)
- **モバイル**: タブ切り替えレイアウト (表/チャート個別表示)

### アクセシビリティ
- **キーボードナビゲーション**: Tab/Enter/Escape/矢印キー対応
- **ARIA属性**: スクリーンリーダー対応
- **コントラスト**: WCAG 2.1 AA準拠
- **フォーカス表示**: 明確なフォーカスインジケーター

### パフォーマンス最適化
- **仮想スクロール**: 大量データ対応
- **メモ化**: useMemo/useCallback活用
- **遅延ローディング**: チャートライブラリの動的読み込み
- **デバウンス**: ホバー・検索処理の最適化

## 🔌 API 仕様

### 設定管理 API
```http
# 設定取得
GET /api/table-settings/settings/{project_folder}/{file_name}/
Response: { success: true, settings: TableDisplaySettings | null }

# 設定保存
POST /api/table-settings/settings/{project_folder}/{file_name}/
Body: TableDisplaySettings
Response: { success: true, settings: TableDisplaySettings, created: boolean }

# 設定削除
DELETE /api/table-settings/settings/{project_folder}/{file_name}/
Response: { success: true, message: string }

# プロジェクト設定一覧
GET /api/table-settings/settings/{project_folder}/
Response: { success: true, settings: TableDisplaySettings[], total: number }
```

### テーブルデータ API
```http
# CSVデータ取得
GET /api/files/table/{project_folder}/?file_path=raw/data.csv
Response: {
  success: true,
  headers: string[],
  rows: string[][],
  total_rows: number,
  is_truncated: boolean
}
```

## 🧪 テスト仕様

### 単体テスト (Jest)
- **コンポーネントレンダリング**: 基本表示・プロパティ変更
- **ユーザーインタラクション**: クリック・ホバー・キーボード操作
- **データ処理**: ソート・フィルター・変換処理
- **エラーハンドリング**: 異常データ・API エラー対応

### E2E テスト (Playwright)
- **統合操作フロー**: 設定変更→ホバー→順序変更の連続操作
- **ドラッグ&ドロップ**: マウス操作による順序変更
- **レスポンシブ**: 画面サイズ変更時の表示調整
- **パフォーマンス**: 大量データでの応答性

### テストカバレッジ目標
- **ライン カバレッジ**: 85%以上
- **分岐 カバレッジ**: 80%以上
- **関数 カバレッジ**: 90%以上

## 🚀 導入・使用方法

### 基本的な使用例
```tsx
import ConfigurableTableViewer from '@/components/ConfigurableTableViewer'

function DataAnalysisPage() {
  const [data, setData] = useState([])
  
  const handleSettingsChange = (settings: TableDisplaySettings) => {
    // 設定変更時の処理
    console.log('Settings updated:', settings)
  }
  
  return (
    <ConfigurableTableViewer
      projectFolder="my-project"
      fileName="data.csv"
      data={data}
      onSettingsChange={handleSettingsChange}
    />
  )
}
```

### 高度な設定例
```tsx
const initialSettings: Partial<TableDisplaySettings> = {
  chartConfig: {
    enabled: true,
    type: 'line',
    xAxis: 'date',
    yAxis: 'value',
    colorScheme: 'purple',
    hoverDetails: {
      enabled: true,
      showTrend: true,
      showBreakdown: false,
      showComparison: true
    }
  },
  layoutConfig: {
    split: 'vertical',
    tableRatio: 0.7,
    chartRatio: 0.3,
    hoverMode: 'sidebar'
  }
}

<ConfigurableTableViewer
  projectFolder="analysis-project"
  fileName="timeseries.csv"
  data={timeSeriesData}
  initialSettings={initialSettings}
  onSettingsChange={handleSettingsChange}
/>
```

## 🔧 カスタマイズ・拡張

### 新しいチャートタイプの追加
1. `DynamicChart.tsx` の `renderChart()` に新しいケース追加
2. `data-types.ts` の `ChartType` に新しい型追加
3. `TableSettingsDialog.tsx` の選択肢に追加
4. 対応するテストケース作成

### 新しいデータタイプの追加
1. `data-types.ts` の `DataType` に新しい型追加
2. `data-sorting.ts` の `compareValues()` に比較ロジック追加
3. `inferDataType()` に判定ロジック追加
4. UI での表示・設定項目追加

### カスタムテーマの追加
1. Tailwind CSS設定でカラーパレット定義
2. `DynamicChart.tsx` の `colors` オブジェクトに追加
3. `TableSettingsDialog.tsx` の選択肢に追加

## 🐛 既知の問題・制限事項

### 現在の制限
- **最大行数**: 10,000行まで（パフォーマンス上の制限）
- **対応ファイル**: CSV形式のみ（Excel・JSON は今後対応予定）
- **同時編集**: 複数ユーザーでの同時設定変更は未対応

### 既知のバグ
- **Edge ブラウザ**: ドラッグ&ドロップ時の描画問題 (Issue #123)
- **Safari**: チャートホバー時の遅延 (Issue #124)

### パフォーマンス注意点
- **大量データ**: 5,000行以上ではページング使用推奨
- **複雑な順序設定**: 100項目以上の順序変更は動作が重くなる可能性

## 📈 今後の開発予定

### Phase 1 (v2.1)
- [ ] Excel ファイル対応
- [ ] JSON データ対応  
- [ ] エクスポート機能（PDF・PNG）

### Phase 2 (v2.2)
- [ ] リアルタイム協業機能
- [ ] 高度フィルター機能
- [ ] カスタムチャート作成機能

### Phase 3 (v2.3)
- [ ] AI による自動レイアウト提案
- [ ] 機械学習による異常値検出
- [ ] ダッシュボード機能

---

**作成日**: 2025年7月30日  
**最終更新**: 2025年7月30日  
**作成者**: Claude Code  
**レビュー者**: StatVizForge Development Team