import matplotlib.pyplot as plt
from Functions import read_file
import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

Home = 'C:/Users\SH\PycharmProjects\MOS_Design\Files\Filters\Passive_PPF\Passive_Gen'
Type = '2'
File_A = f"{Home}/PPF3_Gen_Amp_Type{Type}.csv"
File_P = f"{Home}/PPF3_Gen_Phase_Type{Type}.csv"
List = ['I+', 'Q+', 'I-', 'Q-']


Type_A=read_file(File_A, dot = ',', Text = '')
Type_P=read_file(File_P, dot = ',', Text = '')


plt.figure()
plt.title(f'Type {Type}')
for i in range(len(Type_A[0])-1):
    plt.plot(Type_A[:, 0], Type_A[:, i+1], label=List[i], linewidth ='3')
plt.grid()
plt.legend()
plt.xlabel('f, Гц')
plt.ylabel('Amp, дБ')

plt.figure()
plt.title(f'Type {Type}')
for i in range(len(Type_P[0])-1):
    plt.plot(Type_P[:, 0], Type_P[:, i+1], label=List[i], linewidth ='3')
plt.grid()
plt.legend()
plt.xlabel('f, Гц')
plt.ylabel('Phase, град.')

#Error Phase
plt.figure()
plt.title(f'Type {Type}')
Error_P = abs(Type_P[:, 1]-Type_P[:, 2])-90
plt.plot(Type_P[:, 0], Error_P, linewidth ='3')
plt.grid()
plt.xlabel('f, Гц')
plt.ylabel('Phase error, град.')

#Error Amp
plt.figure()
plt.title(f'Type {Type}')
Error_P = Type_A[:, 1]-Type_A[:, 2]
plt.plot(Type_P[:, 0], Error_P, linewidth ='3')
plt.grid()
plt.xlabel('f, Гц')
plt.ylabel('Amp error, дБ')


dx = 0.001; dy = 0.001
x = np.arange(0.1,0.8,dx)
y = np.arange(0,4,dy)
X,Y = np.meshgrid(x,y)

def f(x,y):
    dA = 10**(x/20)-1
    dFi = y*np.pi/180
    Num = 1-(1+dA)*np.exp(-1j*dFi)
    Den = 1+(1+dA)*np.exp(-1j*dFi)
    return 20*np.log10(abs(Num/Den))
plt.figure()
C = plt.contour(X,Y,f(X,Y),12, colors='black')
plt.contourf(X,Y,f(X,Y),12, cmap=plt.cm.summer)
plt.clabel(C, inline=0.5, fontsize=14)
plt.xlabel('Gain, дБ')
plt.ylabel('Phase, град.')
plt.show()









plt.show()