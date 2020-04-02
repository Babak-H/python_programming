# Numbers and Numerical Values

num = 3
num_1 = 3.14

print(type(num))   # int
print(type(num_1))  # float

print(3 * 2 + 1)  # 7
print(3 * (1 + 2))  # 9

# absolute value
print(abs(-3))

# rounding number
print(round(3.14251, 2))

a,b = 3, 4
print(a // b)   # floors to smaller int from float
print(float(a) / b)

# ==========================
# if else statement with integers

N = int(input())

if N >=1 or N <= 100:
    if N % 2 != 0:
        print("Strange")
    elif N >= 2 and N < 5:
        print("Not Strange")
    else:
        print("None either")

# ==========================
# calculate leap year

def is_leap(year):
    leap = False

    if year % 4 is 0 and year % 100 != 0:
        leap = True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    return leap

year = 1369
print(is_leap(year))

# ==========================
# for two given points calculate euclidean distance in python:
import math

x = [1,2]
y = [3,4]

def euclideanDistance(inst1, inst2):
    distance = 0
    for i in range(len(inst1)):
        distance += pow((inst1[i] - inst2[i]), 2)

    return math.sqrt(distance)

# ==========================
# Efficient way to convert strings from split function to int in Python

test = '8743-12083-15'
first_int = [int(x) for x in test.split("-")]


#  reverse an integer, and tell if palindrome (same number on both sides)
def palindrome(num):
    return str(num) == str(num)[::-1]
