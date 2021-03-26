import missingno as msno

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}
)

print(df)
df.dropna()
print(df)
df.dropna(how = "all")
df.dropna(axis = 1)
print(df)
df.dropna(axis = 1, how = "all")
print(df)
df["sil_beni"] = np.nan
print(df)
df.dropna(axis = 1, how = "all")
print(df)
