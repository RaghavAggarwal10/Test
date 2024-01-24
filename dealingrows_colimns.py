# import pandas as pd 
# # we perform basic operations on columns like selecting, deleting, adding and renaming

# data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# # Convert the dictionary into DataFrame 
# df = pd.DataFrame(data)
 
# # select two columns
# print(df[['Name', 'Qualification']])#we can either access the columns by calling them by their columns name.
# # Order to delete a column in Pandas DataFrame, we can use the drop() method.
# # Columns is deleted by dropping columns with column names
   

# importing pandas module
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name" )#index_coll is used to change the index column values to name 
print(data)
# The drop method is used to remove specified columns from the DataFrame
# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)#1 specifies column and 0 specifies rows
# The inplace=True parameter means that the changes will be made directly to the existing DataFrame (data) without the need to create a new DataFrame. If inplace is set to False (or not specified), a new DataFrame with columns removed will be returned.
# display
print(data) 
