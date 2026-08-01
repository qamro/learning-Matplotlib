import matplotlib.pyplot as plt
import numpy as np
import pandas as pd   

df = pd.read_csv("students.csv") # read the csv file and store it in a pandas dataframe
print(df) # print the dataframe to see what it looks like
print()

# NOTE: we can use the value_counts() function to count the number of students in each age group and store it in a variable
# NOTE: the value_counts() function returns a pandas series with: index = "unique values" and, values = "number of times each value appears"
age_count = df["Age"].value_counts() # count the number of students in each age group and store it in a variable
print(age_count) # print the age count to see what it looks like