from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Functions import Butterworth_pole_zero
from Functions import pole_zero_plot

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#parameters of filter
Order=3
Freq = 1

#Plot different H(f)
plt.figure()
plt.title('Фильтр Баттерворта')
for i in range(5):
    b, a = signal.butter(i+1, Freq, btype='lowpass', analog=True, output='ba')
    f, h = signal.freqs(b, a)
    plt.semilogx(f, 20*np.log10(abs(h)), label= f'N={i+1}')
plt.legend()
plt.xlabel('F, Гц')
plt.ylabel('H(f), дБ')
plt.grid(which='both', axis='both')


z, p , k = signal.butter(Order, Freq, btype='lowpass', analog=True, output='zpk')
Butterworth_pole_zero(Order, Freq, p, z)
pole_zero_plot(p, z)
plt.show()


#plt.title(r'$p(x)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$')