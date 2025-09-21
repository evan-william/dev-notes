import pandas as pd

"""
PANDAS FILTERING WITH CONDITIONS
--------------------------------
Ways to filter rows in a DataFrame:
1. Direct boolean indexing -> df[condition]
2. Using .loc[row_condition, column_selection]

- .loc is recommended when filtering rows + selecting columns.
- Direct boolean indexing is fine if you want all columns.
"""

# ============================
# Load Data
# ============================
bios = pd.read_csv(
    "https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv"
)

print("Original Data (first 6 rows):")
print(bios.head(6))

# ============================
# 1. Basic Filtering
# ============================
print("\n1. Athletes taller than 215 cm (all columns):")
print(bios.loc[bios["height_cm"] > 215])

# ============================
# 2. Filtering + Selecting Columns
# ============================
print("\n2. Athletes taller than 215 cm (name & height only):")
print(bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]])

# ============================
# 3. Alternative Syntax
# ============================
print("\n3. Direct boolean indexing (all columns):")
print(bios[bios["height_cm"] > 215])

print("\n4. Direct boolean indexing + selecting columns:")
print(bios[bios["height_cm"] > 215][["name", "height_cm"]])

# ============================
# 4. Multiple Conditions
# ============================
# Combine conditions with:
#   &  -> AND
#   |  -> OR
#   ~  -> NOT
print("\n5. Taller than 215 cm AND born in USA:")
print(bios[(bios["height_cm"] > 215) & (bios["born_country"] == "USA")])

print("\n6. Born in USA OR France:")
print(bios[(bios["born_country"] == "USA") | (bios["born_country"] == "FRA")])

print("\n7. NOT born in USA:")
print(bios[~(bios["born_country"] == "USA")])

# ============================
# 5. Using isin() for Multiple Matches
# ============================
print("\n8. Born in USA, France, or GBR (with isin):")
print(bios[bios["born_country"].isin(["USA", "FRA", "GBR"])])

# Combine isin() with another condition:
print("\n9. Born in USA/FRA/GBR AND name contains 'Keith':")
print(bios[bios["born_country"].isin(["USA", "FRA", "GBR"]) & bios["name"].str.contains("Keith", na=False)])

# ============================
# 6. String Filtering
# ============================
print("\n10. Names containing 'Keith':")
print(bios[bios["name"].str.contains("Keith", na=False)])

print("\n11. Names containing 'keith' (case-insensitive):")
print(bios[bios["name"].str.contains("keith", case=False, na=False)])

print("\n12. Names containing 'keith' OR 'patrick':")
print(bios[bios["name"].str.contains("keith|patrick", case=False, na=False)])

print("\n13. Names starting with 'K':")
print(bios[bios["name"].str.startswith("K", na=False)])

print("\n14. Names starting with K AND born in USA/FRA/GBR:")
print(bios[bios["name"].str.startswith("K", na=False) & bios["born_country"].isin(["USA","FRA","GBR"])])

# ============================
# 7. Advanced Regex Filtering
# ============================
print("\n15. Born in a city starting with a vowel:")
print(bios[bios["born_city"].str.contains(r"^[AEIOUaeiou]", na=False)])

print("\n16. Names with repeated consecutive letters (e.g., Aaron, Emmet):")
print(bios[bios["name"].str.contains(r"(.)\1", na=False)])

print("\n17. Names ending with 'son' or 'sen':")
print(bios[bios["name"].str.contains(r"(son|sen)$", case=False, na=False)])

print("\n18. Born in a year starting with 19 (1900s):")
print(bios[bios["born_date"].str.contains(r"^19", na=False)])

print("\n19. Names with NO vowels at all:")
print(bios[bios["name"].str.contains(r"^[^AEIOUaeiou]*$", na=False)])

print("\n20. Names containing a hyphen or apostrophe:")
print(bios[bios["name"].str.contains(r"[-']", na=False)])

print("\n21. Names that start and end with the same letter:")
print(bios[bios["name"].str.contains(r"^(.).*\1$", case=False, na=False)])

print("\n22. Born in a city with exactly 7 characters:")
print(bios[bios["born_city"].str.contains(r"^.{7}$", na=False)])

print("\n23. Names with 3 or more vowels:")
print(bios[bios["name"].str.contains(r"(.*[AEIOUaeiou].*){3,}", na=False)])

# Can disable regex to force exact string match
print("\n24. Regex disabled (exact string match only):")
print(bios[bios["name"].str.contains("keith|patrick", case=False, regex=False, na=False)])

# Using .query() to filter data in a cleaner way !!!!!

# Filter by country
test = bios.query("born_country == 'USA'")
print("Born in USA:\n", test)

# Filter by multiple conditions
test = bios.query(
    "born_country == 'USA' and born_city == 'Seattle'"
)
print("\nBorn in USA AND in Seattle:\n", test)

# Filter by died date
test = bios.query(
    "died_date < '1950'"
)
print("\nDied before 1950: \n", test)

# Filter by died date (Name and born date)
test = bios.query(
    "died_date < '1950'"
    ) [["name","born_date"]]
print("\nNames of athletes who died before 1950 (and the born date):\n", test)

# ============================
# Notes & Best Practices
# ============================
# ✅ df.loc[condition, columns]
#    - Best when filtering rows + selecting columns.
#    - Clean, efficient, avoids chained indexing warnings.
#
# ✅ df[condition]
#    - Simpler, concise.
#    - Returns ALL columns by default.
#    - To select columns, must chain another [].
#
# ✅ Multiple conditions:
#    - Wrap each condition in parentheses.
#    - Use & (AND), | (OR), ~ (NOT).
#
# ✅ String filtering:
#    - .str.contains("pattern") supports regex.
#    - .str.startswith("X") / .str.endswith("X") for quick checks.
#    - case=False → ignore capitalization.
#    - na=False → safely exclude NaN values.
#
# ✅ isin() for multiple matches:
#    df[df["col"].isin([list_of_values])]
#
# ✅ Combine conditions freely:
#    df[(cond1) & (cond2)]   → AND
#    df[(cond1) | (cond2)]   → OR
#    df[~(cond1)]            → NOT
#
# ============================
# Regex Cheat Sheet
# ============================
# ^        = Start of string
# $        = End of string
# .        = Any single character
# *        = 0 or more repetitions
# +        = 1 or more repetitions
# ?        = Optional (0 or 1 occurrence)
# []       = Character set (e.g. [aeiou] = any vowel)
# [^ ]     = Negated set (e.g. [^aeiou] = anything but vowels)
# |        = OR (choice between patterns)
# ()       = Grouping or capturing
# (.)      = Capture any single character
# \1       = Backreference (match same text as 1st group)
# {n}      = Exactly n times
# {n,}     = n or more times
# {n,m}    = Between n and m times
# r""      = Raw string (Python won’t treat \ as escape)
