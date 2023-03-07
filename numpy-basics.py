'''
NumPy (or Numpy) is a Linear Algebra Library for Python, the reason it is so important for Data Science 
with Python is that almost all of the libraries in the PyData Ecosystem rely on NumPy as one of their main 
building blocks.
'''

import numpy as np

'''
Numpy has many built-in functions and capabilities. We won't cover them all but instead we will focus on some of 
the most important aspects of Numpy: vectors,arrays,matrices, and number generation. 
Let's start by discussing arrays.

NumPy arrays are the main way we will use Numpy throughout the course. Numpy arrays essentially come in two flavors: 
vectors and matrices. Vectors are strictly 1-d arrays and matrices are 2-d (but you should note a matrix can still 
have only one row or one column).

We can create an array by directly converting a list or list of lists
'''

my_list = [1,2,3]
print(my_list)

# converting array to list (1-d array)
np.array(my_list)  

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)

# now we have 3x3 matrix array (2d array)
np.array(my_matrix)  


'''
Built-in Methods
There are lots of built-in ways to generate Arrays.
arange : Return evenly spaced values within a given interval.
'''
# similar to range() method of python
np.arange(0,10)  
# with two steps
np.arange(0,11,2) 

# Generate arrays of zeros 
np.zeros(3)
# 5x5 matrix array
np.zeros((5,5)) 

np.ones(3)
np.ones((3,3))

# linspace : Return evenly spaced numbers over a specified interval.

# here we want 3 evenly spaced numbers between 0 and 10
np.linspace(0,10,3)  
np.linspace(0,10,50)

# eye : Creates an identity matrix
np.eye(4) 


# Random : Numpy also has lots of ways to create random number arrays:
# rand : Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
np.random.rand(2)
np.random.rand(5,5)

# randn : Return a sample (or samples) from the "standard normal distribution". Unlike rand which is uniform
#  randn() can be both positive and negative
np.random.randn(2)
np.random.randn(5,5)

# randint : Return random integers from low (inclusive) to high (exclusive).
np.random.randint(1,100)
np.random.randint(1,100)
np.random.randint(1,100,10)

# an array from 0 to 25
arr = np.arange(25) 

ranarr = np.random.randint(0,50,10)
print(ranarr)

# Reshape : Returns an array containing the same data with a new shape.
# turn arr into a 5x5 matrix array
arr.reshape(5,5)  

# max, min, argmax, argmin
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax
print(ranarr)
ranarr.max()
# location of max element (start from zero)
ranarr.argmax()  
ranarr.min()
# location of min element
ranarr.argmin() 

# shape is an attribute that arrays have
arr.shape
# notice the two sets of brackets
arr.reshape(1,25)
arr.reshape(25,1)
arr.reshape(25,1).shape

# dtype : grab the datatype of the array
arr.dtype

# numpy Indexing and Selection
arr = np.arange(0,11)
print(arr)
# bracket indexing and selection
# get a value at index 8
arr[8]
# get a value in a range (5 is not included)
arr[1:5]
arr[0:5]

# Broadcasting : numpy arrays differ from normal python arrays because of their ability to broadcast
# Setting a value with index range (Broadcasting)
# sets every element from 0 to 5 to be 100
arr[0:5]=100
# Show
arr

arr = np.arange(0,11)
slice_of_arr = arr[0:6]
slice_of_arr

slice_of_arr[:] = 99
slice_of_arr
# note that the changes also occur in the original array
arr

# normally data is not copied, it just points to original array, to avoid this, use copy
arr_copy = arr.copy()
arr_copy

# Indexing a 2D array (matrix)
# The general format is arr_2d[row][col] or arr_2d[row, col]
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
arr_2d
# indexing row
arr_2d[1]
# grtting individual element value
arr_2d[1][0]
# same
arr_2d[1, 0]

# 2d slicing, shape (2,2) from top right corner
arr_2d[:2, 1:]
# shape bottom row
arr_2d[2]

# Fancy indexing :  allows you to select entire rows or columns out of order

# setup a matrix
arr2d = np.zeros((10,10))
arr2d
# length of array
arr_length = arr2d.shape
arr_length
# coloumn length
arr_length = arr2d.shape[1]
arr_length
# setup array
for i in range(arr_length):
    # every line in this array will have same number as its row number ==> we are using broadcasting here
    arr2d[i] = i

arr2d
# fancy indexing : give user the rows that all this elements are 2,4,...
arr2d[[2,4,6,8]]
# allows in any order
arr2d[[6,4,2,7]]

# selection
# lets go over how to use brackets for selection based off of comparison operators
arr = np.arange(1,11)
arr

arr > 4
bool_arr = arr > 4
bool_arr
# return all values that have True value (are bigger than 4)
arr[bool_arr]

arr[arr>2]
x = 3
arr[arr>x]

# Numpy Operations
# Arithmetic : You can easily perform array with array arithmetic, or scalar with array arithmetic.
arr = np.arange(0,10)
arr + arr
arr * arr
arr - arr
# warning on division by zero, it will replace 0/0 by nan value
arr / arr
# 1/0 is infinite
1 / arr
# to the power of 3
arr**3

# Universal Array Functions
# Numpy comes with many universal array functions, which are essentially just mathematical operations you can use 
# to perform the operation across the array.
np.sqrt(arr) # square root
np.exp(arr) # exponential (e^)
np.max(arr) # same as arr.max()
np.sin(arr)
np.log(arr) # logarithm to the power of 2

# create an array of 10 fives
x = np.ones(10)
x[:] = 5
x

# create an array of the integers from 10 to 50
np.arange(10, 51)

# create an array of all even integers from 10 to 50
np.arange(10, 51, 2)
np.arange(0.01, 1.01, 0.01).reshape(10,10)

# create an array of 20 linearly spaced points between 0 and 1
np.linspace(0, 1, 20)

# given a 9x9 matrix of sudoku numbers, check if it has the correct formatting?
import numpy as np

np_sudoku = np.random.randint(1, 9, (9,9))
print(np_sudoku)

def sudoku_checker(numpy_arr):
    s = {1,2,3,4,5,6,7,8,9}
    
    for i in range(np_sudoku.shape[0]):
        if set(np_sudoku[i, :]) != s:
            return False

    for j in range(np_sudoku.shape[1]):
        if set(np_sudoku[:, i]) != s:
            return False
    x = 0

    while x < 9:
        y = 0
        while y < 9:
            if set(np_sudoku[x:x+3, y:y+3].ravel()) != s:
                return False
            y +=3
            
        x += 3
        
    return True 

print(sudoku_checker(np_sudoku))


# How do I create an empty array/matrix in NumPy?
'''
You have the wrong mental model for using NumPy efficiently. NumPy arrays are stored in contiguous blocks of memory. If you want to add rows or columns to an existing array, 
the entire array needs to be copied to a new block of memory, creating gaps for the new elements to be stored. This is very inefficient if done repeatedly to build an array.

In the case of adding rows, your best bet is to create an array that is as big as your data set will eventually be, and then assign data to it row-by-row:
'''
import numpy
a = numpy.zeros(shape=(5,2))
print(a)
# add data to array
a[0] = [1,2]
a[1] = [2,3]


# 'numpy.ndarray' object has no attribute 'index'
v = np.random.randn(10)
print(v)
maximum = np.max(v)
minimum = np.min(v)
print(maximum, minimum)
v.index(maximum, minimum)  # this is the part that throws the error

# solution
index_of_maximum = np.where(v == maximum)
index_of_minimum = np.where(v == minimum)
