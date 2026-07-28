import matplotlib.pyplot as plt       
import numpy as np 

# scatter graph shows a relationship between two variables
# Example: the relationship between hours studied and test scores

x1 = np.array([0, 1, 1 ,2, 3, 4, 5, 6, 8, 8]) # hours studied of Class A
y1 = np.array([4, 7, 8, 9, 11, 12.5, 14, 15, 17, 19]) # Grades of Class A
x2 = np.array([0, 1, 2 ,2, 3, 4, 5, 6, 8, 9]) # hours studied of Class B
y2 = np.array([2, 5, 7, 7.5, 10, 12, 13, 16, 18, 20]) # Grades of Class B

# create and customize the scatter plots
# the first scatter plot
plt.scatter(x1, y1, color="orange", # customize the color of the dots in scatter plot
                    alpha=0.5, # customize the transparency of the color of the dots in scatter plot
                    s=100, # customize the size of the dots in scatter plot
                    label="Class A") # customize the label name of the first scatter 

# the second scatter plot
plt.scatter(x2, y2, color="skyblue", # customize the color of the dots in scatter plot
                    alpha=0.5, # customize the transparency of the color of the dots in scatter plot
                    s=100, # customize the size of the dots in scatter plot
                    label="Class B") # customize the label name of the second scatter 

plt.title("Test Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Grades")

plt.legend() # we need this to show the legend which contains the names of the labels of the scatter plots to distinguish between the plots
plt.show()