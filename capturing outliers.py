import seaborn as sns
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include = ['float64', 'int64'])
df = df.dropna()

print(df.head())

df_table = df["table"]

sns.boxplot(x = df_table)
Q1 = df_table.quantile(0.25)
Q3 = df_table.quantile(0.75)
IQR = Q3-Q1

print(Q1)
print(Q3)
print(IQR)

alt_sinir = Q1- 1.5*IQR
ust_sinir = Q3 + 1.5*IQR

print(alt_sinir)
print(ust_sinir)


print((df_table < alt_sinir) | (df_table > ust_sinir))

aykiri_tf = (df_table < alt_sinir)

print(aykiri_tf.head())
print(df_table[aykiri_tf])
print(df_table[aykiri_tf].index)




