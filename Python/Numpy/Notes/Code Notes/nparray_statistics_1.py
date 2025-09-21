import numpy as np

# ----------------------------------#
# 1. Define a 2D Array
stats = np.array([[1, 2, 3],
                  [4, 5, 6]])
print("Original Stats Array:\n", stats)

# ----------------------------------#
# 2. Minimum and Maximum
print("\nMinimum and Maximum:")
print("Min of all elements =", np.min(stats))
print("Max of all elements =", np.max(stats))

# Minimum and Maximum along axes
print("Min along rows (axis=1) =", np.min(stats, axis=1))
print("Max along rows (axis=1) =", np.max(stats, axis=1))
print("Min along columns (axis=0) =", np.min(stats, axis=0))
print("Max along columns (axis=0) =", np.max(stats, axis=0))

# ----------------------------------#
# 3. Sum of Elements
print("\nSum of Elements:")
print("Sum of all elements =", np.sum(stats))
print("Sum along rows (axis=1) =", np.sum(stats, axis=1))
print("Sum along columns (axis=0) =", np.sum(stats, axis=0))

# ----------------------------------#
# 4. Mean
print("\nMean (Average):")
print("Mean of all elements =", np.mean(stats))
print("Mean along rows (axis=1) =", np.mean(stats, axis=1))
print("Mean along columns (axis=0) =", np.mean(stats, axis=0))

# ----------------------------------#
# 5. Median
print("\nMedian:")
print("Median of all elements =", np.median(stats))
print("Median along rows (axis=1) =", np.median(stats, axis=1))
print("Median along columns (axis=0) =", np.median(stats, axis=0))

# ----------------------------------#
# 6. Standard Deviation and Variance
print("\nStandard Deviation and Variance:")
print("Std of all elements =", np.std(stats))
print("Variance of all elements =", np.var(stats))
print("Std along rows (axis=1) =", np.std(stats, axis=1))
print("Std along columns (axis=0) =", np.std(stats, axis=0))
print("Variance along rows (axis=1) =", np.var(stats, axis=1))
print("Variance along columns (axis=0) =", np.var(stats, axis=0))
