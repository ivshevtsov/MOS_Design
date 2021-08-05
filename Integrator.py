import control
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

R=20e3
C=4e-12
Gain_OPA_db = 70
Gain = 10**(Gain_OPA_db/20)
r_out=500

s= control.tf('s')
pi=3.1415
p1=1e5*2*pi

A = Gain/((s/p1+1))
H_ideal =1/(s*R*C)
betta_inv=(1/(s*C)+R)/R
betta=1/betta_inv
Aft=(r_out/(r_out+R))/(1+A*betta)
Error_Term = (1/(1+1/(A*betta)))
H = H_ideal*Error_Term
H_res=H_ideal*Error_Term+Aft


Poles = control.pole(H)
Zeros = control.zero(H)
print('Poles = ', Poles)
print('Zeros = ', Zeros)
print(H)

freq = np.logspace(1, 11, 5000)


plt.figure()
control.bode_plot(A,
             label='Open Loop',
             dB=True,
             Hz=True,
             linewidth='3',
             c='Tab:red',
             grid=True,
             wrap_phase=True,
             omega = freq,
             plot=False     )

control.bode(betta_inv,
             label='Feedback Factor',
             dB=True,
             Hz=True,
             linewidth='3',
             c='Tab:blue',
             grid=True,
             wrap_phase=True,
             omega = freq,
             plot=False )

control.bode(Error_Term,
             label='Error Therm',
             dB=True,
             Hz=True,
             linewidth='3',
             c='Tab:green',
             grid=True,
             wrap_phase=True,
             omega = freq,
             plot=False )

control.bode(H,
             label='R=0 Ом',
             dB=True,
             Hz=True,
             linewidth='3',
             c='Tab:orange',
             grid=True,
             wrap_phase=False,
             omega = freq,
             plot=True )

control.bode(H_res,
             label=f'R={r_out} Ом',
             dB=True,
             Hz=True,
             linewidth='3',
             c='Tab:red',
             grid=True,
             wrap_phase=False,
             omega = freq,
             plot=True )

plt.legend()
plt.show()