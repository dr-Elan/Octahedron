import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
from main import *

fig = plt.figure()
# ax = fig.add_subplot(111)
ax = []
ax1 = fig.add_subplot(221)   #top left
ax2 = fig.add_subplot(222)   #top right
ax3 = fig.add_subplot(223)   #bottom left
ax4 = fig.add_subplot(224)   #bottom right
ax.append(ax1)
ax.append(ax2)
ax.append(ax3)
ax.append(ax4)
for a_x in ax:
    a_x.set_xlim(-7, 10)
    a_x.set_ylim(-7, 7)

# ax.set_xlim(-7, 30)
# ax.set_ylim(-7, 7)
list_of_a_edg = [0, 4, 1,  5,  2,  6,  3, 7]
list_of_b_edg = [1, 5, 2,  6,  3,  7,  0, 4]
list_of_c_edg = [8, 8, 10, 10, 11, 11, 9, 9]
list_of_colors = ['Red', 'Red', 'Blue', 'Blue', 'Green', 'Green', 'Yellow', 'Yellow']
list_of_patches = []
smechenie = 0.0
for i in range(0, len(list_of_a_edg)):
    a = length_of_octahedron[list_of_a_edg[i], 0]
    b = length_of_octahedron[list_of_b_edg[i], 0]
    c = length_of_octahedron[list_of_c_edg[i], 0]
    cosine = (a**2 + c**2 - b**2)/(2*a*b)
    print('номера граней:', '\t', list_of_a_edg[i], list_of_b_edg[i], list_of_c_edg[i])
    try:
        sinus = np.sqrt(1 - cosine**2)
    except:
        print('Значение косинуса по модулю больше единицы')
        sys.exit(0)  # Преждевременное завершение программы
    if i == 0:
        vk = np.array([[0, 0.], [a * cosine,  (-1)**i * a * sinus], [c, 0.]])
        # print('pechataem krasnye', v)
        patch = patches.Polygon(vk, closed=False, fc='r', ec='r', alpha=0.4)
        patch.set_color('Red')
        ax[0].add_patch(patch)
    if i == 1:
        v_ = np.array([[0, 0.], [ a * cosine, - a * sinus], [ c, 0.]])
        # print('pechataem krasnye', v_)
        patch_ = patches.Polygon(v_, closed=False, fc='r', ec='r', alpha=0.4)
        patch_.set_color('Red')
        ax[0].add_patch(patch_)
    if list_of_c_edg[i] == 10:
        v1 = np.array([[0, 0.], [a * cosine, (-1) ** i * a * sinus], [c, 0.]])
        patch1 = patches.Polygon(v1, closed=False, fc='r', ec='r', alpha=0.4)
        patch1.set_color('Blue')
        ax[1].add_patch(patch1)
    if list_of_c_edg[i] == 11:
        v2 = np.array([[0, 0.], [a * cosine, (-1) ** i * a * sinus], [c, 0.]])
        patch2 = patches.Polygon(v2, closed=False, fc='r', ec='r', alpha=0.4)
        patch2.set_color('Green')
        ax[2].add_patch(patch2)
    if  list_of_c_edg[i] == 9:
        v3 = np.array([[0, 0.], [a * cosine, (-1) ** i * a * sinus], [c, 0.]])
        # print('pechataem zheltoe',v3)
        patch3 = patches.Polygon(v3, closed=False, fc='r', ec='r', alpha=0.4)
        patch3.set_color('Yellow')
        ax[3].add_patch(patch3)
    # if  i == 7:
    #     v3_ = np.array([[0, 0.], [a * cosine, -a * sinus], [c, 0.]])
    #     # print('pechataem zheltoe',v3)
    #     patch3_ = patches.Polygon(v2, closed=False, fc='r', ec='r', alpha=0.4)
    #     patch3_.set_color('Yellow')
    #     ax[3].add_patch(patch3_)
    # v1 = np.array([[smechenie, 0.], [smechenie + a * cosine, (-1)**i * a * sinus], [smechenie + c, 0.]])
    # print('координаты', '\n', v1)
    # patch = patches.Polygon(v1, closed=False, fc='r', ec='r', alpha=0.4)
    # patch.set_color(list_of_colors[i])
    # list_of_patches.append(patch)

# for pch in range(0, len(list_of_patches)):
#     ax.add_patch(list_of_patches[pch])
# ax.add_patch(list_of_patches[-1])

def init():
    return []

def animate(i):
    list_of_a_edg = [0, 4, 1, 5,   2,  6,  3, 7]
    list_of_b_edg = [1, 5, 2, 6,   3,  7,  0, 4]
    list_of_c_edg = [8, 8, 10,10,  11, 11, 9, 9]


    for j in range(0, len(list_of_a_edg)):
        a = length_of_octahedron[list_of_a_edg[j], i]
        b = length_of_octahedron[list_of_b_edg[j], i]
        c = length_of_octahedron[list_of_c_edg[j], i]
        cosine = (a ** 2 + c ** 2 - b ** 2) / (2 * a * b)
        try:
            sinus = np.sqrt(1 - cosine ** 2)
        except:
            print('Значение косинуса по модулю больше единицы')
            sys.exit(0)  # Преждевременное завершение программы
        if j == 0:
            try:
                vk = np.array([[0, 0.], [a * cosine, (-1) ** j * a * sinus], [c, 0.]])
                patch = patches.Polygon(vk, closed=False, fc='r', ec='r', alpha=0.4)
                patch.set_color('Red')
                patch.set_xy(vk)
            except ZeroDivisionError:
                return None

        if j == 1:
            try:
                v_ = np.array([[0, 0.], [a * cosine, - a * sinus], [c, 0.]])
                patch_ = patches.Polygon(v_, closed=False, fc='r', ec='r', alpha=0.4)
                patch_.set_color('Red')
                patch_.set_xy(v_)
            except ZeroDivisionError:
                return None
        if list_of_c_edg[j] == 10:
            try:
                v1 = np.array([[0, 0.], [a * cosine, (-1) ** j * a * sinus], [c, 0.]])
                patch1 = patches.Polygon(v1, closed=False, fc='r', ec='r', alpha=0.4)
                patch1.set_color('Blue')
                patch1.set_xy(v1)
            except ZeroDivisionError:
                return None
        if list_of_c_edg[j] == 11:
            try:
                v2 = np.array([[0, 0.], [a * cosine, (-1) ** j * a * sinus], [c, 0.]])
                patch2 = patches.Polygon(v2, closed=False, fc='r', ec='r', alpha=0.4)
                patch2.set_color('Yellow')
                patch2.set_xy(v2)
            except ZeroDivisionError:
                return None
        if list_of_c_edg[j] == 9:
            try:
                v3 = np.array([[0, 0.], [a * cosine, (-1) ** j * a * sinus], [c, 0.]])
                patch3 = patches.Polygon(v3, closed=False, fc='r', ec='r', alpha=0.4)
                patch3.set_color('Yellow')
                patch3.set_xy(v3)
            except ZeroDivisionError:
                return None
    return []
    # for pch in range(0, len(list_of_patches)):
    #     patch.set_xy(list_of_patches[pch])
    #     return patch,

ani = animation.FuncAnimation(fig, animate, np.arange(1, TIMES), init_func=init,
                                  interval=100, blit=True)

ani.save('/Users/ruslanpepa/PycharmProjects/Octahedron/data/sine_wave.gif', writer='pillow')


