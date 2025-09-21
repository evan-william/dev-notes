import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: CUMSUM & ROLLING
----------------------------------
- .cumsum(): Cumulative sum of values
- .rolling(window): Apply calculations over a sliding window
- Useful for cumulative totals & moving averages (time-series)
"""

# ==================================================
# 1. LOAD COFFEE DATA
# ==================================================
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("1. Coffee Data (original head):\n", coffee.head())

# ==================================================
# 2. ADD PRICE & REVENUE
# ==================================================
np.random.seed(69)  # reproducible random results
coffee["price"] = np.random.randint(100, 400, size=len(coffee))
coffee["revenue"] = coffee["Units Sold"] * coffee["price"]

print("\n2. Coffee Data with 'price' & 'revenue':\n", coffee.head(10))

# ==================================================
# 3. CUMULATIVE SUM
# ==================================================
coffee["cumulative_revenue"] = coffee["revenue"].cumsum()

print("\n3. Cumulative Revenue (added as new column):")
print(coffee.head(10))

"""
💡 .cumsum()
- Adds up values cumulatively row by row
- Row N = sum of all values from Row 1 → Row N
- Often used in:
    - Running totals (e.g., cumulative sales)
    - Cumulative rainfall, stock prices, etc.
"""

# ==================================================
# 4. ROLLING (MOVING WINDOW)
# ==================================================

# 4.1 Example: Latte sales over last 3 days
latte = coffee[coffee["Coffee Type"] == "Latte"].copy()
latte["3_day_sales"] = latte["Units Sold"].rolling(window=3).sum()

print("\n4. Latte Data with 3-Day Rolling Sum of Units Sold:")
print(latte.head(10))

"""
💡 .rolling(window=n)
- Creates a moving/sliding window of size n
- Default = right-aligned (window ends at current row)
- First (n-1) rows → NaN (not enough data to fill window)
- Common aggregations: .sum(), .mean(), .max(), .min(), .std()

Example:
  Window=3
  Row 3 = sum(Row 1, 2, 3)
  Row 4 = sum(Row 2, 3, 4)
  Row 5 = sum(Row 3, 4, 5)
"""

# 4.2 Rolling Mean Example (smoothing)
latte["3_day_avg_sales"] = latte["Units Sold"].rolling(window=3).mean()

print("\n5. Latte Data with 3-Day Rolling Average of Units Sold:")
print(latte.head(10))

"""
💡 Rolling Mean
- Smooths out short-term fluctuations
- Common in stock analysis, demand forecasting
- Moving Average = sum(window) / n
"""

# ==================================================
# 5. SUMMARY NOTES
# ==================================================
"""
🔑 .cumsum()
- Builds a running total
- Easy way to see "growth over time"

🔑 .rolling()
- Sliding window calculations
- Must call aggregation (.sum(), .mean(), etc.)
- Great for moving averages, rolling trends

✅ Common Uses
- Track cumulative sales/revenue
- Calculate moving averages for stocks
- Rolling sums of production, demand, or rainfall
- Smooth noisy time-series data
"""
