import matplotlib.pyplot as plt
from Functions import plot_two_y
from Functions import poly_from_file
from Functions import poly_db
from Functions import poly_deg

plt.rcParams["font.family"] = "Century Gothic"
plt.rcParams["font.size"] = "14"

File_poles = "Files/SE_OPA_PZ/SE_OP_poles.csv"
File_zeros = "Files/SE_OPA_PZ/SE_OP_zeros.csv"


Polinom = poly_from_file(File_poles, File_zeros, 1, 1e10, 1000)
Polinom_db = poly_db(Polinom)
Polinom_deg = poly_deg(Polinom)

plot_two_y(Polinom_db[:, 0], First=Polinom_db[:,1], Second=Polinom_deg[:, 1],
           label_first='H(f), дБ', label_second='Фаза, град.', xlabel='F, Гц')
plt.show()




