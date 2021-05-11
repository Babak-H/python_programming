import pandas as pd
import logging
import os
from datetime import datetime

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


# custom Exception class
class SalaryError(ValueError):
    pass  # the Error class of parent will catch errors for the child error class too


class BonusError(SalaryError):
    pass

#######################################################


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

#######################################################
