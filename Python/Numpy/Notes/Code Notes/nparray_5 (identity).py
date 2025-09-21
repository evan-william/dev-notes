import numpy as np

"""
NUMPY ARRAYS: SLICING, REPEATING, RANGES, COPYING, AND ITERATION
"""

# ----------------------------------#
# 1. Slicing Rule
print("1. Slicing Rule")
print("Syntax: start:stop:step -> start from 'start', stop before 'stop'\n")

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("arr[1:4] =", arr[1:4])
print("arr[:3] =", arr[:3])
print("arr[::2] =", arr[::2])

# ----------------------------------#
# 1a. Slicing Using slice()
s = slice(1, 4)
print("\nUsing slice(1,4):", arr[s])

s2 = slice(None, 4, 2)
print("Using slice(None,4,2):", arr[s2])

s3 = slice(-1, -6, -2)
print("Using slice(-1,-6,-2):", arr[s3])

start, stop, step = 0, 5, 2
dynamic_slice = slice(start, stop, step)
print("Dynamic slice using variables:", arr[dynamic_slice])

# ----------------------------------#
# 2. Array Ranges
print("\n2. Array Ranges")
print("np.arange(0, 10, 2):", np.arange(0, 10, 2))
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

# ----------------------------------#
# 3. Identity Matrix
print("\n3. Identity Matrix:")
print("np.eye(5):\n", np.eye(5))
print("np.identity(5):\n", np.identity(5))

# ----------------------------------#
# 4. Repeating Arrays
a1 = np.array([1,2,3])
r1 = np.repeat(a1, 10)
print("\n1D Array Repeated:\n", r1)

a2 = np.array([[1,2,3]])
r2 = np.repeat(a2, 5, axis=0)
print("\n2D Array Repeated along axis 0:\n", r2)

# ----------------------------------#
# 4a. Iterating Arrays using np.nditer
arr2d = np.array([[1,2,3],[4,5,6]])
print("\nOriginal 2D Array:\n", arr2d)

# C-order iteration (row-major, left-to-right)
print("\nC-order iteration (row-wise):")
for x in np.nditer(arr2d, order='C'):
    print(x, end=" ")
print()

# F-order iteration (column-major, top-to-bottom)
print("\nF-order iteration (column-wise):")
for x in np.nditer(arr2d, order='F'):
    print(x, end=" ")
print()

# Visualization:
print("\nVisualization:")
print("Row-wise (C-order): 1 2 3 | 4 5 6")
print("Column-wise (F-order): 1 4 | 2 5 | 3 6")

# ----------------------------------#
# 5. 2D Array with Alternating 0s and 1s -> remember [r,c]
print("\n5. Alternating 0-1 6x6 Array")
Z = np.zeros((6,6), dtype=int)
Z[1::2, ::2] = 1  # odd rows, even columns
Z[::2, 1::2] = 1  # even rows, odd columns
print(Z)

# Notes:
# Even rows: 0,2,4 → fill 1 in odd columns (1,3,5)
# Odd rows: 1,3,5  → fill 1 in even columns (0,2,4)
# Pattern:
# [[0 1 0 1 0 1]
#  [1 0 1 0 1 0]
#  [0 1 0 1 0 1]
#  [1 0 1 0 1 0]
#  [0 1 0 1 0 1]
#  [1 0 1 0 1 0]]

# ----------------------------------#
# 6. Coding Challenge: Insert Matrix
output = np.ones((5,5))
zeros = np.zeros((3,3))
zeros[1,1] = 9
output[1:4,1:4] = zeros
print("\nCombined 5x5 Matrix:\n", output)

# ----------------------------------#
# 7. Copying Arrays Correctly
a = np.array([1,2,3])
b = a
b[0] = 100
print("\nWrong Copying (a is affected):\n", a)

a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print("Good Copying (a unchanged, b modified):\n", b)

# ----------------------------------#
# Notes:
"""
1. Slicing → arr[start:stop:step] or arr[slice_obj]
2. np.arange(start, stop, step) → numbers with step.
3. np.linspace(start, stop, num) → evenly spaced values.
4. np.eye(n) / np.identity(n) → identity matrix.
5. np.repeat(array, n) → repeat elements.
6. np.nditer(array, order='C'/'F') → iterate element-wise.
   - C-order: row-wise, left-to-right across rows.
   - F-order: column-wise, top-to-bottom down columns.
7. Alternating 0-1 pattern in 2D array:
   - Z[1::2, ::2] = 1 → odd rows, even columns
   - Z[::2, 1::2] = 1 → even rows, odd columns
8. Use copy() to avoid accidental modifications.
"""

