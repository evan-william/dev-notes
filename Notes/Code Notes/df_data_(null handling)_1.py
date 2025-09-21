import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: NULL HANDLING (DETECTION, FILLING, INTERPOLATION, DROPPING, FILTERING)
"""

# ----------------------------------#
# 1. Load Data
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("1. Coffee Data (head):\n", coffee.head())

# ----------------------------------#
# 2. Setting Values to Null
coffee.loc[[0,1], 'Units Sold'] = np.nan
print("\n2. Set index [0,1] 'Units Sold' to NaN:\n", coffee.head())

# ----------------------------------#
# 3. Checking Nulls with .info()
print("\n3. Null Info with .info():")
coffee.info()

# ----------------------------------#
# 4. Checking Null Counts with .isna()
print("\n4. Null Counts per Column with isna().sum():\n", coffee.isna().sum())

# ----------------------------------#
# 5. Fill NaN with a Constant Value
coffee_filled_const = coffee.fillna("LOL")
print("\n5. Fill all NaN values with 'LOL':\n", coffee_filled_const.head())

# ----------------------------------#
# 6. Fill NaN with Column Mean
coffee_filled_mean = coffee.fillna(coffee['Units Sold'].mean())
print("\n6. Fill NaN in 'Units Sold' with column mean:\n", coffee_filled_mean.head())

"""
💡 Note:
- fillna(value) → replaces missing values with a constant (string, number, etc.)
- fillna(coffee['Units Sold'].mean()) → replaces NaN in the column with its mean.
- You can also use .median(), .mode(), or a specific number.
"""

# ----------------------------------#
# 7. Interpolating Missing Values
# Reset 'Units Sold' first
coffee.loc[[0,1], 'Units Sold'] = 25
# Set new NaNs at index [2,3]
coffee.loc[[2,3], 'Units Sold'] = np.nan

print("\n7. Before Interpolation:\n", coffee)

coffee['Units Sold'] = coffee['Units Sold'].interpolate()
print("\nAfter Interpolation (linear by default):\n", coffee)

"""
💡 Interpolation:
- Estimates missing values by "looking at the trend".
- Default is linear: fills missing with evenly spaced values between known points.
- More advanced methods: method='time', 'spline', 'polynomial'.
"""

# ----------------------------------#
# 8. Dropping Rows with NaN
# Reset NaN for testing
coffee.loc[[2,3],'Units Sold'] = np.nan

print("\n8. Before dropna():\n", coffee)
coffee_dropped = coffee.dropna()
print("\nAfter dropna() (rows with any NaN removed):\n", coffee_dropped)

"""
💡 dropna() options:
- By default → removes rows with *any* NaN.
- dropna(axis=1) → removes entire columns with NaN.
- dropna(how='all') → drops rows/columns only if *all* values are NaN.
- dropna(subset=['Units Sold']) → only considers NaN in specific columns.
"""

# ----------------------------------#
# 9. Dropping Rows with NaN in Specific Columns (subset)
coffee_subset = coffee.dropna(subset=['Units Sold'])
print("\n9. Drop rows only if 'Units Sold' is NaN:\n", coffee_subset)

"""
💡 dropna(subset=['col']):
- Focuses only on specific important columns.
- Example: In sales data, 'Units Sold' is critical, but you may tolerate NaN in other columns.
- Unlike plain dropna(), it won’t drop rows just because 'Price' or 'Coffee Type' is missing.
"""

# ----------------------------------#
# 10. Filtering Rows with isna() / notna()
print("\n10. Filtering Missing Values with isna() and notna():")

missing_units = coffee[coffee['Units Sold'].isna()]
print("\n→ All rows where 'Units Sold' IS NaN:\n", missing_units)

not_missing_units = coffee[coffee['Units Sold'].notna()]
print("\n→ All rows where 'Units Sold' is NOT NaN:\n", not_missing_units)

"""
💡 isna() / notna():
- isna() → True where value is missing (NaN).
- notna() → True where value is present.
- Very useful for filtering DataFrames directly instead of just counting.
"""

# ----------------------------------#
# 11. Summary of Null Handling
print("\n11. Final Coffee DataFrame (after operations):\n", coffee.head())

"""
Summary:
- info(), isna(), notna() → detect missing values.
- fillna() → replace with constant, mean, median, mode, etc.
- interpolate() → smart filling based on trends.
- dropna() → remove rows or columns with missing values.
- dropna(subset=[...]) → enforce non-missing only for critical columns.
- isna()/notna() filtering → directly extract rows with/without missing values.
"""

# ----------------------------------#
# 12. Advanced: Finding the Column of the First / N-th NaN in Each Row
df = pd.DataFrame({
    "A": [1, np.nan, np.nan, 4],
    "B": [np.nan, np.nan, 3, np.nan],
    "C": [np.nan, 2, np.nan, np.nan],
    "D": [np.nan, np.nan, np.nan, 5]
})

print("\n12. Advanced Example DataFrame:\n", df)

# Boolean mask of NaNs
mask = df.isna()
print("\nBoolean mask (True = NaN):\n", mask)

# First NaN per row using idxmax
first_nan_col = mask.idxmax(axis=1)
print("\nColumn label of the first NaN per row:\n", first_nan_col)

# Third NaN per row (slightly trickier)
third_nan_col = mask.cumsum(axis=1).eq(3).idxmax(axis=1)
print("\nColumn label of the third NaN per row:\n", third_nan_col)

"""
💡 Notes on idxmax(axis=1):
- idxmax(axis=1) → returns the column label of the *first True* in each row.
- With a NaN mask, this means: "first column where NaN appears".
- If you want the N-th NaN, you can use cumsum() to count Trues across columns:
    mask.cumsum(axis=1).eq(N).idxmax(axis=1)
- Example:
    N=1 → first NaN
    N=3 → third NaN
- Super useful when you need column *labels* instead of just positions.
"""
