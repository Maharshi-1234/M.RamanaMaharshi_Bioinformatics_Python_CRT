import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt

ypoints = np.array([2, 4, 6, 8])
xpoints = np.array([8, 6, 4, 2])

plt.title('THE GRAPH OF GRAPHS', loc='right')  # loc=Position of title
plt.xlabel('Number of Sales')
plt.ylabel('Average TurnOver')

# Plotting with red circle markers
plt.plot(xpoints, 'o:r', ms=15)

# Grid customization: green dashed grid lines for x-axis with a linewidth of 1
plt.grid(axis='x', color='green', linestyle='--', linewidth=1)

# Display the plot
plt.show()
