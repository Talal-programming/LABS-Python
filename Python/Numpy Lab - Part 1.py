# =========================================================
# Numpy Lab - Part 1
# =========================================================

import numpy as np

# =========================================================
# 1) Array Creation and Properties
# =========================================================
print("\n=== Question 1 ===")

A = np.arange(1, 21).reshape(4, 5)

print("A:\n", A)
print("Data type:", A.dtype)
print("Dimensions:", A.ndim)
print("Shape:", A.shape)
print("Size:", A.size)
print("Item size:", A.itemsize)
print("Total size (bytes):", A.nbytes)

B = A.reshape(5, 4)
print("Reshaped B:\n", B)

# =========================================================
# 2) Array Operations
# =========================================================
print("\n=== Question 2 ===")

a = np.array([[0.,0.,0.],
              [10.,10.,10.],
              [20.,20.,20.],
              [30.,30.,30.]])

b = np.array([0., 1., 2.])

c = a + b
print("c = a + b:\n", c)

mask = (c >= 22)
print("Mask (c >= 22):\n", mask)

count = np.sum(mask)
print("Count of values >= 22:", count)

# =========================================================
# 3) Grades Analysis
# =========================================================
print("\n=== Question 3 ===")

grades = np.array([[87, 96, 70],
                   [100, 87, 90],
                   [94, 77, 90],
                   [100, 81, 82]])

print("Sum:", np.sum(grades))
print("Min:", np.min(grades))
print("Max:", np.max(grades))
print("Mean:", np.mean(grades))
print("Std:", np.std(grades))
print("Var:", np.var(grades))

print("Mean per column:", np.mean(grades, axis=0))
print("Mean per row:", np.mean(grades, axis=1))
print("Max per row:", np.max(grades, axis=1))

# =========================================================
# 4) Matrix Operations
# =========================================================
print("\n=== Question 4 ===")

matrix = np.array([[2, 4, 6],
                   [1, 3, 5],
                   [7, 9, 11]])

print("Row sums:", np.sum(matrix, axis=1))
print("Column sums:", np.sum(matrix, axis=0))
print("Overall mean:", np.mean(matrix))

# =========================================================
# 5) Array Arithmetic
# =========================================================
print("\n=== Question 5 ===")

A = np.array([[10, 20, 30],
              [40, 50, 60]])

B = np.array([1, 2, 3])

print("A + B:\n", A + B)
print("A * 2:\n", A * 2)
print("A - 5:\n", A - 5)

# =========================================================
# 6) Index Operations
# =========================================================
print("\n=== Question 6 ===")

grades = np.array([[70, 85, 90],
                   [88, 76, 95],
                   [60, 80, 72]])

print("Index of largest value:", np.argmax(grades))
print("Index of highest in each row:", np.argmax(grades, axis=1))
print("Index of lowest in each column:", np.argmin(grades, axis=0))

# =========================================================
# 7) Euclidean Distance (L2)
# =========================================================
print("\n=== Question 7 ===")

array1 = np.array([2, 3, 4])
array2 = np.array([5, 6, 7])

distance = np.sqrt(np.sum((array2 - array1) ** 2))

print("Euclidean Distance:", distance)
