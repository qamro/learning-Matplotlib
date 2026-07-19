import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y = np.array([3, 15, 28, 31])
plt.plot(x, y, marker=".",    # customize the marker
                markersize=30,     # customize the marker size
                markerfacecolor="Red",   # customize the color of the marker 
                markeredgecolor="Green",  # customize the color of the edges(borders) of the marker
                )     
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
