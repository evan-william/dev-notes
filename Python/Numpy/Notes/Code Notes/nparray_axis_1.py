import numpy as np

"""
NUMPY AXIS EXPLANATION
"""

# ----------------------------------#
# 1. Define a 2D Array
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print("1. Original 2D Array:\n", a)

# ----------------------------------#
# 2. Sum Example
print("\n2. Sum Example:")
print("Sum along axis=0 (down columns) =", np.sum(a, axis=0))
print("Sum along axis=1 (across rows)  =", np.sum(a, axis=1))

# Visualization:
# Axis=0 (column-wise sum): [1+4, 2+5, 3+6] = [5, 7, 9]
# Axis=1 (row-wise sum):    [1+2+3, 4+5+6] = [6, 15]

# ----------------------------------#
# 3. Max / Min Example
print("\n3. Max / Min Example:")
print("Max along axis=0 (columns) =", np.max(a, axis=0))
print("Max along axis=1 (rows)    =", np.max(a, axis=1))
print("Min along axis=0 (columns) =", np.min(a, axis=0))
print("Min along axis=1 (rows)    =", np.min(a, axis=1))

# ----------------------------------#
# 4. 3D Array Example
b = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print("\n4. Original 3D Array:\n", b)
print("Shape:", b.shape)  # (blocks, rows, columns) = (2, 2, 2)

# ----------------------------------#
# 5. Sum Along Different Axes in 3D
print("\n5. Sum Along Different Axes:")
print("Sum along axis=0 (combine blocks):\n", np.sum(b, axis=0))
print("Sum along axis=1 (combine rows inside block):\n", np.sum(b, axis=1))
print("Sum along axis=2 (combine columns inside block):\n", np.sum(b, axis=2))

# Visualization Notes:
# Axis=0 -> combine along blocks (vertical stacking)
# Axis=1 -> combine rows inside each block
# Axis=2 -> combine columns inside each row of a block

# ----------------------------------#
# 6. Rollaxis Example
c = np.ones((2, 3, 4))  # Shape = (depth=2, rows=3, cols=4)
print("\n6. Rollaxis Example:")
print("Original shape of c:", c.shape)

rolled = np.rollaxis(c, 2, 1)  
print("Shape after np.rollaxis(c, 2, 1):", rolled.shape)

# Explanation:
# Original c shape: (2, 3, 4)
# Axis indices:     0=depth, 1=rows, 2=columns
# np.rollaxis(c, 2, 1) → take axis=2 (columns) and insert it BEFORE axis=1
# New order of axes: (0=depth, 2=columns, 1=rows) → shape becomes (2, 4, 3)

# ----------------------------------#
# 7. Key Takeaways
"""
1. axis=0 → operate down the rows (affects columns)
2. axis=1 → operate across the columns (affects rows)
3. Higher dimensions → axis number increases with depth
4. Think: "Along which direction do I want to combine or operate?"
5. np.rollaxis(arr, source, destination) → moves the `source` axis before `destination`.
   Example: np.rollaxis(c, 2, 1)
   - Original shape (2, 3, 4) → (depth=2, rows=3, cols=4)
   - Moves axis=2 (cols) before axis=1 (rows)
   - Resulting shape: (2, 4, 3)
"""
