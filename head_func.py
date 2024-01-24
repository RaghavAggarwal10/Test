import pandas as pd 
#making dataframe
data=pd.read_csv("nba.csv")
#calling head function which is used to get top 5 values 
dat=data.head()
print(dat)
print(data)
series=data["Name"]
top=series.head(9)
print(top)
# tail() method is used to return bottom n (5 by default) rows of a data frame or series.
data_bottom=data.tail(10)
print(data_bottom)
#same can be done in series
