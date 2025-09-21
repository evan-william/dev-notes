import numpy as np

"""
LINEAR ALGEBRA BASIC RULES & EXAMPLES

C = A x B

shape(A) = (m,n), shape(B) = (p,q)
shape(C) = (rows of A, columns of B)
"""

# ----------------------------------#
# 1. Matrix Multiplication
print("1. Matrix Multiplication Example")
a = np.ones((2,3))
b = np.full((3,2), 2)
print("Matrix A:\n", a)
print("Matrix B:\n", b)
c = np.matmul(a,b)
print("A x B =\n", c)  # shape (2,2)
print("-"*50)

# ----------------------------------#
# 2. Determinant
print("2. Determinant Example")
d = np.array([[1,2,3],
              [0,1,4],
              [5,6,0]])
print("Matrix D:\n", d)
det_d = np.linalg.det(d)
print("det(D) =", det_d)
print("-"*50)

# ----------------------------------#
# 3. Identity Matrix
print("3. Identity Matrix Example")
I = np.identity(3)
print("Identity Matrix 3x3:\n", I)
print("-"*50)

# ----------------------------------#
# 4. Matrix Inverse
print("4. Matrix Inverse Example")
# Must be square and non-singular
A_inv = np.linalg.inv(d)
print("Inverse of D:\n", A_inv)
# Verify: D x D_inv = Identity
print("D x D_inv =\n", np.matmul(d, A_inv))
print("-"*50)

# ----------------------------------#
# 5. Eigenvalues and Eigenvectors
print("5. Eigenvalues & Eigenvectors Example")
eig_vals, eig_vecs = np.linalg.eig(np.array([[4, -2],
                                             [1, 1]]))
print("Eigenvalues:\n", eig_vals)
print("Eigenvectors:\n", eig_vecs)
print("-"*50)

# ----------------------------------#
# 6. Matrix Norm
print("6. Matrix Norm Example")
M = np.array([[1,2],
              [3,4]])
norm_fro = np.linalg.norm(M)   # default = Frobenius norm
print("Matrix M:\n", M)
print("Frobenius Norm ||M|| =", norm_fro)
print("-"*50)

# ----------------------------------#
# 7. Trace
print("7. Trace Example")
trace_M = np.trace(M)
print("Trace of M =", trace_M)
print("-"*50)

# ----------------------------------#
# 8. Singular Value Decomposition (SVD)
print("8. SVD Example")
U, S, Vh = np.linalg.svd(M)
print("Matrix M:\n", M)
print("U:\n", U)
print("Singular Values S:\n", S)
print("Vh (V transposed):\n", Vh)
print("-"*50)
