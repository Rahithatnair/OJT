#Find the number of rows and columns of a given matrix using NumPy

import numpy as np

# Creating a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Get the shape of the matrix
rows, columns = matrix.shape

print(f"The matrix has {rows} rows and {columns} columns.")
