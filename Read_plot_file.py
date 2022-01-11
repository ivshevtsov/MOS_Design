import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


File = "Files/PPF/filters_tt/GPS.csv"
Title = 'GPS'
Value_1=read_file(File, dot = ',', Text = '')
#Resistors = ['1 кОм', '3 кОм', '30 кОм', '300 кОм', '3 МОм', '10 МОм']
#Gains = ['-9', '-7', '-5', '-3', '-1']



'''
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

plt.figure()
plt.title(Title)
plt.plot(Value_1[:, 0], Value_1[:, 1], label='Without DCOC', linewidth ='3')
#plt.plot(Value_1[:, 0], Value_1[:, 3], label='With DCOC', linewidth ='3')

plt.xlabel('f, Гц')
plt.ylabel('H(f), дБ')
#plt.xscale('log')
plt.grid()
#plt.legend()

plt.figure()
plt.title(Title)
plt.plot(Value_1[:, 2], Value_1[:, 3]*1e9, label='Without DCOC', linewidth ='3')
#plt.plot(Value_1[:, 0], Value_1[:, 4]+180*2, label='With DCOC', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('GD, нc')
#plt.xscale('log')
plt.grid()
#plt.legend()



'''
plt.figure()
plt.plot(Value_1[:, 0], Value_1[:, 2], label='Ideal', linewidth ='3')
#plt.plot(Value_1[:, 0], Value_1[:, 4], label='Uncompensated', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 4], linestyle='dashed', label='Compensated', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('phase(F), град.')
plt.xscale('log')
plt.grid()
plt.legend()
'''




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


