import pandas as pd
# print(pd.__version__)#this is used to check the version that pandas is using
arr=[1,2,3]
my=pd.Series(arr)#It is a one-dimensional array holding data of any type and it also stores index of the values and also store the data type of the values 
#As  nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
myvar = pd.Series(arr, index = ["x", "y", "z"])#index can be used to name our argument
print(myvar)
print(my)