import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: PIVOT & PIVOT_TABLE OPERATIONS
------------------------------------------------
- pivot(): reshapes data
  * index → rows
  * columns → new columns
  * values → cell values
  * ❌ Fails if there are duplicate index/column pairs

- pivot_table(): more flexible
  * Handles duplicates with aggregation
  * Has built-in aggregation functions (mean, sum, count, etc.)
  * Similar to Excel Pivot Tables
"""

# =====================================================
# 1. LOADING COFFEE DATAFRAME
# =====================================================
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)

print("\n1. Original Coffee Data (head):\n", coffee.head())

# Add Price column (random integers for demo)
coffee["Price"] = np.random.randint(1, 10, size=len(coffee))

# Add Revenue column (Units Sold * Price)
coffee["Revenue"] = coffee["Units Sold"] * coffee["Price"]
print("\n2. Added 'Revenue' column (Units Sold * Price):\n", coffee.head())


# =====================================================
# 2. PIVOT EXAMPLES
# =====================================================

# (a) Basic Pivot: Day as index, Coffee Type as columns, Revenue as values
pivot = coffee.pivot(index="Day", columns="Coffee Type", values="Revenue")
print("\n3. Pivot Table → Day vs Coffee Type, showing Revenue:\n", pivot)

"""
💡 Explanation:
- index='Day' → rows grouped by day of the week
- columns='Coffee Type' → each coffee type becomes a column
- values='Revenue' → cell entries filled with Revenue values
"""

# (b) Accessing Specific Values (using .loc)
print("\n4. Pivot + .loc → Monday's Latte Revenue:")
print(pivot.loc["Monday", "Latte"])

# (c) Summing Revenue by Coffee Type (column-wise)
print("\n5. Total Revenue per Coffee Type (sum across all days):")
print(pivot.sum(axis=0))

# (d) Summing Revenue by Day (row-wise)
print("\n6. Total Revenue per Day (sum across all coffee types):")
print(pivot.sum(axis=1))

"""
💡 axis parameter:
- axis=0 → sum *down columns* (i.e., per coffee type)
- axis=1 → sum *across rows* (i.e., per day)
"""


# =====================================================
# 3. EXTRA PIVOT USAGE
# =====================================================

# (a) Multiple value columns (Revenue + Units Sold)
pivot_multi = coffee.pivot(
    index="Day", columns="Coffee Type", values=["Units Sold", "Revenue"]
)
print("\n7. Pivot with Multiple Values (Units Sold & Revenue):\n", pivot_multi)

# (b) Pivot with Missing Combinations (NaN handling)
print(
    "\n8. NaN values appear if a combination is missing (e.g., no Mocha sold on Sunday)."
)
print("These can be filled with .fillna():\n", pivot.fillna(0))


# =====================================================
# 4. PIVOT_TABLE EXAMPLES
# =====================================================

"""
💡 pivot_table()
- Works like pivot, but allows aggregation
- Syntax:
  df.pivot_table(
      index=...,        # rows
      columns=...,      # columns
      values=...,       # values to summarize
      aggfunc='mean'    # aggregation function (default = mean)
  )
- Handles duplicate index/column pairs gracefully
"""

# (a) Average Revenue per Coffee Type per Day
pivot_table_mean = coffee.pivot_table(
    index="Day", columns="Coffee Type", values="Revenue", aggfunc="mean"
)
print("\n9. Pivot Table (Mean Revenue per Coffee Type per Day):\n", pivot_table_mean)

# (b) Total Revenue per Coffee Type per Day
pivot_table_sum = coffee.pivot_table(
    index="Day", columns="Coffee Type", values="Revenue", aggfunc="sum"
)
print("\n10. Pivot Table (Sum of Revenue per Coffee Type per Day):\n", pivot_table_sum)

# (c) Multiple Aggregations
pivot_table_multiagg = coffee.pivot_table(
    index="Day",
    columns="Coffee Type",
    values="Revenue",
    aggfunc=["mean", "sum", "count"],
)
print("\n11. Pivot Table with Multiple Aggregations (mean, sum, count):\n", pivot_table_multiagg)

# (d) Adding Margins (Row & Column Totals)
pivot_table_margin = coffee.pivot_table(
    index="Day",
    columns="Coffee Type",
    values="Revenue",
    aggfunc="sum",
    margins=True,
    margins_name="Total",
)
print("\n12. Pivot Table with Margins (Totals included):\n", pivot_table_margin)


# =====================================================
# 5. SUMMARY NOTES
# =====================================================

"""
💡 Pivot vs Pivot Table:
- pivot() → Simple reshaping, no aggregation. Fails if duplicates exist.
- pivot_table() → Can handle duplicates with aggfunc (default = mean).
                  Works like Excel Pivot Tables.

🔑 Common aggfunc options:
- 'mean' → average
- 'sum' → total
- 'count' → number of entries
- 'max' / 'min' → highest / lowest
- Custom: np.std, np.median, lambda functions, etc.

✅ Key Takeaways:
- Use pivot() when data is clean (unique index/column pairs).
- Use pivot_table() when you need aggregation or duplicates handling.
- Both are powerful tools for summarization & reshaping.
"""
