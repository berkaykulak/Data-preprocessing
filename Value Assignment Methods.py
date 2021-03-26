import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V2 = np.array([7,np.NaN,5,8,12,np.NaN,np.NaN,2,3])
V3 = np.array([np.NaN,12,5,6,14,7,np.NaN,2,31])

df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3}
)



print(df)
df["V1"].fillna(0)
print(df)
df["V1"].fillna(df["V1"].mean())
print(df)

df.apply(lambda x: x.fillna(x.mean()), axis = 0)
df.fillna(df.mean()[:])
print(df)
df.fillna(df.mean()["V1":"V2"])
print(df)
print(df["V3"].fillna(df["V3"].median()))
df.where(pd.notna(df), df.mean(), axis = "columns")