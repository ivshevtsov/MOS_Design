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
Directory_1 = f'{Home}/pz_Tow_Thomas_Ideal.csv'
Directory_2 = f'{Home}/pz_Tow_Thomas_Uncompensated.csv'
Directory_3 = f'{Home}/pz_Tow_Thomas_passive_compensated.csv'
Directory_4 = f'{Home}/pz_Tow_Thomas_active_compensated.csv'
#Directory_3 = 'Files/Filters/HF_First_PPF.csv'
label_1 = 'Ideal'
label_2 = 'Uncompensated'
label_3 = 'Passive Comp.'
label_4 = 'Active Comp.'
poles_1 = read_pole_zeros_cadence(Directory_1)
poles_2 = read_pole_zeros_cadence(Directory_2)
poles_3 = read_pole_zeros_cadence(Directory_3)
poles_4 = read_pole_zeros_cadence(Directory_4)
#HF = read_file(Directory_3)

#Plot conditionals
color_1='Tab:orange'
color_2='Tab:blue'

#Plot Pole/Zero
pole_zero_plot(poles_1, poles_2, legend_p=label_1, legend_z=label_2, color_p=color_1, color_z=color_2)
plt.legend()
pole_zero_plot(poles_1, poles_3, legend_p=label_1, legend_z=label_3, color_p=color_1, color_z=color_2)
plt.legend()
pole_zero_plot(poles_1, poles_4, legend_p=label_1, legend_z=label_4, color_p=color_1, color_z=color_2)
plt.legend()


plt.show()

