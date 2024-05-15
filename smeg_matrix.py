# функция, которая будет создавать матрицу смежности
import math

import numpy as np
from scipy import sparse
from faces import Faces

def column(matrix, i):
    return [row[i] for row in matrix]
# функция, которая создает матрицу смежности
def adjacency_matrix(faces, vertex):
    row = []
    col = []
    for fs in faces:
        row.append(fs[0])
        row.append(fs[1])
        col.append(fs[1])
        col.append(fs[0])

        row.append(fs[1])
        row.append(fs[2])
        col.append(fs[2])
        col.append(fs[1])

        row.append(fs[2])
        row.append(fs[0])
        col.append(fs[0])
        col.append(fs[2])
    # print('row and col:','\n', row ,'\n',  col)
    data = [1.] * len(row)  # массив единиц, нужен для конструктора разреженной матрицы
    space_row = np.array(row)
    space_col = np.array(col)
    space_data = np.array(data)
    adj_max = sparse.coo_matrix((space_data, (space_row, space_col)), shape=(vertex, vertex)).tocsc()

    return adj_max


def gauss_curve_calculate(matrix_length, fasec_list):
    lst_fscs = []
    for lfs in fasec_list:
        lst_fscs.append(sorted([lfs[0], lfs[1], lfs[2]]))
        # print(lfs[0], lfs[1], lfs[2])

    row, col = matrix_length.nonzero()  # в
    dictinary_vertex = {}  # вспомогательный словарь, ключ -- номер вершины, значение -- список вершин, смежных с ключом
    dictinary_gauss = {}  # ключ -- вершина, значение -- пара вершин, которая с ключевой формирует грань
    for j in range(0, matrix_length.count_nonzero()):
        if row[j] not in dictinary_vertex.keys():
            dictinary_vertex[row[j]] = [col[j]]
        else:
            dictinary_vertex[row[j]].append(col[j])
    for key, val in dictinary_vertex.items():
        list_of_adjency_vertex = []
        for i in val:
            for j in val:
                if matrix_length[i, j] != 0 and matrix_length[j, i] != 0 and (sorted([key, i, j]) in lst_fscs):
                    list_of_adjency_vertex.append(sorted([i, j]))
        dictinary_gauss[key] = list(map(list, {tuple(x) for x in list_of_adjency_vertex}))
    for key, arr in dictinary_vertex.items():
        print(key, '\t', len(arr))
    # print(dictinary_vertex)
    # print("dictinary_gauss: ", dictinary_gauss)
    # print(dictinary_vertex)
    gauss_curve = np.full(len(dictinary_gauss), 2. * np.pi)
    exeptions = 0
    klmng = set()
    for key, val in dictinary_gauss.items():
        for v in val:
            a = matrix_length[v[0], v[1]]
            b = matrix_length[v[1], key]
            c = matrix_length[v[0], key]


            a_cos = (b ** 2 + c ** 2 - a ** 2) / (2. * c * b)
            # print(key,'\t',"naprotiv", v[0], v[1])
            # print("a_cos: ", a_cos)

            hafl_perim = (a + b + c)/2.

            kl_mng = float("{0:.1f}".format(hafl_perim*(hafl_perim - a)*(hafl_perim - b) * (hafl_perim - c)))
            klmng.add(kl_mng)
            # print('gauss calc', kl_mng)
            if kl_mng >= 0:
                gauss_curve[key] -= np.arccos(a_cos)
            else:
                # print("gauss_curve РАВНО НУЛЮ")
                gauss_curve[key] = 0
                exeptions = 1

    # print('gauss curve calculate', klmng)
    if exeptions == 1:
        return -1
    else:
        return gauss_curve


def keyle_menger_det(mtx_length, vtx):
    num_vertex = vtx + 1
    cayle_menger_matrix = np.zeros((num_vertex, num_vertex), float)
    for i in range(0, num_vertex):
        for j in range(0, num_vertex):
            if i == j:
                cayle_menger_matrix[i, j] = 0
            elif i == 0:
                cayle_menger_matrix[i, j] = 1.
            elif j == 0:
                cayle_menger_matrix[i, j] = 1.
            else:
                cayle_menger_matrix[i, j] = mtx_length[i - 1, j - 1] ** 2
    # print(cayle_menger_matrix)
    determinant = ((-1) ** ((vtx-1) + 1) / ((2 ** (vtx-1)) * (math.factorial(vtx - 1)) ** 2)) * np.linalg.det(cayle_menger_matrix)
    # print( 'determinant:', determinant)
    return determinant



def get_matrix_lenght(lenth, cmfrU, vrtx):
    row, col = lenth.nonzero()
    data = [1.] * len(row)

    space_row = np.array(row)
    space_col = np.array(col)
    space_data = np.array(data)
    new_length_matrix = sparse.coo_matrix((space_data, (space_row, space_col)), shape=(vrtx, vrtx), dtype = 'd').tocsc()

    # print('to_dense:', lenth.todense())
    # print('row:', row, 'col:', col, lenth.data)
    # print('size_row:', len(row), 'size_col:', len(col), 'size_data: ', len(lenth.data))
    for j in range(0, len(row)):
        new_length_matrix[row[j], col[j]] = lenth[row[j], col[j]] * cmfrU[row[j]] * cmfrU[col[j]]
        new_length_matrix[col[j], row[j]] = lenth[col[j], row[j]] * cmfrU[col[j]] * cmfrU[row[j]]
        # for i in range(0, len(cmfrU)):
    #     for j in range(0, len(cmfrU)):

    return new_length_matrix


def get_lenght(matrix_lenght, vrtx):
    new_length_edges = []
    for i1 in range(0, vrtx):
        for j1 in range(i1, vrtx):
            if matrix_lenght[i1, j1] != 0:
                new_length_edges.append(matrix_lenght[i1, j1])
    return new_length_edges

def fasec_kayli_menger (matrix_length):
    row, col = matrix_length.nonzero()  # в
    dictinary_vertex = {}  # вспомогательный словарь, ключ -- номер вершины, значение -- список вершин, смежных с ключом
    dictinary_gauss = {}  # ключ -- вершина, значение -- пара вершин, которая с ключевой формирует грань
    for j in range(0, matrix_length.count_nonzero()):
        if row[j] not in dictinary_vertex.keys():
            dictinary_vertex[row[j]] = [col[j]]
        else:
            dictinary_vertex[row[j]].append(col[j])
    for key, val in dictinary_vertex.items():
        list_of_adjency_vertex = []
        for i in val:
            for j in val:
                if matrix_length[i, j] != 0 and matrix_length[j, i] != 0:
                    list_of_adjency_vertex.append(sorted([i, j]))
        dictinary_gauss[key] = list(map(list, {tuple(x) for x in list_of_adjency_vertex}))
    # print(dictinary_vertex)

    for key, val in dictinary_gauss.items():
        for v in val:
            a = matrix_length[v[0], v[1]]
            b = matrix_length[v[1], key]
            c = matrix_length[v[0], key]
            val_arccos = (b ** 2 + c ** 2 - a ** 2) / (2 * c * b)
            if (1 < val_arccos or val_arccos < -1):
                return False  # если не выполнено неравенство треугольника, то функция возвращает None
    # print('gauss_curve', gauss_curve)
    return True



#####
##### def_face --- вырожденная грань
##### smeg_face --- смежная с вырожденной гранью

def out_of_triangulation(adj_matx_numpy, VERTEX, i):
    for i in range(0, VERTEX):
        for j in range(0, VERTEX):
            if (adj_matx_numpy[i][j] != 0):
                adj_matx_numpy[i][j] = 1
            else:
                adj_matx_numpy[i][j] = 0

    adj_matx_numpy.astype(int)
    ##создаём файл и записываем в него матрицу смежности
    string_matrix = '{'
    for k in range(0, VERTEX):
        string_matrix += "{"
        for l in range(0, VERTEX):
            if l != VERTEX - 1:
                string_matrix += (str(adj_matx_numpy[k][l].astype(int)) + ',')
            else:
                string_matrix += (str(adj_matx_numpy[k][l].astype(int)))
        if k != VERTEX - 1:
            string_matrix += ("},")
        else:
            string_matrix += "}}"


    # print(string_matrix)
    myfile = open("/Users/ruslanpepa/PycharmProjects/Octahedron/data/data_triang.txt", "a")
    myfile.write(string_matrix + '\n' + '\n')
    myfile.close()

def restructuring(list_of_faсes, deg_face, length_mtx):
    a = length_mtx[deg_face[0], deg_face[1]]
    b = length_mtx[deg_face[0], deg_face[2]]
    c = length_mtx[deg_face[2], deg_face[1]]
    if a == max(a, b, c):
        vrtx = {deg_face[0], deg_face[1]}
    elif b == max(a, b, c):
        vrtx = {deg_face[0], deg_face[2]}
    elif c == max(a, b, c):
        vrtx = {deg_face[2], deg_face[1]}
    # создами множество из номеров вершин грани, если это множесвто содержит множетсво двух вершин, к
    for i in range(0, len(list_of_faсes)):
        set_of_vrtx = {list_of_faсes[i][0], list_of_faсes[i][1], list_of_faсes[i][2]}
        if vrtx.issubset(set_of_vrtx):
            smeg_face = list_of_faсes[i]
            list_of_faсes.pop(i)


    ##### создадим два списка с номерами вершин, которые образют две смежные грани
    first_face = [deg_face[0], deg_face[1], deg_face[2]]
    scnd_face = [smeg_face[0], smeg_face[1], smeg_face[2]]
    set_smeg_fase = set(scnd_face)
    for i in scnd_face:
        if not (set(i).issubset(set_smeg_fase)):
            need_vrt = i

    ##### пробегаемся по элементам обоих списсков, находим элементы, которые содержаться в одном и только одном из них
    ##### эти два элемента буду находится в двух новых гранях
    for i in first_face:
        for j in scnd_face:
            if i not in scnd_face and j not in first_face:
                new_edge = [i, j]
            elif i in scnd_face and j in first_face and i != j : # необходимо будет удалить одно из рёбер
                old_edge = [i, j]
    #### пробегаем по номерам вершин одной из старых граней, если вершины нет в новом ребре, которое будет соединять две
    #### новые грани, так как какждая из старых граней содержит по две одинаковые вершины


    for i in first_face:
        if i not in new_edge:
            list_of_faсes.append(Faces(i, new_edge[0], new_edge[1]))
    new_length = adjacency_matrix(list_of_faсes, len(list_of_faсes))
    # удаляем одно из рёбер
    new_length[old_edge[0], old_edge[1]] = new_length[old_edge[1], old_edge[0]] = 0.

    for i in range(0, len(list_of_faсes)):
        for j in range(i, len(list_of_faсes)):
            if new_length[i, j] != 0:
                new_length[i, j] = new_length[j, i] = length_mtx[i, j]
    # length_of_new_edge =
    # new_length[new_edge[0], new_edge[1]] = new_length[new_edge[1], new_edge[0]] =



















































