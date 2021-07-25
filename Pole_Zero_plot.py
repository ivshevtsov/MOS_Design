import control
import matplotlib.pyplot as plt
import numpy as np
import sympy


plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3
plt.rcParams["figure.figsize"]=[4,4]

#first s*(Num/Den) second 1*(Num/Den)
Num=[-1, 1]
Den=[1, 1]

X=np.linspace(-5, 5, 100)
Y=np.arctan(X)*180/3.1415
plt.figure()
plt.plot(X,Y)
plt.grid()
plt.xlabel('X')
plt.ylabel('atan(X), град.')
plt.ylim([-90, 90])

s= control.tf('s')
G =(s*Num[0]+Num[1])/(s*Den[0]+Den[1])
#(s*Num[0]+Num[1])/(s*Den[0]+Den[1])

print('G = ', G)
Poles = control.pole(G)
Zeros = control.zero(G)
print('Poles = ', Poles)
print('Zeros = ', Zeros)

gm, pm, wg, wp = control.margin(G)

plt.figure()
control.bode(G, dB=True, Hz=False, linewidth='3', c='Tab:red', grid=False, wrap_phase=True)
plt.subplots_adjust(bottom=0.16)
plt.subplots_adjust(left=0.2)
plt.subplots_adjust(hspace=0.25)
#control.bode(G1, dB=True, Hz=True)

plt.figure()
N = control.pzmap(G, plot=True)
plt.subplots_adjust(bottom=0.14)
plt.subplots_adjust(left=0.22)
#plt.grid()


print('##-------------------------Sympy---------------------------------##')

if Num[0]>0 or Num[0]<0:
    print('Error Laplace')
else:
    t, s = sympy.symbols('t,s')
    T = (s * Num[0] + Num[1]) / (s * Den[0] + Den[1])
    print(T)
    INV_L = sympy.inverse_laplace_transform(T, s, t)
    print(INV_L)
    A = sympy.plot(INV_L, show=True, line_color='Tab:red',
                   xlim=[-1, 2],
                   ylim=[-1, 2],
                   line_width=3)

plt.show()

