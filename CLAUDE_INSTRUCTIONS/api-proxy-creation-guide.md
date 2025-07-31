# APIプロキシ作成ガイド

## 🚨 重要：新しいAPIエンドポイント作成時の必須手順

### 1. **統一設定の更新**

新しいAPIエンドポイントを追加する際は、**必ず最初に**以下のファイルを更新してください：

**ファイル**: `app/frontend/lib/api-config.ts`

```typescript
export const API_ENDPOINTS = {
  // 既存のエンドポイント...
  
  // 新しいエンドポイントを追加
  NEW_ENDPOINT: '/api/new-endpoint',
  NEW_ENDPOINT_WITH_PARAM: (param: string) => `/api/new-endpoint/${param}`,
} as const;
```

### 2. **プロキシファイルの作成**

新しいAPIプロキシを作成する際は、統一テンプレートを使用：

**ファイル**: `app/frontend/app/api/[new-endpoint]/route.ts`

```typescript
import { NextRequest } from 'next/server';
import { API_ENDPOINTS } from '@/lib/api-config';
import { createGetProxy, createPostProxy } from '@/lib/api-proxy-template';

export async function GET(request: NextRequest) {
  return createGetProxy(request, API_ENDPOINTS.NEW_ENDPOINT, { 
    serviceName: 'NewService' 
  });
}

export async function POST(request: NextRequest) {
  return createPostProxy(request, API_ENDPOINTS.NEW_ENDPOINT, { 
    serviceName: 'NewService',
    timeout: 10000 // 必要に応じてタイムアウトを調整
  });
}
```

### 3. **動的パラメータ付きプロキシ**

パラメータを含むエンドポイントの場合：

```typescript
export async function GET(
  request: NextRequest,
  { params }: { params: { slug: string[] } }
) {
  const slug = params.slug.join('/');
  const endpoint = `/api/files/${slug}`;
  
  return createGetProxy(request, endpoint, { 
    serviceName: 'Files' 
  });
}
```

### 4. **チェックリスト**

新しいAPIプロキシを作成した際は、以下を確認してください：

- [ ] `api-config.ts`にエンドポイントを追加済み
- [ ] 統一テンプレート(`createGetProxy`, `createPostProxy`)を使用
- [ ] 適切なサービス名を設定
- [ ] 必要に応じてタイムアウトを調整
- [ ] ログに一貫した形式を使用

### 5. **禁止事項**

❌ **絶対にしてはいけないこと**：

```typescript
// ❌ 直接バックエンドURLをハードコード
const backendUrl = 'http://localhost:8000/api/endpoint';

// ❌ WSL IPを個別に定義
const wslIp = '172.24.67.130';

// ❌ 独自のfetch実装
const response = await fetch(url, { /* 独自設定 */ });
```

✅ **正しい方法**：

```typescript
// ✅ 統一設定を使用
import { API_ENDPOINTS } from '@/lib/api-config';
import { createGetProxy } from '@/lib/api-proxy-template';

export async function GET(request: NextRequest) {
  return createGetProxy(request, API_ENDPOINTS.ENDPOINT, { 
    serviceName: 'Service' 
  });
}
```

### 6. **テスト手順**

新しいAPIプロキシ作成後：

1. **WSL Firefox**でテスト: `http://localhost:3000`
2. **Windows Chrome**でテスト: `http://172.24.67.130:3000`
3. ログ出力の確認: `[Service API Proxy] GET Success: /api/endpoint`
4. エラーハンドリングの確認

### 7. **トラブルシューティング**

**問題**: 404エラーが発生
- **確認**: `api-config.ts`にエンドポイントが正しく定義されているか
- **確認**: バックエンドにも対応するエンドポイントが存在するか

**問題**: タイムアウトエラー
- **解決**: `timeout`パラメータを増やす

**問題**: WSL IPアクセスができない
- **確認**: `getBackendUrl()`を使用しているか（直接IPを書いていないか）

---

## 🛡️ この手順を守ることで以下を防げます：

- ✅ エンドポイント不整合
- ✅ WSL2ネットワーク問題
- ✅ タイムアウト設定の不統一
- ✅ ログ形式の不統一
- ✅ エラーハンドリングの漏れ

**新しいAPIを追加する開発者は、必ずこのガイドに従ってください。**