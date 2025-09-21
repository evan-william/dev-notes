import numpy as np

"""
NUMPY ARRAY REORGANIZING & STACKING
"""

# ----------------------------------#
# 1. Original Array
before = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
print("1. Original Array:\n", before)


# ----------------------------------#
# 2. Reshape Arrays
# reshape(rows, columns) or higher dimensions
after1 = before.reshape((8, 1))   # Flatten into 8 rows, 1 column
after2 = before.reshape((4, 2))   # 4 rows, 2 columns
after3 = before.reshape((2, 2, 2))# 3D array: 2 blocks, 2 rows, 2 columns

print("\n2. Reshaped Arrays:")
print("Reshape to (8,1):\n", after1)
print("Reshape to (4,2):\n", after2)
print("Reshape to (2,2,2):\n", after3)


# ----------------------------------#
# 3. Flatten Arrays
flat1 = before.ravel()                   # Returns a *view* (modifies original if changed)
flat2 = before.flatten()                 # Returns a *copy* (independent of original)
flat3 = before.flatten(order="F")        # Column-major flatten (Fortran-style)
flat4 = before.flatten(order="C")        # Row-major order (C-style, default: flatten row by row).

print("\n3. Flatten Arrays:")
print("Using ravel():", flat1)
print("Using flatten():", flat2)
print("Using flatten(order='F'):", flat3)
print("Using flatten(order='C'):", flat4)

# ----------------------------------#
# 4. Transpose Arrays
print("\n4. Transpose Arrays:")
print("Transpose using .T:\n", before.T)
print("Transpose using np.transpose():\n", np.transpose(before))


# ----------------------------------#
# 5. Concatenate Arrays
c1 = np.array([[1, 2], [3, 4]])
c2 = np.array([[5, 6]])
print("\n5. Concatenate Arrays:")
print("Concatenate along rows (axis=0):\n", np.concatenate([c1, c2], axis=0))
print("Concatenate along columns (axis=1):\n", np.concatenate([c1, c1], axis=1))


# ----------------------------------#
# 6. Vertical Stacking (vstack)
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print("\n6. Vertical Stacking (vstack):")
print("Stack v1 and v2 vertically:\n", np.vstack([v1, v2]))
print("Stack v1, v2, v2 vertically:\n", np.vstack([v1, v2, v2]))


# ----------------------------------#
# 7. Horizontal Stacking (hstack)
h1 = np.ones((2, 4))   # 2 rows, 4 columns filled with 1
h2 = np.zeros((2, 2))  # 2 rows, 2 columns filled with 0

print("\n7. Horizontal Stacking (hstack):")
print("Stack h1 and h2 horizontally:\n", np.hstack([h1, h2]))


# ----------------------------------#
# 8. Splitting Arrays
s = np.array([1, 2, 3, 4, 5, 6])
print("\n8. Splitting Arrays:")
print("Original s:", s)
print("Split into 3 parts:", np.split(s, 3))
print("Split at [2,4]:", np.split(s, [2, 4])) # -> this is like split before index 2 , then split before index 4, then print thre rest equally


# ----------------------------------#
# Notes:
"""
1. reshape() → reorganizes array into new shape, total elements must match.
2. ravel()   → flatten as a *view* (linked to original).
3. flatten() → flatten as a *copy* (independent).
   - flatten(order='C') → Row-major (default).
   - flatten(order='F') → Column-major (Fortran style).
4. transpose() / .T → swap rows & columns (or higher-dim axes).
5. concatenate() → combine arrays along existing axis.
6. vstack()  → stack arrays vertically (row-wise).
7. hstack()  → stack arrays horizontally (column-wise).
8. split()   → split array into equal or custom-sized parts.
"""
