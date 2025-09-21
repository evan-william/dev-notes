import pandas as pd
import numpy as np

"""
PANDAS TIME SERIES: CREATION, INDEXING, AND RESAMPLING
-------------------------------------------------------
A deep dive into creating, manipulating, and analyzing time series
data in pandas. This note covers:
- Generating date ranges with various frequencies.
- Indexing and filtering data based on date properties.
- Resampling time series data to different frequencies.
- Advanced grouping for periodic analysis.
"""

# ----------------------------------#
# 1. Setup: Creating a Sample Time Series
# ----------------------------------#
# To explore these concepts, we first need a time series.
# Let's create one with a random value for every business day in 2015.
# We'll set a seed for numpy's random number generator so the results are
# reproducible every time we run the script.
np.random.seed(42)

# Step 1: Create an index of all business days in 2015.
# 'B' frequency stands for "Business Day" (Monday to Friday).
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')

# Step 2: Create a pandas Series with random data, using our dates as the index.
# len(dti) ensures we have a random number for every single date in our index.
s = pd.Series(np.random.rand(len(dti)), index=dti)

print("1. Sample Time Series (first 5 rows):")
print(s.head())
print("\nLast 5 rows:")
print(s.tail())

# ----------------------------------#
# 2. Time-Based Indexing & Filtering
# ----------------------------------#
"""
One of the most powerful features of a time series is the ability to select
data based on date properties.
"""
# Example: Sum of all values that occurred on a Wednesday.
# s.index.weekday returns the day of the week for each date (Monday=0, Sunday=6).
# We filter for Wednesdays (weekday == 2) and then sum the results.
wednesday_sum = s[s.index.weekday == 2].sum()
print("\n2. Sum of all values on Wednesdays:", wednesday_sum)

"""
Use Cases for Time-Based Indexing:
- Analyzing weekly patterns (e.g., "Do sales spike on Fridays?").
- Calculating month-end or quarter-end financial reports.
- Isolating data for a specific period (e.g., holiday season).

More Examples:
- Get all data from May 2015: s['2015-05']
- Get the value for a specific day: s['2015-05-04']
- Get all data for the 7th month (July): s[s.index.month == 7].head()
"""
print("\nFirst 5 values in July (s.index.month == 7):")
print(s[s.index.month == 7].head())

# ----------------------------------#
# 3. Resampling: Changing Time Frequency
# ----------------------------------#
"""
Resampling is the process of converting a time series from one frequency
to another. It's like a `groupby()` operation specifically for time.
- Upsampling: Increasing frequency (e.g., from monthly to daily). Fills gaps.
- Downsampling: Decreasing frequency (e.g., from daily to monthly). Aggregates data.

Example: Downsample our daily data to get the average value for each month.
"""
# 'ME' is the frequency code for "Month End".
# This groups our daily data into monthly buckets and then calculates the mean for each.
monthly_average = s.resample('ME').mean()
print("\n3. Monthly Average of Values (Resampled):")
print(monthly_average)

"""
Use Cases for Resampling:
- Creating quarterly or annual reports from daily sales data.
- Calculating the total weekly rainfall from hourly sensor readings.
- Financial analysis: converting daily stock prices to weekly OHLC (Open, High, Low, Close).

More Examples:
- Calculate the SUM of values per QUARTER, labeled by the start of the quarter ('QS').
- Find the MAX value each WEEK, labeled by the end of the week ('W').
"""
quarterly_sum = s.resample('QS').sum()
print("\nQuarterly Sum of Values:")
print(quarterly_sum)

weekly_max = s.resample('W').max()
print("\nWeekly Maximum Value (first 5 weeks):")
print(weekly_max.head())

# ----------------------------------#
# 4. Advanced Grouping with `pd.Grouper`
# ----------------------------------#
"""
While `resample` is great, `groupby(pd.Grouper(...))` offers more
flexibility for complex time-based grouping.

Example: Find the date of the highest value within each 4-month period.
"""
# '4ME' means "4-Month End" frequency. It creates periods of 4 months.
# .idxmax() is the key: it returns the INDEX (the date) of the maximum value,
# not the maximum value itself.
date_of_max_value = s.groupby(pd.Grouper(freq='4ME')).idxmax()
print("\n4. Date of Highest Value in Each 4-Month Period:")
print(date_of_max_value)

"""
Use Cases for `pd.Grouper` and `idxmax`/`idxmin`:
- Pinpointing the exact day of peak sales each quarter.
- Identifying the moment of lowest server load in bi-weekly periods.
- Finding the best-performing day within each major marketing campaign period.

Let's also find the actual maximum value in those periods to compare.
"""
max_value_in_period = s.groupby(pd.Grouper(freq='4ME')).max()
print("\nActual Highest Value in Each 4-Month Period:")
print(max_value_in_period)


# ----------------------------------#
# 5. Advanced Date Range Generation
# ----------------------------------#
"""
`pd.date_range` is extremely versatile thanks to its powerful frequency strings
(also called offset aliases).

Example: Generate a list of dates for the 3rd Thursday of every month for 2 years.
"""
# 'WOM-3THU' is a frequency string with three parts:
# - WOM: "Week Of Month", the anchor for the rule.
# - 3: The 3rd week.
# - THU: The day, Thursday.
third_thursdays = pd.date_range(start='2015-01-01', end='2016-12-31', freq='WOM-3THU')

print("\n5. List of the 3rd Thursday of Each Month (first 5):")
print(third_thursdays[:5])

"""
Use Cases for Advanced Frequencies:
- Scheduling reports that need to run on specific days (e.g., the last business day of a quarter).
- Financial modeling for options that expire on the 3rd Friday of the month.
- Planning recurring meetings or events.

More Examples:
- 'BQS-DEC': Business Quarter Start, for a year ending in December.
- 'A-JUN': Annual frequency, anchored to the end of June.
"""
last_business_day_of_quarter = pd.date_range(start='2024-01-01', end='2025-12-31', freq='BQ-DEC')
print("\nLast Business Day of Each Quarter:")
print(last_business_day_of_quarter)

# ----------------------------------#
# 6. Summary of Key Functions
# ----------------------------------#
"""
🔑 SUMMARY OF KEY FUNCTIONS & USE CASES

1) pd.date_range()
   - Explanation: Generates a sophisticated sequence of dates. Its power lies in the `freq`
     parameter, which can create simple ranges ('B' for business days) or complex,
     repeating dates ('WOM-3THU' for the 3rd Thursday of the month).
   - Primary Use: The foundation for creating any time series. Used to build a DatetimeIndex.

2) Time-Based Indexing (e.g., s[s.index.weekday == 2])
   - Explanation: Filters your data based on date properties. You can access attributes like
     `.weekday`, `.month`, `.year`, `.dayofyear` directly on the series index.
   - Primary Use: Answering specific questions about time periods, like analyzing weekly
     patterns or comparing performance across different months or quarters.

3) s.resample()
   - Explanation: The primary tool for changing a time series' frequency. It acts as a
     `groupby` for time, splitting the data into buckets (e.g., daily -> monthly)
     and then applying an aggregation function (`.mean()`, `.sum()`, `.count()`, etc.).
   - Primary Use: Creating summary reports. The go-to method for converting high-frequency
     (e.g., daily) data into lower-frequency (e.g., monthly, quarterly, annual) summaries.

4) s.groupby(pd.Grouper())
   - Explanation: A more explicit and sometimes more flexible way to group time series data.
     It's used inside a standard `groupby` to define time-based buckets, often for
     non-standard periods like every 4 months (`4ME`) or every 2 weeks (`2W`).
   - Primary Use: Analyzing custom time windows or when the grouping logic is more
     complex than a simple frequency change.

5) .idxmax() / .idxmin()
   - Explanation: An aggregation function used after a groupby or resampling operation.
     Instead of returning the max/min VALUE, it returns the INDEX LABEL (the date)
     where that max/min value occurred.
   - Primary Use: Pinpointing the exact moment a key event happened. It answers "WHEN was the
     peak?" rather than "WHAT was the peak?".
"""