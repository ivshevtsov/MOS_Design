import numpy as np

##Initial state values
unCox = 155e-6
upCox = 50e-6
L=0.55e-6

#requirements
RL = 5.0e3
Gm=5e-3
 

Gain  = 20*np.log10((2**0.5)/(np.pi)*Gm*RL)
print(f'Transconductance {Gm}')
print(f'Gain {Gain}')

##Inverter based gm
Veff_inv = 0.45
Id_inv = Gm*0.5*Veff_inv/2
Wn_inv = 2*Id_inv*L/(unCox*Veff_inv**2)
Wp_inv = 2*Id_inv*L/(upCox*Veff_inv**2)

print(f'Wp inverter {Wp_inv*1e6} um')
print(f'Wn inverter {Wn_inv*1e6} um')

print(f'Transconductance {Gm*0.5*1e3} mS')
print(f'Equivalent resistance {1/(0.5*Gm)} Ohm')
print(f'Current inverter {Id_inv*1e6} uA')
print(f'#-------------------------#')


#Diff amp based gm
Veff_diff = 0.2
Rs_diff = 1/Gm
Gm_diff = Gm
Id_diff = Gm_diff*Veff_diff/2




print(f'Current diff pair {Id_diff*1e6} uA')

