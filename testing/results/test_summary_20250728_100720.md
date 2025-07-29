# ❌ テスト実行結果サマリー

## 📊 総合結果: FAILED

**実行日時**: 2025-07-28T10:07:20.294Z  
**日付**: 20250728

## 🧪 テスト結果詳細

### Jest テスト (単体・統合テスト)
- **結果**: ❌ 失敗
- **総テスト数**: N/A
- **成功**: 0
- **失敗**: 0
- **保留**: 0

### E2E テスト (Playwright)
- **結果**: ❌ 失敗

### バックエンドテスト (Django)
- **結果**: ❌ 失敗

## 📈 カバレッジ情報
❌ カバレッジ情報なし

## 🔍 失敗したテスト
### Jest テスト失敗
### E2E テスト失敗
- エラー: Command failed: npm run test:e2e -- --reporter=json
### バックエンドテスト失敗
- エラー: Command failed: cd ../backend && source venv/bin/activate && python3 manage.py test --verbosity=2
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
test_concurrent_tag_operations (api.test_file_tags.FileTagsAPITestCase.test_concurrent_tag_operations)
並行タグ操作テスト ... FAIL
test_file_tags_persistence (api.test_file_tags.FileTagsAPITestCase.test_file_tags_persistence)
ファイルタグ永続化テスト ... FAIL
test_get_all_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_get_all_file_tags_success)
全ファイルタグ取得成功テスト ... FAIL
test_get_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_get_file_tags_success)
ファイルタグ取得成功テスト ... FAIL
test_project_not_found_error (api.test_file_tags.FileTagsAPITestCase.test_project_not_found_error)
存在しないプロジェクトでのエラーテスト ... ok
test_save_file_tags_invalid_combination (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_invalid_combination)
無効なタグ組み合わせテスト（項目データのみ） ... FAIL
test_save_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_success)
ファイルタグ保存成功テスト ... FAIL
test_save_file_tags_validation_error (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_validation_error)
ファイルタグ保存バリデーションエラーテスト ... FAIL
test_search_files_by_multiple_tags (api.test_file_tags.FileTagsAPITestCase.test_search_files_by_multiple_tags)
複数タグによる検索テスト ... ERROR
test_search_files_by_tags_success (api.test_file_tags.FileTagsAPITestCase.test_search_files_by_tags_success)
タグによるファイル検索成功テスト ... ERROR
test_tag_api_error_handling (api.test_file_tags.FileTagsAPITestCase.test_tag_api_error_handling)
タグAPIエラーハンドリングテスト ... FAIL
test_tag_api_response_format (api.test_file_tags.FileTagsAPITestCase.test_tag_api_response_format)
タグAPIレスポンス形式テスト ... FAIL
test_tag_validation_rules (api.test_file_tags.FileTagsAPITestCase.test_tag_validation_rules)
タグバリデーションルールテスト ... FAIL
test_get_jupyter_status_no_instances (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_no_instances)
JupyterLabインスタンスなしの状態確認テスト ... ERROR
test_get_jupyter_status_running (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_running)
JupyterLab状態確認（起動中）テスト ... ERROR
test_get_jupyter_status_specific_project (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_specific_project)
特定プロジェクトのJupyterLab状態確認テスト ... ERROR
test_jupyter_api_error_responses (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_error_responses)
JupyterLab API エラーレスポンス形式テスト ... ok
test_jupyter_api_performance (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_performance)
JupyterLab API パフォーマンステスト ... ERROR
test_jupyter_api_resource_management (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_resource_management)
JupyterLab API リソース管理テスト ... FAIL
test_jupyter_api_security (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_security)
JupyterLab API セキュリティテスト ... FAIL
test_jupyter_service_separation (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_service_separation)
JupyterLabサービス分離テスト ... ERROR
test_start_jupyter_lab_already_running (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_already_running)
既に起動中のJupyterLabに対する処理テスト ... FAIL
test_start_jupyter_lab_missing_project_folder (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_missing_project_folder)
プロジェクトフォルダ未指定エラーテスト ... ok
test_start_jupyter_lab_project_not_found (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_project_not_found)
存在しないプロジェクトでのエラーテスト ... ok
test_start_jupyter_lab_startup_failure (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_startup_failure)
JupyterLab起動失敗テスト ... FAIL
test_start_jupyter_lab_success (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_success)
JupyterLab起動成功テスト ... FAIL
test_stop_jupyter_lab_not_running (api.test_jupyter_api.JupyterLabAPITestCase.test_stop_jupyter_lab_not_running)
起動していないJupyterLabの停止テスト ... ERROR
test_stop_jupyter_lab_success (api.test_jupyter_api.JupyterLabAPITestCase.test_stop_jupyter_lab_success)
JupyterLab停止成功テスト ... ERROR
test_full_workflow_integration (api.tests.APIIntegrationTestCase.test_full_workflow_integration)
完全ワークフロー統合テスト：プロジェクト作成→ファイル操作→コメント→検索 ... ERROR
test_add_file_comment (api.tests.FileCommentsTestCase.test_add_file_comment)
ファイルコメント追加テスト ... FAIL
test_add_file_comment (api.tests.FileCommentsTestCase.test_add_file_comment)
ファイルコメント追加テスト ... ERROR
test_comment_api_validation (api.tests.FileCommentsTestCase.test_comment_api_validation)
コメントAPI バリデーションテスト ... FAIL
test_comment_api_validation (api.tests.FileCommentsTestCase.test_comment_api_validation)
コメントAPI バリデーションテスト ... ERROR
test_delete_file_comment (api.tests.FileCommentsTestCase.test_delete_file_comment)
ファイルコメント削除テスト ... FAIL
test_delete_file_comment (api.tests.FileCommentsTestCase.test_delete_file_comment)
ファイルコメント削除テスト ... ERROR
test_get_file_comments (api.tests.FileCommentsTestCase.test_get_file_comments)
ファイルコメント取得テスト ... FAIL
test_get_file_comments (api.tests.FileCommentsTestCase.test_get_file_comments)
ファイルコメント取得テスト ... ERROR
test_update_file_comment (api.tests.FileCommentsTestCase.test_update_file_comment)
ファイルコメント更新テスト ... FAIL
test_update_file_comment (api.tests.FileCommentsTestCase.test_update_file_comment)
ファイルコメント更新テスト ... ERROR
test_directory_creation (api.tests.FileManagementTestCase.test_directory_creation)
ディレクトリ作成テスト ... FAIL
test_directory_creation (api.tests.FileManagementTestCase.test_directory_creation)
ディレクトリ作成テスト ... ERROR
test_directory_tree_retrieval (api.tests.FileManagementTestCase.test_directory_tree_retrieval)
ディレクトリツリー取得テスト ... FAIL
test_directory_tree_retrieval (api.tests.FileManagementTestCase.test_directory_tree_retrieval)
ディレクトリツリー取得テスト ... ERROR
test_file_api_error_handling (api.tests.FileManagementTestCase.test_file_api_error_handling)
ファイルAPI エラーハンドリングテスト ... FAIL
test_file_api_error_handling (api.tests.FileManagementTestCase.test_file_api_error_handling)
ファイルAPI エラーハンドリングテスト ... ERROR
test_file_deletion (api.tests.FileManagementTestCase.test_file_deletion)
ファイル削除テスト ... FAIL
test_file_deletion (api.tests.FileManagementTestCase.test_file_deletion)
ファイル削除テスト ... ERROR
test_file_move (api.tests.FileManagementTestCase.test_file_move)
ファイル移動テスト ... FAIL
test_file_move (api.tests.FileManagementTestCase.test_file_move)
ファイル移動テスト ... ERROR
test_file_search (api.tests.FileManagementTestCase.test_file_search)
ファイル検索テスト ... FAIL
test_file_search (api.tests.FileManagementTestCase.test_file_search)
ファイル検索テスト ... ERROR
test_multiple_file_upload (api.tests.FileManagementTestCase.test_multiple_file_upload)
複数ファイルアップロードテスト ... FAIL
test_multiple_file_upload (api.tests.FileManagementTestCase.test_multiple_file_upload)
複数ファイルアップロードテスト ... ERROR
test_single_file_upload (api.tests.FileManagementTestCase.test_single_file_upload)
単一ファイルアップロードテスト ... FAIL
test_single_file_upload (api.tests.FileManagementTestCase.test_single_file_upload)
単一ファイルアップロードテスト ... ERROR
test_api_response_time (api.tests.ProjectAPIPerformanceTestCase.test_api_response_time)
API応答時間テスト ... ok
test_プロジェクトライフサイクル_エラー混在 (api.tests.ProjectIntegrationTestCase.test_プロジェクトライフサイクル_エラー混在)
正常操作とエラー操作が混在するライフサイクル ... ERROR
test_同時削除復元操作 (api.tests.ProjectIntegrationTestCase.test_同時削除復元操作)
複数プロジェクトの同時削除・復元操作 ... ERROR
test_complete_project_lifecycle (api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle)
プロジェクト完全ライフサイクルテスト: 作成→更新→削除→復元 ... ERROR
test_error_handling_scenarios (api.tests.ProjectLifecycleTestCase.test_error_handling_scenarios)
エラーハンドリングシナリオテスト ... ERROR
test_language_parameter_handling (api.tests.ProjectLifecycleTestCase.test_language_parameter_handling)
言語パラメータ処理テスト（エラーメッセージのみ） ... ERROR
test_multiple_projects_interaction (api.tests.ProjectLifecycleTestCase.test_multiple_projects_interaction)
複数プロジェクトの相互作用テスト ... ERROR
test_タグ配列バリデーション_0__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_0__)
様々なタグ配列のバリデーション [with test_name='空のタグ配列', tags=[]] ... ERROR
test_タグ配列バリデーション_1__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_1__)
様々なタグ配列のバリデーション [with test_name='単一タグ', tags=['tag1']] ... ERROR
test_タグ配列バリデーション_2__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_2__)
様々なタグ配列のバリデーション [with test_name='複数タグ', tags=['tag1', 'tag2', 'tag3']] ... ERROR
test_タグ配列バリデーション_3__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_3__)
様々なタグ配列のバリデーション [with test_name='日本語タグ', tags=['日本語', 'テスト', 'サンプル']] ... ERROR
test_タグ配列バリデーション_4__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_4__)
様々なタグ配列のバリデーション [with test_name='英数字タグ', tags=['test', 'sample', 'demo123']] ... ERROR
test_プロジェクト名バリデーション (api.tests.ProjectValidationTestCase.test_プロジェクト名バリデーション)
プロジェクト名の長さと文字種バリデーション ... ERROR
test_重複フォルダ名チェック (api.tests.ProjectValidationTestCase.test_重複フォルダ名チェック)
フォルダ名の重複チェック ... ERROR

======================================================================
ERROR: test_search_files_by_multiple_tags (api.test_file_tags.FileTagsAPITestCase.test_search_files_by_multiple_tags)
複数タグによる検索テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 161, in test_search_files_by_multiple_tags
    with patch('api.views.FileViewSet.search_by_tags') as mock_search:
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <class 'api.views.FileViewSet'> does not have the attribute 'search_by_tags'

======================================================================
ERROR: test_search_files_by_tags_success (api.test_file_tags.FileTagsAPITestCase.test_search_files_by_tags_success)
タグによるファイル検索成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 135, in test_search_files_by_tags_success
    with patch('api.views.FileViewSet.search_by_tags') as mock_search:
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <class 'api.views.FileViewSet'> does not have the attribute 'search_by_tags'

======================================================================
ERROR: test_get_jupyter_status_no_instances (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_no_instances)
JupyterLabインスタンスなしの状態確認テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'get_jupyter_status'

======================================================================
ERROR: test_get_jupyter_status_running (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_running)
JupyterLab状態確認（起動中）テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'get_jupyter_status'

======================================================================
ERROR: test_get_jupyter_status_specific_project (api.test_jupyter_api.JupyterLabAPITestCase.test_get_jupyter_status_specific_project)
特定プロジェクトのJupyterLab状態確認テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'get_jupyter_status'

======================================================================
ERROR: test_jupyter_api_performance (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_performance)
JupyterLab API パフォーマンステスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'get_jupyter_status'

======================================================================
ERROR: test_jupyter_service_separation (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_service_separation)
JupyterLabサービス分離テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'jupyter_service'

======================================================================
ERROR: test_stop_jupyter_lab_not_running (api.test_jupyter_api.JupyterLabAPITestCase.test_stop_jupyter_lab_not_running)
起動していないJupyterLabの停止テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'stop_jupyter_lab'

======================================================================
ERROR: test_stop_jupyter_lab_success (api.test_jupyter_api.JupyterLabAPITestCase.test_stop_jupyter_lab_success)
JupyterLab停止成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1387, in patched
    with self.decoration_helper(patched,
  File "/usr/lib/python3.12/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1369, in decoration_helper
    arg = exit_stack.enter_context(patching)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 526, in enter_context
    result = _enter(cm)
             ^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.views' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/views.py'> does not have the attribute 'stop_jupyter_lab'

======================================================================
ERROR: test_full_workflow_integration (api.tests.APIIntegrationTestCase.test_full_workflow_integration)
完全ワークフロー統合テスト：プロジェクト作成→ファイル操作→コメント→検索
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_add_file_comment (api.tests.FileCommentsTestCase.test_add_file_comment)
ファイルコメント追加テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileCommentsTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_comment_api_validation (api.tests.FileCommentsTestCase.test_comment_api_validation)
コメントAPI バリデーションテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileCommentsTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_delete_file_comment (api.tests.FileCommentsTestCase.test_delete_file_comment)
ファイルコメント削除テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileCommentsTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_get_file_comments (api.tests.FileCommentsTestCase.test_get_file_comments)
ファイルコメント取得テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileCommentsTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_update_file_comment (api.tests.FileCommentsTestCase.test_update_file_comment)
ファイルコメント更新テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileCommentsTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_directory_creation (api.tests.FileManagementTestCase.test_directory_creation)
ディレクトリ作成テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_directory_tree_retrieval (api.tests.FileManagementTestCase.test_directory_tree_retrieval)
ディレクトリツリー取得テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_file_api_error_handling (api.tests.FileManagementTestCase.test_file_api_error_handling)
ファイルAPI エラーハンドリングテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_file_deletion (api.tests.FileManagementTestCase.test_file_deletion)
ファイル削除テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_file_move (api.tests.FileManagementTestCase.test_file_move)
ファイル移動テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_file_search (api.tests.FileManagementTestCase.test_file_search)
ファイル検索テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_multiple_file_upload (api.tests.FileManagementTestCase.test_multiple_file_upload)
複数ファイルアップロードテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_single_file_upload (api.tests.FileManagementTestCase.test_single_file_upload)
単一ファイルアップロードテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 96, in tearDown
    for patcher in self.patchers:
                   ^^^^^^^^^^^^^
AttributeError: 'FileManagementTestCase' object has no attribute 'patchers'

======================================================================
ERROR: test_プロジェクトライフサイクル_エラー混在 (api.tests.ProjectIntegrationTestCase.test_プロジェクトライフサイクル_エラー混在)
正常操作とエラー操作が混在するライフサイクル
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_同時削除復元操作 (api.tests.ProjectIntegrationTestCase.test_同時削除復元操作)
複数プロジェクトの同時削除・復元操作
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_complete_project_lifecycle (api.tests.ProjectLifecycleTestCase.test_complete_project_lifecycle)
プロジェクト完全ライフサイクルテスト: 作成→更新→削除→復元
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 22, in setUp
    super().setUp()
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_error_handling_scenarios (api.tests.ProjectLifecycleTestCase.test_error_handling_scenarios)
エラーハンドリングシナリオテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 22, in setUp
    super().setUp()
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_language_parameter_handling (api.tests.ProjectLifecycleTestCase.test_language_parameter_handling)
言語パラメータ処理テスト（エラーメッセージのみ）
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 22, in setUp
    super().setUp()
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_multiple_projects_interaction (api.tests.ProjectLifecycleTestCase.test_multiple_projects_interaction)
複数プロジェクトの相互作用テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 22, in setUp
    super().setUp()
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_タグ配列バリデーション_0__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_0__)
様々なタグ配列のバリデーション [with test_name='空のタグ配列', tags=[]]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_タグ配列バリデーション_1__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_1__)
様々なタグ配列のバリデーション [with test_name='単一タグ', tags=['tag1']]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_タグ配列バリデーション_2__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_2__)
様々なタグ配列のバリデーション [with test_name='複数タグ', tags=['tag1', 'tag2', 'tag3']]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_タグ配列バリデーション_3__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_3__)
様々なタグ配列のバリデーション [with test_name='日本語タグ', tags=['日本語', 'テスト', 'サンプル']]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_タグ配列バリデーション_4__ (api.tests.ProjectValidationTestCase.test_タグ配列バリデーション_4__)
様々なタグ配列のバリデーション [with test_name='英数字タグ', tags=['test', 'sample', 'demo123']]
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_プロジェクト名バリデーション (api.tests.ProjectValidationTestCase.test_プロジェクト名バリデーション)
プロジェクト名の長さと文字種バリデーション
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
ERROR: test_重複フォルダ名チェック (api.tests.ProjectValidationTestCase.test_重複フォルダ名チェック)
フォルダ名の重複チェック
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_base.py", line 47, in setUp
    self.mock_load_trash = load_trash_patcher.start()
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1606, in start
    result = self.__enter__()
             ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1458, in __enter__
    original, local = self.get_original()
                      ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/unittest/mock.py", line 1431, in get_original
    raise AttributeError(
AttributeError: <module 'api.utils' from '/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/utils.py'> does not have the attribute 'load_trash_registry'

======================================================================
FAIL: test_concurrent_tag_operations (api.test_file_tags.FileTagsAPITestCase.test_concurrent_tag_operations)
並行タグ操作テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 269, in test_concurrent_tag_operations
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_file_tags_persistence (api.test_file_tags.FileTagsAPITestCase.test_file_tags_persistence)
ファイルタグ永続化テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 231, in test_file_tags_persistence
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_get_all_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_get_all_file_tags_success)
全ファイルタグ取得成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 127, in test_get_all_file_tags_success
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_get_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_get_file_tags_success)
ファイルタグ取得成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 114, in test_get_file_tags_success
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_save_file_tags_invalid_combination (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_invalid_combination)
無効なタグ組み合わせテスト（項目データのみ）
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 99, in test_save_file_tags_invalid_combination
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
AssertionError: 404 != 400

======================================================================
FAIL: test_save_file_tags_success (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_success)
ファイルタグ保存成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 68, in test_save_file_tags_success
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_save_file_tags_validation_error (api.test_file_tags.FileTagsAPITestCase.test_save_file_tags_validation_error)
ファイルタグ保存バリデーションエラーテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 83, in test_save_file_tags_validation_error
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
AssertionError: 404 != 400

======================================================================
FAIL: test_tag_api_error_handling (api.test_file_tags.FileTagsAPITestCase.test_tag_api_error_handling)
タグAPIエラーハンドリングテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 285, in test_tag_api_error_handling
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
AssertionError: 404 != 500

======================================================================
FAIL: test_tag_api_response_format (api.test_file_tags.FileTagsAPITestCase.test_tag_api_response_format)
タグAPIレスポンス形式テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 306, in test_tag_api_response_format
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_tag_validation_rules (api.test_file_tags.FileTagsAPITestCase.test_tag_validation_rules)
タグバリデーションルールテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_file_tags.py", line 200, in test_tag_validation_rules
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_jupyter_api_resource_management (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_resource_management)
JupyterLab API リソース管理テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_jupyter_api.py", line 244, in test_jupyter_api_resource_management
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_jupyter_api_security (api.test_jupyter_api.JupyterLabAPITestCase.test_jupyter_api_security)
JupyterLab API セキュリティテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_jupyter_api.py", line 220, in test_jupyter_api_security
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_start_jupyter_lab_already_running (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_already_running)
既に起動中のJupyterLabに対する処理テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_jupyter_api.py", line 101, in test_start_jupyter_lab_already_running
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_start_jupyter_lab_startup_failure (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_startup_failure)
JupyterLab起動失敗テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_jupyter_api.py", line 188, in test_start_jupyter_lab_startup_failure
    self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
AssertionError: 404 != 500

======================================================================
FAIL: test_start_jupyter_lab_success (api.test_jupyter_api.JupyterLabAPITestCase.test_start_jupyter_lab_success)
JupyterLab起動成功テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/test_jupyter_api.py", line 56, in test_start_jupyter_lab_success
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_add_file_comment (api.tests.FileCommentsTestCase.test_add_file_comment)
ファイルコメント追加テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 797, in test_add_file_comment
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
AssertionError: 404 != 201

======================================================================
FAIL: test_comment_api_validation (api.tests.FileCommentsTestCase.test_comment_api_validation)
コメントAPI バリデーションテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 856, in test_comment_api_validation
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
AssertionError: 404 != 400

======================================================================
FAIL: test_delete_file_comment (api.tests.FileCommentsTestCase.test_delete_file_comment)
ファイルコメント削除テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 842, in test_delete_file_comment
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_get_file_comments (api.tests.FileCommentsTestCase.test_get_file_comments)
ファイルコメント取得テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 766, in test_get_file_comments
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_update_file_comment (api.tests.FileCommentsTestCase.test_update_file_comment)
ファイルコメント更新テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 826, in test_update_file_comment
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_directory_creation (api.tests.FileManagementTestCase.test_directory_creation)
ディレクトリ作成テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 707, in test_directory_creation
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_directory_tree_retrieval (api.tests.FileManagementTestCase.test_directory_tree_retrieval)
ディレクトリツリー取得テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 501, in test_directory_tree_retrieval
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_file_api_error_handling (api.tests.FileManagementTestCase.test_file_api_error_handling)
ファイルAPI エラーハンドリングテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 725, in test_file_api_error_handling
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
AssertionError: 404 != 400

======================================================================
FAIL: test_file_deletion (api.tests.FileManagementTestCase.test_file_deletion)
ファイル削除テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 660, in test_file_deletion
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_file_move (api.tests.FileManagementTestCase.test_file_move)
ファイル移動テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 683, in test_file_move
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_file_search (api.tests.FileManagementTestCase.test_file_search)
ファイル検索テスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 634, in test_file_search
    self.assertEqual(response.status_code, status.HTTP_200_OK)
AssertionError: 404 != 200

======================================================================
FAIL: test_multiple_file_upload (api.tests.FileManagementTestCase.test_multiple_file_upload)
複数ファイルアップロードテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 586, in test_multiple_file_upload
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
AssertionError: 404 != 201

======================================================================
FAIL: test_single_file_upload (api.tests.FileManagementTestCase.test_single_file_upload)
単一ファイルアップロードテスト
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/mock.py", line 1390, in patched
    return func(*newargs, **newkeywargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/futaro/project/StatVizForge_JikkenPy/app/backend/api/tests.py", line 540, in test_single_file_upload
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
AssertionError: 404 != 201

----------------------------------------------------------------------
Ran 56 tests in 0.062s

FAILED (failures=28, errors=36)
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...


## 📋 次のアクション
🚨 失敗したテストがあります。詳細ログを確認して修正してください。

## 📁 関連ファイル
- 詳細結果: `test_results_20250728_100720.json`
- カバレッジレポート: `coverage/lcov-report/index.html`

---
*このレポートは自動生成されました - 2025-07-28T10:07:22.247Z*
