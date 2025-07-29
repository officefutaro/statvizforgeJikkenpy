# Git運用ガイドライン

## ブランチ戦略

### 基本方針
- `main`ブランチ：安定版のコードのみ
- フィーチャーブランチ：機能開発用
- 作業が完了したらmainに統合
- 統合後の古いブランチは削除

### ブランチ命名規則
- `feature/機能名` - 新機能開発
- `fix/バグ名` - バグ修正
- `work-session/日付-時刻` - 作業セッション

### ワークフロー

#### 1. 新しい作業の開始
```bash
# mainブランチから新しいブランチを作成
git checkout main
git pull origin main
git checkout -b feature/新機能名
```

#### 2. 作業中
```bash
# 定期的にコミット
git add .
git commit -m "意味のあるコミットメッセージ"

# リモートにバックアップ
git push -u origin feature/新機能名
```

#### 3. mainへの統合
```bash
# 最新のmainを取り込む
git checkout main
git pull origin main
git checkout feature/新機能名
git rebase main  # または git merge main

# mainにマージ
git checkout main
git merge feature/新機能名
git push origin main
```

#### 4. ブランチの削除
```bash
# ローカルブランチの削除
git branch -d feature/新機能名

# リモートブランチの削除
git push origin --delete feature/新機能名
```

### 現在の作業ブランチ
- `work-session-20250729-125658` - 現在の作業セッション
  - TableViewer機能
  - プロジェクト編集機能
  - UI/UX改善

### 統合タイミングの目安
- 機能が完成してテストが通った時
- 大きな区切りがついた時
- 他の開発者と共有が必要な時
- リリース準備ができた時