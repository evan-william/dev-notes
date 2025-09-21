import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: GROUPBY OPERATIONS
-----------------------------------
- Summarize data by categories
- Common aggregations: sum, mean, count, etc.
- Can group by one or multiple columns
- Similar to SQL GROUP BY
"""

# =====================================================
# 1. LOADING DATAFRAMES
# =====================================================

# Load Bios dataset (Olympic Athletes)
bios = pd.read_csv(
    "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv"
)

print("\n1. Original Data of Bios (first 5 rows):")
print(bios.head())

# Top cities of Olympic athletes' birthplaces
print("\n2. Top Cities Olympic Athletes Come From: ")
print(bios['born_city'].value_counts().head(10))

# Filtering example: Top regions for USA-born athletes
print("\n3. Top Regions USA Olympic Athletes Come From: ")
print(
    bios[bios['born_country'] == 'USA']['born_region']
    .value_counts()
    .head(10)
)


# =====================================================
# 2. LOADING COFFEE DATAFRAME
# =====================================================
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)

# Add a random "Price" column for demo purposes
np.random.seed(42)  # reproducible random results
coffee['Price'] = np.random.randint(2, 10, size=len(coffee))

# Add "Revenue" column = Units Sold × Price
coffee['Revenue'] = coffee['Units Sold'] * coffee['Price']

# (Optional) Add a temporary Roast column for testing groupby with multiple columns
coffee['Roast'] = np.random.choice(['Light', 'Medium', 'Dark'], size=len(coffee))

print("\n4. Original Coffee Data (with Price, Revenue & Roast added):\n", coffee.head())


# =====================================================
# 3. GROUPBY EXAMPLES
# =====================================================

# (a) Groupby Coffee Type → Sum of Units Sold
print("\n5. GroupBy Coffee Type → Sum of Units Sold:")
print(coffee.groupby('Coffee Type')['Units Sold'].sum())

# (b) Groupby Coffee Type → Mean of Units Sold
print("\n6. GroupBy Coffee Type → Mean of Units Sold:")
print(coffee.groupby('Coffee Type')['Units Sold'].mean())

# (c) Groupby with Multiple Aggregations
print("\n7. GroupBy Coffee Type → Sum of Units Sold, Mean of Price:")
print(
    coffee.groupby('Coffee Type')
    .agg({'Units Sold':'sum', 'Price':'mean'})
)
"""
💡 .agg({...}) → Allows multiple aggregations at once:
   Example: {'col1':'sum', 'col2':'mean'}
"""

# (d) Groupby with Size (counts number of rows per group) 
print("\n8. GroupBy Coffee Type → Count of Transactions:")
print(coffee.groupby('Coffee Type').size())

# (e) Groupby Multiple Columns (Coffee Type + Roast)
print("\n9. GroupBy Coffee Type + Roast → Sum of Units Sold:")
print(coffee.groupby(['Coffee Type','Roast'])['Units Sold'].sum())

# (f) Groupby and Sort Results
print("\n10. GroupBy Coffee Type → Total Units Sold, Sorted Descending:")
print(
    coffee.groupby('Coffee Type')['Units Sold']
    .sum()
    .sort_values(ascending=False)
)

# (g) Groupby Multiple Columns (Coffee Type + Day) with Multiple Aggregations
print("\n11. GroupBy Coffee Type + Day → Sum of Units Sold, Mean of Price, Total Revenue:")
print(
    coffee.groupby(['Coffee Type','Day'])
    .agg({'Units Sold':'sum', 'Price':'mean', 'Revenue':'sum'})
)

# Drop Roast column after testing (to keep dataset clean)
coffee = coffee.drop(columns=['Roast'])


# =====================================================
# 4. SUMMARY NOTES
# =====================================================

"""
💡 GroupBy Notes:
- groupby('col')['col2'].sum() → aggregate a single column
- groupby('col').agg({...}) → apply multiple aggregations at once
- .size() → counts rows per group
- Can group by multiple columns (multi-index result)
- Combine with .sort_values() for ranking (e.g., top sales)

🔑 Added Columns:
- Price (random integer for demo)
- Revenue = Units Sold × Price
- Roast (temporary, only for testing groupby with multiple columns → then dropped)

🔑 Summary:
- GroupBy is essential for data aggregation and summarization.
- Works like SQL's GROUP BY.
- Very powerful when combined with filtering, sorting, and .agg().
"""
