import matplotlib.pyplot as plt       
import numpy as np 


x = np.array([1, 2, 3, 4, 5])


# NOTE: we can use the subplots() function to create multiple plots in the same figure
# NOTE: the subplots() function returns two values: the figure and the axes of the subplots we created
# NOTE: the axes is a 2D np array of the subplots we created, so we can access each subplot by its index in the array
# NOTE: the subplots() function takes two arguments: the number of rows and the number of columns of the subplots we want to create


# to create subplots we can use the plt.subplots() function which takes two arguments:
# the number of rows and the number of columns of the subplots we want to create
# this is how to create a 2x2 grid of subplots: figure, axes = plt.subplots(number_rows=2, number_columns=2)
figure, axes = plt.subplots(2, 2) # create a 2x2 grid of subplots


# create and customize the first subplot in the first row and first column of the grid
axes[0, 0].plot(x, x**2, color="orange", label="y = x^2") # customize the first subplot  
axes[0, 0].set_title("y = x^2") # set the title of the first subplot
axes[0, 0].legend() # show the legend for the first subplot


# create and customize the second subplot in the first row and second column of the grid
axes[0, 1].scatter(x, x**3, color="skyblue", label="y = x^3") # customize the second subplot 
axes[0, 1].set_title("y = x^3") # set the title of the second subplot
axes[0, 1].legend() # show the legend for the second subplot


# create and customize the third subplot in the second row and first column of the grid
axes[1, 0].bar(x, x**4, color="lightgreen", label="y = x^4") # customize the third subplot
axes[1, 0].set_title("y = x^4") # set the title of the third subplot
axes[1, 0].legend() # show the legend for the third subplot


# create and customize the fourth subplot in the second row and second column of the grid
axes[1, 1].plot(x, x**5, color="red", label="y = x^5") # customize the fourth subplot    
axes[1, 1].set_title("y = x^5") # set the title of the fourth subplot
axes[1, 1].legend() # show the legend for the fourth subplot


plt.tight_layout() # adjust the spacing between subplots to prevent overlap
plt.show()