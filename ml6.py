import math 
import numpy as np 
import scipy.linalg as la 
import statistics 

# (a) Usage of math methods 
num1, num2 = 15, 20 
print("Floor of 3.7:", math.floor(3.7))  # Rounds down 
print("Ceil of 3.2:", math.ceil(3.2))  # Rounds up 
print("Square root of 25:", math.sqrt(25)) 
print("Integer square root of 25:", math.isqrt(25)) 
print("GCD of 15 and 20:", math.gcd(num1, num2)) 

# (b) Usage of NumPy array attributes and methods 
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
print("Number of dimensions:", arr.ndim) 
print("Shape of array:", arr.shape) 
print("Size of array:", arr.size) 
print("Sum of elements:", arr.sum()) 
print("Mean of elements:", arr.mean()) 
print("Sorted array:", np.sort(arr, axis=None)) 
print("Sine of elements:", np.sin(arr)) 

# (c) Usage of determinant and eigenvalues 
a = np.array([[3, 2], [1, 4]]) 
print("Determinant:", la.det(a)) 
print("Eigenvalues:", la.eigvals(a)) 

# (d) Reshaping 1D list to 2D and 3D matrices 
lst = np.arange(1, 13)  # List from 1 to 12 
matrix_2d = lst.reshape(3, 4)  # Reshape to 3x4 matrix 
matrix_3d = lst.reshape(2, 2, 3)  # Reshape to 2x2x3 matrix 
print("2D Matrix:\n", matrix_2d) 
print("3D Matrix:\n", matrix_3d) 

# (e) Generating random matrices 
random_matrix = np.random.rand(3, 3)  # 3x3 matrix with random values 
print("Random Matrix:\n", random_matrix)
