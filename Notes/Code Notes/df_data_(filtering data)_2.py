import pandas as pd

"""
PANDAS FILTERING WITH CONDITIONS
--------------------------------
Covers:
- String operations
- Query filtering
- Datetime conversion & filtering
- Map & Replace
- Exporting final results
"""

# ----------------------------------#
# 1. Load Data
bios = pd.read_csv(
    "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv"
)
print("1. Original Data (first 6 rows):\n", bios.head(6))

# ----------------------------------#
# 2. Copy DataFrame (to keep original safe)
bios_new = bios.copy()
print("\n2. Created a copy of original DataFrame.")

# ----------------------------------#
# 3. String Manipulation - Extract First Name
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
print("\n3. Added 'first_name' column by splitting on space and taking first word:\n",
      bios_new[['name','first_name']].head())

# ----------------------------------#
# 4. Filtering with Query
test = bios_new.query('first_name == "Keith"')
print("\n4. Filtered rows where first_name == 'Keith':\n", test)

# ----------------------------------#
# 5. DataFrame Info (Before Datetime Conversion)
print("\n5. DataFrame Info (before converting dates):")
bios_new.info()

# ----------------------------------#
# 6. Converting String Dates to Datetime
bios_new['born_date_converted'] = pd.to_datetime(bios_new['born_date'], errors='coerce')
print("\n6. Converted 'born_date' → datetime (with errors='coerce'):")
bios_new.info()

# ----------------------------------#
# 7. Extracting Date Components
bios_new['born_year'] = bios_new['born_date_converted'].dt.year
bios_new['born_month'] = bios_new['born_date_converted'].dt.month
bios_new['born_day'] = bios_new['born_date_converted'].dt.day
bios_new['is_leap_year'] = bios_new['born_date_converted'].dt.is_leap_year

print("\n7. Extracted datetime components (year, month, day, leap_year):\n",
      bios_new[['name','born_date_converted','born_year','born_month','born_day','is_leap_year']].head())

# ----------------------------------#
# 8. Filtering by Date Conditions
born_after_1900 = bios_new[bios_new['born_year'] > 1900]
print("\n8. Filtered rows where born_year > 1900:\n",
      born_after_1900[['name','born_year']].head())

# ----------------------------------#
# 9. Combined Filters (String + Date)
combined_filter = bios_new[
    (bios_new['first_name'] == 'Keith') & 
    (bios_new['born_year'] > 1900)
]
print("\n9. Combined filter (first_name='Keith' AND born_year>1900):\n", 
      combined_filter[['name','first_name','born_year']])

# ----------------------------------#
# 10. Using .map() for Value Transformation
# Example: convert 'gender' column into boolean
# 'male' → True, 'female' → False
bios_new['gender_bool'] = bios_new['gender'].map({'male': True, 'female': False})
print("\n10. Added 'gender_bool' column with map():\n",
      bios_new[['gender','gender_bool']].head())

# ----------------------------------#
# 11. Using .replace() for Quick Replacement
# Example: replace 'male' with 'M', 'female' with 'F'
bios_new['gender_short'] = bios_new['gender'].replace({'male': 'M', 'female': 'F'})
print("\n11. Added 'gender_short' column with replace():\n",
      bios_new[['gender','gender_short']].head())

# ----------------------------------#
# 12. Final DataFrame Summary
print("\n12. Final DataFrame after string, datetime, map & replace processing:\n", bios_new.head())

# ----------------------------------#
# 13. Exporting the Result
bios_new.to_csv(r"data/bios_new.csv", index=False)
print("\n13. Exported processed DataFrame to 'data/bios_new.csv'")

# ----------------------------------#
# 14. Removing Duplicates
# Example DataFrame with potential duplicates
df_example = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})

# 14a. Remove all duplicate rows (keeps first occurrence)
df_no_dupes = df_example.drop_duplicates()
print("\n14a. Removed all duplicates (keep first occurrence):\n", df_no_dupes)

# 14b. Remove consecutive duplicates only
df_no_consecutive_dupes = df_example[df_example['A'] != df_example['A'].shift()].reset_index(drop=True)
print("\n14b. Removed consecutive duplicates only:\n", df_no_consecutive_dupes)
