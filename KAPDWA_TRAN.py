import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'Files/KAPDWA_TRAN'

File_1 = f'{Home}/KAPDWA02_c.csv'
File_2 = f'{Home}/KAPDWA02_c_noL(20p).csv'
File_3 = f'{Home}/KAPDWA02_c_noL(100p).csv'
File_4 = f'{Home}/KAPDWA02_c_noL(1n).csv'
File_5 = f'{Home}/KAPDWA02_c_noL(10n).csv'
File_LDO_Ro = f'{Home}/LDO_OUT_RES.csv'
File_LDO_RoL = f'{Home}/LDO_OUT_RES(L).csv'

Value_1=read_file(File_1, dot = ',', Text = '')
Value_2=read_file(File_2, dot = ',', Text = '')
Value_3=read_file(File_3, dot = ',', Text = '')
Value_4=read_file(File_4, dot = ',', Text = '')
Value_5=read_file(File_5, dot = ',', Text = '')
LDO_Ro = read_file(File_LDO_Ro, dot = ',', Text = '')
LDO_RoL = read_file(File_LDO_RoL, dot = ',', Text = '')
List = ['PADC_CLK','VDD12_DIG', 'VDD12_PLL','VDD33_DIG', 'VDD33_PLL']
List_Cap = ['0p','20p', '100p', '1n', '10n']
List_L = ['1n', '2n', '3n']
n=1


plt.figure()
plt.title(List[n])
plt.plot(Value_1[:, n*2], Value_1[:, n*2+1], label='L=1нГн,С=10нФ', linewidth ='2')
plt.plot(Value_2[:, n*2], Value_2[:, n*2+1], label='L=0нГн,С=20пФ', linewidth ='2')
plt.plot(Value_3[:, n*2], Value_3[:, n*2+1], label='L=0нГн,С=100пФ', linewidth ='2')
plt.plot(Value_4[:, n*2], Value_4[:, n*2+1], label='L=0нГн,С=1нФ', linewidth ='2')
plt.plot(Value_5[:, n*2], Value_5[:, n*2+1], label='L=0нГн,С=10нФ', linewidth ='2')
plt.plot(Value_5[:, 0*2], Value_5[:, 0*2+1], label='PAD_CLK', linewidth ='2')
plt.xlabel('t, c')
plt.ylabel('U, В')
plt.legend()
plt.grid()

plt.figure()
plt.title('LDO OUT RES')
for i in range(len(List_Cap)):
    plt.plot(LDO_Ro[:, 0], LDO_Ro[:, i+1], label=f'C={List_Cap[i]}', linewidth ='2')
plt.xlabel('f, Гц')
plt.ylabel('R, Ом')
plt.xscale('log')
plt.legend()
plt.grid()

plt.figure()
plt.title('LDO OUT RES')
for i in range(len(List_L)):
    plt.plot(LDO_RoL[:, 0], LDO_RoL[:, i+1], label=f'L={List_L[i]}', linewidth ='2')
plt.xlabel('f, Гц')
plt.ylabel('R, Ом')
plt.xscale('log')
plt.legend()
plt.grid()

File_LDO_L = f'{Home}/KAPDWA02_LDO_OUT.csv'
File_LDO_noL = f'{Home}/KAPDWA02_LDO_OUT_noL.csv'
LDO = read_file(File_LDO_L, dot = ',', Text = '')
LDO_noL = read_file(File_LDO_noL, dot = ',', Text = '')

LDO_List = ['ID_LDO', 'LDO_PAD', 'VDD12_DIG']
LDO_noL_List = ['VSS_DIG', 'ID_LDO', 'PADC_CLK', 'VDD12_DIG']

plt.figure()
plt.plot(LDO[:, 4], LDO[:, 5], label=f'VDD12_DIG', linewidth ='2')
plt.plot(LDO[:, 2], LDO[:, 3], label=f'LDO_PAD', linewidth ='2')
plt.legend()
plt.xlabel('t,c')
plt.ylabel('U, В')
plt.grid()

plt.figure()
plt.plot(LDO[:, 0], LDO[:, 1]*1e3, label=f'ID_LDO', linewidth ='2')
plt.legend()
plt.xlabel('t,c')
plt.ylabel('I, мА')
plt.grid()

plt.figure()
plt.plot(LDO_noL[:, 0], -LDO_noL[:, 1]*1e3, label=f'ID_DIG', linewidth ='2')
plt.plot(LDO_noL[:, 2], LDO_noL[:, 3]*1e3, label=f'ID_LDO', linewidth ='2')
plt.legend()
plt.xlabel('t,c')
plt.ylabel('I, мА')
plt.grid()



plt.show()