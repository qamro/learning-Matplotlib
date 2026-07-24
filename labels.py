import matplotlib.pyplot as plt       
import numpy as np   

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([3, 15, 28, 31])
y2 = np.array([5, 32, 15, 7])
y3 = np.array([25, 12, 40, 2])

# customize the title of the plots
plt.title("Class size", fontsize=20,  # customize the font size of the title
                        family="Arial",  # customize the font family of the title
                        fontweight="bold",  # customize the font weight(font type) of the title
                        color="Red")  # customize the font color of the title

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()