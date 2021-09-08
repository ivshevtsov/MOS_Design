import random
import matplotlib.pyplot as plt
import numpy as np
import control

def Second_poly(W0, Q, Num_Fig=1):
    s = control.tf('s')
    TF = (W0 ** 2) / (s ** 2 + s * (W0 / Q) + W0 ** 2)
    mag, ph, w = control.bode(TF, plot=False, color='Tab:red')
    plt.figure(Num_Fig)
    plt.plot(w, 20 * np.log10(mag), color='Tab:red')


#-----------Global Variable---------#

N=1000
Q=0.707
w0=4e6
Accuracy = 0.2

#---Sallen-Key architecture(VCVS)---#
SK_R  = 20e3
SK_C1 = 2*Q/(SK_R*w0)
SK_C2 = 1/(2*Q*SK_R*w0)
SK_W0_sens =[]
SK_Q_sens = []
for i in range(N):
    #randomization elements
    SK_R_sens = random.gauss(SK_R, SK_R * Accuracy / 3)
    SK_C1_sens = random.gauss(SK_C1, SK_C1 * Accuracy / 3)
    SK_C2_sens = random.gauss(SK_C2, SK_C2 * Accuracy / 3)
    #calculate W0 and Q
    SK_W0 = 1/(np.sqrt(SK_C1_sens*SK_C2_sens)*SK_R_sens)
    SK_W0_sens.append(SK_W0)
    SK_Q = 0.5*np.sqrt(SK_C1_sens/SK_C2_sens)
    SK_Q_sens.append(SK_Q)
    Second_poly(W0=SK_W0, Q=SK_Q, Num_Fig=1)

plt.xscale("log")
plt.grid(which='both', axis='both')

plt.figure()
plt.hist(SK_W0_sens)
plt.grid()
plt.figure()
plt.hist(SK_Q_sens)
plt.grid()

#---------------end------------------#

#-------Multiple Feedback(VCVS)------#



plt.show()

