
#Find the sum of values in a matrix


import numpy as np

# Creating a sample matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculating the sum of each column
column_sums = np.sum(matrix, axis=0)
print("The sum of each column:" ,column_sums)

# Calculating the sum of each row
row_sums = np.sum(matrix, axis=1)
print("The sum of each row:", row_sums)
