import numpy as np

"""
NUMPY 3D ARRAY: INDEXING, SLICING, AND REPLACING
"""

# ----------------------------------#
# 1. Define a 3D Array
a = np.array([[[1,2],[3,4]],
              [[5,6],[7,8]]])
print("1. Original 3D Array:\n", a)

# ----------------------------------#
# 2. Access Specific Elements (Indexing)
print("\n2. Access Specific Elements:")

# Access single element: [block, row, col]
print("Element at [0,1,1] =", a[0,1,1])  # 4
print("Element at [1,0,1] =", a[1,0,1])  # 6

# Access full row/column with slicing
print("Row at [0,1,:] =", a[0,1,:])      # [3 4]

# ----------------------------------#
# 3. Replace Specific Elements (Slicing)
print("\n3. Replace Elements via Slicing:")

# Current slice [:,1,:] -> all blocks, row 1, all columns
print("Current slice [:,1,:]:\n", a[:,1,:])

# Replace with same-shape array
a[:,1,:] = [[69,69],[69,69]]
print("After replacement [:,1,:] = [[69,69],[69,69]]:\n", a[:,1,:])

# Verify full array
print("\nUpdated 3D Array:\n", a)
