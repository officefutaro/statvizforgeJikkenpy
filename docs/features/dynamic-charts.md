# 動的チャート 技術仕様書

## 📋 概要

動的チャートシステムは StatVizForge のリアルタイム データ可視化を担う核心コンポーネントです。マウスホバー連動、リアルタイム更新、多様なチャートタイプをサポートしています。

## 🎯 機能概要

### 1. マウスホバー連動表示
- **即座の応答**: テーブル行ホバー時に200ms以内でチャート更新
- **コンテキスト表示**: ホバー対象に関連する詳細データ表示
- **スムーズアニメーション**: フェード・スライド・ズーム効果

### 2. リアルタイム更新
- **データ変更検知**: props変更の自動検知
- **差分更新**: 変更部分のみの効率的な再描画
- **パフォーマンス最適化**: useMemo・useCallback活用

### 3. 多様なチャートタイプ
- **棒グラフ**: カテゴリ別データ比較
- **線グラフ**: 時系列データ・トレンド表示
- **円グラフ**: 構成比・割合表示
- **散布図**: 2変数間の相関表示
- **エリアチャート**: 累積・範囲データ表示

## 📁 ファイル構成

```
components/
├── DynamicChart.tsx              # メインチャートコンポーネント
├── charts/
│   ├── BarChart.tsx             # 棒グラフ実装
│   ├── LineChart.tsx            # 線グラフ実装
│   ├── PieChart.tsx             # 円グラフ実装
│   ├── ScatterChart.tsx         # 散布図実装
│   └── AreaChart.tsx            # エリアチャート実装

types/
├── chart-types.ts               # チャート型定義
└── data-types.ts               # データ型定義

utils/
├── chart-utils.ts              # チャート描画ユーティリティ
├── data-processing.ts          # データ前処理
└── color-schemes.ts            # カラーパレット定義

hooks/
├── useChartData.ts             # チャートデータ管理
├── useHoverState.ts            # ホバー状態管理
└── useChartResize.ts           # レスポンシブ対応

__tests__/
├── DynamicChart.test.tsx
├── charts/
│   ├── BarChart.test.tsx
│   └── LineChart.test.tsx
└── utils/
    └── chart-utils.test.ts
```

## 🔧 技術スタック

### コアライブラリ
- **Recharts 2.12.7**: 主要可視化ライブラリ
- **React 18**: コンポーネント基盤
- **TypeScript**: 型安全性

### 支援ライブラリ
- **d3-scale**: 数値スケーリング
- **d3-interpolate**: アニメーション補完
- **react-transition-group**: アニメーション管理

## 🏗️ アーキテクチャ

### コンポーネント設計
```
DynamicChart
├── ChartContainer (レスポンシブコンテナー)
├── ChartSelector (チャート種類選択・切り替え)
├── ChartRenderer (実際のチャート描画)
│   ├── ResponsiveContainer
│   ├── XAxis / YAxis (軸設定)
│   ├── CartesianGrid (グリッド線)
│   ├── Tooltip (ツールチップ)
│   ├── Legend (凡例)
│   └── ChartElements (棒・線・円など)
└── ChartControls (ズーム・フィルター等)
```

### データフロー
```
1. 親コンポーネント → 2. プロパティ受信 → 3. データ前処理 → 4. チャート描画
     ↑                                                                    ↓
     ←←← 8. イベント通知 ←←← 7. ユーザー操作 ←←← 6. UI更新 ←←← 5. DOM反映
```

## 📊 データ構造

### ChartConfig
```typescript
interface ChartConfig {
  type: 'bar' | 'line' | 'pie' | 'scatter' | 'area'
  width?: number
  height?: number
  
  // 軸設定
  xAxis: {
    dataKey: string
    label?: string
    domain?: [number, number]
    type?: 'number' | 'category' | 'datetime'
  }
  
  yAxis: {
    dataKey: string | string[]
    label?: string
    domain?: [number, number]
    orientation?: 'left' | 'right'
  }
  
  // スタイル設定
  colors: string[]
  theme: 'light' | 'dark' | 'auto'
  showGrid: boolean
  showLegend: boolean
  showTooltip: boolean
  
  // アニメーション設定
  animation: {
    enabled: boolean
    duration: number
    easing: 'ease' | 'linear' | 'ease-in' | 'ease-out'
  }
  
  // インタラクション設定
  hover: {
    enabled: boolean
    highlightColor: string
    showDetails: boolean
  }
  
  // レスポンシブ設定
  responsive: {
    enabled: boolean
    breakpoints: {
      mobile: number
      tablet: number
      desktop: number
    }
  }
}
```

### ChartData
```typescript
interface ChartData {
  data: Array<Record<string, any>>
  metadata: {
    totalRows: number
    columns: Array<{
      key: string
      type: 'number' | 'string' | 'date'
      format?: string
    }>
    dateRange?: {
      start: Date
      end: Date
    }
    valueRange?: {
      min: number
      max: number
    }
  }
}
```

## 🎨 カラーパレット

### デフォルトテーマ
```typescript
const colorSchemes = {
  default: ['#8884d8', '#82ca9d', '#ffc658', '#ff7c7c', '#8dd1e1'],
  purple: ['#8b5cf6', '#a855f7', '#c084fc', '#ddd6fe', '#ede9fe'],
  blue: ['#3b82f6', '#60a5fa', '#93c5fd', '#dbeafe', '#eff6ff'],
  green: ['#10b981', '#34d399', '#6ee7b7', '#a7f3d0', '#d1fae5'],
  warm: ['#f59e0b', '#fbbf24', '#fcd34d', '#fde68a', '#fef3c7'],
  monochrome: ['#374151', '#6b7280', '#9ca3af', '#d1d5db', '#f3f4f6']
}
```

### アクセシビリティ対応
- **コントラスト比**: 4.5:1以上（WCAG AA準拠）
- **色盲対応**: ColorBrewer推奨パレット使用
- **代替表現**: パターン・テクスチャでの区別

## 🔌 API仕様

### プロパティ
```typescript
interface DynamicChartProps {
  // 必須プロパティ
  data: ChartData
  config: ChartConfig
  
  // オプションプロパティ
  className?: string
  style?: React.CSSProperties
  loading?: boolean
  error?: string
  
  // イベントハンドラー
  onChartClick?: (data: any, event: MouseEvent) => void
  onChartHover?: (data: any, event: MouseEvent) => void
  onChartResize?: (width: number, height: number) => void
  onConfigChange?: (config: ChartConfig) => void
  
  // ホバー連動
  hoveredRow?: any
  hoveredColumn?: string
  
  // カスタマイズ
  customRenderer?: (data: any, config: ChartConfig) => JSX.Element
  theme?: 'light' | 'dark' | 'auto'
}
```

### 使用例
```typescript
<DynamicChart
  data={{
    data: [
      { month: 'Jan', sales: 1000, profit: 200 },
      { month: 'Feb', sales: 1200, profit: 300 },
      { month: 'Mar', sales: 900, profit: 150 }
    ],
    metadata: {
      totalRows: 3,
      columns: [
        { key: 'month', type: 'string' },
        { key: 'sales', type: 'number' },
        { key: 'profit', type: 'number' }
      ]
    }
  }}
  config={{
    type: 'line',
    xAxis: { dataKey: 'month', label: '月' },
    yAxis: { dataKey: ['sales', 'profit'], label: '金額' },
    colors: ['#8884d8', '#82ca9d'],
    showGrid: true,
    showLegend: true,
    animation: { enabled: true, duration: 500, easing: 'ease-out' }
  }}
  onChartHover={(data, event) => {
    console.log('Hovered:', data)
  }}
/>
```

## 🧪 テスト仕様

### 単体テスト項目
```typescript
// コンポーネント基本動作
describe('DynamicChart', () => {
  test('正常レンダリング', () => {
    // チャートが正しく描画される
  })
  
  test('プロパティ変更反映', () => {
    // configやdata変更で適切に更新される
  })
  
  test('ホバーイベント', () => {
    // マウスホバーで適切なコールバック呼び出し
  })
  
  test('レスポンシブ対応', () => {
    // 画面サイズ変更で適切にリサイズ
  })
  
  test('エラーハンドリング', () => {
    // 不正データでエラー表示
  })
})

// チャート種類別テスト
describe('Chart Types', () => {
  test.each(['bar', 'line', 'pie', 'scatter', 'area'])(
    '%s chart rendering', (chartType) => {
      // 各チャートタイプの正常描画
    }
  )
})
```

### E2Eテスト項目
```typescript
// Playwright テスト
test('チャート操作フロー', async ({ page }) => {
  // 1. ページ読み込み
  await page.goto('/data-analysis')
  
  // 2. テーブル行ホバー
  await page.hover('[data-testid="table-row-0"]')
  
  // 3. チャート更新確認
  await expect(page.locator('[data-testid="dynamic-chart"]')).toBeVisible()
  
  // 4. チャート種類変更
  await page.click('[data-testid="chart-type-selector"]')
  await page.click('[data-testid="chart-type-line"]')
  
  // 5. 変更反映確認
  await expect(page.locator('.recharts-line')).toBeVisible()
})
```

## 🚀 パフォーマンス最適化

### メモ化戦略
```typescript
// データ処理のメモ化
const processedData = useMemo(() => {
  return processChartData(data, config)
}, [data, config])

// チャートコンポーネントのメモ化
const ChartComponent = memo(({ data, config }) => {
  return <ResponsiveContainer>...</ResponsiveContainer>
})

// イベントハンドラーのメモ化
const handleChartHover = useCallback((data, event) => {
  onChartHover?.(data, event)
}, [onChartHover])
```

### レンダリング最適化
- **仮想化**: 大量データ点の効率的描画
- **間引き**: 高密度データの適切なサンプリング
- **遅延読み込み**: チャートライブラリの動的インポート
- **キャッシュ**: 計算結果のブラウザキャッシュ活用

### アニメーション最適化
- **requestAnimationFrame**: 滑らかなアニメーション
- **CSS Transform**: GPU加速活用
- **プリロード**: 次のフレームの事前計算

## 🔧 カスタマイズ・拡張

### 新しいチャートタイプ追加
```typescript
// 1. 新しいチャートコンポーネント作成
const CustomChart: React.FC<ChartProps> = ({ data, config }) => {
  return (
    <ResponsiveContainer>
      {/* カスタムチャート実装 */}
    </ResponsiveContainer>
  )
}

// 2. DynamicChart に統合
const chartComponents = {
  bar: BarChart,
  line: LineChart,
  custom: CustomChart // 追加
}

// 3. 型定義更新
type ChartType = 'bar' | 'line' | 'pie' | 'scatter' | 'area' | 'custom'
```

### カスタムテーマ作成
```typescript
const customTheme = {
  colors: ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7'],
  background: '#f8f9fa',
  grid: '#e9ecef',
  text: '#495057',
  tooltip: {
    background: '#ffffff',
    border: '#dee2e6',
    shadow: '0 2px 8px rgba(0,0,0,0.1)'
  }
}
```

## 🐛 既知の問題・制限事項

### ブラウザ互換性
- **IE11**: Rechartsがサポート終了（Polyfill必要）
- **Safari**: 一部CSS Grid機能制限
- **Mobile Safari**: タッチイベント遅延

### パフォーマンス制限
- **データ点数**: 1万点以上で描画性能低下
- **アニメーション**: 複雑なSVGで60fps維持困難
- **メモリ使用量**: 大量チャート同時表示時の制限

### 機能制限
- **3Dチャート**: 現在未対応
- **リアルタイムストリーミング**: WebSocket統合未実装
- **高度統計**: 回帰分析・予測機能未実装

## 📈 今後の開発予定

### Phase 1 (v1.1)
- [ ] 3Dチャート対応
- [ ] WebGLレンダリング
- [ ] リアルタイムデータストリーミング

### Phase 2 (v1.2)
- [ ] 高度統計機能（回帰・予測）
- [ ] インタラクティブフィルター
- [ ] チャート間連動機能

### Phase 3 (v1.3)
- [ ] AI チャート自動生成
- [ ] 音声による操作対応
- [ ] VR/AR チャート表示

---

**作成日**: 2025年7月30日  
**最終更新**: 2025年7月30日  
**作成者**: Claude Code  
**レビュー者**: StatVizForge Development Team