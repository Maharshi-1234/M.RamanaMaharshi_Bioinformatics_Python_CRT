#View Method - Modifies the original array
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 23
print(arr)
print(x)