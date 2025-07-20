# フロントエンド統合ガイド

## API接続情報

### ベースURL
- 開発環境（WSL）: `http://172.24.67.130:8000/api`
- ローカル環境: `http://localhost:8000/api`

### 主要エンドポイント

#### プロジェクト管理
```javascript
// 一覧取得
GET /api/projects/

// 新規作成
POST /api/projects/
{
  "folder_name": "project_001",
  "project_name": "プロジェクト名",
  "description": "説明",
  "tags": ["タグ1", "タグ2"],
  "status": "active"
}

// 詳細取得
GET /api/projects/{id}/

// 更新
PUT /api/projects/{id}/

// 削除
DELETE /api/projects/{id}/
```

#### ファイル操作
```javascript
// アップロード
POST /api/files/upload/
FormData: { file, project_id }

// ダウンロード
GET /api/files/{id}/download/

// プロジェクト別一覧
GET /api/files/list/{project_id}/
```

## Bolt.newでの使用例

```javascript
// API設定
const API_BASE_URL = 'http://172.24.67.130:8000/api';

// プロジェクト一覧取得
async function fetchProjects() {
  try {
    const response = await fetch(`${API_BASE_URL}/projects/`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching projects:', error);
  }
}

// プロジェクト作成
async function createProject(projectData) {
  try {
    const response = await fetch(`${API_BASE_URL}/projects/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(projectData)
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error creating project:', error);
  }
}
```

## CORS設定
開発環境では全てのオリジンからのアクセスを許可しています。
本番環境では、特定のドメインのみを許可するよう設定を変更してください。

## テスト方法
1. `api_test.html`をブラウザで開く
2. API URLを確認・変更
3. 各ボタンをクリックしてAPIをテスト