import numpy as np
import matplotlib.pyplot as plt
xpoints = np.array([2, 4, 6, 8, 1, 13, 16, 18, 20])
ypoints = np.array([8, 6, 4, 2, 15, 12, 14, 15, 19])
# Plot original data
plt.scatter(xpoints, ypoints, color='blue', label='Main Data')
# Highlight xpoints on x-axis (y=0)
plt.scatter(xpoints, np.zeros_like(xpoints), color='yellow', label='xpoints on x-axis')
# Highlight ypoints on y-axis (x=0)
plt.scatter(np.zeros_like(ypoints), ypoints, color='red', label='ypoints on y-axis')
plt.legend()
plt.grid(True)
plt.title("Scatter Plot with Highlights")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
