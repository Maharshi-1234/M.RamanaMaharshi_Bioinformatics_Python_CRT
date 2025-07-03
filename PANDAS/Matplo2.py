import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
ypoints=np.array([2,4,6,8])
xpoints=np.array([8,6,4,2])
plt.title('THE GRAPH OF GRAPHS')
plt.plot(ypoints,'o:y',ms=15,mec='r',mfc='c') #ms = markersize,mec = markeredgecolor,mfc=markerfacecolor
plt.plot(xpoints,'o:g',ms=15)
plt.show()
