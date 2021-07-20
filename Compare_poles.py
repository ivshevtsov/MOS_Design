from Functions import pole_zero_plot
from Functions import read_pole_zeros_cadence
import matplotlib.pyplot as plt
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Initial conditions
x_lim = [-2e6, 0]

#read files
Directory_1 = 'Files/Filters/PZ_PPF_18M_IDEAL.csv'
Directory_2 = 'Files/Filters/PZ_PPF_18M_REAL.csv'
Directory_3 = 'Files/Filters/HF_First_PPF.csv'
label_1 = 'GBP 1T'
label_2 = 'GBP 200M'
poles_1 = read_pole_zeros_cadence(Directory_1)
poles_2 = read_pole_zeros_cadence(Directory_2)
HF = read_file(Directory_3)


#Plot conditionals
color_1='Tab:orange'
color_2='Tab:blue'

#Plot Pole/Zero
pole_zero_plot(poles_1, poles_2, legend_p=label_1, legend_z=label_2, color_p=color_1, color_z=color_2)
plt.legend()
plt.xlim(*x_lim)
plt.title(f'Butterworth. N=1')

#H(f) plot
plt.figure()
plt.plot(HF[:, 0], HF[:, 1], linewidth=3, color=color_1, label='LPF')
plt.plot(HF[:, 0], HF[:, 2], linewidth=3, color=color_2, label='PPF')
plt.xlabel('F, Гц')
plt.ylabel('H(f), дБ')
plt.legend()
plt.grid(which='both', axis='both')



plt.show()

