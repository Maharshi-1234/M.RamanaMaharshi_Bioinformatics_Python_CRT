import numpy as np
import matplotlib.pyplot as plt

# Plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Plot-1", loc="left")

# Plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("Plot-2", loc="left")

# Plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("Plot-3")

# Plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 4)
plt.plot(x, y)
plt.title("Plot-4")

# Plot 5:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("Plot-5")

# Plot 6:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 3, 6)
plt.plot(x, y)
plt.title("Plot-6", loc="left")


plt.tight_layout()  
plt.show()
