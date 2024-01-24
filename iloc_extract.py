import pandas as pd

# Creating a sample DataFrame
data = pd.DataFrame({
	'Name': ['Geek1', 'Geek2', 'Geek3', 'Geek4', 'Geek5'],
	'Age': [25, 30, 22, 35, 28],
	'Salary': [50000, 60000, 45000, 70000, 55000]
})

# Setting 'Name' column as the index for clarity
data.set_index('Name', inplace=True)

# Displaying the original DataFrame
print("Original DataFrame:")
print(data)

# Extracting a single row by index
row_alice = data.iloc[0, :]
print("\nExtracted Row (Geek1):")
print(row_alice)

# Extracting multiple rows using a slice
rows_geek2_to_geek3 = data.iloc[1:3, :]
print("\nExtracted Rows (Geek2 to Geek3):")
print(rows_geek2_to_geek3)
# Dataframe.loc[["row1", "row2"], ["column1", "column2", "column3"]]
# importing pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
		'degree': ["BCA", "BCA", "M.Tech", "BCA"],
		'score':[90, 40, 80, 98]}

# creating a dataframe 
df = pd.DataFrame(dict)

# using a comparison operator for filtering of data
print(df['degree'] == 'BCA')
dat = pd.read_csv("nba.csv", index_col ="Name")
  
# using greater than operator for filtering of data
print(dat['Age'] > 25)
# reading csv
s = pd.read_csv("stock.csv", squeeze = True)
# defining function to check price
def fun(num):

	if num<200:
		return "Low"

	elif num>= 200 and num<400:
		return "Normal"

	else:
		return "High"

# passing function to apply and storing returned series in new
new = s.apply(fun)

# printing first 3 element
print(new.head(3))

# printing elements somewhere near the middle of series
print(new[1400], new[1500], new[1600])

# printing last 3 elements
print(new.tail(3))
