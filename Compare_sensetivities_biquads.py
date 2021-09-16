import random
import matplotlib.pyplot as plt
import numpy as np
import control
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3


#------------Functions---------------#

def Second_poly(W0, Q, Num_Fig=1):
    s = control.tf('s')
    Freq = np.logspace(4, 8, 500)
    TF = (W0 ** 2) / (s ** 2 + s * (W0 / Q) + W0 ** 2)
    mag, ph, w = control.bode(TF, plot=False, color='Tab:red', omega=Freq)
    plt.figure(Num_Fig)
    plt.plot(w, 20 * np.log10(mag), color='Tab:red')

def Plot_hist(Title, Hist_w0, Hist_Q):
    plt.figure()
    plt.title(rf'{Title}:$\mu$={np.mean(Hist_w0):.2e},$\sigma$={np.std(Hist_w0):.2e}')
    plt.hist(Hist_w0)
    plt.xlabel(r'$\omega _{0}$')
    plt.ylabel('N')
    plt.grid()
    plt.figure()
    plt.title(rf'{Title}:$\mu$={np.mean(Hist_Q):.2e},$\sigma$={np.std(Hist_Q):.2e}')
    plt.hist(Hist_Q)
    plt.xlabel('Q')
    plt.ylabel('N')
    plt.grid()

def VCVS(w0, Q, Res, N, Accuracy):
    SK_R = Res
    SK_C1 = 2 * Q / (SK_R * w0)
    SK_C2 = 1 / (2 * Q * SK_R * w0)

    print('#---Sallen-Key---#')
    print(f'C1={SK_C1}')
    print(f'C2={SK_C2}')
    print(f'R1={SK_R}')
    print(f'R2={SK_R}')
    print('#----------------#')
    SK_W0_sens = []
    SK_Q_sens = []
    for i in range(N):
        # randomization elements
        SK_R1_sens = random.gauss(SK_R, SK_R * Accuracy / 3)
        SK_R2_sens = random.gauss(SK_R, SK_R * Accuracy / 3)
        SK_C1_sens = random.gauss(SK_C1, SK_C1 * Accuracy / 3)
        SK_C2_sens = random.gauss(SK_C2, SK_C2 * Accuracy / 3)
        # calculate W0 and Q
        SK_W0 = 1 / (np.sqrt(SK_C1_sens * SK_C2_sens * SK_R1_sens * SK_R2_sens))
        SK_W0_sens.append(SK_W0)
        SK_Q = (SK_W0 * SK_C1_sens * SK_R2_sens * SK_R1_sens) / (SK_R1_sens + SK_R2_sens)
        SK_Q_sens.append(SK_Q)
        Second_poly(W0=SK_W0, Q=SK_Q, Num_Fig=1)
    plt.xscale("log")
    plt.title('VCVS')
    plt.ylabel(r'T($\omega$), дБ')
    plt.xlabel(r'$\omega$, рад/с')
    plt.grid(which='both', axis='both')

    # plot histograms
    Plot_hist('VCVS', Hist_w0=SK_W0_sens, Hist_Q=SK_Q_sens)

    # Plot From Files
    SK_Home = "Files/Filters/Second_order_cell/sallen-key"
    SK_NON_Rout = read_file(f'{SK_Home}/Sallen_Key_Rout.csv', dot=',', Text='')
    R_outs = [0, 10, 100, 500]

    SK_NON_Unity = read_file(f'{SK_Home}/Sallen_Key_Unity_Band.csv', dot=',', Text='')

    plt.figure()
    for i in range(len(SK_NON_Rout[0]) - 1):
        plt.plot(SK_NON_Rout[:, 0], SK_NON_Rout[:, i + 1], label=f'Rout={R_outs[i]}', linewidth='3')
    plt.xlabel('F, Гц')
    plt.title('VCVS')
    plt.xscale('log')
    plt.ylabel('T(F), дБ')
    plt.grid()
    plt.legend()

    plt.figure()
    plt.title('VCVS')
    plt.plot(SK_NON_Unity[:, 0], SK_NON_Unity[:, 1], linewidth='3')
    plt.xlabel('GBP, Гц')
    plt.xscale('log')
    plt.ylabel('Bandwidth, Гц')
    plt.grid()

def MFB(w0, Q, Res, N, Accuracy):
    MFB_R2 = Res
    MFB_R1 = 2 * MFB_R2
    MFB_R3 = 2 * MFB_R2
    MFB_C1 = (4 * Q) / (w0 * MFB_R3)
    MFB_C2 = 1 / (4 * Q * w0 * MFB_R2)

    print('#------MFB------#')
    print(f'C1={MFB_C1}')
    print(f'C2={MFB_C2}')
    print(f'R1={MFB_R1}')
    print(f'R2={MFB_R2}')
    print(f'R3={MFB_R3}')
    print('#----------------#')

    MFB_W0_sens = []
    MFB_Q_sens = []
    for i in range(N):
        # randomization elements
        MFB_R1_sens = random.gauss(MFB_R1, MFB_R1 * Accuracy / 3)
        MFB_R2_sens = random.gauss(MFB_R2, MFB_R2 * Accuracy / 3)
        MFB_R3_sens = random.gauss(MFB_R3, MFB_R3 * Accuracy / 3)
        MFB_C1_sens = random.gauss(MFB_C1, MFB_C1 * Accuracy / 3)
        MFB_C2_sens = random.gauss(MFB_C2, MFB_C2 * Accuracy / 3)

        # calculate W0 and Q
        MFB_W0 = 1 / (np.sqrt(MFB_C1_sens * MFB_C2_sens * MFB_R2_sens * MFB_R3_sens))
        MFB_W0_sens.append(MFB_W0)
        Num = MFB_W0 * MFB_C1_sens * MFB_R1_sens * MFB_R2_sens * MFB_R3_sens
        Den = MFB_R2_sens * MFB_R3_sens + MFB_R1_sens * MFB_R3_sens + MFB_R1_sens * MFB_R2_sens
        MFB_Q = Num / Den
        MFB_Q_sens.append(MFB_Q)
        Second_poly(W0=MFB_W0, Q=MFB_Q, Num_Fig=6)
    plt.xscale("log")
    plt.title('MFB')
    plt.ylabel(r'T($\omega$), дБ')
    plt.xlabel(r'$\omega$, рад/с')
    plt.grid(which='both', axis='both')

    # plot histograms
    Plot_hist('MFB', Hist_w0=MFB_W0_sens, Hist_Q=MFB_Q_sens)

    # Plot From Files
    MFB_Home = "Files/Filters/Second_order_cell/MFB"
    MFB_NON_Rout = read_file(f'{MFB_Home}/MFB_Rout.csv', dot=',', Text='')

    MFB_NON_Unity = read_file(f'{MFB_Home}/MFB_Unity_Band.csv', dot=',', Text='')
    R_outs = [0, 10, 100, 500]

    plt.figure()
    for i in range(len(MFB_NON_Rout[0]) - 1):
        plt.plot(MFB_NON_Rout[:, 0], MFB_NON_Rout[:, i + 1], label=f'Rout={R_outs[i]}', linewidth='3')
    plt.xlabel('F, Гц')
    plt.title('MFB')
    plt.xscale('log')
    plt.ylabel('T(F), дБ')
    plt.grid()
    plt.legend()

    plt.figure()
    plt.title('MFB')
    plt.plot(MFB_NON_Unity[:, 0], MFB_NON_Unity[:, 1], linewidth='3')
    plt.xlabel('GBP, Гц')
    plt.xscale('log')
    plt.ylabel('Bandwidth, Гц')
    plt.grid()

def BQ(w0, Q, Res, N, Accuracy):
    BQ_R2 = Res
    BQ_R1 = Q * BQ_R2
    BQ_R4 = BQ_R2
    BQ_R3 = BQ_R2
    BQ_C1 = 1 / (w0 * BQ_R2)
    BQ_C2 = BQ_C1

    print('#------BQ------#')
    print(f'C1={BQ_C1}')
    print(f'C2={BQ_C2}')
    print(f'R1={BQ_R1}')
    print(f'R2={BQ_R2}')
    print(f'R3={BQ_R3}')
    print(f'R4={BQ_R4}')
    print('#----------------#')

    BQ_W0_sens = []
    BQ_Q_sens = []
    for i in range(N):
        # randomization elements
        BQ_R1_sens = random.gauss(BQ_R1, BQ_R1 * Accuracy / 3)
        BQ_R2_sens = random.gauss(BQ_R2, BQ_R2 * Accuracy / 3)
        BQ_R3_sens = random.gauss(BQ_R3, BQ_R3 * Accuracy / 3)
        BQ_R4_sens = random.gauss(BQ_R4, BQ_R4 * Accuracy / 3)
        BQ_C1_sens = random.gauss(BQ_C1, BQ_C1 * Accuracy / 3)
        BQ_C2_sens = random.gauss(BQ_C2, BQ_C2 * Accuracy / 3)

        # calculate W0 and Q
        BQ_W0 = 1 / (np.sqrt(BQ_C1_sens * BQ_C2_sens * BQ_R2_sens * BQ_R4_sens))
        BQ_W0_sens.append(BQ_W0)
        BQ_Q = BQ_W0 * BQ_R1_sens * BQ_C1_sens
        BQ_Q_sens.append(BQ_Q)
        Second_poly(W0=BQ_W0, Q=BQ_Q, Num_Fig=12)
    plt.xscale("log")
    plt.title('BQ')
    plt.ylabel(r'T($\omega$), дБ')
    plt.xlabel(r'$\omega$, рад/с')
    plt.grid(which='both', axis='both')

    # plot histograms
    Plot_hist('BQ', Hist_w0=BQ_W0_sens, Hist_Q=BQ_Q_sens)

    # Plot From Files
    BQ_Home = "Files/Filters/Second_order_cell/BQ"
    BQ_NON_Rout = read_file(f'{BQ_Home}/BQ_Rout.csv', dot=',', Text='')

    BQ_NON_Unity = read_file(f'{BQ_Home}/BQ_Unity_Band.csv', dot=',', Text='')
    R_outs = [0, 10, 100, 500]

    plt.figure()
    for i in range(len(BQ_NON_Rout[0]) - 1):
        plt.plot(BQ_NON_Rout[:, 0], BQ_NON_Rout[:, i + 1], label=f'Rout={R_outs[i]}', linewidth='3')
    plt.xlabel('F, Гц')
    plt.title('BQ')
    plt.xscale('log')
    plt.ylabel('T(F), дБ')
    plt.grid()
    plt.legend()

    plt.figure()
    plt.title('BQ')
    plt.plot(BQ_NON_Unity[:, 0], BQ_NON_Unity[:, 1], linewidth='3')
    plt.xlabel('GBP, Гц')
    plt.xscale('log')
    plt.ylabel('Bandwidth, Гц')
    plt.grid()


#-----------Global Variable---------#

N=1000
Q=0.707
w0=10e6
Accuracy = 0.2

#---Sallen-Key architecture(VCVS)---#
#VCVS(w0=w0, Q=Q, Res=20e3, Accuracy=Accuracy, N=N)
#---------------end------------------#

#-------Multiple Feedback(VCVS)------#
#MFB(w0=w0, Q=Q, Res=10e3, Accuracy=Accuracy, N=N)
#---------------end------------------#

#----------Biquad Filter-------------#
BQ(w0=w0, Q=Q, Res=20e3, Accuracy=Accuracy, N=N)
#---------------end------------------#








plt.show()

