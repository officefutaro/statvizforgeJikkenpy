# 自動ブランチワークフロー

## 概要
作業中の変更を自動的に管理するため、以下のワークフローを採用します。

## ルール

### 1. 作業開始時
- 自動的に作業用ブランチを作成します
- ブランチ名: `work-session-YYYYMMDD-HHMMSS` 形式
- 例: `work-session-20250729-072213`

### 2. 作業中
- ファイルの変更は通常通り行います
- コミットは行いません（変更は作業ブランチに保持）
- 各作業は完了するまで継続します

### 3. 作業終了時
以下のいずれかを選択：
- **オプション1**: すべての変更を1つのコミットにまとめる
- **オプション2**: 変更を破棄してmainブランチに戻る

### 4. 利点
- 作業履歴が煩雑にならない
- いつでも変更を破棄可能
- 最終的に必要な変更のみをコミット
- mainブランチをクリーンに保つ

## 実行例
```bash
# 作業開始
git checkout -b work-session-$(date +%Y%m%d-%H%M%S)

# 作業終了（変更を保持）
git add .
git commit -m "作業内容の説明"
git checkout main
git merge --squash work-session-YYYYMMDD-HHMMSS
git commit -m "最終的なコミットメッセージ"
git branch -d work-session-YYYYMMDD-HHMMSS

# 作業終了（変更を破棄）
git checkout main
git branch -D work-session-YYYYMMDD-HHMMSS
```