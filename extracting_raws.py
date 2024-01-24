import pandas as pd 
data=pd.read_csv("nba.csv",index_col="Name")#changing the index value to names 
first=data.loc["Avery Bradley"]
second=data.loc["R.J. Hunter"]
print(first )
print(second)#loc function is used to get all the values that are related with that index we can extract two functions at same time 
rows=data.loc[["Avery Bradley","R.J. Hunter"]]#extracting multiple  values at same time
print(rows)#this method can also be used to extract multiple values at same time 
# row=data["Utah Jazz"] THIS WILshow an error as we are trying to access row values and we cann't access them without using loc fnction
row = data.loc["Avery Bradley":"Isaiah Thomas"] #this is used to extract allthe values that are present betwwn these index values 
print(row)
print(type(rows))
#.iloc[] is an indexer used for integer-location-based indexing of data in a DataFrame.

