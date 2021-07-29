import matplotlib.pyplot as plt
from Functions import plot_two_y
from Functions import pole_zero_plot
from Functions import read_file
from Functions import read_pole_zeros_cadence

import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
Home='Files/Filters/First_order_example'

File_HF = f"{Home}/First_order_example.csv"
File_pole = f'{Home}/First_order_pole.csv'
File_zero = f'{Home}/First_order_zero.csv'


Title = 'Closed loop gain (R1=1 кОм)'
Value_1=read_file(File_HF, dot = ',', Text = '')

plot_two_y(Value_1[:, 0], First=Value_1[:,1], Second=Value_1[:, 2],
           label_first='H(f), дБ', label_second='Фаза, град.', xlabel='F, Гц')
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.15)
plt.subplots_adjust(right=0.88)


#Plot conditionals
color_1='Tab:orange'
color_2='Tab:blue'

#Directories
poles = read_pole_zeros_cadence(File_pole)
zeros = read_pole_zeros_cadence(File_zero)

#Plot Pole/Zero
pole_zero_plot(poles, zeros, legend_p='Poles', legend_z='Zeros', color_p=color_1, color_z=color_2)
plt.legend()
plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(left=0.22)

plt.show()
