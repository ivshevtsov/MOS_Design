import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3

sample_rate = 44100*2 #частота дискретизации
duration = 1 #длительность импульса
freq = 10000 #частота импульса
N = sample_rate*duration

t = np.linspace(0, duration, sample_rate*duration, endpoint=False)
LO_t=np.cos((2*np.pi)*freq*t)
IM_t = np.cos((2*np.pi)*(freq-5000)*t)
SI_t = np.cos((2*np.pi)*(freq+5000)*t)
IM_IF_t = IM_t*LO_t
SI_IF_t = SI_t*LO_t

LO_f = fft(LO_t)/N
IM_f = fft(IM_t)/N
SI_f = fft(SI_t)/N
IM_IF_f = fft(IM_IF_t)/N
SI_IF_f = fft(SI_IF_t)/N

tf = fftfreq(N, 1/sample_rate)

plt.figure()
plt.plot(tf, SI_IF_f.real, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('Re')
plt.ylim(min(LO_f.real)-0.1,max(LO_f.real)+0.1)
plt.grid()

plt.figure()
plt.plot(tf, SI_IF_f.imag, linewidth='3')
plt.xlabel('F, Гц')
plt.ylabel('Im')
plt.ylim(min(LO_f.imag)-0.1,max(LO_f.imag)+0.1)
plt.grid()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(tf, IM_IF_f.real, IM_IF_f.imag,  label='parametric curve', color = 'Tab:green', linewidth='6')
ax.plot(tf, SI_IF_f.real, SI_IF_f.imag,  label='parametric curve', color = 'Tab:blue')

#ax.plot(tf, IM_f.real, IM_f.imag,  label='parametric curve', color = 'Tab:green')
#ax.plot(tf, SI_f.real, SI_f.imag,  label='parametric curve', color = 'Tab:blue')
#ax.plot(tf, LO_f.real, LO_f.imag,  label='parametric curve', color = 'Tab:red')
ax.set_zlim(-max(SI_IF_f.real)-0.1, max(SI_IF_f.real)+0.1)
ax.set_ylim(min(SI_IF_f.real)-0.1, max(SI_IF_f.real)+0.1)
ax.set_xlabel('F, Гц')
ax.set_ylabel('Re')
ax.set_zlabel('Im')

plt.show()
