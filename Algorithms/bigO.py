# big O notation

# O(n)
arr = [1, 2, 3, 4, 5, 6, 7, 8]

for num in arr:
    print(num)

# O(1)


def compressBoxes(arr: [int]):
    print(arr[0])


compressBoxes([1, 2, 3])


# Big O(3 + 4n) = O(n)
def funChallenge(arr):
    a = 10  # O(1)
    b = 50 + 3  # O(1)

    for _ in range(len(arr)):
        compressBoxes(arr)  # O(n)
        _ = True    # O(n)
        b += 1  # O(n)

    return b  # O(1)


# O(n^2) = (n * n)
def log_all_pairs(arr):
    for num in arr:
        for num_2 in arr:
            print(f'{num} * {num_2}')


log_all_pairs([1, 2, 3])


# big O = O(n + n^3) = O(n^3) drop non-dominant variables
def longLoop(arr):
    # O(n)
    for num in arr:
        print(num)

    for num_1 in arr:  # O(n)
        for num_2 in arr:  # O(n)
            for num_3 in arr:  # O(n)
                print(num_1 + num_2 + num_3)


def boo(num):
    # Space complexity O(1) = doesnt add any extra memory to the system
    for i in range(num):
        print(i)

    arr = []
    # space complexity O(n)
    for i in range(num):
        arr.append(i)


boo(10)


def array_of_Hi_n_times(num):
    hi_arr = []
    # Space complexity O(n)
    for i in range(num):
        # here we create a new memory space for each run of this loop
        hi_arr[i] = "Hi"
    return hi_arr


# find the most recent tweet
tweet_arr = [{"tweet": "hi", "date": 2012},
             {"tweet": "bye", "date": 2012},
             {"tweet": "teddy", "date": 2011}]

# to do so we need nested loop to compare all the tweets together, therefore we have time complexity of O(n^2)

tweet_arr[0]  # O(1)
tweet_arr[:-1]  # O(1)

len("asddfDgfJ")  # O(1) because this function is a built-in lookup function


# given two arrays create a function that lets users know wether these two arrays contain any common items:
a1 = [1, 2, 3]
a2 = [3, 4, 5]
# should return True

# using brute force here gives back time complexity of O(a*b)

# optimal solution here would be using a hashtable or dictionary
# Big O time complexity = O(a+b)
# accessing item in a dictionary/hashmap is O(1)


def contains_common_item(arr1, arr2):
    my_dict = {}

    for item in arr1:  # O(a)
        if item not in my_dict:
            my_dict[item] = True

    for item in arr2:  # O(b)
        if my_dict[item] == True:
            return True
    return False


print(contains_common_item(a1, a2))
