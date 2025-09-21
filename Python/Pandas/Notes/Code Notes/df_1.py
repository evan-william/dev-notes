import pandas as pd
import numpy as np

"""
INTRODUCTION
PANDAS DATAFRAME: CREATION, ACCESSING & ANALYSIS
PANDAS SERIES: FUNDAMENTALS
----------------------------------------
- Series = 1D labeled array (like a single column in DataFrame).
- DataFrame = collection of Series objects sharing the same index.
"""

# ----------------------------------#
# 1. Create a DataFrame
df = pd.DataFrame([[1,2,3],
                   [4,5,6],
                   [5,6,7],
                   [8,9,10]],
                  columns=["A","B","C"])
print("1. Original DataFrame:\n", df)

# ----------------------------------#
# 2. Access Top & Bottom Rows
print("\n2. Access Top & Bottom Rows:")
print("First row (head 1):\n", df.head(1))
print("Last row (tail 1):\n", df.tail(1))

# ----------------------------------#
# 3. Columns & Index
print("\n3. Columns & Index:")
print("Columns =", df.columns)
print("Index =", df.index)
print("Index (as list) =", df.index.tolist())

# ----------------------------------#
# 4. Specify Custom Index
df2 = pd.DataFrame([[1,2,3],
                    [4,5,6],
                    [5,6,7],
                    [8,9,10]],
                   columns=["A","B","C"],
                   index=["W","X","Y","Z"])
print("\n4. DataFrame with Custom Index:\n", df2)

# ----------------------------------#
# 5. Info About DataFrame
print("\n5. DataFrame Info:")
df.info()

# ----------------------------------#
# 6. Descriptive Statistics
print("\n6. Descriptive Statistics (describe):\n", df.describe())

# ----------------------------------#
# 7. Unique Values
print("\n7. Unique Values:")
print("Unique values count per column:\n", df.nunique())
print("Unique values in column A =", df['A'].unique())

# ----------------------------------#
# 8. Shape & Size
print("\n8. Shape & Size:")
print("Shape [rows, columns] =", df.shape)
print("Total elements (size) =", df.size)

# ----------------------------------#
# 9. Select Columns
print("\n9. Select Columns:")
print("Column A:\n", df["A"])
print("Multiple Columns A & C:\n", df[["A","C"]])

# ----------------------------------#
# 10. Select Rows
print("\n10. Select Rows by Index:")
print("Row with label 0:\n", df.loc[0])
print("Row at position 1:\n", df.iloc[1])

# ----------------------------------#
# 11. Conditional Selection
print("\n11. Conditional Selection:")
print("Rows where A > 4:\n", df[df["A"] > 4])

# ----------------------------------#
# 12. Adding New Column
df["D"] = df["A"] + df["B"]
print("\n12. Added New Column D = A + B:\n", df)

# ----------------------------------#
# 13. Dropping Column
df_dropped = df.drop("D", axis=1)
print("\n13. Dropped Column D:\n", df_dropped)

# ----------------------------------#
# 14. Renaming Columns
df_renamed = df.rename(columns={"A":"Alpha", "B":"Beta"})
print("\n14. Renamed Columns A->Alpha, B->Beta:\n", df_renamed)

# ----------------------------------#
# 15. Sorting
print("\n15. Sorting:")
print("Sort by Column B:\n", df.sort_values("B"))
print("Sort by Column A descending:\n", df.sort_values("A", ascending=False))

# ----------------------------------#
# 16. GroupBy
print("\n16. GroupBy Example:")
df_group = pd.DataFrame({
    "Category": ["A","A","B","B","C","C","C"],
    "Values": [10,20,30,40,50,50,10]
})
print("Grouped by Category (mean):\n", df_group.groupby("Category").mean())

# ----------------------------------#
# 17. Handling Missing Values
df_nan = pd.DataFrame({
    "A":[1,2,None,4],
    "B":[5,None,7,8]
})
print("\n17. Handling Missing Values:")
print("DataFrame with NaN:\n", df_nan)
print("Drop rows with NaN:\n", df_nan.dropna())
print("Fill NaN with 0:\n", df_nan.fillna(0))

# ----------------------------------#
# 18. Export & Import
print("\n18. Export & Import (CSV):")
df.to_csv("data.csv", index=False)
print("DataFrame exported to 'data.csv'")
df_loaded = pd.read_csv("data.csv")
print("DataFrame loaded from 'data.csv':\n", df_loaded)

# ----------------------------------#
# 19. Pandas Series
# (a) Series from Dictionary
a = {"x": 10, "y": 20, "z": 30}
s_dict = pd.Series(a)
print("\n19(a). Series from Dictionary:\n", s_dict)

# (b) Series from Tuple (with custom index)
t1 = (3,4,5)
s_tuple = pd.Series(t1, index=['a','b','c'])
print("\n19(b). Series from Tuple with Custom Index:\n", s_tuple)

# (c) Series from List
s_list = pd.Series([100,'test',300], index=["A","B","C"]) # Index optional
print("\n19(c). Series from List:\n", s_list)

# ----------------------------------#
# 20. Comparing Series
series1 = pd.Series([10,20,30], index=['a','b','c'])
series2 = pd.Series([10,25,30], index=['a','b','c'])

print("\n20. Comparing Series element-wise (series1 vs series2):")
print(series1 == series2)   # equality
print(series1 != series2)   # inequality
print(series1 > series2)    # greater than
print(series1 < series2)    # less than

# Multiple Series Comparison Example
series3 = pd.Series([10,20,35], index=['a','b','c'])
print("\nMultiple Series Comparison (all three equal?):")
print(series1.eq(series2) & series2.eq(series3))  # compare across 3 series

# ----------------------------------#
# 21. Value Counts
print("\n21. Value Counts (frequency of unique values in a column):")
print("Value counts for 'Category' column in df_group:\n", df_group["Category"].value_counts())
print("Value counts (normalized %):\n", df_group["Category"].value_counts(normalize=True))

# ----------------------------------#
# 22. Duplicates
df_dup = pd.DataFrame({
    "A":[1,2,2,3,3,3],
    "B":["x","y","y","z","z","z"]
})
print("\n22. Duplicates Handling:")
print("Original:\n", df_dup)
print("Check duplicates (duplicated):\n", df_dup.duplicated())
print("Drop duplicates (default keeps first):\n", df_dup.drop_duplicates())
print("Drop duplicates keep last:\n", df_dup.drop_duplicates(keep='last'))

# ----------------------------------#
# 23. Sort by Index
df_unsorted = df2.sample(frac=1)  # shuffle rows
print("\n23. Sort by Index (row labels):")
print("Unsorted:\n", df_unsorted)
print("Sorted by index:\n", df_unsorted.sort_index())
print("Sorted by index descending:\n", df_unsorted.sort_index(ascending=False))

# ----------------------------------#
# 24. Unstack: Convert DataFrames to Series
"""
💡 unstack()
- Converts a DataFrame to a Series with a MultiIndex
- Each column/row combination becomes a single value in the Series
- Default: unstack columns → index becomes MultiIndex (column_index, row_index)
- Often used for:
    • Flattening the DataFrame for easy sorting
    • Identifying top/bottom values
    • Transforming data for pivot-like operations
"""

# Example DataFrame
df_example = pd.DataFrame(np.random.RandomState(30).randint(1, 101, size=(4, 4)),
                          columns=['A','B','C','D'])
print("\n24. DataFrame Example:\n", df_example)

# 24.1 Unstacking
unstacked = df_example.unstack()
print("\nUnstacked Series (MultiIndex):\n", unstacked)

"""
Explanation:
- MultiIndex format: (column_index, row_index)
- Each cell in the DataFrame is now a value in a Series
"""

# 24.2 Sort values
sorted_series = unstacked.sort_values()
print("\nSorted values of unstacked Series:\n", sorted_series)

# 24.3 Top 3 values
top3_index = sorted_series[-3:].index.tolist()
print("\nTop 3 values index (column, row):\n", top3_index)

"""
Step-by-Step:
1️⃣ df_example.unstack() → flatten DataFrame to Series with MultiIndex
2️⃣ .sort_values() → sort all values ascending
3️⃣ [-3:] → take last 3 items → largest values
4️⃣ .index.tolist() → convert MultiIndex to list of tuples (column_index, row_index)

✅ Key Points:
- MultiIndex preserves column and row information
- Useful for finding top/bottom values across the entire DataFrame
- Can be combined with:
    • .max(), .min() for global extremes
    • .idxmax(), .idxmin() for positions
"""

# 24.4 Alternative: idxmax and idxmin for largest value
max_pos = df_example.unstack().idxmax()
min_pos = df_example.unstack().idxmin()
print("\nLargest value position:", max_pos)
print("Smallest value position:", min_pos)

# 24.5 Example with larger DataFrame
df_large = pd.DataFrame(np.random.RandomState(42).randint(1, 101, size=(6,6)))
top5_index = df_large.unstack().sort_values()[-5:].index.tolist()
print("\nTop 5 values in df_large (column, row):\n", top5_index)

"""
💡 NOTES SUMMARY:
1. value_counts():
   - Counts frequency of unique values in Series/column.
   - .value_counts(normalize=True) → percentage distribution.
   - Useful for categorical analysis.

2. duplicated():
   - Returns True for duplicate rows (by default considers all columns).
   - Can pass subset=['colname'] to check duplicates only on specific column.

3. drop_duplicates():
   - Removes duplicates.
   - keep='first' (default), keep='last', or keep=False (drop all duplicates).

4. sort_index():
   - Sorts DataFrame/Series by index (row labels or column labels if axis=1).
   - Different from sort_values(), which sorts by data values.
"""
