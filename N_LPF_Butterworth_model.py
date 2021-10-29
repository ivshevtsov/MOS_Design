from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Functions import pole_zero_plot
from Functions import read_file
from Functions import read_pole_zeros_cadence

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


#parameters of filter
Order = 3
Freq = 5e6
start_f = 1e3
stop_f =  1e8
N_points = 100

#read file
Directory_1 = 'Files/Filters/Poles_zeros_real.csv'
Directory_2 = 'Files/Filters/HF_LPF_3_real.csv'
poles = read_pole_zeros_cadence(Directory_1)
HF = read_file(Directory_2)

#calculate numerator(b) and denumerator(a)
b, a = signal.butter(Order, Freq, btype='lowpass', analog=True, output='ba')

#create H(f) function
f, h = signal.freqs(b, a, worN=np.logspace(np.log10(start_f), np.log10(stop_f), N_points))

#calculate poles/zeros
z, p , k = signal.butter(Order, Freq, btype='lowpass', analog=True, output='zpk')

print('*---Poles---*')
for i in range(len(p)):
    print(np.round(p[i], 3))
print('*-----------*')

#Plot conditionals
color_1='Tab:orange'
color_2='Tab:blue'

#Plot Pole/Zero
pole_zero_plot(p, poles, legend_p='Ideal', legend_z='Model', color_p=color_1, color_z=color_2)
plt.legend()
plt.title(f'Butterworth. N={Order}')

#Plot H(f)
plt.figure()
plt.title(f'Butterworth. N={Order}')
plt.semilogx(f, 20*np.log10(abs(h)), linewidth=3, color=color_1, label='Ideal')
plt.semilogx(HF[:, 0], HF[:, 1], '--', linewidth=3, color=color_2, label='Model')
plt.xlabel('F, Гц')
plt.ylabel('H(f), дБ')
plt.legend()
plt.grid(which='both', axis='both')
plt.show()