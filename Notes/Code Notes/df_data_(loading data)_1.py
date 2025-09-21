import pandas as pd

"""
PANDAS FILE I/O: READING & WRITING DATA
"""

# ----------------------------------#
# 1. Reading CSV Files
# ----------------------------------#
coffee = pd.read_csv(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\warmup-data\coffee.csv"
)
print("Coffee Data (head):")
print(coffee.head())  # -> can use display() in Jupyter

# ----------------------------------#
# 2. Reading Parquet Files
# ----------------------------------#
results = pd.read_parquet(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\data\results.parquet"
)
print("\nResults Data (head):")
print(results.head())

# ----------------------------------#
# 3. Reading Excel Files (.xlsx)
# ----------------------------------#
olympics_data = pd.read_excel(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\data\olympics-data.xlsx"
)
print("\nOlympics Data (default sheet, head):")
print(olympics_data.head())

# ----------------------------------#
# 4. Reading Excel with Specific Sheet
# ----------------------------------#
olympics_data_sheet = pd.read_excel(
    r"D:\College\Programming Files\Codes\ML Engineer\Pandas\Notes\Code Notes\data\olympics-data.xlsx",
    sheet_name="results"
)
print("\nOlympics Data - Sheet 'results' (head):")
print(olympics_data_sheet.head())

# ----------------------------------#
# 5. Writing to CSV, Excel, Parquet
# ----------------------------------#
coffee.to_csv("coffee_copy.csv", index=False)
print("\nExported to coffee_copy.csv")

results.to_parquet("results_copy.parquet", index=False)
print("Exported to results_copy.parquet")

olympics_data.to_excel("olympics_copy.xlsx", index=False, sheet_name="data")
print("Exported to olympics_copy.xlsx")

# ----------------------------------#
# 6. Sampling Data
# ----------------------------------#
print("\n6. Sampling Data from Coffee DataFrame:")

print("\nSingle random row:")
print(coffee.sample())

print("\n10 random rows:")
print(coffee.sample(10))

print("\n20% of the data (random fraction):")
print(coffee.sample(frac=0.2)) # -> showing fractions of the data, 0,2 means showing 20% of the data

print("\n5 reproducible random rows (random_state=42):")
print(coffee.sample(n=5, random_state=42)) # -> set sseed to always show same random result
                                           # -> the n=5 shows 5 rows

# ----------------------------------#
# 7. Reading Other Formats (Examples)
# ----------------------------------#
# JSON
# json_data = pd.read_json("data.json")
# print("JSON Data (head):\n", json_data.head())

# Feather
# feather_data = pd.read_feather("data.feather")

# Pickle
# pickle_data = pd.read_pickle("data.pkl")

# SQL (requires a connection, e.g., sqlite3/SQLAlchemy)
# sql_data = pd.read_sql("SELECT * FROM table_name", con=connection)

# ----------------------------------#
# 8. Useful Parameters for Reading
# ----------------------------------#
# pd.read_csv("file.csv", delimiter=";", header=None, names=["Col1","Col2"])
# pd.read_excel("file.xlsx", sheet_name=["Sheet1","Sheet2"])  # load multiple sheets
# pd.read_csv("file.csv", usecols=["Col1","Col3"])            # load selected columns
# pd.read_csv("file.csv", nrows=100)                         # load only first 100 rows
# pd.read_csv("file.csv", skiprows=5)                        # skip first 5 rows
# pd.read_csv("file.csv", dtype={"Col1": str})               # specify column type
# pd.read_csv("file.csv", parse_dates=["date_column"])       # parse dates
