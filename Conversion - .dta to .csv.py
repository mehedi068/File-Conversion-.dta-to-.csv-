import pandas as pd
import os
import numpy as np
import tqdm
arr = 'Data/'
print(arr)

for dir,_, files in os.walk(arr):
    print(len(files))
    length = len(files)
    for i in range(length):
        arr = arr +"\\"+ files[i]
        temp = np.array(files[i].split('.dta'))
        data = pd.io.stata.read_stata("/home/mehedi/Documents/HIES/Data/"+files[i], convert_categoricals=False, convert_missing=True)
        data.to_csv(temp[0]+'.csv')
