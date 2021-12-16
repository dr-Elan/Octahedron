class Rebuilding():
    """ Здесь будет проходить перестройка триангуляции """
    def __init__(self, list_of_faces, deg_face, lenth_mtx):
        self.l_o_f = list_of_faces
        self.dg_fc = deg_face
        self.l_mtx = lenth_mtx

    def find_faces(self):
        self.a = self.l_mtx[self.dg_fc[0], self.dg_fc[1]]
        self.b = self.l_mtx[self.dg_fc[1], self.dg_fc[2]]
        self.c = self.l_mtx[self.dg_fc[0], self.dg_fc[2]]
        if self.a == max(self.a, self.b, self.c):
            self.old_edge = {self.dg_fc[0], self.dg_fc[1]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[2]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера
        elif self.b == max(self.a, self.b, self.c):
            self.old_edge = {self.dg_fc[0], self.dg_fc[2]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[1]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера
        elif self.c == max(self.a, self.b, self.c):
            self.old_edge = {self.dg_fc[1], self.dg_fc[2]} # вершины, которые лежат на ребре, которое надо удалит
            self.vrtx = {self.dg_fc[0]} # вершина вырожденной грани, которая лежит напротив наибольшего ребера

        for i in range(0, len(self.l_o_f)):
            set_of_vrtx = {self.l_o_f[i][0], self.l_o_f[i][1], self.l_o_f[i][2]}
            if self.old_edge.issubset(set_of_vrtx) and self.vrtx.difference(set_of_vrtx) != self.vrtx:
                self.smeg_face = self.l_o_f[i]
            if self.old_edge.issubset(set_of_vrtx) and self.vrtx.difference(set_of_vrtx) == self.vrtx:
                self.degenerat_face = self.l_o_f[i]
        return print(self.smeg_face[0], self.smeg_face[1], self.smeg_face[2], "сlass Rebuild , find smeg faces", '\n',
                     self.dg_fc[0], self.degenerat_face[1], self.degenerat_face[2], "сlass Rebuild , find  degenerate function")

    def dell_faces(self):
        "создаем множество из вершин грани, если оно содержится в множестве вершин вырожденной грани, то удаляем грань"
        for i in range(0, len(self.l_o_f)):
            if self.old_edge.issubset({self.l_o_f[0], self.l_o_f[1], self.l_o_f[2]}):
                self.l_o_f.pop(i)
            break
        "создаем множество из вершин грани, если оно содержится в множестве вершин вырожденной грани, то удаляем грань"
        for i in range(0, len(self.l_o_f)):
            if self.old_edge.issubset({self.l_o_f[0], self.l_o_f[1], self.l_o_f[2]}):
                self.l_o_f.pop(i)
            break
        return self.l_o_f

