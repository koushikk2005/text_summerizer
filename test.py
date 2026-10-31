import pandas as pd
df=pd.read_csv("C:\\Users\\Koushik Khan\\Downloads\\Dataset.csv")
print (df.head())
print (df.shape)
df_not_duplicated=df.drop_duplicates()
print (df_not_duplicated.shape)
df_not_missing=df_not_duplicated.dropna()
print ("Shape of DataFrame after removing missing values:", df_not_missing.shape)
