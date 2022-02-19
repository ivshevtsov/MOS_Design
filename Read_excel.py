from openpyxl import load_workbook

#directory
HOME = 'C:/Users/ELECTRONIC/Desktop'

#file name
File = 'test'

#load document
wb = load_workbook(f'{HOME}/{File}.xlsx')

#number of sheet
N_sheet = 1

#number rows and colums
n_rows = 5
n_columns = 5

#separator
sep = ' - '

##------------------------------------------------##
##------------------------------------------------##

#get sheet names
sheetnames = wb.sheetnames
#get sheet data
sheet = wb[sheetnames[N_sheet-1]]

with open(f'{HOME}/{File}.txt', "w") as file:
    for row in range(2, n_rows+1):
        for column in range(2, n_columns+1):
            row_x = sheet.cell(row=row, column=1).value
            column_x = sheet.cell(row=1, column=column).value
            Value = sheet.cell(row=row, column=column).value
            String = f'{row_x}'+f'{column_x}'+ f'{sep}'  f'{Value}'
            #print(String)
            file.write(f'{String} \n')
    file.close()