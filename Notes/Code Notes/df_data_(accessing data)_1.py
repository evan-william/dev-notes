import pandas as pd

"""
PANDAS INDEXING & SELECTION
REMEMBER: [ROW, COLUMN]
"""

# =====================================================
# Load Data
# =====================================================
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("Coffee Data (head):")
print(coffee.head())

# =====================================================
# 1. loc[] - Label-based Indexing
# =====================================================

# Single row
print("\n1. loc[0] -> Select row at index 0")
print(coffee.loc[0])  # -> loc[row,column]

# Multiple rows
print("\n2. loc[[0, 2, 3]] -> Select rows 0, 2, 3")
print(coffee.loc[[0, 2, 3]])

# Slice rows (inclusive of end index!)
print("\n3. loc[:3] -> Rows from start to index 3")
print(coffee.loc[:3])

print("\n4. loc[5:] -> Rows from index 5 to end")
print(coffee.loc[5:])

print("\n5. loc[5:8] -> Rows 5 to 8 (inclusive!)")
print(coffee.loc[5:8])

# Slice rows + single column
print("\n6. loc[5:8, 'Day'] -> 'Day' column, rows 5-8")
print(coffee.loc[5:8, "Day"])

# Slice rows + multiple columns
print("\n7. loc[5:8, ['Day', 'Units Sold']] -> 2 columns, rows 5-8")
print(coffee.loc[5:8, ["Day", "Units Sold"]])

# =====================================================
# 2. iloc[] - Integer-location Based Indexing
# =====================================================

# Select specific rows & columns by index number
print("\n8. iloc[:, [0, 2]] -> All rows, only columns 0 & 2")
print(coffee.iloc[:, [0, 2]])

# Slice rows and cols by index numbers
print("\n9. iloc[0:5, 0:2] -> First 5 rows, first 2 cols")
print(coffee.iloc[0:5, 0:2])

# =====================================================
# 3. Index Manipulation
# =====================================================

# View current index
print("\n10. Current index:")
print(coffee.index)

# Set index to a column
coffee.index = coffee["Day"]
print("\n11. Index set to 'Day':")
print(coffee.index)

# Label-based selection with single row
print("\n12. coffee.loc['Monday'] -> Row(s) where Day == 'Monday'")
print(coffee.loc["Monday"])

# Label-based selection with multiple rows (Monday to Wednesday)
print("\n13. coffee.loc['Monday':'Wednesday'] -> Rows Monday to Wednesday")
print(coffee.loc["Monday":"Wednesday"])

# Label-based selection with multiple rows + column
print("\n14. coffee.loc['Monday':'Wednesday', 'Units Sold'] -> Units Sold Monday to Wednesday")
print(coffee.loc["Monday":"Wednesday", "Units Sold"])

# Reset index back to default integers
coffee.reset_index(drop=True, inplace=True)
print("\n15. After reset_index:")
print(coffee.head())

# =====================================================
# 4. Quick Tips
# =====================================================
# coffee['col']           -> Select single column as Series
# coffee[['col1','col2']] -> Select multiple columns as DataFrame
# coffee.iloc[0,0]        -> Single value by position (row 0, col 0)
# coffee.loc[0,'Day']     -> Single value by label (row 0, col 'Day')

# =====================================================
# 5. Changing Data
# =====================================================
# Changing wrong values in DataFrames can be done with .loc/.iloc
# (for multiple values) or .at/.iat (optimized for single values).
# =====================================================

# (A) Change a single wrong value using loc
coffee.loc[1, "Units Sold"] = 10
print("\n16. Change Data with loc -> [1,'Units Sold'] = 10")
print(coffee.head())

# (B) Change multiple wrong values using loc (rows 1-3, column Units Sold)
coffee.loc[1:3, "Units Sold"] = 10
print("\n17. Change Data with loc -> [1:3,'Units Sold'] = 10")
print(coffee.head())

# (C) More optimized way -> .at for single value
# .at is faster than .loc when updating ONE cell (label-based)
coffee.at[0, "Units Sold"] = 20
print("\n18. Change Data with at -> [0,'Units Sold'] = 20 (optimized for single cell)")
print(coffee.head())

# (D) More optimized way -> .iat for single value
# .iat is faster than .iloc when updating ONE cell (integer-based)
coffee.iat[2, 2] = 30   # row index 2, col index 2 (assuming 'Units Sold' is col 2)
print("\n19. Change Data with iat -> [2,2] = 30 (optimized for single cell)")
print(coffee.head())

# =====================================================
# Notes:
# - Use loc/iloc if working with multiple rows or columns.
# - Use at/iat if changing/getting a SINGLE value (faster).
# =====================================================
