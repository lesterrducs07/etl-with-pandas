import pandas as pd
import numpy as np

#so i just imported 2 libraries pandas and numpy
lac = [
    ['westbrook','harden', 'george', 'leonard'],
    [0, 1, 13, 2],
    ['ucla', 'sandiego', 'fresno state', 'SDC']
]

lal = [
    ['james', 'davis', 'reaves', 'd.russel'],
    [23, 5, 21, 1],
    ['st vincent', 'kentucky', 'oklahoma', 'louisville']
]
# i added to list of arrays(lac and lal), this is 2d array becos is a list inside a list

pd.set_option('display.max_columns', None)
# i added pd.set_option function to be able to display all the arrays on the print.
#inside set_option() i pass display.max_columns', and then None

colhead = ['NAMES', 'JERSEY NO.', 'COLLEGE']
# i added 3 column header to be on top of my list(NAME, JERSEY NO., AND COLLEGE)

lateams = pd.DataFrame([lac, lal,],columns=colhead)
# i initialize lateams to be my variable for the two list of array
# i use pd.DataFrame so i can make them in tabular.
# and then i pass 2 parameter to  pd.DataFrame function (lac, and lal) and then i set the column to be (colhead)

print(lateams)
#so when i print the lateams dataframe it combines the 2 list of array inside 1 dataframe

#heres the result of the print(lateams)
#p.s i did not use the numpy lib

                                  NAMES      JERSEY NO.                                       COLLEGE
0  [westbrook, harden, george, leonard]   [0, 1, 13, 2]           [ucla, sandiego, fresno state, SDC] 
1      [james, davis, reaves, d.russel]  [23, 5, 21, 1]  [st vincent, kentucky, oklahoma, louisville]

                                         

