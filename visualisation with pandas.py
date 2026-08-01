import matplotlib.pyplot as plt
import numpy as np
import pandas as pd   

df = pd.read_csv("students.csv") # read the csv file and store it in a pandas dataframe
print(df) # print the dataframe to see what it looks like
print()

# NOTE: we can use the value_counts() function to count the number of students in each age group and store it in a variable
# NOTE: the value_counts() function returns a pandas series with: index = "unique values" and, values = "number of times each value appears"
city_count = df["City"].value_counts() # count the number of students in each city and store it in a variable
print(city_count) # print the city count to see what it looks like
print()


# create and customize a bar chart to visualize the number of students in each city
plt.bar(city_count.index, city_count.values, color="skyblue")
plt.title("Number of Students in Each City") # set the title of the bar chart
plt.xlabel("City") # set the x-axis label of the bar chart
plt.ylabel("Number of Students") # set the y-axis label of the bar chart
plt.show() # show the bar chart