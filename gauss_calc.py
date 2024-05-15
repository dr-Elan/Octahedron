# from matplotlib.pyplot import cla
import math

import numpy as np
from scipy import sparse
# from sklearn import exceptions
from faces import Faces

class Gauss():
    def __init__(self, matrix_lenght, lst_fasec):
        
        self.lst_fs = lst_fasec
        # print('создаём класс Gauss', 13)
        self.mtx_lght = matrix_lenght
        # print('создаём класс Gauss', 15)
        self.row, self.col = self.mtx_lght.nonzero()
        # print('создаём класс Gauss', 17)
        self.dictinary_vertex = {}
        # print('создаём класс Gauss', 19)
        self.dictinary_gauss = {}
        # print('создаём класс Gauss', 20)
        self.existence = 0
        # print('создаём класс Gauss', 23)
        self.gauss_curve = np.full(len(self.dictinary_gauss), 2.*np.pi)
        # print('создаём класс Gauss', 25)
        self.massiv_fasece = []
        # print('создаём класс Gauss', 27)
        for lfs in self.lst_fs:
            self.massiv_fasece.append(sorted([lfs[0], lfs[1], lfs[2]]))
        # print('создаём класс Gauss', 30)

    def date_prepare(self):
        for j in range(0, self.mtx_lght.count_nonzero()):
            if self.row[j] not in self.dictinary_vertex.keys():
                self.dictinary_vertex[self.row[j]] = [self.col[j]]
            else:
                self.dictinary_vertex[self.row[j]].append(self.col[j])
        for key, val in self.dictinary_vertex.items():
            list_of_adjency_vertex = []
            for i in val:
                for j in val:
                    if self.mtx_lght[i, j] != 0 and self.mtx_lght[j, i] != 0 and (sorted([key, i, j]) in  self.lst_fs):
                        list_of_adjency_vertex.append(sorted([i,j]))
            self.dictinary_gauss[key] = list(map(list, {tuple(x) for x in list_of_adjency_vertex}))
        for key, arr in self.dictinary_vertex.items():
            print(key, '\t', len(arr))
        return None
            
    def gauss_calculate(self):
        self.gauss_curve = np.full(len(self.dictinary_gauss), 2.*np.pi)
        # exceptions = 0
        klmgn = set()
        for key, val in self.dictinary_gauss.items():
            for v in val:
                a =  self.mtx_lght[v[0], v[1]]
                b =  self.mtx_lght[v[1], key]
                c =  self.mtx_lght[v[0], key]

                c_cos = (b**2 + c**2 - a**2)/(2.*c*b)

                half_perim = (a + b + c )/2.

                kl_mng = float("{0:.1f}".format(half_perim*(half_perim - a)*(half_perim - b) * (half_perim - c)))
                klmgn.add(kl_mng)

                if kl_mng >= 0:
                    self.gauss_curve[key] -= np.arccos(c_cos)
                else:
                    # print("gauss_curve РАВНО НУЛЮ")
                    self.gauss_curve[key] = 0
                    self.existence = 1

        
        
        






