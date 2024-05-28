import pandas as pd
data=[10,2,3,45,65]
series=pd.Series(data)
print(series)

# acess the element seperately by using indexing
print(series[3])


# arithmetical operations
series_add = series +10
print(series_add)

# filter the elements in the series.
filtered_series = series[series > 20]
print(filtered_series)

# statical method
# data =[10,2,3,45,65]
mean= series.mean()
print(f"the mean value of the series is {mean}")