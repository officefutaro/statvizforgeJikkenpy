# GUIテスト実装 技術仕様書

## 📋 概要

StatVizForge のGUIテスト実装は、Jest + Testing Library による単体テストと Playwright による E2E テストを組み合わせた包括的なテスト戦略です。ユーザーインタラクション、視覚的回帰、パフォーマンスを総合的に検証します。

## 🎯 テスト方針

### 1. テストピラミッド
- **単体テスト (70%)**: コンポーネント・関数の個別テスト
- **統合テスト (20%)**: コンポーネント間の連携テスト
- **E2Eテスト (10%)**: ユーザーシナリオの完全再現

### 2. GUI固有の課題
- **非同期処理**: ローディング・API呼び出し・アニメーション
- **状態管理**: 複雑な状態遷移・イベント連鎖
- **レスポンシブ**: 画面サイズ・デバイス別表示
- **ブラウザ差異**: 描画・イベント処理の差異

### 3. テスト自動化
- **CI統合**: プルリクエスト時の自動実行
- **並列実行**: 複数ブラウザでの同時テスト
- **視覚的回帰**: スクリーンショット比較
- **パフォーマンス**: メトリクス収集・閾値監視

## 📁 ファイル構成

```
__tests__/
├── components/
│   ├── ConfigurableTableViewer.test.tsx    # メインGUIコンポーネント
│   ├── DynamicChart.test.tsx               # チャートGUI
│   ├── TableSettingsDialog.test.tsx       # ダイアログGUI
│   └── OrdinalOrderSettings.test.tsx      # 順序設定GUI
├── hooks/
│   ├── useHoverState.test.ts               # ホバー状態管理
│   └── useChartData.test.ts                # チャートデータ管理
├── utils/
│   ├── dom-testing-utils.ts                # DOM操作ヘルパー
│   └── mock-data-generator.ts              # テスト用データ生成
└── setup/
    ├── jest.setup.ts                       # Jest設定
    └── testing-library.setup.ts            # Testing Library設定

e2e/
├── configurable-table-viewer.spec.ts       # E2Eメインテスト
├── responsive-design.spec.ts               # レスポンシブテスト
├── performance.spec.ts                     # パフォーマンステスト
├── accessibility.spec.ts                   # アクセシビリティテスト
└── visual-regression.spec.ts               # 視覚的回帰テスト

fixtures/
├── test-data/
│   ├── sample-csv.csv                      # サンプルデータ
│   └── large-dataset.csv                  # 大量データ
├── screenshots/
│   ├── baseline/                           # ベースライン画像
│   └── diff/                               # 差分画像
└── mock-responses/
    └── api-responses.json                  # モックAPIレスポンス
```

## 🔧 技術スタック

### 単体・統合テスト
- **Jest 29.7**: テストランナー・アサーション
- **Testing Library**: DOM操作・ユーザーイベント
- **jest-dom**: DOM状態のアサーション拡張
- **user-event**: リアルなユーザー操作シミュレーション

### E2Eテスト
- **Playwright 1.40**: クロスブラウザ自動化
- **percy**: 視覚的回帰テスト
- **lighthouse**: パフォーマンス測定
- **axe-core**: アクセシビリティ検証

### 支援ツール
- **MSW**: APIモッキング
- **Faker.js**: テストデータ生成
- **jest-coverage**: カバレッジ測定
- **allure**: テストレポート生成

## 🏗️ テスト設計パターン

### Page Objectパターン
```typescript
// e2e/page-objects/ConfigurableTableViewerPage.ts
export class ConfigurableTableViewerPage {
  constructor(private page: Page) {}

  // 要素セレクター
  private selectors = {
    tableContainer: '[data-testid="table-container"]',
    chartContainer: '[data-testid="chart-container"]',
    settingsButton: '[data-testid="settings-button"]',
    hoverRow: (index: number) => `[data-testid="table-row-${index}"]`,
    dynamicChart: '[data-testid="dynamic-chart"]'
  }

  // アクション
  async hoverTableRow(index: number) {
    await this.page.hover(this.selectors.hoverRow(index))
  }

  async openSettings() {
    await this.page.click(this.selectors.settingsButton)
  }

  async waitForChartUpdate() {
    await this.page.waitForSelector(this.selectors.dynamicChart)
  }

  // アサーション
  async expectChartVisible() {
    await expect(this.page.locator(this.selectors.dynamicChart)).toBeVisible()
  }
}
```

### Custom Renderパターン
```typescript
// __tests__/utils/custom-render.tsx
export function renderWithProviders(
  ui: React.ReactElement,
  options: RenderOptions = {}
) {
  const AllTheProviders = ({ children }: { children: React.ReactNode }) => {
    return (
      <QueryClientProvider client={testQueryClient}>
        <ThemeProvider theme="light">
          <MemoryRouter>
            {children}
          </MemoryRouter>
        </ThemeProvider>
      </QueryClientProvider>
    )
  }

  return render(ui, { wrapper: AllTheProviders, ...options })
}

// カスタムフック
export * from '@testing-library/react'
export { renderWithProviders as render }
```

## 📊 テスト仕様書

### ConfigurableTableViewer GUI テスト

#### 1. マウスオーバー連動機能
```typescript
describe('マウスオーバー連動グラフ表示機能', () => {
  test('テーブル行ホバー時にチャートが表示される', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer {...defaultProps} />
    )

    // テーブル最初の行をホバー
    const firstRow = screen.getByTestId('table-row-0')
    await user.hover(firstRow)

    // チャートが表示される
    expect(screen.getByTestId('dynamic-chart')).toBeVisible()
    
    // ホバー詳細情報が表示される
    expect(screen.getByTestId('hover-details')).toBeVisible()
  })

  test('ホバー解除時にチャートが非表示になる', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer {...defaultProps} />
    )

    const row = screen.getByTestId('table-row-0')
    await user.hover(row)
    await user.unhover(row)

    // チャートが非表示になる
    await waitFor(() => {
      expect(screen.queryByTestId('dynamic-chart')).not.toBeVisible()
    })
  })

  test('異なる行のホバーでチャートが更新される', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer {...defaultProps} />
    )

    // 最初の行をホバー
    await user.hover(screen.getByTestId('table-row-0'))
    const firstChartData = screen.getByTestId('chart-data').textContent

    // 2番目の行をホバー
    await user.hover(screen.getByTestId('table-row-1'))
    const secondChartData = screen.getByTestId('chart-data').textContent

    // チャートデータが異なる
    expect(firstChartData).not.toBe(secondChartData)
  })
})
```

#### 2. 設定ダイアログ機能
```typescript
describe('設定ダイアログ機能', () => {
  test('設定ボタンクリックでダイアログが開く', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer {...defaultProps} />
    )

    await user.click(screen.getByTestId('settings-button'))
    
    expect(screen.getByRole('dialog')).toBeVisible()
    expect(screen.getByText('表示設定')).toBeVisible()
  })

  test('設定変更が即座に反映される', async () => {
    const onSettingsChange = jest.fn()
    const { user } = renderWithProviders(
      <ConfigurableTableViewer 
        {...defaultProps} 
        onSettingsChange={onSettingsChange}
      />
    )

    // 設定ダイアログを開く
    await user.click(screen.getByTestId('settings-button'))
    
    // チャートタイプを変更
    await user.click(screen.getByLabelText('線グラフ'))
    
    // 設定変更コールバックが呼ばれる
    expect(onSettingsChange).toHaveBeenCalledWith(
      expect.objectContaining({
        chartConfig: expect.objectContaining({ type: 'line' })
      })
    )
  })

  test('タブ切り替えが正常に動作する', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer {...defaultProps} />
    )

    await user.click(screen.getByTestId('settings-button'))
    
    // チャート設定タブに切り替え
    await user.click(screen.getByRole('tab', { name: 'チャート設定' }))
    expect(screen.getByTestId('chart-settings-panel')).toBeVisible()
    
    // レイアウト設定タブに切り替え
    await user.click(screen.getByRole('tab', { name: 'レイアウト設定' }))
    expect(screen.getByTestId('layout-settings-panel')).toBeVisible()
  })
})
```

#### 3. 順序設定機能
```typescript
describe('順序量データの順序決定機能', () => {
  test('順序決定ボタンでダイアログが開く', async () => {
    const { user } = renderWithProviders(
      <ConfigurableTableViewer 
        {...defaultProps} 
        data={ordinalData}
      />
    )

    const ordinalColumn = screen.getByTestId('column-header-priority')
    await user.click(ordinalColumn)
    
    const orderButton = screen.getByTestId('order-settings-button')
    await user.click(orderButton)
    
    expect(screen.getByRole('dialog')).toBeVisible()
    expect(screen.getByText('順序設定')).toBeVisible()
  })

  test('ドラッグ&ドロップで順序変更', async () => {
    const { user } = renderWithProviders(
      <OrdinalOrderSettings {...ordinalProps} />
    )

    const firstItem = screen.getByTestId('ordinal-item-0')
    const secondItem = screen.getByTestId('ordinal-item-1')

    // ドラッグ&ドロップシミュレーション
    await user.dragAndDrop(firstItem, secondItem)

    // 順序が変更される
    const items = screen.getAllByTestId(/ordinal-item-/)
    expect(items[0]).toHaveTextContent(originalItems[1])
    expect(items[1]).toHaveTextContent(originalItems[0])
  })

  test('自動並び替えボタン動作', async () => {
    const { user } = renderWithProviders(
      <OrdinalOrderSettings {...ordinalProps} />
    )

    // アルファベット順ボタンをクリック
    await user.click(screen.getByTestId('sort-alphabetical'))

    // 項目がアルファベット順に並び替えられる
    const items = screen.getAllByTestId(/ordinal-item-/)
    const sortedTexts = items.map(item => item.textContent).sort()
    items.forEach((item, index) => {
      expect(item).toHaveTextContent(sortedTexts[index])
    })
  })
})
```

### E2E テスト仕様

#### 統合操作フロー
```typescript
// e2e/configurable-table-viewer.spec.ts
test('完全なユーザーフロー', async ({ page }) => {
  const tableViewer = new ConfigurableTableViewerPage(page)
  
  // 1. ページ読み込み
  await page.goto('/project/sample/analysis')
  await tableViewer.waitForChartUpdate()

  // 2. テーブル行ホバー → チャート表示
  await tableViewer.hoverTableRow(0)
  await tableViewer.expectChartVisible()

  // 3. 設定ダイアログ開く
  await tableViewer.openSettings()
  
  // 4. チャートタイプ変更
  await page.click('[data-testid="chart-type-line"]')
  
  // 5. レイアウト変更
  await page.click('[data-testid="layout-vertical"]')
  
  // 6. 設定保存
  await page.click('[data-testid="save-settings"]')
  
  // 7. 変更反映確認
  await expect(page.locator('.recharts-line')).toBeVisible()
  await expect(page.locator('[data-testid="vertical-layout"]')).toBeVisible()

  // 8. 順序設定
  await page.click('[data-testid="column-header-status"]')
  await page.click('[data-testid="order-settings-button"]')
  
  // 9. ドラッグ&ドロップ
  const source = page.locator('[data-testid="ordinal-item-0"]')
  const target = page.locator('[data-testid="ordinal-item-2"]')
  await source.dragTo(target)
  
  // 10. プレビュー確認
  await expect(page.locator('[data-testid="order-preview"]')).toBeVisible()
  
  // 11. 順序適用
  await page.click('[data-testid="apply-order"]')
  
  // 12. テーブル順序変更確認
  const firstCell = page.locator('[data-testid="table-row-0"] td').first()
  await expect(firstCell).toHaveText('High')
})
```

#### レスポンシブテスト
```typescript
// e2e/responsive-design.spec.ts
test.describe('レスポンシブデザイン', () => {
  test('モバイル表示', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 })
    await page.goto('/project/sample/analysis')

    // モバイル用レイアウト
    await expect(page.locator('[data-testid="mobile-layout"]')).toBeVisible()
    
    // タブ切り替え表示
    await expect(page.locator('[data-testid="tab-switcher"]')).toBeVisible()
    
    // チャートタブに切り替え
    await page.click('[data-testid="chart-tab"]')
    await expect(page.locator('[data-testid="chart-container"]')).toBeVisible()
    await expect(page.locator('[data-testid="table-container"]')).not.toBeVisible()
  })

  test('タブレット表示', async ({ page }) => {
    await page.setViewportSize({ width: 768, height: 1024 })
    await page.goto('/project/sample/analysis')

    // 垂直分割レイアウト
    await expect(page.locator('[data-testid="vertical-split"]')).toBeVisible()
    
    // 両方同時表示
    await expect(page.locator('[data-testid="table-container"]')).toBeVisible()
    await expect(page.locator('[data-testid="chart-container"]')).toBeVisible()
  })

  test('デスクトップ表示', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 })
    await page.goto('/project/sample/analysis')

    // 水平分割レイアウト
    await expect(page.locator('[data-testid="horizontal-split"]')).toBeVisible()
    
    // サイドバー表示
    await expect(page.locator('[data-testid="settings-sidebar"]')).toBeVisible()
  })
})
```

#### パフォーマンステスト
```typescript
// e2e/performance.spec.ts
test('パフォーマンス測定', async ({ page }) => {
  // Lighthouse 統合
  const { lhr } = await lighthouse(page.url(), {
    port: 9222,
    output: 'json',
    onlyCategories: ['performance'],
  })

  // パフォーマンススコア確認
  expect(lhr.categories.performance.score).toBeGreaterThan(0.8)

  // Core Web Vitals
  const vitals = await page.evaluate(() => {
    return new Promise((resolve) => {
      new PerformanceObserver((list) => {
        const entries = list.getEntries()
        resolve({
          lcp: entries.find(e => e.entryType === 'largest-contentful-paint')?.startTime,
          fid: entries.find(e => e.entryType === 'first-input')?.processingStart,
          cls: entries.find(e => e.entryType === 'layout-shift')?.value
        })
      }).observe({ entryTypes: ['paint', 'navigation', 'layout-shift'] })
    })
  })

  expect(vitals.lcp).toBeLessThan(2500) // 2.5秒以内
  expect(vitals.fid).toBeLessThan(100)  // 100ms以内
  expect(vitals.cls).toBeLessThan(0.1)  // 0.1以内
})
```

## 🔍 視覚的回帰テスト

### スクリーンショット比較
```typescript
// e2e/visual-regression.spec.ts
test('視覚的回帰テスト', async ({ page }) => {
  await page.goto('/project/sample/analysis')
  
  // 基本表示
  await expect(page).toHaveScreenshot('table-viewer-initial.png')
  
  // ホバー状態
  await page.hover('[data-testid="table-row-0"]')
  await expect(page).toHaveScreenshot('table-viewer-hover.png')
  
  // 設定ダイアログ
  await page.click('[data-testid="settings-button"]')
  await expect(page).toHaveScreenshot('settings-dialog.png')
  
  // チャート種類変更
  await page.click('[data-testid="chart-type-pie"]')
  await expect(page).toHaveScreenshot('pie-chart-view.png')
})
```

### CI統合設定
```yaml
# .github/workflows/visual-tests.yml
name: Visual Regression Tests

on:
  pull_request:
    paths:
      - 'app/frontend/**'
      - 'e2e/**'

jobs:
  visual-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run visual tests
        run: npm run test:visual
        
      - name: Upload screenshots
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: screenshot-diffs
          path: e2e/screenshots/diff/
```

## 📈 テストメトリクス・レポート

### カバレッジ目標
- **ライン カバレッジ**: 85%以上
- **分岐 カバレッジ**: 80%以上  
- **関数 カバレッジ**: 90%以上
- **GUI操作 カバレッジ**: 75%以上

### 継続的監視
```typescript
// scripts/test-metrics.js
const metrics = {
  // テスト実行時間
  executionTime: {
    unit: 120,      // 2分以内
    integration: 300, // 5分以内
    e2e: 900        // 15分以内
  },
  
  // 安定性指標
  stability: {
    flakiness: 0.02,  // 2%以下の不安定率
    timeout: 0.01     // 1%以下のタイムアウト率
  },
  
  // 品質指標
  quality: {
    bugEscapeRate: 0.05,  // 5%以下のバグ流出率
    regressionRate: 0.03  // 3%以下の機能退行率
  }
}
```

## 🚀 実行・運用

### ローカル開発
```bash
# 単体テスト実行
npm run test:gui

# ウォッチモード
npm run test:gui:watch

# カバレッジ付き実行
npm run test:gui:coverage

# E2Eテスト実行
npm run test:e2e

# UIモード（デバッグ用）
npm run test:e2e:ui
```

### CI/CD統合
```bash
# 全テスト実行
npm run test:all

# 高速テスト（PRチェック用）
npm run test:fast

# 完全テスト（リリース前）
npm run test:full

# レポート生成
npm run test:report
```

---

**作成日**: 2025年7月30日  
**最終更新**: 2025年7月30日  
**作成者**: Claude Code  
**レビュー者**: StatVizForge Development Team