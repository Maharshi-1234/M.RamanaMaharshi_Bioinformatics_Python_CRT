import numpy as np
import matplotlib.pyplot as plt

A = np.array([1, 2, 3, 4])
B = np.array([2, 4, 6, 8])

# Use values of B for color mapping
plt.scatter(A, B, c=B, cmap='viridis', marker='D', s=100)

plt.colorbar(label='Color scale from B')  # Show the color bar
plt.title("Scatter Plot with Normal Colormap")
plt.xlabel("A")
plt.ylabel("B")
plt.grid(True)
plt.show()
