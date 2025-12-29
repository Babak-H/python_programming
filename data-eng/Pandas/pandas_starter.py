'''
Introduction to Pandas
You can think of pandas as an extremely powerful version of Excel, with a lot more features.
A Series is very similar to a NumPy array (in fact it is built on top of the NumPy array object). What differentiates the NumPy array from a Series, is that a Series can have axis labels, meaning it can be indexed by a label, instead of just a number location. It also doesn't need to hold numeric data, it can hold any arbitrary Python Object
'''

from numpy.random import randn
import numpy as np
import pandas as pd
from datetime import datetime

############################## Series ###########################

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a': 10, 'b': 20, 'c': 30}

# Creating a Series => You can convert a list,numpy array, or dictionary to a Series
pd.Series(data=my_list)
pd.Series(data=my_list, index=labels)
pd.Series(my_list, labels)
pd.Series(arr)
pd.Series(arr, labels)
pd.Series(d)  # series from a dictionary

# print(tabulate(df, headers='keys', tablefmt='psql'))


# Data in a Series => A pandas Series can hold a variety of object types:
pd.Series(data=labels)  # String type

# Even functions (although unlikely that you will use this)
pd.Series([sum, print, len])

# Using an Index => The key to using a Series is understanding its index. Pandas makes use of these index names or numbers
# by allowing for fast look ups of information (works like a hash table or dictionary).
ser1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
ser1

ser2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])
ser2

ser1['USA']

# Operations are then also done based off of index:
ser1 + ser2


'''
DataFrames
DataFrames are the workhorse of pandas and are directly inspired by the R programming language. We can think of a DataFrame as a bunch of Series objects put together to share the same index.
pd.DataFrame(data, index=idx, columns=col)
'''

np.random.seed(101)
# randn(5,4) : 5 rows and 4 columns
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(),
                  columns='W X Y Z'.split())

df

# Selection and Indexing => Let's learn the various methods to grab data from a DataFrame
# returns back a series
df['W']

# Pass a list of column names
# returns back another dataframe
df[['W', 'Z']]

# SQL Syntax (NOT RECOMMENDED!)
df.W

# DataFrame Columns are just Series
print(type(df['W']))

# Creating a new column:
df['new'] = df['W'] + df['Y']
df

# Removing Columns
df.drop('new', axis=1)  # axis=1 refers to columns

# Not inplace unless specified!
df

df.drop('new', axis=1, inplace=True)
df

# Can also drop rows this way
df.drop('E', axis=0)

# Selecting Rows
df.loc['A']

# Or select based off of position instead of label
df.iloc[2]  # row C

# Selecting subset of rows and columns
df.loc['B', 'Y']  # [row, col]

df.loc[['A', 'B'], ['W', 'Y']]   # returns back a dataframe


# Conditional Selection => An important feature of pandas is conditional selection using bracket notation, very similar to numpy
df > 0

df[df > 0]  # true => show value | false => NaN

df[df['W'] > 0]  # those rows that have <0 in column 'W' will be removed

df[df['W'] > 0]['Y']

df[df['W'] > 0][['Y', 'X']]  # changed the order of Y and X

# For two conditions you can use | and & with parenthesis:
df[(df['W'] > 0) & (df['Y'] > 1)]


# More Index Details => resetting the index or setting it something else
df

# Reset to default 0,1...n index
df.reset_index()   # this will add previous index as a new column


newind = 'CA NY WY OR CO'.split()
df['States'] = newind  # add a new column to the dataframe
df

df.set_index('States', inplace=True)
df


# Multi-Index and Index Hierarchy
# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

hier_index

df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
df

# For index hierarchy we use df.loc[], if this was on the columns axis, you would just use normal bracket notation df[].
# Calling one level of the index returns the sub-dataframe:

df.loc['G1']
df.loc['G1'].loc[1]
df.index.names


# setting names for different levels of indexes
df.index.names = ['Group', 'Num']
df


# Missing Data => a few methods to deal with Missing Data in pandas:

df = pd.DataFrame({'A': [1, 2, np.nan],
                  'B': [5, np.nan, np.nan],
                   'C': [1, 2, 3]})

df
df.dropna()  # removes all rows that include any sort of NaN cell
df.dropna(axis=1)  # drop all cols that include NaN
df.dropna(thresh=2)  # only remove rows that have atleast 2 NaN element in them
df.fillna(value='Fill Value')
df['A'].fillna(value=df['A'].mean())


# Groupby => The groupby method allows you to group rows of data together and call aggregate functions

# Create dataframe out of a dictionary
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
df

# Now you can use the .groupby() method to group rows together based off of a column name.
# For instance let's group based of Company. This will create a "DataFrameGroupBy" object:
df.groupby('Company')

# You can save this object as a new variable:
by_comp = df.groupby("Company")
# And then call aggregate methods off the object:
by_comp.mean()
by_comp.std()  # standard diviation

# for text based columns we get mean and max based on first character
by_comp.min()
by_comp.max()

by_comp.count()  # how many unqiue cells based on each group

by_comp.describe()
by_comp.describe().loc['GOOG']


# Merging, Joining, Concatenating
# There are 3 main ways of combining DataFrames together: Merging, Joining and Concatenating.
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

'''
Concatenation
Concatenation basically glues together DataFrames. Keep in mind that dimensions should match along the axis you are concatenating on. You can use 'pd.concat' and pass in a list of DataFrames to concatenate together
'''
# will concat them based on rows, stack dataframes on top of each other
pd.concat([df1, df2, df3])

pd.concat([df1, df2, df3], axis=1)  # based on columns

'''
Merging
The merge function allows you to merge DataFrames together using a similar logic as merging SQL Tables together. For example:
'''
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# here we get keys from second DataFrame
pd.merge(left, right, how='inner', on='key')

# a more complicated example:
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
left
right

# only shows rows that in them both dataframes have same key1,key2
pd.merge(left, right, on=['key1', 'key2'])
pd.merge(left, right, how='outer', on=['key1', 'key2'])  # outter merge
pd.merge(left, right, how='left', on=['key1', 'key2'])   # left merge
pd.merge(left, right, how='right', on=['key1', 'key2'])   # right merge


'''
Joining
Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a single result DataFrame.
'''
l = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                  'B': ['B0', 'B1', 'B2']},
                 index=['K0', 'K1', 'K2'])

r = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                  'D': ['D0', 'D2', 'D3']},
                 index=['K0', 'K2', 'K3'])
left
right

l.join(r)
left.join(r, how='outer')


'''
Operations
There are lots of operations with pandas that will be really useful, but don't fall into any distinct category.
'''

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                  444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
df

# Info on Unique Values
df['col2'].unique()  # gives back array of unique elements in col2 column
df['col2'].nunique()  # count of unique elements
# see each element in the coulmn has been repeated how many times
df['col2'].value_counts()

# Selecting Data
# Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1'] > 2) & (df['col2'] == 444)]
newdf


def times2(x):
    return x*2


# Applying Functions
df['col1'].apply(times2)

# sum of all elements in the column
df['col1'].sum()

# Permanently Removing a Column
del df['col1']
df

# Get column names and index:
df.columns
df.index

# Sorting and Ordering a DataFrame:
df.sort_values(by='col2')  # inplace=False by default

# Find Null Values or Check for Null Values
df.isnull()


# PIVOT TABLE => allows to change columns and indexes of the dataframe to reshape it
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)
df

df.pivot_table(values='D', index=['A', 'B'], columns=['C'])


# Data Input, Output => How to read and write files in Pandas

# csv in
df = pd.read_csv('example')
# csv out
df.to_csv('df')

# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects. (needs 'conda install BeautifulSoup4' to work)
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
df


'''
Date and Time in Pandas
'''
my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

# January 2nd, 2017
my_date = datetime(my_year, my_month, my_day)
my_date
# You can grab any part of the datetime object you want
print(my_date.day)

'''
NumPy Datetime Arrays
NumPy handles dates more efficiently than Python's datetime format.
The NumPy data type is called datetime64 to distinguish it from Python's datetime
'''
np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64')
np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[h]')
np.array(['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[Y]')

'''
NumPy Date Ranges
Just as np.arange(start,stop,step) can be used to produce an array of evenly-spaced integers, we can pass a dtype argument to obtain an array of dates. Remember that the stop date is exclusive.
'''
# AN ARRAY OF DATES FROM 6/1/18 TO 6/22/18 SPACED ONE WEEK APART
np.arange('2018-06-01', '2018-06-23', 7, dtype='datetime64[D]')

# By omitting the step value we can obtain every value based on the precision.
# AN ARRAY OF DATES FOR EVERY YEAR FROM 1968 TO 1975
np.arange('1968', '1976', dtype='datetime64[Y]')

'''
Pandas Datetime Index
We'll usually deal with time series as a datetime index when working with pandas dataframes. Fortunately pandas has a lot of functions and methods to work with time series
The simplest way to build a DatetimeIndex is with the pd.date_range() method:
'''
# THE WEEK OF JULY 8TH, 2018
pd.date_range('7/8/2018', periods=7, freq='D')

# Create a NumPy datetime array
some_dates = np.array(
    ['2016-03-15', '2017-05-24', '2018-08-09'], dtype='datetime64[D]')
some_dates
# Convert to an index
idx = pd.DatetimeIndex(some_dates)
idx
# Create some random data
data = np.random.randn(3, 2)
cols = ['A', 'B']
print(data)
# Create a DataFrame with our random data, our date index, and our columns
df = pd.DataFrame(data, idx, cols)
df

print(df.index)
print(df.index.max())
# Latest Date Index Location
print(df.index.argmax())
# Earliest Date Value
print(df.index.min())
# earliest date location
print(df.index.argmin())


# example dataset cleaning
df = pd.read_excel("AFI market all4.xlsx")

df["Date"] = df["%Key"].apply(lambda x: x[-7:])
df["SCC"] = df["%Key"].apply(lambda x: x[:4])

date_format = '%Y0%m'
df["Date_excel"] = df["Date"].apply(
    lambda x: datetime.datetime.strptime(x, date_format))
df.columns

df["Duration"] = [*map(lambda x, y: (x-y).days if y !=
                       "-" else "Not cleared", df["NetDueDate_PIA"], df["ClearDate_PIA"])]

df["Overdue_Y_N"] = df["Duration"].apply(lambda x: "Yes" if (isinstance(
    x, (int, float)) and x < 0) else ("-" if x == "Not cleared" else "No"))

df["NetDueDate_PIA_before_today"] = [*map(lambda x, y: "Yes" if (
    x != "-" and x < datetime.today() and y == "-") else "No", df["NetDueDate_PIA"], df["ClearDate_PIA"])]

df["Overdue_BM"] = [*map(lambda x, y, z: "Yes" if (x == "Yes" or y == "Yes") else (x if z ==
                         "-" else y), df["Overdue_Y_N"], df["NetDueDate_PIA_before_today"], df["ClearDate_PIA"])]

pd.unique(df["Overdue_BM"] == df["OverDue_PIA"])

#======================================================
#  How to group dataframe rows into list in pandas groupby?
'''
a b
A 1
A 2
B 5
B 5
B 4
C 6

A [1,2]
B [5,5,4]
C [6]
'''
df = pd.DataFrame({'a': ['A', 'A', 'B', 'B', 'B', 'C'], 'b': [1, 2, 5, 5, 4, 6]})
df.groupby('a')['b'].apply(list)
df1 = df.groupby('a')['b'].apply(list).reset_index(name='new')

# python dataframe pandas drop column using int
df.drop(df.columns[i], axis=1)

# Add column in dataframe from list
import numpy as np

m = np.arange(16) * 10
m[df.A]
array([0, 40, 50, 60, 150, 150, 140, 130])
df["D"] = m[df.A]
