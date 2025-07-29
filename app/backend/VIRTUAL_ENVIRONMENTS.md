# 仮想環境の管理

## 概要
app/backend ディレクトリには、用途別に以下の仮想環境を管理しています。

## 仮想環境の種類

### 1. venv（バックエンド用）
- **用途**: Django アプリケーション実行環境
- **パス**: `app/backend/venv/`
- **起動方法**: `source venv/bin/activate`
- **主要パッケージ**: Django, DRF, その他バックエンド依存関係

### 2. analysis_env（分析用）
- **用途**: データ分析、JupyterLab、その他分析ツール
- **パス**: `app/backend/analysis_env/`
- **起動方法**: `source analysis_env/bin/activate`
- **主要パッケージ**: JupyterLab, pandas, numpy, matplotlib, seaborn, plotly, scipy, scikit-learn

## 使用方法

### バックエンド開発時
```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source venv/bin/activate
python manage.py runserver
```

### データ分析・JupyterLab起動時
```bash
cd /home/futaro/project/StatVizForge_JikkenPy/app/backend
source analysis_env/bin/activate
jupyter lab
```

### 起動時エラー発生時
分析用環境でエラーが発生した場合は、`analysis_env` を使用してください：
```bash
source analysis_env/bin/activate
```

## 将来的な拡張

### 対応予定の分析ツール
- JupyterLab（既に対応済み）
- VS Code Jupyter Extension
- Spyder
- PyCharm Professional
- R Studio（Rpy2経由）
- その他統計・機械学習ツール

### 名称の理由
- `analysis_env`という名称は、JupyterLab に限定されない汎用的な分析環境を意図しています
- 将来的に他の分析ツールを導入する際も、この環境で統一的に管理できます

## 注意事項

1. **環境の分離**: バックエンド用と分析用の環境は完全に分離されています
2. **依存関係の競合防止**: それぞれの用途に特化したパッケージのみをインストール
3. **統一管理**: 分析関連のツールは全て `analysis_env` で管理
4. **エラー対応**: 起動時エラーが発生した場合の標準環境として機能