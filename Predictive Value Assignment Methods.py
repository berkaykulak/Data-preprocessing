import seaborn as sns
import missingno as msno
from ycimpute.imputer import knnimput
import pandas as pd
import numpy as np
from ycimpute.imputer import iterforest

import seaborn as sns
import missingno as msno
from ycimpute.imputer import EM


df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])
print(df.head())
df.isnull().sum()


var_names = list(df)
n_df = np.array(df)

print(n_df[0:10])
print(n_df.shape)
dff = knnimput.KNN(k = 4).complete(n_df)
print(type(dff))
dff = pd.DataFrame(dff, columns = var_names)



df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])


df.isnull().sum()

var_names = list(df)

n_df = np.array(df)
dff = iterforest.IterImput().complete(n_df)

dff = pd.DataFrame(dff, columns = var_names)

dff.isnull().sum()

df = sns.load_dataset('titanic')
df = df.select_dtypes(include = ['float64', 'int64'])
var_names = list(df)

n_df = np.array(df)
dff = EM().complete(n_df)
dff = pd.DataFrame(dff, columns = var_names)
dff.isnull().sum()