import pandas as pd

"""
PANDAS CUSTOM FUNCTIONS + MERGING & CONCATENATION
--------------------------------------------------
This note covers:
- Custom functions with apply (lambda + normal def)
- Merging DataFrames (inner, left, right, outer joins)
- Handling suffixes when overlapping column names
- Comparing merged columns
- Filtering subsets of DataFrames
- Concatenating multiple DataFrames
"""

# =====================================================
# 1. LOADING DATAFRAMES
# =====================================================

# Load from CSV (Bios dataset)
bios = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv")

print("\nOriginal Data of Bios (first 5 rows):")
print(bios.head())

# =====================================================
# 2. CUSTOM FUNCTION (COLUMN CREATION & AGGREGATION)
# =====================================================

# ---- Lambda function example (Column Creation) ----
print("\nAdded 'height_category' column using Lambda Function:")

bios['height_category'] = bios['height_cm'].apply(
    lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall')
)
print(bios[['name','height_cm','height_category']].head())


# ---- Lambda function for aggregation (groupby) ----
print("\nSumming the Top 3 values within groups using Lambda:")

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'),
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

# For each group, find the 3 largest values and sum them
result = (
    df.groupby('grps')['vals']
      .apply(lambda x: x.nlargest(3).sum())
)
print(result)

"""
💡 Explanation of the aggregation:
- df.groupby('grps')['vals']: First, the DataFrame is grouped by the 'grps' column, and we select the 'vals' column for our operation.
- .apply(lambda x: ...): The apply function is used to execute a custom operation on each group.
- lambda x: x.nlargest(3).sum(): This is the custom lambda function.
    - 'x' represents the Series of 'vals' for each individual group (e.g., all 'vals' for group 'a').
    - x.nlargest(3) selects the top 3 highest values from that Series.
    - .sum() calculates the sum of those 3 values.
- The final result is a new Series showing the calculated sum for each group.
"""


# ---- Normal Python function example ----
print("\nAdded 'Category' column using Custom Python Function:")

def categorize_weight(row):
    """
    Categorize athlete based on height & weight.
    Must use axis=1 so that function is applied row-by-row.
    """
    if row['height_cm'] < 175 and row['weight_kg'] < 70:
        return 'Lightweight'
    elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
        return 'Middleweight'
    else:
        return 'Heavyweight'

bios['Category'] = bios.apply(categorize_weight, axis=1)
print(bios[['name','height_cm','weight_kg','Category']].head())


# =====================================================
# 3. MERGING DATAFRAMES
# =====================================================

# Reload fresh bios for merge demo
bios = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv")

# Load NOCs data
nocs = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/noc_regions.csv")
print("\nOriginal NOCs Data (first 5 rows):")
print(nocs.head())

# ---- Basic Merge ----
print("\nMerging 'bios' and 'nocs' DataFrames (on born_country = NOC):")

merged = pd.merge(
    bios, nocs,
    left_on='born_country',
    right_on='NOC',
    how='left'   # LEFT JOIN
)
print(merged.head())

"""
💡 Explanation of how='left':
- 'left' means: keep ALL rows from the left DataFrame (bios).
- For each row in 'bios', Pandas looks up matches in 'nocs' based on born_country = NOC.
- If a match exists → values from 'nocs' are added.
- If no match exists → result will contain NaN for 'nocs' columns.

Other join options:
- how='inner' → only rows with matches in both DataFrames are kept.
- how='right' → keep ALL rows from 'nocs' (right DataFrame).
- how='outer' → keep ALL rows from both DataFrames; unmatched rows get NaN.

This is conceptually the same as SQL joins:
LEFT JOIN, RIGHT JOIN, INNER JOIN, FULL OUTER JOIN.
"""

# ---- Handling duplicate column names with suffixes ----
print("\nCustom Suffix Example (since both have 'NOC' column):")

merged_custom = pd.merge(
    bios, nocs,
    left_on='born_country',
    right_on='NOC',
    how='left',
    suffixes=["_bios","_nocs"]
)
print(merged_custom.head())


# =====================================================
# 4. COMPARING MERGED COLUMNS
# =====================================================

print("\nComparing where 'NOC_bios' and 'region' do NOT match:")

comparison = merged_custom[
    merged_custom['NOC_bios'] != merged_custom['region']
][['name','NOC_bios','region']]

print(comparison)

"""
💡 Explanation of comparison:
- After merging, we now have both bios['born_country'] (renamed NOC_bios) and nocs['region'].
- Sometimes the codes don't match the expected region (data inconsistency).
- merged_custom['NOC_bios'] != merged_custom['region'] creates a Boolean mask (True/False for each row).
- Using that mask inside DataFrame filtering → selects only the rows with mismatch.
- Finally, we print only 'name', 'NOC_bios', and 'region' columns to inspect inconsistencies.
"""


# =====================================================
# 5. FILTERING SUBSETS (USA / GBR EXAMPLES)
# =====================================================

print("\nSubset where born_country == 'USA':")
usa = bios[bios['born_country'] == 'USA'].copy()
print(usa.head())

print("\nSubset where born_country == 'GBR':")
gbr = bios[bios['born_country'] == 'GBR'].copy()
print(gbr.head())

# ---- Combine multiple subsets ----
print("\nConcatenated DataFrame (USA + GBR athletes):")

usa_gbr = pd.concat([usa, gbr])
print(usa_gbr[['name','born_country']].head(10))

"""
💡 Explanation of concat:
- pd.concat([df1, df2]) stacks DataFrames vertically (like SQL UNION ALL).
- Columns must match (otherwise Pandas fills missing ones with NaN).
- By default, row indices are preserved. Can reset index with ignore_index=True.
"""


# =====================================================
# 6. MERGING WITH A THIRD DATAFRAME
# =====================================================

# Reload for clean example
bios = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv")
results = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/results.csv")

print("\nOriginal Results Data (first 5 rows):")
print(results.head())

# Merge on athlete_id
print("\nMerging 'results' with 'bios' on athlete_id:")
combined_df = pd.merge(results, bios, on='athlete_id', how='left')
print(combined_df.head())

"""
💡 Key Notes on Merge:
- on='athlete_id' → join key column present in BOTH DataFrames.
- how='left' → keep all rows from 'results' (the left DataFrame).
- If an athlete_id exists in 'results' but not in 'bios', the bio columns = NaN.
- If an athlete_id exists in both → values are merged.
"""


# =====================================================
# END NOTES
# =====================================================

"""
Summary:
- Custom functions (lambda + def) let us flexibly create new columns and perform complex aggregations.
- Merges align rows across DataFrames, like SQL joins.
- how= parameter controls inclusion of unmatched rows.
- suffixes resolve column name collisions.
- Filtering lets us spot inconsistencies.
- concat simply stacks DataFrames vertically (row-wise).
"""