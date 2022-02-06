import control
import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3


File = f"Files/PPF_VGA/VGA_GLO_GAIN_K1.csv"
Value_1=read_file(File, dot = ',', Text = '')
Gains = [5, 15, 25, 35]


#Plot H(f)
plt.figure()
plt.title('GLO')
for i in range(len(Gains)):
    plt.plot(Value_1[:, 0], Value_1[:, i+1], label=f'GAIN_GPS={Gains[i]}', linewidth ='3')

plt.xlabel('F, Гц')
plt.ylabel('H(F), дБ')
plt.legend()
plt.grid(which='both', axis='both')

File_1 = f"Files/PPF_VGA/IF_GPS_GAIN_60_K1.csv"
Value_1=read_file(File_1, dot = ',', Text = '')
plt.figure()
plt.title('GPS')
plt.plot(Value_1[:, 0], Value_1[:, 1], label=f'IF', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 2], label=f'PPF', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('H(F), дБ')
plt.legend()
plt.grid(which='both', axis='both')


plt.show()