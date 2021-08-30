import control
import matplotlib.pyplot as plt
import numpy as np
import sympy

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3
plt.rcParams["figure.figsize"]=[4,4]

Q=0.7
Q_L=[0.5, 0.707, 1, 3]
T=np.linspace(0, 25, 100)
omega = np.logspace(-1, 1, 500)
w=1
Type = 'BSF'



s= control.tf('s')
if Type=='LPF':
    G = (w**2) / (s ** 2 + s * (w / Q) + w**2)
elif Type=='BPF':
    G = (s*(w/Q)) / (s ** 2 + s * (w / Q) + w**2)
elif Type=='HPF':
    G = (s**2) / (s ** 2 + s * (w / Q) + w**2)
elif Type=='BSF':
    G = (s**2+w**2) / (s ** 2 + s * (w / Q) + w**2)




ts, xs =control.step_response(G)
mag, ph, w = control.bode(G, plot=False, color='Tab:red')
Poles = control.pole(G)
Zeros = control.zero(G)
print('G = ', G)
print('Poles = ', Poles)
print('Zeros = ', Zeros)


#Step responce
plt.figure()
plt.grid()
plt.plot(ts, xs)

#plot PZ
plt.figure()
N = control.pzmap(G, plot=True)
plt.subplots_adjust(bottom=0.14)
plt.subplots_adjust(left=0.22)
#plt.grid()

#Plot H(f)
plt.figure()
plt.plot(w, 20*np.log10(mag), color='Tab:red')
plt.xscale("log")
plt.grid(which='both', axis='both')

#multiple Step
plt.figure()
for i in Q_L:
    TF = 1 / (s ** 2 + s * (1 / i) + 1)
    ts, xs = control.step_response(TF, T=T)
    plt.plot(ts, xs, label=rf'Q={i}, $\zeta$={round(1/(2*i),3)}')
plt.grid()
plt.legend()

#multiple H(f)

plt.figure()
for i in Q_L:
    TF = 1 / (s ** 2 + s * (1 / i) + 1)
    mag, ph, w = control.bode(TF, plot=False, omega=omega)
    plt.plot(w, 20*np.log10(mag), label=rf'Q={i}, $\zeta$={round(1/(2*i),3)}')

plt.xscale("log")
plt.grid(which='both', axis='both')
plt.legend()


plt.show()