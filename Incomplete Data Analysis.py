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

print(df.isnull().sum())
print(df.notnull().sum())
print(df.isnull().sum().sum())
print(df.isnull())
print(df[df.isnull().any(axis = 1)])
print(df[df.notnull().all(axis = 1)])



print(df[df["V1"].notnull() & df["V2"].notnull()& df["V3"].notnull()])
print(df.dropna())


print(df)
print(df["V1"])
print(df["V1"].mean())


print(df["V1"].fillna(df["V1"].mean()))
print(df["V2"].fillna(0))
print(df.apply(lambda x: x.fillna(x.mean()), axis = 0))
