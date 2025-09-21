import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
                'Budapest_PaRis', 'Brussels_londOn'],
    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
                '12. Air France', '"Swiss Air"']
})

# Split into From and To for demonstration
temp = df['From_To'].str.split('_', expand=True)
temp.columns = ['From', 'To']

print("Original temp DataFrame:\n", temp, "\n")


"""
PANDAS STRING MANIPULATION METHODS
"""

# ----------------------------------#
# 1. Capitalize (First letter upper, rest lower)
temp_cap = temp.copy()
temp_cap['From'] = temp_cap['From'].str.capitalize()
temp_cap['To'] = temp_cap['To'].str.capitalize()
print("1. Capitalize (first letter uppercase):\n", temp_cap, "\n")

# ----------------------------------#
# 2. Lowercase All Letters
temp_lower = temp.copy()
temp_lower['From'] = temp_lower['From'].str.lower()
temp_lower['To'] = temp_lower['To'].str.lower()
print("2. Lowercase all letters:\n", temp_lower, "\n")

# ----------------------------------#
# 3. Uppercase All Letters
temp_upper = temp.copy()
temp_upper['From'] = temp_upper['From'].str.upper()
temp_upper['To'] = temp_upper['To'].str.upper()
print("3. Uppercase all letters:\n", temp_upper, "\n")

# ----------------------------------#
# 4. Title Case (Each Word’s First Letter Upper)
temp_title = temp.copy()
temp_title['From'] = temp_title['From'].str.title()
temp_title['To'] = temp_title['To'].str.title()
print("4. Title Case:\n", temp_title, "\n")

# ----------------------------------#
# 5. Swapcase (Upper → Lower, Lower → Upper)
temp_swap = temp.copy()
temp_swap['From'] = temp_swap['From'].str.swapcase()
temp_swap['To'] = temp_swap['To'].str.swapcase()
print("5. Swapcase:\n", temp_swap, "\n")

# ----------------------------------#
# 6. Strip Spaces (Leading & Trailing)
temp_strip = pd.DataFrame({
    "City": ["  London ", " Paris  ", "  Milan  "]
})
temp_strip['City_Stripped'] = temp_strip['City'].str.strip()
print("6. Strip spaces:\n", temp_strip, "\n")

# ----------------------------------#
# 7. Replace Characters / Substrings
temp_replace = temp.copy()
temp_replace['From'] = temp_replace['From'].str.replace("o", "0", regex=False)
temp_replace['To'] = temp_replace['To'].str.replace("i", "1", regex=False)
print("7. Replace characters:\n", temp_replace, "\n")

# ----------------------------------#
# 8. Remove Non-Alphabetic Characters
temp_clean = df['Airline'].str.replace(r'[^A-Za-z\s]', '', regex=True)
print("8. Remove non-alphabetic characters (Airline column):\n", temp_clean, "\n")

# ----------------------------------#
# 9. Check String Properties
print("9. String property checks:")
print("Is 'From' alphabetic?:\n", temp['From'].str.isalpha())
print("Is 'To' lower?:\n", temp['To'].str.islower())
print("Is 'From' upper?:\n", temp['From'].str.isupper(), "\n")

# ----------------------------------#
# 10. Summary of String Manipulation
print("10. Summary of Methods Covered:")
print("""
1. str.capitalize() → First letter uppercase, rest lowercase
2. str.lower()      → All lowercase
3. str.upper()      → All uppercase
4. str.title()      → Each word's first letter uppercase
5. str.swapcase()   → Swap upper/lower
6. str.strip()      → Remove leading/trailing spaces
7. str.replace()    → Replace substring/characters
8. Regex cleaning   → Remove unwanted characters
9. str.isalpha(), str.islower(), str.isupper() → Boolean checks
""")
