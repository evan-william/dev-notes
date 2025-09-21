import numpy as np

"""
NUMPY ARRAY TYPES, DIMENSIONS, AND MEMORY
"""

# ----------------------------------#
# 1. Data Type Notes
"""
NumPy stores numbers efficiently using different integer types:

1. int16 → 16-bit integer → 2 bytes → range: -32,768 to +32,767
2. int32 → 32-bit integer → 4 bytes → range: -2,147,483,648 to +2,147,483,647
3. int64 → 64-bit integer → 8 bytes → range: -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807

For floats, the default dtype is float64 (8 bytes per element).
"""

# ----------------------------------#
# 2. Create 1D and 2D Arrays
a = np.array([3,3,4])
b = np.array([3,2,4])
b1 = np.array([2.1, 2.3])

print("1D Arrays:")
print("a =", a)
print("b =", b)
print("b1 (float) =", b1)

# 2D Array
a2 = np.array([[9.9,8.7,3.4],
               [3.4,6.2,9.1]])
print("\n2D Array:")
print(a2)

# Display with commas
print("\n2D Array with commas:")
print(np.array2string(a2, separator=', '))

# ----------------------------------#
# 3. Array Dimensions & Shape
print("\nArray Dimensions & Shape:")
print("a.ndim =", a.ndim)      # Number of dimensions
print("a.shape =", a.shape)    # Shape (1D → 3,)
print("a2.shape =", a2.shape)  # Shape (2D → 2x3)

# ----------------------------------#
# 4. Data Types & Memory
print("\nArray Data Types & Memory:")

# Default dtype
print("a.dtype =", a.dtype)
print("b1.dtype =", b1.dtype)

# Redefine dtype
ared = np.array([32767,2,3], dtype='int16')
print("ared dtype =", ared.dtype)

# Item size (bytes per element)
print("ared.itemsize =", ared.itemsize)
print("b1.itemsize =", b1.itemsize)

# Total number of elements
atest = np.array([1,2,3,4,5,6])
print("\nTotal elements:")
print("atest.size =", atest.size)
print("b1.size =", b1.size)

# Total memory size (bytes)
print("\nTotal size in bytes:")
print("atest:", atest.size * atest.itemsize)  # equivalent to atest.nbytes
print("b1:", b1.size * b1.itemsize)
