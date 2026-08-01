import matplotlib.pyplot as plt       
import numpy as np         

#NOTE: i used a normal list for categories cuz a list of strings doesn't benefit from numpy arrays
categories = ["grain", "fruits", "vegetables", "proteins", "sweets"]
values = np.array([3, 5, 2, 11, 4])

# create our horizontal bar chart and customize it as we want
# NOTE: wa can customize our horizontal bar charts as we want just like we did with the the normal bar charts
plt.barh(categories, values, color="skyblue")
plt.title("Daily Consumption")
plt.xlabel("Quantity")
plt.ylabel("Food")

plt.tight_layout() # adjust the spacing and layout of the plot to prevent overlap and make it look better
plt.show()