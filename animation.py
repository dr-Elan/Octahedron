import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
from main import  *

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 10)
ax.set_ylim(-0, 2)

a = length_of_tetrahedron[0, 0]
b = length_of_tetrahedron[1, 0]
c = length_of_tetrahedron[2, 0]
# print('a, b , c:', a, b , c)
cosine = (a**2 + c**2 - b**2)/(2*a*b)
sinus = np.sqrt(1 - cosine**2)
v = np.array([[0.,0.], [b*cosine, b*sinus], [c, 0.]])

patch = patches.Polygon(v,closed=True, fc='r', ec='r')
ax.add_patch(patch)

def init():
    return patch,

def animate(i):
    # v[:, 0] += i*0.1
    a = length_of_tetrahedron[0, i]
    b = length_of_tetrahedron[1, i]
    c = length_of_tetrahedron[2, i]
    # print(length_matrix.todense())
    # print('a, b , c:', a, b, c)
    try:
        cosine = (a ** 2 + c ** 2 - b ** 2) / (2 * a * b)
        sinus = np.sqrt(1 - cosine ** 2)
        v = np.array([[0., 0.], [b * cosine, b * sinus], [c, 0.]])
        patch.set_xy(v)
    except ZeroDivisionError:
        return None
    return patch,

ani = animation.FuncAnimation(fig, animate, np.arange(1, TIMES), init_func=init,
                              interval=100, blit=True)

ani.save('sine_wave.gif', writer='pillow')
