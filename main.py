import random


import matplotlib.pyplot as plt
import numpy as np

from faces import Faces
from smeg_matrix import *
# from animation import *
from rebuilding import Rebuilding

file_path = '/Users/ruslanpepa/PycharmProjects/Octahedron/octahedron.txt'
VERTEX = 6  # количество вершин в многограннике
EDGES = 12  # количество ребер в многограннике
FACES = 8  # количестов граней в многограннике
TIMES = 12000 # количество шагов по времени
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
                length_matrix[i, j] = length_matrix[j, i] = random.uniform(1, 7)
    if len(gauss_curve_calculate(length_matrix)) == VERTEX:
        break
# for i in range(0, VERTEX):
#     for j in range(i, VERTEX):
#         if length_matrix[i, j] != 0:
#             length_matrix[i, j] = length_matrix[j, i] = random.uniform(4, 7)

gauss_curve = gauss_curve_calculate(length_matrix)

for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    print('gauss_curvature in vertex', i, gauss_curvature[i, 0])


for i in range(0, TIMES - 1):
    if i%1000 == 0:
        print(i)
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
    for fs in list_faces:
        a = length_matrix[fs[0], fs[1]]
        b = length_matrix[fs[1], fs[2]]
        c = length_matrix[fs[2], fs[0]]
        # print(fases_len_matrix.todense())
        half_perimetr = (a+b+c)/2.
        if half_perimetr*(half_perimetr - a)*(half_perimetr - b)*(half_perimetr - c) <= 0:
            rebuild = Rebuilding(list_faces, fs, length_matrix)
            rebuild.find_faces()
            print(i)

           ######################################################################################################
           ####                                                                                             #####
           #### ЗДЕСЬ НАЧИНАЕТСЯ КОД НА СЛУЧАЙ ЕСЛИ ОДНА ИЗ ГРАНЕЙ СХЛОПНИТСЯ И НАДО СДЕЛАТЬ ПЕРЕСТРОЙКУ    #####

           #### ЗДЕСЬ ЗАКАНЧИВАЕТСЯ КОД НА СЛУЧАЙ ЕСЛИ ОДНА ИЗ ГРАНЕЙ СХЛОПНИТСЯ И НАДО СДЕЛАТЬ ПЕРЕСТРОЙКУ #####
           ####                                                                                             #####
           ######################################################################################################
            break
        else:
            kl_mng = np.sqrt(half_perimetr*(half_perimetr - a)*(half_perimetr - b)*(half_perimetr - c))
        kayli_manger[times, i+1] = kl_mng
        times += 1
        # print('keyli_menger:',kl_mng)

    i_lng_mtx = get_length(length_matrix, conformal_weights[:, i+1])  # Пересчитываем все длины сторон
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
    # print('gauss curve:', gauss_curve)
