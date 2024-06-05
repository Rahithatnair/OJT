import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9]) 

split_array = np.split(array,3)
print("original array : ",array)
print("split array : ",split_array)

#multi dimensional
#horizontally and vertically

array_2D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
vsplit_array = np.vsplit(array_2D,2)
print("vsplited array : ",vsplit_array)
