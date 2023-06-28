import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import windows

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams["figure.figsize"] = (15,4)


Type = 'PEX'
Plot_Signal_1 = 'PPF(GPS)'
Home = 'Files/KAPDWA2_TRAN'
File = 'KAPDWA_FULL_1.8G_9.5-10.5u_interpolate_50p.csv'


if Type =='SCH':
    N_Sinals = {'RF_Port': 1, 'RF_IN': 2, 'MIX_OUT': 3,
                'PPF(GPS)': 4, 'PPF(GLO)': 5,'GPS_A': 6,
                'GLO_A': 7, 'VCAP': 8, 'QVCO(SINE)': 9}

    N_Sinals_NAME = {'RF_Port': 'A', 'RF_IN': 'B', 'MIX_OUT': 'D',
                'PPF(GPS)': 'E(GPS)', 'PPF(GLO)': 'E(GLO)','GPS_A': 'F(GPS)',
                'GLO_A': 'F(GLO)', 'VCAP': 'VCAP', 'QVCO(SINE)': 'C'}
else:
    N_Sinals = {'RF_Port': 1, 'RF_IN': 2, 'MIX_OUT': 3,
                'PPF(GPS)': 4, 'PPF(GLO)': 5, 'GPS_A': 6,
                'GLO_A': 7, 'QVCO(SINE)': 8}

    N_Sinals_NAME = {'RF_Port': 'A', 'RF_IN': 'B', 'MIX_OUT': 'D',
                     'PPF(GPS)': 'E(GPS)', 'PPF(GLO)': 'E(GLO)', 'GPS_A': 'F(GPS)',
                     'GLO_A': 'F(GLO)', 'QVCO(SINE)': 'C'}



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

freq = 9e9
divide = int(10e9/freq)
print(max(xf[0:N//2]))

plt.figure()
plt.title(N_Sinals_NAME[Plot_Signal_1])
plt.plot(xf[0:N//(2)], 20*np.log10(yf[0:N//(2)]*(2/N)), label='Rectangular')
plt.plot(xf[0:N//(2)], 20*np.log10(ywf[0:N//(2)]*(2/N)), label='Blackman')
plt.legend()
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.subplots_adjust(left=0.06, bottom=0.135, right=0.97, top=0.92, wspace=None, hspace=None)
plt.grid()

V_PP = max(Data)-min(Data)
print(f'V(PP) = {round(V_PP*1e3,3)} мВ')

plt.figure()
plt.title(N_Sinals_NAME[Plot_Signal_1])
plt.plot(X[:, 0], Data)
plt.xlabel('t, с')
plt.ylabel('U, В')
plt.subplots_adjust(left=0.06, bottom=0.135, right=0.97, top=0.92, wspace=None, hspace=None)
plt.grid()

plt.show()

