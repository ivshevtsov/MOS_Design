import numpy as np
import matplotlib.pyplot as plt
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3

def Lambda_example(L, VDD, figure):
    Na = 10e25
    Veff = 0.25
    Ks = 11.8
    e0=8.854e-12
    q=1.6e-19
    F0=0.9
    Kds = (2*Ks*e0/(q*Na))**0.5
    Idsat = 25e-6
    lamb=[]
    rout= []
    VDS = np.linspace(0, VDD, 100)
    for i in VDS:
        x=Kds/(2*L*(i-Veff+F0)**0.5)
        lamb.append(x)
        rout.append(1/(x*Idsat))
    #plot lambda
    plt.figure(figure)
    plt.plot(VDS, lamb)
    plt.xlabel(r'$V_{DS}$')
    plt.ylabel(r'$\lambda$')
    plt.grid()
    #plot Rout
    plt.figure(figure+1)
    plt.plot(VDS, rout)
    plt.xlabel(r'$V_{DS}$')
    plt.ylabel(r'$r_{OUT}$')
    plt.grid()


def Cascode_rout(gm_casc, gds_casc, gs_casc, gds):
    r_out = (1/gds_casc)*(1+(1/gds)*(gm_casc+gs_casc+gds_casc))
    print(r_out)


Cascode_rout(gm_casc=823.6e-6, gds_casc=10.72e-6, gs_casc=220e-6, gds=41.52e-6)

#Lambda_example(500e-9, 3.3, 1)

Home = 'Files/PPF/current_mirrors'
File_DC = f'{Home}/cascode2_current_mirror_dc.csv'
File_AC = f'{Home}/cascode2_current_mirror_ac.csv'
DC=read_file(File_DC, dot = ',', Text = '')
AC=read_file(File_AC, dot = ',', Text = '')

#low Veff current mirror
File_Compare = f'{Home}/cascode_current_mirror_minVeff.csv'
Compare=read_file(File_Compare, dot = ',', Text = '')

plt.figure()
plt.plot(DC[:, 0], DC[:, 1] *1e6 , linewidth ='3')
plt.xlabel(r'$V_{DS}$, В')
plt.ylabel(r'$I_{D}$, мкA')
#plt.xscale('log')
plt.grid()

plt.figure()
plt.plot(AC[:, 0], AC[:, 1]/1e6, linewidth ='3')
plt.xlabel(r'F, Гц')
plt.ylabel(r'$r_{OUT}$, МОм')
plt.xscale('log')
plt.grid()

plt.figure()
plt.title(r'$V_{MIN}$=0.5В')
plt.plot(Compare[:, 0], Compare[:, 1]/1e3, label='Simple',  linewidth ='3')
plt.plot(Compare[:, 0], Compare[:, 2]/1e3, label='Cascode', linewidth ='3')
plt.xlabel(r'F, Гц')
plt.ylabel(r'$r_{OUT}$, кОм')
plt.xscale('log')
plt.legend()
plt.grid()

plt.show()
