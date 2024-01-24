# import pandas as pd
import pandas as pd
import numpy as np 
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# simple array
data = [1, 2, 3, 4]
ser = pd.Series(data)#a one-dimensional labeled array capable of holding data of any type 
#axis labels are collectively called index
# In order to create a series from the dictionary, we have to first create a dictionary after that we can make a series using dictionary.
dict = {'Geeks': 10,
        'for': 20,
        'geeks': 30}
 
# create series from dictionary
ser1 = pd.Series(dict)
#here key values will act as index 
# we can change the value of index using  index function 
see=pd.Series(data, index=[10,11,21,13])
#creating series using arrange function
se=np.arange(10,15)
serobj=pd.Series(data=se*5,index=se)
print(serobj)
print(see)
print(ser1)
print(ser)
# The number of rows returned is defined in Pandas option settings.

# You can check your system's maximum rows with the pd.options.display.max_rows statement.