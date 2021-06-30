import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

comment = ["#", ";"]
dot = ","
File = "Files/S21_Attenuator_10db_ff_ss_tt.vcsv"

num_colums = 0
num_strings =  0
#Size of massive
with open(File) as Read:
    for line in Read:
        string  = line
        if  string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
            num_colums = len(line.split(","))
            mas = line.split(dot)
            num_strings = num_strings+1

mas = []
Value_1 = np.zeros((num_strings, num_colums))
i=0

#Write massive
with open(File) as Read:
    for line in Read:
        string  = line
        if  string[0] != comment[0] and string[0] != comment[1] and string[0].isalpha() != True:
            mas = line.split(dot)
            for k in range(num_colums):
                Value_1[i, k] = float(mas[k])
            i=i+1

print(num_colums)
plt.figure()

plt.plot(Value_1[:, 0], Value_1[:, 1], label='FF', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 3], label='SS', linewidth ='3')
plt.plot(Value_1[:, 0], Value_1[:, 5], label='TT', linewidth ='3')
plt.xlabel('F, Гц')
plt.ylabel('S21, dB')
plt.grid()
plt.legend()
plt.show()