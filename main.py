import matplotlib.pyplot as plt
import numpy as np
from gauss_calc import Gauss

from smeg_matrix import *
import matplotlib.patches as patches
from rebuilding import Rebuilding
from calculation import Calculate
from matplotlib.animation import ArtistAnimation
from matplotlib.ticker import NullLocator

# warnings.simplefilter('ignore', SparseEfficiencyWarning)
lc = NullLocator()

file_path = '/Users/ruslanpepa/PycharmProjects/Octahedron/tet_octahed.txt'
VERTEX = 5  # количество вершин в многограннике
EDGES = 9  # количество ребер в многограннике
FACES = 6  # количестов граней в многограннике
TIMES = 15  # количество шагов по времени
step_time = 0.01  # шаг по времени
list_faces = []  # список, который будет содержать все грани
with open(file_path) as fl_wth_fs:  # выгрузим из файла все номера вершин
    lines = fl_wth_fs.readlines()
for line in lines:  # все номера вершин загоним в списко файлову
    ns_vx = line.rstrip('\n').split('\t')  # получили только числа из каждой строки
    a = int(ns_vx[0])
    b = int(ns_vx[1])
    c = int(ns_vx[2])
    list_faces.append(Faces(a, b, c))
max_gauss_curv = np.ones(TIMES, float) # график максимальной кривизнв веришне 
min_gauss_curv = np.ones(TIMES, float) # график минимальной кривизнв веришне
conformal_weights = np.ones((VERTEX, TIMES), float)  # конформные веса в вершинах
gauss_curvature = np.zeros((VERTEX, TIMES), float) # гауссова кривизна в начальный момент времени
# length_matrix = sparse.coo_matrix((space_data, (space_row, space_col)), shape=(vertex, vertex)).tocsc() # матрица для того, чтобы
# length_of_octahedron = np.ones((EDGES, TIMES), float) # экспериментальная матрица для отображения длин рёбер
kayli_manger = np.zeros((FACES, TIMES), float) # массив, который будет содержать значения определителей Кэлли-Менгера на грани
adj_matx = adjacency_matrix(list_faces, VERTEX)  # матрица смежности длин рёбер
adj_matx_numpy = adj_matx.toarray()
for i in range(0, VERTEX):
    for j in range(0, VERTEX):
        if (adj_matx_numpy[i][j] != 0):
            adj_matx_numpy[i][j] = 1
        else:
            adj_matx_numpy[i][j] = 0

adj_matx_numpy.astype(int)
##создаём файл и записываем в него матрицу смежности
degenerate_faces = []

# print(degenerate_faces[0][0])
myfile = open("/Users/ruslanpepa/PycharmProjects/Octahedron/data/data_triang.txt", "w+")
string_matrix = '{'
for k in range(0, VERTEX):
    string_matrix += "{"
    for l in range(0, VERTEX):
        if l != VERTEX-1:
            string_matrix += (str(adj_matx_numpy[k][l].astype(int)) + ',')
        else:
            string_matrix += (str(adj_matx_numpy[k][l].astype(int)) )
    if k != VERTEX-1:
        string_matrix += "},"
    else:
        string_matrix += "}}"


myfile.write(string_matrix + '\n' + '\n')
myfile.close()



length_matrix = []
length_matrix.append(adj_matx)
times_of_finding = 0
# while True:
#     times_of_finding += 1
#     print("times_of_finding:", times_of_finding)
#     for i in range(0, VERTEX):
#         for j in range(i, VERTEX):
#             if adj_matx[i, j] != 0:
#                 length_matrix[0][i, j] = length_matrix[0][j,i] = np.random.uniform(5.0, 6.0)
#     while True:
#         random_i = np.random.randint(0, VERTEX)
#         random_j = np.random.randint(0, VERTEX)
#         if adj_matx[random_i, random_j] != 0:
#             break
    
#     # length_matrix[0][random_i, random_j] = length_matrix[0][random_j, random_i] = np.random.uniform(0.9, 1.2)
#     Gauss_Curve = Gauss(length_matrix[0], list_faces)
#     Gauss_Curve.date_prepare()
#     Gauss_Curve.gauss_calculate()
#     if Gauss_Curve.existence == 0:
#         break
#     # if len(gauss_curve_calculate(length_matrix[0])) != 0:
#         # break
# numerate_of_edges = {}

length_matrix[0][0, 1] = length_matrix[0][1, 0] = 0.421955
length_matrix[0][0, 2] = length_matrix[0][2, 0] = 0.591201
length_matrix[0][0, 3] = length_matrix[0][3, 0] = 0.557806
length_matrix[0][1, 2] = length_matrix[0][2, 1] = 0.294093
length_matrix[0][1, 3] = length_matrix[0][3, 1] = 0.899176
length_matrix[0][1, 4] = length_matrix[0][4, 1] = 0.764728
length_matrix[0][2, 3] = length_matrix[0][3, 2] = 0.145223
length_matrix[0][2, 4] = length_matrix[0][4, 2] = 0.70348
length_matrix[0][3, 4] = length_matrix[0][4, 3] = 0.752389



# Этот словарь для сопоставления номеров рёбер и вершин
# ij = 0 # Переменная, которая нужна для того, чтобы нумеровать рёбра на октаедре
# for i in range(0, VERTEX):
#     for j in range(i, VERTEX):
#         if length_matrix[i,j, 0] != 0:
#             length_of_octahedron[ij, 0] = length_matrix[i, j, 0]
#             numerate_of_edges[ij] = {i, j}
#             ij += 1
# for fs in list_faces:

prorisovka = 0

Gauss_Curve = Gauss(length_matrix[0], list_faces)
Gauss_Curve.date_prepare()
Gauss_Curve.gauss_calculate()
gauss_curve = Gauss_Curve.gauss_curve
# gauss_curve = gauss_curve_calculate(length_matrix[0], list_faces)


for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    # print('gauss_curvature in vertex', i, gauss_curvature[i, 0])
for j in range(0, VERTEX):
    for k in range(0, VERTEX):
        print(float("{0:.10f}".format(length_matrix[0][j, k])), end='\t')
    print('\n')


# gauss_curve = gauss_curve_calculate(length_matrix[0], list_faces)

for i in range(0, VERTEX):
    gauss_curvature[i, 0] = gauss_curve[i]
    # print('gauss_curvature in vertex', i, gauss_curvature[i, 0])



perestroyka = 0
for i in range(0, TIMES - 1):
    str_for_faces = str()
    degenerate_face = Faces(0, 0, 0)
    exceptions = 0
    # print(i, 'hello world')
    calc = Calculate(gauss_curvature[:, i], list_faces, conformal_weights[:, 0])
    conformal_weights[:, i+1] = calc.weight_calculate() # Пересчитываем конфорные веса
    length_matrix.append(get_matrix_lenght(length_matrix[i], conformal_weights[:, i + 1 ], VERTEX))  # вычисляем матрицу длин рёбер

    times_for_faces = 0

    klmng = set()
    generate_faces = Faces(0, 0, 0)
    deg_face = []
    for fs in list_faces:
        times_for_faces += 1
        a = length_matrix[i + 1][fs[0], fs[1]]
        b = length_matrix[i + 1][fs[1], fs[2]]
        c = length_matrix[i + 1][fs[2], fs[0]]
        # print(a, b, c)


        hafl_perim = (a + b + c)/2.
        kl_mng = 0
        # print('sting NUMBER 86: exception:', exceptions)
        kl_mng = float("{0:.10f}".format(hafl_perim * (hafl_perim - a) * (hafl_perim - b) * (hafl_perim - c)))
        print(kl_mng)
        klmng.add(kl_mng)
        # print('times_for_faces%', times_for_faces,kl_mng )

        if kl_mng > 0:
            # kl_mng = Error:failed to create a child event loop
            # print('try', half_perimetr * (half_perimetr - a) * (half_perimetr - b) * (half_perimetr - c))
            a_cos = (b ** 2 + c ** 2 - a ** 2) / (2. * c * b)
            b_cos = (c ** 2 + a ** 2 - b ** 2) / (2. * a * c)
            c_cos = (a ** 2 + b ** 2 - c ** 2) / (2. * a * b)
            a_sin = np.sqrt(1. - a_cos ** 2)
            b_sin = np.sqrt(1. - b_cos ** 2)
            c_sin = np.sqrt(1. - c_cos ** 2)
            # print("keyli menger:", kl_mng)
            # kayli_manger[TIMES, i + 1] = kl_mng
        else:
            deg_face.append(fs)
            a_fs = length_matrix[i + 1][fs[0], fs[1]]
            b_fs = length_matrix[i + 1][fs[1], fs[2]]
            c_fs = length_matrix[i + 1][fs[2], fs[0]]
            max_str = str()
            if a_fs == max(a_fs, b_fs, c_fs):
                max_str += (' maximalnoe rebro = ' + str(fs[0]) + str(fs[1]) )
            if b == max(a_fs, b_fs, c_fs):
                max_str += (' maximalnoe rebro = ' + str(fs[0]) + str(fs[2]))
            if c == max(a_fs, b_fs, c_fs):
                max_str += (' maximalnoe rebro = ' + str(fs[1]) + str(fs[2]))

            max_rebro = str(max(a_fs, b_fs, c_fs))
            str_for_faces += (str(fs[0]) + str(fs[1]) + str(fs[2]) + ' shag po vremeny ' + str(i) + max_str + ' \n')
    print("КОЛИЧЕСТВО ВЫРОЖДЕННЫХ ГРАНЕЙ РАВНО: ", len(deg_face))
    for sf in deg_face:
        degenerate_face = sf
        exceptions = 1
        print('Перестройка №_', perestroyka, 'шаг по времени: ', i)
        perestroyka += 1

        print('pered tem kak sozdat class rebuild')
        rebuild = Rebuilding(list_faces, sf, length_matrix[i + 1])
        rebuild.find_faces()
        rebuild.dell_faces()
        list_faces = rebuild.new_faces()
        length_matrix.append(rebuild.new_length())
        gaus_curv = Gauss(length_matrix[i + 1],list_faces)
        gaus_curv.date_prepare()
        gaus_curv.gauss_calculate()
        if gaus_curv.existence == 1:
            break

        out_of_triangulation(adjacency_matrix(list_faces, VERTEX).toarray(), VERTEX, i)
        print('perestroyka zakonchena', 'шаг по времени равен', i)



    #     exceptions = 0
    try:
        # length_of_octahedron[:, i + 1] = get_lenght(i_lng_mtx, VERTEX)  # длину рёбер октаэдра вносим в массив длин ребер
        prorisovka = i
        # print('do otkrytiya file')

        length_file = open("/Users/ruslanpepa/PycharmProjects/Octahedron/data/lenght_file.txt", "a")
        # print('posle otkrytiya file')
        length_file.write(str_for_faces + '\n')
        # print('posle zapisy v file')
        length_file.close()
        # print('posle zakrytiya file')
        for k in range(0, VERTEX):
            for l in range(0, VERTEX):
                if length_matrix[i][k, l] != 0:
                    length_file = open("/Users/ruslanpepa/PycharmProjects/Octahedron/data/lenght_file.txt", "a")
                    length_file.write(str(k) + str(l) + "=" + str(length_matrix[i][k, l])  + '\t' + str(i) + '\n')
                    length_file.close()
        # print('pered podschetom krivizn')
        # gauss_curve = gauss_curve_calculate(length_matrix[i + 1])  # пересчитываем гаусовы кривизны
        gaus_curv = Gauss(length_matrix[i + 1], list_faces )
        gaus_curv.date_prepare()
        gaus_curv.gauss_calculate()

        if gaus_curv.existence == 1:
            break
        # for j in range(0, VERTEX):
        #     gauss_curvature[j, i+1] = gaus_curv.gauss_curve
    except:
        print("perestroyka ne udalas")
        prorisovka = i
        break

    # degenerate_faces.append(deg_face)
    gauss_curve = gauss_curve_calculate(length_matrix[i+1], list_faces)

    for j in range(0, VERTEX):
        gauss_curvature[j, i+1] = gauss_curve[j]
    # Gaus_curv_i = Gauss(length_matrix[i], list_faces)
    # Gaus_curv_i.date_prepare()
    # Gaus_curv_i.gauss_calculate()
    # gauss_curvature[:, i+1] = Gaus_curv_i.gauss_curve




list_of_a_edg = [0, 4, 1, 5, 2, 6, 3, 7]
list_of_b_edg = [1, 5, 2, 6, 3, 7, 0, 4]
list_of_c_edg = [8, 8, 10, 10, 11, 11, 9, 9]

fig, ax = plt.subplots(2, 3)

for j in range(0, 3):
        ax[0, j].set_xlim(0, 8)
        ax[0, j].set_ylim(0, 8)
        ax[0, j].grid(True)

for j in range(0, 3):
        ax[1, j].set_xlim(0, 8)
        ax[1, j].set_ylim(-8, 0)
        ax[1, j].grid(True)
phasa = np.arange(0, len(length_matrix))
frames = []

for p in phasa:
    pats = []
    for i in range(0, 6):
        a = length_matrix[p][list_faces[i][0], list_faces[i][1]]
        b = length_matrix[p][list_faces[i][1], list_faces[i][2]]
        c = length_matrix[p][list_faces[i][2], list_faces[i][0]]
        # a = length_of_octahedron[list_of_a_edg[i], p]
        # b = length_of_octahedron[list_of_b_edg[i], p]
        # c = length_of_octahedron[list_of_c_edg[i], p]
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
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[0,0].legend(legend)

        elif i == 1:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Green')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[1, 0].legend(legend)

        elif i == 2:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Blue')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[0,1].legend(legend)

        elif i == 3:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('Yellow')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[1,1].legend(legend)
        if i == 4:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('k')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[0,2].legend(legend)

        elif i == 5:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('b')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[1,2].legend(legend)

        elif i == 6:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('m')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[0,3].legend(legend)

        elif i == 7:
            patch_ = patches.Polygon(points, closed=False, fc='r', ec='r', alpha=0.4)
            patch_.set_color('c')
            patch_.set_xy(points)
            pats.append(patch_)
            legend = str(list_faces[i][0]) + str(list_faces[i][1]) + str(list_faces[i][2])
            ax[1, 3].legend(legend)
    line1 = ax[0, 0].add_patch(pats[0])
    # line.set_label('la-la-la')
    # ax[0,0].legend()
    line2 = ax[1, 0].add_patch(pats[1])
    line3 = ax[0, 1].add_patch(pats[2])
    line4 = ax[1, 1].add_patch(pats[3])
    line5 = ax[0, 2].add_patch(pats[4])
    line6 = ax[1, 2].add_patch(pats[5])
    # line7 = ax[0, 3].add_patch(pats[6])
    # line8 = ax[1, 3].add_patch(pats[7])
    frames.append([line1, line2, line3, line4, line5, line6])


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
