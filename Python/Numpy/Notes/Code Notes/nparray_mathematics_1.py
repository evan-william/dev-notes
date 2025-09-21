import numpy as np

# ===============================
# NUMPY: General Math Operations
# ===============================

# 1. Define the Array
print("Original Array = ", end="")
a = np.array([1, 2, 3, 4])
print(a)

# ----------------------------------#
# 2. Basic Arithmetic Operations
print("\nBasic Arithmetic Operations:")
print("Plus 2 = ", a + 2)
print("Minus 2 = ", a - 2)
print("Multiply 2 = ", a * 2)
print("Divide 2 = ", a / 2)
print("Power 2 = ", a ** 2)

# ----------------------------------#
# 3. Trigonometric Functions
print("\nTrigonometric Functions:")
print("Sin(a) = ", np.sin(a))
print("Cos(a) = ", np.cos(a))
print("Tan(a) = ", np.tan(a))

# ----------------------------------#
# 4. Exponential and Logarithmic Functions
print("\nExponential & Logarithmic Functions:")
print("Exp(a) = ", np.exp(a))
print("Log(a) = ", np.log(a))        # natural log
print("Log10(a) = ", np.log10(a))    # base 10 log

# ----------------------------------#
# 5. Element-wise Operations with Another Array (Operators)
print("\nAdding/Subtracting/Multiplying Two Arrays (Operators):")
anew = np.array([2, 3, 4, 5])
print("New Array = ", anew)
print("Original + New = ", a + anew)
print("Original - New = ", a - anew)
print("Original * New = ", a * anew)
print("Original / New = ", a / anew)

# ----------------------------------#
# 6. Element-wise Operations with Another Array (Functions)
print("\nAdding/Subtracting/Multiplying Two Arrays (Functions):")
print("np.add(a, anew)       =", np.add(a, anew))
print("np.subtract(a, anew)  =", np.subtract(a, anew))
print("np.multiply(a, anew)  =", np.multiply(a, anew))
print("np.divide(a, anew)    =", np.divide(a, anew))

# ----------------------------------#
# 7. Linear Algebra: Dot & Matmul
print("\nLinear Algebra Operations:")
b = np.array([10, 20, 30, 40])
print("Another Array b =", b)

# Dot product (1D vectors)
print("Dot product (a · b) =", np.dot(a, b))

# Matrix multiplication (2D)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Matrix Multiplication (A @ B) =\n", np.matmul(A, B))

# ----------------------------------#
# 8. Universal Functions (ufuncs)
print("\nUniversal Functions (ufuncs):")
print("Square Root = ", np.sqrt(a))
print("Absolute = ", np.abs(np.array([-1, -2, 3, -4])))
print("Ceil = ", np.ceil(np.array([1.2, 2.5, 3.7])))
print("Floor = ", np.floor(np.array([1.2, 2.5, 3.7])))
print("Round = ", np.round(np.array([1.2, 2.5, 3.7])))

# ----------------------------------#
# 9. Comparison Operators
print("\nComparison Operations:")
print("a > 2: ", a > 2)
print("a < 3: ", a < 3)
print("a == 2: ", a == 2)
print("a != 3: ", a != 3)
