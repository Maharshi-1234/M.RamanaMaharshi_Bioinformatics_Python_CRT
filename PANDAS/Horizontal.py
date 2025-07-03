import numpy as np
import matplotlib.pyplot as plt
A = np.array([-2, 7, 3, 4])
B = np.array([2, 4, 6, 8])
plt.title("Horizontal Bar Plot")
plt.barh(A,B)
plt.show()