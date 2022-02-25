import numpy as np
from openpyxl import Workbook, load_workbook

wb = load_workbook(filename=f"Files/Exel_reverse/SILICAT_SUB_BALLS_fin.xlsx")
sh = wb['Лист1']

list = ['A', 'B', 'C', 'D', 'E', 'F']

massive = np.array()
print(sh[f'{list[1]}2'].value)

for col in range(len(list)):
    for ro in range(10):
        massive[ro][col] = sh[f'{list[col]}'+f'{ro+1}'].value

print(massive)











