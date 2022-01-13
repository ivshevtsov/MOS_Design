import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
import skrf as rf
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


def Fitting_error(File_Model, File_EM_sim):
    S_Model = rf.Network(File_Model)
    S_EM_sim = rf.Network(File_EM_sim)
    n = len(S_Model.f)

    for j in range(2):
        for k in range(2):
            #Calculation denominator(local sum)
            sum_local_im = 0
            sum_local_re = 0
            for i in range(n):
                sum_local_im = sum_local_im + S_EM_sim.y_im[i, j, k] ** 2
                sum_local_re = sum_local_re + S_EM_sim.y_re[i, j, k] ** 2
            sum_local_im = sum_local_im / n
            sum_local_re = sum_local_re / n
            # Calculation numerator(global sum)
            sum_global_im = 0
            sum_global_re = 0
            for i in range(n):
                numerator_im = ((S_EM_sim.y_im[i, j, k] - S_Model.y_im[i, j, k]) ** 2) / sum_local_im
                numerator_re = ((S_EM_sim.y_re[i, j, k] - S_Model.y_re[i, j, k]) ** 2) / sum_local_re
                sum_global_im = sum_global_im + numerator_im
                sum_global_re = sum_global_re + numerator_re
            Error_im = ((sum_global_im / n) ** (1 / 2)) * 100
            Error_re = ((sum_global_re / n) ** (1 / 2)) * 100
            print(f'Error Real(Y{j + 1}{k + 1})(%) = {Error_re}')
            print(f'Error Imag(Y{j + 1}{k + 1})(%) = {Error_im}')


File_Model = f'Files/Y_Spiral/IND_TSMC.s2p'
File_EM_sim =   f'Files/Y_Spiral/IND_EM_1.s2p'

Fitting_error(File_Model = File_Model, File_EM_sim = File_EM_sim)

Model = rf.Network(File_Model)
EM_sim =rf.Network(File_EM_sim)

plt.figure()
Model.plot_s_db(m=2-1, n=1-1, label=f'TSMC Model', linewidth='3')
EM_sim.plot_s_db(m=2-1, n=1-1, label=f'Simulation', linewidth='3')
plt.grid()
plt.show()



