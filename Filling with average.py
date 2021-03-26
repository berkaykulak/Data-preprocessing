import seaborn as sns
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


print(df.head())
df_table = df["table"]
print(aykiri_tf.head())
print(df_table[aykiri_tf])
print(df_table.mean())
print(df_table.mean())

df_table[aykiri_tf] = df_table.mean()
print(df_table[aykiri_tf])


print()
print()
print()
