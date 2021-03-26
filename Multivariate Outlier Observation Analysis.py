import seaborn as sns
import numpy as np
from sklearn.neighbors import LocalOutlierFactor
import pandas as pd

df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64'])
df = df.dropna()


df_table = df["table"]
sns.boxplot(x = df_table)
Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3-Q1
alt_sinir = Q1- 1.5*IQR
ust_sinir = Q3 + 1.5*IQR
aykiri_tf = (df_table < alt_sinir)
df_table = df["table"]
df_table[aykiri_tf] = df_table.mean()

df_table = df["table"]
print(df_table[aykiri_tf])
print(alt_sinir)
df_table[aykiri_tf] = alt_sinir
print(df_table[aykiri_tf])

clf = LocalOutlierFactor(n_neighbors = 20, contamination = 0.1)


print(clf.fit_predict(df))
df_scores = clf.negative_outlier_factor_


print(df_scores[0:10])
print(np.sort(df_scores)[0:20])
esik_deger = np.sort(df_scores)[13]
aykiri_tf = df_scores > esik_deger

print(aykiri_tf)
yeni_df  = df[df_scores > esik_deger]
print(yeni_df)

print(df[df_scores < esik_deger])
print(df[df_scores == esik_deger])
baski_deger = df[df_scores == esik_deger]
aykirilar = df[~aykiri_tf]
print(aykirilar)


print(aykirilar.to_records(index = False))

res = aykirilar.to_records(index = False)
res[:] = baski_deger.to_records(index = False)
print(res)
print(df[~aykiri_tf])

df[~aykiri_tf] = pd.DataFrame(res, index = df[~aykiri_tf].index)
print(df[~aykiri_tf])

