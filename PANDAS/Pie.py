import matplotlib.pyplot as plt
import numpy as np
# 7 data values
y = np.array([10, 10, 15, 20, 12, 13, 20])
# 7 labels
mylabels = ["Java", "Python", "C++", "SQL", "JavaScript", "C#", "Go"]
# 7 explode values (explode only the 3rd one - C++)
explode = [0, 0, 0.1, 0, 0, 0, 0]
# Create pie chart
plt.pie(y, labels=mylabels, explode=explode, autopct='%1.1f%%')
# Move legend outside
plt.legend(title="Languages:", loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()