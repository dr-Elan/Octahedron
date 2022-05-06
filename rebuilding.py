import numpy as np
from smeg_matrix import adjacency_matrix

from faces import Faces
class Rebuilding():
    """ Здесь будет проходить перестройка триангуляции """
    def __init__(self, list_of_faces, deg_face, lenth_mtx):
        self.l_o_f = list_of_faces
        self.dg_fc = deg_face
        self.l_mtx = lenth_mtx
        self.set_of_vertex = set()
        for i in range(0, len(self.l_o_f)):
            self.set_of_vertex.add(self.l_o_f[i][0])
            self.set_of_vertex.add(self.l_o_f[i][1])
            self.set_of_vertex.add(self.l_o_f[i][2])
        print("создаём класс", self.set_of_vertex)
        # for i in range(0, len(self.l_o_f)):
        #     print('initialisation', self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2])

    def find_faces(self):
        self.a = self.l_mtx[self.dg_fc[0], self.dg_fc[1]]
        self.b = self.l_mtx[self.dg_fc[1], self.dg_fc[2]]
        self.c = self.l_mtx[self.dg_fc[0], self.dg_fc[2]]
        print('find_faces')
        if self.a == max(self.a, self.b, self.c):
            self.old_edge = {self.dg_fc[0], self.dg_fc[1]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[2]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера
        elif self.b == max(self.a, self.b, self.c):
            self.old_edge = {self.dg_fc[0], self.dg_fc[2]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[1]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера
        else:
            self.old_edge = {self.dg_fc[1], self.dg_fc[2]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[0]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера
        print(self.old_edge, 'ребро для удаления', self.vrtx, "вершина")

        for i in range(0, len(self.l_o_f)):
            set_of_vrtx = {self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2]}
            if self.old_edge.issubset(set_of_vrtx):
                if self.vrtx.issubset(set_of_vrtx):
                    self.degenerat_face = self.l_o_f[i]

                    print('вырожденная грань:', self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2])
                else:
                    self.smeg_face = self.l_o_f[i]
                    print('смежная с вырожденной гранью:', self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2])

        return print(self.smeg_face[0], self.smeg_face[1], self.smeg_face[2], "сlass Rebuild , find smeg faces", '\n',
                     self.dg_fc[0], self.degenerat_face[1], self.degenerat_face[2], "сlass Rebuild , find  degenerate function")

    def dell_faces(self):
        "создаем множество из вершин грани, если оно содержится в множестве вершин вырожденной грани, то удаляем грань"
        for i in range(0, len(self.l_o_f)):
            # print(self.old_edge, 'dell function', '\t', self.l_o_f[i][0], '\t', self.l_o_f[i][1], '\t', self.l_o_f[i][2])
            set_of_vertex_faces = {self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2]}
            if self.old_edge.issubset(set_of_vertex_faces):
                self.l_o_f.pop(i)
                print('удаляем вырожденную грань')
                break

        "создаем множество из вершин грани, если оно содержится в множестве вершин вырожденной грани, то удаляем грань"
        for i in range(0, len(self.l_o_f)):
            set_of_vertex_faces = {self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2]}
            if self.old_edge.issubset({self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2]}):
                self.l_o_f.pop(i)
                print('удалем смежную с вырожденной грань')
                break
        for i in range(0, len(self.l_o_f)):
            print(self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2])
    def new_faces(self):
        self.vrx_of_deg = {self.degenerat_face[0], self.degenerat_face[1], self.degenerat_face[2]} # ножество вершин вырожденной грани
        self.vrx_of_smg = {self.smeg_face[0], self.smeg_face[1],self.smeg_face[2]} # множество вершин смежной с вырожденной гранью
        # self.a , self.b -- список вершин, который состоит всего из одного элемента,
        self.a = list(self.vrx_of_deg.difference(self.old_edge)) # вершина, которая не входит в ребро для удаления, но содержится в вырожденной грани
        self.b = list(self.vrx_of_smg.difference(self.old_edge)) # вершина, которая не входит, в ребро для удаления, но содержится в смежной с вырожденной гранью
        for i in self.old_edge:
            self.l_o_f.append(Faces(self.a[0], self.b[0], i))
            # print(self.a[0], self.b[0], i)
        # print(self.a, self.b, self.old_edge[0])
        # print(self.a, self.b, self.old_edge[1])
        # self.l_o_f.append(Faces(fst_vtx, scn_vtx, self.old_edge[0]))
        # self.l_o_f.append(Faces(fst_vtx, scn_vtx, self.old_edge[1]))
        print('выводим список новых граней')
        for i in range(0, len(self.l_o_f)):
            print('hello, operation new_faces, rebuilding class:', self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2])
        # self.adj_matx = adjacency_matrix(self.l_o_f, 6)
        return self.l_o_f

    def new_length(self):
        edge_4_dell = list(self.old_edge)
        self.l_mtx[self.a[0], self.b[0]] = self.l_mtx[self.b[0], self.a[0]]

        c_length = self.l_mtx[self.a[0], edge_4_dell[0]] # длина ребра C, которое соединяте ребро для удаления и вершину вырожденной грани
        b_length = self.l_mtx[self.a[0], edge_4_dell[1]] # длина ребра B, которое соединяет ребро для удаления и вершину вырожденной грани
        a_length = self.l_mtx[edge_4_dell[0], edge_4_dell[1]] # длина ребра A равна длине ребра, которое необходимо удалить
        c_shtrih = self.l_mtx[self.b[0], edge_4_dell[0]] # А штрих
        b_shtrih = self.l_mtx[self.b[0], edge_4_dell[1]] # B штрих
        # delta = (b_length + c_length - a_length)/(c_length + b_length)

        try:
            cosine_alpha = ((a_length) ** 2 + c_shtrih ** 2 - b_shtrih ** 2) / (2. * (c_length + b_length) * c_shtrih)
            lenth_of_new_edge = np.sqrt(c_length**2 + c_shtrih**2 - 2.*c_length*c_shtrih * cosine_alpha)
        except ArithmeticError:
            print('Delenie na nol')
        print('lenth_of_new_edge:', lenth_of_new_edge)
        self.adj_matx = adjacency_matrix(self.l_o_f, len(list(self.set_of_vertex)))
        print(len(self.adj_matx.nonzero()), 'количество ненулевых элементов в новой матрице')
        for i in range(0, len(list(self.set_of_vertex))):
            for j in range(i, len(list(self.set_of_vertex))):
                if self.adj_matx[i, j] != 0:
                    self.adj_matx[i, j] = self.l_mtx[i, j]
                    self.adj_matx[j, i] = self.l_mtx[i, j]
        print('номера вершин, которые необходимо соединить:', self.a[0], self.b[0])
        self.adj_matx[self.a[0], self.b[0]] = self.adj_matx[self.b[0], self.a[0]] = lenth_of_new_edge
        # self.l_mtx[edge_4_dell[0], edge_4_dell[1]] = self.l_mtx[edge_4_dell[1], edge_4_dell[0]] = 0
        # print(self.set_of_vrtx)
        #
        # self.l_mtx[self.a[0], self.b[0]] = self.l_mtx[self.b[0], self.a[0]] = lenth_of_new_edge
        for i in range(0, len(list(self.set_of_vertex))):
            for j in range(0, len(list(self.set_of_vertex))):
                print(float("{0:.1f}".format(self.adj_matx[i, j])), end='\t')
            print('\n')
        return self.adj_matx


