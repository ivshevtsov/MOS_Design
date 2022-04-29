import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home_NF = 'Files/KAPDWA2_AC_NF_P1DB/'
File_NF = 'KAPDWA_NF_GLO.csv'
Title_NF = 'Тракт GPS'

File_P1dB = 'KAPDWA_P1dB_GLO.csv'

NF_Data = np.genfromtxt(f'{Home_NF}/{File_NF}', delimiter=',', skip_header=1)
P1dB_Data = np.genfromtxt(f'{Home_NF}/{File_P1dB}', delimiter=',', skip_header=1)



plt.figure()
plt.title(Title_NF)
plt.plot(NF_Data[:,0], NF_Data[:,1], label = 'VGA_OUT(GPS)', linewidth ='3')
plt.plot(NF_Data[:,2], NF_Data[:,3], label = 'VGA_OUT(GLO)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.legend()
plt.grid(which="both")

plt.figure()
plt.title(Title_NF)
plt.plot(NF_Data[:,4], NF_Data[:,5], label = 'NF', linewidth ='3')
plt.plot(NF_Data[:,6], NF_Data[:,7], label = 'NF(DSB)', linewidth ='3')
plt.plot(NF_Data[:,8], NF_Data[:,9], label = 'NF(SSB)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('NF, дБ')
plt.legend()
plt.grid(which="both")


Pin_ideal = np.linspace(-80, -60, 20)
Pout_ideal = Pin_ideal+P1dB_Data[0,1]-P1dB_Data[0,0]-1

plt.figure()
plt.title(Title_NF)
plt.plot(P1dB_Data[:,0], P1dB_Data[:,1], linewidth ='3')
plt.plot(Pin_ideal, Pout_ideal, linewidth ='3')
plt.xlabel('Pin, дБм')
plt.ylabel('Pout, дБм')
plt.grid(which="both")

plt.figure()
plt.title(Title_NF)
plt.plot(P1dB_Data[:,2], P1dB_Data[:,3], linewidth ='3')

plt.xlabel('Pin, дБм')
plt.ylabel('Gain, дБ')
plt.grid(which="both")



plt.show()



