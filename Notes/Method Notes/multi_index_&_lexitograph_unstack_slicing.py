import pandas as pd
import numpy as np

letters = ['A', 'B', 'C']
numbers = list(range(10))

# ----------------------------------#
# 1. Create MultiIndex Series
mi = pd.MultiIndex.from_product([letters, numbers])
s = pd.Series(np.random.rand(30), index=mi)

print("1. MultiIndex Series:\n", s.head(12), "\n")

"""
- MultiIndex: hierarchical indexing with multiple levels.
- Here: Level 0 = letters (A, B, C), Level 1 = numbers (0–9).
- Total = 3 × 10 = 30 rows.
"""

# ----------------------------------#
# 2. MultiIndex Slicing with IndexSlice
result1 = s.loc[pd.IndexSlice[:'B', 5:]]
print("2. Slicing with IndexSlice (letters up to 'B', numbers >=5):\n", result1, "\n")

"""
Explanation:
- pd.IndexSlice[:'B', 5:] → 
  • Select all letters up to 'B' (A, B)
  • Within them, numbers from 5 to 9
"""

# ----------------------------------#
# 3. Equivalent Slicing Without IndexSlice
result2 = s.loc[slice(None, 'B'), slice(5, None)]
print("3. Equivalent slicing using slice():\n", result2, "\n")

"""
slice(None, 'B') → Level 0: everything up to 'B'
slice(5, None)  → Level 1: numbers from 5 onward
"""

# ----------------------------------#
# 4. Using .unstack()
unstacked = s.unstack()
print("4. Unstacked (Series → DataFrame):\n", unstacked.head(), "\n")

col_sum = unstacked.sum(axis=0)
print("Column sums after unstacking:\n", col_sum, "\n")

"""
- unstack() pivots inner index (numbers) into columns.
- Now looks & behaves like a DataFrame.
- .sum(axis=0) sums down rows for each column (per number).
"""

# ----------------------------------#
# 5. Swap Index Levels
new_s = s.swaplevel(0, 1)
print("5. Swap levels (numbers outer, letters inner):\n", new_s.head(12), "\n")

"""
swaplevel(0,1) → flips index hierarchy:
   Before: (Letter, Number)
   After : (Number, Letter)
"""

# ----------------------------------#
# 6. Sort Index if Not Monotonic Increasing
if not new_s.index.is_monotonic_increasing:
    new_s = new_s.sort_index()
print("6. After sort_index (monotonic increasing):\n", new_s.head(12), "\n")

"""
- MultiIndex slicing requires sorted order.
- Use .is_monotonic_increasing instead of deprecated .is_lexsorted().
- If False → sort with .sort_index().
"""

# ----------------------------------#
# 7. Summation by Level
level_sum = s.groupby(level=0).sum()
print("7. Sum by Level 0 (letters):\n", level_sum, "\n")

level_sum_num = s.groupby(level=1).sum()
print("Sum by Level 1 (numbers):\n", level_sum_num, "\n")

"""
- groupby(level=0).sum() → collapse across numbers, keeping one value per letter.
- groupby(level=1).sum() → collapse across letters, keeping one value per number.
"""

# ----------------------------------#
# 8. Selecting Specific Inner Index Values
subset = s.loc[:, [1, 3, 6]]
print("8. Selecting only numbers 1, 3, 6:\n", subset, "\n")

"""
- loc[:, [1,3,6]] → keep all letters, only numbers 1, 3, 6.
"""

# ----------------------------------#
# 9. Monotonicity / Lexicographic Check
print("9. Monotonicity check:")
print("Is index monotonic increasing? :", s.index.is_monotonic_increasing)
print("Is index fully sorted for slicing?:", s.index.is_monotonic_increasing)
print("Number of levels in MultiIndex:   ", s.index.nlevels, "\n")

"""
- .is_monotonic_increasing → modern way to check sorted order.
- .lexsort_depth shows how many levels are sorted.
- If lexsort_depth == nlevels → fully sorted.
"""

# ----------------------------------#
# 10. Summary of MultiIndex Concepts
print("10. Summary of MultiIndex Concepts:")
print("""
1. MultiIndex = hierarchical index (multi-level).
2. Use pd.IndexSlice or slice() for advanced slicing.
3. .unstack() → reshape Series → DataFrame.
4. .swaplevel() → flip hierarchy of index levels.
5. .sort_index() → ensures monotonic increasing order.
6. .groupby(level=n).sum() → collapse data across a level (like old sum(level=n)).
7. loc[:, [values]] → select specific inner index values.
8. .is_monotonic_increasing → check if index is sorted for slicing (replaces is_lexsorted).
9. .nlevels → number of levels in the MultiIndex.
""")
