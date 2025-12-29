# Type Hint => what we expect something to be, python ignores the type hint during runtime by default, even when you assign the wrong type to something!

# Type Check => Static Analysis, makes sure we stick to the type hinted (before code runs), it requires external library
# we can install extentions such as "mypy" on vscode to run the type checking, it just highlights wrong types, does not throw any error!
# pip install mypy

# Data Validation => Runs at run time to check we stick to the type hinted, when data validation failed, it throws validation errors to prevent the script from runnig
# pydantic is a library for data validation
# pip install pydantic

# for external libraries to be type hinted, we need to install extra stub modules for them
# python3 -m pip install types-requests

import random
import requests

from pydantic import validate_call
from typing import NewType, TypedDict, Any, TypeVar
from dataclasses import dataclass


# type RGB = tuple[int, int, int]
# type HSL = tuple[int, int, int]

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])

# we define a object User that is a dictionary with key of type string and value of type int,string or none
# User is called a "Type Alias"
# type User = dict[str, str | int | RGB |None]


# instead of type User we can use class User that inherits TypedDict, since we want to map each key to specifc value type
class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int | None
    fav_color: RGB | None
    
@validate_call
# age: int | None => age is of type int but it is optional
def create_user(
        first_name: str, 
        last_name: str, 
        age: int | None = None,
        fav_color: RGB | None = None ) -> User:
    email: str = f"{first_name.lower()}_{last_name.lower()}@gmail.com"
    
    # manual data validation
    if not isinstance(first_name, str):
        raise TypeError("first_name must be an string!")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be an string!")
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "fav_color": fav_color
    }


name: str = "Corey"
age: int = 32
last: str = "Schafer"

user1: User = create_user(name, last, age=age, fav_color=RGB((109, 123, 134)))
print(user1)

# age is supposed to be int but when we give input of string "32" there is no error here!
# pydantic automatically converts this into int 32
user2: User = create_user("Corey", "Schafer", "38")
print(user2)

try:
    user3: User = create_user("Corey", "Schafer", "thirty-eight")
except ValueError as e:
    print(e)


# ---------------------------------------------------------------------------
# ValidationError                           Traceback (most recent call last)
# Cell In[18], line 1
# ----> 1 user2: dict = create_user("Corey", "Schafer", "thirty-eight")
#       2 print(user2)

# File c:\Users\babak\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pydantic\_internal\_validate_call.py:39, in update_wrapper_attributes.<locals>.wrapper_function(*args, **kwargs)
#      37 @functools.wraps(wrapped)
#      38 def wrapper_function(*args, **kwargs):
# ---> 39     return wrapper(*args, **kwargs)

# File c:\Users\babak\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pydantic\_internal\_validate_call.py:136, in ValidateCallWrapper.__call__(self, *args, **kwargs)
#     133 if not self.__pydantic_complete__:
#     134     self._create_validators()
# --> 136 res = self.__pydantic_validator__.validate_python(pydantic_core.ArgsKwargs(args, kwargs))
#     137 if self.__return_pydantic_validator__:
#     138     return self.__return_pydantic_validator__(res)

# ValidationError: 1 validation error for create_user
# 2
#   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='thirty-eight', input_type=str]
#     For further information visit https://errors.pydantic.dev/2.12/v/int_parsing


user4: User = create_user("Corey", "Doe", 28, fav_color=RGB((206, 10, 48)))
print(user4)


# another way is to use data-class instead of TypedDict
@dataclass 
class UserClass:
    first_name: str
    last_name: str
    email: str
    # dataclass allows default variables
    age: int | None = None
    fav_color: RGB | None = None


@validate_call
def create_user_1(
        first_name: str, 
        last_name: str, 
        age: int | None = None,
        fav_color: RGB | None = None ) -> UserClass:
    email: str = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
    
    return UserClass(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color
    )
    
user_1: UserClass = create_user_1("Alex", "Jones", age=age, fav_color=RGB((109, 123, 134)))
user_2: UserClass = create_user_1("John", "Adams", age=age, fav_color=RGB((109, 123, 134)))

# we create an alias of type TypeVar
T = TypeVar("T")

# we want to get input of one type as list [T] and get output of SAME type T, so [str] and str or [UserClass] and UserClass
def random_choice(items: list[T]) -> T:
    return random.choice(items)

users = [user_1, user_2]
rando_user = random_choice(users)
print(rando_user)

emails = [user.email for user in users]
rando_email = random_choice(emails)
print(rando_email)


resp = requests.get("https://coreyms.com", timeout=5)
status = resp.status_code
print(status)

# Incompatible types in assignment (expression has type "str", variable has type "int")Mypyassignment
# status = "ok" # it should be numerical value like 200,404,...