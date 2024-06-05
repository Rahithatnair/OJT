# Change data type from float to integer by using int as parameter value
import numpy as np

float_array = np.array([1.5, 2.7, 3.1, 4.9, 5.2])
int_array = float_array.astype(int)
print(int_array)
print(f"Data type of int_array: {int_array.dtype}")

