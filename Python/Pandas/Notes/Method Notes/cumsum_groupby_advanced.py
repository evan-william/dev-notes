import pandas as pd

# ==================================================
# 1. CREATE DATAFRAME
# ==================================================
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
print("Original DataFrame:\n", df)

# ==================================================
# 2. IDENTIFY NON-ZERO SEQUENCES
# ==================================================
x = (df['X'] != 0).cumsum()
y = x != x.shift()

print("\nStep 1: x = cumulative count of non-zeros")
print(x)
print("\nStep 2: y = mark start of new sequences")
print(y)

# ==================================================
# 3. COUNT CONSECUTIVE NON-ZEROS WITH RESET AFTER ZERO
# ==================================================
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()

print("\nFinal DataFrame with Y (consecutive count):\n", df)

"""
💡 Step-by-Step Explanation

1️⃣ Identify Non-Zero Values
- df['X'] != 0 → Boolean Series (True for non-zero, False for zero)
  Example: [7,2,0,...] → [T,T,F,T,...]

2️⃣ Count Cumulative Non-Zeros
- x = (df['X'] != 0).cumsum()
- Treat True=1, False=0
- Running sum counts how many non-zeros appeared so far
  Example: [T,T,F,...] → [1,2,2,...]

3️⃣ Detect Start of New Sequence
- y = x != x.shift()
- Shift x down by 1 → compare current vs previous
- True = new sequence start, False = continuation
  Example: [1,2,2,...] → [T,T,F,...]

4️⃣ Group Consecutive Runs and Compute Cumulative Count
- group_ids = (y != y.shift()).cumsum()
- Splits rows into consecutive groups where sequence resets
- y.groupby(group_ids).cumsum() → cumulative count **within each group**
- Result: consecutive non-zero count, resets after zero
  Example Output:
      X  Y
  0   7  1
  1   2  2
  2   0  0
  3   3  1
  4   4  2
  5   2  3
  6   5  4
  7   0  0
  8   3  1
  9   4  2

✅ Key Points
- .cumsum() + groupby allows **conditional cumulative sums**
- group_ids determine where the count resets
- Useful for:
  • Counting sequences that reset under certain conditions
  • Event numbering
  • Conditional running totals
"""
