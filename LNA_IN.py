import numpy as np
import skrf as rf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"



#Directory
Power = [0, 10, 20, 40]
Experiment='1'
Home=f'Files/KapDwa/LNA_IN_PCB/'

#S11
plt.figure()
plt.title(f'Experiment {Experiment}')
P=0
for i in Power:
    if i>0:
        P=-i
    # Directory
    File_VNA = f'{Home}/{Experiment}/m{i}dBm.s1p'
    LNA_IN_VNA = rf.Network(File_VNA)
    LNA_IN_VNA.plot_s_db(m=1-1, n=1-1, label=f'{P} дБм', linewidth='3')
plt.ylabel(f'S{11}, дБ')
plt.xlabel('F, Гц')
plt.grid()


#S11 smith
plt.figure()
plt.title(f'Experiment {Experiment}')
P=0
for i in Power:
    if i>0:
        P=-i
    # Directory
    File_VNA = f'{Home}/{Experiment}/m{i}dBm.s1p'
    LNA_IN_VNA = rf.Network(File_VNA)
    LNA_IN_VNA.plot_s_smith(m=1-1, n=1-1, label=f'{P} дБм', linewidth='3')
plt.ylabel(f'S{11}, дБ')
plt.xlabel('F, Гц')
plt.grid()


#Compare
Power = 40
Experiment_1_F=f'Files/KapDwa/LNA_IN_PCB/1/m{Power}dBm.s1p'
Experiment_2_F=f'Files/KapDwa/LNA_IN_PCB/2/m{Power}dBm.s1p'
Experiment_1 = rf.Network(Experiment_1_F)
Experiment_2 = rf.Network(Experiment_2_F)

plt.figure()
Experiment_1.plot_s_db(m=1-1, n=1-1, label=f'EX1.-{Power} дБм', linewidth='3')
Experiment_2.plot_s_db(m=1-1, n=1-1, label=f'EX2.-{Power} дБм', linewidth='3')
plt.ylabel(f'S{11}, дБ')
plt.xlabel('F, Гц')
plt.grid()

plt.figure()
Experiment_1.plot_s_smith(m=1-1, n=1-1, label=f'EX1.-{Power} дБм', linewidth='3')
Experiment_2.plot_s_smith(m=1-1, n=1-1, label=f'EX2.-{Power} дБм', linewidth='3')
plt.ylabel(f'S{11}, дБ')
plt.xlabel('F, Гц')
plt.grid()

plt.show()

















plt.show()