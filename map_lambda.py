# reduce()

'''
function accepts a function and a sequence and returns a single value calculated as follows:
Initially, the function is called with the first two items from the sequence and the result is returned. 
The function is then called again with the result obtained in step 1 and the next value in the sequence. 
This process keeps repeating until there are items in the sequence. 

The syntax of the reduce() function is as follows:
Syntax: reduce(function, sequence[, initial]) -> value
'''

from functools import reduce


def do_sum(x1, x2): return x1 + x2


print(reduce(do_sum, [1, 2, 3, 4]))   # 1+2 -> 3+3 -> 6+4 = 10


# ==========================
# List Comprehensions , lambda fuctions, map

nums = [1,2,3,4,5]

l_nums = [n*n for n in nums]
print(l_nums)

l_2 = [n for n in nums if n%2 == 0]
print(l_nums)

# map applies a lambda function to list and returns result of a lambda (here True / False)
print(list(map(lambda x: x%2 == 0, nums)))

# filter applies lambda function but only returns value of element that returned True
print(list(filter(lambda x: x%2 == 0, nums)))

                     # outter loop        # inner loop
print([(letter, num) for letter in 'abcd' for num in range(4)])


# map function and tuples
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))


# map and lambda for fibonacci
# the map() function applies a function to every memeber of an iterable and returns the result
print(list(map(len, ['Tina', 'Tony', 'Tom'])))

# lambda is a single expression anonymous function often used as an inline function
sum = lambda a,b,c: a+b+c
sum(1,2,3)

cube = lambda x: x**3

def fibonacci(n):
    for i in range(0, n):
        if i == 0 or i == 1:
            list.append(i)
        else:
            list.append(list[i-1]+list[i-2])
    return list

print(list(map(cube, fibonacci(10))))

#===========================
# slicing strings and using map function

n = 5
student_marks = {}
for _ in range(n): # we use _ since we just want to iterate
    line = input().split()
    name, score = line[0], line[1:]
    # map function applies float to all elements of the list
    scores = map(float, scores)
    student_marks[name] = scores


# lambda example
answer = lambda x: print(x*7)
answer(5)

#======================
# zip

stocks = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'APPL': 99.76
}

'''
change a dictionary to two lists:
stocks.keys() = gives you a list of first items (keys) of the dictionary.
stocks.values() = gives you a list of second items (values) of the dictionary.
* you can't min/max a dictionary but you can min/max it if you change it to a zipped list.
* if you want to min/max a dictionary based on it's values give the zipped list the values or the other way around.
* zipped list sorts based on the first value in a (x, y).
'''

min = min(zip(stocks.values(), stocks.keys()))  # key will be related to min value
max = max(zip(stocks.values(), stocks.keys()))

sorted_num = sorted(zip(stocks.values(), stocks.keys())) # sorts on values
sorted_word = sorted(zip(stocks.keys(), stocks.values())) # sorts on keys

print(min, max, sorted_num, sorted_word)


# zip will stop when the shortest list ends:
x = [1,2,3,4]
y = [1,4,6]

for i,j in zip(x, y):
    print(i/j)

