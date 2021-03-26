import numpy as np
import pandas as pd
from sklearn import preprocessing
V1 = np.array([1,3,6,5,7])
V2 = np.array([7,7,5,8,12])
V3 = np.array([6,12,5,6,14])
df = pd.DataFrame(
        {"V1" : V1,
         "V2" : V2,
         "V3" : V3})

df = df.astype(float)

print(df)

#Standardizasyon
preprocessing.scale(df)
print(df)

# Normalizasyon

preprocessing.normalize(df)

#Min-Max Dönüşümü¶
scaler = preprocessing.MinMaxScaler(feature_range = (100,200))
scaler.fit_transform(df)
