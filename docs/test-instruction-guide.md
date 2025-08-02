# テスト指示ガイド - ユーザーインタラクションテスト

## 概要

ユーザーインタラクションテストの内容を指示する際の効果的な方法とフォーマットを説明します。

## 1. テスト指示の基本フォーマット

### A. 自然言語による指示

```markdown
## テストシナリオ: データテーブルの編集機能

### 前提条件
- データテーブルが表示されている
- 編集権限を持つユーザーでログイン済み

### テスト手順
1. 「顧客名」列の1行目セルをダブルクリック
2. 「新しい顧客名」と入力
3. Enterキーを押下
4. 変更が保存されることを確認

### 期待結果
- セルの値が「新しい顧客名」に更新される
- 保存成功メッセージが表示される
- データベースに変更が反映される
```

### B. 構造化された指示形式

```yaml
test_scenario:
  name: "フィルター機能テスト"
  category: "user_interaction"
  
  setup:
    - component: "DataTable"
    - data_size: 100
    - filters_enabled: true
  
  actions:
    - type: "click"
      target: "filter-input"
    - type: "type"
      text: "東京"
    - type: "keyboard"
      keys: "Enter"
    - type: "wait"
      condition: "data_filtered"
  
  assertions:
    - element: "table-rows"
      count: 25
    - element: "filter-result-text"
      contains: "25件が見つかりました"
```

## 2. 操作タイプ別の指示方法

### マウス操作

```javascript
// 基本的なクリック操作
{
  type: "mouse",
  actions: [
    { operation: "click", target: "data-testid:submit-button" },
    { operation: "dblclick", target: "data-testid:cell-0-name" },
    { operation: "rightclick", target: "data-testid:table-row-1" },
    { operation: "hover", target: "data-testid:tooltip-trigger" },
    { operation: "drag", from: "drag-source", to: "drop-target" }
  ]
}
```

### キーボード操作

```javascript
// キーボード操作の指示
{
  type: "keyboard",
  actions: [
    { keys: "Control+s", description: "保存ショートカット" },
    { keys: "Tab Tab Tab", description: "3回タブキーでナビゲート" },
    { keys: "ArrowDown ArrowDown", description: "2行下に移動" },
    { keys: "Enter", description: "選択を確定" },
    { keys: "Escape", description: "操作をキャンセル" }
  ]
}
```

### フォーム操作

```javascript
// フォーム入力の指示
{
  type: "form",
  actions: [
    { field: "name-input", value: "山田太郎", method: "type" },
    { field: "email-input", value: "yamada@example.com", method: "type" },
    { field: "prefecture-select", value: "東京都", method: "select" },
    { field: "agree-checkbox", value: true, method: "check" },
    { field: "gender-male", value: true, method: "radio" }
  ]
}
```

## 3. テスト指示のレベル

### レベル1: 簡易指示（推奨）

```markdown
## テスト指示: ログイン機能

**操作手順:**
1. メールアドレス入力: "test@example.com"
2. パスワード入力: "password123"
3. ログインボタンクリック

**期待結果:**
- ダッシュボード画面に遷移
- ユーザー名が右上に表示
```

### レベル2: 詳細指示

```json
{
  "test_name": "ログイン機能テスト",
  "preconditions": [
    "ログイン画面が表示されている",
    "有効なテストアカウントが存在する"
  ],
  "steps": [
    {
      "step": 1,
      "action": "input_text",
      "target": "[data-testid='email-input']",
      "value": "test@example.com",
      "description": "メールアドレスを入力"
    },
    {
      "step": 2,
      "action": "input_text",
      "target": "[data-testid='password-input']",
      "value": "password123",
      "description": "パスワードを入力"
    },
    {
      "step": 3,
      "action": "click",
      "target": "[data-testid='login-button']",
      "description": "ログインボタンをクリック"
    }
  ],
  "expected_results": [
    {
      "assertion": "url_contains",
      "value": "/dashboard",
      "description": "ダッシュボードURLに遷移"
    },
    {
      "assertion": "element_visible",
      "target": "[data-testid='user-name']",
      "description": "ユーザー名が表示される"
    }
  ]
}
```

### レベル3: プログラマティック指示

```typescript
// TypeScript による型安全な指示
interface TestInstruction {
  scenario: string;
  setup: SetupConfig;
  interactions: UserInteraction[];
  assertions: Assertion[];
  cleanup?: CleanupAction[];
}

const loginTest: TestInstruction = {
  scenario: "ユーザーログイン",
  setup: {
    route: "/login",
    mockData: { users: testUsers }
  },
  interactions: [
    { type: "type", selector: "#email", value: "test@example.com" },
    { type: "type", selector: "#password", value: "password123" },
    { type: "click", selector: "#login-btn" }
  ],
  assertions: [
    { type: "url", expected: "/dashboard" },
    { type: "visible", selector: ".user-profile" }
  ]
};
```

## 4. 実際の使用例と指示方法

### 方法1: Markdownファイルによる指示

```markdown
<!-- tests/scenarios/data-table-operations.md -->

# データテーブル操作テストシナリオ

## シナリオ1: セルの編集

**目的**: ユーザーがテーブルのセルを直接編集できることを確認

**手順**:
1. データテーブルの1行目「名前」セルをダブルクリック
2. "新しい名前"と入力
3. Enterキーを押下
4. セルの内容が更新されることを確認

**検証ポイント**:
- [ ] セルが編集モードになる
- [ ] 入力値が反映される
- [ ] 他のセルには影響しない

## シナリオ2: ソート機能

**手順**:
1. 「年齢」列のヘッダーをクリック
2. 昇順ソートされることを確認
3. 再度クリックして降順ソートを確認
```

### 方法2: JSONによる構造化指示

```json
{
  "test_suite": "データ操作テスト",
  "scenarios": [
    {
      "id": "table_sort",
      "name": "テーブルソート機能",
      "interactions": [
        {
          "type": "click",
          "target": "header-age",
          "expected": {
            "visual": "昇順ソートアイコン表示",
            "data": "年齢が昇順に並び替え"
          }
        },
        {
          "type": "click", 
          "target": "header-age",
          "expected": {
            "visual": "降順ソートアイコン表示",
            "data": "年齢が降順に並び替え"
          }
        }
      ]
    }
  ]
}
```

### 方法3: 自然言語 + コード指示の組み合わせ

```markdown
## テスト要求

「顧客データの一括更新機能をテストしてください」

### 詳細要件
- 複数行を選択して一括編集できること
- 変更内容はリアルタイムで反映されること
- エラー時は適切なメッセージが表示されること

### 実装例
```typescript
// この要件に基づいて、以下のようなテストを自動生成
await helper.performMouseSequence([
  { type: 'click', target: 'row-0-checkbox' },
  { type: 'click', target: 'row-1-checkbox', options: { ctrlKey: true } },
  { type: 'click', target: 'bulk-edit-button' }
]);
```

## 5. Claude Code への効果的な指示方法

### 推奨フォーマット

```markdown
## テスト作成依頼

**コンポーネント**: ConfigurableTableViewer
**テスト対象**: フィルター機能とソート機能の組み合わせ

**シナリオ**:
1. 名前フィルターに"田"を入力
2. 年齢列で昇順ソート
3. 結果が正しく表示されることを確認

**期待動作**:
- フィルター後のデータのみがソート対象
- 表示件数が正しく更新される
- パフォーマンスが良好（1秒以内）

**使用ツール**: Jest + Testing Library
**追加要件**: アクセシビリティテストも含む
```

### 段階的指示

```markdown
## Phase 1: 基本テスト作成
「まず、クリック操作のテストを作成してください」

## Phase 2: 複雑な操作追加  
「次に、ドラッグ&ドロップ機能を追加してください」

## Phase 3: エラーケース
「最後に、ネットワークエラー時の動作をテストしてください」
```

## 6. テスト指示のベストプラクティス

### ✅ 良い指示例

```markdown
## 明確で具体的な指示

**テスト対象**: ユーザー登録フォーム  
**操作**: 必須フィールドを空で送信  
**期待結果**: 各フィールドにエラーメッセージ表示  
**検証項目**: 
- メールアドレス: "メールアドレスは必須です"
- パスワード: "パスワードは8文字以上です"
- フォーカス: 最初のエラーフィールドにフォーカス移動
```

### ❌ 避けるべき指示例

```markdown
## 曖昧な指示

「フォームのテストを作って」
「なんかエラーが出るかテストして」
「いい感じにユーザビリティを確認して」
```

## 7. 指示の自動化と効率化

### テンプレート使用

```typescript
// テスト指示テンプレート
const createTestInstruction = (component: string, scenario: string) => `
## テスト作成依頼

**コンポーネント**: ${component}
**シナリオ**: ${scenario}

**基本要件**:
- [ ] 正常系のテスト
- [ ] 異常系のテスト  
- [ ] アクセシビリティテスト
- [ ] パフォーマンステスト

**実装フレームワーク**: Jest + Testing Library
**期待テストカバレッジ**: 90%以上
`;
```

### AI アシスタント向けの構造化指示

```json
{
  "instruction_type": "create_interaction_test",
  "target_component": "DataTable",
  "test_scenarios": [
    "cell_editing",
    "row_selection", 
    "column_sorting",
    "data_filtering"
  ],
  "interaction_types": ["mouse", "keyboard", "touch"],
  "accessibility_requirements": true,
  "performance_requirements": {
    "max_response_time": 500,
    "max_memory_usage": "50MB"
  },
  "coverage_target": 95
}
```

## まとめ

効果的なテスト指示のポイント：

1. **明確性**: 具体的な操作手順と期待結果
2. **構造化**: 標準的なフォーマットの使用
3. **段階的**: 簡単なものから複雑なものへ
4. **検証可能**: 定量的な成功基準
5. **実用性**: 実際のユーザー行動に基づく

適切な指示により、効率的で信頼性の高いテストが自動生成できます。