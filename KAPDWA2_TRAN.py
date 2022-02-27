import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import windows

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


N_Sinals = {'RF_Port': 1, 'RF_IN': 2, 'MIX_OUT': 3,
            'PPF(GPS)': 4, 'PPF(GLO)': 5,'GPS_A': 6,
            'GLO_A': 7, 'VCAP': 8, 'QVCO(SINE)': 9}

Plot_Signal_1 = 'RF_IN'

Home = 'C:/Users\ELECTRONIC\Desktop'
File = 'KAPDWA_1.6G_5_9u_interpolate_50p.csv'

X = np.genfromtxt(f'{Home}/{File}', delimiter=',', skip_header=1)

Column = N_Sinals[Plot_Signal_1]*2-1
Data = X[:, Column]

#initial data
dT = 50e-12
SAMPLE_RATE = 1/dT
N = len(Data)
##------------------
##Calculate spectrum
yf = fft(Data)
xf = fftfreq(N, 1/SAMPLE_RATE)

w = windows.blackman(N)
ywf = fft(Data*w)
##------------------

freq = 2e9
divide = int(max(xf[0:N//2])/freq)
print(max(xf[0:N//2]))

plt.figure()
plt.title(Plot_Signal_1)
plt.plot(xf[0:N//(2*divide)], 20*np.log10(yf[0:N//(2*divide)]*(2/N)), label='FFT')
plt.plot(xf[0:N//(2*divide)], 20*np.log10(ywf[0:N//(2*divide)]*(2/N)), label='Blackman')
plt.legend()
plt.grid()

plt.show()

