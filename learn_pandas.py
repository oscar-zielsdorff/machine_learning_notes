import pandas as pd

# Pandas uses DataFrame and Series objects (among others)

## DataFrame #####################################################
# A table of data.
# Functionally different series glued together.

# dictionary where keys = column names & list = data rows
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

# The list of row labels is called an Index.
# The index defaults to ascending count starting at 0.
# This can be manually assigned instead if desired
df = pd.DataFrame({
    'John':['It was ok', 'I liked this one'], 
    'Jane':['It was bland', 'This one was better']},
    index=['Product A', 'Product B']
)

## Series ########################################################
# A sequence of data values (like a list).
series = pd.Series([1,2,3,])

# An index can also be assigned for a series
series = pd.Series(
    [1, 2, 4,],
    index=['2014 Price', '2016 Price', '2020 Price'],
    name='McChicken Prices'
)

## Reading Data Files ###############################################
salaries = pd.read_csv('csv_files/sample_pandas_data.csv')
print(salaries.head())

# Shape tells how large a dataframe is (rows, cols)
print(salaries.shape)
print()

# If the csv file contains an index it can be specified
pd.read_csv('csv_files/sample_pandas_data.csv', index_col=0)

## Saving Data Files ################################################
# df.to_csv('my_data_file.csv')

## Native Accessors #################################################
# columns can be accessed like an attribute or dictionary.
salaries.City
salaries['City'] # returns a series for the col data
salaries['City'][0] # returns first entry in City col

## Indexing in Pandas ###############################################
# For more advanced operations pd has built-in functions.
# iloc and loc
# These functions are row 1st, col 2nd (oposite of python).
# Making it slightly easier to get rows, harder to get cols.

# When choosing between iloc and loc note that they use
# different indexing schemes:
# iloc is exclusive, so [0:3] will grab indices 0,1,2
# loc is inclusive, so [0:3] will grab indices 0,1,2,3

# iloc allows selecting rows through numerical position.
salaries.iloc[0] # select first row
salaries.iloc[-3:] # select last 3 rows
salaries.iloc[[1, 3, 5]] # select rows 1, 3, & 5

# iloc can select columns using the : operator
salaries.iloc[:, 1] # gets whole column at idx 1
salaries.iloc[:3, 1] # gets first 3 entries in col
salaries.iloc[[0,1,2], 1] # gets listed rows in col

# loc allows label-based selection.
salaries.loc[:, 'City'] # get the City column
salaries.loc[0, 'City'] # get first row in City col
salaries.loc[:, ['Name', 'City', 'Salary']] # get listed cols
salaries.loc[:, 'Name':'City'] # gets cols ranging the two
salaries.loc[[1, 3, 5], ['Name', 'City']] # indices of cols

## Manipulating the Index ###########################################
# The index used can be set to a column (if applicable)
# salaries.set_index('Name')

## Conditional Selection ############################################
salaries.Name == 'Frank' # returns boolean series

# used with loc to select relevant data.
salaries.loc[salaries.Name == 'Frank'] # all rows named Frank

# multiple conditions require parenthesis
# 'and' statements use the & symbol
salaries.loc[
    (salaries.Name == 'Frank')
    & (salaries.Salary >= 50000)
]
# 'or' statements use the | symbol
salaries.loc[
    (salaries.Name == 'Frank')
    | (salaries.Name == 'Grace')
]

## Pandas built-in conditionals
# isin / isnull / notnull

# isin lets you select values that are in a list
salaries.loc[salaries.Name.isin(['Frank','Grace'])]

# isnull and notnull highlight values which are/aren't empty
salaries.loc[salaries.Salary.isnull()]
salaries.loc[salaries.Salary.notnull()]

## Assigning Data ###################################################
sals = pd.read_csv('csv_files/sample_pandas_data.csv')

# assign constant value
sals['Name'] = 'Oscar' # all Name entries set to 'Oscar'

# assign with an iterable of values (of same size)
sals['index_reversed'] = range(len(sals), 0, -1)

## Summary Functions ###############################################
# Restructures / insight into the data in a useful way.

# high-level summary of column attributes
salaries.describe() # shows data for numerical columns
salaries.Name.describe() # shows diff data for string data

# specific statistics
salaries.Salary.mean() # average value (num only)
salaries.Name.unique() # list of unique values
salaries.Name.value_counts() # unique values and their counts

## Map Functions #################################################
# Takes set of data and 'maps' them to another set of values.
# e.g. Change data format or represent in another way.
# This returns a new object w/o modifying the original.

# map() takes a function that expects a single value from
# a series. It returns a new series with transformed values.
# e.g. demeaning the salary data to 0:
salary_mean = salaries.Salary.mean()
s = salaries.Salary.map(lambda salary: salary - salary_mean)

# apply() applies a function to each row of a dataframe.
# axis='columns' (default) applies the function to each row.
# axis='index' applies the function to each column.
def demean_salary(row):
    row.Salary = row.Salary - salary_mean
    return row

s2 = salaries.apply(demean_salary, axis='columns')

# Pandas will try to recognize operations based on the type.
# using a single value will apply the operation to each row:
salaries.Salary - salary_mean
# while using a series of same size will go by element:
salaries.Name + ' - ' + salaries.City

## Grouping #########################################################
# value_counts() is a shortcut to this grouping
unique_counts_1 = salaries['Age'].value_counts()
unique_counts_2 = salaries.groupby('Age').Age.count()

# Summary functions can be applied to groupings
max_sal_by_age = salaries.groupby('Age').Salary.max()

# apply() can be used to access the grouped dataframe directly
salaries.groupby('Age').apply(lambda df: df.loc[df.Salary.idxmax()])

# Grouping can be applied to multiple columns
salaries.groupby(['Age', 'City']).apply(lambda df: df.loc[df.Salary.idxmax()])

# agg() allows running multiple functions on the df at once
salaries.groupby(['City']).Salary.agg([len, min, max])

# Multiple indices can result from groupings and have several
# methods to deal with their tiered structure.
grouped = salaries.groupby(['City', 'Age']).describe()
mi = grouped.index
type(mi) # <class 'pandas.core.indexes.multi.MultiIndex'>
grouped.reset_index() # return to a standard index

## Sorting ##########################################################
# Sorting by values, which retains the original index
salaries.sort_values(by='Salary') # sort ascending
salaries.sort_values(by='Salary', ascending=False) # descending
salaries.sort_values(by=['City','Salary'], ascending=False)

# Sorting by index is also possible
salaries.sort_index()

## Data Types (dtype) ###############################################
# The data type for a column or series is known as the dtype.
salaries.Salary.dtype # dtype('int64')
salaries.Name.dtype # dtype('O') (object)

# every column of a dataframe can be checked at once
salaries.dtypes # returns a series with cols as index and dtype vals

# dtypes can be converted on a column
salaries.Salary.astype('float64')
salaries.Salary.astype('str')

# the index also has its own dtype
salaries.index.dtype # dtype('int64')

# Other dtypes possible include categorical and timeseries data

## Missing Data #####################################################
# Entries missing values are assigned NaN (not a number).
# These are always a float64 dtype.

# They can be selected via pd.isnull() or pd.notnull()
salaries[pd.isnull(salaries.City)] # []

# Replacing missing data:
salaries.City.fillna('Unknown')

# Replacing existing/specific data:
salaries.City.replace('', 'Unknown')
salaries.City.replace('Los Angeles', 'LA')

# Example:
entries_per_city = salaries.fillna('Unknown').groupby('City').size().sort_values(ascending=False)

## Renaming ##########################################################
# Change index and/or column names. A dictionary maps the change.
# Index changes are rare and may be easier with set_index().
salaries.rename(columns={'Name':'FirstName'})
salaries.rename(index={0:'FirstEntry', 1:'SecondEntry'})

# Both row and column indices have a name attribute that can be set.
(
    salaries.rename_axis('entries', axis='rows')
    .rename_axis('fields', axis='columns')
)

## Combining #########################################################
# Sometimes different dataframes and/or series will need to
# be combined. These are, in increasing complexity, the
# concat(), join(), and merge() functions.

# concat will combine a list of elements along an axis.
# This is useful if 2 data sets have the same columns.
# canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
# british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
# pd.concat([canadian_youtube, british_youtube])

# join combines dataframe objects that have an index in common.
# lsuffix and rsuffix are needed because the data shares col names.
# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# left.join(right, lsuffix='_CAN', rsuffix='_UK') # adds suffix to col

# example for joining on a shared column
# powerlifting_combined = (
#     powerlifting_meets.set_index('MeetID')
#     .join(powerlifting_competitors.set_index('MeetID'))
# )