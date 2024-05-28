import pandas as pd

#read the csv file into the dataframe
df=pd.read_csv('data.csv',
               dtype={'age':int,'salary':float},
                      usecols=['name','age','place']) #read the specific column  which we 
print(df)