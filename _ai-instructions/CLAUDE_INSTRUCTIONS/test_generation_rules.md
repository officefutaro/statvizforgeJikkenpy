# テスト生成時の約束事

## 基本方針
テストコードの生成・作成時は以下の約束事を厳守する。

## 1. テストファイルの命名規則
- **バックエンド**: `test_*.py` 形式
- **フロントエンド**: `*.test.tsx` または `*.spec.ts` 形式
- 元のファイル名を基準とした命名
  - 例: `views.py` → `test_views.py`
  - 例: `FileExplorer.tsx` → `FileExplorer.test.tsx`

## 2. テスト内容の網羅性
### 必須テストケース
1. **正常系テスト**: 期待される動作の確認
2. **異常系テスト**: エラーハンドリングの確認
3. **境界値テスト**: 限界値での動作確認
4. **バリデーションテスト**: 入力検証の確認

### 機能別テストケース
- **API**: リクエスト/レスポンス、ステータスコード、エラーハンドリング
- **UI**: ユーザーインタラクション、表示/非表示、状態変化
- **データ処理**: 入力変換、計算結果、データ整合性

## 3. テストコードの品質基準
### 構造
- **Arrange**: テストデータの準備
- **Act**: テスト対象の実行
- **Assert**: 結果の検証

### 命名
- テスト関数名は処理内容を明確に表現
- 日本語でのテスト名も許可（`test_save_file_tags_success`）
- 目的が分かりやすいコメント追加

### データ
- **モックデータ**: 実際のデータ構造に準拠
- **テスト用プロジェクト**: `test_project` などの専用名称使用
- **一意性**: テスト間でのデータ競合回避

## 4. 技術的要件
### バックエンド (Django)
- `APITestCase` または `TestCase` の使用
- `@patch` デコレータでの外部依存関係モック
- `DjangoTestCaseMixin` の継承（利用可能な場合）
- レスポンス形式の検証（JSON構造、必須フィールド）

#### Django特有の重要な注意事項
1. **QueryDict の配列データ処理**
   - Django の QueryDict は複数値フィールドで最後の値のみ返す
   - `request.data.getlist('tags')` でリスト取得が必要
   - テストでは配列として送信したデータが文字列で返されることを想定
   
   **対策例**:
   ```python
   # View側の修正
   tags = request.data.getlist('tags') if 'tags' in request.data else []
   
   # テスト側では文字列レスポンスも考慮
   self.assertEqual(response.data['tags'], 'tag3')  # 最後の要素のみ
   # または配列で期待する場合は View 側修正後にテスト
   ```

2. **JSONファイル読み込みのモック設定**
   - `mock_open(read_data='{}')` は空JSONで json.load() エラーの原因
   - 適切な初期データで設定: `mock_open(read_data='{"key": "value"}')`
   - アーカイブ処理では trash-registry.json の適切なモック必須

3. **ファイルシステム操作のモック**
   - `pathlib.Path.exists()` のモック設定
   - `os.walk()` で動的パス処理が必要
   - `shutil.rmtree()`, `zipfile.ZipFile` の適切なモック
   
   **動的パスモック例**:
   ```python
   def mock_walk_side_effect(path):
       from config.paths import PROJECT_DATA_DIR
       if str(PROJECT_DATA_DIR) in str(path):
           return [(str(path), [], ['file1.txt'])]
       return []
   
   mock_walk.side_effect = mock_walk_side_effect
   ```

### フロントエンド (React/TypeScript)
- `@testing-library/react` の使用
- ユーザーインタラクション重視のテスト
- アクセシビリティを考慮したクエリ使用
- 非同期処理の適切な待機

## 5. プロジェクト固有のルール
### ファイルタグ機能
- タグバリデーションルールの確認
  - 分析データ → 時系列データ/項目データ (階層関係)
  - 参考資料 (独立)
- `file_tags.json` 形式での永続化テスト
- プロジェクトフォルダ構造の確認

### API仕様
- 多言語対応レスポンス
- エラーメッセージの国際化
- CORS設定の確認
- セキュリティ考慮事項

## 6. テストデータ管理
### 使用可能なテスト用プロジェクト
- `test_project`
- `minimal_test`
- `debug_test_project`

### プロジェクトフォルダ保護の徹底
**重要**: テスト前後でprojectフォルダの内容が変わらないことを保証する

#### 保護対象
- `project/` ディレクトリ全体
- 既存プロジェクトの `project.json`
- 既存プロジェクトの `file_tags.json`
- 既存プロジェクトの raw データファイル
- `projects-registry.json`

#### 保護手段
1. **テストデータの分離**
   - テスト専用の一時ディレクトリ使用
   - 既存プロジェクトフォルダへの直接操作禁止
   - テスト用プロジェクト名の使用（例: `test_project_12345`）

2. **バックアップ・復元システム**
   ```python
   # テスト前: バックアップ作成
   def setUp(self):
       super().setUp()
       self.backup_manager = ProjectBackupManager()
       self.backup_manager.create_backup()
   
   # テスト後: 復元実行
   def tearDown(self):
       self.backup_manager.restore_backup()
       super().tearDown()
   ```

3. **モックによる代替**
   - ファイルシステム操作のモック化
   - `pathlib.Path.exists()` のモック
   - `json.load()`, `json.dump()` のモック
   - API呼び出しの完全モック化
   
   **重要**: JSONファイルモック設定
   ```python
   # ❌ 間違い: 空JSONは json.load() エラーの原因
   @patch('builtins.open', new_callable=mock_open)
   
   # ✅ 正しい: 適切な初期データを設定
   @patch('builtins.open', new_callable=lambda: mock_open(
       read_data='{"version": "1.0.0", "deleted_projects": []}'
   ))
   ```

4. **テスト用ミックスイン活用**
   ```python
   from test_utils.project_backup import DjangoTestCaseMixin
   
   class MyTestCase(DjangoTestCaseMixin, APITestCase):
       # 自動的にバックアップ・復元が実行される
   ```

5. **基底テストクラスの活用**
   - `MockedFileSystemTestCase` を継承してモック設定を簡素化
   - 共通のモックパターンを基底クラスで提供
   
   ```python
   from .test_base import MockedFileSystemTestCase
   
   class MyTestCase(MockedFileSystemTestCase):
       def test_example(self):
           # ファイルシステム関連のモックは自動設定済み
           with patch('zipfile.ZipFile') as mock_zip:
               # 追加のモックのみ設定
               pass
   ```

5. **一時ディレクトリの使用**
   ```python
   import tempfile
   import shutil
   
   def setUp(self):
       self.temp_dir = tempfile.mkdtemp()
       # テストデータを一時ディレクトリに配置
   
   def tearDown(self):
       shutil.rmtree(self.temp_dir)
   ```

6. **読み取り専用テスト**
   - 既存データの参照のみ
   - 変更を伴う操作は完全モック
   - アサーションは戻り値のみで実行

#### 検証方法
- テスト実行前後でのファイルハッシュ比較
- ディレクトリ構造の変更検出
- プロジェクト数の一致確認
- レジストリファイルの整合性確認

### 避けるべき事項
- 本番データの使用
- 既存プロジェクトフォルダへの直接書き込み
- ハードコードされた絶対パス
- タイムゾーン依存の日時比較
- 並行実行時の競合状態
- バックアップなしでの破壊的操作

### よくあるテストエラーとその対策
1. **404エラー（エンドポイント不存在）**
   - URL パターンの確認: `urls.py` で定義されているか
   - ViewSet のアクション名とURLの一致確認
   - `detail=True/False` の設定確認
   
   **デバッグ方法**:
   ```python
   # URLconf確認
   python manage.py show_urls | grep project
   
   # テストでURL確認
   print(f"Testing URL: {url}")
   print(f"Available URLs: {self.client.get('/api/').data}")
   ```

2. **500エラー（内部サーバーエラー）**
   - JSON読み込み失敗: mock_open の read_data 確認
   - AttributeError: モックが設定されていないメソッド呼び出し
   - ImportError: 設定されていないモジュールパス
   
   **対策**:
   ```python
   # 詳細エラー情報を取得
   print(f"Response status: {response.status_code}")
   print(f"Response data: {response.data}")
   if hasattr(response, 'content'):
       print(f"Response content: {response.content}")
   ```

3. **レスポンス形式エラー**
   - タグ配列 → 文字列: QueryDict.getlist() 使用必須
   - 日時形式: timezone aware datetime の使用
   - ID重複: uuid生成の適切なモック
   
   **修正例**:
   ```python
   # View側でQueryDict処理
   def create(self, request, *args, **kwargs):
       data = request.data.copy()
       if 'tags' in data:
           data['tags'] = request.data.getlist('tags')
       
   # テスト側で配列/文字列両方に対応
   tags = response.data.get('tags', [])
   if isinstance(tags, str):
       tags = [tags]  # 文字列の場合は配列に変換
   self.assertIn('expected_tag', tags)
   ```

## 7. 実行環境への配慮
### CI/CD対応
- 環境変数への依存最小化
- ファイルシステム操作の冪等性
- 並行実行時の安全性確保

### 開発環境
- ローカル開発での実行可能性
- 必要な依存関係の明示
- 設定ファイルでの調整可能性

## 8. メンテナンス性
### 更新しやすさ
- 設定変更時の影響範囲最小化
- 新機能追加時のテスト拡張容易性
- リファクタリング時の安全性確保

### ドキュメント
- テストケースの目的明記
- 複雑なロジックの説明追加
- 前提条件や制約事項の記載

## 9. テストの優先度と修正戦略

### 修正の優先順位
1. **高優先度**: 500エラー（サーバー内部エラー）
   - システム動作に影響する致命的エラー
   - JSON読み込み失敗、モック設定不備
   
2. **中優先度**: レスポンス形式エラー
   - 機能は動作するが期待値と異なる
   - QueryDict配列処理、日時形式
   
3. **低優先度**: 404エラー（当該機能未実装）
   - 将来実装予定の機能
   - URL設定の確認と修正

### 効率的な修正アプローチ
1. **基底クラス修正**: 共通問題の一括解決
2. **View修正**: QueryDict処理の根本対策
3. **個別テスト修正**: 特殊ケースの対応

## 10. パフォーマンス考慮
- 不要な重複テスト回避
- 効率的なモック使用
- テスト実行時間の最適化
- リソース使用量の適正化

## 11. セキュリティ考慮
- 機密情報のハードコード禁止
- テスト用認証情報の分離
- 権限テストの実装
- 入力検証の徹底確認

## 12. **必須**: フロントエンド・バックエンドAPI整合性テスト

### 実施タイミング
**全てのテスト実施時に必ず以下のAPI整合性テストを実行する**
- 新機能追加時
- API仕様変更時
- バグ修正時
- 定期的なテスト実行時

### テスト対象範囲
1. **エンドポイント網羅性テスト**
   - バックエンドに定義された全エンドポイントがフロントエンドで実装済みか
   - フロントエンドで使用している全エンドポイントがバックエンドに存在するか
   - doc/APIja.mdの実装状況との整合性確認

2. **リクエスト・レスポンス型整合性テスト**
   - フロントエンドの型定義（TypeScript interface）とバックエンドのシリアライザーの一致
   - 必須フィールド、オプションフィールドの整合性
   - データ型（string, number, boolean, array, object）の一致
   - 日時形式、配列処理の統一性

3. **HTTPメソッド・ステータスコード整合性テスト**
   - 各エンドポイントのHTTPメソッド（GET, POST, PUT, DELETE）の一致
   - 成功時・エラー時のステータスコードの統一
   - エラーレスポンス形式の統一

4. **API バージョニング整合性テスト**
   - フロントエンドがcurrent APIバージョン（/api/v1/）を使用しているか
   - 後方互換性の確認
   - 環境変数設定の整合性

### 必須実装ファイル
```bash
# バックエンド
api/tests_api_contract.py        # APIコントラクトテスト
api/tests_frontend_integration.py  # フロントエンド統合テスト

# フロントエンド  
src/tests/api-client.test.ts     # APIクライアントテスト
src/tests/api-integration.test.ts # バックエンド統合テスト

# 共通
tests/api_schema_validation.py   # APIスキーマ検証
tests/endpoint_coverage.test.js  # エンドポイント網羅性テスト
```

### テスト実装必須項目

#### 1. エンドポイント発見テスト
```python
def test_all_backend_endpoints_have_frontend_client():
    """バックエンドの全エンドポイントにフロントエンドクライアントが存在することを確認"""
    backend_urls = extract_all_api_urls()  # URLconfから全エンドポイント取得
    frontend_clients = extract_frontend_api_calls()  # フロントエンドから取得
    
    missing_in_frontend = set(backend_urls) - set(frontend_clients)
    assert len(missing_in_frontend) == 0, f"フロントエンドに未実装: {missing_in_frontend}"

def test_all_frontend_calls_have_backend_endpoint():
    """フロントエンドの全API呼び出しにバックエンドエンドポイントが存在することを確認"""
    # 逆方向の確認
```

#### 2. 型整合性テスト
```typescript
// フロントエンド側
describe('API Type Consistency', () => {
  test('project API response matches TypeScript interface', async () => {
    const response = await projectAPI.getAll();
    // レスポンス構造の検証
    expect(response).toMatchSchema(ProjectRegistrySchema);
    expect(response.projects[0]).toMatchSchema(ProjectSchema);
  });
});
```

```python
# バックエンド側
def test_serializer_matches_frontend_types():
    """シリアライザーの出力がフロントエンドの型定義と一致することを確認"""
    serializer = ProjectSerializer(instance=sample_project)
    data = serializer.data
    
    # TypeScriptインターフェースとの比較
    assert_matches_typescript_interface(data, "Project")
```

#### 3. 実際の通信テスト
```python
def test_frontend_backend_communication():
    """実際のHTTP通信でフロントエンドとバックエンドの整合性を確認"""
    # 実際のHTTPリクエストを送信
    response = requests.get(f"{BACKEND_URL}/api/v1/projects/")
    
    # フロントエンドの期待する形式と一致するか
    data = response.json()
    assert validate_frontend_expected_format(data)
```

#### 4. 環境設定整合性テスト
```python
def test_api_base_url_consistency():
    """フロントエンドとバックエンドのAPI URL設定の整合性確認"""
    # .env.local の NEXT_PUBLIC_API_BASE_URL
    # api-client.ts の API_BASE_URL デフォルト値
    # バックエンドの CORS設定
    # の整合性を確認
```

### テスト実行スクリプト
```bash
#!/bin/bash
# tests/run_api_integration_tests.sh

echo "=== API整合性テスト実行開始 ==="

# バックエンドテスト
echo "1. バックエンドAPIテスト実行..."
cd app/backend && python manage.py test api.tests_api_contract

# フロントエンドテスト  
echo "2. フロントエンドAPIテスト実行..."
cd app/frontend && npm test -- api-integration.test.ts

# 結合テスト
echo "3. API結合テスト実行..."
python tests/api_integration_suite.py

echo "=== API整合性テスト完了 ==="
```

### テスト失敗時の対応手順
1. **型不整合**: シリアライザーまたはTypeScriptインターフェースを修正
2. **エンドポイント不足**: 未実装側にエンドポイント追加
3. **HTTPメソッド不一致**: 適切なメソッドに統一
4. **URL設定エラー**: 環境変数・デフォルト値を修正

### レポート生成
```python
# テスト結果をdoc/history/api_integration_YYYYMMDD.mdに出力
def generate_api_integration_report():
    """API整合性テストの結果レポートを生成"""
    report = {
        'test_date': datetime.now(),
        'endpoint_coverage': calculate_coverage(),
        'type_mismatches': find_type_mismatches(),
        'missing_implementations': find_missing_implementations(),
        'recommendations': generate_recommendations()
    }
    save_report_to_markdown(report)
```

### doc/APIja.md連携
- テスト結果を基にAPIja.mdの「フロントエンド」「テスト結果」列を自動更新
- 整合性チェック結果を実装状況表に反映
- 不整合箇所は❌マークと対応必要として記録