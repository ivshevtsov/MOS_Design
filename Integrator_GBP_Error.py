import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#---Read_File---

File = "Files/Filters/Integrator_error/Integrator_Error_F.csv"
Sim_Error_F=read_file(File, dot = ',', Text = '')

#---------------




#input parameters

INT_UNITY=1


#calculate
GBP = np.linspace(INT_UNITY*10, 1e3, 1000)
epsilon = 1/(1+(INT_UNITY/GBP)+complex(0, 1)*(INT_UNITY/GBP))
epsilon = np.abs(epsilon)

epsilon_db = 20*np.log10(epsilon)
Error_f = (1-epsilon)*100

#error Freq
plt.figure()
plt.plot(GBP/INT_UNITY, Error_f, linewidth=3, label='Calculated')
plt.plot(Sim_Error_F[:, 0], Sim_Error_F[:, 1], linewidth=3, label='Measured')
plt.xscale('log')
plt.xlabel(r'$\frac{GBP}{fo}$')
plt.ylabel('Error F, %')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)
plt.legend()

#error gain
plt.figure()
plt.plot(GBP/INT_UNITY, epsilon_db, linewidth=3, label='Calculated')
plt.xscale('log')
plt.xlabel(r'$\frac{GBP}{fo}$')
plt.ylabel('Error дБ')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)


plt.show()
