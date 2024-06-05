# converting 1D into 2D
# reshape() is the method which is used foe reshaping arrays

import numpy as np
array_1D=np.array([1,2,3,4,5,6])
print("array1D : ",array_1D)
print("shape of array1D : ",array_1D.shape)

#reshaping the 1D arrya to 2D array

array_2D = array_1D.reshape((2,3))
print("2D array :",array_2D)
print("shape of array2D :",array_2D.shape)


#reshape 1D array into 3D array
array_3D = array_1D.reshape((3,2))
print("3D array :",array_3D)
print("shape of the array3d",array_3D.shape)


#reshape back a 2d array to 1D
arr_1D_again = array_2D.reshape(-1)
print("Array 1D again : ",arr_1D_again)