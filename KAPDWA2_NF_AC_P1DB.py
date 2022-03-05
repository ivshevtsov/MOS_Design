import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'Files/KAPDWA2_AC_NF_P1DB/'
File = 'KAPDWA_NF_GLO.csv'
Title_NF = 'Тракт ГЛОНАСС'


NF_Data = np.genfromtxt(f'{Home}/{File}', delimiter=',', skip_header=1)

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

plt.show()



