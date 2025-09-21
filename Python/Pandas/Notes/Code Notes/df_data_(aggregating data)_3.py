import numpy as np
import pandas as pd

"""
PANDAS DATAFRAME: GROUPBY OPERATIONS (DATETIME EDITION)
-------------------------------------------------------
- Using groupby with datetime values
- Extracting year, month, etc. using .dt accessor
- Resetting index for cleaner DataFrames
- Sorting aggregated results
- Using pd.cut for binning numeric data
"""

# =====================================================
# 1. LOADING DATAFRAME
# =====================================================

# Load Olympic Athletes (bios dataset)
bios = pd.read_csv(
    "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv"
)

print("\n1. Original Data of Bios (first 5 rows):")
print(bios.head())

# =====================================================
# 2. DATETIME CONVERSION
# =====================================================

print("\n2. DataFrame Info BEFORE converting 'born_date':")
bios.info()

# Convert "born_date" from string → datetime
bios['born_date'] = pd.to_datetime(bios['born_date'])

print("\n3. DataFrame Info AFTER converting 'born_date':")
bios.info()

# =====================================================
# 3. GROUPBY USING YEAR
# =====================================================

print("\n4. GroupBy 'born_date'.dt.year → Count Athletes:")
print(
    bios.groupby(bios['born_date'].dt.year)['name'].count()
)

# =====================================================
# 4. CLEANING RESULTS WITH RESET_INDEX & SORT_VALUES
# =====================================================

# Reset index → converts the groupby index into normal columns
# Sort values → order results by athlete count (descending)
yearly_counts = (
    bios.groupby(bios['born_date'].dt.year)['name']
    .count()
    .reset_index()                     # index → normal column
    .sort_values('name', ascending=False)  # sort by count
)

print("\n5. Yearly Athlete Counts (Cleaned):")
print(yearly_counts.head(10))

# =====================================================
# 5. GROUPBY YEAR + MONTH
# =====================================================

# Extract year & month as new columns
bios['year_born'] = bios['born_date'].dt.year
bios['month_born'] = bios['born_date'].dt.month

# Group by (year, month)
year_month_counts = (
    bios.groupby(['year_born','month_born'])['name']
    .count()
    .reset_index()
    .sort_values('name', ascending=False)
)

print("\n6. Year + Month Athlete Counts (Top Results):")
print(year_month_counts.head(10))

# =====================================================
# 6. BINNING NUMERIC DATA WITH pd.cut
# =====================================================

# Example DataFrame
df = pd.DataFrame({'A': [5, 12, 25, 33, 47, 55, 68, 75, 82, 95],
                   'B': [10, 20, 15, 10, 25, 30, 22, 18, 40, 35]})

# Define bins for column 'A'
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Use pd.cut to assign each value of 'A' into a bin
df['A_bin'] = pd.cut(df['A'], bins=bins)

print("\n7. DataFrame with Binned Column 'A_bin':")
print(df)

# Group by bins and sum 'B' values per bin
binned_sum = df.groupby('A_bin')['B'].sum()
print("\nSum of B per bin of A:")
print(binned_sum)

"""
💡 Notes on pd.cut:
- pd.cut(array, bins) → categorizes numeric data into discrete intervals (bins).
- Each bin is represented as a range (e.g., (0,10], (10,20], etc.).
- Useful for summarizing continuous data in ranges.
- Often combined with groupby to aggregate values per bin.
- In the example:
  1) df['A'] values are assigned to bins defined by 'bins'.
  2) Then we group by 'A_bin' to sum the corresponding 'B' values per interval.
"""

# =====================================================
# 7. SUMMARY NOTES
# =====================================================

"""
🔑 Key Concepts:

1) GroupBy with DateTime
   - bios['born_date'].dt.year → extracts YEAR
   - bios['born_date'].dt.month → extracts MONTH
   - Useful for time-based aggregations (yearly sales, monthly users, etc.)

2) reset_index()
   - Converts grouped index back into normal DataFrame column.
   - Makes DataFrame easier to filter, merge, or visualize.

3) sort_values()
   - Orders results by a column.
   - Common to see "Top N" categories or trends.

4) Multi-Level GroupBy
   - Grouping by year & month creates a multi-index.
   - reset_index() flattens it into normal columns.

5) pd.cut()
   - Bins numeric data into discrete intervals.
   - Often combined with groupby to aggregate values per bin.
   - Example: Summing column 'B' per interval of 'A'.

-------------------------------------
✅ Practical Uses:
- Time series aggregation (sales, users, revenue)
- Seasonal trends (month, quarter)
- Year-over-year or month-over-month growth
- Binning continuous numeric data for analysis (age groups, revenue ranges, etc.)
"""
