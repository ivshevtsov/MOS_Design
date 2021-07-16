from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#input parameters

INT_UNITY=1


#calculate
GBP = np.linspace(INT_UNITY*10, 1e3, 1000)
epsilon = 1/(1+(INT_UNITY/GBP)+complex(0, 1)*(INT_UNITY/GBP))
epsilon = np.abs(epsilon)

epsilon_db = 20*np.log10(epsilon)
Error_f = ((INT_UNITY/epsilon-INT_UNITY)/INT_UNITY)*100

#error Freq
plt.figure()
plt.plot(GBP/INT_UNITY, Error_f, linewidth=3)
plt.xscale('log')
plt.xlabel(r'$\frac{GBP}{fo}$')
plt.ylabel('Error F, %')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)

#error gain
plt.figure()
plt.plot(GBP/INT_UNITY, epsilon_db, linewidth=3)
plt.xscale('log')
plt.xlabel(r'$\frac{GBP}{fo}$')
plt.ylabel('Error дБ')
plt.grid(which='both', axis='both')
plt.subplots_adjust(bottom=0.16)


plt.show()
