import numpy as np

"""
NUMPY ARRAY INITIALIZATION & PROPERTIES
"""

# ----------------------------------#
# 1. Array Dimensions Reference
"""
1D = Single Line
2D = Rows, Columns
3D = Depth, Rows, Columns
4D = Batch, Depth, Rows, Columns
"""

# ----------------------------------#
# 2. Initialize All Zeros
print("2. Initialize Arrays with Zeros")
print("1D zeros:", np.zeros(5))
print("2D zeros (2x3):\n", np.zeros((2,3)))
print("3D zeros (2x3x3):\n", np.zeros((2,3,3)))
print("4D zeros (2x3x3x4):\n", np.zeros((2,3,3,4)))  # 2 blocks, each with 3x3x4

# ----------------------------------#
# 3. Initialize All Ones
print("\n3. Initialize Arrays with Ones (3D example, int32)")
ones_3d = np.ones((4,2,2), dtype='int32')
print(ones_3d)

# Array Properties
print("\nArray Properties:")
print("Item size (byte) =", ones_3d.itemsize)
print("Number of elements =", ones_3d.size)
print("Total bytes =", ones_3d.nbytes)
print("Data type =", ones_3d.dtype)

# ----------------------------------#
# 4. Initialize Any Number
print("\n4. Initialize Arrays with Any Number")
b1 = np.full((2,2), 69)
print("2D Array filled with 69:\n", b1)

# Using shape of existing array
b2 = np.full(ones_3d.shape, 100)  # or np.full_like(ones_3d, 100)
print("\n3D Array filled with 100, same shape as ones_3d:\n", b2)

# ----------------------------------#
# 5. Random Decimal Numbers
print("\n5. Random Decimal Numbers")
b3 = np.random.rand(4,3)  # uniform [0,1), shape 4x3
print("Random 4x3 decimals:\n", b3)

b4 = np.random.random_sample(ones_3d.shape)  # same shape as ones_3d
print("\nRandom decimals with shape of ones_3d:\n", b4)

# ----------------------------------#
# 6. Random Integers
print("\n6. Random Integers")
b5 = np.random.randint(9)  # single integer [0,9)
print("Single random integer [0,9):", b5)

b6 = np.random.randint(10, size=(3,3))  # 3x3 matrix integers [0,10)
print("\nRandom 3x3 integers [0,10):\n", b6)

b7 = np.random.randint(-2, 10, size=(4,1))  # 4x1 matrix [-2,10)
print("\nRandom 4x1 integers [-2,10):\n", b7)
