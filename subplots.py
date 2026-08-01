import matplotlib.pyplot as plt       
import numpy as np 


# NOTE: we can use the subplots() function to create multiple plots in the same figure
# NOTE: the subplots() function returns two values: the figure and the axes of the subplots we created
# NOTE: the axes is a 2D np array of the subplots we created, so we can access each subplot by its index in the array
# NOTE: the subplots() function takes two arguments: the number of rows and the number of columns of the subplots we want to create


# to create subplots we can use the plt.subplots() function which takes two arguments:
# the number of rows and the number of columns of the subplots we want to create
figure, axes = plt.subplots(number_rows=2, number_columns=2) # create a 2x2 grid of subplots