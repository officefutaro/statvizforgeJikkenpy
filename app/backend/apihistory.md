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

[2025-07-27 09:35:04] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:43:11] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:43:11] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:44:06] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:44:06] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:44:39] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 09:44:39] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:08:53] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:08:53] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:13:58] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:13:58] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:20:10] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:20:10] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:31:10] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_debug
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

デバッグテスト
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

デバッグ用プロジェクト
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 10:32:30] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 10:32:30] GET /api/files/tree/test_project
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/tree/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 10:32:30] GET /api/files/search/test_project
リクエスト: {'q': ['test'], 'type': ['name']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/search/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/search/test_project?q=test&amp;type=name</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/search/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 10:32:30] POST /api/files/comments/test_project
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/comments/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/comments/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/comments/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 10:32:30] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-25T00:00:00.000000",
  "deleted_projects": []
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 10:33:12] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "SEARCH_QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 10:33:12] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T10:33:12.910414",
  "last_updated": "2025-07-27T10:33:12.910419",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-24T23:31:44.186614",
  "retention_months": 13,
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
  ],
  "archived_projects": [],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-25T00:00:00.000000",
  "deleted_projects": []
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 10:33:12] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "SEARCH_QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 10:33:12] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T10:33:12.912960",
  "last_updated": "2025-07-27T10:33:12.912964",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 10:33:12] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 10:37:20] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

debug_test_project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

デバッグテストプロジェクト
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

デバッグ用プロジェクト
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

debug
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 10:38:36] POST /api/projects/
リクエスト: {"folder_name":"minimal_test","project_name":"Minimal Test","description":"Minimal test project"}
レスポンス: {
  "folder_name": "minimal_test",
  "project_name": "Minimal Test",
  "description": "Minimal test project",
  "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
  "created_date": "2025-07-27T10:38:36.026164",
  "modified_date": "2025-07-27T10:38:36.026164"
}
ステータス: 201
---

[2025-07-27 10:38:36] DELETE /api/projects/1c91b519-f4e1-428c-833d-bfbc95483b9d/
リクエスト: {}
レスポンス: 
ステータス: 204
---

[2025-07-27 10:38:36] POST /api/projects/
リクエスト: {"folder_name": "minimal_test", "project_name": "Minimal Test", "description": "Minimal test project"}
レスポンス: {
  "folder_name": "minimal_test",
  "project_name": "Minimal Test",
  "description": "Minimal test project",
  "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
  "created_date": "2025-07-27T10:38:36.031250",
  "modified_date": "2025-07-27T10:38:36.031250"
}
ステータス: 201
---

[2025-07-27 10:38:36] POST /api/projects/
リクエスト: {"folder_name":"","project_name":"Invalid Test","description":"Invalid test"}
レスポンス: {
  "error": "VALIDATION_ERROR",
  "message": "Invalid input data",
  "details": {
    "folder_name": "This field is required"
  }
}
ステータス: 400
---

[2025-07-27 10:38:36] POST /api/projects/
リクエスト: {"folder_name":"testProject","project_name":"Duplicate Test","description":"Duplicate test"}
レスポンス: {
  "error": "DUPLICATE_FOLDER",
  "message": "A project with this folder name already exists"
}
ステータス: 409
---

[2025-07-27 10:38:36] POST /api/projects/
リクエスト: {"folder_name":"success_test_project","project_name":"成功テストプロジェクト","description":"正常に作成されるべきプロジェクト","tags":["success","test"],"status":"active"}
レスポンス: {
  "folder_name": "success_test_project",
  "project_name": "成功テストプロジェクト",
  "description": "正常に作成されるべきプロジェクト",
  "tags": [
    "success",
    "test"
  ],
  "status": "active",
  "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
  "created_date": "2025-07-27T10:38:36.034282",
  "modified_date": "2025-07-27T10:38:36.034282"
}
ステータス: 201
---

[2025-07-27 10:38:36] DELETE /api/projects/658786da-0f80-4434-bf7c-4e389df4b9b2/
リクエスト: {}
レスポンス: 
ステータス: 204
---

[2025-07-27 10:44:06] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 10:44:06] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:28:13] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:28:13] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:30:51] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:30:51] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:31:01] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:31:01] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:31:13] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:31:13] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:37:24] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:37:24] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:37:28] GET /api/files/tree/testProject
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/tree/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 13:37:28] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:37:28] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:37:59] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:37:59] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:02] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:02] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:06] GET /api/projects/
リクエスト: {'lang': ['zh']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:06] GET /api/projects/
リクエスト: {'lang': ['zh']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:17] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:17] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:38:21] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:38:21] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:39:09] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:39:09] GET /api/projects/
リクエスト: {'lang': ['en']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 13:40:04] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:40:04] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:59:08] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 13:59:08] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 14:10:19] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 14:10:19] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 14:41:24] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 14:41:24] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 14:47:55] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./テスト"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 14:48:02] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./Test"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:09:07] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./TEST"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:13:04] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:13:04] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:13:08] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:13:08] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:13:16] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./テスト"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:13:21] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./Test"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:13:25] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./Test"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:21:12] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./テスト"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:21:17] POST /api/files/mkdir/testProject
リクエスト: {"dir_path":"./テスト"}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/mkdir/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://172.24.67.130:8000/api/files/mkdir/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/mkdir/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:23:21] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:23:25] POST /api/files/mkdir/testProject/
リクエスト: {"dir_path": "test_folder"}
レスポンス: {
  "detail": "リクエストのメディアタイプ \"application/json\" はサポートされていません。"
}
ステータス: 415
---

[2025-07-27 15:23:36] POST /api/files/mkdir/testProject/
リクエスト: dir_path=test_folder
レスポンス: {
  "success": true,
  "message": "Directory created successfully",
  "path": "test_folder"
}
ステータス: 200
---

[2025-07-27 15:39:38] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:39:38] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:39:43] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:39:43] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:39:50] POST /api/files/mkdir/testProject/
リクエスト: ------WebKitFormBoundaryAkY7TgW8fDWItRf2
Content-Disposition: form-data; name="dir_path"

./test
------WebKitFormBoundaryAkY7TgW8fDWItRf2--

レスポンス: {
  "success": true,
  "message": "Directory created successfully",
  "path": "./test"
}
ステータス: 200
---

[2025-07-27 15:39:50] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:39:59] POST /api/files/mkdir/testProject/
リクエスト: ------WebKitFormBoundaryxuVUhKp7ocOH4RIj
Content-Disposition: form-data; name="dir_path"

./test
------WebKitFormBoundaryxuVUhKp7ocOH4RIj--

レスポンス: {
  "success": true,
  "message": "Directory created successfully",
  "path": "./test"
}
ステータス: 200
---

[2025-07-27 15:39:59] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:46:34] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "SEARCH_QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:46:34] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T15:46:34.765182",
  "last_updated": "2025-07-27T15:46:34.765187",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:46:34] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "SEARCH_QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:46:34] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T15:46:34.767943",
  "last_updated": "2025-07-27T15:46:34.767947",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 15:46:34] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:47:02] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 15:47:02] GET /api/files/tree/test_project
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/tree/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:47:02] GET /api/files/search/test_project
リクエスト: {'q': ['test'], 'type': ['name']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/search/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/search/test_project?q=test&amp;type=name</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/search/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:47:02] POST /api/files/comments/test_project
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/comments/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/comments/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-list']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)/$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/(?P&lt;comment_id&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/mkdir/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-create-directory']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/delete/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-delete-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/tree/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-directory-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/comments/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/move/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-move-file']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/search/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-search-files']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)/$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/upload/(?P&lt;project_folder&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)/$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                ^files/(?P&lt;pk&gt;[^/.]+)\.(?P&lt;format&gt;[a-z0-9]+)/?$
                [name='file-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                
                
              </code>
            
              <code>
                &lt;drf_format_suffix:format&gt;
                [name='api-root']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/comments/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:47:02] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:55:51] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:55:51] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T15:55:51.150558",
  "last_updated": "2025-07-27T15:55:51.150563",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:55:51] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:55:51] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "created": "2025-07-27T15:55:51.152796",
  "last_updated": "2025-07-27T15:55:51.152799",
  "comments": {}
}
ステータス: 200
---

[2025-07-27 15:55:51] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:56:36] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 15:56:36] GET /api/files/tree/test_project
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/tree/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:56:36] GET /api/files/search/test_project
リクエスト: {'q': ['test'], 'type': ['name']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/search/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/search/test_project?q=test&amp;type=name</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/search/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:56:36] POST /api/files/comments/test_project
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/comments/test_project</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://testserver/api/files/comments/test_project</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/comments/test_project</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 15:56:36] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:57:48] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 15:57:48] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:57:48] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:57:48] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 15:57:48] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:58:44] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:58:44] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:58:44] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035931",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:58:44] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:58:44] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 15:58:44] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 15:58:44] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 15:59:04] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project"
}
ステータス: 500
---

[2025-07-27 15:59:04] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 15:59:04] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 15:59:04] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 15:59:04] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:03:20] POST /api/projects/
リクエスト: {"folder_name":"debug_test_project","project_name":"デバッグテストプロジェクト","description":"デバッグのためのテストプロジェクト","tags":["debug","test"]}
レスポンス: {
  "folder_name": "debug_test_project",
  "project_name": "デバッグテストプロジェクト",
  "description": "デバッグのためのテストプロジェクト",
  "tags": [
    "debug",
    "test"
  ],
  "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
  "created_date": "2025-07-27T16:03:20.315824",
  "modified_date": "2025-07-27T16:03:20.315824"
}
ステータス: 201
---

[2025-07-27 16:04:49] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:03:20.315824",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:04:49] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:04:49] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:04:49] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 16:04:49] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:04:49] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:03:20.315824",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:06:01] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 16:06:01] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:06:01] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:03:20.315824",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:06:01] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:06:01] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 16:06:01] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 16:06:01] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:06:09] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "error": "FAILED_TO_CREATE_PROJECT",
  "message": "Failed to create project",
  "details": {
    "error_message": "This QueryDict instance is immutable",
    "traceback": "Traceback (most recent call last):\n  File \"/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py\", line 87, in create\n    new_project['id'] = str(uuid.uuid4())\n    ~~~~~~~~~~~^^^^^^\n  File \"/home/futaro/project/StatVizForge_JikkenPy/backend_env/lib/python3.12/site-packages/django/http/request.py\", line 613, in __setitem__\n    self._assert_mutable()\n  File \"/home/futaro/project/StatVizForge_JikkenPy/backend_env/lib/python3.12/site-packages/django/http/request.py\", line 610, in _assert_mutable\n    raise AttributeError(\"This QueryDict instance is immutable\")\nAttributeError: This QueryDict instance is immutable\n"
  }
}
ステータス: 500
---

[2025-07-27 16:06:09] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 16:06:09] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:06:09] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 16:06:09] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:08:14] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "folder_name": [
    "test_project_simple"
  ],
  "project_name": [
    "Simple Test Project"
  ],
  "description": [
    "A simple test project"
  ],
  "tags": [
    "test"
  ],
  "status": [
    "active"
  ],
  "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
  "created_date": "2025-07-27T16:08:14.889746",
  "modified_date": "2025-07-27T16:08:14.889746"
}
ステータス: 201
---

[2025-07-27 16:08:14] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 16:08:14] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:08:14] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 16:08:14] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:42:31] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "folder_name": "test_project_simple",
  "project_name": "Simple Test Project",
  "description": "A simple test project",
  "tags": "test",
  "status": "active",
  "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
  "created_date": "2025-07-27T16:42:31.526622",
  "modified_date": "2025-07-27T16:42:31.526622"
}
ステータス: 201
---

[2025-07-27 16:42:31] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 16:42:31] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 16:42:31] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 16:42:31] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 16:44:36] POST /api/files/mkdir/testProject/
リクエスト: ------WebKitFormBoundaryVPwvqM4gluSt2YZy
Content-Disposition: form-data; name="dir_path"

./test
------WebKitFormBoundaryVPwvqM4gluSt2YZy--

レスポンス: {
  "error": "MKDIR_ERROR",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 500
---

[2025-07-27 16:44:45] POST /api/files/mkdir/testProject/
リクエスト: ------WebKitFormBoundaryhzIKA2P6hBwFGHwK
Content-Disposition: form-data; name="dir_path"

./DDD
------WebKitFormBoundaryhzIKA2P6hBwFGHwK--

レスポンス: {
  "error": "MKDIR_ERROR",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 500
---

[2025-07-27 16:44:48] POST /api/files/mkdir/testProject/
リクエスト: ------WebKitFormBoundaryDaZZxOh0eyXtlL7B
Content-Disposition: form-data; name="dir_path"

./DDD
------WebKitFormBoundaryDaZZxOh0eyXtlL7B--

レスポンス: {
  "error": "MKDIR_ERROR",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 500
---

[2025-07-27 16:45:05] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:45:05] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:45:26] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:45:26] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:51:10] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:52:12] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 16:52:12] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:24:29] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:24:29] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:25:36] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:25:36] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:27:19] GET /api/files/tree/testProject
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8001/api/files/tree/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 20:27:19] GET /api/files/tree/testProject
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/files/tree/testProject</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8001/api/files/tree/testProject</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/files/tree/testProject</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 20:28:31] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:28:36] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:28:42] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:28:51] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:28:51] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T16:42:31.526622",
  "retention_months": 13,
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
    },
    {
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "tags": [],
      "status": "active"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    },
    {
      "folder_name": [
        "test_project_simple"
      ],
      "project_name": [
        "Simple Test Project"
      ],
      "description": [
        "A simple test project"
      ],
      "tags": [
        "test"
      ],
      "status": [
        "active"
      ],
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project",
      "tags": "test",
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "created_date": "2025-07-27T10:38:36.026164",
      "modified_date": "2025-07-27T10:38:36.026164",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.030515",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:33:25] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 20:33:25] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:33:25] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 20:33:25] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:33:25] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 20:33:25] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:33:25] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 20:33:30] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-24T23:31:44.193276",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:33:34] GET /api/files/tree/debug_test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T16:03:20.309871",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:33:39] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:38:36.029027",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:34:15] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:33:51.353635",
  "children": [
    {
      "name": "sample.txt",
      "path": "sample.txt",
      "type": "file",
      "size": 123,
      "modified": "2025-07-27T20:33:46.000352",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "subfolder",
      "path": "subfolder",
      "type": "directory",
      "size": 0,
      "modified": "2025-07-27T20:33:56.074794",
      "children": [
        {
          "name": "nested_file.py",
          "path": "subfolder/nested_file.py",
          "type": "file",
          "size": 185,
          "modified": "2025-07-27T20:33:56.067116",
          "children": [],
          "comment_count": 0,
          "has_comments": false
        }
      ],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:34:22] GET /api/files/tree/debug_test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:00.984380",
  "children": [
    {
      "name": "debug_data.json",
      "path": "debug_data.json",
      "type": "file",
      "size": 236,
      "modified": "2025-07-27T20:34:00.980542",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:34:26] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:34:41] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:39:14] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 20:39:14] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:39:14] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-27 20:39:14] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:39:14] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-27 20:39:14] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-27 20:39:14] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 20:39:21] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "folder_name": "test_project_simple",
  "project_name": "Simple Test Project",
  "description": "A simple test project",
  "tags": "test",
  "status": "active",
  "id": "30e0ecd5-6765-4922-8796-454163240a0b",
  "created_date": "2025-07-27T20:39:21.557377",
  "modified_date": "2025-07-27T20:39:21.557377"
}
ステータス: 201
---

[2025-07-27 20:39:21] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:39:21] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-27 20:39:21] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-27 20:39:21] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-27 20:39:26] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T17:30:00.000000",
  "retention_months": 13,
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
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T10:38:36.031250"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト",
      "tags": [
        "debug",
        "test"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T16:03:20.315824"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:44:36] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:44:41] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:33:51.353635",
  "children": [
    {
      "name": "sample.txt",
      "path": "sample.txt",
      "type": "file",
      "size": 123,
      "modified": "2025-07-27T20:33:46.000352",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "subfolder",
      "path": "subfolder",
      "type": "directory",
      "size": 0,
      "modified": "2025-07-27T20:33:56.074794",
      "children": [
        {
          "name": "nested_file.py",
          "path": "subfolder/nested_file.py",
          "type": "file",
          "size": 185,
          "modified": "2025-07-27T20:33:56.067116",
          "children": [],
          "comment_count": 0,
          "has_comments": false
        }
      ],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:44:45] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:44:50] GET /api/files/tree/debug_test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:00.984380",
  "children": [
    {
      "name": "debug_data.json",
      "path": "debug_data.json",
      "type": "file",
      "size": 236,
      "modified": "2025-07-27T20:34:00.980542",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:46:28] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:46:28] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 20:46:35] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:33:51.353635",
  "children": [
    {
      "name": "sample.txt",
      "path": "sample.txt",
      "type": "file",
      "size": 123,
      "modified": "2025-07-27T20:33:46.000352",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "subfolder",
      "path": "subfolder",
      "type": "directory",
      "size": 0,
      "modified": "2025-07-27T20:33:56.074794",
      "children": [
        {
          "name": "nested_file.py",
          "path": "subfolder/nested_file.py",
          "type": "file",
          "size": 185,
          "modified": "2025-07-27T20:33:56.067116",
          "children": [],
          "comment_count": 0,
          "has_comments": false
        }
      ],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 20:46:35] GET /api/files/tree/testProject/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:33:51.353635",
  "children": [
    {
      "name": "sample.txt",
      "path": "sample.txt",
      "type": "file",
      "size": 123,
      "modified": "2025-07-27T20:33:46.000352",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "subfolder",
      "path": "subfolder",
      "type": "directory",
      "size": 0,
      "modified": "2025-07-27T20:33:56.074794",
      "children": [
        {
          "name": "nested_file.py",
          "path": "subfolder/nested_file.py",
          "type": "file",
          "size": 185,
          "modified": "2025-07-27T20:33:56.067116",
          "children": [],
          "comment_count": 0,
          "has_comments": false
        }
      ],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:00:26] POST /api/jupyter/start/
リクエスト: {"project_folder": "testProject"}
レスポンス: {
  "success": true,
  "url": "http://127.0.0.1:8888",
  "port": 8888,
  "message": "JupyterLab started successfully",
  "project_folder": "testProject"
}
ステータス: 200
---

[2025-07-27 21:20:22] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 21:20:22] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 21:20:30] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:20:30] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:20:37] POST /api/jupyter/start/
リクエスト: {"project_folder":"minimal_test"}
レスポンス: {
  "success": true,
  "url": "http://127.0.0.1:8889",
  "port": 8889,
  "message": "JupyterLab started successfully",
  "project_folder": "minimal_test"
}
ステータス: 200
---

[2025-07-27 21:20:39] POST /api/jupyter/start/
リクエスト: {"project_folder":"minimal_test"}
レスポンス: {
  "success": true,
  "url": "http://127.0.0.1:8890",
  "port": 8890,
  "message": "JupyterLab started successfully",
  "project_folder": "minimal_test"
}
ステータス: 200
---

[2025-07-27 21:23:01] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 21:23:07] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:23:07] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:23:13] POST /api/jupyter/start/
リクエスト: {"project_folder":"minimal_test"}
レスポンス: {
  "success": true,
  "url": "http://172.24.67.130:8891",
  "port": 8891,
  "message": "JupyterLab started successfully",
  "project_folder": "minimal_test"
}
ステータス: 200
---

[2025-07-27 21:23:16] POST /api/jupyter/start/
リクエスト: {"project_folder":"minimal_test"}
レスポンス: {
  "success": true,
  "url": "http://172.24.67.130:8892",
  "port": 8892,
  "message": "JupyterLab started successfully",
  "project_folder": "minimal_test"
}
ステータス: 200
---

[2025-07-27 21:29:08] POST /api/jupyter/start/
リクエスト: {"project_folder": "testProject"}
レスポンス: {
  "success": true,
  "url": "http://172.24.67.130:8893",
  "port": 8893,
  "message": "JupyterLab started successfully",
  "project_folder": "testProject"
}
ステータス: 200
---

[2025-07-27 21:29:28] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 21:29:28] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 21:29:38] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:29:38] GET /api/files/tree/minimal_test/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": ".",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T20:34:11.205509",
  "children": [
    {
      "name": "README.md",
      "path": "README.md",
      "type": "file",
      "size": 295,
      "modified": "2025-07-27T20:34:06.625921",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    },
    {
      "name": "data.csv",
      "path": "data.csv",
      "type": "file",
      "size": 142,
      "modified": "2025-07-27T20:34:11.201611",
      "children": [],
      "comment_count": 0,
      "has_comments": false
    }
  ],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-27 21:29:40] POST /api/jupyter/start/
リクエスト: {"project_folder":"minimal_test"}
レスポンス: {
  "success": true,
  "url": "http://172.24.67.130:8892",
  "port": 8892,
  "message": "JupyterLab is already running",
  "project_folder": "minimal_test"
}
ステータス: 200
---

[2025-07-27 23:46:45] HEAD /api/
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>HEAD</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-27 23:46:45] HEAD /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 23:47:21] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 23:47:24] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 23:54:52] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 23:54:53] HEAD /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-27 23:55:32] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 00:12:51] HEAD /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 00:12:51] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 00:16:01] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 00:26:53] HEAD /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/files/tree/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-28 07:41:11] GET /api/files/search/test_project/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-28 07:41:11] GET /api/files/comments/nonexistent_project/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-28 07:41:11] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/projects/deleted/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T10:38:36.035743",
  "deleted_projects": [
    {
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952598",
      "original_created_date": "2025-07-27T10:37:56.949497",
      "tags": [
        "test"
      ],
      "description": "直接テスト用プロジェクト"
    },
    {
      "id": "1c91b519-f4e1-428c-833d-bfbc95483b9d",
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "archive_filename": "minimal_test_20250727_103836.zip",
      "archive_size": 292,
      "deletion_date": "2025-07-27T10:38:36.029972",
      "original_created_date": "2025-07-27T10:38:36.026164",
      "tags": [],
      "description": "Minimal test project"
    },
    {
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035740",
      "original_created_date": "2025-07-27T10:38:36.034282",
      "tags": [
        "success",
        "test"
      ],
      "description": "正常に作成されるべきプロジェクト"
    }
  ]
}
ステータス: 200
---

[2025-07-28 07:41:11] GET /api/files/tree/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-28 07:41:11] GET /api/files/search/test/
リクエスト: {}
レスポンス: {
  "error": "QUERY_REQUIRED",
  "message": "An unexpected error occurred. Please try again later"
}
ステータス: 400
---

[2025-07-28 07:41:11] GET /api/files/comments/test/
リクエスト: {}
レスポンス: {
  "error": "PROJECT_NOT_FOUND",
  "message": "Project not found"
}
ステータス: 404
---

[2025-07-28 07:41:11] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 07:41:23] POST /api/projects/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="folder_name"

test_project_simple
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="project_name"

Simple Test Project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="description"

A simple test project
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="tags"

test
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="status"

active
--BoUnDaRyStRiNg--

レスポンス: {
  "folder_name": "test_project_simple",
  "project_name": "Simple Test Project",
  "description": "A simple test project",
  "tags": "test",
  "status": "active",
  "id": "28674338-2539-4ab8-8786-214a92533a7b",
  "created_date": "2025-07-28T07:41:23.132407",
  "modified_date": "2025-07-28T07:41:23.132407"
}
ステータス: 201
---

[2025-07-28 07:41:23] GET /api/files/tree/test_project/
リクエスト: {}
レスポンス: {
  "name": "raw",
  "path": "",
  "type": "directory",
  "size": 0,
  "modified": "2025-07-27T10:00:00",
  "children": [],
  "comment_count": 0,
  "has_comments": false
}
ステータス: 200
---

[2025-07-28 07:41:23] GET /api/files/search/test_project/
リクエスト: {'query': ['test'], 'type': ['name']}
レスポンス: {
  "success": true,
  "query": "test",
  "search_type": "name",
  "total_results": 1,
  "results": [
    {
      "name": "test.txt",
      "path": "test.txt",
      "type": "file",
      "size": 100,
      "modified": "2025-07-27T10:00:00",
      "match_type": "name",
      "directory": ""
    }
  ]
}
ステータス: 200
---

[2025-07-28 07:41:23] POST /api/files/comments/test_project/
リクエスト: --BoUnDaRyStRiNg
Content-Disposition: form-data; name="file_path"

test.txt
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="comment"

Test comment
--BoUnDaRyStRiNg
Content-Disposition: form-data; name="author"

Test User
--BoUnDaRyStRiNg--

レスポンス: {
  "success": true,
  "comment": {
    "id": "test_comment",
    "text": "Test comment",
    "author": "Test User",
    "created_at": "2025-07-27T10:00:00"
  }
}
ステータス: 201
---

[2025-07-28 07:41:23] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 09:22:06] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 09:30:54] GET /api/projects/
リクエスト: {}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 09:54:07] GET /api/projects
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:10] GET /api/projects
リクエスト: {'lang': ['ja']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects?lang=ja</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:10] GET /api/projects
リクエスト: {'lang': ['ja']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects?lang=ja</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:10] GET /api/projects
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:10] GET /api/projects
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:28] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 10:11:33] GET /api/projects
リクエスト: {'lang': ['ja']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects?lang=ja</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:33] GET /api/projects
リクエスト: {'lang': ['ja']}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects?lang=ja</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:33] GET /api/projects
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:11:33] GET /api/projects
リクエスト: {}
レスポンス: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/projects</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style>
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font-family: sans-serif; background:#eee; color:#000; }
    body > :where(header, main, footer) { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 small { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
</head>
<body>
  <header id="summary">
    <h1>Page not found <small>(404)</small></h1>
    
    <table class="meta">
      <tr>
        <th scope="row">Request Method:</th>
        <td>GET</td>
      </tr>
      <tr>
        <th scope="row">Request URL:</th>
        <td>http://localhost:8000/api/projects</td>
      </tr>
      
    </table>
  </header>

  <main id="info">
    
      <p>
      Using the URLconf defined in <code>config.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
              <code>
                admin/
                
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/tree/&lt;str:project_folder&gt;/
                [name='file-tree']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/upload/&lt;str:project_folder&gt;/
                [name='file-upload']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/search/&lt;str:project_folder&gt;/
                [name='file-search']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/delete/&lt;str:project_folder&gt;/
                [name='file-delete']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/move/&lt;str:project_folder&gt;/
                [name='file-move']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/mkdir/&lt;str:project_folder&gt;/
                [name='file-mkdir']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/
                [name='file-comments']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                files/comments/&lt;str:project_folder&gt;/&lt;str:comment_id&gt;/
                [name='file-comment-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/
                [name='project-list-create']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/deleted/
                [name='project-deleted']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/
                [name='project-detail']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                projects/&lt;str:pk&gt;/restore/
                [name='project-restore']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/start/
                [name='jupyter-start']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/stop/
                [name='jupyter-stop']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                jupyter/status/
                [name='jupyter-status']
              </code>
            
          </li>
        
          <li>
            
              <code>
                api/
                
              </code>
            
              <code>
                server-info/
                [name='server_info']
              </code>
            
          </li>
        
          <li>
            
              <code>
                ^media/(?P&lt;path&gt;.*)$
                
              </code>
            
          </li>
        
      </ol>
      <p>
        
          The current path, <code>api/projects</code>,
        
        didn’t match any of these.
      </p>
    
  </main>

  <footer id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </footer>
</body>
</html>

ステータス: 404
---

[2025-07-28 10:24:50] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 10:24:57] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 10:24:57] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 10:35:39] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 10:35:39] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 10:36:46] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 11:03:41] GET /api/server-info/
リクエスト: {}
レスポンス: {
  "debug_mode": true,
  "environment": "development",
  "django_version": "5.2.4",
  "api_version": "1.0.0"
}
ステータス: 200
---

[2025-07-28 11:04:20] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---

[2025-07-28 11:04:20] GET /api/projects/
リクエスト: {'lang': ['ja']}
レスポンス: {
  "version": "1.0.0",
  "last_updated": "2025-07-27T20:40:00.000000",
  "retention_months": 13,
  "projects": [
    {
      "folder_name": "testProject",
      "project_name": "テストのためのプロジェクト",
      "description": "テストです。サンプルファイルとサブフォルダが追加されました。",
      "tags": [
        "sample"
      ],
      "status": "active",
      "id": "2cec431a-0416-4451-a43b-fdc85e0c5c62",
      "created_date": "2025-07-24T23:31:44.186614",
      "modified_date": "2025-07-27T20:33:51.353635"
    },
    {
      "folder_name": "minimal_test",
      "project_name": "Minimal Test",
      "description": "Minimal test project with README and CSV data",
      "tags": [
        "test",
        "data"
      ],
      "status": "active",
      "id": "a908299f-f131-4f70-8b16-43fd9f01b7d2",
      "created_date": "2025-07-27T10:38:36.031250",
      "modified_date": "2025-07-27T20:34:11.205509"
    },
    {
      "folder_name": "debug_test_project",
      "project_name": "デバッグテストプロジェクト",
      "description": "デバッグのためのテストプロジェクト（JSONデータファイル付き）",
      "tags": [
        "debug",
        "test",
        "json"
      ],
      "status": "active",
      "id": "c51050dc-a2c0-418f-9e1f-e65e42c6516a",
      "created_date": "2025-07-27T16:03:20.315824",
      "modified_date": "2025-07-27T20:34:00.984380"
    }
  ],
  "archived_projects": [
    {
      "folder_name": "direct_test_project",
      "project_name": "直接テストプロジェクト",
      "description": "直接テスト用プロジェクト",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "82886a55-fe6c-4559-9dfa-27aeb21e924e",
      "created_date": "2025-07-27T10:37:56.949497",
      "modified_date": "2025-07-27T10:37:56.949497",
      "archive_filename": "direct_test_project_20250727_103756.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/direct_test_project_20250727_103756.zip",
      "archive_size": 347,
      "deletion_date": "2025-07-27T10:37:56.952974",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "success_test_project",
      "project_name": "成功テストプロジェクト",
      "description": "正常に作成されるべきプロジェクト",
      "tags": [
        "success",
        "test"
      ],
      "status": "active",
      "id": "658786da-0f80-4434-bf7c-4e389df4b9b2",
      "created_date": "2025-07-27T10:38:36.034282",
      "modified_date": "2025-07-27T10:38:36.034282",
      "archive_filename": "success_test_project_20250727_103836.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/success_test_project_20250727_103836.zip",
      "archive_size": 385,
      "deletion_date": "2025-07-27T10:38:36.035929",
      "reason": "ユーザー削除"
    },
    {
      "folder_name": "save_test",
      "project_name": "セーブテスト",
      "description": "セーブテスト（フォルダが存在しないため移動）",
      "tags": [],
      "status": "active",
      "id": "bb5830e9-e13c-4960-bc25-fa8045a272e9",
      "created_date": "2025-07-27T10:37:56.948759",
      "modified_date": "2025-07-27T10:37:56.948769",
      "archive_filename": "save_test_auto_archived.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/save_test_auto_archived.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "フォルダが存在しないため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（不正データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "bd7e7a94-fce7-471b-9dce-7e4c1bcb8255",
      "created_date": "2025-07-27T16:08:14.889746",
      "modified_date": "2025-07-27T16:08:14.889746",
      "archive_filename": "test_project_simple_invalid_data.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_invalid_data.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "不正な配列データのため自動アーカイブ"
    },
    {
      "folder_name": "test_project_simple",
      "project_name": "Simple Test Project",
      "description": "A simple test project（重複データのため移動）",
      "tags": [
        "test"
      ],
      "status": "active",
      "id": "7e7be177-9396-4e40-baf3-0b15c2310500",
      "created_date": "2025-07-27T16:42:31.526622",
      "modified_date": "2025-07-27T16:42:31.526622",
      "archive_filename": "test_project_simple_duplicate.zip",
      "archive_path": "/home/futaro/project/StatVizForge_JikkenPy/project/trash/test_project_simple_duplicate.zip",
      "archive_size": 0,
      "deletion_date": "2025-07-27T17:30:00.000000",
      "reason": "重複データのため自動アーカイブ"
    }
  ],
  "reserved_folders": [
    "node_modules",
    "dist",
    "build",
    ".git",
    "backend",
    "frontend",
    "trash",
    "recycle_bin",
    "deleted",
    ".trash"
  ]
}
ステータス: 200
---
