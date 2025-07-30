# StatVizForge API v2.0 テスト計画

## 概要
API v2.0の主要な改善点に対する包括的なテスト計画です。セキュリティ強化、バージョニング、バリデーション、エラーハンドリングの改善をテストします。

## テスト実行日時
- **計画作成日**: 2025年7月30日
- **対象バージョン**: v2.0.0
- **テスト環境**: 開発環境（localhost:8000）

## 1. APIバージョニングテスト

### 1.1 バージョン別アクセステスト
```python
# テストケース
- GET /api/v1/projects/ → 成功（200）
- GET /api/projects/ → 成功（200、後方互換性）
- GET /api/v2/projects/ → 失敗（404、未実装バージョン）
```

### 1.2 バージョン間の動作確認
```python
# 両バージョンで同じ結果が返ることを確認
response_v1 = GET /api/v1/projects/
response_legacy = GET /api/projects/
assert response_v1.json() == response_legacy.json()
```

## 2. セキュリティ強化テスト

### 2.1 ファイルパスバリデーション
```python
# ディレクトリトラバーサル攻撃の防止
test_cases = [
    {"file_path": "../../../etc/passwd", "expected": 400},
    {"file_path": "/etc/passwd", "expected": 400},
    {"file_path": "..\\..\\windows\\system32", "expected": 400},
    {"file_path": "data/file.csv", "expected": 200},
    {"file_path": "folder/subfolder/file.txt", "expected": 200}
]
```

### 2.2 プロジェクトフォルダ名バリデーション
```python
# 無効な文字のテスト
test_cases = [
    {"folder_name": "valid_project-123", "expected": 200},
    {"folder_name": "invalid/project", "expected": 400},
    {"folder_name": "project with spaces", "expected": 400},
    {"folder_name": "プロジェクト", "expected": 400},
    {"folder_name": "a" * 101, "expected": 400}  # 長さ制限
]
```

### 2.3 危険な文字のフィルタリング
```python
# Null文字、改行コードなどの検証
dangerous_paths = [
    "file\0.csv",
    "file\n.csv",
    "file\r\n.csv",
    "~file.csv"
]
```

## 3. レート制限テスト（本番環境）

### 3.1 匿名ユーザーのレート制限
```python
# 100リクエスト/時間の制限
for i in range(101):
    response = GET /api/v1/projects/
    if i < 100:
        assert response.status_code == 200
    else:
        assert response.status_code == 429  # Too Many Requests
```

### 3.2 認証済みユーザーのレート制限
```python
# 1000リクエスト/時間の制限（将来の実装）
# ヘッダー: X-API-KEY: valid_key
```

## 4. エラーハンドリング統一テスト

### 4.1 統一エラーレスポンス形式
```python
# すべてのエラーが統一形式であることを確認
error_endpoints = [
    ("/api/v1/projects/invalid-uuid/", 404),
    ("/api/v1/files/tree/nonexistent/", 404),
    ("/api/v1/files/descriptions/test/", {"file_path": "../etc/passwd"}, 400)
]

for endpoint, expected_status in error_endpoints:
    response = request(endpoint)
    assert response.status_code == expected_status
    assert "error" in response.json()
    assert "message" in response.json()
```

### 4.2 多言語対応エラーメッセージ
```python
# 言語別エラーメッセージのテスト
languages = ["en", "ja", "zh"]
for lang in languages:
    response = GET /api/v1/projects/invalid/?lang={lang}
    assert response.json()["message"] != ""  # ローカライズされたメッセージ
```

## 5. 認証・認可基盤テスト（将来の実装確認）

### 5.1 APIキー認証の準備確認
```python
# 認証クラスが実装されていることを確認
from api.authentication import APIKeyAuthentication, IsProjectOwner
assert APIKeyAuthentication is not None
assert IsProjectOwner is not None
```

### 5.2 権限クラスの動作確認
```python
# 開発環境では全て許可されることを確認
permission = IsProjectOwner()
assert permission.has_permission(request, view) == True
```

## 6. パフォーマンステスト

### 6.1 レスポンス時間測定
```python
import time

endpoints = [
    "/api/v1/projects/",
    "/api/v1/files/tree/test_project/",
    "/api/v1/server-info/"
]

for endpoint in endpoints:
    start = time.time()
    response = GET endpoint
    duration = time.time() - start
    assert duration < 1.0  # 1秒以内
```

## 7. 後方互換性テスト

### 7.1 既存エンドポイントの動作確認
```python
# 既存のエンドポイントが引き続き動作することを確認
legacy_endpoints = [
    "/api/projects/",
    "/api/files/tree/project/",
    "/api/server-info/"
]

for endpoint in legacy_endpoints:
    response = GET endpoint
    assert response.status_code in [200, 404]  # 正常またはNot Found
```

## 8. 統合テスト

### 8.1 完全なワークフローテスト
```python
# 1. プロジェクト作成（バリデーション含む）
project_data = {
    "folder_name": "test_project_v2",
    "project_name": "テストプロジェクトv2",
    "description": "API v2.0テスト"
}
response = POST /api/v1/projects/ data=project_data

# 2. ファイル操作（セキュリティチェック含む）
file_data = {
    "file_path": "data/test.csv",
    "description": "テストファイル"
}
response = POST /api/v1/files/descriptions/{folder}/ data=file_data

# 3. 削除・復元
DELETE /api/v1/projects/{id}/
POST /api/v1/projects/{id}/restore/
```

## テスト実行スクリプト

```bash
#!/bin/bash
# API v2.0 テスト実行スクリプト

cd /home/futaro/project/StatVizForge_JikkenPy/app/backend

# 仮想環境をアクティベート
source venv/bin/activate

# テスト実行
python manage.py test api.tests.test_api_v2 --verbosity=2

# カスタムテストスクリプト実行
python test_api_v2_security.py
python test_api_v2_validation.py
python test_api_v2_performance.py

# レポート生成
python generate_test_report.py --version=v2.0.0
```

## 期待される結果

1. **セキュリティ**: すべての危険なパスが適切にブロックされる
2. **バリデーション**: 無効な入力が適切なエラーメッセージと共に拒否される
3. **パフォーマンス**: すべてのエンドポイントが1秒以内に応答
4. **互換性**: 既存のAPIクライアントが引き続き動作
5. **エラーハンドリング**: 統一されたエラーレスポンス形式

## 成功基準

- [ ] すべてのセキュリティテストが合格
- [ ] バリデーションエラーが適切に処理される
- [ ] レート制限が正しく機能（本番環境）
- [ ] 後方互換性が維持される
- [ ] パフォーマンス基準を満たす
- [ ] エラーレスポンスが統一形式

## リスクと対策

1. **リスク**: 既存クライアントの互換性問題
   - **対策**: /api/エンドポイントの維持、段階的移行

2. **リスク**: 過度なバリデーションによる正当なリクエストの拒否
   - **対策**: 十分なテストケースとログ監視

3. **リスク**: パフォーマンスの低下
   - **対策**: バリデーション処理の最適化