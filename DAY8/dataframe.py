import pandas as pd

#create  a dataframe with a dictionary
data={
    'name':["abc",'cde','efg'],
    'age':[24,23,24],
    'place':['tvm','tvm','klm']
}
df=pd.DataFrame(data)
print(df)

# print((df[['name','place']]))

#for accessing each row from the dataframe we need to use the inbuild function in pandas
# print(df.iloc[1])

# print(df[df['age']>23])

#add a new column into the dataframe

df['stipend']= [15000,5000,5000]
print(df)

#remove a column
df=df.drop(columns=['stipend'])
print(df)

#statistical function
#describe() help get the summery of statistics of your dataframe
print(df.describe())