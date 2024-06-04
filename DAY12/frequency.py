
# How to count the frequency of unique values in NumPy array

import numpy as np
# Creating a sample array
array = np.array([1, 2, 3, 1, 2, 1, 3, 4, 5])

# Get unique values and its counts
unique_values = np.unique(array)
counts = np.bincount(array)

print("Unique values:", unique_values)
print("Counts:", counts[unique_values])
