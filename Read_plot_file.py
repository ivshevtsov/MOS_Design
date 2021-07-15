import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


File = "Files/FD_OPA_PZ/FD_Closed_loop.csv"
Title = 'Closed loop gain (R1=1 кОм)'
Value_1=read_file(File, dot = ',', Text = '')
Resistors = ['1 кОм', '3 кОм', '30 кОм', '300 кОм', '3 МОм', '10 МОм']
#Gains = ['-9', '-7', '-5', '-3', '-1']

plt.title(Title)
for i in range(len(Value_1[0])-1):
    plt.plot(Value_1[:, 0], Value_1[:, i+1], label=f'R2={Resistors[i]}', linewidth='3')
plt.xlabel('F, Гц')
plt.xscale('log')
plt.ylabel('A, дБ')
plt.grid()
plt.legend()
plt.show()


'''
plt.plot(Value_1[:, 0], Value_1[:, 1], label='FF', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 3], label='SS', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 5], label='TT', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, dB')
plt.grid()
plt.legend()
plt.show()
'''


