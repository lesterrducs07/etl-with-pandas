#imports pandas library inyo your IDE and assign pandas alias "AS" pd
#if you havent installed pandas yet into your IDE you can go to any terminal and type
#pip install pandas. wait for it to initialize for about 2mins.

import pandas as pd

#declare variable(xcl) and equal it to pd.read_excel() function in the bracket type your file name(excelfile)
#with its corresponding format(xlsx) . if your file is not in the same folder of your code(etlproject1.py)
#you need to add the directory of the file. ex. C:Users/Username/Desktop/New Folder/excelfile.xlsx
xcl = pd.read_excel("excelfile.xlsx")

x = pd.DataFrame(xcl)
# we upload excelfile to our code, now we need to initialize it again using pd.DataFrame()
# put it inside the () so we can call the DataFrame function.

# this what inside excelfile.xlsx files:

'''
      ID First Name  Last Name  Company ID
0      1    Lindsay     Holden           7
1      2    Anushka     Wilcox           1
2      3    Bernard   Gonzalez          14
3      4       Jody    Bentley           7
4      5    Theresa    Sampson          12
..   ...        ...        ...         ...
495  496     Mikail    Beasley          14
496  497      Diogo    Bradley           4
497  498      Layan     Ashley          19
498  499        Dua   Cisneros           5
499  500    Danyaal  Tomlinson          16

[500 rows x 4 columns]
'''

y = x[['First Name', 'Last Name']]
# so here we declare variable Y to be equal to the x variable and put an index to it, so we can gather
# the specified column in our excelfile. we chose First Name and Last Name column

# so here we will print Y which has the value of x which is excelfile.xlsx which will gather the column
# First Name and Last Name. and then we apply .loc[] function to it so that it will gather all the data
# that is equal to the index of data to our excelfile.xlsx from index 10 to 50 with 2 gaps between indexe
# it will print the values.

# this is the final result of my print
'''
   First Name   Last Name
10      Nigel        Kane
12      Karen     Watkins
14     Kelsie      Pearce
16      Mared  Pennington
18      Rhona       Heath
20     Verity     Simmons
22      Lilly      Mcleod
24        Mac    Christie
26     Gracie   Pemberton
28       Sade       Povey
30       Zaki      Finney
32      Lubna     Vazquez
34      Pippa   Velasquez
36     Caolan       Knott
38     Hallie    Mcarthur
40      Bodhi      Gamble
42     Haidar  Strickland
44     Kishan      Patton
46    Suleman    Delacruz
48     Damien     Ellwood
50    Lincoln     Mueller
'''
print(y.loc[10:50:2])

# and thats how i manipulate transform and sort out file from excelfile.xlsx