import matplotlib.pyplot as plt       
import numpy as np 

# scatter graph shows a relationship between two variables
# Example: the relationship between hours studied and test scores

# create and customize the scatter plot
x = np.array([0, 1, 1 ,2, 3, 4, 5, 6, 8, 8]) # hours studied
y = np.array([4, 7, 8, 9, 11, 12.5, 14, 15, 17, 19]) # test scores
plt.scatter(x, y)
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")
plt.show()