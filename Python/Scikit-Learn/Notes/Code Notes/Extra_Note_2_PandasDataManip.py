"""
=================================================================
PANDAS - Comprehensive Data Manipulation Guide
=================================================================

This file covers essential Pandas operations:
- Missing value handling
- Data filtering and selection
- GroupBy operations
- Pivot tables
- Reading different file formats
"""

import pandas as pd
import numpy as np

# =================================================================
# 1. COUNTING MISSING VALUES
# =================================================================
print("=" * 60)
print("1. COUNTING MISSING VALUES IN DATAFRAME")
print("=" * 60)

# Create sample DataFrame with missing values
df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'David', 'Eve'],
    'age': [25, None, 30, 35, None],
    'salary': [50000, 60000, None, 70000, 65000],
    'department': ['HR', 'IT', 'IT', None, 'HR']
})

print("Sample DataFrame:")
print(df)

# Count missing values per column
print("\nMissing values per column:")
print(df.isna().sum())

# TOTAL missing values in entire DataFrame
total_missing = df.isna().sum().sum()
print(f"\nTotal missing values: {total_missing}")

print("\nExplanation:")
print("df.isna()        → Boolean DataFrame (True where NaN)")
print("df.isna().sum()  → Count NaN per column")
print("df.isna().sum().sum() → Total count across all columns")


# =================================================================
# 2. IMPUTING MISSING VALUES
# =================================================================
print("\n" + "=" * 60)
print("2. IMPUTING (FILLING) MISSING VALUES")
print("=" * 60)

# Create DataFrame with missing values
df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D', 'E'],
    'price': [10.5, None, 15.0, None, 20.0],
    'quantity': [100, 150, None, 200, 250]
})

print("Original DataFrame:")
print(df)

# Fill missing prices with mean
df['price'] = df['price'].fillna(df['price'].mean())
print("\nAfter imputing price with mean:")
print(df)

# Fill missing quantity with median
df['quantity'] = df['quantity'].fillna(df['quantity'].median())
print("\nAfter imputing quantity with median:")
print(df)

# Other imputation strategies
df_example = pd.DataFrame({'values': [1, None, 3, None, 5]})
print("\n--- Other Imputation Methods ---")
print(f"Forward fill: {df_example['values'].fillna(method='ffill').tolist()}")
print(f"Backward fill: {df_example['values'].fillna(method='bfill').tolist()}")
print(f"Fill with 0: {df_example['values'].fillna(0).tolist()}")


# =================================================================
# 3. NOTNA() - NON-MISSING VALUES
# =================================================================
print("\n" + "=" * 60)
print("3. CHECKING FOR NON-MISSING VALUES")
print("=" * 60)

df = pd.DataFrame({
    'A': [1, None, 3],
    'B': [4, 5, None],
    'C': [7, 8, 9]
})

print("DataFrame:")
print(df)

# .notna() returns True for non-missing values
print("\nNon-missing values (Boolean):")
print(df.notna())

# Count non-missing values per column
print("\nCount of non-missing values per column:")
print(df.notna().sum())

# Filter rows with no missing values
complete_rows = df[df.notna().all(axis=1)]
print("\nRows with no missing values:")
print(complete_rows)


# =================================================================
# 4. FILTERING DATAFRAMES
# =================================================================
print("\n" + "=" * 60)
print("4. FILTERING DATAFRAMES (BOOLEAN INDEXING)")
print("=" * 60)

# Create sample employee DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'position': ['Engineer', 'Designer', 'Engineer', 'Designer', 'Manager'],
    'salary': [75000, 65000, 80000, 60000, 90000],
    'experience': [5, 3, 7, 2, 10]
})

print("Original DataFrame:")
print(df)

# Filter: Exclude Designers
filtered_df = df[df['position'] != 'Designer']
print("\nExclude Designers:")
print(filtered_df)

# Multiple conditions (AND)
high_exp_engineers = df[(df['position'] == 'Engineer') & (df['experience'] > 5)]
print("\nEngineers with >5 years experience:")
print(high_exp_engineers)

# Multiple conditions (OR)
high_salary_or_manager = df[(df['salary'] > 70000) | (df['position'] == 'Manager')]
print("\nHigh salary OR Manager:")
print(high_salary_or_manager)


# =================================================================
# 5. READING DELIMITED FILES
# =================================================================
print("\n" + "=" * 60)
print("5. READING DELIMITED TEXT FILES")
print("=" * 60)

# Example of reading different file formats
print("Reading CSV (comma-separated):")
print("pd.read_csv('file.csv')")

print("\nReading pipe-delimited file:")
print("pd.read_csv('file.txt', sep='|')")

print("\nReading tab-delimited file:")
print("pd.read_csv('file.tsv', sep='\\t')")

# Create example pipe-delimited data
pipe_data = """name|age|city
Alice|25|New York
Bob|30|Los Angeles
Charlie|35|Chicago"""

from io import StringIO
df = pd.read_csv(StringIO(pipe_data), sep='|')
print("\nExample pipe-delimited data loaded:")
print(df)


# =================================================================
# 6. ISIN() METHOD - FILTER BY LIST
# =================================================================
print("\n" + "=" * 60)
print("6. FILTERING WITH .ISIN() METHOD")
print("=" * 60)

# Create sales DataFrame
df = pd.DataFrame({
    'store': ['ABC01', 'DEF02', 'GHI03', 'ABC01', 'JKL04', 'GHI03'],
    'product': ['Widget', 'Gadget', 'Widget', 'Gadget', 'Widget', 'Gadget'],
    'sales': [100, 150, 200, 120, 180, 160]
})

print("Sales DataFrame:")
print(df)

# Filter for specific stores
target_stores = ['ABC01', 'GHI03']
filtered = df[df['store'].isin(target_stores)]
print(f"\nFilter for stores {target_stores}:")
print(filtered)

# Inverse - exclude specific stores
excluded = df[~df['store'].isin(target_stores)]
print(f"\nExclude stores {target_stores}:")
print(excluded)


# =================================================================
# 7. GROUPBY AND AGGREGATION
# =================================================================
print("\n" + "=" * 60)
print("7. GROUPBY AND AGGREGATION")
print("=" * 60)

# Create sales data
df = pd.DataFrame({
    'region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'product': ['A', 'A', 'B', 'B', 'A', 'B'],
    'quantity': [10, 15, 20, 25, 30, 35],
    'revenue': [100, 150, 200, 250, 300, 350]
})

print("Sales Data:")
print(df)

# Simple groupby with single aggregation
region_totals = df.groupby('region')['revenue'].sum()
print("\nTotal revenue by region:")
print(region_totals)

# Multiple aggregations with .agg()
region_stats = df.groupby('region').agg({
    'quantity': 'sum',
    'revenue': ['sum', 'mean', 'count']
})
print("\nMultiple aggregations by region:")
print(region_stats)

# Group by multiple columns
product_region = df.groupby(['region', 'product']).agg({
    'quantity': 'sum',
    'revenue': 'sum'
})
print("\nGroup by region AND product:")
print(product_region)


# =================================================================
# 8. DESCRIBE() - STATISTICAL SUMMARY
# =================================================================
print("\n" + "=" * 60)
print("8. STATISTICAL SUMMARY WITH .DESCRIBE()")
print("=" * 60)

df = pd.DataFrame({
    'score_a': [85, 90, 78, 92, 88, 76, 95, 82],
    'score_b': [88, 85, 82, 90, 91, 79, 87, 84],
    'age': [22, 24, 23, 25, 22, 26, 24, 23]
})

print("DataFrame:")
print(df)

# Get statistical summary
summary = df.describe()
print("\nStatistical Summary:")
print(summary)

print("\nThe summary includes:")
print("- count: number of non-null values")
print("- mean: average")
print("- std: standard deviation")
print("- min: minimum value")
print("- 25%: first quartile")
print("- 50%: median (second quartile)")
print("- 75%: third quartile")
print("- max: maximum value")


# =================================================================
# 9. PIVOT TABLES
# =================================================================
print("\n" + "=" * 60)
print("9. CREATING PIVOT TABLES")
print("=" * 60)

# Create sales data
df = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02', '2024-01', '2024-02'],
    'region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'product': ['A', 'A', 'A', 'A', 'B', 'B'],
    'sales': [100, 150, 120, 180, 200, 220]
})

print("Sales Data:")
print(df)

# Create pivot table
pivot = pd.pivot_table(
    df,
    values='sales',
    index='region',  # Rows
    columns='product',  # Columns
    aggfunc='sum',  # Aggregation function
    fill_value=0  # Replace NaN with 0
)
print("\nPivot Table (Sales by Region and Product):")
print(pivot)

# Pivot with multiple aggregations
pivot_multi = pd.pivot_table(
    df,
    values='sales',
    index='region',
    columns='date',
    aggfunc=['sum', 'mean'],
    fill_value=0
)
print("\nPivot with multiple aggregations:")
print(pivot_multi)


# =================================================================
# 10. SELECTING COLUMNS BY DATA TYPE
# =================================================================
print("\n" + "=" * 60)
print("10. SELECTING COLUMNS BY DATA TYPE")
print("=" * 60)

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000.0, 60000.0, 70000.0],
    'department': ['HR', 'IT', 'Finance'],
    'employed': [True, True, False]
})

print("DataFrame:")
print(df)
print("\nData types:")
print(df.dtypes)

# Select only integer columns
int_cols = df.select_dtypes(include=['int'])
print("\nInteger columns:")
print(int_cols)

# Select numeric columns (int and float)
numeric_cols = df.select_dtypes(include=['number'])
print("\nNumeric columns:")
print(numeric_cols)

# Select object (string) columns
string_cols = df.select_dtypes(include=['object'])
print("\nString columns:")
print(string_cols)


# =================================================================
# 11. CHECKING FOR MISSING VALUES
# =================================================================
print("\n" + "=" * 60)
print("11. CHECKING WHICH COLUMNS HAVE MISSING VALUES")
print("=" * 60)

df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [5, 6, 7, 8],
    'C': [None, 10, 11, None],
    'D': [13, 14, 15, 16]
})

print("DataFrame:")
print(df)

# Check which columns have at least one missing value
has_missing = df.isna().any()
print("\nColumns with at least one missing value:")
print(has_missing)

# Get only column names with missing values
cols_with_missing = df.columns[df.isna().any()].tolist()
print(f"\nColumn names with missing values: {cols_with_missing}")

# Count missing values per column (only non-zero)
missing_counts = df.isna().sum()
missing_counts = missing_counts[missing_counts > 0]
print("\nMissing value counts:")
print(missing_counts)


# =================================================================
# SUMMARY
# =================================================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Pandas Operations Covered:

1. Missing Values:
   - df.isna().sum().sum() → total missing
   - df.fillna(value) → impute missing
   - df.notna() → check non-missing

2. Filtering:
   - df[df['col'] != value] → exclude rows
   - df[df['col'].isin([list])] → filter by list
   - df[(cond1) & (cond2)] → multiple conditions

3. Reading Files:
   - pd.read_csv(file, sep='|') → custom delimiter

4. GroupBy:
   - df.groupby('col')['col2'].agg(['sum', 'mean'])
   - df.groupby(['col1', 'col2']) → multiple groups

5. Analysis:
   - df.describe() → statistical summary
   - pd.pivot_table() → reshape data
   - df.select_dtypes() → filter by type
""")