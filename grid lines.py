import matplotlib.pyplot as plt       
import numpy as np  

# plt.grid() make the plots easier to read by adding reference lines(grid lines)
# we can use just plt.grid() to create simple grid lines or you can customize them by adding arguments to the grid() function

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

# customize the grid lines
plt.grid(axis="x", # here we select the axis that we want to be shown and customized(we can write:axis="x", axis="y" or axis="both") 
        linewidth=2, # customize the linewidth of the grid lines (its 1 by default)
        linestyle="dashed", # customize the linestyle of the grid lines
        color="Green") # customize the color of the grid lines

plt.plot(x, y)
plt.show()