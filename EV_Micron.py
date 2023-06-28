import skrf as rf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

#function for creation s2p sim files /s2p_sim
def create_s2p_files():

    SxP = rf.Network(f'{Home}/sXp/raw_data.s3p')

    # Create touchstone file
    S2P_BUF = rf.four_oneports_2_twoport(SxP.s11, SxP.s12, SxP.s21, SxP.s22)
    S2P_LPF = rf.four_oneports_2_twoport(SxP.s11, SxP.s13, SxP.s31, SxP.s33)
    print(S2P_LPF)
    print(S2P_BUF)
    # Write file
    S2P_BUF.write_touchstone(filename=f'BUF.s2p', dir=f'{Home}/s2p_sim')
    S2P_LPF.write_touchstone(filename=f'LPF.s2p', dir=f'{Home}/s2p_sim')
#create_s2p_files()
#Calculate Bandwidth
def Band(LPF, BUF, label):
    HF = LPF.s_db[:,1,0]-BUF.s_db[:,1,0]
    Gain = max(HF)
    i=0
    for k in HF:
        if k>=Gain-3:
            i=i+1
        else:
            Band = LPF.f[i]
    print(label)
    print(f'Gain={round(Gain,3)} дБ')
    print(f'Band={round(Band/1e6,3)} МГц')
    print('#----------#')


Home = f'Files/EV_Micron'
list_dir = ['sim', 'meas_1', 'meas_2']


for i in list_dir:
    LPF = rf.Network(f'{Home}/s2p_{i}/LPF.s2p')
    BUF = rf.Network(f'{Home}/s2p_{i}/BUF.s2p')
    Band(LPF, BUF, i)
    #Plot results

    plt.figure(1)
    #PLOT_s_db_Netw(LPF, label='LPF', N_fig=1, sp=21)
    #PLOT_s_db_Netw(BUF, label='BUF', N_fig=1, sp=21)
    plt.semilogx(LPF.f, LPF.s_db[:,1,0]-BUF.s_db[:,1,0], linewidth=3, label=f'{i}')
    plt.xlabel('Freq, Гц')
    plt.ylabel('HF, дБ')
    plt.legend()
    plt.grid(1)

    plt.figure(2)
    p = 2
    gd = abs(LPF.group_delay)-abs(BUF.group_delay)
    delta_GD = max(gd[p:,1,0]*1e9)-gd[p,1,0]*1e9
    plt.plot(LPF.f[p:], gd[p:,1,0]*1e9, linewidth=3, label=f'{i}(dGD={round(delta_GD,1)} нс)')
    plt.xlabel('Freq, Гц')
    plt.ylabel('GD, нс')
    plt.legend()
    plt.grid(2)


plt.show()

#Links
#https://scikit-rf.readthedocs.io/en/latest/tutorials/Plotting.html?highlight=group_delay