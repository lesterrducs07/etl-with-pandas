import pandas as pd

file1 = pd.read_excel("excelfile.xlsx")
file2 = pd.read_excel("excelfile2.xlsx")

file1_col = file1[['First Name', 'Last Name']]
file2_col = file2[['ID', 'Company ID']]

file1_col.reset_index(drop= True, inplace= True)
file2_col.reset_index(drop= True, inplace= True)

con = pd.concat([file1_col, file2_col], axis=1)

a = pd.DataFrame(con)

print(a)