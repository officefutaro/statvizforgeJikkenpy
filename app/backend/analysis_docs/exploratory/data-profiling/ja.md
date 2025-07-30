# データプロファイリング 詳細ガイド

## 📋 概要

データプロファイリングは、データセットの**基本統計情報**、**品質**、**構造**を体系的に調査・評価する探索的分析の基礎手法です。データ分析プロジェクトの最初のステップとして、データの全体像を理解し、適切な分析戦略を決定するために実行されます。

### 重要性
- データ品質の早期発見により、分析精度向上
- 適切な前処理手法の選択指針
- 分析工数の削減と効率化
- ステークホルダーへの分かりやすい現状報告

## 🎯 使用場面

### 適用シナリオ
- **新規データセット取得時**: 初めて扱うデータの全体把握
- **データ統合前**: 複数データソースの品質確認
- **定期的な品質監視**: データパイプラインの健全性チェック
- **分析企画時**: 分析可能性の事前評価

### データタイプ別推奨度
- **構造化データ (CSV, Excel)**: ★★★★★ 必須
- **時系列データ**: ★★★★☆ 高推奨
- **カテゴリデータ**: ★★★★☆ 高推奨
- **テキストデータ**: ★★★☆☆ 基本統計のみ
- **画像・音声データ**: ★★☆☆☆ メタデータのみ

## 🔧 実装手順

### 1. データ読み込みと基本情報確認

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# データ読み込み
df = pd.read_csv('your_dataset.csv')

# 基本情報の確認
print("=" * 50)
print("データセット基本情報")
print("=" * 50)
print(f"行数: {len(df):,}")
print(f"列数: {len(df.columns)}")
print(f"データサイズ: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"データ型: {df.dtypes.value_counts().to_dict()}")
```

### 2. データ品質評価

```python
def analyze_data_quality(df):
    """データ品質の包括的評価"""
    quality_report = {}
    
    for column in df.columns:
        col_data = df[column]
        
        # 基本統計
        quality_report[column] = {
            'dtype': str(col_data.dtype),
            'non_null_count': col_data.count(),
            'null_count': col_data.isnull().sum(),
            'null_percentage': (col_data.isnull().sum() / len(df)) * 100,
            'unique_count': col_data.nunique(),
            'duplicate_count': col_data.duplicated().sum(),
        }
        
        # 数値型の場合の追加統計
        if pd.api.types.is_numeric_dtype(col_data):
            quality_report[column].update({
                'mean': col_data.mean(),
                'median': col_data.median(),
                'std': col_data.std(),
                'min': col_data.min(),
                'max': col_data.max(),
                'q25': col_data.quantile(0.25),
                'q75': col_data.quantile(0.75),
                'outliers_iqr': detect_outliers_iqr(col_data),
                'skewness': stats.skew(col_data.dropna()),
                'kurtosis': stats.kurtosis(col_data.dropna())
            })
    
    return quality_report

def detect_outliers_iqr(data):
    """IQR法による外れ値検出"""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return len(outliers)

# 実行
quality_report = analyze_data_quality(df)
```

### 3. 統計的要約の生成

```python
def generate_statistical_summary(df):
    """統計的要約の生成"""
    summary = {
        'numerical_summary': df.describe(),
        'categorical_summary': df.describe(include=['object']),
        'correlation_matrix': df.corr(),
        'missing_data_pattern': df.isnull().sum().sort_values(ascending=False)
    }
    
    return summary

# 実行例
summary = generate_statistical_summary(df)
print("数値変数の統計的要約:")
print(summary['numerical_summary'])
```

### 4. 可視化による探索

```python
def create_data_profile_plots(df, output_dir='./plots/'):
    """データプロファイル用の可視化作成"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. 欠損値パターンの可視化
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
    plt.title('欠損値パターン')
    plt.savefig(f'{output_dir}/missing_pattern.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. 数値変数の分布
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        fig, axes = plt.subplots(nrows=(len(numeric_cols)+2)//3, ncols=3, 
                                figsize=(15, 5*((len(numeric_cols)+2)//3)))
        axes = axes.flatten() if len(numeric_cols) > 1 else [axes]
        
        for i, col in enumerate(numeric_cols):
            if i < len(axes):
                sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
                axes[i].set_title(f'{col} の分布')
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/numeric_distributions.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    # 3. カテゴリ変数の分布
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        for col in categorical_cols[:5]:  # 最初の5つのみ表示
            plt.figure(figsize=(10, 6))
            value_counts = df[col].value_counts().head(10)
            sns.barplot(x=value_counts.values, y=value_counts.index)
            plt.title(f'{col} の値分布（上位10位）')
            plt.xlabel('出現回数')
            plt.savefig(f'{output_dir}/categorical_{col}.png', dpi=300, bbox_inches='tight')
            plt.show()

# 実行
create_data_profile_plots(df)
```

### 5. レポート生成

```python
def generate_data_profile_report(df, quality_report, output_file='data_profile_report.md'):
    """Markdownレポートの生成"""
    
    report_content = f"""# データプロファイリングレポート

## データセット概要
- **ファイル名**: {df.name if hasattr(df, 'name') else 'Unknown'}
- **行数**: {len(df):,}
- **列数**: {len(df.columns)}
- **メモリ使用量**: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB
- **分析日時**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

## データ品質サマリー

### 欠損値の状況
"""
    
    # 欠損値情報の追加
    missing_summary = df.isnull().sum()
    missing_columns = missing_summary[missing_summary > 0]
    
    if len(missing_columns) > 0:
        report_content += "| 列名 | 欠損数 | 欠損率 |\n|------|--------|--------|\n"
        for col, missing_count in missing_columns.items():
            missing_rate = (missing_count / len(df)) * 100
            report_content += f"| {col} | {missing_count:,} | {missing_rate:.2f}% |\n"
    else:
        report_content += "✅ **欠損値なし** - 全ての列でデータが完全です。\n"
    
    # 数値変数のサマリー
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        report_content += f"\n### 数値変数サマリー ({len(numeric_cols)}列)\n\n"
        report_content += "| 列名 | 平均 | 中央値 | 標準偏差 | 最小値 | 最大値 | 外れ値 |\n"
        report_content += "|------|------|--------|----------|--------|--------|---------|\n"
        
        for col in numeric_cols:
            col_data = df[col]
            outliers = detect_outliers_iqr(col_data)
            report_content += f"| {col} | {col_data.mean():.2f} | {col_data.median():.2f} | {col_data.std():.2f} | {col_data.min():.2f} | {col_data.max():.2f} | {outliers} |\n"
    
    # ファイル出力
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"レポートを {output_file} に保存しました。")
    return report_content

# 実行
report = generate_data_profile_report(df, quality_report)
```

## 📊 結果の解釈

### 重要な指標の読み方

#### 1. データ品質指標
- **欠損率**: 10%以下が理想、20%以上は要注意
- **重複率**: 5%以下が一般的、業務データでは要確認
- **外れ値**: IQR法で3%以下が通常範囲

#### 2.分布特性
- **歪度 (Skewness)**:
  - -0.5 ～ 0.5: 正規分布に近い
  - |0.5| ～ |1.0|: 軽度の歪み
  - |1.0| 以上: 強い歪み（対数変換等を検討）

- **尖度 (Kurtosis)**:
  - 3付近: 正規分布
  - 3より大きい: 尖った分布
  - 3より小さい: 平坦な分布

#### 3. 相関関係
- **|r| > 0.7**: 強い相関（多重共線性に注意）
- **0.3 < |r| < 0.7**: 中程度の相関
- **|r| < 0.3**: 弱い相関

### 注意点・制限事項
- 大規模データ（>100万行）では処理時間が長くなる可能性
- カテゴリ変数の種類が多い場合、メモリ使用量に注意
- 時系列データでは時間軸の考慮が必要
- 欠損値の意味（構造的欠損 vs ランダム欠損）の理解が重要

### ベストプラクティス
1. **段階的アプローチ**: 全体 → 詳細の順で分析
2. **ドメイン知識の活用**: 業務理解と統計分析の組み合わせ
3. **可視化重視**: 数値だけでなく図表での確認
4. **文書化**: 発見事項の記録と共有
5. **反復的改善**: 分析を進めながら理解を深化

## 📈 活用例

### 不動産データの例
```python
# 市川市アパート家賃データのプロファイリング例
rent_df = pd.read_csv('ichikawa_apartment_rent.csv')

# 特徴的な分析ポイント
print("家賃データの特徴:")
print(f"平均家賃: {rent_df['rent'].mean():.0f}円")
print(f"家賃の標準偏差: {rent_df['rent'].std():.0f}円")
print(f"築年数と家賃の相関: {rent_df['age'].corr(rent_df['rent']):.3f}")

# 地域別の家賃分布
location_stats = rent_df.groupby('location')['rent'].agg(['mean', 'median', 'count'])
print("\n地域別家賃統計:")
print(location_stats.sort_values('mean', ascending=False))
```

## 🔗 関連リンク

### 内部関連ドキュメント
- [初期探索](../initial-exploration/ja.md): より詳細な探索手法
- [相関分析](../../statistical/correlation-analysis/ja.md): 変数間関係の分析
- [可視化ガイド](../../visualization/chart-selection/ja.md): 適切なグラフの選択

### 外部参考資料
- [pandas公式ドキュメント](https://pandas.pydata.org/docs/)
- [seaborn統計可視化](https://seaborn.pydata.org/)
- [scipy統計関数](https://docs.scipy.org/doc/scipy/reference/stats.html)

### 推奨ツール
- **Jupyter Notebook**: インタラクティブ分析
- **pandas-profiling**: 自動プロファイリング
- **Great Expectations**: データ品質監視
- **Apache Superset**: ダッシュボード作成

---

**作成日**: 2025年1月30日  
**最終更新**: 2025年1月30日  
**作成者**: Claude Code  
**レビュー者**: StatVizForge データ分析チーム