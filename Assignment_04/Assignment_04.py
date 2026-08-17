import numpy as np
import numpy.ma as ma

# Set seed for reproducible random outputs
np.random.seed(42)

# ==========================================
# Assignment 1: Array Creation and Manipulation
# ==========================================
print("=== Assignment 1 ===")
# 1. Shape (5,5) random ints 1-20, replace 3rd column (index 2) with 1
a1_1 = np.random.randint(1, 21, size=(5, 5))
a1_1[:, 2] = 1
print("1. Replaced 3rd column with 1:\n", a1_1)

# 2. Shape (4,4) 1-16, diagonal elements set to 0
a1_2 = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(a1_2, 0)
print("2. Diagonal set to 0:\n", a1_2)

# ==========================================
# Assignment 2: Array Indexing and Slicing
# ==========================================
print("\n=== Assignment 2 ===")
# 1. Shape (6,6) 1-36, extract 3rd-5th rows (idx 2:5) & 2nd-4th cols (idx 1:4)
a2_1 = np.arange(1, 37).reshape(6, 6)
sub_array = a2_1[2:5, 1:4]
print("1. Sub-array (rows 3-5, cols 2-4):\n", sub_array)

# 2. Shape (5,5) random ints, extract border elements
a2_2 = np.random.randint(1, 20, size=(5, 5))
border = np.concatenate(
    [a2_2[0, :], a2_2[-1, :], a2_2[1:-1, 0], a2_2[1:-1, -1]]
)
print("2. Original Array:\n", a2_2)
print("   Border Elements:", border)

# ==========================================
# Assignment 3: Array Operations
# ==========================================
print("\n=== Assignment 3 ===")
arr_a = np.random.randint(1, 10, size=(3, 4))
arr_b = np.random.randint(1, 10, size=(3, 4))
print("1. Element-wise operations:")
print("   Addition:\n", arr_a + arr_b)
print("   Subtraction:\n", arr_a - arr_b)
print("   Multiplication:\n", arr_a * arr_b)
print("   Division:\n", np.round(arr_a / arr_b, 2))

a3_2 = np.arange(1, 17).reshape(4, 4)
print("2. Row-wise sum:", np.sum(a3_2, axis=1))
print("   Column-wise sum:", np.sum(a3_2, axis=0))

# ==========================================
# Assignment 4: Statistical Operations
# ==========================================
print("\n=== Assignment 4 ===")
a4_1 = np.random.randint(1, 50, size=(5, 5))
print(
    f"1. Mean: {np.mean(a4_1):.2f}, Median: {np.median(a4_1)}, Std: {np.std(a4_1):.2f}, Var: {np.var(a4_1):.2f}"
)

a4_2 = np.arange(1, 10, dtype=float).reshape(3, 3)
normalized = (a4_2 - np.mean(a4_2)) / np.std(a4_2)
print("2. Normalized array (Mean=0, Std=1):\n", np.round(normalized, 2))

# ==========================================
# Assignment 5: Broadcasting
# ==========================================
print("\n=== Assignment 5 ===")
# 1. Add (3,) array to each row of (3,3)
a5_1 = np.random.randint(1, 10, size=(3, 3))
row_vec = np.array([10, 20, 30])
print("1. Add row vector via broadcasting:\n", a5_1 + row_vec)

# 2. Subtract (4,) array from each column of (4,4)
a5_2 = np.random.randint(1, 10, size=(4, 4))
col_vec = np.array([1, 2, 3, 4]).reshape(4, 1)  # reshape to (4,1) for column
print("2. Subtract column vector via broadcasting:\n", a5_2 - col_vec)

# ==========================================
# Assignment 6: Linear Algebra
# ==========================================
print("\n=== Assignment 6 ===")
matrix = np.array([[2, 1, 1], [1, 3, 2], [1, 0, 0]], dtype=float)
det = np.linalg.det(matrix)
inv = np.linalg.inv(matrix)
eigenvalues, _ = np.linalg.eig(matrix)
print(f"1. Determinant: {det:.2f}")
print("   Inverse:\n", np.round(inv, 2))
print("   Eigenvalues:", np.round(eigenvalues, 2))

m1 = np.random.randint(1, 5, size=(2, 3))
m2 = np.random.randint(1, 5, size=(3, 2))
print("2. Matrix Multiplication (2x3 @ 3x2):\n", np.matmul(m1, m2))

# ==========================================
# Assignment 7: Advanced Array Manipulation
# ==========================================
print("\n=== Assignment 7 ===")
a7_1 = np.arange(1, 10).reshape(3, 3)
print("1. Reshaped (1,9):\n", a7_1.reshape(1, 9))
print("   Reshaped (9,1):\n", a7_1.reshape(9, 1))

a7_2 = np.random.randint(1, 20, size=(5, 5))
flattened = a7_2.flatten()
reshaped_back = flattened.reshape(5, 5)
print("2. Is reshaped array identical to original?", np.array_equal(a7_2, reshaped_back))

# ==========================================
# Assignment 8: Fancy Indexing and Boolean Indexing
# ==========================================
print("\n=== Assignment 8 ===")
a8_1 = np.random.randint(1, 50, size=(5, 5))
# Four corners: (0,0), (0,4), (4,0), (4,4)
rows = np.array([[0, 0], [4, 4]])
cols = np.array([[0, 4], [0, 4]])
corners = a8_1[rows, cols]
print("1. Corner Elements:\n", corners)

a8_2 = np.random.randint(1, 20, size=(4, 4))
a8_2[a8_2 > 10] = 10
print("2. Elements > 10 capped to 10:\n", a8_2)

# ==========================================
# Assignment 9: Structured Arrays
# ==========================================
print("\n=== Assignment 9 ===")
# 1. Structured array with name, age, weight
dtype1 = [("name", "U10"), ("age", "i4"), ("weight", "f4")]
data1 = [("Alice", 25, 55.5), ("Bob", 20, 75.0), ("Charlie", 30, 68.2)]
struct_arr = np.array(data1, dtype=dtype1)
sorted_struct = np.sort(struct_arr, order="age")
print("1. Sorted by age:\n", sorted_struct)

# 2. Euclidean distance between 2D points
dtype2 = [("x", "i4"), ("y", "i4")]
points = np.array([(1, 2), (4, 6), (7, 1)], dtype=dtype2)
p_x = points["x"]
p_y = points["y"]
# Pairwise distance matrix calculation
dist_matrix = np.sqrt(
    (p_x[:, np.newaxis] - p_x) ** 2 + (p_y[:, np.newaxis] - p_y) ** 2
)
print("2. Pairwise Euclidean Distances between points:\n", np.round(dist_matrix, 2))

# ==========================================
# Assignment 10: Masked Arrays
# ==========================================
print("\n=== Assignment 10 ===")
# 1. Mask elements > 10
data10_1 = np.random.randint(1, 20, size=(4, 4))
masked_1 = ma.masked_greater(data10_1, 10)
print("1. Masked Array (> 10):\n", masked_1)
print("   Sum of unmasked elements:", masked_1.sum())

# 2. Mask diagonal and replace with mean of unmasked elements
data10_2 = np.random.randint(1, 20, size=(3, 3)).astype(float)
mask_diag = np.eye(3, dtype=bool)
masked_2 = ma.masked_array(data10_2, mask=mask_diag)
unmasked_mean = masked_2.mean()
# Replace masked values
data10_2[masked_2.mask] = unmasked_mean
print("2. Diagonal replaced with unmasked mean:\n", np.round(data10_2, 2))