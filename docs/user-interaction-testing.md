# ユーザーインタラクションテスト実装ガイド

## 概要

StatVizForge_JikkenPyプロジェクトにおいて、ユーザーのマウス操作やキーボード操作を模擬したフロントエンドテスト機能を実装しました。この機能により、実際のユーザー操作を自動化してテストできます。

## 実装済み機能

### 1. 単体テスト（Jest + Testing Library）

**ファイル**: `app/frontend/src/tests/user-interaction.test.tsx`

#### マウス操作テスト
- **シングルクリック**: セル選択、ボタン押下
- **ダブルクリック**: 編集モード起動
- **右クリック**: コンテキストメニュー表示
- **マウスホバー**: ツールチップ表示
- **ドラッグ&ドロップ**: データ移動、順序変更

#### キーボード操作テスト
- **テキスト入力**: フィルタ入力、フォーム操作
- **キーコンビネーション**: Ctrl+S（保存）、Ctrl+Z（アンドゥ）、Escape（キャンセル）
- **Tab ナビゲーション**: フォーカス移動の確認
- **矢印キー**: テーブル内ナビゲーション

#### 複合操作テスト
- **ソート機能**: クリックによる列ソート
- **フィルタリング**: 入力とクリア操作
- **マウス＋キーボード**: 検索入力とEnterキー実行

### 2. E2Eテスト（Playwright）

**ファイル**: `app/frontend/e2e/user-interactions.spec.ts`

#### 高度なマウス操作
- **複雑なマウスシーケンス**: 複数操作の連続実行
- **精密なドラッグ&ドロップ**: 座標指定による正確な操作
- **スクロール操作**: プログラマティックスクロール

#### キーボードショートカット
- **システムショートカット**: Ctrl+A、Ctrl+C、Ctrl+V
- **アプリケーション固有**: カスタムショートカット

#### タッチ操作（モバイル）
- **タップ操作**: シングルタップ、長押し
- **スワイプ**: 左右、上下のスワイプ
- **ピンチ操作**: ズームイン・アウト

#### フォーム操作
- **包括的な入力**: テキスト、選択、チェック、ファイル
- **バリデーション**: エラー表示の確認

### 3. テストヘルパー機能

**ファイル**: `app/frontend/src/utils/test-helpers.ts`

#### UserInteractionTestHelper クラス
```typescript
const helper = new UserInteractionTestHelper();

// 複雑なマウス操作シーケンス
await helper.performMouseSequence([
  { type: 'click', target: 'cell-0-name' },
  { type: 'hover', target: 'cell-0-age' },
  { type: 'dblclick', target: 'edit-button' }
]);

// フォーム自動入力
await helper.fillForm({
  name: { type: 'text', value: '山田太郎', testId: 'name-input' },
  email: { type: 'text', value: 'yamada@example.com', testId: 'email-input' },
  agree: { type: 'checkbox', value: true, testId: 'agree-checkbox' }
});
```

#### AccessibilityTestHelper クラス
```typescript
// キーボードナビゲーションテスト
await AccessibilityTestHelper.testKeyboardNavigation(
  'start-button',
  ['input-1', 'input-2', 'submit-button']
);

// ARIA属性チェック
AccessibilityTestHelper.checkAriaAttributes('dialog', {
  'aria-label': 'データ編集ダイアログ',
  'role': 'dialog'
});
```

#### MockDataGenerator クラス
```typescript
// テスト用データ生成
const tableData = MockDataGenerator.generateTableData(100, ['id', 'name', 'email', 'age']);

// 大容量データでのパフォーマンステスト
const largeDataset = MockDataGenerator.generateLargeDataset(10000);
```

## 使用方法

### 基本的なテスト実行

```bash
# ユーザーインタラクションテスト実行
npm run test:user-interaction

# ウォッチモードで実行
npm run test:user-interaction:watch

# カバレッジ付きで実行
npm run test:user-interaction:coverage

# E2Eインタラクションテスト実行
npm run test:e2e:interaction
```

### テストの書き方例

```typescript
import { UserInteractionTestHelper, MockDataGenerator } from '../utils/test-helpers';

describe('データテーブル操作テスト', () => {
  let helper: UserInteractionTestHelper;
  let mockData: any[];

  beforeEach(() => {
    helper = new UserInteractionTestHelper();
    mockData = MockDataGenerator.generateTableData(10, ['id', 'name', 'age', 'city']);
  });

  test('セル編集フロー', async () => {
    render(<DataTable data={mockData} />);

    // 1. セルをダブルクリックして編集モード
    await helper.performMouseSequence([
      { type: 'dblclick', target: 'cell-0-name' }
    ]);

    // 2. 新しい値を入力
    const editInput = screen.getByTestId('edit-input');
    await helper.user.clear(editInput);
    await helper.user.type(editInput, '新しい名前');

    // 3. Enterキーで確定
    await helper.user.keyboard('{Enter}');

    // 4. 変更が反映されていることを確認
    expect(screen.getByTestId('cell-0-name')).toHaveTextContent('新しい名前');
  });
});
```

## テスト可能な操作パターン

### 1. データテーブル操作
- ✅ セルクリック選択
- ✅ 列ヘッダークリックソート
- ✅ 行選択（Shift+クリック、Ctrl+クリック）
- ✅ セル編集（ダブルクリック→入力→Enter）
- ✅ コンテキストメニュー（右クリック）
- ✅ キーボードナビゲーション（矢印キー）

### 2. フォーム操作
- ✅ テキスト入力（文字入力、クリア、選択）
- ✅ セレクトボックス選択
- ✅ チェックボックス・ラジオボタン
- ✅ ファイルアップロード
- ✅ バリデーションエラー表示

### 3. ナビゲーション
- ✅ タブナビゲーション（Tab、Shift+Tab）
- ✅ メニューナビゲーション
- ✅ モーダルダイアログ操作
- ✅ アコーディオン・タブ切り替え

### 4. 高度な操作
- ✅ ドラッグ&ドロップ
- ✅ リサイズ操作
- ✅ 無限スクロール
- ✅ 仮想スクロール

## パフォーマンステスト

### レスポンス時間測定
```typescript
const { result, duration } = await helper.measurePerformance(
  'データ読み込み',
  async () => {
    await user.click(screen.getByTestId('load-button'));
    await waitFor(() => screen.getByTestId('data-loaded'));
  },
  1000 // 1秒以内の期待値
);
```

### 大量データでの操作性能
```typescript
test('10000行データでのスクロール性能', async ({ page }) => {
  // 大量データの生成と表示
  await page.evaluate(() => {
    // 10000行のデータを生成
  });

  const startTime = Date.now();
  
  // スクロール操作
  await page.evaluate(() => window.scrollTo(0, 10000));
  
  const endTime = Date.now();
  expect(endTime - startTime).toBeLessThan(500); // 500ms以内
});
```

## アクセシビリティテスト

### キーボードアクセシビリティ
```typescript
test('キーボードのみでの完全操作', async () => {
  // マウスを使わずに全機能を操作
  await user.tab(); // ナビゲーション
  await user.keyboard('{Enter}'); // アクティベート
  await user.keyboard('{Escape}'); // キャンセル
});
```

### スクリーンリーダー対応
```typescript
test('ARIA属性の確認', () => {
  AccessibilityTestHelper.checkScreenReaderSupport('main-form');
  
  // すべてのインタラクティブ要素がラベルを持つ
  // 画像がalt属性を持つ
  // フォーカス可能な要素が適切なroleを持つ
});
```

## ベストプラクティス

### 1. テストの構造化
- **AAA パターン**: Arrange（準備）、Act（実行）、Assert（検証）
- **Page Object Model**: 複雑なページは再利用可能なオブジェクトとして実装
- **テストデータの分離**: MockDataGeneratorを活用

### 2. 信頼性の確保
- **明示的な待機**: waitForを使用してDOM更新を待機
- **安定したセレクタ**: data-testidを使用
- **リトライ機能**: 不安定なテストに対する再試行

### 3. メンテナンス性
- **ヘルパー関数の活用**: 共通操作の抽象化
- **設定の外部化**: テストデータと設定の分離
- **ドキュメント化**: テストの意図を明確に記述

## 今後の拡張予定

### 1. 視覚的回帰テスト
- スクリーンショット比較
- コンポーネントの見た目の変化検出

### 2. パフォーマンス監視
- Core Web Vitals測定
- メモリリーク検出

### 3. クロスブラウザテスト
- 複数ブラウザでの動作確認
- デバイス固有の操作テスト

## まとめ

実装したユーザーインタラクションテスト機能により、以下が可能になりました：

- **包括的なUI操作テスト**: マウス、キーボード、タッチ操作の自動化
- **アクセシビリティ確保**: キーボードナビゲーション、スクリーンリーダー対応
- **パフォーマンス検証**: 操作レスポンス時間、大量データ処理
- **回帰テスト**: UI変更時の既存機能の動作確認

これらの機能により、ユーザー体験の品質を継続的に保証できる体制が整いました。