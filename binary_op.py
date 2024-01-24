import pandas as pd  
# creating a series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
# creating a series
data1 = pd.Series([1, 6, 4], index=['a', 'b', 'd'])
print(data)
print(data1)
# we can add two series using add(). keyword
#fill_vaalue=0 will be used to put the values to zero if there are less values present in it 
s=data.add(data1, fill_value=0)#elements with same index are added e
print(s)
<<<<<<< HEAD

###extra
a=104
b=2
=======
#extra
a=10
b=10
>>>>>>> 67be8dfa7b4c7cd90cc2b94c3464bfae5f1742db
c=a+b
print(c)