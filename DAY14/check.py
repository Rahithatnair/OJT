import numpy as np

array = np.array([10,12,14,16,18,20])

#np.where(array==20)  where() used to check a particular condition

#element greater than 15 for the above array
elements = np.where(array>15)
print(array[elements])

#replacing with 0
elements = np.where(array > 15,0,array)
print(elements)

