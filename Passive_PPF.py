import control
import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"
plt.rcParams['lines.linewidth'] = 3

#Read from file
Home = 'C:/Users\SH\PycharmProjects\MOS_Design\Files\Filters\Passive_PPF'
File = f"{Home}/Three_stage_passive_PPF.csv"
File_1 = f"{Home}/Three_stage_passive_PPF_woL.csv"
Value_1=read_file(File, dot = ',', Text = '')
Value_2=read_file(File_1, dot = ',', Text = '')


def First_PPF(freq, fp, Positive_r = True):
    s = control.tf('s')
    if Positive_r:
        G = (1 + 1j * s / fp) / (1 + s / fp)
    else:
        G = (1 - 1j * s / fp) / (1 + s / fp)
    mag, ph, w = control.bode(G, plot=False, color='Tab:red', omega=freq, Hz=True)
    return mag, w

def First_PPF_IRR(freq, fp, Positive_r = True):
    s = control.tf('s')
    GP = (1 + 1j * s / fp) / (1 + s / fp)
    GN = (1 - 1j * s / fp) / (1 + s / fp)
    if Positive_r:
        IRR = GP/GN
        mag, ph, w = control.bode(IRR, plot=False, color='Tab:red', omega=freq, Hz=True)
    else:
        IRR = GN / GP
        mag, ph, w = control.bode(IRR, plot=False, color='Tab:red', omega=freq, Hz=True)
    return mag,  w

def Calculate_RC(R, fp, Title):
    C = 1/(2*np.pi*R*fp)
    print(f'#----{Title}----#')
    print(f'R = {R} Ом')
    print(f'C = {C} Ф')
    print(f'Fc = {fp} Гц')
    print('#---------------#')


fp = 6e6 #First pole
k=2 #Frequency scale factor
Max_F = 40e6 #Max F for plot
Value = False #Positive(True)/Negative rejection(False)
R=5000 #Value for resistors

freq = np.linspace(-Max_F, Max_F, 500)
if Value:
    freq_IRR = np.linspace(0, Max_F, 500)
else:
    freq_IRR = np.linspace(-Max_F, 0, 500)

#Calculate RC
Calculate_RC(R=R, fp=fp, Title='First stage')
Calculate_RC(R=R, fp=fp*k, Title='Second stage')
Calculate_RC(R=R, fp=fp*k**2, Title='Third stage')


#H(s) stages
First, w =  First_PPF(freq, fp, Positive_r = Value)
Second, _ = First_PPF(freq, fp*k, Positive_r = Value)
Third, _ =  First_PPF(freq, fp*k**2, Positive_r = Value)

#IRR(s) stages
First_IRR, w_IRR = First_PPF_IRR(freq_IRR, fp, Positive_r = Value)
Second_IRR, _ =    First_PPF_IRR(freq_IRR, fp*k, Positive_r = Value)
Third_IRR, _ =     First_PPF_IRR(freq_IRR, fp*k**2, Positive_r = Value)


#Cascade
FULL = First*Second*Third
FULL_IRR = First_IRR*Second_IRR*Third_IRR


#Plot H(f)
plt.figure()
#plt.plot(w, 20*np.log10(First),  linewidth='3', label='Ideal' )
#plt.plot(w_IRR, 20*np.log10(First_IRR),  linewidth='3', label='IRR')
plt.plot(w, 20*np.log10(FULL),  linewidth='3', label='Ideal')
plt.plot(w_IRR, 20*np.log10(FULL_IRR),  linewidth='3', label='IRR')
#plt.plot(Value_2[:, 0], Value_2[:, 1], '--', label='Simulated', linewidth ='3')
plt.xlabel('f, Гц')
plt.ylabel('T(f), дБ')
plt.legend()
plt.grid(which='both', axis='both')

plt.show()