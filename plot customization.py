import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([3, 15, 28, 31])
y2 = np.array([5, 32, 15, 7])
y3 = np.array([5, 32, 15, 7])
plt.plot(x, y1, marker=".",    # customize the marker
                markersize=30,     # customize the marker size
                markerfacecolor="Red",   # customize the color of the marker 
                markeredgecolor="Green",  # customize the color of the edges(borders) of the marker
                linestyle="solid",  # customize the line style of the plot
                linewidth=4,  # customize the line width of the plot(its linewidth=1 by default btw)
                color="Grey")  # customize the color of the line plot

# NOTE: we can use multiple plots in the same figure
# customize a second plot line in the same figure with the first plot
plt.plot(x, y2, marker=".",    # customize the marker
                markersize=30,     # customize the marker size
                markerfacecolor="Red",   # customize the color of the marker 
                markeredgecolor="Green",  # customize the color of the edges(borders) of the marker
                linestyle="solid",  # customize the line style of the plot
                linewidth=4,  # customize the line width of the plot(its linewidth=1 by default btw)
                color="Grey")  # customize the color of the line plot)

# customize a third plot line in the same figure with the first and the second plots
plt.plot(x, y3, marker=".",    # customize the marker
                markersize=30,     # customize the marker size
                markerfacecolor="Red",   # customize the color of the marker 
                markeredgecolor="Green",  # customize the color of the edges(borders) of the marker
                linestyle="solid",  # customize the line style of the plot
                linewidth=4,  # customize the line width of the plot(its linewidth=1 by default btw)
                color="Grey")  # customize the color of the line plot)
plt.show()



"""
HERE ARE ALL THE MARKERS: 

Points/dots

. : point
, : pixel

Basic shapes

o : circle
s : square
D : diamond
d : thin diamond
p : pentagon
h : hexagon1
H : hexagon2
8 : octagon

Triangles

v : triangle down
^ : triangle up
< : triangle left
> : triangle right
1 : tri_down
2 : tri_up
3 : tri_left
4 : tri_right

Lines/crosses

+ : plus
x : x
X : filled x
| : vertical line
_ : horizontal line

"""



"""
HERE ARE ALL THE LINE STYLES :

"solid" or "-" → Solid
"dashed" or "--" → Dashed
"dashdot" or "-." → Dash-dot
"dotted" or ":" → Dotted
"None" (or "", " ", "none") → No line (markers only)

"""