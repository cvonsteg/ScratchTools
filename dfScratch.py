import pandas as pd
import numpy as np


#Dimension Variable
n = 10

#letters and NaN columns
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
choice2 = pd.Series(['x', 'y', np.nan])

# Arbitrary DataFrame
df = pd.DataFrame({'A': range(1, n+1, 1),
                   'B': np.random.randint(1, 1000, size = n),
                   'C': np.random.choice(np.array(letters, dtype = "|S1"), n),
                   'D': np.random.choice(choice2, n)})


df2 = pd.DataFrame({'A': {0:, 1:, 2:, 3:, 4:, 5:},
                    'B': {0: ,1: ,2: ,3: ,4: ,5:},
                    'C': {0: ,1: ,2: ,3: ,4: ,5:},
                    'D': {0: 'first', 1: 'second', 2: 'third', 3: 'fourth', 4: 'fifth', 5: 'sixth'}})