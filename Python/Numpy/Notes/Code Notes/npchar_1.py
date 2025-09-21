import numpy as np

# ----------------------------------#
# 1. String Concatenation
print("Concatenation Example:")
print(np.char.add(['hello', 'hi'], ['abc', 'xyz']))  # Element-wise string addition

# ----------------------------------#
# 2. String Multiplication & Centering
print("\nString Multiplication and Centering:")
print(np.char.multiply('Hello ', 3))                     # Repeat string 3 times
print(np.char.center('Hello ', 3))                       # Center in width=3
print(np.char.center('Hello', 20, fillchar='-'))         # Center in width=20 with '-'

# ----------------------------------#
# 3. Changing Case
print("\nChanging Case:")
print("Capitalize:", np.char.capitalize("hello world"))  # First letter uppercase
print("Title Case:", np.char.title("how are you doing")) # Each word starts with uppercase
print("Lowercase (array):", np.char.lower(["HELLO", "WORLD"]))
print("Lowercase (string):", np.char.lower("HELLO"))
print("Uppercase (array):", np.char.upper(["python", "data"]))
print("Uppercase (string):", np.char.upper("python is easy"))

# ----------------------------------#
# 4. Splitting Strings
print("\nSplitting Strings:")
print("Split by space:", np.char.split("are you coming to the party"))
print("Split by lines:", np.char.splitlines("hello\nhow are you?"))

# ----------------------------------#
# 5. Stripping Characters
print("\nStripping Characters:")
print(np.char.strip(["nina", "admin", "anaita"], 'a'))  # Removes 'a' from both ends

# ----------------------------------#
# 6. Joining Strings
print("\nJoining Strings:")
print(np.char.join([':', '-'], ['dmy', 'ymd']))  # Insert separators element-wise

# ----------------------------------#
# 7. Replacing Substrings
print("\nReplacing Substrings:")
print(np.char.replace('He is a good dancer', 'is', 'was'))  # Replace 'is' → 'was'
