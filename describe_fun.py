#this function is used to view basic statistical details like percentile ,mean ,median etc  
# percentiles=None: If not specified, the default percentiles (25th, 50th, and 75th) will be included in the summary.
# include=None: If not specified, all numeric types will be included in the summary.
# exclude=None: If not specified, no data types will be excluded from the summary.

import pandas as pd
# reading and printing csv file
data = pd.read_csv('nba.csv')
#  use to_string() to print the entire DataFrame.
print(data.describe ())