import pandas as pd
import numpy as np

"""
PANDAS DATAFRAME: ADDING, REMOVING, COPYING, AND MODIFYING
"""

# ----------------------------------#
# 1. Load Data
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("1. Coffee Data (head):\n", coffee.head())

# ----------------------------------#
# 2. Adding a New Column (All Same Value)
coffee['price'] = 4.99
print("\n2. Added 'price' column with constant 4.99:\n", coffee.head())

# ----------------------------------#
# 3. Adding Column with Numpy Where
coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 3.99, 5.99)
print("\n3. Added 'new_price' column (3.99 if Espresso, else 5.99):\n", coffee.head())

# ----------------------------------#
# 4. Dropping Rows
coffee_dropped_row = coffee.drop(0)
print("\n4. Dropped Row (index=0):\n", coffee_dropped_row.head())

# ----------------------------------#
# 5. Dropping Columns (Temporary vs Permanent)
print("\n5. Dropping Columns:")
print("Temporary drop of 'price':\n", coffee.drop(columns=['price']).head())

coffee.drop(columns=['price'], inplace=True)
print("\nAfter inplace drop, 'price' removed permanently:\n", coffee.head())

# ----------------------------------#
# 6. Copying DataFrames (Don't vs Do)
print("\n6. Copying DataFrames:")

# Don't (reference only)
coffee_new = coffee
coffee_new['bad_copy'] = "Bad Copy"
print("After modifying coffee_new (bad copy), original also changes:\n", coffee.head())

# Do (independent copy)
coffee_new = coffee.copy()
coffee_new['good_copy'] = "Good Copy"
print("\nAfter modifying coffee_new (good copy), original unaffected:\n")
print("coffee_new:\n", coffee_new.head())
print("\ncoffee (original):\n", coffee.head())

# ----------------------------------#
# 7. Selecting Columns
print("\n7. Selecting Columns:")
print("Two columns [Day, Coffee Type]:\n", coffee[['Day','Coffee Type']].head())

# ----------------------------------#
# 8. Creating Derived Column (Revenue)
coffee['revenue'] = coffee["Units Sold"] * coffee["new_price"]
print("\n8. Added 'revenue' column (Units Sold * new_price):\n", coffee.head())

# ----------------------------------#
# 9. Renaming Columns
print("\n9. Renaming Columns:")

# Temporary
coffee_temp = coffee.rename(columns={'new_price':'New Price'})
print("Temporary rename (new_price → New Price):\n", coffee_temp.head())

# Permanent
coffee.rename(columns={'new_price':'New Price'}, inplace=True)
print("\nPermanent rename applied:\n", coffee.head())

# ----------------------------------#
# 10. Summary of Operations Done
print("\n10. Final DataFrame after modifications:\n", coffee.head())
