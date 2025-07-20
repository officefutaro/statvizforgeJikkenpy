# Backend環境セットアップガイド

## 前提条件
まず、python3-venvパッケージをインストールしてください：
```bash
sudo apt update
sudo apt install python3.12-venv
```

## セットアップ手順

### 方法1: setup_venv.shスクリプトを使用
```bash
./setup_venv.sh
```

### 方法2: 手動セットアップ
1. 仮想環境の作成：
   ```bash
   python3 -m venv venv
   ```

2. 仮想環境の有効化：
   ```bash
   source venv/bin/activate
   ```

3. 依存関係のインストール：
   ```bash
   pip install -r requirements.txt
   ```

## 仮想環境の使用方法

### 有効化
```bash
source venv/bin/activate
```

### 無効化
```bash
deactivate
```