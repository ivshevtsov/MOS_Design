import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


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

plt.show()