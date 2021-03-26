import seaborn as sns
df = sns.load_dataset('tips')
df.head()

#0-1 Conversion
from sklearn.preprocessing import LabelEncoder

lbe = LabelEncoder()

lbe.fit_transform(df["sex"])

df["yeni_sex"] = lbe.fit_transform(df["sex"])



print(df)



#1 and others (0) " conversion
df["day"].str.contains("Sun")

import numpy as np
df["yeni_day"] = np.where(df["day"].str.contains("Sun"), 1, 0)

#Multi-Class Conversion
from sklearn.preprocessing import LabelEncoder
lbe = LabelEncoder()

lbe.fit_transform(df["day"])

#One-Hot transform and Dummy variable trap

import pandas as pd
print(df.head())
df_one_hot = pd.get_dummies(df, columns = ["sex"], prefix = ["sex"])
print(df_one_hot.head())
print(pd.get_dummies(df, columns = ["day"], prefix = ["day"]).head())



