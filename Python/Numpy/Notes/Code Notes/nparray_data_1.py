import numpy as np

# =======================================
# NUMPY: Reading Data, Advanced Indexing, Data Generation & Handling Missing Values
# =======================================

# ---------------------------------------
# 1. Reading CSV/TXT Data
# ---------------------------------------
# np.loadtxt()  -> simple loading (uniform types, no missing values)
# np.genfromtxt() -> flexible (handles missing values, headers, etc.)

data = np.genfromtxt(
    r"D:\College\Programming Files\Codes\ML Engineer\Numpy\Notes\Code Notes\sample_data.txt",
    delimiter=","
)
print("Data (float by default):\n", data)

data_int = data.astype(int)
print("\nData converted to int:\n", data_int)

# Handling missing values
data_missing = np.genfromtxt(
    r"D:\College\Programming Files\Codes\ML Engineer\Numpy\Notes\Code Notes\sample_data_missing.txt",
    delimiter=",",
    filling_values=-1
)
print("\nData with missing values filled:\n", data_missing)


# ---------------------------------------
# 2. Saving & Loading NumPy Binary Files
# ---------------------------------------
np.save("my_array.npy", data)
loaded_arr = np.load("my_array.npy")
print("\nLoaded array from .npy file:\n", loaded_arr)


# ---------------------------------------
# 3. Boolean Masking & Advanced Indexing
# ---------------------------------------
mask = data > 50
print("\nBoolean mask (data > 50):\n", mask)

values_gt50 = data[mask]
print("\nValues greater than 50:\n", values_gt50)

rows, cols = np.where(data > 50)
print("\nIndices where data > 50:\nRows:", rows, "\nCols:", cols)

extracted_values = data[rows, cols]
print("\nExtracted values using advanced indexing:\n", extracted_values)

mask2 = (data > 20) & (data < 60)
print("\nValues between 20 and 60:\n", data[mask2])

mask_not = ~((data > 20) & (data < 60))
print("\nValues NOT between 20 and 60:\n", data[mask_not])


# ---------------------------------------
# 4. Indexing with Lists (Fancy Indexing)
# ---------------------------------------
x = np.array([1,2,3,4,5,6,7,8,9])
print("\nOriginal Array x:", x)
print("Elements at indices [1,2,8]:", x[[1,2,8]])


# ---------------------------------------
# 5. np.any() and np.all() with axis
# ---------------------------------------
any_gt50_axis0 = np.any(data > 50, axis=0)
print("\nAny element > 50 along each column:", any_gt50_axis0)

all_gt50_axis0 = np.all(data > 50, axis=0)
print("All elements > 50 along each column:", all_gt50_axis0)


# ---------------------------------------
# 6. Generating Data
# ---------------------------------------
a1 = np.arange(0, 10, 2)
print("\nnp.arange(0,10,2):", a1)

a2 = np.linspace(0, 1, 5)
print("np.linspace(0,1,5):", a2)

a3 = np.logspace(1, 3, 3)
print("np.logspace(1,3,3):", a3)

rand_uniform = np.random.rand(5)
rand_normal = np.random.randn(5)
rand_int = np.random.randint(0,10,5)
print("\nRandom uniform:", rand_uniform)
print("Random normal:", rand_normal)
print("Random integers:", rand_int)


# ---------------------------------------
# 7. Handling Missing Values in Arrays
# ---------------------------------------
# Create random 10x10 array
Z = np.random.rand(10,10)

# Randomly assign NaN to 5 elements
Z[np.random.randint(10, size=5), np.random.randint(10, size=5)] = np.nan
print("\nArray with missing values:\n", Z)

# Total number of missing values
total_missing = np.isnan(Z).sum()
print("\nTotal number of missing values:", total_missing)

# Indexes of missing values
indexes_missing = np.argwhere(np.isnan(Z))
print("\nIndexes of missing values:\n", indexes_missing)

# Another way to get indexes
inds = np.where(np.isnan(Z))
print("\nIndexes using np.where:", inds)

# Fill missing values with 0
Z[inds] = 0
print("\nArray after filling missing values with 0:\n", Z)


# ---------------------------------------
# Notes:
"""
1. np.isnan(array) -> Boolean array where True indicates NaN.
2. np.argwhere(array) -> returns coordinates of True elements (useful for NaNs).
3. np.where(condition) -> returns tuple of arrays (row indices, column indices).
4. Filling missing values:
   - Z[np.isnan(Z)] = value
5. Boolean masking & fancy indexing are useful for handling missing or filtered data.
6. Random data generation:
   - np.random.rand() → uniform [0,1)
   - np.random.randn() → normal distribution
   - np.random.randint(low, high, size) → random integers
"""
