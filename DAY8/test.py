import pandas as pd

#read csv file into dataframe
df=pd.read_csv('data.csv')
print(df)

#clean the row without empty values
df_cleaned_Row=df.dropna(how='all')
# print(df_cleaned_Row)

df_cleaned_col=df.dropna(axis=1,how="all")
# print(df_cleaned_col)

df_filled_data=df.fillna(0)
print(df_filled_data)