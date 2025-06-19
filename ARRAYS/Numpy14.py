#Concatenation of arrays
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr)

#Joining two 2D arrays
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[7,6],[3,8]])
arr = np.concatenate((arr1,arr2),axis=1)
#axis represents directions and depends upon number of values
print(arr)

#joining two array 2D:
import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis=0)
print(arr)