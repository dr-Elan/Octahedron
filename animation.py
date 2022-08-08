import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from matplotlib.patches import *
from matplotlib.ticker import NullLocator

lc = NullLocator()


TIMES = 100

list_of_a_edg = [0, 4, 1,  5,  2,  6,  3, 7]
list_of_b_edg = [1, 5, 2,  6,  3,  7,  0, 4]
list_of_c_edg = [8, 8, 10, 10, 11, 11, 9, 9]
fig, ax = plt.subplots(2, 4)

for j in range(0,4):
        ax[0, j].set_xlim(0, 7)
        ax[0, j].set_ylim(0, 7)
        ax[0, j].grid(True)

for j in range(0,4):
        ax[1, j].set_xlim(0, 7)
        ax[1, j].set_ylim(-7, 0)
        ax[1, j].grid(True)
phasa = np.arange(0, TIMES-1)
frames = []

# for p in phasa:
#     pats = []
#     for i in range(0, 8):
#         a = length_of_octahedron[list_of_a_edg[i], p]
#         b = length_of_octahedron[list_of_b_edg[i], p]
#         c = length_of_octahedron[list_of_c_edg[i], p]
#         cosine = (a**2 + c**2 - b**2)/(2*a*b)
#         sinus = np.sqrt(1. - cosine**2)
#         points = np.array([[0, 0.], [a * cosine, (-1)**i * a * sinus], [c, 0.]])
#         if i == 0:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('Red')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 1:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('Green')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 2:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('Blue')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 3:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('Yellow')
#             patch_.set_xy(points)
#             pats.append(patch_)
#         if i == 4:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('k')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 5:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('b')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 6:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('m')
#             patch_.set_xy(points)
#             pats.append(patch_)
#
#         elif i == 7:
#             patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
#             patch_.set_color('c')
#             patch_.set_xy(points)
#             pats.append(patch_)
#     line1 = ax[0, 0].add_patch(pats[0])
#     line2 = ax[1, 0].add_patch(pats[1])
#     line3 = ax[0, 1].add_patch(pats[2])
#     line4 = ax[1, 1].add_patch(pats[3])
#     line5 = ax[0, 2].add_patch(pats[4])
#     line6 = ax[1, 2].add_patch(pats[5])
#     line7 = ax[0, 3].add_patch(pats[6])
#     line8 = ax[1, 3].add_patch(pats[7])
#     frames.append([line1, line2, line3, line4, line5, line6, line7, line8])


ani = animation = ArtistAnimation(
    fig,                # фигура, где отображается анимация
    frames,              # кадры
    interval=30,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)       # зацикливать ли анимацию
ani.save('/Users/ruslanpepa/PycharmProjects/Octahedron/data/sine1_wave.gif', writer='pillow')
plt.show()