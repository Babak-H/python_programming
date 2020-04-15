# *****Soring Algorithms******

# Bubble Sort
def bubbleSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    # we dont have the last item here, because there is no number after it and it will be compared with previous items
    for i in range(0, len(arr)-1):
        # here we remove the last i-th elements of the list, because they have been sorted in the previous iteration
        # in first iteration i=0 so we will compare all values.
        for j in range(0, len(arr)-1-i):
            # compare each two elements of the list,
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

A = [3,2,4,1]
print(bubbleSort(A))

# =============================
# Selection Sort
def selection_sort(arr):
    # loop through all elements of list (except last one)
    for i in range(0, len(arr)-1):
        # set current index as min
        minIndex = i
        # loop though all elements after arr[i]
        for j in range(i+1, len(arr)):
            # if an element is smaller the set it to be minIndex
            if arr[j] < arr[minIndex]:
                minIndex = j
            # if current element isn't min, then swap it with smallest value
            if minIndex != i:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

print(selection_sort(A))

# =============================          
# Insertion Sort
def insertion_sort(arr):
    # go from first number to last one in the list:
    for i in range(1, len(arr)):
        # then compare the i value (j+1) with each previous number till first one
        for j in range(i-1, 0, -1):
            # if previous number is bigger, then swap it, repeat this check/swap prcoess for all numbers before i
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break

'''
A[j], A[j+1] = A[j+1], A[j] for each swap operation in python behind the scene we have : 
temp = x
x = y
y = x
so for each swap we have 3 operations, and if smallest number is at end of list, for each swap it will have all this 3 
operations, so instead we can improve our insertion sort to method below :
'''

def inserstion_sort_optimized(arr):
    # go from first number to last one in the list
    for i in range(1, len(A)):
        # save value of i in a variable curNum
        curNum = A[i]
        # then compare the curNum with each previous number til first one
        for j in range(i-1, 0, -1):
            if A[j] > curNum:
                #  for each value that is bigger than curNum, we basically move it one index further
                A[j+1] = A[j]
            else:
                # if a number isn't bigger than curNum (A[i]) will will keep A[i] there and break off the loop
                A[j+1] = curNum
                break
    
    return A

# =============================
# Merge Sort
# this first function is just a interface to call the soorting
import sys

def merge_sort(arr):
    merge_sort2(arr, 0, len(arr)-1)

'''
this second function will divide the list into smaller lists recursively until each list is only 1 element.
so the first part merge_sort2(A, first, middle) will go on until it reachs one element,then going back it will call merge_sort2(A, middle+1, last)
to divide each left part to smaller parts then it will call merge(), sort itself
then we go one level back (when the sublist had two elements) again it will call merge() and sort the bigger sublist,....
until at end when both left and right side are sorted we can do the final merge sort by calling merge() 
'''

def merge_sort2(arr, first, last):
    if first < last:
        middle = (first + last) // 2
        # until we havent finished with this recursive method, it wont read further lines
        merge_sort2(arr, first, middle)
        merge_sort2(arr, middle+1, last)
        merge(arr, first, middle, last)


# here we have two sub lists from arr and we will sort them (sort an smaller part of arr)
def merge(arr, first, middle, last):
    L = arr[first:middle+1]
    R = A[middle+1:last+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


A = [5,9,1,2,4,8,6,3,7]
merge_sort(A)
print(A) 

# =============================
# Quick Sort
"""
quick sort is recursive (until we reach were each sublist is one element)
it is a divide and conquer algorithm
very effective for large datasets
wost case is O(n^2) and averge case is O(nlogn)
performance depends alot on pivot selection
"""

# the interface function that calls the recursive function
def quick_sort(arr):
    quick_sort2(arr, 0, len(arr)-1)


def quick_sort2(arr, low, high):
    # until the sublist has more than 1 value, continue sorting sublists and calling the recursive 
    #fuction to make sublists smaller
    if low < high:
        # find the pivot point in list
        p = partition(arr, low, high)
        # quick sort on left part of pivot
        quick_sort2(arr, low, p-1)
        # quick sort on right part of pivot
        quick_sort2(arr, p+1, high)


def partition(arr, low, high):
    # get pivot index and its value
    pivotIndex = get_pivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    # put pivot point at start of the list (swap it with low index, which will be one next to it)
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    # set low index as border
    border = low

    # loop though all elements after pivot (including high)
    for i in range(low, high+1):
    # if there is a number smaller than the pivot, swap it with current border value and increase range of border with one point
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    # at the end move pivot point (now with low index) after all border elements (which are smaller than pivot value)
    arr[low], arr[border] = arr[border], arr[low]
    # then return the pivot point
    return border


# find pivot point as middle point of start, middle, high of unsorted list and returns it
def get_pivot(A, low, high):
    mid = (high + low) // 2
    s = sorted([A[low], A[mid], A[high]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    else:
        return high


A = [12, 14, 66, 5, 0, 9]
quick_sort(A)
print(A)

