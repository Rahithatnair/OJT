import numpy as np
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

concat_array  = np.concatenate((array1,array2))
print("concatenated array",concat_array)

#created a 2D array
array2D1 = np.array([[1,2,3],[4,5,6]])
array2D2 = np.array([[7,8,9],[10,11,12],[13,14,15]])

#vertically and horizontaly
#vstack - for vertical joining
#hstack - for horizontal joining

#vertically
vstack_array = np.vstack((array2D1,array2D2))
print("verticl stacked array is :",vstack_array)

#horizontally
arr2D1 = np.array([[1,2,3],[4,5,6]])
arr2D2 = np.array([[7,8,9],[10,11,12]])
hstack_array = np.hstack((arr2D1,arr2D2))
print("horizontally stacked array is",hstack_array)