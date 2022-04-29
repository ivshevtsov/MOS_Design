import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'Files/PPF_MFB_PASS'
File_MFB = 'MFB_PPF_HF_GD.csv'
File_PASS = 'Passive_PPF_HF_GD.csv'
File_PASS_rx = 'Passive_receiver.csv'
File_MFB_rx = 'MFB_receiver.csv'

def Band_PPF(Data_HF_x, Data_HF_y):
    max_gain = max(Data_HF_y)
    list_band = []
    for i in range(len(Data_HF_y)):
        if max_gain-Data_HF_y[i]<=3.1 and max_gain-Data_HF_y[i]>=2.9:
            list_band.append(Data_HF_x[i])
    Band_PPF = max(list_band)-min(list_band)
    Band_LPF = max(list_band)
    return max_gain, Band_PPF, Band_LPF





Data_MFB = np.genfromtxt(f'{Home}/{File_MFB}', delimiter=',', skip_header=1)
Data_PASS = np.genfromtxt(f'{Home}/{File_PASS}', delimiter=',', skip_header=1)
Data_PASS_rx = np.genfromtxt(f'{Home}/{File_PASS_rx}', delimiter=',', skip_header=1)
Data_MFB_rx = np.genfromtxt(f'{Home}/{File_MFB_rx}', delimiter=',', skip_header=1)


#Passive
gain_pass, band_pass, band_pass_lpf =Band_PPF(Data_PASS[:,0], Data_PASS[:,1])
print(f'Gain(PASS) = {gain_pass}, дБ')
print(f'Band_PPF(PASS)={band_pass/1e6}, МГц')
print(f'Band_LPF(PASS)={band_pass_lpf/1e6}, МГц')

plt.figure()
plt.title('Passive')
plt.plot(Data_PASS[:,0], Data_PASS[:,1], label = '', linewidth ='3')
plt.plot(Data_PASS[:,0], Data_PASS[:,2], label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.grid(which="both")

plt.figure()
plt.title('Passive')
plt.plot(Data_PASS[:,3], Data_PASS[:,4]*1e9, label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('GD, нс')
plt.grid(which="both")

plt.figure()
plt.title('Passive')
plt.plot(Data_PASS_rx[:,0], Data_PASS_rx[:,1], label = '', linewidth ='3')
plt.plot(Data_PASS_rx[:,0], Data_PASS_rx[:,2], label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.grid(which="both")

plt.figure()
plt.title('Passive')
plt.plot(Data_PASS_rx[:,3], Data_PASS_rx[:,4], label = 'NF(DSB)', linewidth ='3')
plt.plot(Data_PASS_rx[:,3], Data_PASS_rx[:,5], label = 'NF(SSB)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('NF, дБ')
plt.legend()
plt.grid(which="both")

#MFB
gain_mfb, band_mfb, band_mfb_lpf =Band_PPF(Data_MFB[:,0], Data_MFB[:,1])
print(f'Gain(MFB) = {gain_mfb}, дБ')
print(f'Band_PPF(MFB)={band_mfb/1e6}, МГц')
print(f'Band_LPF(MFB)={band_mfb_lpf/1e6}, МГц')

plt.figure()
plt.title('MFB')
plt.plot(Data_MFB[:,0], Data_MFB[:,1], label = '', linewidth ='3')
plt.plot(Data_MFB[:,0], Data_MFB[:,2], label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.grid(which="both")

plt.figure()
plt.title('MFB')
plt.plot(Data_MFB[:,3], Data_MFB[:,4]*1e9, label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('GD, нс')
plt.grid(which="both")

plt.figure()
plt.title('MFB')
plt.plot(Data_MFB_rx[:,0], Data_MFB_rx[:,1], label = '', linewidth ='3')
plt.plot(Data_MFB_rx[:,0], Data_MFB_rx[:,2], label = '', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.grid(which="both")

plt.figure()
plt.title('MFB')
plt.plot(Data_PASS_rx[:,3], Data_MFB_rx[:,4], label = 'NF(DSB)', linewidth ='3')
plt.plot(Data_PASS_rx[:,3], Data_MFB_rx[:,5], label = 'NF(SSB)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('NF, дБ')
plt.legend()
plt.grid(which="both")





plt.show()