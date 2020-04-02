# loops


# loop over an string
for letter in 'Hello':
    print(letter)


# skip first entry in a for loop in python
cars = [1,2,3,4]

itercars = iter(cars)
next(itercars)  # jump first element
for car in itercars:
    print(car)


# while loop
x = 0

while True:
    if x == 5:
        break

    print(x)
    x += 1


# Fibonaci sequence
a,b = 0,1
for _ in range(0, 10):
    print(a)
    a,b = b, a+b

''' 
The enumerate() function adds a counter to an iterable. So for each element in cursor, 
a tuple is produced with (counter, element). the for loop binds that to row_number 
and row, respectively.
'''

elements = ('a', 'b', 'c')
for element in elements:
    print(element)

for count, element in enumerate(elements):
    print(count, element)


# else clause after loop
my_list = [1,2,3,4]

for i in my_list:
    print(i)
    if i == 6:
        break
else:
    print("this will be executed if we didnt have any breaks")

j = 0
while j < 5:
    print(j)
    j += 1
    if j == 3:
        break
else:
    print("this will be executed if we didnt have any breaks")