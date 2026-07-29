import numpy as np
import matplotlib.pyplot as plt

A = np.random.normal(loc=50, scale=8, size=1000)
B = np.random.normal(loc=60, scale=10, size=1000)

plt.hist(A, bins=20, color="lightgreen", alpha=0.5, label="Group A")
plt.hist(B, bins=20,color="skyblue", alpha=0.5, label="Group B")

plt.legend()
plt.show()