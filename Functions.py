import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import log10
from cmath import phase

#calculate number strings and colums
#return mas[string, colums]
def n_string_colums(File, dot = ','):
    comment = ["#", ";"]
    num_colums = 0
    num_strings = 0
    # Size of massive
    with open(File) as Read:
        for line in Read:
            string = line
            if string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
                num_colums = len(line.split(","))
                num_strings = num_strings + 1
    string_colum = [num_strings, num_colums]
    return string_colum

#read random file from simulation
#return mas[i,j]
def read_file(File, dot = ',', Text = ''):
    comment = ["#", ";"]
    Size = n_string_colums(File)
    mas = []
    Value_1 = np.zeros((Size[0], Size[1]))
    i=0

    #Write massive
    with open(File) as Read:
        for line in Read:
            string  = line
            if  string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
                mas = line.split(dot)
                for k in range(Size[1]):
                    Value_1[i, k] = float(mas[k])
                i=i+1
    print(f'Число столбцов {Text}= {Size[1]}')
    print(f'Число строк {Text}= {Size[0]}')
    return Value_1


#plot with two y labels
def plot_two_y(F, First, Second, label_first, label_second, xlabel):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    #axis one
    color = 'tab:red'
    ax1.plot(F, First, color = color, linewidth=3)
    ax1.set_ylabel(label_first, color = color)
    ax1.set_xlabel(xlabel)
    ax1.grid()
    #axis two
    color ='tab:blue'
    ax2.plot(F, Second, color=color, linewidth=3)
    ax2.set_ylabel(label_second, color=color)
    plt.xscale('log')

#calculate stepen of ten
def stepen(k):
    i = 0
    if k >= 10:
        while k > 1:
            k = k / 10
            i = i + 1
    else:
        i = 0.1
    return i

#Calculate polinom for plot
def poly_from_file(File_poles, File_zeros, from_x, to_x, N_point):

    #Poles and zeros files
    Poles = read_file(File_poles, Text='Poles')
    Size_File_pole = n_string_colums(File_poles)
    Zeros = read_file(File_zeros, Text='Zeros')
    Size_File_zero = n_string_colums(File_zeros)

    F = np.logspace(stepen(from_x), stepen(to_x), N_point, endpoint=True)
    POLINOM = np.zeros([len(F), 2], complex)

    for i in range(len(F)):

        # Poles
        Denominator = 1
        for string in range(Size_File_pole[0]):
            sigma_p = -(Poles[string, 1] / (2 * Poles[string, 0]))
            omega_p = sqrt(pow(Poles[string, 1], 2) - pow(sigma_p, 2))
            c_Pole = complex(sigma_p, omega_p)
            Denominator = Denominator * (1 - complex(0, F[i]) / c_Pole)

        # Zeros
        Numerator = 1
        counter = 0
        for string in range(Size_File_zero[0]):
            counter = counter + 1
            if Zeros[string, 0] == 0.5 or Zeros[string, 0] == -0.5:
                sigma_z = -(Zeros[string, 1] / (2 * Zeros[string, 0]))
                omega_z = sqrt(pow(Zeros[string, 1], 2) - pow(sigma_z, 2))
                c_Zero = complex(sigma_z, omega_z)
            else:
                k = pow(-1, counter)
                sigma_z = -(Zeros[string, 1] / (2 * abs(Zeros[string, 0])))
                omega_z = sqrt(pow(Zeros[string, 1], 2) - pow(sigma_z, 2))
                c_Zero = complex(sigma_z, omega_z * k)
            Numerator = Numerator * (1 - complex(0, F[i]) / c_Zero)

        # Poly
        POLINOM[i, 1] = Numerator / Denominator
        POLINOM[i, 0] = F[i]

    return POLINOM

#calculate db values of polynom
def poly_db(Massive):
    Polinom_db = np.zeros([len(Massive), 2], float)

    for i in range(len(Massive)):
        #db Value
        Polinom_db[i, 1] = 20 * log10(abs(Massive[i, 1]))
        #Frequency
        Polinom_db[i, 0] = Massive[i, 0].real
    return Polinom_db

#calculate deg Values of polynom
def poly_deg(Massive):
    Polinom_phase = np.zeros([len(Massive), 2], float)
    flag_phase = 0
    for i in range(len(Massive)):
        # Phase
        if flag_phase == 0:
            Polinom_phase[i, 1] = phase(Massive[i, 1]) * 180 / 3.14
        else:
            Polinom_phase[i, 1] = phase(Massive[i, 1]) * 180 / 3.14 - 360
        if Polinom_phase[i, 1] <= -179:
            flag_phase = 1
    # Frequency
    Polinom_phase[i, 0] = Massive[i, 0].real

    return Polinom_phase
