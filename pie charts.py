import matplotlib.pyplot as plt       
import numpy as np 

categories = ["web developers", "mobile developers", "DevOps engineers", "AI/ML enginners"]
values = np.array([432, 210, 150, 298])
colors = ["red", "skyblue", "yellow", "green"]

# create and customize the pie chart
plt.pie(values, labels=categories, # show the labels
                autopct="%.1f%%", # show the percentage in each slice of the pie chart using the format specifiers of the percentage
                colors=colors, # customize the colors of the slices of the pie chart
                explode=[0, 0, 0, 0.1], # explode any slices we want by a customized distance that we put in a list for each slice(we put 0 for non exploded slices and we put a customized distance for exploded slices)
                shadow=True, # add a drop shadow to the pie chart 
                startangle=90) # customize the start angle of the pie chart by making an angle rotation(90° rotation for example) 
plt.title("Algerian Community")
plt.show()