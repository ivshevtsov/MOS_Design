import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'Files/PPF_Problem/'
File = 'PPF_NON_NO_VGA.csv'



Data = np.genfromtxt(f'{Home}/{File}', delimiter=',', skip_header=1)


plt.figure()
plt.plot(Data[:,0], Data[:,1], label = 'I+', linewidth ='3')
plt.plot(Data[:,2], Data[:,3], label = 'I-', linewidth ='3')
plt.plot(Data[:,4], Data[:,5], label = 'Q+', linewidth ='3')
plt.plot(Data[:,6], Data[:,7], label = 'Q-', linewidth ='3')

plt.xlabel('f, Гц')
plt.ylabel('Gain, дБ')
plt.legend()
plt.grid(which="both")

plt.figure()
plt.plot(Data[:,0], Data[:,1]-Data[:,3], label = 'I_Error', linewidth ='3')
plt.plot(Data[:,2], Data[:,5]-Data[:,7], label = 'Q_Error', linewidth ='3')
plt.plot(Data[:,2], Data[:,1]-Data[:,7], label = 'IQ_Error', linewidth ='3')
plt.plot(Data[:,2], Data[:,5]-Data[:,3], label = 'IQ_Error', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Error Gain, дБ')
plt.legend()
plt.grid(which="both")


plt.figure()
plt.plot(Data[:,8], Data[:,9], label = 'I+', linewidth ='3')
plt.plot(Data[:,10], Data[:,11], label = 'I-', linewidth ='3')
plt.plot(Data[:,12], Data[:,13], label = 'Q+', linewidth ='3')
plt.plot(Data[:,14], Data[:,15], label = 'Q-', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Phase, град.')
plt.legend()
plt.grid(which="both")

plt.figure()
plt.plot(Data[:,8], abs(Data[:,9]-Data[:,11])-180, label = 'I_Error', linewidth ='3')
plt.plot(Data[:,8], abs(Data[:,13]-Data[:,15])-180, label = 'Q_Error', linewidth ='3')
plt.plot(Data[:,8], abs(Data[:,13]-Data[:,11])-90, label = 'IQ_Error', linewidth ='3')
plt.plot(Data[:,8], abs(Data[:,15]-Data[:,9])-90, label = 'IQ_Error', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('Error, град.')
plt.legend()
plt.grid(which="both")

plt.figure()
plt.plot(Data[:,16], Data[:,17]-max(Data[:,17]), label = 'HF', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('HF, дБ')
plt.legend()
plt.grid(which="both")



h = Data[:,19]
w=  Data[:,18]
w1 = np.delete(w, -1)
group_delay = -(1/360)*np.diff(h)/np.diff(w)


plt.figure()
plt.plot(w1, group_delay*1e9 , label = 'HF', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('GD, c')
plt.legend()
plt.grid(which="both")

plt.show()