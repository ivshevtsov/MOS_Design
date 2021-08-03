import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#---Read_File---
File = "Files/Filters/Integrator_error/Integrator_Error_Gain.csv"
Sim_Error_F=read_file(File, dot = ',', Text = '')
#---------------


#input parameters
INT_UNITY=1


#calculate
Gain = np.linspace(10, 1e3, 1000)
epsilon = 1/(1+(1/Gain)+(1/(Gain*complex(0, 1))))
epsilon = np.abs(epsilon)

epsilon_db = 20*np.log10(epsilon)
Error_f = ((INT_UNITY-INT_UNITY*epsilon)/INT_UNITY)*100

#error Freq
plt.figure()
plt.plot(20*np.log10(Gain), Error_f, linewidth=3, label='Calculated')
plt.plot(20*np.log10(Sim_Error_F[:, 0]), Sim_Error_F[:, 1], linewidth=3, label='Measured')
plt.xscale('log')
plt.xlabel('Gain, дБ')
plt.ylabel('Error F, %')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)
plt.legend()

#error gain
plt.figure()
plt.plot(20*np.log10(Gain), epsilon_db, linewidth=3, label='Calculated')
#plt.xscale('log')
plt.xlabel('Gain, дБ')
plt.ylabel('Error дБ')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)
plt.legend()


plt.show()