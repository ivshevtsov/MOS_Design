import control
import numpy as np
from Functions import pole_zero_plot
from Functions import read_pole_zeros_cadence
import matplotlib.pyplot as plt
from Functions import read_file
from Functions import pole_plot
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3
#plt.rcParams["figure.figsize"]=[4,4]




omega = np.linspace(-10, 10, 100)
w = 1
w_P =4
s= control.tf('s')
T_LPF = (w) / (1+s/w)
T_PPF = (w) / (1+(s-1j*w_P)/w)
#parameters
mag_LPF, _, w_LPF = control.bode(T_LPF, plot=False, color='Tab:red', omega = omega)
mag_PPF, _, w_PPF = control.bode(T_PPF, plot=False, color='Tab:red', omega = omega)
#Plot T(f)
plt.figure()
plt.plot(w_PPF, 20*np.log10(mag_PPF), color='Tab:red')
#plt.xscale("log")
plt.grid(which='both', axis='both')

#Initial conditions
x_lim = [-3e6, 1e6]

#read files
Home = 'Files/Filters/Second_order_ppf(a)'

Directory_1 = f'{Home}/Second_order_ideal_pole_Gain_100.csv'
Directory_2 = f'{Home}/Second_order_ideal_pole_Gain_50.csv'
Directory_3 = f'{Home}/Second_order_ideal_pole_Gain_30.csv'
Directory_4 = f'{Home}/Second_order_ideal_pole_Gain_20.csv'
Directory_5 = f'{Home}/Second_order_active_H_Gain.csv'


label_1 = '100 дБ'
label_2 = '50 дБ'
label_3 = '30 дБ'
label_4 = '20 дБ'

poles_1 = read_pole_zeros_cadence(Directory_1)
poles_2 = read_pole_zeros_cadence(Directory_2)
poles_3 = read_pole_zeros_cadence(Directory_3)
poles_4 = read_pole_zeros_cadence(Directory_4)
HF = read_file(Directory_5)


#Plot conditionals
color_0='Tab:pink'
color_1='Tab:orange'
color_2='Tab:blue'
color_3='Tab:green'
color_4='Tab:red'

#Plot Pole/Zero
plt.figure()

pole_plot(poles_1, legend_p=label_1, color_p=color_1)
pole_plot(poles_2, legend_p=label_2, color_p=color_2)
pole_plot(poles_3, legend_p=label_3, color_p=color_3)
pole_plot(poles_4, legend_p=label_4, color_p=color_4)
plt.legend()
plt.xlim(*x_lim)
plt.grid()
plt.xlabel('Real')
plt.ylabel('Imag')


plt.title(f'Second order')

#H(f) plot
plt.figure()
plt.title(f'Second order')
plt.plot(HF[:, 0], HF[:, 1], linewidth=3, color=color_1, label=label_1)
plt.plot(HF[:, 0], HF[:, 2], linewidth=3, color=color_2, label=label_2)
plt.plot(HF[:, 0], HF[:, 3], linewidth=3, color=color_3, label=label_3)
plt.plot(HF[:, 0], HF[:, 4], linewidth=3, color=color_4, label=label_4)
plt.xlabel('F, Гц')
plt.ylabel('T(f), дБ')
plt.legend()
plt.grid(which='both', axis='both')







plt.show()