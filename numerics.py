import math

num = 3
num_1 = 3.14
print(type(num))
print(type(num_1))

print(3 * 2 + 1)
print(3 * (1 + 2))

# absolute value 
print(abs(-3))

# rounding number
print(round(3.14251, 2))

# if else statement with integers:
N = 25

if (N >= 1 or N <= 100):
    if (N % 2 != 0):
        print("strange")
    elif (N >=2 and N < 5):
        print("Not strange")
    elif(N >= 6 and N <= 20):
        print("strange")
    else:
        print("Not strange")


if __name__ == '__main__':
    a = 12
    b = 13

print(a + b)
print(a - b)
print(a * b)
print(a // b)  # floors to smaller int from float
print(float(a) / b)


# calculate leap year
def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0):
        leap = True
    elif (year % 4 == 0 and year % 100 == 0 and year % 400 ==0):
        leap = True
    return leap

year = 2021
print(is_leap(year))

# Efficient way to convert string from split function to int in Python
test = '8743-12083-15'
lst_int = [int(x) for x in test.split("-")]

#  reverse an integer, and tell if palindrome (same number on both sides)
def palindrome(num):
    return str(num) == str(num)[::-1]

print(palindrome(121))