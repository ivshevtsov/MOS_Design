import numpy as np
import matplotlib.pyplot as plt
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

LOW_SIDEBAND_File = "Files/MIX/LNA_MIX_PEX.csv"
Title = 'MIX'
LOW_SIDEBAND=read_file(LOW_SIDEBAND_File, dot = ',', Text = '')



plt.figure()
plt.title('Conversion Gain')
plt.plot(LOW_SIDEBAND[:, 0], LOW_SIDEBAND[:, 1], label='I', linewidth ='3')
plt.plot(LOW_SIDEBAND[:, 0], LOW_SIDEBAND[:, 2], label='Q', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title('Conversion Gain Error')
plt.plot(LOW_SIDEBAND[:, 0], abs(LOW_SIDEBAND[:, 1]-LOW_SIDEBAND[:, 2]), linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Error, дБ')
plt.grid()

plt.figure()
plt.title('Noise')
plt.plot(LOW_SIDEBAND[:, 3], LOW_SIDEBAND[:, 4], label='DSB', linewidth ='3')
plt.plot(LOW_SIDEBAND[:, 3], LOW_SIDEBAND[:, 5], label='SSB', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()


plt.figure()
plt.title('LNA(OUT)')
plt.plot(LOW_SIDEBAND[:, 6], LOW_SIDEBAND[:, 7], label='LNA(OUT)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()


plt.show()