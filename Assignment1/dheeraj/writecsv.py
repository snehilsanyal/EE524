import pandas as pd
import numpy as np
import random
df = pd.DataFrame(np.random.randint(0,100,size=(10, 10)), columns=list('ABCDEFGHIJ'))

df.to_csv('my_first_csv.csv')


print(df)
