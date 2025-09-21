import pandas as pd

"""
SORTING DATA WITH sort_values()
- Default: ascending order.
- Can sort by one or multiple columns.
- Use ascending=[True/False,...] for multi-column sorting.
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
# 1. Sorting by Single Column
# =====================================================
print("\n1. Sorted by 'Units Sold' (Ascending):")
print(coffee.sort_values("Units Sold"))

print("\n2. Sorted by 'Units Sold' (Descending):")
print(coffee.sort_values("Units Sold", ascending=False))

# =====================================================
# 2. Sorting by Multiple Columns
# =====================================================
# If the first column has duplicates, Pandas sorts by the second (tie-breaker).
print("\n3. Sorted by 'Units Sold' then 'Coffee Type' (Both Ascending):")
print(coffee.sort_values(["Units Sold", "Coffee Type"]))

# =====================================================
# 3. Sorting with Different Orders
# =====================================================
# Use ascending=[list of booleans]:
# - 'Units Sold' -> Descending (largest first)
# - 'Coffee Type' -> Ascending (A → Z) if 'Units Sold' is equal
print("\n4. Sorted by 'Units Sold' (Descending) and 'Coffee Type' (Ascending):")
print(coffee.sort_values(["Units Sold", "Coffee Type"], ascending=[False, True]))

# =====================================================
# Notes (Cleaned Up)
# -----------------------------------------------------
# ✅ ascending=True/False (single column)
# ✅ ascending=[True, False] (multi-column, mixed order)
# ✅ inplace=True → modify the DataFrame directly
# ✅ na_position='first'/'last' → control where NaN values appear
#
# Example: df.sort_values("col", ascending=False, na_position="first")
# -----------------------------------------------------

# =====================================================
# 4. Iterating Rows (Not the most efficient in pandas)
# =====================================================
# iterrows() allows you to loop through rows as (index, Series).
# It's flexible but slower than vectorized operations.
# Better: use vectorized methods instead of loops if possible.
print("\n5. Iterating rows with iterrows():")
for index, row in coffee.iterrows():
    print(f"Index: {index}, Units Sold: {row['Units Sold']}")
