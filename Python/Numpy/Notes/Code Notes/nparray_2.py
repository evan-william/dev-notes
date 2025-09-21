import numpy as np

"""
NUMPY 2D ARRAY: ACCESSING & MODIFYING ELEMENTS
"""

# ----------------------------------#
# 1. Define a 2D Array
a = np.array([[1,2,3,4,5,6],
              [9,3,2,4,1,5]])
print("1. Original 2D Array:\n", a)

# ----------------------------------#
# 2. Access Specific Element
print("\n2. Access Specific Element [row, column]:")
print("Element at [1,4] =", a[1,4])  # 1

# ----------------------------------#
# 3. Access Entire Row
print("\n3. Access Entire Row:")
print("Row 1 (all elements) =", a[1, :])
print("Row 1 (from index 1 onwards) =", a[1, 1:])

# ----------------------------------#
# 4. Access Entire Column
print("\n4. Access Entire Column:")
print("Column 5 (all rows) =", a[:,5])

# ----------------------------------#
# 5. Access with Start, Stop, Step
print("\n5. Access with Start:Stop:Step:")
print("Row 1, elements 1 to 5 with step 2 =", a[1, 1:6:2])
print("Row 1, elements 0 to second-last with step 2 =", a[1, 0:-1:2])

# ----------------------------------#
# 6. Change a Single Element
print("\n6. Change Single Element:")
print("Original Array:\n", a)
a[1,5] = 999
print("Changed [1,5] to 999:\n", a)
a[1,5] = 5  # revert back

# ----------------------------------#
# 7. Change All Elements in a Column
print("\n7. Change Entire Column:")
print("Original Array:\n", a)
a[:,5] = 69
print("Changed [:,5] to 69:\n", a)

# ----------------------------------#
# 8. Change Column to Different Values
print("\n8. Change Column to Different Values:")
a[:,5] = [68,70]  # first row 68, second row 70
print("Changed [:,5] to [68,70]:\n", a)
