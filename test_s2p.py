import skrf as rf
import matplotlib.pyplot as plt



Name = rf.Network(f'C:/Users/SH/PycharmProjects/KAP_Verification/DATA/IB2/LNA0/s2p/LNA0_chip_#2.s2p')
plt.figure()
Name.s12.plot_s_db(label='S21')
Name.s11.plot_s_db(label='S21')

plt.figure()
Name.s11.plot_s_smith()
plt.grid()
plt.show()