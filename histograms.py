import matplotlib.pyplot as plt       
import numpy as np 

# histogram is a graph that shows the distribution of numerical data.
# Axes:
# X-axis: ranges (intervals) of the data called bins.
# Y-axis: the frequency (count) of values in each bin.
# bin is an interval that groups data values.
"""
For example we have these data:

Data: [1, 2, 2, 3, 5, 6, 7, 8]

Bins=4:

1–2
3–4
5–6
7–8

The height of each bar is the number of values inside that interval.
"""

# generate random values using np.random.normal()
# loc   -> Mean (center) of the normal distribution.
# scale -> Standard deviation (spread of the data).
# size  -> Number or shape of the random values to generate.
scores = np.random.normal(loc=50, scale=10, size=100)
# Generates 100 random values with:
# Mean = 50
# Standard deviation = 10 (that means almost all numbers will be around 40 and 60)


# we use np.clip(scores, the lower bound, the upper bound) to limits the values of an array between two bounds
# We use it here because if the normal distribution has a large scale
# (for example scale=70), it may generate values below 0 or above 100.
# np.clip() keeps all scores inside the valid range [0, 100].
scores = np.clip(scores, 0 ,100)

# create and customize our histogram
plt.hist(scores, bins=5, # Number of intervals
                color="lightgreen", # customize the color of histogram bars
                edgecolor="black", # customize th edge color of histogram
                alpha=0.5) # customize the transparency of the color of histogram bars

plt.show()






# NOTE: in the plt.hist() u can pass bin=5 for example or u can specify the bins by bins=[0,20,40,60,80,100] for example
"""
bins=[0,20,40,60,80,100] creates these intervals:

Bin 1: 0  → 20
Bin 2: 20 → 40
Bin 3: 40 → 60
Bin 4: 60 → 80
Bin 5: 80 → 100
"""



# NOTE: if you dont pass the bins number in plt.hist() then The axis will be:
# Matplotlib automatically chooses a reasonable number of bins.
# X-axis: your data grouped into bins.
# Y-axis: automatically computed frequencies (counts).