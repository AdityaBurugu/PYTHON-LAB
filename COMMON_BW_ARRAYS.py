import numpy as np
array1=np.array([0,10,20,40,60])
print("Array1 is:",array1)
array2=np.array([10,20,30,40])
print("Array2 is:",array2)
print("Common Values between Two Arrays:")
common_values=np.intersect1d(array1,array2)
print(common_values)
print(type(common_values))