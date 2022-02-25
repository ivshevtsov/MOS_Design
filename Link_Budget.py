import docx
import matplotlib.pyplot as plt
import numpy as np
from Functions import read_file
import docx

def Cascaded_noise(Noise, Gain):
    result=[]
    x=[1]
    result.append(Noise[0])
    Gain_Cascaded = 1
    NF_Cascaded = 10 ** (NF_dB_GPS[0] / 10)
    for i in range(len(Noise) - 1):
        Gain_Cascaded = Gain_Cascaded * (10 ** (Gain[i] / 10))
        NF_block = 10 ** (Noise[i + 1] / 10)
        NF_Cascaded = NF_Cascaded + (NF_block - 1) / Gain_Cascaded
        result.append(10*np.log10(NF_Cascaded))
        x.append(i+2)
    return x, result

def Cascaded_gain(Gain):
    result=[]
    x=[]
    Gain_sum=0
    for i in range(len(Gain)):
        Gain_sum = Gain_sum +Gain[i]
        result.append(Gain_sum)
        x.append(i+1)
    return x, result

def Cascaded_P1dB(Gain, P1db):
    result = []
    x=[1]
    result.append(P1db[0])
    P1db_sum = 1/(10**(P1db[0]/10))
    Cascaded_gain=1
    for i in range(len(P1db)-1):
        Cascaded_gain=Cascaded_gain*(10**(Gain[i]/10))
        P1db_sum = P1db_sum +  Cascaded_gain/(10**(P1db[i+1]/10))
        result.append(10*np.log10(1/P1db_sum))
        x.append(i+2)
    return x, result

def Cascaded_signals(Band,Gain,Noise, Signal_level):
    k = 1.38e-23
    T = 290
    _ , Gain_C = Cascaded_gain(Gain)
    _ , NF_C = Cascaded_noise(Noise, Gain)
    Noise_L = [10*np.log10(k*T*1000)+10*np.log10(Band[0])]
    Signal_L = [Signal_level]
    SNR = [Signal_L[0]-Noise_L[0]]
    for i in range(len(Band)):
        X = 10*np.log10(k*T*1000)+10*np.log10(Band[i])+NF_C[i]+ Gain_C[i]
        Noise_L.append(X)
        Signal_L.append(Signal_level + Gain_C[i])
        SNR.append(Signal_L[i+1]-Noise_L[i+1])
    return Signal_L , Noise_L, SNR

def Plot_with_dots(x, y, Legend, XLabel, YLabel, N_Fig):
    plt.figure(N_Fig)
    plt.plot(x, y, linewidth='3')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'o', label=f'{i + 1}.{Legend[i]}')
    plt.ylabel(YLabel)
    plt.xlabel(XLabel)
    plt.legend()
    plt.grid()

def Sensetivity(Band, NF, SNR_MIN, IRR, PN, SNR_ADC):
    k = 1.38e-23
    T = 290
    SNR_IRR = -10*np.log10(1/(1+1/(10**(IRR/10))))
    SNR_PN = -10*np.log10(1/(1+10**((PN+10*np.log10(Band))/10)))
    Sens = 10*np.log10(k*T*1000)+ 10*np.log10(Band)+NF+ SNR_MIN +SNR_IRR + SNR_PN+SNR_ADC
    print(f'IRR={SNR_IRR}')
    print(f'PN={SNR_PN}')
    print(f'Sens={Sens}')
    return Sens

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"


Band_RF=50e6
Band_GPS = 4.8e6
Band_GLO = 9.5e6
ADC_FS = -8-1.75
k=1.38e-23
T=290

##--------------##
LNA_0_G =20.5
LNA_0_NF=1.88
LNA_0_P1db = -27
##--------------##
SAW_G=0
SAW_NF=0
SAW_P1db = 100
##--------------##
LNA_1_G=24
LNA_1_NF=17.8
LNA_1_P1db =-20
##--------------##
MIX_G=20
MIX_NF = 17
MIX_P1db = -20
##--------------##
PPF_G = 19
PPF_NF = 41
PPF_P1db = -20
##--------------##

Max_Gain_VGA = 42.5
NF_Min_VGA = 33
P1db_min_VGA = -34.5
##--------------##

#-----------------------------------------------------
Signal_GPS = 10*np.log10(k*T*1000)+10*np.log10(Band_GPS)
Signal_GLO = 10*np.log10(k*T*1000)+10*np.log10(Band_GLO)
##------------Require gain---------##
Gain_GPS = ADC_FS-Signal_GPS
Gain_GLO = ADC_FS-Signal_GLO
print(Gain_GPS)
##---------------------------------##

VGA_GPS_G = Gain_GPS-(LNA_0_G+SAW_G+LNA_1_G+MIX_G+PPF_G)
VGA_GPS_NF = NF_Min_VGA - VGA_GPS_G + Max_Gain_VGA
VGA_GPS_P1db = P1db_min_VGA-VGA_GPS_G+Max_Gain_VGA

if VGA_GPS_G>Max_Gain_VGA or VGA_GPS_G<-10:
    print('VGA out of range')
##--------------##
VGA_GLO_G = Gain_GLO-(LNA_0_G+SAW_G+LNA_1_G+MIX_G+PPF_G)
VGA_GLO_NF = NF_Min_VGA - VGA_GLO_G + Max_Gain_VGA
VGA_GLO_P1db = P1db_min_VGA-VGA_GLO_G+Max_Gain_VGA
##--------------##
##----Receiver Gain-----##
Gain_dB_GPS = [LNA_0_G, SAW_G, LNA_1_G, MIX_G, PPF_G, VGA_GPS_G]
Gain_dB_GLO = [LNA_0_G, SAW_G, LNA_1_G, MIX_G, PPF_G, VGA_GLO_G]

##----Receiver Noise-----##
NF_dB_GPS = [LNA_0_NF, SAW_NF, LNA_1_NF, MIX_NF, PPF_NF, VGA_GPS_NF]
NF_dB_GLO = [LNA_0_NF, SAW_NF, LNA_1_NF, MIX_NF, PPF_NF, VGA_GLO_NF]

##----Receiver P1dB-----##
P1dB_GPS = [LNA_0_P1db, SAW_P1db, LNA_1_P1db, MIX_P1db, PPF_P1db, VGA_GPS_P1db]
P1dB_GLO = [LNA_0_P1db, SAW_P1db, LNA_1_P1db, MIX_P1db, PPF_P1db, VGA_GLO_P1db]

##----Receiver Bands-----##
Band_GPS_BLOCKS = [Band_RF, Band_RF, Band_RF, Band_RF, Band_GPS, Band_GPS]
Band_GLO_BLOCKS = [Band_RF, Band_RF, Band_RF, Band_RF, Band_GLO, Band_GLO]

##----Receiver Legend-----##
Legend = ['МШУ', 'SAW', 'МШУ', 'Смеситель', 'PPF', 'VGA']

###Results###
GPS=1

if GPS==1:
    Gain_dB= Gain_dB_GPS
    NF_dB = NF_dB_GPS
    P1dB = P1dB_GPS
    Band_BLOCKS=Band_GPS_BLOCKS
else:
    Gain_dB= Gain_dB_GLO
    NF_dB = NF_dB_GLO
    P1dB = P1dB_GLO
    Band_BLOCKS = Band_GLO_BLOCKS




x_1, y_1 = Cascaded_noise(NF_dB, Gain_dB)
Plot_with_dots(x_1, y_1, Legend=Legend, XLabel='N', YLabel='NF, дБ', N_Fig=1)

x_2, y_2=Cascaded_gain(Gain_dB)
Plot_with_dots(x_2, y_2, Legend=Legend, XLabel='N', YLabel='Gain, дБ', N_Fig=2)

x_3, y_3 = Cascaded_P1dB(Gain_dB, P1dB)
Plot_with_dots(x_3, y_3, Legend=Legend, XLabel='N', YLabel='P1dB(IN), дБм', N_Fig=3)

Sens=Sensetivity(Band=Band_BLOCKS[-1], NF=y_1[-1], SNR_MIN=-44, IRR=30, PN=-80, SNR_ADC=0.7)
SIG, Noise, SNR = Cascaded_signals(Band_BLOCKS,Gain_dB,NF_dB, Sens)


##Write to word##
Table_Title = ['Блок', 'Pout(Noise), дБм', 'Pout(Sig), дБм','SNR, дБ','P1db(IN), дБм','NF, дБ', 'Усиление, дБ']

doc = docx.Document()
table = doc.add_table(rows=len(x_1)+2, cols=len(Table_Title))
#Title

for k in range(len(x_1)+2):
    if k==0:
        row = table.rows[k].cells
        for i in range(len(Table_Title)):
            row[i].text = Table_Title[i]
    elif k==1:
        row = table.rows[k].cells
        row[1].text = str(round(Noise[0],2))
        row[2].text = str(round(SIG[0],2))
        row[3].text = str(round(SNR[0],2))
    else:
        row = table.rows[k].cells
        row[0].text = Legend[k-2]
        row[1].text = str(round(Noise[k-1],2))
        row[2].text = str(round(SIG[k-1],2))
        row[3].text = str(round(SNR[k - 1],2))
        row[4].text = str(round(P1dB[k - 2],2))
        row[5].text = str(round(NF_dB[k - 2],2))
        row[6].text = str(round(Gain_dB[k - 2], 2))

doc.save('Files/Budget/Test.docx')



plt.show()