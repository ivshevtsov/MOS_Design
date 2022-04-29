import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'Files/MIX_PPF_NON/'
File = '/GLO/PPF_NON_IDEAL.csv'



Data_Ideal = np.genfromtxt(f'{Home}/{File}', delimiter=',', skip_header=1)
Data_LPF = np.genfromtxt(f'{Home}/GLO/PPF_NON_LPF_10k_200F.csv', delimiter=',', skip_header=1)
Data_PAC = np.genfromtxt(f'{Home}/GLO/PPF_PAC_outPPF_GLO.csv', delimiter=',', skip_header=1)
Data_Tran = np.genfromtxt(f'{Home}/GLO/PPF_NON_Tran(MIX).csv', delimiter=',', skip_header=1)

Data_I5_Tran = np.genfromtxt(f'{Home}/GLO/PPF_5mV_reverse_90.csv', delimiter=',', skip_header=1)
Data_I10_Tran = np.genfromtxt(f'{Home}/GLO/PPF_10mV_reverse_90.csv', delimiter=',', skip_header=1)
Data_I20_Tran = np.genfromtxt(f'{Home}/GLO/PPF_10mV_reverse_90.csv', delimiter=',', skip_header=1)

plt.figure()
plt.plot(Data_Ideal[:,0], Data_Ideal[:,1]-max(Data_Ideal[:,1]), label = 'Ideal', linewidth ='3')
plt.plot(Data_LPF[:,0], Data_LPF[:,1]-max(Data_LPF[:,1]), label = 'LPF+Ideal', linewidth ='3')
plt.plot(Data_PAC[:,2]+700e3, Data_PAC[:,3]-max(Data_PAC[:,3]), label = 'PAC', linewidth ='3')
plt.plot(Data_Tran[:,0]-1.588e9+700e3, Data_Tran[:,1]-max(Data_Tran[:,1]), label = 'Tran', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.legend()
plt.grid(which="both")


plt.figure()
plt.plot(Data_I5_Tran[:,0], Data_I5_Tran[:,1]-max(Data_I5_Tran[:,1]), label = 'VPP=20m', linewidth ='3')
plt.plot(Data_I10_Tran[:,0], Data_I10_Tran[:,1]-max(Data_I10_Tran[:,1]), label = 'VPP=40m', linewidth ='3')
plt.plot(Data_I20_Tran[:,0], Data_I20_Tran[:,1]-max(Data_I20_Tran[:,1]), label = 'VPP=80m', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.legend()
plt.grid(which="both")

plt.show()