import control
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3


F_LPF = 2.5e6
F_PPF = 13.29e6
Fmin = -50e6
Fmax =  50e6
##-----------------------------------##
##-----------------------------------##
s= control.tf('s')
omega = np.linspace( Fmin, Fmax, 1000)
Q=0.707
TF = (F_LPF**2) / ((s-1j*F_PPF)**2 + (s-1j*F_PPF)*(F_LPF / Q) + F_LPF**2)

mag, ph, w = control.bode(TF, plot=False, color='Tab:red', Hz = True, omega=omega)
Poles = control.pole(TF)
Zeros = control.zero(TF)

print('G = ', TF)
print('Poles = ', Poles)
print('Zeros = ', Zeros)

Home = 'Files/Filters/PPF_HF_model'
with open(f'{Home}/GPS.csv', 'w') as File:
    File.write('freq(Hz), HF(dB)\n')
    for i in range(len(mag)):
        str = '{freq:.4e}, {mag:15.10f}\n'.format(freq=w[i], mag =20*np.log10(mag[i]))
        File.write(str)
    File.close()




#Plot H(f)
plt.figure()
plt.plot(w, 20*np.log10(mag), color='Tab:red')
plt.grid(which='both', axis='both')
plt.show()