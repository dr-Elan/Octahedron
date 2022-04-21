import matplotlib.pyplot as plt
import numpy as np

from smeg_matrix import *
import matplotlib.patches as patches
from rebuilding import Rebuilding
from calculation import Calculate
from matplotlib.animation import ArtistAnimation
from matplotlib.ticker import NullLocator
lc = NullLocator()

file_path = '/Users/ruslanpepa/PycharmProjects/Octahedron/octahedron.txt'
VERTEX = 6  # количество вершин в многограннике
EDGES = 12  # количество ребер в многограннике
FACES = 8  # количестов граней в многограннике
TIMES = 1000 # количество шагов по времени
step_time = 0.001  # шаг по времени
list_faces = []  # список, который будет содержать все грани
with open(file_path) as fl_wth_fs:  # выгрузим из файла все номера вершин
    lines = fl_wth_fs.readlines()
for line in lines:  # все номера вершин загоним в списко файлов
    ns_vx = line.rstrip('\n').split('\t')  # получили только числа из каждой строки
    a = int(ns_vx[0])
    b = int(ns_vx[1])
    c = int(ns_vx[2])
    list_faces.append(Faces(a, b, c))
max_gauss_curv = np.ones(TIMES, float) # график максимальной кривизнв веришне
min_gauss_curv = np.ones(TIMES, float) # график минимальной кривизнв веришне
conformal_weights = np.ones((VERTEX, TIMES), float)  # конформные веса в вершинах
gauss_curvature = np.zeros((VERTEX, TIMES), float) # гауссова кривизна в начальный момент времени
length_of_octahedron = np.ones((EDGES, TIMES), float) # экспериментальная матрица для отображения длин рёбер
kayli_manger = np.zeros((FACES, TIMES), float) # массив, который будет содержать значения определителей Кэлли-Менгера на грани
length_matrix = adjacency_matrix(list_faces, VERTEX)  # матрица смежности длин рёбер

times_of_finding = 0
while True:
    times_of_finding += 1
    print("times_of_finding:", times_of_finding)
    for i in range(0, VERTEX):
        for j in range(i, VERTEX):
            if length_matrix[i, j] != 0:
                length_matrix[i, j] = length_matrix[j, i] = np.random.uniform(5.0, 7.1)
    if len(gauss_curve_calculate(length_matrix)) != 0:
        break
numerate_of_edges = {} # Этот словарь для сопоставления номеров рёбер и вершин
ij = 0 # Переменная, которая нужна для того, чтобы нумеровать рёбра на октаедре
for i in range(0, VERTEX):
    for j in range(i, VERTEX):
        if length_matrix[i,j] != 0:
            length_of_octahedron[ij, 0] = length_matrix[i,j]
            numerate_of_edges[ij] = {i, j}
            ij += 1



gauss_curve = gauss_curve_calculate(length_matrix)

for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    # print('gauss_curvature in vertex', i, gauss_curvature[i, 0])
for j in range(0, VERTEX):
    for k in range(0, VERTEX):
        print(float("{0:.1f}".format(length_matrix[i, j])), end='\t')
    print('\n')
for i in range(0, TIMES - 1):

    # print(i, 'hello world')
    calc = Calculate(length_of_octahedron, gauss_curvature[:, 0], list_faces, conformal_weights[:, i])
    conformal_weights[:, i+1] = calc.weight_calculate() # Пересчитываем конфорные веса
    i_lng_mtx = get_matrix_lenght(length_matrix, conformal_weights[:, i + 1], VERTEX)  # вычисляем матрицу длин рёбер

    times = 0
    perestroyka = 0

    for fs in list_faces:
        a = i_lng_mtx[fs[0], fs[1]]
        b = i_lng_mtx[fs[1], fs[2]]
        c = i_lng_mtx[fs[2], fs[0]]
        exceptions = 0
        half_perimetr = (a + b + c) / 2.
        if half_perimetr >= 0:
            exceptions = 0
        else:
            exceptions = 1
        kl_mng = 0

        try:
            print('try')
            kl_mng =np.sqrt(half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))
            a_cos = (b ** 2 + c ** 2 - a ** 2) / (2 * c * b)
            b_cos = (c ** 2 + a ** 2 - b ** 2) / (2 * a * c)
            c_cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
            a_sin = np.sqrt(1. - a_cos**2)
            b_sin = np.sqrt(1. - b_cos ** 2)
            c_sin = np.sqrt(1. - c_cos ** 2)
            # print("keyli menger:", kl_mng)
            kayli_manger[times, i + 1] = kl_mng
        except:
            print('Перестройка №_', perestroyka)
            perestroyka += 1
            exceptions = 1
            exit(0)
        if exceptions == 1:

            print('pered tem kak sozdat class rebuild')
            rebuild = Rebuilding(list_faces, fs, length_matrix)
            rebuild.find_faces()
            rebuild.dell_faces()
            list_faces = rebuild.new_faces()
            i_lng_mtx = rebuild.new_length()
            kayli_manger[times, i + 1] = kl_mng
            times += 1
            print('perestroyka zakonchena')
        if len(gauss_curve_calculate(i_lng_mtx)) == 0:
            print("perestroyka ne udalas")
            break
        else:
            length_of_octahedron[:, i + 1] = get_lenght(i_lng_mtx, VERTEX)  # длину рёбер октаэдра вносим в массив длин ребер
            gauss_curve = gauss_curve_calculate(i_lng_mtx)  # пересчитываем гаусовы кривизны
            # exit(0)





list_of_a_edg = [0, 4, 1, 5, 2, 6, 3, 7]
list_of_b_edg = [1, 5, 2, 6, 3, 7, 0, 4]
list_of_c_edg = [8, 8, 10, 10, 11, 11, 9, 9]

fig, ax = plt.subplots(2, 4)

for j in range(0, 4):
        ax[0, j].set_xlim(0, 7)
        ax[0, j].set_ylim(0, 7)
        ax[0, j].grid(True)

for j in range(0, 4):
        ax[1, j].set_xlim(0, 7)
        ax[1, j].set_ylim(-7, 0)
        ax[1, j].grid(True)
phasa = np.arange(0, TIMES-1)
frames = []

for p in phasa:
    pats = []
    for i in range(0, 8):
        a = length_of_octahedron[list_of_a_edg[i], p]
        b = length_of_octahedron[list_of_b_edg[i], p]
        c = length_of_octahedron[list_of_c_edg[i], p]
        b_cosine = (a**2 + c**2 - b**2)/(2.*a*c)
        if 1. - b_cosine**2 >= 0:
            b_sinus = np.sqrt(1. - b_cosine**2)
        else:
            b_sinus = 0
        points = np.array([[0, 0.], [a * b_cosine, (-1)**i * a * b_sinus], [c, 0.]])
        if i == 0:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Red')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 1:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Green')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 2:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Blue')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 3:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Yellow')
            patch_.set_xy(points)
            pats.append(patch_)
        if i == 4:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('k')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 5:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('b')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 6:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('m')
            patch_.set_xy(points)
            pats.append(patch_)

        elif i == 7:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('c')
            patch_.set_xy(points)
            pats.append(patch_)
    line1 = ax[0, 0].add_patch(pats[0])
    line2 = ax[1, 0].add_patch(pats[1])
    line3 = ax[0, 1].add_patch(pats[2])
    line4 = ax[1, 1].add_patch(pats[3])
    line5 = ax[0, 2].add_patch(pats[4])
    line6 = ax[1, 2].add_patch(pats[5])
    line7 = ax[0, 3].add_patch(pats[6])
    line8 = ax[1, 3].add_patch(pats[7])
    frames.append([line1, line2, line3, line4, line5, line6, line7, line8])


ani = animation = ArtistAnimation(
    fig,                # фигура, где отображается анимация
    frames,              # кадры
    interval=30,        # задержка между кадрами в мс
    blit=True,          # использовать ли двойную буферизацию
    repeat=True)       # зацикливать ли анимацию
ani.save('/Users/ruslanpepa/PycharmProjects/Octahedron/data/sine1_wave.gif', writer='pillow')
plt.show()




exit(0)















        # print('keyli_menger:',kl_mng)
    # conformal_weights[:, i] = calc.weight_calculate()
#     for j in range(0, VERTEX):
#         # k1 = k2 = k3 = k4 = .0
#         k0 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * conformal_weights[j, i]
#         k1 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k0 / 2.)
#         k2 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k1 / 2.)
#         k3 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k2)
#         # print('(step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3):', (step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3))
#         conformal_weights[j, i + 1] = conformal_weights[j, i] + (step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3)
#     # vector_times = conformal_weights[:, i]
#     # print('kaly_menger:', keyle_menger_det(length_matrix, VERTEX))

#
#
#     i_lng_mtx = get_length(length_matrix, conformal_weights[:, i+1])  # Пересчитываем все длины сторон
#     ij = 0
#     for i1 in range(0, VERTEX):
#         for j1 in range(i1, VERTEX):
#             if length_matrix[i1, j1] != 0:
#                 length_of_octahedron[ij, i+1] = i_lng_mtx[i1, j1]
#                 ij += 1
#                 # numerate_of_edges[ij] = {i, j}
#     gauss_curve = gauss_curve_calculate(i_lng_mtx)  # Пересчитываем все значения кривизн в вершинах тетраэдра
#     if len(gauss_curve) != VERTEX:
#         print('calculate gauss_curve return ', None)
#         break
#     if fasec_kayli_menger(i_lng_mtx) <= 0:
#         print('keyle menger <= 0', 'step: ', i)
#         break
#     for j in range(0, VERTEX):
#         gauss_curvature[j, i+1] = gauss_curve[j]
#         max_gauss_curv[i+1] = max(gauss_curve)
#         min_gauss_curv[i+1] = min(gauss_curve)
#

# ani = animation.FuncAnimation(fig, animate, np.arange(1, TIMES), init_func=init,
#                               interval=100, blit=True)
#
# ani.save('sine_wave.gif', writer='pillow')
