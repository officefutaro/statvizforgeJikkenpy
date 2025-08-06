# Git機能 包括的テスト計画

## 🚨 **発見された重要な問題**

### **問題1: Git初期化の深刻な設計エラー**
- **現象**: `git init`実行時にプロジェクト全体のGitリポジトリが初期化される
- **原因**: プロジェクト固有のgitフォルダではなく、全体StatVizForgeプロジェクトが初期化対象となっている
- **影響**: 全開発環境のGit状態が混乱する危険性

### **問題2: Git パス設定の不適切性**  
- **現象**: `/project/Yachin/git/` でgit statusを実行すると、`../../../` パスが大量表示
- **原因**: Git作業ディレクトリが適切に分離されていない
- **影響**: プロジェクト間のファイル混合、意図しないコミット

## 📋 **包括的Git機能テスト計画**

### **Phase 1: 緊急修正テスト**
#### **1.1 Git分離修正テスト**
```bash
# テスト項目
✅ Git初期化対象パスの確認
✅ プロジェクト固有のgitフォルダ分離
✅ 全体プロジェクトへの影響確認
✅ バックアップとロールバック機能

# 期待結果
- プロジェクト固有のGitリポジトリが作成される
- 他プロジェクト・全体環境への影響なし
```

#### **1.2 Git初期化API修正テスト**
```python
# テスト対象: GitSyncUtils.initialize_git_folder()
# 修正内容: 正しいcwd設定、git init実行パス
def test_git_init_isolation():
    # 1. プロジェクトフォルダ内でのみgit init実行
    # 2. 他フォルダへの影響なし確認
    # 3. Git設定がプロジェクト固有である確認
```

### **Phase 2: 基本Git機能テスト**
#### **2.1 Git同期機能テスト**
```bash
# Test Suite: GitSyncUtilsテスト
test_sync_analysisdata_to_git/     ✅ analysisdata → git フォルダ同期
test_sync_raw_to_git/             ✅ raw → git フォルダ同期  
test_sync_status_detection/       ✅ 同期必要ファイル検出
test_sync_incremental_update/     ✅ 増分同期機能
test_sync_large_files/           ✅ 大容量ファイル同期
test_sync_permission_handling/    ✅ ファイル権限処理
```

#### **2.2 Git基本操作テスト**
```bash  
# Test Suite: GitUtilsテスト
test_git_init_fresh_project/      ✅ 新規プロジェクトGit初期化
test_git_add_files/              ✅ ファイル追加
test_git_commit_basic/           ✅ 基本コミット
test_git_commit_with_author/     ✅ 作者情報付きコミット
test_git_status_check/           ✅ ステータス確認
test_git_log_retrieval/          ✅ 履歴取得
test_git_diff_generation/        ✅ 差分生成
```

### **Phase 3: API統合テスト**
#### **3.1 GitSync API テスト**
```python
# Endpoint Tests: /api/v1/git-sync/
GET    /status/{project}/         ✅ 同期状態取得
POST   /init/{project}/          ✅ Git初期化
POST   /sync/{project}/          ✅ 同期実行
POST   /commit/{project}/        ✅ コミット実行
GET    /diff/{project}/          ✅ 差分確認  
GET    /log/{project}/           ✅ 履歴取得
GET    /info/{project}/          ✅ Git情報取得
```

#### **3.2 多言語API対応テスト**
```python
# Language Parameter Tests
test_api_japanese_responses/      ✅ ?lang=ja
test_api_english_responses/       ✅ ?lang=en  
test_api_chinese_cn_responses/    ✅ ?lang=zh-cn
test_api_chinese_tw_responses/    ✅ ?lang=zh-tw
test_api_language_fallback/       ✅ 不正言語パラメータ処理
```

### **Phase 4: フロントエンド統合テスト**
#### **4.1 GitCommitButtonテスト**
```typescript
# Component Tests
test_git_button_display/          ✅ ボタン表示状態
test_git_init_workflow/          ✅ 初期化フロー
test_commit_modal_functionality/  ✅ コミットモーダル
test_diff_check_display/         ✅ 差分確認表示
test_history_view/               ✅ 履歴表示
test_language_switching/         ✅ 言語切り替え
test_error_handling_display/     ✅ エラー表示
```

#### **4.2 ワークスペース統合テスト**
```typescript  
# Integration Tests
test_workspace_git_integration/   ✅ ワークスペース内Git操作
test_project_switching_git_state/ ✅ プロジェクト切り替え時状態保持
test_realtime_status_updates/    ✅ リアルタイム状態更新
test_concurrent_git_operations/  ✅ 同時Git操作制御
```

### **Phase 5: パフォーマンス・ストレステスト**
#### **5.1 大容量データテスト**
```python
# Performance Tests  
test_large_file_sync_performance/     # 100MB+ ファイル同期
test_many_files_sync_performance/     # 1000+ ファイル同期
test_git_operations_timeout/          # タイムアウト制御
test_concurrent_users_git_ops/        # 同時ユーザーGit操作
test_memory_usage_monitoring/         # メモリ使用量監視
```

#### **5.2 エラー復旧テスト**
```python  
# Error Recovery Tests
test_git_corruption_recovery/         # Gitリポジトリ破損復旧
test_network_failure_handling/       # ネットワーク障害対応
test_disk_full_scenario/             # ディスク容量不足対応
test_permission_denied_recovery/     # 権限エラー復旧
test_partial_sync_recovery/          # 部分同期失敗復旧
```

### **Phase 6: セキュリティテスト** 
#### **6.1 アクセス制御テスト**
```python
# Security Tests
test_project_isolation/              # プロジェクト間分離
test_path_traversal_prevention/     # パストラバーサル防止
test_git_command_injection/         # コマンドインジェクション防止
test_file_permission_validation/    # ファイル権限検証
test_git_author_validation/         # Git作者情報検証
```

### **Phase 7: 運用監視テスト**
#### **7.1 ログ・監視テスト** 
```python
# Monitoring Tests
test_git_operation_logging/          # Git操作ログ記録
test_error_notification_system/     # エラー通知システム
test_performance_metrics_collection/ # パフォーマンス指標収集
test_audit_trail_generation/        # 監査証跡生成
test_storage_usage_monitoring/      # ストレージ使用量監視
```

## 🛠 **修正優先順位**

### **最高優先度 (即座対応)**
1. **Git初期化パス修正** - プロジェクト固有Git分離
2. **API安全性確保** - 既存環境への影響防止
3. **基本機能動作確認** - コアGit機能検証

### **高優先度 (今週中)**  
4. **エラーハンドリング強化** - 堅牢性向上
5. **多言語UI完全対応** - 4言語サポート検証
6. **フロントエンド統合完成** - ワークスペース統合

### **中優先度 (来週)**
7. **パフォーマンス最適化** - 大容量データ対応
8. **セキュリティ検証** - アクセス制御確認
9. **運用監視機能** - ログ・メトリクス

## 📊 **テスト実行環境**

### **テスト環境構成**
```bash
# 1. ローカル開発環境テスト
OS: WSL2 Ubuntu
Git: 2.43.0
Python: 3.12  
Django: Latest
Node.js: Latest

# 2. CI/CD自動テスト
GitHub Actions
テストデータセット準備
自動回帰テスト

# 3. 本番類似環境テスト  
Docker環境
複数ユーザー同時アクセス
リアルデータボリューム
```

### **テスト実行手順**
```bash
# 1. 緊急修正後の基本動作確認
./run_git_basic_tests.sh

# 2. 段階的機能テスト実行
./run_git_integration_tests.sh --phase=1-7

# 3. 全機能包括テスト
./run_git_comprehensive_test.sh --full

# 4. 本番デプロイ前最終確認
./run_git_production_readiness.sh
```

## ✅ **成功基準**

### **機能面**
- [ ] Git初期化が完全にプロジェクト固有で実行される
- [ ] 全API機能が4言語で正常動作する  
- [ ] フロントエンドUI全操作が正常動作する
- [ ] エラー状況でも安全に復旧する

### **性能面**  
- [ ] 100MB+ファイル同期が5秒以内完了
- [ ] 1000+ファイル同期が30秒以内完了
- [ ] 同時5ユーザーでの操作が正常動作

### **運用面**
- [ ] 全操作が適切にログ記録される
- [ ] エラー発生時に自動通知される
- [ ] 運用監視ダッシュボードが正常表示

---

**この包括的テスト計画により、Git機能の安全で堅牢な実装を保証します。**