from sympy.abc import s
from sympy.abc import t
from sympy import lambdify
from sympy.physics.control.lti import TransferFunction
import matplotlib.pyplot as plt
import numpy as np
from math import log10
from cmath import phase
from matplotlib.widgets import Cursor, Button

fp = 1/((1+s/100)*(1+s/1e6))
Freq = np.logspace(1, 9, 100, endpoint=True)
Function_plot = np.zeros([len(Freq), 2], float)
Function = lambdify(s, fp)

for i in range(len(Freq)):
    Function_Buf = 20*np.log10(abs(Function(complex(0, Freq[i]))))
    Function_Buf_1 = phase(Function(complex(0, Freq[i])))*180/3.14
    Function_plot[i, 0] = Function_Buf
    Function_plot[i, 1] = Function_Buf_1


fig, ax =plt.subplots()
plt.plot(Freq[:], Function_plot[:, 1])
plt.plot(Freq[:], Function_plot[:, 0])
plt.xscale('log')

cursor = Cursor(ax,useblit=True, color = 'tab:green')

plt.grid()

plt.show()









