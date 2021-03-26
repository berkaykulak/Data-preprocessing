import seaborn as sns
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



print(df_table[aykiri_tf])

#delete
print(type(df_table))
df_table = pd.DataFrame(df_table)
print(df_table.shape)
t_df = df_table[~((df_table < (alt_sinir)) | (df_table > (ust_sinir))).any(axis = 1)]
print(t_df.shape)
print()

