from frequency_counter import *
import pytest
from collections import Counter
import pandas as pd
import logging
import os
from datetime import datetime
from functools import wraps

#######################################################

'''
change a dictionary to two lists:
    stocks.keys() = gives you a list of first items (keys) of the dictionary.
    stocks.values() = gives you a list of second items (values) of the dictionary.
you can't min/max a dictionary but you can min/max it if you change it to a zipped list.

if you want to min/max a dictionary based on it's values give the zipped list the values or the other way around.
zipped list sorts based on the first value in a (x, y).
'''
stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'APPL': 99.76
}

min = min(zip(stocks.values(), stocks.keys()))
max = max(zip(stocks.values(), stocks.keys()))
sorted_num = sorted(zip(stocks.values(), stocks.keys()))
sorted_word = sorted(zip(stocks.keys(), stocks.values()))
print(min, max)
print(sorted_num)
print(sorted_word)

#######################################################
# doc string

def square(x):
    """Returns the square of the argument x"""
    return x*x


square.__doc__  # => will return 'Returns the square of the argument x'

s = "fox"
s.rjust(4)  # adds one space to start of the string => ' fox'

# ['hello', 'world'] ==> ['HELLO', 'WORLD']
[s.upper for s in ['hello', 'world']]

# add space to both sides of a string
s = "a"
s.center(3)  # ' a '

x = (1, 2, 3)
set(x)   # {1, 2, 3}


list_keys = ['a', 'b']
list_values = [['x', 'y'], [1, 2]]

list(zip(list_keys, list_values))  # [('a', ['x', 'y']), ('b', [1, 2])]

#######################################################
'''
*** interview question ***
given a timestamp date "2019-07-01 12:42:33" return string of "19Jul1B"
hours : 0-7 A 7-14 B 14-21 C 21-24 D  it should be the shown after start of the hour (7:00:01 accepted)
'''

def DateChecker(timestamp):
    date = re.match(
        r'(\d{4})\-(\d{2})\-(\d{2}) (\d{2})\:(\d{2})\:(\d{2})', timestamp)
    year = date.group(1)[2:]
    month = int(date.group(2))
    day = int(date.group(3))
    hour = int(date.group(4))
    mint = int(date.group(5))
    sec = int(date.group(6))
    string = ""
    string += year
    string += calendar.month_abbr[month]
    string += str(day)

    if ((hour >= 0 and hour < 7) and (mint > 0 or sec > 0)):
        string += "A"
    elif ((hour >= 7 and hour < 14) and (mint > 0 or sec > 0)):
        print(mint, sec)
        string += "B"
    elif ((hour >= 14 and hour < 24) and (mint > 0 or sec > 0)):
        string += "C"
    return string


print(DateChecker("2019-07-01 12:00:33"))

#######################################################

# Iterating through 2 dimensional lists in 1 line
sandwiches = [["bacon", "banana"], ["ham", "salami", "cheese"]]
prefs = {"bacon": 5, "ham": -2, "salami": 1}

scores = [[", ".join(i), sum(prefs[j] for j in i if j in prefs)]
          for i in sandwiches]
print(scores)

#######################################################

# write a program that prints numbers from 1 to 50, for multiples of 3 print "Fizz", for mutilples of 5 print "Buzz"
# for both print "FizzBuzz"
for i in range(1, 51):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)

#######################################################

# slicing strings and using map function
n = int(input())  # this only receives the first line of input
student_marks = {}
for _ in range(n):   # we use _ since we just want to iterate
    line = input().split()
    name, scores = line[0], line[1:]
    # map function applies float to all elements of the list
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()

print("{0:.2f}".format(
    sum(student_marks[query_name]) / len(student_marks[query_name])))

#######################################################

# find second smallest number in a inner list
p_list = []
for _ in range(0, int(input())):
    p_list.append([input(), float(input())])


# for name, marks in marksheet : this is how we iterate inner lists with two array
# then we select mark
# and use set to remove duplicates
second_low = sorted(list(set([marks for name, marks in p_list])))[1]

#######################################################

# for two given points calculate eucledian distance in python:
x = [1, 2]
y = [3, 4]


def euclideanDistance(inst1, inst2):
    dist = 0
    for i in range(len(inst1)):
        dist += pow((inst1[i] - inst2[i]), 2)
    return round(math.sqrt(dist), 2)


print(euclideanDistance(x, y))

#######################################################
# if a character in string is lower case make it upper and vice versa then return the string


def swap_case(s):
    l = list(s)
    for i in range(len(l)):
        if(l[i].isupper()):
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()
    return "".join(l)


s = "Today Weather is gooD"
result = swap_case(s)
print(result)

#######################################################
# how many times a string occurs in a substring:


def count_substring(string, substring):
    count = 0
    num = 0
    for i in range(len(string)):
        if string[i] == substring[num]:
            num = num+1
        else:
            num = 0
        if num == len(substring):
            count = count + 1
            num = 0
        return count


string = "bad fox jumped over good dog , bad fox"
sub_string = "bad fox"
count = count_substring(string, sub_string)
print(count)

# easier way to do same thing:
message = "bad fox jumped over good dog , bad fox"
print(message.lower().count('bad fox'))

#######################################################

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

LOGGING_FORMAT = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

DATE_NOW = datetime.now()
F_PREFIX = "{year}.{month}.{day}".format(year=DATE_NOW.year,
                                         month=str(DATE_NOW.month).zfill(2),
                                         day=str(DATE_NOW.day).zfill(2))
F_SUFFIX = 'Error.log'

file_handler = logging.FileHandler(f"{F_PREFIX}_{F_SUFFIX}")
file_handler.setFormatter(LOGGING_FORMAT)
LOGGER.addHandler(file_handler)


LOGGER.info("Starting the Data Extraction")


#######################################################

try:
    x = 1000/0
except Exception as e:
    Error_message = "problem with data extraction "
    LOGGER.info('[-] %s', Error_message+str(e), exc_info=True)

#######################################################

class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day

#######################################################

class Counter:
    def __init__(self, count):
        self.count = count

    def add_counts(self, n):
        self.count += n


class Indexer(Counter):  # this will cause an error as we don't pass anything to default constructor
    pass

#######################################################

class LoggedDF(pd.DataFrame):

    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        # Copy self to a temporary DataFrame, the "self" here is an actual dataframe itself
        temp = self.copy()
        # Create a new column filled with self.created_at
        temp["created_at"] = self.created_at
        # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
        pd.DataFrame.to_csv(temp, *args, **kwargs)

#######################################################

class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    # Define __eq__ that returns True if the number attributes are equal
    # MODIFY to add a check for the type()
    def __eq__(self, other):
        if type(self) == type(other):
            return (self.number == other.number)
        else:
            return False


# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

#######################################################

class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True


class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True


p = Parent()
c = Child()

p == c  # Child's __eq__() called

#######################################################

my_num = 5
my_str = "Hello"
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
print(f)  # my_num is 5, and my_str is "Hello".

#######################################################
# MODIFY the function to catch exceptions


def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError as e:
        print("Cannot divide by zero!")
    except IndexError as e:
        print("Index out of range!")


a = [5, 6, 0, 7]

# Works okay
print(invert_at_index(a, 1))
# Potential ZeroDivisionError
print(invert_at_index(a, 2))
# Potential IndexError
print(invert_at_index(a, 5))

#######################################################
# custom Exception class


class SalaryError(ValueError):
    pass  # the Error class of parent will catch errors for the child error class too


class BonusError(SalaryError):
    pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")
        elif self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")
        else:
            self.salary += amount


# It's better to list the except blocks in the increasing order of specificity, i.e. children before parents, otherwise
# the child exception will be called in the parent except block.
emp = Employee("Katze Rik", 50000)
try:
    emp.give_bonus(7000)
except SalaryError:
    print("SalaryError caught")  # this will be executed
except BonusError:
    print("BonusError caught")


emp = Employee("Katze Rik", 50000)
try:
    emp.give_bonus(7000)
except BonusError:
    print("BonusError caught")  # this will be executed
except SalaryError:
    print("SalaryError caught")

#######################################################

class BetterDate:

    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    # Add _is_valid() checking day and month values
    def _is_valid(self):
        if (self.day <= BetterDate._MAX_DAYS) and (self.month <= BetterDate._MAX_MONTHS):
            return True
        else:
            return False


bd1 = BetterDate(2020, 4, 30)
print(bd1._is_valid())

bd2 = BetterDate(2020, 6, 45)
print(bd2._is_valid())

#######################################################

class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

    # Add a decorated balance() method returning _balance
    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal
        print("Setter method called")


# Create a Customer
cust = Customer("Belinda Lutz", 2000)
cust.balance = 3000
print(cust.balance)

#######################################################
# MODIFY the class to use _created_at instead of created_at


class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        print("arg", *args)
        print("kwarg", **kwargs)
        pd.DataFrame.__init__(self, *args, **kwargs)
        self._created_at = datetime.today()

    def to_csv(self, *args, **kwargs):
        temp = self.copy()
        temp["created_at"] = self._created_at
        pd.DataFrame.to_csv(temp, *args, **kwargs)

    # Add a read-only property: _created_at
    @property
    def created_at(self):
        return self._created_at


# Instantiate a LoggedDF called ldf
ldf = LoggedDF({"col1": [1, 2], "col2": [3, 4]})

# this will throw an AttributeError as we haven't asigned setter method to _created_at
ldf.created_at = '2035-07-13'
######################################################################

def func():
    # print(a)
    a = "python is cool"


a = "data analytics is good"
func()   # UnboundLocalError: local variable 'a' referenced before assignment


def func_1():
    a = "python is cool"
    print(a)


a = "data analytics is good"
func_1()   # python is cool

######################################################################

def wrap():
    def inside():
        global lang  # this means that the variable below it is global
        lang = "German"

    print("Before calling wrap: " + lang)
    inside()
    print("After calling inside: " + lang)


lang = "English"
wrap()
# Before calling wrap: English
# After calling inside: German

print("Language in global scope: " + lang)  # Language in global scope: German

######################################################################

def wrap():
    lang = "Polish"

    def inside():
        nonlocal lang  # this will refer to closest non-local variable, which is the one inside wrap
        lang = "German"

    print("Before calling wrap: " + lang)
    inside()
    print("After calling inside: " + lang)


lang = "English"
wrap()
# Before calling wrap: Polish
# After calling inside: German
print("Language in global scope: " + lang)

######################################################################

def catch_it(a):

    try:
        2 + 2
        a = 5
        print(a)  # this will return 5
    # won't be executed since there is no error here
    except:
        print('exception raised')
        print(a)

    # will since there is no exception
    else:
        a -= 1
        print('else clause executed')
        print(a)  # this will return 4

    # will run regardless (always)
    finally:
        print('finally')
        print(a)  # this will return 4


a = 1  # won't be used since we have local variables inside the method
catch_it(a)

######################################################################

def result_or_fail(a):

    try:
        a += 1

    except ValueError:
        print('ValueError raised')

    # this will be printed, since the variable is string, yet we try to add it to an integer
    except TypeError:
        print('TypeError raised')

    except:
        print('error raised')

    else:
        print('else executed')

    # this will be printed
    finally:
        print('that is all')


a = '2'
result_or_fail(a)

######################################################################

def make_bold(fn):

    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def make_italic(fn):

    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def make_underline(fn):

    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped


@make_bold
@make_underline
@make_italic
def hello():
    return "Python 3 is superb"


print(hello())  # <b><u><i>Python 3 is superb</i></u></b>

######################################################################

def algorithmone(n,b,a):
     assert(b > 1)
     q = n
     k = 0
     while q != 0:
        a[k] = q % b
        q = q / b
        k++

     return k

print (algorithmone(5,233,676))

# what error will this code produce  => TypeError: 'int' object does not support item assignment, because: 50[42] = 7

######################################################################

# IndexError: string index out of range in Python [closed]
s = 'aba'
letter = ''
substring = ''

i = 0

while(i <= len(s)):    # here is the error: Change while(i <= len(s): to while(i < len(s)):, or to while(i <= len(s)-1)
    prev_letter = s[0]
    letter = s[i]

    if letter <= prev_letter:
        substring += letter
        prev_letter = letter
    i += 1

'''
In Python, a string is a single-dimensional array of characters. Indexes in Python programming start at 0. This means that the maximum index for any string will always 
be len(s)-1. In your code, i will eventually be equal to len(s), which is one element higher than the maximum.
As a side note, it would probably be beneficial to use a for loop rather than a while loop in your code. Your code can be replaced with this:
''''
# a better solution would be :
s = 'aba'
letter = ''
substring = ''

i = 0

for i in range(len(s)):
    prev_letter = s[0]
    letter = s[i]

    if letter <= prev_letter:
        substring += letter
        prev_letter = letter
        
######################################################################
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 2892: invalid continuation byte
for line in open('u.item'):
    # Read each line
    pass

# solution
'''
the right encoding for that problem. The encoding was "ISO-8859-1", so replacing open("u.item", encoding="utf-8") with 
open('u.item', encoding = "ISO-8859-1") will solve the problem.
'''
file = open('../Resources/' + filename, 'r', encoding="ISO-8859-1");
