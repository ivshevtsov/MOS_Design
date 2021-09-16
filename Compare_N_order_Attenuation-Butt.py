import control
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def GD(Phase, Freq, label):
    Diff = -(np.diff(Phase) / np.diff(Freq))
    wGD = []
    for i in range(len(Diff)):
        xtemp = (Freq[i] + Freq[i + 1]) / 2
        wGD = np.append(wGD, xtemp)
    plt.plot(wGD/(2*np.pi), Diff,linewidth=3, label=label)
    plt.grid(which='both', axis='both')

K=0
if K==0:
    Title = 'GPS'
    F3db = 2e6
    Fppf = 14.6e6
elif K==1:
    Title = 'GLONASS'
    F3db = 5e6
    Fppf = 12e6


w_LPF = 2*np.pi*F3db
wPPF = 2*np.pi*Fppf
F_range = np.linspace(-2*np.pi*Fppf,2*np.pi*2.5*Fppf, 500)

s= control.tf('s')

#First order Filter
FIRST = w_LPF/((s-1j*wPPF)+w_LPF)

#Second order filter
Q2 = 0.707
SECOND = (w_LPF**2) / ((s-1j*wPPF) ** 2 + (s-1j*wPPF) * (w_LPF / Q2) + w_LPF**2)

#Third order filter
Q3 = 1
THIRD = FIRST*(w_LPF**2) / ((s-1j*wPPF) ** 2 + (s-1j*wPPF) * (w_LPF / Q3) + w_LPF**2)

mag1, ph1, w1 = control.bode(FIRST, plot=False,  omega=F_range)
mag2, ph2, w2 = control.bode(SECOND, plot=False, omega=F_range)
mag3, ph3, w3 = control.bode(THIRD, plot=False, omega=F_range)

plt.figure()
plt.title(Title)
GD(Phase=ph1, Freq=w1, label='N=1')
GD(Phase=ph2, Freq=w2, label='N=2')
GD(Phase=ph3, Freq=w3, label='N=3')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('GD(f), c')

plt.figure()
plt.title(Title)
plt.plot(w1/(2*np.pi), 20*np.log10(mag1), linewidth=3, label='N=1')
plt.plot(w2/(2*np.pi), 20*np.log10(mag2), linewidth=3, label='N=2')
plt.plot(w3/(2*np.pi), 20*np.log10(mag3), linewidth=3, label='N=3')
#plt.xscale("log")
plt.legend()
plt.grid(which='both', axis='both')
plt.xlabel('f, Гц')
plt.ylabel('T(f), дБ')



plt.show()