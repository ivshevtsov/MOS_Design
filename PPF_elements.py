import numpy as np

##--Initial conditions--##
F_CLK = 16e6
F_3dB = F_CLK/(2*np.pi)
R = 2000*6
C = 1/(2*np.pi*R*F_3dB)
F_PPF = 13.3e6
R_PPF = 1/(2*np.pi*C*F_PPF)

F_LPF = 1/(2*np.pi*R*C)
print(C)
print(F_LPF)
print(R_PPF)

print(1/(2*np.pi*C*1900))



