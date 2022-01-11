import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
import skrf as rf
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#S-parameters
File_1 = f'Files/QVCO_IND/QVCO_Bank_1.s4p'
File_2 = f'Files/QVCO_IND/QVCO_Bank_2.s4p'
File_3 = f'Files/QVCO_IND/QVCO_Bank_3.s4p'
File_4 = f'Files/QVCO_IND/QVCO_Bank_4.s4p'
Bank_1 = rf.Network(File_1)
Bank_2 = rf.Network(File_2)
Bank_3 = rf.Network(File_3)
Bank_4 = rf.Network(File_4)


plt.figure()
Bank_1.plot_s_db(m=2-1, n=1-1, label=f'TSMC', linewidth='3')
Bank_1.plot_s_db(m=4-1, n=3-1, label=f'FEM(Ground_1)', linewidth='3')
Bank_3.plot_s_db(m=4-1, n=3-1, label=f'FEM(Ground_2)', linewidth='3')
Bank_4.plot_s_db(m=4-1, n=3-1, label=f'MoM(Ground_2)', linewidth='3')
plt.ylabel(f'S{21}, дБ')
plt.xlabel('f, Гц')
plt.legend()
plt.grid()






plt.show()