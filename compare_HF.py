from Functions import pole_zero_plot
from Functions import read_pole_zeros_cadence
import matplotlib.pyplot as plt
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#Initial conditions
x_lim = [-2e6, 0]

#read files
Home ='Files/Filters/Tow_thomas_compensation'
Directory_1 = f'{Home}/HF_Tow_Thomas_Ideal.csv'
Directory_2 = f'{Home}/HF_Tow_Thomas_Uncompensated.csv'
Directory_3 = f'{Home}/HF_Tow_Thomas_pass_compensated.csv'
Directory_4 = f'{Home}/HF_Tow_Thomas_activ_compensated.csv'
label_1 = 'Ideal'
label_2 = 'Uncompensated'
label_3 = 'Passive Comp.'
label_4 = 'Active Comp.'

HF_1 = read_file(Directory_1)
HF_2 = read_file(Directory_2)
HF_3 = read_file(Directory_3)
HF_4 = read_file(Directory_4)
#Plot conditionals
color_1='Tab:orange'
color_2='Tab:blue'

plt.figure()
plt.plot(HF_1[:, 0], HF_1[:, 1], linewidth=3, color=color_1, label='Ideal')
plt.plot(HF_2[:, 0], HF_2[:, 1], linewidth=3, color=color_2, label='Uncompensated')
plt.xlabel('F, Гц')
plt.ylabel('T(F), дБ')
plt.xscale('log')
plt.legend()
plt.grid(which='both', axis='both')

plt.figure()
plt.plot(HF_1[:, 0], HF_1[:, 1], linewidth=3, color=color_1, label='Ideal')
plt.plot(HF_3[:, 0], HF_3[:, 1], linewidth=3, color=color_2, label='Passive Comp.')
plt.xlabel('F, Гц')
plt.ylabel('T(F), дБ')
plt.xscale('log')
plt.legend()
plt.grid(which='both', axis='both')

plt.figure()
plt.plot(HF_1[:, 0], HF_1[:, 1], linewidth=3, color=color_1, label='Ideal')
plt.plot(HF_4[:, 0], HF_4[:, 1], linewidth=3, color=color_2, label='Active Comp.')
plt.xlabel('F, Гц')
plt.ylabel('T(F), дБ')
plt.xscale('log')
plt.legend()
plt.grid(which='both', axis='both')


plt.show()