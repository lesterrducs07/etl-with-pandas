import pandas as pd
import numpy as np

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
pd.set_option('display.max_columns', None)  # Show all columns
colhead = ['NAMES', 'JERSEY NO.', 'COLLEGE']
lateams = pd.DataFrame([lac, lal,],columns=colhead)

print(lateams)