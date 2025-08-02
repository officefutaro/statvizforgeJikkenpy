# ClaudeCode起動と異常時の対応

## 1. 自動起動機能

### VSCodeでプロジェクトを開いた時の動作
- プロジェクトフォルダを開くと、自動でtmuxセッション内でClaudeCodeが起動します
- 下部のターミナルパネルに新しいタブが作成され、ClaudeCodeが実行されます
- tmuxセッション名: `claude-code`

### UI変化
- VSCode下部にターミナルパネルが自動で開く
- 新しいターミナルタブが作成される
- ターミナル内でClaudeCodeのプロンプトが表示される
- tmuxステータスバーがターミナル下部に表示される場合がある

## 2. 手動起動・接続方法

### 方法1: VSCodeタスクを使用
1. `Ctrl+Shift+P`でコマンドパレットを開く
2. "Tasks: Run Task"を選択
3. "Attach to Claude Code tmux session"を選択
4. 既存セッションに接続される

### 方法2: ターミナルコマンド
```bash
# 新しいセッションを作成してClaudeCodeを起動
tmux new-session -d -s claude-code 'claude-code'

# 既存セッションに接続
tmux attach-session -t claude-code
```

### 方法3: 通常起動
```bash
# tmux保護なしで起動（Ctrl+Z脆弱性あり）
claude-code
```

## 3. Ctrl+Z問題の対応

### 問題
- 通常のターミナルでClaudeCodeを実行中にCtrl+Zを押すとプロセスが一時停止する
- 復帰するには`fg`コマンドが必要

### 解決策（tmux使用）
- tmuxセッション内で実行することで、Ctrl+Zを押してもセッションが保護される
- 誤って停止してもセッションが残り、簡単に復帰可能

## 4. 異常時の対応

### Case 1: tmuxセッションが見つからない
```bash
# セッション一覧を確認
tmux list-sessions

# セッションが存在しない場合、新規作成
tmux new-session -d -s claude-code 'claude-code'
```

### Case 2: ClaudeCodeが応答しない
```bash
# セッションを強制終了
tmux kill-session -t claude-code

# 新しいセッションを作成
tmux new-session -d -s claude-code 'claude-code'
```

### Case 3: Ctrl+Zで停止してしまった場合
```bash
# フォアグラウンドに復帰
fg

# または、バックグラウンドプロセス一覧を確認
jobs

# 特定のジョブを復帰
fg %1
```

### Case 4: VSCode自動起動が失敗する場合
1. `.vscode/tasks.json`の設定を確認
2. 手動でタスクを実行する
3. tmuxがインストールされているか確認:
   ```bash
   sudo apt update && sudo apt install tmux
   ```

## 5. セッション管理

### セッション状態確認
```bash
# 全セッション一覧
tmux list-sessions

# セッション内のウィンドウ一覧
tmux list-windows -t claude-code
```

### セッション操作
```bash
# セッションから安全に切断（セッションは残る）
Ctrl+B, d

# セッションを完全終了
tmux kill-session -t claude-code

# 全セッションを終了
tmux kill-server
```

## 6. トラブルシューティング

### tmuxが起動しない
```bash
# tmuxインストール確認
which tmux

# インストール
sudo apt update && sudo apt install tmux
```

### ClaudeCodeが見つからない
```bash
# ClaudeCodeインストール確認
which claude-code

# パス確認
echo $PATH
```

### VSCodeタスクが表示されない
1. `.vscode/tasks.json`ファイルが存在するか確認
2. VSCodeを再起動
3. プロジェクトフォルダで`Ctrl+Shift+P` → "Tasks: Configure Task"

## 7. 設定ファイル

### .vscode/tasks.json
- 自動起動タスクとアタッチタスクが定義されている
- `runOn: "folderOpen"`により自動実行される

### .vscode/settings.json
- ターミナルの基本設定
- bashをデフォルトシェルに設定

## 8. 推奨ワークフロー

1. **日常利用**: VSCodeでプロジェクトを開くだけ（自動起動）
2. **セッション復帰**: `tmux attach-session -t claude-code`
3. **クリーンスタート**: セッション終了後、VSCodeでプロジェクトを再度開く
4. **緊急時**: 手動でtmuxセッションを作成・管理

この設定により、Ctrl+Zによる誤った停止を防ぎ、安定したClaudeCode環境を維持できます。