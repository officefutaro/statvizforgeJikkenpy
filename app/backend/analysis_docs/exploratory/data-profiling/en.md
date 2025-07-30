# Data Profiling Detailed Guide

## 📋 Overview

Data profiling is a fundamental exploratory analysis technique that systematically investigates and evaluates the **basic statistical information**, **quality**, and **structure** of datasets. It is executed as the first step in data analysis projects to understand the overall picture of data and determine appropriate analysis strategies.

### Importance
- Early detection of data quality issues improves analysis accuracy
- Guidance for selecting appropriate preprocessing methods
- Reduction of analysis effort and improved efficiency
- Clear status reporting to stakeholders

## 🎯 Use Cases

### Application Scenarios
- **New dataset acquisition**: Overall understanding of first-time data
- **Pre-data integration**: Quality verification of multiple data sources
- **Periodic quality monitoring**: Health checks of data pipelines
- **Analysis planning**: Pre-evaluation of analysis feasibility

### Recommendation by Data Type
- **Structured data (CSV, Excel)**: ★★★★★ Essential
- **Time series data**: ★★★★☆ Highly recommended
- **Categorical data**: ★★★★☆ Highly recommended
- **Text data**: ★★★☆☆ Basic statistics only
- **Image/Audio data**: ★★☆☆☆ Metadata only

## 🔧 Implementation Steps

### 1. Data Loading and Basic Information Check

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load data
df = pd.read_csv('your_dataset.csv')

# Check basic information
print("=" * 50)
print("Dataset Basic Information")
print("=" * 50)
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Data size: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"Data types: {df.dtypes.value_counts().to_dict()}")
```

### 2. Data Quality Assessment

```python
def analyze_data_quality(df):
    """Comprehensive data quality evaluation"""
    quality_report = {}
    
    for column in df.columns:
        col_data = df[column]
        
        # Basic statistics
        quality_report[column] = {
            'dtype': str(col_data.dtype),
            'non_null_count': col_data.count(),
            'null_count': col_data.isnull().sum(),
            'null_percentage': (col_data.isnull().sum() / len(df)) * 100,
            'unique_count': col_data.nunique(),
            'duplicate_count': col_data.duplicated().sum(),
        }
        
        # Additional statistics for numeric types
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
    """Outlier detection using IQR method"""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return len(outliers)

# Execute
quality_report = analyze_data_quality(df)
```

### 3. Statistical Summary Generation

```python
def generate_statistical_summary(df):
    """Generate statistical summary"""
    summary = {
        'numerical_summary': df.describe(),
        'categorical_summary': df.describe(include=['object']),
        'correlation_matrix': df.corr(),
        'missing_data_pattern': df.isnull().sum().sort_values(ascending=False)
    }
    
    return summary

# Execution example
summary = generate_statistical_summary(df)
print("Statistical summary of numerical variables:")
print(summary['numerical_summary'])
```

### 4. Visualization-based Exploration

```python
def create_data_profile_plots(df, output_dir='./plots/'):
    """Create visualizations for data profiling"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Missing value pattern visualization
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=True, yticklabels=False, cmap='viridis')
    plt.title('Missing Value Pattern')
    plt.savefig(f'{output_dir}/missing_pattern.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. Distribution of numerical variables
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        fig, axes = plt.subplots(nrows=(len(numeric_cols)+2)//3, ncols=3, 
                                figsize=(15, 5*((len(numeric_cols)+2)//3)))
        axes = axes.flatten() if len(numeric_cols) > 1 else [axes]
        
        for i, col in enumerate(numeric_cols):
            if i < len(axes):
                sns.histplot(df[col].dropna(), kde=True, ax=axes[i])
                axes[i].set_title(f'Distribution of {col}')
        
        plt.tight_layout()
        plt.savefig(f'{output_dir}/numeric_distributions.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    # 3. Distribution of categorical variables
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        for col in categorical_cols[:5]:  # Show only first 5
            plt.figure(figsize=(10, 6))
            value_counts = df[col].value_counts().head(10)
            sns.barplot(x=value_counts.values, y=value_counts.index)
            plt.title(f'Value Distribution of {col} (Top 10)')
            plt.xlabel('Count')
            plt.savefig(f'{output_dir}/categorical_{col}.png', dpi=300, bbox_inches='tight')
            plt.show()

# Execute
create_data_profile_plots(df)
```

### 5. Report Generation

```python
def generate_data_profile_report(df, quality_report, output_file='data_profile_report.md'):
    """Generate Markdown report"""
    
    report_content = f"""# Data Profiling Report

## Dataset Overview
- **File name**: {df.name if hasattr(df, 'name') else 'Unknown'}
- **Rows**: {len(df):,}
- **Columns**: {len(df.columns)}
- **Memory usage**: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB
- **Analysis date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}

## Data Quality Summary

### Missing Values Status
"""
    
    # Add missing value information
    missing_summary = df.isnull().sum()
    missing_columns = missing_summary[missing_summary > 0]
    
    if len(missing_columns) > 0:
        report_content += "| Column | Missing Count | Missing Rate |\n|--------|---------------|---------------|\n"
        for col, missing_count in missing_columns.items():
            missing_rate = (missing_count / len(df)) * 100
            report_content += f"| {col} | {missing_count:,} | {missing_rate:.2f}% |\n"
    else:
        report_content += "✅ **No missing values** - All columns have complete data.\n"
    
    # Numerical variables summary
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        report_content += f"\n### Numerical Variables Summary ({len(numeric_cols)} columns)\n\n"
        report_content += "| Column | Mean | Median | Std Dev | Min | Max | Outliers |\n"
        report_content += "|--------|------|--------|---------|-----|-----|----------|\n"
        
        for col in numeric_cols:
            col_data = df[col]
            outliers = detect_outliers_iqr(col_data)
            report_content += f"| {col} | {col_data.mean():.2f} | {col_data.median():.2f} | {col_data.std():.2f} | {col_data.min():.2f} | {col_data.max():.2f} | {outliers} |\n"
    
    # File output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"Report saved to {output_file}")
    return report_content

# Execute
report = generate_data_profile_report(df, quality_report)
```

## 📊 Result Interpretation

### Reading Important Indicators

#### 1. Data Quality Indicators
- **Missing rate**: Ideal <10%, caution >20%
- **Duplicate rate**: Generally <5%, verify for business data
- **Outliers**: <3% is normal range with IQR method

#### 2. Distribution Characteristics
- **Skewness**:
  - -0.5 to 0.5: Close to normal distribution
  - |0.5| to |1.0|: Moderate skewness
  - |1.0|+: Strong skewness (consider log transformation)

- **Kurtosis**:
  - Around 3: Normal distribution
  - >3: Peaked distribution
  - <3: Flat distribution

#### 3. Correlations
- **|r| > 0.7**: Strong correlation (watch for multicollinearity)
- **0.3 < |r| < 0.7**: Moderate correlation
- **|r| < 0.3**: Weak correlation

### Precautions and Limitations
- Processing time may be long for large data (>1M rows)
- Pay attention to memory usage with many categorical variables
- Time axis consideration needed for time series data
- Understanding missing value meaning (structural vs random missing) is important

### Best Practices
1. **Stepwise approach**: Overall → detailed analysis
2. **Domain knowledge utilization**: Combine business understanding with statistical analysis
3. **Visualization emphasis**: Check with charts, not just numbers
4. **Documentation**: Record and share findings
5. **Iterative improvement**: Deepen understanding while progressing analysis

## 📈 Usage Examples

### Real Estate Data Example
```python
# Example of profiling Ichikawa apartment rent data
rent_df = pd.read_csv('ichikawa_apartment_rent.csv')

# Key analysis points
print("Rent data characteristics:")
print(f"Average rent: {rent_df['rent'].mean():.0f} yen")
print(f"Rent standard deviation: {rent_df['rent'].std():.0f} yen")
print(f"Correlation between age and rent: {rent_df['age'].corr(rent_df['rent']):.3f}")

# Rent distribution by location
location_stats = rent_df.groupby('location')['rent'].agg(['mean', 'median', 'count'])
print("\nRent statistics by location:")
print(location_stats.sort_values('mean', ascending=False))
```

## 🔗 Related Links

### Internal Related Documents
- [Initial Exploration](../initial-exploration/en.md): More detailed exploration methods
- [Correlation Analysis](../../statistical/correlation-analysis/en.md): Analysis of relationships between variables
- [Visualization Guide](../../visualization/chart-selection/en.md): Selecting appropriate charts

### External References
- [pandas Official Documentation](https://pandas.pydata.org/docs/)
- [seaborn Statistical Visualization](https://seaborn.pydata.org/)
- [scipy Statistical Functions](https://docs.scipy.org/doc/scipy/reference/stats.html)

### Recommended Tools
- **Jupyter Notebook**: Interactive analysis
- **pandas-profiling**: Automated profiling
- **Great Expectations**: Data quality monitoring
- **Apache Superset**: Dashboard creation

---

**Created**: January 30, 2025  
**Last Updated**: January 30, 2025  
**Author**: Claude Code  
**Reviewer**: StatVizForge Data Analysis Team