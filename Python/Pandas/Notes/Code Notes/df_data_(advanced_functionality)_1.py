import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: SHIFT & PERCENTAGE CHANGE
-------------------------------------------
- .shift(n): Shift data up/down by n rows
- .pct_change(): % change relative to previous row
- Useful for time-series & financial data
"""

# ----------------------------------#
# 1. Load Coffee Data
# ----------------------------------#
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("1. Coffee Data (original head):\n", coffee.head())

# ----------------------------------#
# 2. Add Price & Revenue
# ----------------------------------#
np.random.seed(69)  # reproducible random results
coffee["price"] = np.random.randint(100, 400, size=len(coffee))
coffee["revenue"] = coffee["Units Sold"] * coffee["price"]

print("\n2. Coffee Data with 'price' & 'revenue':\n", coffee.head(10))

# ----------------------------------#
# 3. Shift (Lag Values)
# ----------------------------------#
coffee["yesterday_revenue"] = coffee["revenue"].shift(2)

print("\n3. Yesterday's Revenue with shift(2):\n", coffee.head(10))

"""
💡 shift(2)
- Moves values DOWN by 2 rows
- Row N takes value from Row N-2
- First 2 rows become NaN
- Used for lag comparison (e.g., today vs 2 days ago)
"""

# ----------------------------------#
# 4. Negative Shift (Future Values)
# ----------------------------------#
coffee["next2_revenue"] = coffee["revenue"].shift(-2)

print("\n4. Next-2 Revenue with shift(-2):\n", coffee.head(10))

"""
💡 shift(-2)
- Moves values UP by 2 rows
- Row N takes value from Row N+2
- Last 2 rows become NaN
- Useful for comparing current vs future periods
"""

# ----------------------------------#
# 5. Percentage Change (Manual)
# ----------------------------------#
coffee["pct_change_manual"] = (
    coffee["revenue"] / coffee["yesterday_revenue"] - 1
) * 100

print("\n5. % Change vs Yesterday (manual formula):\n", coffee.head(10))

# ----------------------------------#
# 6. Percentage Change (Built-in)
# ----------------------------------#
coffee["pct_change_builtin"] = coffee["revenue"].pct_change(periods=2) * 100

print("\n6. % Change vs Yesterday (using .pct_change):\n", coffee.head(10))

"""
💡 .pct_change()
- Built-in method for percentage change
- Default: periods=1 (row N vs N-1)
- Can set periods=n → row N vs N-n
"""

# ----------------------------------#
# 7. Summary Notes
# ----------------------------------#
"""
🔑 .shift(n)
- Positive n = lag (look back)
- Negative n = lead (look ahead)
- Inserts NaN where data is missing

🔑 .pct_change()
- % change = (current - previous) / previous
- Handy for growth rates, stock returns, sales trends
- Equivalent to manual calculation with shift()

✅ Common Uses
- Compare sales today vs yesterday
- Calculate stock returns over n days
- Create lag/lead features for time-series ML models
"""

# Usage of Rank:
# Load Bios DataFrame
# =====================================================
# 1. LOADING DATAFRAMES
# =====================================================

# Load Bios dataset (Olympic Athletes)
bios = pd.read_csv(
    "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv"
)

print("\n1. Original Data of Bios (first 5 rows):")
print(bios.head())

# Rank Heights:
bios['height_rank'] = bios['height_cm'].rank()
test = bios.sort_values(['height_rank'],ascending=False)
print("\nBelow is the new Column Height_Rank with .rank(): ")
print(test)

# Better Heights Ranking:
bios['height_rank'] = bios['height_cm'].rank(ascending=False)
print("\nBelow is same like above but with better ranking number: ")
print(bios.sort_values(['height_rank']))    

# Get Sample(Random) Based On The Name and Height RAnk
print("\nBelow is 10 random sample for above: ")
print(bios.sort_values(['height_rank'])
      .sample(10)[['name','height_rank']])