import numpy as np
import pandas as pd
V1 = np.array([1,3,6,np.NaN,7,1,np.NaN,9,15])
V4 = np.array(["IT",np.nan,"IK","IK","IK","IK","IK","IT","IT"], dtype=object)

df = pd.DataFrame(
        {"maas" : V1,
        "departman" : V4}
)

print(df)

print(df["departman"].mode()[0])
print(df["departman"].fillna(df["departman"].mode()[0]))
print(df)
print(df["departman"].fillna(method = "bfill"))
print(df["departman"].fillna(method = "ffill"))
print()
print()