import numpy as np
from rebuilding import Rebuilding
class Calculate():
    def __init__(self, gauss_curve, list_faces, conformal_weights, time_step ):
        # self.lenght_of_edges = length_of_octahedron
        self.curv_gauss_vrtx = gauss_curve
        self.l_o_f = list_faces
        self.conf_weght = conformal_weights
        self.vertex = len(self.conf_weght)
        self.step_time = time_step
        # print(self.vertex, "тестируем класс калькулейт")
        # print("длина массива конформал вейт:", len(self.conf_weght))

    def weight_calculate(self):
        new_weight = []
        for j in range(0, self.vertex):
            k0 = - (self.curv_gauss_vrtx[j] - 4. * np.pi / self.vertex) * self.conf_weght[j]
            k1 = - (self.curv_gauss_vrtx[j] - 4. * np.pi / self.vertex) * (self.conf_weght[j] + self.step_time * k0 / 2.)
            k2 = - (self.curv_gauss_vrtx[j] - 4. * np.pi / self.vertex) * (self.conf_weght[j] + self.step_time * k1 / 2.)
            k3 = - (self.curv_gauss_vrtx[j] - 4. * np.pi / self.vertex) * (self.conf_weght[j] + self.step_time * k2)
            new_weight.append(self.conf_weght[j] + (self.step_time/6.) * (k0 + k1*2. + k3*2. + k3))
        return new_weight
