import numpy as np

#creating 1D array
array_1d=np.array([1,2,3,4,5])
print("1D array : ",array_1d)

#creating 2D array
array_2d=np.array([[2,4,3],[3,4,2]])
print("2D array:",array_2d)


#creating 3D array
array_3d=np.array([[[1,2,3],[4,5,6],[5,6,7]]])
print("3D array:",array_3d)

#create an array with ones
array_ones = np.ones((2,4))
print("array with ones : ",array_ones)

#create an array with zeros
array_zeros=np.zeros((3,3))
print("arrray with zeros : ",array_zeros)

#create an array with a particular range
array_range=np.arange(10)
print("array with a range : ",array_range)
