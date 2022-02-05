import random


import matplotlib.pyplot as plt
import numpy as np
import sys
from faces import Faces
from smeg_matrix import *
from animation import *
from rebuilding import Rebuilding

file_path = '/Users/ruslanpepa/PycharmProjects/Octahedron/octahedron.txt'
VERTEX = 6  # количество вершин в многограннике
EDGES = 12  # количество ребер в многограннике
FACES = 8  # количестов граней в многограннике
TIMES = 100 # количество шагов по времени
step_time = 0.0001  # шаг по времени
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
for ls in list_faces:
    print(ls[0], ls[1], ls[2])
for i in range(0, VERTEX):
    for j in range(0, VERTEX):
        print(length_matrix[i, j], end='\t')
    print(end='\n')
while True:
    for i in range(0, VERTEX):
        for j in range(i, VERTEX):
            if length_matrix[i, j] != 0:
                length_matrix[i, j] = length_matrix[j, i] = np.random.uniform(6.1, 7.1)
    if len(gauss_curve_calculate(length_matrix)) == VERTEX:
        break
numerate_of_edges = {} # Этот словарь для сопоставления номеров рёбер и вершин
ij = 0 # Переменная, которая нужна для того, чтобы нумеровать рёбра на октаедре
for i in range(0, VERTEX):
    for j in range(i, VERTEX):
        if length_matrix[i,j] != 0:
            length_of_octahedron[ij, 0] = length_matrix[i,j]
            numerate_of_edges[ij] = {i,j}
            ij += 1
print(numerate_of_edges)
print(length_of_octahedron[:,:4])
# for i in range(0, VERTEX):
#     for j in range(i, VERTEX):
#         if length_matrix[i, j] != 0:
#             length_matrix[i, j] = length_matrix[j, i] = random.uniform(4, 7)

gauss_curve = gauss_curve_calculate(length_matrix)

for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    print('gauss_curvature in vertex', i, gauss_curvature[i, 0])


for i in range(0, TIMES - 1):
    if i%100 == 0:
        print(i, 'hello')
    for j in range(0, VERTEX):
        # k1 = k2 = k3 = k4 = .0
        k0 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * conformal_weights[j, i]
        k1 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k0 / 2.)
        k2 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k1 / 2.)
        k3 = -(gauss_curve[j] - 4. * np.pi / VERTEX) * (conformal_weights[j, i] + step_time * k2)
        # print('(step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3):', (step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3))
        conformal_weights[j, i + 1] = conformal_weights[j, i] + (step_time / 6.) * (k0 + k1 * 2. + k2 * 2. + k3)
    # vector_times = conformal_weights[:, i]
    # print('kaly_menger:', keyle_menger_det(length_matrix, VERTEX))
    times = 0
    perestroyka = 0
    for fs in list_faces:
        a = length_matrix[fs[0], fs[1]]
        b = length_matrix[fs[1], fs[2]]
        c = length_matrix[fs[2], fs[0]]
        # print(fases_len_matrix.todense())
        half_perimetr = (a+b+c)/2.
        if half_perimetr*(half_perimetr - a)*(half_perimetr - b)*(half_perimetr - c) <= 0:
            print('Перестройка', perestroyka)
            perestroyka += 1
            rebuild = Rebuilding(list_faces, fs, length_matrix )
            rebuild.find_faces()
            rebuild.dell_faces()
            rebuild.new_faces()
            rebuild.new_length()
            sys.exit(0) # Преждевременное завершение программы
        else:
            kl_mng = np.sqrt(half_perimetr*(half_perimetr - a)*(half_perimetr - b)*(half_perimetr - c))
        kayli_manger[times, i+1] = kl_mng
        times += 1
        # print('keyli_menger:',kl_mng)

    i_lng_mtx = get_length(length_matrix, conformal_weights[:, i+1])  # Пересчитываем все длины сторон
    ij = 0
    for i1 in range(0, VERTEX):
        for j1 in range(i1, VERTEX):
            if length_matrix[i1, j1] != 0:
                length_of_octahedron[ij, i+1] = i_lng_mtx[i1, j1]
                ij +=1
                # numerate_of_edges[ij] = {i, j}
    gauss_curve = gauss_curve_calculate(i_lng_mtx)  # Пересчитываем все значения кривизн в вершинах тетраэдра
    if len(gauss_curve) != VERTEX:
        print('calculate gauss_curve return ', None)
        break
    if fasec_kayli_menger(i_lng_mtx) <= 0:
        print('keyle menger <= 0', 'step: ', i)
        break
    for j in range(0, VERTEX):
        gauss_curvature[j, i+1] = gauss_curve[j]
        max_gauss_curv[i+1] = max(gauss_curve)
        min_gauss_curv[i+1] = min(gauss_curve)
#     # print('gauss curve:', gauss_curve)
# ani = animation.FuncAnimation(fig, animate, np.arange(1, TIMES), init_func=init,
#                               interval=100, blit=True)
#
# ani.save('sine_wave.gif', writer='pillow')