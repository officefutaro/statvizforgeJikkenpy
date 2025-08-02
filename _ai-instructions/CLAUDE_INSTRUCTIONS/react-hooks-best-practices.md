# React Hooks Best Practices

## 初期化順序の重要性

React Hooksを使用する際は、以下の順序ルールを厳守してください：

### 1. 関数定義の順序
- `useCallback`や通常の関数は、それらを使用する`useEffect`や他の`useCallback`より**前に**定義する
- 依存配列に含まれる関数は、必ずその依存配列を持つHookより前に定義する

### 2. よくあるエラーパターン

❌ **間違った例**：
```typescript
// useEffectが先に定義されている
useEffect(() => {
  fetchData(); // エラー: fetchDataはまだ定義されていない
}, [fetchData]);

// useCallbackが後に定義されている
const fetchData = useCallback(() => {
  // ...
}, []);
```

✅ **正しい例**：
```typescript
// useCallbackを先に定義
const fetchData = useCallback(() => {
  // ...
}, []);

// その後でuseEffectで使用
useEffect(() => {
  fetchData();
}, [fetchData]);
```

### 3. ヘルパー関数の配置

❌ **間違った例**：
```typescript
const processData = useCallback(() => {
  const result = helperFunction(data); // エラー: helperFunctionはまだ定義されていない
  // ...
}, [data]);

const helperFunction = (data: any) => {
  // ...
};
```

✅ **正しい例**：
```typescript
// ヘルパー関数を先に定義
const helperFunction = (data: any) => {
  // ...
};

// その後でuseCallbackで使用
const processData = useCallback(() => {
  const result = helperFunction(data);
  // ...
}, [data]);
```

### 4. 新機能追加時の注意点

新しい関数やuseCallbackを追加する際は：
1. 既存のコードを確認し、その関数を使用する箇所があるか確認
2. 使用箇所がある場合は、それらより**前に**新しい関数を配置
3. ESLintの警告/エラーを必ず確認

### 5. ESLint設定

`.eslintrc.json`で以下の設定を確認：
```json
{
  "rules": {
    "react-hooks/exhaustive-deps": "error",
    "react-hooks/rules-of-hooks": "error"
  }
}
```

これらの設定により、開発時に初期化順序の問題を検出できます。

### 6. デバッグ方法

初期化順序エラーが発生した場合：
1. エラーメッセージで指摘された関数名を確認
2. その関数の定義位置を特定
3. その関数を使用している箇所（useEffect、useCallbackなど）を探す
4. 関数定義を使用箇所より前に移動

### 7. 予防策

- コードレビュー時にHooksの順序を確認
- 新機能追加前に`npm run lint`を実行
- コミット前に必ずアプリケーションの動作確認