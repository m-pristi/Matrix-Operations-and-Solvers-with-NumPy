import numpy as np
import random

# Ask for the matrix size
print("Enter the matrix size:")
n = int(input())

# Choose the input method
print('Choose the input method:\n1. Row-by-row input\n2. Column-by-column input\n3. Random')
choice = int(input())

# Input the matrix based on the selected method
if choice == 1:
    A = np.array([[int(k) for k in input().split()] for j in range(n)])  # Row-by-row input
elif choice == 2:
    A = np.array([[int(input(f"Element [{k+1},{j+1}]: ")) for k in range(n)] for j in range(n)]).T  # Column-by-column input
elif choice == 3:
    A = np.array([[random.randint(-30, 25) for k in range(n)] for j in range(n)])  # Random matrix
else:
    print("Invalid choice! A random matrix will be generated.")
    A = np.array([[random.randint(-30, 25) for k in range(n)] for j in range(n)])

# Display the matrix and its transpose
print("\nMatrix A:\n", A)
print("\nTransposed Matrix:\n", np.transpose(A))

# Compute and display the determinant
det = np.linalg.det(A)
print(f"\nDeterminant of the matrix: {det:.2f}")

# Check if the matrix is invertible
if abs(det) < 1e-10:
    print("\nInverse matrix:\nDoes not exist! Determinant is 0!\n")
else:
    print("\nInverse matrix:\n", np.linalg.inv(A))

# Generate another random matrix B
B = np.array([[random.randint(-30, 24) for o in range(n)] for u in range(n)])

print("\nMatrix B:\n", B)

# Matrix operations
print("\nMatrix C = A + B:\n", A + B)  # Matrix addition
print("\nMatrix D = A - B:\n", A - B)  # Matrix subtraction
print("\nMatrix E = A * B:\n", A @ B)  # Matrix multiplication

# Generate a matrix F with random floating-point numbers
F = np.array([[random.uniform(-30, 24) for k in range(6)] for j in range(4)])
print("\nMatrix F with random floating-point numbers:\n", F)

# Shuffle the rows of matrix F
np.random.shuffle(F)

print("\nShuffled matrix F:\n", F)

# Index elements that are >= 5
print("\nIndex elements that are >= 5:\n")
I = F >= 5
print("Matrix I:\n", I)

# Replace values less than 0 or greater than 7 with 5
F[np.logical_or(F < 0, F > 7)] = 5

print("\nMatrix after replacing values <0 or >7 with 5:\n", F)

# Solve the matrix equation AX = B
print("\nSolving the matrix equation AX = B.")

A = np.array([[3, 2],
              [4, 3]])

B = np.array([[7], [8]])

# Display the matrices A and B
print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)

# Compute the inverse of matrix A
print("\nInverse matrix A:\n", np.linalg.inv(A))

# Solve for X using the inverse of A
X = np.dot(np.linalg.inv(A), B)
print("\nSolution X:\n", X)

# Check the solution by multiplying A with X
check = np.dot(A, X)

# Verify if the solution is correct
if np.allclose(check, B):
    print("\nThe solution is correct!")
else:
    print("\nThe solution is incorrect!")   