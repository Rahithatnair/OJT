
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array_3d = array_1d.reshape(2, 3, 2)
# Print the reshaped array
print("Reshaped 3-D array:\n", array_3d)
