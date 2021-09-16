import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3

sample_rate = 44100 #частота дискретизации
duration = 1 #длительность импульса
freq = 10000 #частота импульса
N = sample_rate*duration

t = np.linspace(0, duration, sample_rate*duration, endpoint=False)
y=np.sin((2*np.pi)*freq*t)
#y=(np.exp(1j*2*np.pi*freq*t)+np.exp(-1j*2*np.pi*freq*t))/2


yf = fft(y)/N
tf = fftfreq(N, 1/sample_rate)

plt.figure()
plt.plot(tf, yf.real, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('Re')
plt.ylim(min(yf.real)-0.1,max(yf.real)+0.1)
plt.grid()

plt.figure()
plt.plot(tf, yf.imag, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('Im')
plt.ylim(min(yf.imag)-0.1,max(yf.imag)+0.1)
plt.grid()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(tf, yf.real,yf.imag,  label='parametric curve')
ax.plot(tf, yf.real,-yf.imag,  label='parametric curve')
ax.set_zlim(min(yf.imag)-0.1, max(yf.imag)+0.1)
ax.set_ylim(min(yf.real)-0.1, max(yf.real)+0.1)
ax.set_xlabel('F, Гц')
ax.set_ylabel('Re')
ax.set_zlabel('Im')


plt.show()
