import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
from main import *

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-7, 28)
ax.set_ylim(-7, 7)
# ПЕРВАЯ ГРАНЬ
a1 = length_of_octahedron[0, 0]  #
b1 = length_of_octahedron[1, 0]
c1 = length_of_octahedron[8, 0]
cosine = (a1 ** 2 + c1 ** 2 - b1 ** 2) / (2 * a1 * b1)
sinus = np.sqrt(1 - cosine ** 2)
v1 = np.array([[0., 0.], [a1 * cosine, a1 * sinus], [c1, 0.]])
patch = patches.Polygon(v1, closed=False, fc='r', ec='r', alpha=0.4)
# # ВТОРАЯ ГРАНЬ
a2 = length_of_octahedron[4, 0]  #
b2 = length_of_octahedron[5, 0]
c2 = length_of_octahedron[8, 0]
cosine = (a2 ** 2 + c2 ** 2 - b2 ** 2) / (2 * a2 * b2)
sinus = np.sqrt(1 - cosine ** 2)
v2 = np.array([[0., 0.], [a2 * cosine, -a2 * sinus], [c2, 0.]])
patch2 = patches.Polygon(v2, closed=False, fc='r', ec='r', alpha=0.4)
# ТРЕТЬЯ и ЧЕТВЕРТАЯ ГРАНИ СДВИГАЕМ ВСЕ КООРДИАНТЫ НА ДЛИНУ РЕБРА №8
smecheniee = length_of_octahedron[8, 0]
a3 = length_of_octahedron[1, 0]  #
b3 = length_of_octahedron[2, 0]
c3 = length_of_octahedron[10, 0]
cosine = (a3 ** 2 + c3 ** 2 - b3 ** 2) / (2 * a3 * b3)
sinus = np.sqrt(1 - cosine ** 2)
v3 = np.array([[smecheniee + 0., 0.], [smecheniee + a3 * cosine, a3 * sinus], [smecheniee + c3, 0.]])
patch3 = patches.Polygon(v3, closed=False, fc='r', ec='r', alpha=0.4)
#
# ЧЕТВЕРТАЯ ГРАНЬ, СДВИГАЕМ ВСЕ КООРДИНАТЫ НА ДЛИНУ РЕБРА 8

a4 = length_of_octahedron[5, 0]  #
b4 = length_of_octahedron[6, 0]
c4 = length_of_octahedron[10, 0]
cosine = (a4 ** 2 + c4 ** 2 - b4 ** 2) / (2 * a4 * b4)
sinus = np.sqrt(1 - cosine ** 2)
v4 = np.array([[smecheniee + 0., 0.], [smecheniee + a4 * cosine, -a4 * sinus], [smecheniee + c4, 0.]])
patch4 = patches.Polygon(v4, closed=False, fc='r', ec='r', alpha=0.4)

# # ПЯТАЯ И ШЕСТАЯ ГРАНИ
# smecheniee += length_of_octahedron[10,0]
# a5 = length_of_octahedron[2, 0]
# b5 = length_of_octahedron[3, 0]
# c5 = length_of_octahedron[11, 0]
# cosine = (a5**2 + c5**2 - b5**2)/(2 * a5 * b5)
# sinus = np.sqrt(1 - cosine ** 2)
# v5 = np.array([[smecheniee , 0.], [smecheniee + a5 * cosine, a5 * sinus], [smecheniee + c5, 0.]])
# patch5 = patches.Polygon(v5, closed=False, fc = 'r', ec = 'r', alpha = 0.4)
# # ШЕСТАЯ ГРАНЬ
# a6 = length_of_octahedron[6,0]
# b6 = length_of_octahedron[7,0]
# c6 = length_of_octahedron[11,0]
# cosine = (a6**2 + c6**2 - b**2)/ (2 * a6 * b6)
# sinus = np.sqrt(1 - cosine**2)
# v6 = np.array([[smecheniee + 0., 0.], [smecheniee + a6 * cosine, -a6 * sinus], [smecheniee + c6, 0.]])
# patch6 = patches.Polygon(v6, closed = False, fc = 'r', ec = 'r', alpha = 0.4)
# #СЕДЬМАЯ ГРАНЬ
# smecheniee += length_of_octahedron[11, 0]
# a7 = length_of_octahedron[3,0]
# b7 = length_of_octahedron[0,0]
# c7 = length_of_octahedron[9,0]
# cosine = (a7 ** 2 + c7 ** 2 - b7**2)/(2 * a7 * b7)
# sinus = np.sqrt(1 - cosine**2)
# v7 = np.array([[smecheniee + 0., 0.], [smecheniee + a7 * cosine, a7 * sinus], [smecheniee + c7, 0.]])
# patch7 = patches.Polygon(v7, closed = False, fc = 'r', ec = 'r', alpha = 0.4)
# #ВОСЬМАЯ ГРАНЬ
# a8 = length_of_octahedron[7, 0]
# b8 = length_of_octahedron[4, 0]
# c8 = length_of_octahedron[9, 0]
# cosine = (a8**2 + c8 ** 2 - b8 ** 2)/(2 * a8 * b8)
# sinus = np.sqrt(1 - cosine**2)
# v8 = np.array([[smecheniee + 0., 0.], [smecheniee + a8 * cosine, -a8 * sinus], [smecheniee + c8, 0.]])
# patch8 = patches.Polygon(v8, closed = False, fc = 'r', ec = 'r', alpha = 0.4)

patch.set_color('Red')
patch2.set_color('Red')
patch3.set_color('Blue')
patch4.set_color('Blue')
# patch5.set_color('Green')
# patch6.set_color('Green')
# patch7.set_color('Yellow')
# patch8.set_color('Yellow')
#
# # patch.append(patch1)
# # ax.add_collection(patch1,patch2)
ax.add_patch(patch)
ax.add_patch(patch2)
ax.add_patch(patch3)
ax.add_patch(patch4)


def init():
    return patch,


def animate(i):
    # v[:, 0] += i*0.1
    a1 = length_of_octahedron[0, i]
    b1 = length_of_octahedron[1, i]
    c1 = length_of_octahedron[8, i]

    a2 = length_of_octahedron[4, i]  #
    b2 = length_of_octahedron[5, i]
    c2 = length_of_octahedron[8, i]
    #
    smecheniee = length_of_octahedron[8, i]
    a3 = length_of_octahedron[1, i]  #
    b3 = length_of_octahedron[2, i]
    c3 = length_of_octahedron[10, i]

    a4 = length_of_octahedron[5, i]  #
    b4 = length_of_octahedron[6, i]
    c4 = length_of_octahedron[10, i]

    a_list = [length_of_octahedron[0, i], length_of_octahedron[4, i], length_of_octahedron[1, i],
              length_of_octahedron[5, i], length_of_octahedron[2,i], length_of_octahedron[6,i],length_of_octahedron[3,i], length_of_octahedron[7,i]]
    b_list = [length_of_octahedron[1, i], length_of_octahedron[5, i], length_of_octahedron[2, i],
              length_of_octahedron[6, i], length_of_octahedron[3,i], length_of_octahedron[7,i], length_of_octahedron[0,i], length_of_octahedron[4,i]]
    c_list = [length_of_octahedron[8, i], length_of_octahedron[8, i], length_of_octahedron[10, i],
              length_of_octahedron[10, i], length_of_octahedron[11,i], length_of_octahedron[11,i], length_of_octahedron[9,i]]
    # print(length_matrix.todense())
    # print('a, b , c:', a, b, c)
    try:
        cos_list = []
        sin_list = []
        for k in range(0, len(a_list)):
            cos_k = (a_list[k]**2 + c_list[k]**2 - b_list[k]**2)/(2. * a_list[k] * b_list[k])
            sin_k = np.sqrt(1. - cos_k**2)
            cos_list.append(cos_k)
            sin_list.append(sin_k)


        cosine1 = (a1 ** 2 + c1 ** 2 - b1 ** 2) / (2 * a1 * b1)
        sinus1 = np.sqrt(1 - cosine1 ** 2)
        cosine2 = (a2 ** 2 + c2 ** 2 - b2 ** 2) / (2 * a2 * b2)
        sinus2 = np.sqrt(1 - cosine2 ** 2)
        cosine3 = (a3 ** 2 + c3 ** 2 - b3 ** 2) / (2 * a3 * b3)
        sinus3 = np.sqrt(1 - cosine3 ** 2)
        cosine4 = (a4 ** 2 + c4 ** 2 - b4 ** 2) / (2 * a4 * b4)
        sinus4 = np.sqrt(1 - cosine4 ** 2)
        v1 = np.array([[0., 0.], [a_list[0] * cos_list[0], a_list[0] * sin_list[0]], [c_list[0], 0.]])
        v2 = np.array([[0., 0.], [a_list[1] * cos_list[1], -a_list[1] * sin_list[1]], [c_list[1], 0.]])
        v3 = np.array([[smecheniee, 0.], [smecheniee + a_list[2] * cos_list[2], a_list[2] * sin_list[2]], [smecheniee + c_list[2], 0.]])
        v4 = np.array([[smecheniee , 0.], [smecheniee + a_list[3] * cos_list[3], -a_list[3] * sin_list[3]], [smecheniee + c_list[3], 0.]])
        # smecheniee += length_of_octahedron[10,i]
        # v5 = np.array([[smecheniee, 0.], [smecheniee + a_list[4] * cos_list[4], a_list[4] * sin_list[4]], [smecheniee + c_list[4], 0.]])
        # v6 = np.array([[smecheniee, 0.], [smecheniee + a_list[5] * cos_list[5], -a_list[5] * sin_list[5]],
        #                [smecheniee + c_list[5], 0.]])
        # smecheniee += length_of_octahedron[11,i]
        # v7 = np.array([[smecheniee, 0.], [smecheniee + a_list[6] * cos_list[6], a_list[6] * sin_list[6]], [smecheniee + c_list[6], 0.]])
        # v8 = np.array([[smecheniee, 0.], [smecheniee + a_list[7] * cos_list[7], -a_list[7] * sin_list[7]],
        #                [smecheniee + c_list[7], 0.]])


        # v2 = np.array([[0., 0.], [a2 * cosine2, -a2 * sinus2], [c2, 0]])
        # v3 = np.array([[smecheniee, 0.], [smecheniee + a3 * cosine3, a3 * sinus3], [smecheniee + c3, 0.]])
        # v4 = np.array([[smecheniee, 0.], [smecheniee + a4 * cosine4, -a4 * sinus4], [smecheniee + c4, 0.]])

        patch.set_xy(v1)
        patch2.set_xy(v2)
        patch3.set_xy(v3)
        patch4.set_xy(v4)

    except ZeroDivisionError:
        return None
    return patch,


ani = animation.FuncAnimation(fig, animate, np.arange(1, TIMES), init_func=init,
                              interval=100, blit=True)

ani.save('/Users/ruslanpepa/PycharmProjects/Octahedron/data/sine_wave.gif', writer='pillow')
