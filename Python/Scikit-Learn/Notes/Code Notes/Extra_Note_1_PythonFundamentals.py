"""
=================================================================
PYTHON FUNDAMENTALS - Comprehensive Guide with Examples
=================================================================

This file covers essential Python fundamentals including:
- Statistics calculations (variance, standard deviation, range)
- List manipulation (comprehensions, filtering)
- Core data operations
"""

import math
import statistics

# =================================================================
# 1. STANDARD DEVIATION FROM VARIANCE
# =================================================================
print("=" * 60)
print("1. CALCULATING STANDARD DEVIATION FROM VARIANCE")
print("=" * 60)

# The standard deviation is the square root of variance
# Variance measures how spread out numbers are from their mean
variance = 25
standard_deviation = math.sqrt(variance)

print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")
print("\nExplanation: If variance = 25, then std dev = √25 = 5")


# =================================================================
# 2. SAMPLE VARIANCE CALCULATION
# =================================================================
print("\n" + "=" * 60)
print("2. CALCULATING SAMPLE VARIANCE")
print("=" * 60)

# Sample variance measures variability in a dataset
data = [12, 15, 18, 20, 22, 25, 28, 30]
sample_var = statistics.variance(data)

print(f"Data: {data}")
print(f"Sample Variance: {sample_var:.2f}")
print(f"Standard Deviation: {math.sqrt(sample_var):.2f}")
print("\nNote: Sample variance uses n-1 denominator (Bessel's correction)")


# =================================================================
# 3. LIST COMPREHENSION
# =================================================================
print("\n" + "=" * 60)
print("3. LIST COMPREHENSION - FILTERING DATA")
print("=" * 60)

# List comprehension: concise way to create filtered/transformed lists
my_list = [10, 12, 15, 18, 20, 22, 25, 30, 8, 5]

# Filter numbers >= 15
filtered_list = [num for num in my_list if num >= 15]

print(f"Original list: {my_list}")
print(f"Numbers >= 15: {filtered_list}")

# More examples
squared_numbers = [num**2 for num in my_list]
even_numbers = [num for num in my_list if num % 2 == 0]

print(f"Squared numbers: {squared_numbers}")
print(f"Even numbers: {even_numbers}")


# =================================================================
# 4. FILTER() FUNCTION WITH LAMBDA
# =================================================================
print("\n" + "=" * 60)
print("4. FILTER() FUNCTION WITH LAMBDA")
print("=" * 60)

# Alternative to list comprehension using filter() and lambda
my_list = [10, 12, 15, 18, 20, 22, 25, 30, 8, 5]

# Lambda is an anonymous function: lambda argument: expression
filtered_with_lambda = list(filter(lambda x: x >= 15, my_list))

print(f"Original list: {my_list}")
print(f"Filtered (>= 15): {filtered_with_lambda}")

# More lambda examples
greater_than_20 = list(filter(lambda x: x > 20, my_list))
divisible_by_5 = list(filter(lambda x: x % 5 == 0, my_list))

print(f"Greater than 20: {greater_than_20}")
print(f"Divisible by 5: {divisible_by_5}")

print("\nComparison:")
print("List comprehension: [num for num in my_list if num >= 15]")
print("Filter + lambda:    list(filter(lambda x: x >= 15, my_list))")


# =================================================================
# 5. APPEND() METHOD
# =================================================================
print("\n" + "=" * 60)
print("5. ADDING ITEMS TO A LIST WITH APPEND()")
print("=" * 60)

# .append() adds an item to the end of a list
fruits = ['apple', 'banana', 'orange']
print(f"Original list: {fruits}")

fruits.append('grape')
print(f"After append('grape'): {fruits}")

fruits.append('mango')
print(f"After append('mango'): {fruits}")

# Append is in-place (modifies the original list)
# Other list methods:
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])  # Adds multiple items
numbers.insert(0, 0)  # Insert at specific position
print(f"\nExtend and insert example: {numbers}")


# =================================================================
# 6. STATISTICAL RANGE
# =================================================================
print("\n" + "=" * 60)
print("6. CALCULATING STATISTICAL RANGE")
print("=" * 60)

# Range = Maximum value - Minimum value
# Measures the spread of data
data = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40]

data_range = max(data) - min(data)

print(f"Data: {data}")
print(f"Minimum: {min(data)}")
print(f"Maximum: {max(data)}")
print(f"Range: {data_range}")

# Using numpy (if available)
try:
    import numpy as np
    data_array = np.array(data)
    range_numpy = data_array.max() - data_array.min()
    print(f"\nUsing NumPy: {range_numpy}")
except ImportError:
    print("\nNumPy not available for this example")


# =================================================================
# 7. CONTROL FLOW - CONTINUE AND BREAK
# =================================================================
print("\n" + "=" * 60)
print("7. CONTROL FLOW: CONTINUE AND BREAK")
print("=" * 60)

# CONTINUE: Skip rest of current iteration
print("Using CONTINUE (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}", end=" ")

print("\n\nUsing BREAK (stop at 5):")
for i in range(10):
    if i == 5:
        break  # Exit loop entirely
    print(f"  {i}", end=" ")


# =================================================================
# 8. WHILE LOOP
# =================================================================
print("\n\n" + "=" * 60)
print("8. WHILE LOOP - REPEAT UNTIL CONDITION IS FALSE")
print("=" * 60)

# While loop: executes as long as condition is true
count = 0
print("Counting to 5:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# Practical example: process until threshold
total = 0
numbers_to_add = [5, 10, 15, 20, 25, 30]
i = 0
print("\nAdding numbers until total exceeds 40:")
while total <= 40 and i < len(numbers_to_add):
    total += numbers_to_add[i]
    print(f"  Added {numbers_to_add[i]}, Total: {total}")
    i += 1


# =================================================================
# 9. FOR LOOP
# =================================================================
print("\n" + "=" * 60)
print("9. FOR LOOP - ITERATE OVER SEQUENCES")
print("=" * 60)

# For loop: iterate over sequences (lists, strings, dicts)
fruits = ['apple', 'banana', 'cherry']
print("Iterating over list:")
for fruit in fruits:
    print(f"  {fruit}")

# Iterate over string
print("\nIterating over string:")
for char in "Python":
    print(f"  {char}", end=" ")

# Iterate over dictionary
print("\n\nIterating over dictionary:")
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
for name, score in scores.items():
    print(f"  {name}: {score}")


# =================================================================
# 10. IF-ELSE STRUCTURE
# =================================================================
print("\n" + "=" * 60)
print("10. IF-ELSE CONDITIONAL STATEMENTS")
print("=" * 60)

# If-else: execute different code based on conditions
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's pleasant outside!")
else:
    print("It's cold outside!")

# Nested conditions and multiple checks
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"\nScore: {score}, Grade: {grade}")


# =================================================================
# SUMMARY AND PRACTICE EXERCISES
# =================================================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Concepts Covered:
1. Statistics: variance → std dev (√variance), sample variance
2. List comprehensions: [x for x in list if condition]
3. Filter + lambda: filter(lambda x: condition, list)
4. List methods: .append(), .extend(), .insert()
5. Range calculation: max - min
6. Control flow: continue, break, while, for, if-else

Practice Exercise:
- Create a list of 20 random numbers
- Calculate mean, variance, and standard deviation
- Filter numbers above the mean
- Use both list comprehension and filter()
- Compare the results
""")

print("\n" + "=" * 60)
print("END OF PYTHON FUNDAMENTALS")
print("=" * 60)