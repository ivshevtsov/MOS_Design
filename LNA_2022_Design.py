import numpy as np
import matplotlib.pyplot as plt
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

gm = 20e-3
Cgs = 500e-15
L = 2e-9
w = 1.6e9*2*np.pi
Cpad = 0.5e-12

#Cgs for plot
Cgs = np.linspace(300e-15, 2e-12, 100)
#print(Cgs)


Zpad = 1/(1j*w*Cpad)
Zin_LNA = (gm*L)/Cgs + 1j*w*L + 1/(1j*w*Cgs)
Zin_PAD = (Zpad*Zin_LNA)/(Zin_LNA+Zpad)

n=40
print(f'Zin(LNA)={Zin_LNA[n]}')
print(f'Zin(PAD)={Zin_PAD[n]}')
print(f'Cgs={Cgs[n]}')
#print(f'Lg={abs(Zin_PAD[n])/w}')


plt.figure()
plt.title(f'Cpad={Cpad*1e12}пФ')
plt.plot(Cgs*1e12, Zin_LNA.imag, label='Zin(LNA)', linewidth='3')
plt.plot(Cgs*1e12, Zin_PAD.imag, label='Zin(PAD+LNA)', linewidth='3')
plt.xlabel('Cgs, пФ')
plt.ylabel('Z(Im), Ом')
plt.legend()
plt.grid()

plt.figure()
plt.title(f'Cpad={Cpad*1e12}пФ')
plt.plot(Cgs*1e12, Zin_LNA.real, label='Zin(LNA)', linewidth='3')
plt.plot(Cgs*1e12, Zin_PAD.real, label='Zin(PAD+LNA)', linewidth='3')
plt.xlabel('Cgs, пФ')
plt.ylabel('Z(Re), Ом')
plt.legend()
plt.grid()

plt.figure()
plt.title(f'Cpad={Cpad*1e12}пФ')
plt.plot(Cgs*1e12, (abs(Zin_LNA)/w)*1e9, label='Lg(LNA)', linewidth='3')
plt.plot(Cgs*1e12, (abs(Zin_PAD)/w)*1e9, label='Lg(PAD)', linewidth='3')
plt.xlabel('Cgs, пФ')
plt.ylabel('L, нГн')
plt.legend()
plt.grid()


EM_File = "Files/LNA/Results/LNA_0_EM_TYP.csv"
Title = 'EM'
EM_RES=read_file(EM_File, dot = ',', Text = '')

PEX_File = "Files/LNA/Results/LNA_0_PEX_TYP.csv"
PEX_RES=read_file(PEX_File, dot = ',', Text = '')

Casc_File = "Files/LNA/Results/LNA_cascaded.csv"
Casc_RES=read_file(Casc_File, dot = ',', Text = '')


plt.figure()
plt.title(Title)
plt.plot(EM_RES[:, 0], EM_RES[:, 1], label='Gain', linewidth ='3')
plt.plot(EM_RES[:, 0], EM_RES[:, 2], label='S11', linewidth ='3')
plt.plot(EM_RES[:, 0], EM_RES[:, 3], label='S22', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title(Title)
plt.plot(EM_RES[:, 0], EM_RES[:, 4], label='NF', linewidth ='3')
plt.plot(EM_RES[:, 0], EM_RES[:, 5], label='NF(min)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title('EM/PEX Compare')
plt.plot(EM_RES[:, 0], EM_RES[:, 1], label='Gain(EM)', linewidth ='3')
plt.plot(PEX_RES[:, 0], PEX_RES[:, 1], label='Gain(PEX)', linewidth ='3')
plt.plot(EM_RES[:, 0], EM_RES[:, 2], label='S11(EM)', linewidth ='3')
plt.plot(PEX_RES[:, 0], PEX_RES[:, 2], label='S11(PEX)', linewidth ='3')
plt.plot(EM_RES[:, 0], EM_RES[:, 3], label='S22(EM)', linewidth ='3')
plt.plot(PEX_RES[:, 0], PEX_RES[:, 3], label='S22(PEX)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title('EM/PEX Compare')
plt.plot(EM_RES[:, 0], EM_RES[:, 4], label='NF(EM)', linewidth ='3')
plt.plot(PEX_RES[:, 0], PEX_RES[:, 4], label='NF(PEX)', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title('Cascade')
plt.plot(Casc_RES[:, 0], Casc_RES[:, 1], label='Gain', linewidth ='3')
plt.plot(Casc_RES[:, 0], Casc_RES[:, 2], label='S11', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()

plt.figure()
plt.title('Cascade')
plt.plot(Casc_RES[:, 0], Casc_RES[:, 3], label='NF', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('дБ')
plt.legend()
plt.grid()



plt.show()



#print(Zin)
#print(Zin_LNA)