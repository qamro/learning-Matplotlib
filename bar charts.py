import matplotlib.pyplot as plt       
import numpy as np         

#NOTE: i used a normal list for categories cuz a list of strings doesn't benefit from numpy arrays
categories = ["grain", "fruits", "vegetables", "proteins", "sweets"]
values = np.array([3, 5, 2, 11, 4])

# create our bar chart and customize it as we want
# NOTE: wa can customize our bar charts as we want just like we did with the line plots
plt.bar(categories, values, color="skyblue")
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()