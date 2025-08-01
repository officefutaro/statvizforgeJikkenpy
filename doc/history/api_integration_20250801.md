# API整合性テストレポート - 2025年08月01日

## サマリー

- **総エンドポイント数**: 64
- **実装済みエンドポイント数**: 5
- **カバレッジ**: 27.8%

## フロントエンド未実装エンドポイント

- [ ] /api/v1/
- [ ] /api/v1/files/
- [ ] /api/v1/files/(?P{}[^/.]+)/
- [ ] /api/v1/files/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/column-types/(?P{}[^/.]+)/
- [ ] /api/v1/files/column-types/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/comments/(?P{}[^/.]+)/(?P{}[^/.]+)/
- [ ] /api/v1/files/comments/(?P{}[^/.]+)/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/delete/(?P{}[^/.]+)/
- [ ] /api/v1/files/delete/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/delete/{}/
- [ ] /api/v1/files/descriptions/(?P{}[^/.]+)/?/
- [ ] /api/v1/files/descriptions/(?P{}[^/.]+)/?\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/descriptions/{}/
- [ ] /api/v1/files/mkdir/(?P{}[^/.]+)/
- [ ] /api/v1/files/mkdir/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/move/(?P{}[^/.]+)/
- [ ] /api/v1/files/move/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/move/{}/
- [ ] /api/v1/files/search/(?P{}[^/.]+)/
- [ ] /api/v1/files/search/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/search/{}/
- [ ] /api/v1/files/table/
- [ ] /api/v1/files/table/{}/
- [ ] /api/v1/files/table\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/tags/(?P{}[^/.]+)/?/
- [ ] /api/v1/files/tags/(?P{}[^/.]+)/?\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/tags/{}/
- [ ] /api/v1/files/tree/(?P{}[^/.]+)/
- [ ] /api/v1/files/tree/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files/upload/(?P{}[^/.]+)/
- [ ] /api/v1/files/upload/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/files\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/jupyter/start/
- [ ] /api/v1/jupyter/start\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/jupyter/status/
- [ ] /api/v1/jupyter/status\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/jupyter/stop/
- [ ] /api/v1/jupyter/stop\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/projects/
- [ ] /api/v1/projects/(?P{}[^/.]+)/
- [ ] /api/v1/projects/(?P{}[^/.]+)/restore/
- [ ] /api/v1/projects/(?P{}[^/.]+)/restore\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/projects/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/projects/deleted/
- [ ] /api/v1/projects/deleted\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/projects/validate_registry/
- [ ] /api/v1/projects/validate_registry\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/projects/{}/restore/
- [ ] /api/v1/projects\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/table-settings/mouseover-settings/(?P{}[^/.]+)/
- [ ] /api/v1/table-settings/mouseover-settings/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/table-settings/settings/(?P{}[^/.]+)/
- [ ] /api/v1/table-settings/settings/(?P{}[^/.]+)/(?P{}[^/.]+)/
- [ ] /api/v1/table-settings/settings/(?P{}[^/.]+)/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/table-settings/settings/(?P{}[^/.]+)\.(?P{}[a-z0-9]+)/?/
- [ ] /api/v1/table-settings/settings/{}/
- [ ] /api/v1/test/
- [ ] /api/v1/{}/

## バックエンド未実装エンドポイント

- [ ] /api/v1/files/comment/{}/
- [ ] /api/v1/files/search/{}?{}/
- [ ] /api/v1/projects/deleted/{}/
- [ ] /api/v1/projects/{}/restore/{}/
- [ ] /api/v1/projects/{}/{}/

## 型定義の不整合

### Project

**TypeScriptに不足**:
- l
- a
- _
**Djangoに不足**:
- folder_name
- description
- created_date
- status
- tags
- project_name
- modified_date
- id

## 改善提案

- エンドポイントカバレッジが80%未満です。未実装のエンドポイントを確認してください。
- TypeScriptインターフェースとDjangoシリアライザーの型定義に不整合があります。
- フロントエンドに59個の未実装エンドポイントがあります。
- バックエンドに5個の未実装エンドポイントがあります。
