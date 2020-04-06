# Binary search
# log(N) << N

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 5

# going through each element of the list to look for items is called linear search. if the number isn't in the list, we
# need to go through all elements to realise that
def linear_search(data, target):
    for num in data:
        if num == target:
            return True
        return False

# iterative binary search
def binary_search_iterative(data, target):
    # indices
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


'''while loop iterations:
t = 1
[1,2,3,4,5,6,7,8,9]
t < mid

[1,2,3,4]
t < mid

[1,2]
t < mid

[1]
t = mid
'''

# recursive binary search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))

# =======================
'''
Given an array of "sorted" integers. We need to find the closest value to the given number.
Array may contain duplicate values and negative numbers.
Examples:
Input : arr = [1, 2, 4, 5, 6, 6, 8, 9]
Target number = 11
Output : 9
9 is closest to 11 in given array
'''

def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    # Edge cases for empty list or when the list is only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    # repeat this process until you get to the smallest possible two numbers close to the target:
    while low <= high:
        mid = (low + high) // 2  # find mid point
        # find difference on both sides
        if mid+1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)
        # set the smallest value for min difference and closest number
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid-1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid+1]
        # now change the high/low indexes, then move to side that is closer
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # in case of midpoint being same as the target
        else:
            return A[mid]

    return closest_num

arr = [1, 2, 4, 5, 6, 6, 8, 9, 10 , 12]
target = 11

print(find_closest_num(arr, target))

# =======================
'''
Given an array of n "distinct" integers "sorted" in ascending order, write a function that returns a "fixed point" in the array. 
If there is not a fixed point return "None".
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".
'''

# Fixed point is 3:
# #     0    1  2  3   4
# A = [-10, -5, 0, 3, 7]

# Fixed point is 0:
#     0  1  2  3   4
# A = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
#      0    1  2  3  4  5
# A = [-10, -5, 3, 4, 7, 9]

'''
check if value in the midpoint is smaller or larger than its index
if value_mid < index_mid : there is no way that in previous indexes value is equal to index
if value_mid > index_mid : there is no way that the later indexes value is equal to index
'''

A = [-10, -5, 0, 3, 7]
B = [0, 2, 5, 8, 17]


# Time complexity : O(n) linear
# Space complexity : O(l)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
        else:
            return None


# Time complexity : O(logn)
def find_fixed_point_binary(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]

    return None


print(find_fixed_point_binary(A))
print(find_fixed_point_binary(B))

# ==========================
"""
Define a bitonic sequence as a sequence of integers such that:
    x_1 <= ... <= x_k >= ... >= x_n-1  for some k, 0 <= k < n.
For example:
    1, 2, 3, 4, 5, 4, 3, 2, 1

is a bitonic sequence. Write a program to find the largest element in such a
sequence. In the example above, the program should return "5".
We assume that such a "peak" element exists.
"""

A = [1, 2, 3, 4, 5, 4, 3, 2, 1]  # peak 5
B = [1, 2, 3, 4, 1]  # peak 4
C = [1, 6, 5, 4, 3, 2, 1]  # peak 6


# basically we have a sequence that first is sorted ascending to a peak, then dscends down. now we need to find the the peak
# in most efficient way *** both elements to right and left of peak are smaller than it

def find_highest_number(A):
    low = 0
    high = len(A) - 1

    # Require at least 3 elements for a bitonic sequence.
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float("inf")  # this is when we reached first element
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")  # this is when we reached last element

        # if left of mid is smaller and right is bigger, it means peak is after middle point
        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        # if left of mid is bigger and right is smaller, it means peak is before the middle point
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        #  if both elements to right and left of mid are smaller than it, it means we found the peak
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
        else:
            return None


print(find_highest_number(A))
print(find_highest_number(B))
print(find_highest_number(C))
5

# =========================
"""
Write a function that takes a non-negative integer and returns
the largest integer whose square is less than or equal to
the integer given.
Example:
    Assume input is integer 300.
    Then the expected output of the function should be
    17, since 17^2 = 289 < 300. Note that 18^2 = 324 > 300,
    so the number 17 is the correct response.


low point = 1
high point = k
"""

k = 300


def integer_square_root(k):
    low = 0
    high = k
    #   high = k//2

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        elif mid_squared > k:
            high = mid - 1

    return low - 1


print(integer_square_root(15))

























