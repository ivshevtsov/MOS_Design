import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#---Read_File---
File = "Files/Filters/Integrator_error/Integrator_Error_Rout.csv"
Sim_Error_R=read_file(File, dot = ',', Text = '')
#---------------

#input parameters
R=20e3


#calculate
R_out = np.linspace(10, 1e3, 1000)
Gain = R_out/(R+R_out)

#Plot Gain
plt.figure()
plt.plot(R_out, 20*np.log10(Gain), linewidth=3, label='Calculated')
plt.xscale('log')
plt.xlabel('Rout')
plt.ylabel('Gain, дБ')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)

#Plot simulated values

#error Freq
plt.figure()
plt.plot(Sim_Error_R[:, 0], Sim_Error_R[:, 1], linewidth=3, label='R=0 Ом')
plt.plot(Sim_Error_R[:, 0], Sim_Error_R[:, 2], linewidth=3, label='R=500 Ом')
plt.xscale('log')
plt.xlabel('f, Гц')
plt.ylabel('H(f), дБ')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.13)
plt.subplots_adjust(left=0.14)
plt.legend()




plt.show()