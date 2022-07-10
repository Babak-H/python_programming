nums = [1, 2, 3, 4, 5]
l_nums = [n*n for n in nums]
print(l_nums)

l_2 = [n for n in nums if n % 2 == 0]
print(l_2)

# map applies a lambda function to list and returns result of lambda (here True / False)
print(list(map(lambda x: x % 2 == 0, nums)))
# filter applies lambda function but only returns value of elements that returned True
print(list(filter(lambda x: x % 2 == 0, nums)))
                     # outer loop         # inner loop
print([(letter, num) for letter in 'abcd' for num in range(4)])

# map function and tuples
n = 5
integer_list = map(int, "123".split())
print(hash(tuple(integer_list)))

# map and lambda for fibonacci
# The map() function applies a function to every member of an iterable and returns the result.
print(list(map(len, ['Tina', 'babak', 'Tom'])))

# Lambda is a single expression anonymous function often used as an inline function.
sum = lambda a, b, c: a+b+c
sum(1, 2, 3)
cube = lambda x: x**3

def fibonacci(n):
    list = []
    for i in range(0, n):
        if i == 0 or i == 1:
            list.append(i)
        else:
            list.append(list[i-1] + list[i-2])
    return list

n = 5
print(list(map(cube, fibonacci(n))))

# Extract first item of each sublist
lst = [["a", "b", "c"], [1, 2, 3], ["x", "y", "z"]]
lst2 = [item[0] for item in lst]
print(lst2)

# access all list elements from last to first in python list
l = [4, 3, 2, 1]
print([x for x in l[::-1]])

# lambda function:
answer = lambda x: print(x*7)
answer(5)

# sort() / sorted() function with lambda expressions => using lambda to sort by last name
names = ['Alf Zed', 'Mike Mo', 'Steve Jobs']
names.sort(key=lambda x: x.split()[-1].lower)  # sorts based on the second part of each string

people = [('A', 28), ('B', 13), ('C', 58)]
people.sort(key=lambda x: x[1], reverse=True)  # this will change the original list


# reduce()
'''
reduce() function accepts a function and a sequence and returns a single value calculated as follows:
Initially, the function is called with the first two items from the sequence and the result is returned. 
The function is then called again with the result obtained in step 1 and the next value in the sequence. 
This process keeps repeating until there are items in the sequence. The syntax of the reduce() function 
is as follows:
Syntax: reduce(function, sequence[, initial]) -> value
'''
from functools import reduce

def do_sum(x1, x2): return x1 + x2
reduce(do_sum, [1, 2, 3, 4])  # 1+2  -> 3+3  -> 6+4 => 10


