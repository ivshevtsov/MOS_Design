import skrf as rf
import matplotlib.pyplot as plt
from Functions import PLOT_s_db_Dir
from Functions import PLOT_s_db_Netw
from Functions import read_file
from skrf import Network
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Formula on plot
#https://latex.codecogs.com/eqneditor/editor.php

#First Directory
File_1 = 'Files/EV_BOARD/RF_IN_0R5MM_18MM.s2p'
File_1_label = '1.8 мм'

#Second Directory
File_2 = 'Files/EV_BOARD/RF_IN_0R5MM_15MM.s2p'
File_2_label = '1.5 мм'

File_3 = 'Files/EV_BOARD/RF_IN_Thru.s2p'
File_3_label = 'Thru'

list = ['0R2', '0R5', '1R0']
list_names = ['0.2мм', '0.5мм', '1.0мм']


epsilon = 4.7
c = 3e8
Freq = np.linspace(start=1e9, stop=5e9, num=100)
lamb= c/(Freq*np.sqrt(epsilon))
lamb_4 = lamb/4

plt.plot(Freq, lamb_4*1000, linewidth='3')
plt.ylabel(r'$\frac{\lambda }{4}$, мм,')
plt.xlabel('F, Гц')
plt.grid()



'''
for i in range(len(list)):
    NET = rf.Network(f'Files/EV_BOARD/RF_IN_{list[i]}MM_15MM.s2p')
    PLOT_s_db_Netw(NET, label=list_names[i], N_fig=1, sp=11)
    plt.grid()
    PLOT_s_db_Netw(NET, label=list_names[i], N_fig=2, sp=21)
    plt.grid()
    plt.figure(3)
    NET.plot_s_smith(1 - 1, 1 - 1, label=list_names[i], linewidth='3')
    plt.ylabel('S11')
plt.grid()
plt.show()


Data_1 = rf.Network(File_1)
Data_2 = rf.Network(File_2)
Data_3 = rf.Network(File_3)

PLOT_s_db_Netw(Data_1, label=File_1_label, N_fig=4, sp=11)
PLOT_s_db_Netw(Data_2, label=File_2_label, N_fig=4, sp=11)
plt.grid()
PLOT_s_db_Netw(Data_1, label=File_1_label, N_fig=5, sp=21)
PLOT_s_db_Netw(Data_2, label=File_2_label, N_fig=5, sp=21)
plt.grid()

plt.figure()
Data_1.plot_s_smith(1-1, 1-1, label=File_1_label, linewidth='3')
Data_2.plot_s_smith(1-1, 1-1, label=File_2_label, linewidth='3')
plt.ylabel('S11')



PLOT_s_db_Netw(Data_3, label=File_3_label, N_fig=7, sp=11)
plt.grid()
PLOT_s_db_Netw(Data_3, label=File_3_label, N_fig=8, sp=21)
plt.grid()
plt.figure()
Data_3.plot_s_smith(1-1, 1-1, label=File_3_label, linewidth='3')
plt.ylabel('S11')
'''
plt.show()
