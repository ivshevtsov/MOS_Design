import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

def dBm_to_uV(Value,Z):
    V_RMS = np.sqrt(10**(Value/10)*Z*1e-3)
    V_PP = V_RMS*2*np.sqrt(2)
    return V_RMS, V_PP

def uV_to_dBm(Value, Z):
    dBm = 20*np.log10(Value*1e6)-10*np.log10(Z)-90
    return dBm

dBm_Value = -100
Rs=50

V_RMS, V_PP = dBm_to_uV(dBm_Value, Rs)
dBm = uV_to_dBm(V_RMS, Rs)

print(f'RMS Voltage={V_RMS}, V')
print(f'Peak to Peak Voltage={V_PP}, V')
print(f'dBm Value={dBm}, dBm')


dBm_plot = np.linspace(0, -100, 100)
uV_plot = dBm_to_uV(dBm_plot,Rs)

plt.plot(dBm_plot, uV_plot[0], linewidth ='3')
plt.xlabel('dBm')
plt.ylabel('V(RMS)')
plt.yscale('log')
plt.grid(which="both")
plt.show()
