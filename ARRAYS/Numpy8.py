#Copy Method
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 32
print(arr)
print(x)