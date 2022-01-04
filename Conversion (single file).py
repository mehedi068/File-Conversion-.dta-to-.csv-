import pandas as pd
import os
arr = os.listdir('Data/')
print(arr)
data = pd.io.stata.read_stata('Data/COVER.dta')
data.to_csv('COVER.csv')
