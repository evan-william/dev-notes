import pandas as pd

"""
CONTINUATION OF df_data_1.py
Accessing Data (Loading & Saving DataFrames)
"""

# ============================
#  LOADING DATAFRAMES FROM FILES
# ============================

# Load from CSV
bios = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/data/bios.csv")

print("\nBelow is the Data of Bios: ")
print(bios.head())   # show first 5 rows

# ============================
#  SAVING DATAFRAMES TO FILES
# ============================
# Pandas allows saving into many formats:

# 1. Save to CSV
bios.to_csv("bios_saved.csv", index=False)  # index=False to avoid saving row numbers

# 2. Save to Excel
bios.to_excel("bios_saved.xlsx", index=False)

# 3. Save to JSON
bios.to_json("bios_saved.json", orient="records", lines=True)  # orient="records" = row-wise

# 4. Save to Parquet (efficient columnar storage)
bios.to_parquet("bios_saved.parquet", index=False)

# 5. Save to HTML (creates an HTML table)
bios.to_html("bios_saved.html", index=False)

# 6. Save to Clipboard (quick copy-paste into Excel/Sheets)
# bios.to_clipboard(index=False)

# ============================
#  NOTES
# ============================
# - Use index=False to avoid storing row indices unless needed.
# - Common formats:
#     * CSV → text-based, widely supported
#     * Excel → useful for business users
#     * JSON → good for web APIs & data exchange
#     * Parquet → optimized for big data, fast & compressed
#     * HTML → easy table export for web
# - `read_...` functions are paired with `to_...` (e.g., read_csv ↔ to_csv).
