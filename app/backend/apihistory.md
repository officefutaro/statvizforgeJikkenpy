# API呼び出し履歴

開発モードでのAPI呼び出し履歴を記録します。

---

## 履歴フォーマット
```
[日時] [メソッド] [エンドポイント]
リクエスト: {リクエスト内容}
レスポンス: {レスポンス内容}
---
```

## 履歴開始: 2025-07-20

[2025-07-23 23:09:53] GET /api/projects/list
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-01-22T12:00:00Z",
  "projects": []
}
ステータス: 200
---

[2025-07-23 23:14:31] GET /api/projects/list
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-01-22T12:00:00Z",
  "projects": []
}
ステータス: 200
---

[2025-07-24 23:31:11] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-01-22T12:00:00Z",
  "projects": []
}
ステータス: 200
---

[2025-07-24 23:31:11] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-01-22T12:00:00Z",
  "projects": []
}
ステータス: 200
---

[2025-07-24 23:31:16] GET /api/projects/list
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-01-22T12:00:00Z",
  "projects": []
}
ステータス: 200
---

[2025-07-24 23:31:44] POST /api/projects/create
リクエスト: {"folder_name":"testProject","project_name":"テストのためのプロジェクト","description":"テストです。","tags":[],"status":"active"}
レスポンス: {
  "folder_name": "testProject",
  "project_name": "テストのためのプロジェクト",
  "description": "テストです。",
  "tags": [],
  "status": "active",
  "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
  "created_date": "2025-07-24T23:31:44.186614",
  "modified_date": "2025-07-24T23:31:44.186614"
}
ステータス: 201
---

[2025-07-24 23:31:44] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:32:46] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:32:46] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:32:47] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:32:47] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:43:50] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:43:50] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:43:58] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:43:58] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:44:05] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:44:05] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:44:42] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-24 23:44:42] GET /api/projects/list
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。",
      "tags": [],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-24T23:31:44.186614"
    }
  ]
}
ステータス: 200
---

[2025-07-26 18:03:20] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---
