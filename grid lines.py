import matplotlib.pyplot as plt       
import numpy as np  

# plt.grid() make the plots easier to read by adding reference lines(grid lines)
# we can use just plt.grid() to create simple grid lines or you can customize them by adding arguments to the grid() function

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])
plt.grid()
plt.plot(x, y)
plt.show()