import pandas as pd
import numpy as np

"""
PANDAS: SPLITTING LISTS INTO MULTIPLE COLUMNS
"""

# Sample DataFrame
df = pd.DataFrame({
    'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                'Budapest_PaRis', 'Brussels_londOn'],
    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                '12. Air France', '"Swiss Air"']
})

print("Original DataFrame:\n", df, "\n")

# ----------------------------------#
# 1. Convert list-like column into Series
delays = df['RecentDelays'].apply(pd.Series)
print("1. Converted 'RecentDelays' into a new DataFrame:\n", delays, "\n")

# Explanation:
# - Each list in 'RecentDelays' becomes a row.
# - Elements of the list are spread across new columns.
# - If a list is shorter, missing values become NaN.

# ----------------------------------#
# 2. Rename delay columns dynamically
delays.columns = ['delay_{}'.format(n) for n in range(1, len(delays.columns)+1)]
print("2. Renamed columns:\n", delays.head(), "\n")

# ----------------------------------#
# 3. Drop original 'RecentDelays' and join expanded columns
df = df.drop('RecentDelays', axis=1).join(delays)
print("3. Final DataFrame after join:\n", df, "\n")

# ----------------------------------#
# 4. Summary of Steps
print("4. Summary of Steps Performed:")
print("""
1. df['RecentDelays'].apply(pd.Series) 
   → Expands lists into multiple columns.
2. Rename columns dynamically (delay_1, delay_2, etc.).
3. Drop the original 'RecentDelays' column.
4. Join new columns back to the main DataFrame.
""")
