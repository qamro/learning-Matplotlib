import matplotlib.pyplot as plt       
import numpy as np 

categories = ["web developers", "mobile developers", "DevOps engineers", "AI/ML enginners"]
values = np.array([432, 210, 150, 298])
colors = ["red", "skyblue", "yellow", "green"]
# create and customize the pie chart
plt.pie(values, labels=categories, # show the labels
                autopct="%.1f%%", # show the percentage in each slice of the pie chart using the format specifiers of the percentage
                colors=colors)  # customize the colors of the slices of the pie chart
plt.show()