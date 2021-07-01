import numpy as np
import control
import matplotlib.pyplot as plt

s = control.tf('s')
G = (s+1)*(s+2)/((s+1)*(s+3))
G1 = (1)/((s+4)*(s+12))

print('G = ', G)
Poles = control.pole(G)
Zeros = control.zero(G)
print('Poles = ', Poles)
print('Zeros = ', Zeros)

gm, pm, wg, wp = control.margin(G)

plt.figure()
control.bode(G, dB=True, Hz=True)
#control.bode(G1, dB=True, Hz=True)

plt.figure()
N = control.pzmap(G, plot=True)
plt.grid()
plt.show()

